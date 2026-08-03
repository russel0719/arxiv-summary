#!/usr/bin/env python3
"""사내 웹(arxiv-web)용 manifest_internal.json 생성.

공개 build_manifest.py와 달리 (1) full daily 리포트(실무 관련성 포함)를 인덱싱하고
(2) weekly match 리포트 목록을 함께 담는다. 정적 SPA(index.html)가 이 파일을 읽는다.

경로는 웹 루트(ARXIV_WEB_ROOT, 기본 ~/workspace/.meta/arxiv-web) 기준 상대경로.
weekly/ 는 ../paper-match 심링크를 가리킨다. 외부 의존성 없음(표준 라이브러리만).
"""

import json
import os
import re
from collections import Counter
from pathlib import Path

WEB_ROOT = Path(
    os.environ.get("ARXIV_WEB_ROOT", Path.home() / "workspace/.meta/arxiv-web")
)
DAILY_DIR = WEB_ROOT / "daily"
WEEKLY_DIR = WEB_ROOT / "weekly"
OUT_FILE = WEB_ROOT / "manifest_internal.json"

DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
WEEK_NEW_RE = re.compile(r"(\d{4})-(\d{2})-w(\d+)")  # 2026-07-w3
WEEK_OLD_RE = re.compile(r"(\d{4})-W(\d{2})")  # 구형 2026-W30 (호환)
HEAD_RE = re.compile(r"^###\s+\[(.+?)\]\((.+?)\)\s*$")
TAG_RE = re.compile(r"^\s*-?\s*\*\*(?:태그|키워드)\*\*\s*[:：]\s*(.+?)\s*$")


def week_label(stem: str) -> str:
    m = WEEK_NEW_RE.search(stem)
    if m:
        return f"{m.group(1)}년 {int(m.group(2))}월 {m.group(3)}째주"
    m = WEEK_OLD_RE.search(stem)
    if m:
        return f"{m.group(1)}-W{m.group(2)}"
    return stem


def norm_tag(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[\s_/]+", "-", s)
    s = re.sub(r"[^\w\-]", "", s, flags=re.UNICODE)
    return re.sub(r"-+", "-", s).strip("-")


def daily_date(md: Path) -> str:
    parts = md.relative_to(DAILY_DIR).parts  # (YYYY, MM, report_DD.md)
    if len(parts) >= 3 and md.stem.startswith("report_"):
        return f"{parts[0]}-{parts[1]}-{md.stem.split('_')[-1]}"
    m = DATE_RE.search(md.stem)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else ""


def first_title(md: Path) -> str:
    for line in md.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def parse_papers(md: Path, date: str, relpath: str) -> list:
    lines = md.read_text(encoding="utf-8", errors="ignore").splitlines()
    papers, cur = [], None
    for line in lines:
        h = HEAD_RE.match(line)
        if h:
            if cur:
                papers.append(cur)
            cur = {
                "title": h.group(1).strip(),
                "url": h.group(2).strip(),
                "date": date,
                "report": relpath,
                "tags": [],
            }
            continue
        if cur is not None:
            t = TAG_RE.match(line)
            if t and not cur["tags"]:
                cur["tags"] = [
                    n for n in (norm_tag(x) for x in t.group(1).split(",")) if n
                ]
    if cur:
        papers.append(cur)
    return papers


def main() -> None:
    reports, papers = [], []
    if DAILY_DIR.is_dir():
        for md in DAILY_DIR.rglob("*.md"):
            date = daily_date(md)
            rel = md.relative_to(WEB_ROOT).as_posix()
            reports.append(
                {"path": rel, "date": date, "title": first_title(md) or date}
            )
            papers.extend(parse_papers(md, date, rel))
    reports.sort(key=lambda e: (e["date"], e["path"]), reverse=True)
    papers.sort(key=lambda e: e["date"], reverse=True)
    counts = Counter(t for p in papers for t in p["tags"])
    tags = [
        {"tag": t, "count": c}
        for t, c in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    ]

    weekly = []
    if WEEKLY_DIR.exists():
        for md in sorted(WEEKLY_DIR.glob("weekly_match_*.md"), reverse=True):
            weekly.append(
                {
                    "path": "weekly/" + md.name,
                    "week": week_label(md.stem),
                    "title": first_title(md) or md.stem,
                }
            )

    OUT_FILE.write_text(
        json.dumps(
            {
                "daily": {"reports": reports, "papers": papers, "tags": tags},
                "weekly": weekly,
            },
            ensure_ascii=False,
            indent=1,
        )
    )
    print(
        f"internal: {len(reports)} daily reports, {len(papers)} papers, "
        f"{len(tags)} tags, {len(weekly)} weekly -> {OUT_FILE}"
    )


if __name__ == "__main__":
    main()

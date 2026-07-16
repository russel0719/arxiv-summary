#!/usr/bin/env python3
"""reports/ 아래 모든 .md를 스캔해 사이트용 manifest.json을 생성한다.

정적 GitHub Pages에는 디렉터리 목록 API가 없으므로, 클라이언트(index.html)가
읽을 인덱스를 미리 파일로 만들어 둔다. 세 가지를 담는다:
  - reports: 날짜별 리포트 목록 (리포트 브라우즈용)
  - papers : 논문별 항목 {제목, arxiv url, 날짜, 소속 리포트, 태그} (태그/검색용)
  - tags   : 태그별 등장 횟수 (태그 클라우드용)

신규 포맷(### [제목](url) ... **태그**/**키워드**)만 논문 단위로 파싱한다.
구형(daily_reports) 리포트는 reports 목록에만 포함된다.

외부 의존성 없음 (표준 라이브러리만 사용).
"""

import json
import re
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPORTS_DIR = BASE_DIR / "reports"
OUT_FILE = BASE_DIR / "manifest.json"

DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
HEAD_RE = re.compile(r"^###\s+\[(.+?)\]\((.+?)\)\s*$")
TAG_RE = re.compile(r"^\*\*(?:태그|키워드)\*\*\s*[:：]\s*(.+?)\s*$")


def date_of(md: Path) -> str:
    name = md.stem
    m = DATE_RE.search(name)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    parts = md.relative_to(REPORTS_DIR).parts
    if len(parts) >= 3 and name.startswith("report_"):
        return f"{parts[0]}-{parts[1]}-{name.split('_')[-1]}"
    return ""


def norm_tag(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[\s_/]+", "-", s)
    s = re.sub(r"[^\w\-]", "", s, flags=re.UNICODE)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def parse_papers(md: Path, date: str) -> list:
    """### [제목](url) 블록에서 논문 단위 항목을 뽑는다."""
    rel = md.relative_to(BASE_DIR).as_posix()
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
                "report": rel,
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
    for md in REPORTS_DIR.rglob("*.md"):
        date = date_of(md)
        name = md.stem
        cat = "AI" if name.startswith("AI_") else "CV"
        title = ""
        for line in md.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        reports.append(
            {
                "path": md.relative_to(BASE_DIR).as_posix(),
                "date": date,
                "title": title or date,
                "cat": cat,
            }
        )
        papers.extend(parse_papers(md, date))

    reports.sort(key=lambda e: (e["date"], e["path"]), reverse=True)
    papers.sort(key=lambda e: e["date"], reverse=True)

    counts = Counter(t for p in papers for t in p["tags"])
    tags = [
        {"tag": t, "count": c}
        for t, c in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    ]

    OUT_FILE.write_text(
        json.dumps(
            {"reports": reports, "papers": papers, "tags": tags},
            ensure_ascii=False,
            indent=1,
        )
    )
    print(
        f"{len(reports)} reports, {len(papers)} papers, {len(tags)} tags -> {OUT_FILE}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""arXiv cs.CV 신규 공개(announcement) 논문 수집 스크립트.

- arXiv RSS 공개 피드에서 최근 공개된 cs.CV 논문(announce_type: new, cross)을 가져온다.
  (제출일 기준이 아니라 '공개일' 기준이라, 주말 직후에도 그날 공개분을 놓치지 않는다.)
- seen_ids.txt로 이미 처리한 논문을 중복 제거한다.
- 결과를 today_papers.json으로 저장한다 (Claude Code가 읽을 입력 파일).
- 같은 내용을 raw/YYYY/MM/DD.json 에 일별로 보존한다 (주간 스크리닝·백로그 재심사 입력, gitignore).
- EXTRA_CATEGORIES(cs.LG 등)는 **raw 아카이브에만** 저장한다 — 일일 다이제스트 입력(today_papers.json)은
  cs.CV 그대로 두고, 프로젝트 병목 기준의 주간 스크리닝(utils/arxiv-internal)만 넓힌다.
  cs.CV 로 cross-list 된 논문은 cs.CV 피드에 이미 있으므로 제외한다.

외부 의존성 없음 (표준 라이브러리만 사용).
"""

import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SEEN_FILE = BASE_DIR / "seen_ids.txt"
SEEN_EXTRA_FILE = BASE_DIR / "seen_extra.txt"   # 추가 카테고리 전용 (cs.CV 중복 제거와 분리)
OUT_FILE = BASE_DIR / "today_papers.json"
RAW_DIR = BASE_DIR / "raw"

# 수집 대상 카테고리 (일일 다이제스트 입력 — 각 카테고리별 RSS 피드)
CATEGORIES = ["cs.CV"]
# raw 아카이브 전용 추가 카테고리 (calibration·conformal·continual learning 은 cs.LG/stat.ML 이 주류)
EXTRA_CATEGORIES = ["cs.LG", "stat.ML", "eess.IV"]
# 수집할 공개 유형: new(순수 신규 제출), cross(타 분야에서 cs.CV로 cross-list)
WANT_TYPES = {"new", "cross"}

DC = "{http://purl.org/dc/elements/1.1/}"
ARX = "{http://arxiv.org/schemas/atom}"


def load_seen(path: Path = SEEN_FILE) -> set:
    if path.exists():
        return set(path.read_text().split())
    return set()


def save_seen(seen: set, path: Path = SEEN_FILE) -> None:
    # 파일이 무한히 커지지 않도록 최근 5000개만 유지
    ids = sorted(seen)[-5000:]
    path.write_text("\n".join(ids))


def raw_path(suffix: str = "") -> Path:
    """raw/YYYY/MM/DD[suffix].json — 날짜는 KST 실행일 (run_digest.sh 가 TZ 를 고정한다)."""
    import datetime as _dt
    d = _dt.date.today()
    p = RAW_DIR / f"{d:%Y}" / f"{d:%m}" / f"{d:%d}{suffix}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


# RSS 호스트 — 2026-09-09 부터 legacy(export.arxiv.org)가 공개일 pubDate 만 있는 빈 채널을 돌려준다.
# 새 호스트(rss.arxiv.org)를 먼저 읽고, 항목이 0이면 legacy 로 한 번 더 시도한다.
FEED_HOSTS = ["https://rss.arxiv.org/rss/{cat}", "http://export.arxiv.org/rss/{cat}"]


def fetch_category(cat: str) -> list:
    last_err: Exception | None = None
    for tmpl in FEED_HOSTS:
        try:
            entries, n_items = _fetch_feed(tmpl.format(cat=cat))
        except Exception as e:  # 네트워크·파싱 실패 → 다음 호스트
            last_err = e
            continue
        if n_items > 0:
            return entries
        print(f"{cat}: {tmpl.format(cat=cat)} 항목 0 → 다음 호스트")
    if last_err is not None:
        raise last_err
    return []


def _fetch_feed(url: str) -> tuple[list, int]:
    """피드 하나를 읽어 (new/cross 항목, 전체 item 수)를 돌려준다."""
    req = urllib.request.Request(url, headers={"User-Agent": "arxiv-digest/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    root = ET.fromstring(data)
    channel = root.find("channel")
    if channel is None:
        return [], 0
    pub = channel.findtext("pubDate", "")  # 공개(announcement) 일자
    items = channel.findall("item")

    entries = []
    for it in items:
        if it.findtext(f"{ARX}announce_type", "") not in WANT_TYPES:
            continue
        arxiv_id = it.findtext("link", "").rsplit("/", 1)[-1]
        # description 형식: "arXiv:ID Announce Type: new  Abstract: <초록>"
        desc = it.findtext("description", "")
        m = re.search(r"Abstract:\s*(.*)", desc, re.DOTALL)
        abstract = _clean(m.group(1)) if m else _clean(desc)
        creator = it.findtext(f"{DC}creator", "")
        entries.append(
            {
                "id": arxiv_id,
                "title": _clean(it.findtext("title", "")),
                "abstract": abstract,
                "authors": [a.strip() for a in creator.split(",") if a.strip()],
                "published": pub,
                "announce_type": it.findtext(f"{ARX}announce_type", ""),
                "categories": [c.text for c in it.findall("category") if c.text],
                "url": f"https://arxiv.org/abs/{arxiv_id}",
            }
        )
    return entries, len(items)


def main() -> int:
    seen = load_seen()

    papers = []
    for cat in CATEGORIES:
        papers.extend(fetch_category(cat))
        time.sleep(3)  # arXiv API 예의상 딜레이

    fresh = []
    dedup = set()
    for p in papers:
        base_id = p["id"].split("v")[0]
        if base_id in seen or base_id in dedup:
            continue
        dedup.add(base_id)
        fresh.append(p)

    OUT_FILE.write_text(json.dumps(fresh, ensure_ascii=False, indent=2))
    if fresh:
        raw_path().write_text(json.dumps(fresh, ensure_ascii=False, indent=2))
    seen.update(dedup)
    save_seen(seen)

    # 추가 카테고리 → raw 아카이브만. cs.CV 에 걸린 것(cross-list)은 위 피드에 있으니 제외.
    try:
        fetch_extra(seen | dedup)
    except Exception as e:  # 부가 기능 — 실패해도 일일 다이제스트는 진행
        print(f"extra categories skipped: {e}")

    print(f"{len(fresh)} new papers saved to {OUT_FILE}")
    return 0 if fresh else 1  # 신규 논문 없으면 exit 1 → 셸에서 Claude 호출 스킵


def fetch_extra(seen_cv: set) -> None:
    if not EXTRA_CATEGORIES:
        return
    seen_extra = load_seen(SEEN_EXTRA_FILE)
    extra, dedup = [], set()
    for cat in EXTRA_CATEGORIES:
        time.sleep(3)
        for p in fetch_category(cat):
            base_id = p["id"].split("v")[0]
            if base_id in seen_cv or base_id in seen_extra or base_id in dedup:
                continue
            if "cs.CV" in p["categories"]:
                continue
            dedup.add(base_id)
            extra.append(p)
    if extra:
        raw_path("_extra").write_text(json.dumps(extra, ensure_ascii=False, indent=2))
    seen_extra.update(dedup)
    save_seen(seen_extra, SEEN_EXTRA_FILE)
    print(f"{len(extra)} extra-category papers archived ({', '.join(EXTRA_CATEGORIES)})")


if __name__ == "__main__":
    sys.exit(main())

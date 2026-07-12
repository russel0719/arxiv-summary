#!/usr/bin/env python3
"""arXiv cs.CV 신규 논문 수집 스크립트.

- arXiv API에서 최근 제출된 cs.CV 논문을 가져온다.
- seen_ids.txt로 이미 처리한 논문을 중복 제거한다.
- 결과를 today_papers.json으로 저장한다 (Claude Code가 읽을 입력 파일).

외부 의존성 없음 (표준 라이브러리만 사용).
"""

import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SEEN_FILE = BASE_DIR / "seen_ids.txt"
OUT_FILE = BASE_DIR / "today_papers.json"

# 수집 대상 카테고리 (필요시 cs.LG, cs.AI 등 추가)
CATEGORIES = ["cs.CV"]
MAX_RESULTS = 300          # 하루 cs.CV 신규 제출은 보통 100~250편
LOOKBACK_HOURS = 36        # 최근 36시간 내 제출분만 (주말 건너뛴 월요일은 아래에서 확장)

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def load_seen() -> set:
    if SEEN_FILE.exists():
        return set(SEEN_FILE.read_text().split())
    return set()


def save_seen(seen: set) -> None:
    # 파일이 무한히 커지지 않도록 최근 5000개만 유지
    ids = sorted(seen)[-5000:]
    SEEN_FILE.write_text("\n".join(ids))


def fetch_category(cat: str) -> list:
    url = (
        "http://export.arxiv.org/api/query?"
        f"search_query=cat:{cat}"
        f"&sortBy=submittedDate&sortOrder=descending&max_results={MAX_RESULTS}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "arxiv-digest/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    root = ET.fromstring(data)
    entries = []
    for e in root.findall("atom:entry", ATOM_NS):
        arxiv_id = e.findtext("atom:id", "", ATOM_NS).rsplit("/", 1)[-1]
        published = e.findtext("atom:published", "", ATOM_NS)
        entries.append(
            {
                "id": arxiv_id,
                "title": re.sub(r"\s+", " ", e.findtext("atom:title", "", ATOM_NS)).strip(),
                "abstract": re.sub(r"\s+", " ", e.findtext("atom:summary", "", ATOM_NS)).strip(),
                "authors": [
                    a.findtext("atom:name", "", ATOM_NS)
                    for a in e.findall("atom:author", ATOM_NS)
                ],
                "published": published,
                "categories": [
                    c.get("term") for c in e.findall("atom:category", ATOM_NS)
                ],
                "url": f"https://arxiv.org/abs/{arxiv_id}",
            }
        )
    return entries


def main() -> int:
    now = datetime.now(timezone.utc)
    lookback = LOOKBACK_HOURS
    # 월요일(KST 기준)에는 주말 제출분까지 포함
    if now.astimezone(timezone(timedelta(hours=9))).weekday() == 0:
        lookback = 84

    cutoff = now - timedelta(hours=lookback)
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
        try:
            pub = datetime.fromisoformat(p["published"].replace("Z", "+00:00"))
        except ValueError:
            continue
        if pub < cutoff:
            continue
        dedup.add(base_id)
        fresh.append(p)

    OUT_FILE.write_text(json.dumps(fresh, ensure_ascii=False, indent=2))
    seen.update(dedup)
    save_seen(seen)

    print(f"{len(fresh)} new papers saved to {OUT_FILE}")
    return 0 if fresh else 1  # 신규 논문 없으면 exit 1 → 셸에서 Claude 호출 스킵


if __name__ == "__main__":
    sys.exit(main())

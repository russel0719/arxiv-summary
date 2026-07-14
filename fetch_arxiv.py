#!/usr/bin/env python3
"""arXiv cs.CV 신규 공개(announcement) 논문 수집 스크립트.

- arXiv RSS 공개 피드에서 최근 공개된 cs.CV 논문(announce_type: new, cross)을 가져온다.
  (제출일 기준이 아니라 '공개일' 기준이라, 주말 직후에도 그날 공개분을 놓치지 않는다.)
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
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SEEN_FILE = BASE_DIR / "seen_ids.txt"
OUT_FILE = BASE_DIR / "today_papers.json"

# 수집 대상 카테고리 (필요시 cs.LG, cs.AI 등 추가 — 각 카테고리별 RSS 피드)
CATEGORIES = ["cs.CV"]
# 수집할 공개 유형: new(순수 신규 제출), cross(타 분야에서 cs.CV로 cross-list)
WANT_TYPES = {"new", "cross"}

DC = "{http://purl.org/dc/elements/1.1/}"
ARX = "{http://arxiv.org/schemas/atom}"


def load_seen() -> set:
    if SEEN_FILE.exists():
        return set(SEEN_FILE.read_text().split())
    return set()


def save_seen(seen: set) -> None:
    # 파일이 무한히 커지지 않도록 최근 5000개만 유지
    ids = sorted(seen)[-5000:]
    SEEN_FILE.write_text("\n".join(ids))


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def fetch_category(cat: str) -> list:
    url = f"http://export.arxiv.org/rss/{cat}"
    req = urllib.request.Request(url, headers={"User-Agent": "arxiv-digest/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    root = ET.fromstring(data)
    channel = root.find("channel")
    if channel is None:
        return []
    pub = channel.findtext("pubDate", "")  # 공개(announcement) 일자

    entries = []
    for it in channel.findall("item"):
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
    return entries


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
    seen.update(dedup)
    save_seen(seen)

    print(f"{len(fresh)} new papers saved to {OUT_FILE}")
    return 0 if fresh else 1  # 신규 논문 없으면 exit 1 → 셸에서 Claude 호출 스킵


if __name__ == "__main__":
    sys.exit(main())

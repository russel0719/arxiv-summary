#!/usr/bin/env python3
"""reports/ 아래 모든 .md를 스캔해 사이트용 manifest.json을 생성한다.

정적 GitHub Pages에는 디렉터리 목록 API가 없으므로, 클라이언트(index.html)가
읽을 리포트 인덱스를 미리 파일로 만들어 둔다. 신·구 파일명 규칙을 모두 처리한다:
  - 신규: reports/YYYY/MM/report_DD.md
  - 구형: reports/YYYY/MM/{CV,AI}_Daily_Trend_YYYY-MM-DD.md

외부 의존성 없음 (표준 라이브러리만 사용).
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPORTS_DIR = BASE_DIR / "reports"
OUT_FILE = BASE_DIR / "manifest.json"

DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def entry_for(md: Path) -> dict:
    rel = md.relative_to(BASE_DIR).as_posix()
    parts = md.relative_to(REPORTS_DIR).parts  # (YYYY, MM, filename)
    name = md.stem

    # 날짜: 파일명의 YYYY-MM-DD, 없으면 경로(YYYY/MM) + report_DD
    m = DATE_RE.search(name)
    if m:
        date = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    elif len(parts) >= 3 and name.startswith("report_"):
        date = f"{parts[0]}-{parts[1]}-{name.split('_')[-1]}"
    else:
        date = ""

    # 카테고리 태그
    if name.startswith("AI_"):
        cat = "AI"
    else:
        cat = "CV"

    # 제목: 첫 '# ' 헤딩
    title = ""
    for line in md.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break

    return {"path": rel, "date": date, "title": title or date, "cat": cat}


def main() -> None:
    entries = [entry_for(md) for md in REPORTS_DIR.rglob("*.md")]
    entries.sort(key=lambda e: (e["date"], e["path"]), reverse=True)
    OUT_FILE.write_text(json.dumps(entries, ensure_ascii=False, indent=1))
    print(f"{len(entries)} reports -> {OUT_FILE}")


if __name__ == "__main__":
    main()

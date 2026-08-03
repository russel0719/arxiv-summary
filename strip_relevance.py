#!/usr/bin/env python3
"""공개 배포용: daily digest 리포트에서 '실무 관련성' 줄만 제거한다.

'실무 관련성'은 내 프로젝트를 겨냥한 항목이라 공개 GitHub Pages에는 싣지 않는다.
사내 웹은 원본(실무 관련성 포함)을 그대로 쓴다. 이 스크립트는 결정론적으로
해당 한 줄만 지우고 잉여 빈 줄을 정리한다(불릿 `- **실무 관련성**:` / 문단 `**실무 관련성**:` 모두).

사용:
  strip_relevance.py <file.md> [<file.md> ...]   # 각 파일 in-place 스트립
  strip_relevance.py --stdout <file.md>          # 표준출력으로 (in-place 아님)
"""

import re
import sys

REL_RE = re.compile(r"^\s*(?:[-*]\s+)?\*\*\s*실무\s*관련성\s*\*\*")


def strip_text(text: str) -> str:
    lines = text.splitlines()
    kept = [ln for ln in lines if not REL_RE.match(ln)]
    if len(kept) == len(lines):
        return text  # 실무 관련성 줄 없음 → 원본 그대로 (no-op, 공백 등 불변)
    out = "\n".join(kept)
    out = re.sub(r"\n{3,}", "\n\n", out)  # 실무 관련성 제거로 생긴 잉여 빈 줄만 정리
    if text.endswith("\n") and not out.endswith("\n"):
        out += "\n"
    return out


def main(argv: list) -> int:
    if not argv:
        print(__doc__)
        return 2
    to_stdout = argv[0] == "--stdout"
    files = argv[1:] if to_stdout else argv
    for path in files:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        stripped = strip_text(text)
        if to_stdout:
            sys.stdout.write(stripped)
        elif stripped != text:  # 변경된 파일만 기록 (무변경 파일은 건드리지 않음)
            with open(path, "w", encoding="utf-8") as f:
                f.write(stripped)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

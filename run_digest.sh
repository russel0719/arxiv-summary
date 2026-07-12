#!/usr/bin/env bash
# arXiv 일일 요약 파이프라인
# cron에서 실행: 1) 신규 논문 수집 → 2) claude -p로 선별·요약 → 3) git push
set -uo pipefail

# 모든 날짜/시각을 KST로 통일 (fetch_arxiv.py는 내부적으로 UTC를 쓰므로 영향 없음)
export TZ="Asia/Seoul"
DATE="$(date +%F)"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

mkdir -p digests logs
LOG="logs/$DATE.log"

# claude가 PATH에 없을 수 있으므로 cron 환경 대비 (npm global 경로 등 환경에 맞게 수정)
export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:/usr/local/bin:$PATH"

echo "[$(date '+%F %T')] fetching arxiv..." >> "$LOG"

if ! uv run python fetch_arxiv.py >> "$LOG" 2>&1; then
  echo "[$(date '+%F %T')] no new papers (or fetch failed). skip." >> "$LOG"
  exit 0
fi

echo "[$(date '+%F %T')] running claude..." >> "$LOG"

claude -p "CLAUDE.md의 요약 작업 규칙에 따라 today_papers.json을 처리하고 \
digests/$DATE.md 파일을 생성해줘." \
  --allowedTools "Read,Write,WebFetch,WebSearch,Bash(date *)" \
  --max-turns 40 \
  >> "$LOG" 2>&1

if [ -f "digests/$DATE.md" ]; then
  echo "[$(date '+%F %T')] done: digests/$DATE.md" >> "$LOG"

  # 테스트 시 DIGEST_SKIP_PUSH=1 로 원격 push 생략 가능
  if [ "${DIGEST_SKIP_PUSH:-0}" = "1" ]; then
    echo "[$(date '+%F %T')] DIGEST_SKIP_PUSH=1 → skip git push" >> "$LOG"
  else
    # 결과물을 원격 repo에 반영 (원격 push 인증은 머신에 미리 설정되어 있어야 함)
    git -C "$DIR" add "digests/$DATE.md"
    if ! git -C "$DIR" diff --cached --quiet; then
      echo "[$(date '+%F %T')] pushing to remote..." >> "$LOG"
      git -C "$DIR" commit -m "auto: update digest $DATE" >> "$LOG" 2>&1
      git -C "$DIR" pull --rebase --autostash >> "$LOG" 2>&1
      git -C "$DIR" push >> "$LOG" 2>&1
    fi
  fi
else
  echo "[$(date '+%F %T')] WARNING: digest file not created. check log." >> "$LOG"
fi

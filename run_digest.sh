#!/usr/bin/env bash
# arXiv 일일 요약 파이프라인
# cron에서 실행: 1) 신규 논문 수집 → 2) claude -p로 선별·요약 → 3) git push
set -uo pipefail

# 모든 날짜/시각을 KST로 통일 (fetch_arxiv.py는 내부적으로 UTC를 쓰므로 영향 없음)
export TZ="Asia/Seoul"
DATE="$(date +%F)"                                  # YYYY-MM-DD
YEAR="$(date +%Y)"; MONTH="$(date +%m)"; DAY="$(date +%d)"
REPORT="reports/$YEAR/$MONTH/report_$DAY.md"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

mkdir -p "reports/$YEAR/$MONTH" logs
LOG="logs/$DATE.log"

# claude가 PATH에 없을 수 있으므로 cron 환경 대비 (npm global 경로 등 환경에 맞게 수정)
export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:/usr/local/bin:$PATH"

# cron 무인 실행용 장수명 OAuth 토큰(선택, 권장). 있으면 인터랙티브 세션 자격증명 대신 사용해
# 새벽 refresh 실패("OAuth session expired and could not be refreshed")를 방지한다.
# 최초 1회: `claude setup-token` 출력 토큰을 $TOKEN_FILE 에 저장 후 chmod 600.
TOKEN_FILE="${CLAUDE_OAUTH_TOKEN_FILE:-$HOME/.claude/arxiv_digest.token}"
if [ -z "${CLAUDE_CODE_OAUTH_TOKEN:-}" ] && [ -f "$TOKEN_FILE" ]; then
  export CLAUDE_CODE_OAUTH_TOKEN="$(tr -d '[:space:]' < "$TOKEN_FILE")"
fi

echo "[$(date '+%F %T')] fetching arxiv..." >> "$LOG"

if ! uv run python fetch_arxiv.py >> "$LOG" 2>&1; then
  echo "[$(date '+%F %T')] no new papers (or fetch failed). skip." >> "$LOG"
  exit 0
fi

echo "[$(date '+%F %T')] running claude..." >> "$LOG"

# 프롬프트는 prompts/ 에서 관리 (규칙 daily_rules.md + 태스크 daily_digest.md).
# 규칙 뒤에 태스크를 이어붙이고 {{PLACEHOLDER}} 를 런타임 값으로 치환.
PROMPT="$(cat "$DIR/prompts/daily_rules.md" "$DIR/prompts/daily_digest.md")"
PROMPT="${PROMPT//'{{REPORT}}'/$REPORT}"

claude -p "$PROMPT" \
  --allowedTools "Read,Write,WebFetch,WebSearch,Bash(date *)" \
  --max-turns 40 \
  >> "$LOG" 2>&1

if [ -f "$REPORT" ]; then
  echo "[$(date '+%F %T')] done: $REPORT" >> "$LOG"

  # 공개 사이트 manifest 갱신
  uv run python build_manifest.py >> "$LOG" 2>&1 || true

  # 테스트 시 DIGEST_SKIP_PUSH=1 로 원격 push 생략 가능
  if [ "${DIGEST_SKIP_PUSH:-0}" = "1" ]; then
    echo "[$(date '+%F %T')] DIGEST_SKIP_PUSH=1 → skip git push" >> "$LOG"
  else
    # 결과물을 원격 repo에 반영.
    # cron 무인 push: 무암호 deploy key가 있으면 SSH로 push (origin은 HTTPS 유지 → gh/수동 git 그대로)
    DEPLOY_KEY="$HOME/.ssh/id_arxiv_digest"
    if [ -f "$DEPLOY_KEY" ]; then
      export GIT_SSH_COMMAND="ssh -i $DEPLOY_KEY -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
      REMOTE="git@github.com:russel0719/arxiv-summary.git"
    else
      REMOTE="origin"
    fi
    # claude가 (settings.local.json 허용으로) 직접 커밋하는 경우까지 대비:
    # 스테이징분이 있으면 커밋(없으면 no-op), 그 뒤 로컬이 앞서면 무조건 push.
    git -C "$DIR" add "$REPORT" manifest.json
    git -C "$DIR" commit -m "auto: update report $DATE" >> "$LOG" 2>&1 || true
    echo "[$(date '+%F %T')] pushing to remote..." >> "$LOG"
    git -C "$DIR" pull --rebase --autostash "$REMOTE" main >> "$LOG" 2>&1
    git -C "$DIR" push "$REMOTE" HEAD:main >> "$LOG" 2>&1
  fi
else
  echo "[$(date '+%F %T')] WARNING: report file not created. check log." >> "$LOG"
fi

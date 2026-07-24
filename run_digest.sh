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

echo "[$(date '+%F %T')] fetching arxiv..." >> "$LOG"

if ! uv run python fetch_arxiv.py >> "$LOG" 2>&1; then
  echo "[$(date '+%F %T')] no new papers (or fetch failed). skip." >> "$LOG"
  exit 0
fi

echo "[$(date '+%F %T')] running claude..." >> "$LOG"

# 실무 관련성 근거로 쓰는 프로젝트 프로파일(선택). 있으면 경로를 프롬프트로 넘긴다.
# (weekly_match.sh 와 동일한 WORKSPACE_ROOT 규칙. 없으면 관심사 프로필만으로 생성.)
WS="${WORKSPACE_ROOT:-$HOME/workspace}"
PROFILES="$WS/.meta/project_profiles.md"
if [ -f "$PROFILES" ]; then
  PROFILE_LINE="실무 관련성은 프로젝트 프로파일($PROFILES)을 함께 읽고 쓰되, 프로젝트를 task·역할로만 지칭하고 내부 모델·제품·repo 이름은 쓰지 마."
else
  PROFILE_LINE=""
fi

# 프롬프트는 prompts/ 에서 관리 (규칙 daily_rules.md + 태스크 daily_digest.md).
# 규칙 뒤에 태스크를 이어붙이고 {{PLACEHOLDER}} 를 런타임 값으로 치환.
PROMPT="$(cat "$DIR/prompts/daily_rules.md" "$DIR/prompts/daily_digest.md")"
PROMPT="${PROMPT//'{{REPORT}}'/$REPORT}"
PROMPT="${PROMPT//'{{PROFILE_LINE}}'/$PROFILE_LINE}"

claude -p "$PROMPT" \
  --allowedTools "Read,Write,WebFetch,WebSearch,Bash(date *)" \
  --max-turns 40 \
  >> "$LOG" 2>&1

if [ -f "$REPORT" ]; then
  echo "[$(date '+%F %T')] done: $REPORT" >> "$LOG"

  # 사이트(index.html)가 읽는 리포트 인덱스 갱신
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

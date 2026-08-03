#!/usr/bin/env bash
# 주간 논문 → 프로젝트 적용 매칭 파이프라인
# cron 주 1회 실행: 그 주 일일 다이제스트(reports/) + 프로젝트 프로파일 →
#   claude -p 로 매칭 → ~/workspace/.meta/paper-match/weekly_match_YYYY-MM-wN.md
# (일일 run_digest.sh 와 같은 headless-claude 패턴. git push 는 하지 않는다.)
set -uo pipefail

export TZ="Asia/Seoul"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

# claude 가 cron PATH 에 없을 수 있으므로 대비 (run_digest.sh 와 동일)
export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:/usr/local/bin:$PATH"

# cron 무인 실행용 장수명 OAuth 토큰(선택, 권장). run_digest.sh 와 동일 규칙.
# 최초 1회: `claude setup-token` 출력 토큰을 $TOKEN_FILE 에 저장 후 chmod 600.
TOKEN_FILE="${CLAUDE_OAUTH_TOKEN_FILE:-$HOME/.claude/arxiv_digest.token}"
if [ -z "${CLAUDE_CODE_OAUTH_TOKEN:-}" ] && [ -f "$TOKEN_FILE" ]; then
  export CLAUDE_CODE_OAUTH_TOKEN="$(tr -d '[:space:]' < "$TOKEN_FILE")"
fi

WS="${WORKSPACE_ROOT:-$HOME/workspace}"
PROFILES="$WS/.meta/project_profiles.md"
OUTDIR="$WS/.meta/paper-match"
# 이번 ISO 주의 월요일 기준으로 주차 산출 (파일명: 2026-07-w3 / 표시: 2026년 7월 3째주)
MON="$(date -d "-$(( $(date +%u) - 1 )) days" +%F)"   # 이번 주 월요일
WY="$(date -d "$MON" +%Y)"; WM="$(date -d "$MON" +%m)"; WD="$(date -d "$MON" +%-d)"
WKN=$(( (WD - 1) / 7 + 1 ))
WEEK_ID="${WY}-${WM}-w${WKN}"                 # 파일명·식별자
WEEK_LABEL="${WY}년 ${WM#0}월 ${WKN}째주"     # 리포트 제목 표시용
OUT="$OUTDIR/weekly_match_${WEEK_ID}.md"

mkdir -p "$OUTDIR" logs
LOG="logs/weekly_$(date +%F).log"

# 지난 7일 일일 다이제스트 수집 (report_DD.md)
REPORTS="$(find reports -name 'report_*.md' -mtime -7 2>/dev/null | sort)"
if [ -z "$REPORTS" ]; then
  echo "[$(date '+%F %T')] 최근 7일 일일 리포트 없음 → skip." >> "$LOG"
  exit 0
fi
if [ ! -f "$PROFILES" ]; then
  echo "[$(date '+%F %T')] 프로파일 없음: $PROFILES → 중단." >> "$LOG"
  exit 1
fi

REPORT_LIST="$(echo "$REPORTS" | sed 's|^|- |')"
echo "[$(date '+%F %T')] $WEEK_LABEL 매칭 시작 ($(echo "$REPORTS" | wc -l)개 리포트)..." >> "$LOG"

# 프롬프트는 prompts/ 에서 관리 (규칙 weekly_rules.md + 태스크 weekly_match.md).
# 규칙 뒤에 태스크를 이어붙이고 {{PLACEHOLDER}} 를 런타임 값으로 치환.
PROMPT="$(cat "$DIR/prompts/weekly_rules.md" "$DIR/prompts/weekly_match.md")"
PROMPT="${PROMPT//'{{WEEK}}'/$WEEK_LABEL}"
PROMPT="${PROMPT//'{{REPORT_LIST}}'/$REPORT_LIST}"
PROMPT="${PROMPT//'{{PROFILES}}'/$PROFILES}"
PROMPT="${PROMPT//'{{OUT}}'/$OUT}"

claude -p "$PROMPT" \
  --allowedTools "Read,Write,WebFetch,WebSearch,Bash(date *)" \
  --max-turns 40 \
  >> "$LOG" 2>&1

if [ -f "$OUT" ]; then
  echo "[$(date '+%F %T')] 완료: $OUT" >> "$LOG"
else
  echo "[$(date '+%F %T')] 경고: 리포트 미생성. 로그 확인." >> "$LOG"
fi

# arXiv Daily CV Digest (Claude Code Pro, API 키 불필요)

매 평일 arXiv cs.CV 신규 논문을 수집하고, Claude Code headless 모드로
유용한 논문만 선별·요약해 마크다운으로 저장한 뒤 git push로 repo에 반영하는 파이프라인.

## 구조

```
arxiv-summary/            # git repo (결과를 push해서 보관)
├── fetch_arxiv.py        # arXiv API에서 신규 논문 수집 (표준 라이브러리만 사용)
├── CLAUDE.md             # 일일·주간 공통 규칙 (claude -p가 루트에서 자동 로드)
├── prompts/              # claude -p 프롬프트 (작업별 규칙 + 태스크 분리 관리)
│   ├── daily_rules.md    # 일일: 관심사 프로필 + 요약 규칙
│   ├── daily_digest.md   # 일일: 태스크 프롬프트 ({{PLACEHOLDER}} 치환)
│   ├── weekly_rules.md   # 주간: 매칭 지침 + 출력 형식
│   └── weekly_match.md   # 주간: 태스크 프롬프트 ({{PLACEHOLDER}} 치환)
├── run_digest.sh         # cron이 호출하는 일일 스크립트 (fetch → claude → git push)
├── weekly_match.sh       # cron이 호출하는 주간 매칭 스크립트 (git push 안 함)
├── seen_ids.txt          # 중복 제거용 (자동 생성, gitignore)
├── today_papers.json     # 당일 수집 결과 (자동 생성, gitignore)
├── reports/              # 최종 산출물: YYYY/MM/report_DD.md (git에 커밋·push)
├── logs/                 # 실행 로그 (gitignore)
└── main.py               # (legacy) Gemini API 기반 파이프라인 — 수동 실행용으로 보존
```

## 설치 (원격 Linux 머신 기준)

1. Claude Code 설치 및 Pro 계정 로그인 (최초 1회, 인터랙티브):

    ```bash
    npm install -g @anthropic-ai/claude-code
    claude          # 브라우저/코드로 Pro 계정 로그인
    ```

    로그인 후에는 `claude -p`가 구독 계정으로 실행되며 API 키가 필요 없다.

2. repo를 clone하고 스크립트에 실행 권한 부여:

    ```bash
    git clone <this-repo> ~/workspace/utils/arxiv-summary
    cd ~/workspace/utils/arxiv-summary
    chmod +x run_digest.sh
    ```

    결과 digest는 `git push`로 원격 repo에 반영되므로, 이 머신에서 push가
    가능하도록 git remote 인증(SSH 키 또는 토큰)을 미리 설정해 둔다.

3. 수동 테스트 (원격 push 없이):

    ```bash
    DIGEST_SKIP_PUSH=1 ./run_digest.sh
    cat reports/$(TZ=Asia/Seoul date '+%Y/%m/report_%d').md
    ```

    같은 날 다시 테스트하려면 중복 제거 상태를 초기화한다:

    ```bash
    rm -f seen_ids.txt today_papers.json
    ```

4. cron 등록 (`crontab -e`) — 한국시간 기준 화~토 새벽 1시에 실행되도록 예시:
    ```
    0 1 * * 2-6 /home/jmkang/workspace/utils/arxiv-summary/run_digest.sh
    ```
    `run_digest.sh`가 내부에서 `TZ=Asia/Seoul`을 고정하므로 서버 타임존과
    무관하게 digest 날짜는 항상 KST 기준으로 저장된다. 단, cron 스케줄 자체는
    서버 로컬 시각으로 해석되므로 서버가 UTC라면 `0 16 * * 1-5`를 사용한다
    (01:00 KST = 16:00 UTC, 화~토 새벽 1시 KST = 월~금 16:00 UTC).

## 운영 팁

- **arXiv 발표 시간**: 신규 논문은 미국 동부 기준 일~목 저녁에 공개되므로
  KST 오전 10시면 당일 발표분이 안정적으로 잡힌다. `fetch_arxiv.py`는
  36시간 lookback + `seen_ids.txt` 중복 제거로 빠짐/중복을 방지하고,
  월요일에는 lookback을 84시간으로 늘려 주말 공백을 커버한다.
- **관심사 조정**: `prompts/daily_rules.md`의 프로필만 수정하면 선별 기준이 바뀐다.
- **카테고리 추가**: `fetch_arxiv.py`의 `CATEGORIES`에 `cs.LG`, `cs.AI` 등 추가.
- **권한**: `--allowedTools "Read,Write,WebFetch,WebSearch,Bash(date *)"`로
  최소 권한만 부여했다. Claude가 임의 셸 명령을 실행할 수 없다.
- **사용량**: Pro 구독 사용량 한도를 공유하므로, 하루 1회 요약 정도는
  일반적으로 문제없지만 낮 업무 시간과 겹치지 않게 스케줄하면 좋다.
- **PATH 문제**: cron은 로그인 셸 환경이 아니므로 `claude`/`uv` 경로가 다르면
  `run_digest.sh` 상단의 PATH를 본인 환경(`which claude`, `which uv`)에 맞게 수정.

## 대안

- **Claude Code Desktop 예약 작업(Routines → Local)**: GUI로 동일한 작업을
  스케줄 가능. 단, 앱이 켜져 있고 머신이 깨어 있어야 실행됨.
- **GitHub Actions + OAuth 토큰**: 상시 머신이 없다면 `claude setup-token`으로
  만든 Pro/Max OAuth 토큰(`CLAUDE_CODE_OAUTH_TOKEN`)을 secret으로 넣어
  클라우드에서 headless 실행할 수 있다 (과금형 API 키 불필요).

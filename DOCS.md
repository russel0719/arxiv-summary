← [README (최신 보고서)](README.md)로 돌아가기

# arxiv-summary

arXiv에서 매일 AI 연구 논문을 수집하고, LLM을 활용해 상위 논문을 선별 및 요약한 뒤 한국어 트렌드 리포트를 자동으로 생성하는 도구입니다.

GitHub Actions를 통해 평일 오전 9시(KST)마다 자동 실행되며, 결과 리포트는 `daily_reports/` 디렉토리에 커밋됩니다.

## 동작 흐름

1. arXiv API에서 전날 제출된 논문을 카테고리별로 수집 (`cs.AI`, `cs.LG`, `cs.CV`, `cs.CL`, `stat.ML`)
2. 키워드 기반 필터링으로 관련성 낮은 논문(survey, dataset 등) 제거
3. Groq LLM으로 각 논문에 점수를 매겨 상위 8편 선별
4. 선별된 논문의 PDF를 다운로드하여 본문 기반 상세 요약 생성
5. 전체 트렌드 분석 및 개별 논문 요약을 Markdown 리포트로 저장

## 요구 사항

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)
- Groq API 키

## 설치

```bash
uv sync
```

## 환경 변수 설정

`.env` 파일을 생성하고 아래 내용을 추가합니다.

```
GROQ_API_KEY=your_groq_api_key
```

## 실행

```bash
# 전날(평일 기준) 논문 자동 수집
uv run python main.py

# 특정 날짜 지정 (YYYYMMDD 형식)
uv run python main.py --date 20250301
```

## 출력

- `daily_reports/YYYY/MM/AI_Daily_Trend_YYYY-MM-DD.md`: 일일 AI 트렌드 리포트 (한국어)
  - 전체 트렌드 요약 (CV, NLP, Cross-domain)
  - 상위 논문별 주요 아이디어 / 기여 / 방법론 / 의의

## GitHub Actions 자동화

`.github/workflows/ai-report.yml`에 정의된 워크플로우가 평일 매일 실행됩니다.

Secrets에 `GROQ_API_KEY`를 등록해야 합니다.

```
Settings > Secrets and variables > Actions > New repository secret
Name: GROQ_API_KEY
```

## 의존성

| 패키지 | 용도 |
|---|---|
| `groq` | LLM API 호출 |
| `feedparser` | arXiv RSS/Atom 피드 파싱 |
| `pymupdf` | PDF 텍스트 추출 |
| `requests` | PDF 다운로드 |
| `python-dotenv` | 환경 변수 로드 |

# Arxiv Summary

이 프로젝트는 Arxiv cs.CV 카테고리의 논문 요약을 자동화하는 도구입니다.

## 주요 기능

-   Arxiv 논문 메타데이터 수집
-   논문 내용 요약 생성
-   요약 결과 저장 및 관리

## 사용 방법

1. 이 저장소를 클론합니다:
    ```bash
    git clone https://github.com/your-repo/arxiv-summary.git
    ```
2. `.env` 파일을 생성하고 필요한 환경 변수(Perplexity API key)를 설정합니다. 예시:
    ```bash
    touch .env
    ```
    ```env
    PPLX_API_KEY=pplx-xxxxxxxxxxxxxxxxxxxx
    ```
3. uv를 통해 `summarize.py`파일을 실행합니다:
    ```bash
    uv run summarize.py
    ```
4. uv를 통해 `evaluate.py`파일을 실행합니다:
    ```bash
    uv run evaluate.py
    ```

## API 사용량 분석

-   summarize.py(1 요청 = 25 논문): 40 요청 1.0 USD
-   evaluate.py(1 요청 = 1 논문): 100 요청 0.6 USD

# arXiv Daily Digest — 작업 컨텍스트

이 프로젝트는 매일 arXiv cs.CV 신규 논문 중 유용한 것을 선별·요약하여
마크다운 파일로 저장하는 자동화 파이프라인이다.

## 내 관심사 프로필 (선별 기준)

우선순위 높음:
- Fine-grained visual recognition / similarity, metric learning
- Self-supervised vision (DINO 계열, MAE 등), image embedding
- Open-vocabulary detection (GroundingDINO 계열), segmentation (SAM 계열)
- Vision retrieval, FAISS/벡터 검색과 결합 가능한 표현 학습
- 제조/품질검사, 위조 판별, anomaly detection 등 산업 응용
- OCR, document AI
- 경량화/증류 등 실서비스 배포 관련 기법

우선순위 낮음 (특별히 뛰어나지 않으면 제외):
- 순수 이론, medical imaging 전용, 자율주행 전용 벤치마크 논문
- 단순 데이터셋 공개, 소폭 SOTA 갱신만 있는 논문

## 요약 작업 규칙

1. `today_papers.json`을 읽는다. (title, abstract, authors, url 포함)
2. 위 프로필 기준으로 **가치 있는 논문 5~12편**을 선별한다.
   해당하는 논문이 적으면 적게 뽑아도 된다. 억지로 채우지 말 것.
3. `digests/YYYY-MM-DD.md` 형식으로 저장한다. (오늘 날짜, KST 기준)
4. 각 논문 항목 형식:
   - `### [제목](arxiv url)`
   - **한 줄 요약** (한국어)
   - **핵심 기여**: 2~4문장 (한국어)
   - **실무 관련성**: 내 프로젝트/관심사와 어떻게 연결되는지 1~2문장
   - **키워드**: 3~5개
5. 파일 맨 위에 날짜, 전체 신규 논문 수, 선별 수, 그리고
   오늘의 전반적 트렌드 한 단락을 쓴다.
6. abstract만으로 판단이 어려운 최상위 1~2편은 웹에서 본문/프로젝트
   페이지를 추가로 확인해도 좋다 (선택 사항, 시간 제한 고려).
7. 요약은 모두 한국어로 작성한다. 고유 명사/기법명은 영어 유지.

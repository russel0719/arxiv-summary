# arXiv Daily Digest — 작업 컨텍스트

이 프로젝트는 매일 arXiv cs.CV 신규 논문 중 유용한 것을 선별·요약하여
마크다운 파일로 저장하는 자동화 파이프라인이다.

## 내 관심사 프로필 (선별 기준)

**핵심 전제**: 입력을 **2D 이미지만으로 추론에 쓸 수 있는 모델**을 본다.
3D·멀티모달(VLM)이라도 2D 이미지 입력만으로 활용 가능하면 포함하고,
point cloud·multi-view·특수센서 등 2D 이미지만으로는 못 쓰는 모델은 제외한다.
선별 시 novelty(새 방법론)와 실서비스 적용 가능성을 **균형 있게** 본다.

### 최우선 관심
- **Self-supervised vision backbone** — 특히 새로운 SSL 사전학습 백본
  (DINO/DINOv3, MAE 계열 등)과 image embedding. (이 카테고리가 1순위)
- **피쳐 매칭 / 대응(correspondence)** — 두 이미지 간 유사도로 활용 가능한 표현 전반:
  - local feature/keypoint 매칭 (SuperPoint·SuperGlue·LoFTR 계열)
  - dense / semantic correspondence
  - 이미지쌍 유사도·검증 (verification, re-identification 성격)
  - 매칭·검색용 descriptor/임베딩 표현학습
- **표현학습 + 이미지 검색/유사도** — metric learning, contrastive learning,
  retrieval, FAISS/벡터 검색과 결합 가능한 표현.
- **Fine-grained visual recognition / similarity.**

### 우선순위 높음
- Open-vocabulary detection (GroundingDINO 계열), segmentation (SAM 계열) — 2D 이미지 입력 기준.
- 산업 응용: 제조/품질검사, 결함·anomaly detection, 위조·딥페이크 판별.
- Foundation model 실무 적용 기법 (부차적 관심): 증류/경량화, PEFT/LoRA/adapter,
  양자화·pruning 등 배포 최적화.

### 우선순위 낮음 (특별히 뛰어날 때만)
- OCR, document AI.
- 3D·멀티모달(VLM): 2D 이미지 입력만으로 추론 가능한 경우에 한해 검토.

### 제외 (우선순위 낮음)
- 2D 이미지 입력만으로 사용할 수 없는 모델 (point cloud·multi-view·특수센서 전용 입력).
- 순수 생성모델 (diffusion 등, 인식·표현학습과 무관한 것).
- medical imaging 전용, 자율주행 전용 벤치마크 논문.
- 순수 이론, 단순 데이터셋 공개, 소폭 SOTA 갱신만 있는 논문.

## 요약 작업 규칙

1. `today_papers.json`을 읽는다. (title, abstract, authors, url 포함)
   또한 **프로젝트 프로파일**(`~/workspace/.meta/project_profiles.md`, 러너가 경로를
   넘겨주면 그 경로)이 있으면 함께 읽는다 — 각 프로젝트의 task·개선 여지가 정리돼 있어
   '실무 관련성'을 구체적으로 쓰는 근거가 된다. 없으면 아래 관심사 프로필만으로
   작성한다(선택 입력, 파일이 없어도 다이제스트는 정상 생성).
2. 위 프로필 기준으로 **가치 있는 논문 5~12편**을 선별한다.
   해당하는 논문이 적으면 적게 뽑아도 된다. 억지로 채우지 말 것.
3. `reports/YYYY/MM/report_DD.md` 형식으로 저장한다. (오늘 날짜, KST 기준.
   예: 2026-07-14 → `reports/2026/07/report_14.md`)
4. 각 논문 항목 형식:
   - `### [제목](arxiv url)`
   - **한 줄 요약** (한국어)
   - **핵심 기여**: 2~4문장 (한국어)
   - **실무 관련성**: 내 프로젝트/관심사와 어떻게 연결되는지 1~2문장.
     프로파일을 읽었다면 논문이 어느 프로젝트의 어떤 개선 여지·task에 닿는지 구체적으로
     쓰되, **프로젝트는 task·역할로만 지칭하고 프로파일에 나오는 내부 모델·제품·repo
     이름은 절대 쓰지 않는다** (이 리포트는 공개 repo에 push된다).
     예: "mambaglue에 적용" (X) → "sparse feature matcher 학습에 적용" (O),
     "kering 파이프라인" (X) → "retrieval 기반 정가품 판정 파이프라인" (O).
     (논문 자체의 기법·모델명은 공통 규칙대로 영어로 유지 — 금지 대상은 내 프로젝트 식별자뿐.)
     닿는 프로젝트가 없으면 관심사 프로필 기준으로만 쓴다(억지 매칭 금지).
   - **태그**: 3~5개, 영문 **kebab-case** (검색·모아보기용). 아래 '표준 태그'에서
     우선 고르고, 마땅한 게 없으면 새로 만들되 kebab-case를 유지한다.
     예: `**태그**: ssl-backbone, feature-matching, image-retrieval`

   표준 태그 (우선 선택):
   `ssl-backbone`, `feature-matching`, `correspondence`, `image-retrieval`,
   `metric-learning`, `image-embedding`, `fine-grained`, `re-identification`,
   `open-vocab-detection`, `object-detection`, `segmentation`,
   `industrial-inspection`, `anomaly-detection`, `defect-detection`, `forgery-detection`,
   `foundation-model`, `distillation`, `peft`, `quantization`, `efficient-inference`,
   `vlm`, `ocr-document`, `3d`, `video`, `depth`, `pose`, `generative`, `dataset-benchmark`
5. 파일은 **아래 고정 형식**을 그대로 따른다 (매일 산출물이 동일 포맷이어야 함):

   ```
   # arXiv cs.CV Daily Digest — YYYY-MM-DD (KST)

   - **전체 신규 논문 수**: N편 (new N1 + cross-list N2)
   - **선별 수**: M편

   ## 오늘의 트렌드

   <전반적 트렌드 한 단락>

   ---

   ### [제목](arxiv url)
   (이하 4번의 논문 항목 형식을 각 논문마다 반복, 항목 사이 `---` 구분)
   ```
6. abstract만으로 판단이 어려운 최상위 1~2편은 웹에서 본문/프로젝트
   페이지를 추가로 확인해도 좋다 (선택 사항, 시간 제한 고려).

(언어·git·산출물 범위 등 공통 규칙은 repo 루트 `CLAUDE.md` 참조.)

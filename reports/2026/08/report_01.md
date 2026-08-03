# arXiv cs.CV Daily Digest — 2026-08-01 (KST)

- **전체 신규 논문 수**: 131편 (new 107 + cross-list 24)
- **선별 수**: 10편

## 오늘의 트렌드

오늘 목록은 MLLM/VLM 계열(의료 VQA·시각 토큰 프루닝·agentic reasoning·이미지 편집)과 생성·3D(아바타, video world model)가 수적으로 압도했다. 반면 최우선 관심인 **새 SSL 사전학습 백본**이나 **순수 feature-matching/correspondence** 신작은 오늘은 거의 없었다. 대신 내 관심사에 걸리는 흐름은 네 갈래로 정리된다. (1) **foundation model을 좁은 인식 태스크로 전이**하는 실무형 연구 — DINOv3 백본을 결함 탐지에 이식하거나, pathology FM을 검출 백본으로 재활용하는 시도. (2) **위조·AI 생성물 판별의 성숙** — 단발 이진분류를 넘어 continual(신규 생성기 대응)·해석가능/영역 로컬라이제이션 방향으로 이동. (3) **검색·유사도 표현학습** — MLLM 기반 범용 리트리버·composed image retrieval, 그리고 "무엇이 유사도를 만드는가"를 설명하는 similarity explainability. (4) **배포 최적화** — ViT 혼합정밀도 PTQ, 쿼리 조건부 시각 토큰 선택. 아래는 이 네 흐름에서 실서비스 연결이 뚜렷한 것들을 골랐다.

---

### [BladeYOLO: Wind Turbine Blade Defect Detection with Limited Annotations and Weak-Saliency Awareness](https://arxiv.org/abs/2607.28065)

**한 줄 요약**: DINOv3 SSL 사전학습 ViT를 YOLOv12-L에 이식하고 약결함 강조 모듈을 더해, 라벨이 적고 저대비인 산업 결함을 견고하게 탐지한다.

**핵심 기여**: DINOv3 자기지도 가중치로 초기화한 ViT 백본을 검출기에 통합해 대규모 일반 시각 prior를 소량 라벨 환경으로 전이한다. Mamba 기반 약결함 강조 모듈(고주파 구조 보존 분기 + 얕은 층으로의 의미 전파)과 Fourier 분해로 환경 스타일을 self-attention에 주입하는 Style-Injector로, 작고 저대비인 결함과 조명·배경 변동에 대한 강건성을 높였다. 라벨 예산을 줄인 실험과 공개 표면결함 데이터 교차평가에서 최고 대비 mAP50 +3.5%p를 보고한다.

**태그**: ssl-backbone, defect-detection, industrial-inspection, object-detection, foundation-model

---

### [FiRE: Enhancing MLLMs with Fine-Grained Context Learning for Complex Image Retrieval](https://arxiv.org/abs/2607.27959)

**한 줄 요약**: MLLM을 범용 이미지 리트리버로 쓰되, fine-grained 문맥 모델링과 2단계 분리 파인튜닝으로 long-text-to-image·visual dialog·composed image retrieval 같은 복합 검색을 강화한다.

**핵심 기여**: fine-grained 캡션과 수정 텍스트를 자동 생성하는 multimodal quintuple 데이터 파이프라인으로 CIR 학습 데이터를 구성한다. 기존의 엉킨 파인튜닝을 (1) fine-grained 문맥 추론 지향 단계와 (2) 검색 지향 단계로 분리해, 문맥 이해와 query-target 정합을 순차적으로 끌어올린다. 더 가벼운 백본으로도 5개 데이터셋의 zero-shot 검색에서 기존 기법을 능가한다.

**태그**: image-retrieval, fine-grained, vlm, metric-learning

---

### [Explaining Image Similarity with Automatically Extracted Concept Activation Vectors](https://arxiv.org/abs/2607.28386)

**한 줄 요약**: Sparse Autoencoder로 자동 추출한 Concept Activation Vector를 이용해, 두 이미지의 유사도 점수를 texture·shape·color 같은 개념 단위로 설명하는 모델·메트릭 무관 프레임워크.

**핵심 기여**: 임베딩을 발견된 개념 방향으로 섭동시키고 유사도 함수의 변화량을 측정해 개념별 중요도를 얻는다. 이미지 쌍에는 개념 attribution map으로 국소 근거를, 클러스터에는 group 단위 설명을 제공하며, "유사한 이유"가 비슷한 샘플을 찾는 Exemplar Retrieval로 확장한다. latent 섭동이 pixel-space 기법보다 데이터 분포에 충실하고, 개념 중요도가 실제 유사도 점수를 선형으로 복원함을 보인다.

**태그**: metric-learning, image-retrieval, image-embedding, explainability

---

### [DECODE: Tackling Representation and Decision Degradation in Continual AI-Generated Image Detection](https://arxiv.org/abs/2607.27882)

**한 줄 요약**: AI 생성 이미지 탐지기를 신규 생성 도메인에 증분 적응시킬 때 나타나는 표현·결정경계 이중 열화(Dual Degradation)를 분리해 완화하는 continual 탐지 프레임워크.

**핵심 기여**: 기존 방법이 forgetting을 표현 수준 문제로만 보던 관점을 깨고, 특징이 판별력을 유지해도 분류 헤드의 결정경계가 점진 표류함을 실증한다. Subspace Diversity Regularization으로 다양한 forensic 표현을 보존하고, Closed-Form Decision Alignment로 어댑터 병합 후 공유 분류 헤드를 하이퍼파라미터 튜닝 없이 재보정한다. 19개 생성 도메인에서 평균 99.36% 정확도·0.39% forgetting, 미지 생성기 11종에도 95.36%로 일반화한다.

**태그**: forgery-detection, continual-learning, foundation-model

---

### [Can Vision-Language Models Reason about AI Edits in Images?](https://arxiv.org/abs/2607.28464)

**한 줄 요약**: 명시적 reasoning 라벨 없이 RL(GRPO)만으로 VLM이 AI 변조 여부를 추론하게 학습시키고, 그 근거를 이용해 픽셀 단위 변조 영역까지 로컬라이즈한다.

**핵심 기여**: 정확도·형식 보상만 쓰는 GRPO 프레임워크로, 모델이 답 이전에 구조화된 thinking trace를 생성하도록 유도해 이진분류기의 낮은 해석성·일반화 한계를 넘는다. 추론 출력으로 경량 세그멘테이션 모델을 가이드해 변조 마스크를 만들고, 탐지와 로컬라이제이션을 함께 재는 eff-IoU를 제안한다. 훨씬 약한 감독만으로도 SOTA forgery 탐지기에 준하는 탐지·로컬라이제이션 성능을 보인다.

**태그**: forgery-detection, vlm, segmentation, reinforcement-learning

---

### [Private Face Recognition Training Dataset Publication via Identity-Decoupled and Geometry-Preserving Face Distillation](https://arxiv.org/abs/2607.27764)

**한 줄 요약**: 원본 신원과는 분리(decouple)하되 인식 학습에 유용한 proxy identity 기하는 보존하도록, hyperspherical 임베딩 구조를 유지하며 얼굴 데이터를 distill한다.

**핵심 기여**: "released face를 유용하게 만드는 identity cue가 곧 실제 개인과 연결시키는 cue"라는 identity paradox를, source 정렬 identity 의미(억제)와 인식용 proxy identity 기하(보존)로 분리해 해소한다. Orthogonal Geometry Preservation으로 hyperspherical 기하를 유지한 decoupled proxy 신원을 구성하고, Relational Topology Alignment로 인식 학습에 필요한 신원 간 관계를 보존한다. 도메인 이동 FR 시나리오에서 IJB-C surveillance TAR@FAR=1e-3를 +3.94%p 개선하며 source-identity 연결 가능성은 낮췄다.

**태그**: metric-learning, re-identification, distillation, fine-grained

---

### [Understanding Submodular Information Measure Based Objectives for Representation Learning: A Variance and Separation Perspective](https://arxiv.org/abs/2607.27660)

**한 줄 요약**: 지도 대조학습 목적함수로 쓰이는 Submodular Information Measure(SIM)들이 각각 어떤 분산·분리 기하를 유도하는지 통합 이론으로 규명한다.

**핵심 기여**: Total Information 계열은 클래스 내부 구조(within-class variance, covariance volume, 불균형-인식 분리)를, Mutual Information 계열은 클래스 간 구조(centroid 분리·Fisher 판별, Mahalanobis 기반 분리, nearest-mode overlap)를 포착함을 보인다. 분산·공분산·클래스 불균형·분리·멀티모달 overlap을 독립적으로 변주한 합성 실험에서 이론적 특성이 실제 거동과 일치함을 검증한다. SIM 기반 목적함수를 선택·설계하기 위한 최초의 통합 기하·통계 지침을 제공한다.

**태그**: metric-learning, image-embedding, representation-learning

---

### [MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers](https://arxiv.org/abs/2607.28589)

**한 줄 요약**: ViT 구성요소별 양자화 민감도(fragility)를 KL divergence로 재고, 비트 배분을 배낭문제로 풀어 목표 비트 예산 아래 계층별 정밀도를 적응적으로 할당하는 혼합정밀도 PTQ.

**핵심 기여**: 소량 calibration set으로 full-precision과 고립 양자화 출력 분포 간 KL divergence를 재어 component-level fragility를 추정한다. 비트 할당을 Multiple-Choice Knapsack Problem으로 정식화해 균일 비트폭의 비효율적 정밀도 배분을 대체한다. ImageNet-1K 다수 ViT에서 경쟁력 있는 정확도를, COCO 검출·인스턴스 분할에서 기존 혼합정밀 PTQ 대비 최대 9.6 AP 개선을 보고한다.

**태그**: quantization, efficient-inference, foundation-model

---

### [ReToken: One Token to Improve Vision-Language Models for Visual Retrieval](https://arxiv.org/abs/2607.28627)

**한 줄 요약**: 학습 가능한 단일 임베딩 하나를 명시적 검색 타깃으로 훈련해, 미리 채워둔 시각 KV 캐시에서 쿼리 관련 시각 토큰만 희소하게 골라내는 방식으로 긴 시각 문맥 VLM 성능을 끌어올린다.

**핵심 기여**: 소규모 image-QA 데이터만으로 학습한 단일 학습형 토큰(ReToken)이 distractor가 많은 긴 문맥에서 쿼리 관련 토큰을 선별한다. Visual Haystacks에서 Qwen3VL-8B +13.4점, InternVL3.5 +12.4점(상대 20%↑), LVBench 긴 영상에는 zero-shot 전이로 +8.0점을 얻는다. 경량 설계로 학습·긴 영상 추론이 단일 H100에 들어간다.

**태그**: image-retrieval, efficient-inference, vlm

---

### [Deep learning-based hierarchical insect classification using camera trap imagery](https://arxiv.org/abs/2607.28005)

**한 줄 요약**: 5단계 34클래스 분류 계층을 따라, 세부 단계가 불확실하면 신뢰도 임계값(0.6)에서 더 거친 상위 단계로 물러나 예측하는 롱테일 fine-grained 분류 모델.

**핵심 기여**: 카메라 트랩 영상에서 추출한 약 100만 장·5단계 계층 라벨의 롱테일 데이터셋을 큐레이션하고, class-balanced 가중으로 가변깊이 계층 분류 구조를 적응시킨다. 생물 분류체계를 활용해 granularity별 시각 특징을 뽑고, 신뢰도 임계값을 만족하는 가장 깊은 단계까지만 hierarchy-consistent 예측을 낸다. 5개 계층에서 단계별 80–99% 정확도를 달성한다.

**태그**: fine-grained, image-classification, dataset-benchmark

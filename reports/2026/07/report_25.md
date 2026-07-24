# arXiv cs.CV Daily Digest — 2026-07-25 (KST)

- **전체 신규 논문 수**: 107편 (new 94 + cross-list 13)
- **선별 수**: 9편

## 오늘의 트렌드

오늘은 **3D Gaussian Splatting·비디오 생성**(SubSplat, FA-LAM, Ms.Forcing, SANA-Video 2.0, GraphVid 등)과 **MLLM 벤치마크·환각 진단**(ViSTR-Bench, HalluScope, Geo3R, CRAG-MM-Diagnostics 등)이 물량의 대부분을 차지했고, 인식·표현학습 코어 논문은 상대적으로 적었다. 그 속에서 눈에 띄는 흐름은 **frozen DINO 계열 백본 위에 가벼운 모듈만 얹어 새 능력을 부여하는 설계**다 — CLIP 텍스트 임베딩을 ODE 궤적으로 DINOv3 매니폴드에 정렬해 open-vocabulary segmentation을 푸는 DINOde, 멀티모달 융합 없이 hierarchical visual prompt tuning만으로 물리+디지털 위조를 통합 판별하는 DINO-VPT가 대표적이다. 산업 검사 쪽에서는 철강 표면의 가늘고 긴 결함에 특화한 분할 네트워크와, 그라비어 인쇄 품질검사용 합성 결함 데이터 생성 프레임워크가 나란히 나와 **합성 데이터 기반 결함 검사**의 실무 레시피가 쌓이고 있다. 배포 최적화 축에서는 MLLM 양자화(C-PTQ)와 LoRA 어댑터 병합(CT-Merging)이, 검색 축에서는 쿼리 세밀도(granularity) 불확실성을 정면으로 다룬 person retrieval 벤치마크가 수확이다.

---

### [DINOde: Continuous Vision-Text Alignment for Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2607.21371)

**한 줄 요약**: CLIP 텍스트 임베딩을 ODE 기반 연속 궤적으로 DINOv3 시각 매니폴드에 정렬해, 텍스트 정렬이 없는 SSL 백본으로 open-vocabulary segmentation을 푸는 프레임워크.

**핵심 기여**: DINOv3는 구조적으로 강한 시각 표현을 주지만 텍스트 정렬이 없어 open-vocabulary segmentation(OVSS)에 바로 못 쓴다는 간극을 겨냥한다. Semantic Text Flow가 CLIP 텍스트 임베딩을 연속 ODE 궤적으로 DINO 매니폴드까지 진화시키고, Global Context Flow가 DINO CLS 토큰의 전역 이미지 표현을 점진 정제하며, Velocity Tangent Projection으로 속도장을 접공간에 구속해 hypersphere 기하를 보존한다. 이산 MLP projection이 일으키는 manifold entanglement를 피해 더 견고한 cross-modal 정렬을 얻고, 다수 OVSS 벤치마크에서 SOTA를 달성했다. 코드 공개.

**실무 관련성**: frozen DINOv3 임베딩 위에 retrieval 기반 정가품 판정을 올려둔 파이프라인에서, 같은 백본에 텍스트 정렬 모듈만 추가하면 부위 단위 open-vocab 분할까지 단일 백본으로 통합할 수 있는 경로를 보여준다 — 무거운 검출+분할 스택을 SSL 백본 하나로 합치려는 개선 방향과 직결된다.

**태그**: ssl-backbone, segmentation, open-vocab-detection, foundation-model, image-embedding

---

### [Visual Contrastive Self-Distillation](https://arxiv.org/abs/2607.21556)

**한 줄 요약**: 외부 teacher·정답·추론 트레이스 없이, 이미지 조건부/이미지 제거 두 분포의 대비만으로 VLM을 on-policy self-distillation하는 VCSD.

**핵심 기여**: on-policy self-distillation은 teacher-student 간 비대칭 정보(특권 정답, 시각 증거 등)에 의존해 왔는데, VCSD는 이를 입력 조건화만으로 대체한다. EMA teacher가 같은 프롬프트·프리픽스에서 원본 이미지 조건 분포와 내용 제거(content-erased) 조건 분포를 각각 내고, 토큰별 log-probability 차이로 "그 이미지 내용 때문에 확률이 오른 후보"를 식별해 teacher 분포를 그 방향으로 날카롭게 만든 뒤 full-distribution으로 증류한다. Qwen3-VL 2B/4B/8B에서 7개 벤치마크 종합을 각각 +4.8/+1.9/+3.8pp 개선했고 추가 추론 비용이 없다.

**실무 관련성**: 외부 teacher와 라벨 없이 증류 신호를 만드는 레시피라, foundation model을 서비스 규모로 경량화·증류할 때 데이터 준비 부담을 크게 줄이는 접근으로 참고할 만하다. 이미지 조건 유무의 분포 대비로 "시각적으로 근거 있는" 신호만 강화하는 아이디어 자체도 시각 근거가 중요한 판별 태스크에 시사점이 있다.

**태그**: distillation, vlm, foundation-model, efficient-inference

---

### [Achieving Text-based Person Retrieval with Any Granularity](https://arxiv.org/abs/2607.21057)

**한 줄 요약**: 쿼리 세밀도(granularity)의 불확실성을 5단계 스펙트럼으로 정식화하고, 다중 정답을 확률적으로 정렬하는 granularity-aware 검색 프레임워크 CMAM.

**핵심 기여**: 실제 검색에서 쿼리가 얼마나 상세할지 알 수 없다는 문제를 정면으로 다룬다. 5단계 granularity 스펙트럼을 정의하고 전 단계를 주석한 UFine6926-MG 데이터셋과, 거친 쿼리는 복수 정답에 대응한다는 현실을 반영한 cross-identity 라벨·전용 지표의 MG-Eval 벤치마크를 구축했다. CMAM은 (1) granularity별 특성을 분리하는 orthogonal-expert perception, (2) 쿼리 불확실성 하의 many-to-many 매칭을 모델링하는 probabilistic alignment, (3) 교차모달 granularity 검증으로 표현학습을 조향하는 consistency reasoning으로 전 granularity에서 SOTA를 넘었다.

**실무 관련성**: "거친 쿼리 → 복수 유효 후보"를 명시적으로 모델링하는 확률적 정렬과 평가 프로토콜은, top-N retrieval 점수로 판정을 내리는 정가품 판정 파이프라인에서 판정불가 구간을 다루고 검색 평가 지표를 설계하는 데 그대로 참고할 만하다.

**태그**: image-retrieval, metric-learning, re-identification, fine-grained, dataset-benchmark

---

### [DINO-VPT: Hierarchical Visual Prompt Tuning for Joint Physical-Digital Face Anti-Spoofing](https://arxiv.org/abs/2607.20900)

**한 줄 요약**: 멀티모달 융합·텍스트 인코더 없이, 입력 조건부 prompt routing 기반 hierarchical visual prompt tuning만으로 물리+디지털 위조를 통합 판별하는 vision-only FAS.

**핵심 기여**: 물리 공격(인쇄물·리플레이)과 디지털 공격(딥페이크)을 하나의 모델로 잡는 unified Face Anti-Spoofing에서, 기존 VLM 기반 접근의 복잡한 멀티모달 융합·외부 텍스트 인코더 의존을 제거한다. Prompt Routing Network가 입력 특징에 조건화된 프롬프트를 동적으로 주입해 다양한 위조 아티팩트를 분리(disentangle)하며, UniAttackData 벤치마크에서 VLM 기반 SOTA보다 높은 정확도를 경량 vision-only 구조로 달성했다.

**실무 관련성**: frozen SSL 백본에 가벼운 prompt tuning만으로 진위 판별력을 부여하는 사례로, frozen 백본+얇은 어댑터 구조의 정가품 판정 파이프라인에서 PEFT로 판별력을 끌어올리려는 개선 여지에 직접 닿는다. 위조 유형별 아티팩트를 입력 조건부 프롬프트로 분리하는 설계도 다양한 위조 패턴 대응에 참고가 된다.

**태그**: forgery-detection, peft, ssl-backbone, fine-grained

---

### [SPDCN: Strip-based Deformable Convolutional Network for Steel Surface Defect Segmentation](https://arxiv.org/abs/2607.21456)

**한 줄 요약**: 수평·수직 strip convolution으로 offset을 분리 예측해, 가늘고 긴 이방성 결함(크랙·스크래치)에 샘플링 그리드를 정렬하는 3.5M 파라미터 철강 결함 분할 네트워크.

**핵심 기여**: 표준 convolution의 등방성 수용영역과 경직된 샘플링 그리드가 가늘고 긴 결함의 불규칙 경계에 적응하지 못한다는 문제를 겨냥한다. Fuzzy-enhanced Multi-scale Context Module이 그룹별 멀티브랜치 convolution과 fuzzy 채널 어텐션으로 크기가 제각각인 결함의 문맥을 잡고, Adaptive Direction-Aware Deformable Convolution이 기존 offset predictor를 수평·수직 strip convolution으로 분해해 deformable 샘플링을 결함의 주방향에 이방성으로 정렬한다. NEU-Seg에서 3.54M 파라미터로 89.60% mIoU를 달성하며 SOTA를 넘었다. 코드 공개.

**실무 관련성**: 제조 표면 품질검사에서 스크래치·크랙류 세장형 결함은 흔한 난제라, 경량 파라미터로 이방성 결함 경계를 잡는 이 설계는 산업 결함 분할 모델을 만들 때 바로 시험해 볼 만한 백본 구성이다.

**태그**: industrial-inspection, defect-detection, segmentation, efficient-inference

---

### [Synthetic data generation framework for quality control automation in gravure printing](https://arxiv.org/abs/2607.21577)

**한 줄 요약**: 그라비어(rotogravure) 인쇄 결함(주름·줄무늬·misregistration 등)을 bbox 주석과 함께 자동 합성해, 실제 산업 샘플에서 mAP 80.9%의 검출기를 실데이터 없이 학습시키는 프레임워크.

**핵심 기여**: 인쇄 품질검사 자동화의 최대 병목인 실결함 이미지 희소성을 겨냥해, 인쇄 결함 유형별 고충실도 이미지를 bbox·주석과 함께 자동 생성하는 파이프라인을 제안한다. 합성 7,533장으로 RF-DETR을 학습시켜 실제 산업 테스트 샘플에서 mAP 80.9%를 달성, 대규모 수작업 수집 없이 인쇄 라인 결함 검사를 배포할 수 있음을 보였다.

**실무 관련성**: 합성 데이터로 인쇄물·타이포그래피 위조 판정을 학습하는 파이프라인의 핵심 병목이 합성→실전 전이 갭인데, 같은 인쇄 도메인에서 어떤 결함 축·합성 충실도가 실데이터 일반화로 이어졌는지를 보여주는 직접적인 비교 사례다. 인쇄 특유의 결함 유형(줄무늬·misregistration) 합성 레시피도 합성 데이터 생성기 설계에 참고할 수 있다.

**태그**: industrial-inspection, defect-detection, dataset-benchmark, object-detection

---

### [Explainable Deepfake Detection Challenge](https://arxiv.org/abs/2607.21007)

**한 줄 요약**: 진위 라벨과 함께 기술 사용자용·일반 사용자용 두 층위의 시각 근거 설명을 요구하는, million-scale 벤치마크(XPlainVerse) 기반 ACM MM 2026 챌린지.

**핵심 기여**: 딥페이크 판별을 이진 분류를 넘어 "왜 의심스러운가"를 설명하는 문제로 확장한다. 이미지마다 real/fake 라벨과 상세한 기술적 설명·간결한 일반인용 설명을 함께 제출하게 하고, 분류 지표에 더해 설명이 실제 조작된 개체와 시각 증거를 짚는지 평가하는 intent-aware grounding 지표를 도입했다. 평가 스크립트·베이스라인·코드가 공개돼 있다.

**실무 관련성**: 위조 판별 결과에 부위 단위 의심 영역과 판정 근거를 함께 제시해야 하는 정가품 판정 task와 요구사항이 정확히 겹친다 — 판정+근거 설명을 공동 평가하는 지표 설계는 판별 서비스의 신뢰성 리포트 설계에 참고할 만하다.

**태그**: forgery-detection, dataset-benchmark, vlm

---

### [C-PTQ: Fisher-weighted Channel-wise Sensitivity for Post-training Quantization of MLLMs](https://arxiv.org/abs/2607.21076)

**한 줄 요약**: Fisher 근사로 태스크 손실 민감도를 채널별 스케일링에 주입해, LoRA 같은 보조 모듈 없이 MLLM PTQ SOTA를 달성하는 방법.

**핵심 기여**: 기존 MLLM PTQ의 채널별 스케일링이 modality·token 수준 지표에 의존해 태스크 손실에 대한 채널별 영향을 못 잡는다는 문제를 지적한다. 2차 미분에 착안한 Fisher-weighted 목적함수를 Hessian의 tractable 근사로 설계해, 태스크 민감도와 양자화 오차를 하나의 스케일링 과정에서 조화시킨다. Qwen2.5-VL·InternVL2·LLaVA-OV, 8개 벤치마크의 weight-only·weight-activation 설정 모두에서 보조 모듈 없이 SOTA를 달성했다.

**실무 관련성**: foundation model을 서비스에 붙일 때의 배포 최적화(양자화) 관심에 해당한다. 채널 중요도를 태스크 손실 기준으로 재정의하는 아이디어는 MLLM에 국한되지 않아, 무거운 검출·임베딩 모델의 PTQ에도 이식을 검토할 수 있다.

**태그**: quantization, efficient-inference, vlm, foundation-model

---

### [CT-Merging: Consensus Directions and Task-Level Scaling for LoRA Adapter Merging](https://arxiv.org/abs/2607.20561)

**한 줄 요약**: 태스크별 SVD 부분공간의 반복 지지(repeated support)로 합의 방향을 잡고 태스크 수준 RMS 계수로 스케일을 재배정해, 여러 LoRA 어댑터를 하나의 멀티태스크 어댑터로 병합하는 방법.

**핵심 기여**: 태스크마다 LoRA 어댑터를 따로 배포하면 저장·추론 시 태스크 선택 부담이 생기는데, 기존 SVD 기반 병합은 방향 구성에 집중하고 계수는 원 태스크 SVD에서 그대로 물려받아 크기 불일치가 생긴다는 점을 짚는다. CT-Merging은 평균 태스크 부분공간 projector에서 합의 방향을 추정하고, rank별 SVD 크기 의존을 줄인 태스크 수준 RMS 계수 스케일을 최종 업데이트에 배정한다. DC-Merge CLIP 어댑터 벤치마크에서 기존 SOTA 병합법을 넘고 DC-Merge 대비 ViT-B/32 +2.56pp, ViT-L/14 +1.51pp를 얻었다.

**실무 관련성**: frozen 백본 + 태스크별 경량 어댑터 구조를 쓰는 판별 파이프라인에서 브랜드·카테고리가 늘어 어댑터가 증식할 때, 단일 멀티태스크 어댑터로 병합해 배포를 단순화하는 실무 옵션이 된다.

**태그**: peft, foundation-model, efficient-inference

---

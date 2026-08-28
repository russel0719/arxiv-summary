# arXiv cs.CV Daily Digest — 2026-08-14 (arXiv 공개일)

- **전체 신규 논문 수**: 107편 (new 91 + cross-list 16)
- **선별 수**: 11편

## 오늘의 트렌드

오늘 cs.CV 신규·크로스리스트 107편은 (1) 비디오·인터랙티브 world model과 diffusion 가속·distillation, (2) egocentric·long-form 비디오 이해와 MLLM 신뢰성 벤치마크, (3) 의료 영상 3D·longitudinal 추론에 크게 몰려 있었다. 내 관심 축에서는 **SSL 백본을 어떻게 실전에 쓰는가**가 하나의 흐름으로 드러났다 — 자원 제약 하에서 SSL 목적함수를 통제 비교한 연구와, DINOv2 교사의 신뢰도 포화를 다루는 준지도 학습이 나란히 등장했다. 그 밖에 open-world·sparse 검출, 속성 제어형 retrieval, 얼굴·보행자 검증/재검색, AI 생성 이미지·위조 탐지, 엣지 배포용 ViT 경량화가 고르게 나와 표현학습·매칭·검증·배포라는 실무 축과 맞닿는 논문이 여럿 있었다.

---

### [A Controlled Study of Self-Supervised Image and Video Pretraining under Limited Resources](https://arxiv.org/abs/2608.13183)

**한 줄 요약**: 데이터·아키텍처·연산 예산을 맞춘 통제 실험에서 이미지·비디오 SSL 목적함수들을 공정 비교해, 제한된 자원에서는 DINOv2 스타일 사전학습이 가장 강력함을 보인 연구.

**핵심 기여**: contrastive, reconstruction, feature-prediction, diffusion 목적을 동일 예산 하에서 비교하고 이미지·비디오 SSL을 단독/공동 학습으로 평가했다. DINOv2 스타일이 전반적으로 최고 성능을 냈으며, DINOv2에 VideoMAE 같은 비디오 SSL을 결합하면 이미지 분류·분할은 크게 개선되지만 video tracking·camera-pose 추정은 저하됐다. 이는 semantic 표현과 geometric 표현 사이의 근본적 트레이드오프를 드러낸다.

**태그**: ssl-backbone, image-embedding, foundation-model, segmentation

---

### [CW-BASS v2: Saturation-Aware Pseudo-Label Selection for Semi-Supervised Segmentation under Foundation-Model Teachers](https://arxiv.org/abs/2608.12773)

**한 줄 요약**: DINOv2 같은 강한 SSL 교사에서 confidence가 포화되면 pseudo-label 필터링이 오히려 해가 된다는 점을 짚고, 교사의 신뢰도 regime을 읽어 필터링 전략을 무튜닝으로 자동 조정하는 준지도 분할 기법.

**핵심 기여**: 약한 ResNet 교사용으로 설계된 기존 pseudo-label 선택 규칙(동적 임계값·per-class 커리큘럼 등)이 DINOv2 교사에서는 confidence 포화 때문에 성능을 떨어뜨림을 지적한다. held-out 보정으로 confident set의 신뢰도(pi_kept = Pr[correct | c≥τ])를 측정해 엄격 필터링과 적응형 floor 중 하나를 한 번에 선택하는 one-pass gate를 제안한다. 포화 벤치마크에서 강한 교사의 운용점을 복원하고, confident set이 불안정한 곳(ADE20K)에서는 floor가 앞선다.

**태그**: ssl-backbone, foundation-model, segmentation, distillation

---

### [Online Learning of Correspondences between Images](https://arxiv.org/abs/2608.13104)

**한 줄 요약**: 3D 장면에 접근하지 않고 이미지쌍의 점 대응을 반복적·온라인으로 학습해 실시간으로 대응 매핑을 갱신하는 방법.

**핵심 기여**: 투영 기하·왜곡·표면 형상을 모르는 상태에서, point-set 쌍들만으로 두 뷰 간 대응 매핑을 학습한다. 추정 위치와 실제 위치의 불확실성 밀도 간 Neyman χ² divergence를 최소화하며, 밀도를 basis function 기반 channel vector로 표현한다. 새 이미지쌍이 들어올 때마다 매핑을 갱신해 빠른 수렴과 높은 정확도를 얻고 실시간으로 동작하며, 수렴·정확도에서 SOTA를 넘는다.

**태그**: correspondence, feature-matching, efficient-inference

---

### [Attribute-Conditioned Multimodal Slot Factorization for Controllable Fashion Retrieval](https://arxiv.org/abs/2608.12570)

**한 줄 요약**: Fashion-CLIP의 텍스트·이미지 임베딩을 이름 붙은 속성 슬롯 4개로 분해해, 속성별로 독립 제어 가능한 패션 검색을 구현한 MM-slotgate.

**핵심 기여**: 단일 임베딩이 category·color·pattern·demographic 신호를 한 벡터에 섞어 속성별 제어를 어렵게 만드는 문제를 지적한다. 각 슬롯이 자체 text-image gate를 학습해 시각적 속성(color·pattern)은 이미지 근거에, 분류적 속성(category)은 텍스트에 더 의존하도록 한다. slot-similarity + slot-logit 결합 점수로 H&M에서 macro ConstraintSatisfied@10 0.7566을 달성(등가중 융합 0.7142 대비 개선), color가 0.321→0.889로 크게 향상됐고 학습된 gate가 해석 가능하다.

**태그**: image-retrieval, metric-learning, fine-grained, image-embedding

---

### [Heterogeneous Vision-Language Ensemble with Disagreement-Aware Reranking for Text-Based Person Anomaly Retrieval](https://arxiv.org/abs/2608.12843)

**한 줄 요약**: 자연어로 이상행동 보행자를 대규모 갤러리에서 검색하기 위해 이종 VLM 임베딩을 앙상블·재랭킹한 AI City Challenge 우승급 솔루션.

**핵심 기여**: 강한 retrieval 백본 위에 이종 vision-language 임베딩 모델들을 score alignment과 반복 앙상블 융합으로 통합하고, 모호한 쿼리에 한해 disagreement-aware VLM 재랭킹을 적용한다. PAB 벤치마크에서 mAP 90.92%, Recall@1 85.13%, Recall@5 97.72%를 달성해 상보적 표현 결합과 선택적 멀티모달 추론의 효과를 보였다.

**태그**: image-retrieval, re-identification, anomaly-detection, metric-learning

---

### [Bias Mitigation in Face Recognition via Demographic-based Supervised Contrastive Learning](https://arxiv.org/abs/2608.12971)

**한 줄 요약**: 데모그래픽 인지 pair 선택으로 배치를 구성하는 supervised contrastive loss(DeSCon)로, 얼굴 인식의 공정성을 비매칭 점수 분포의 꼬리에서 개선.

**핵심 기여**: 데이터를 인위적으로 균형 맞춰도 저 false-match-rate 운용점(비매칭 점수 분포의 꼬리)의 편향이 완전히 해소되지 않는다는 점을 짚는다. DeSCon은 배치 구성과 데모그래픽 인지 pair 선택을 통해 분포의 평균이 아니라 꼬리 거동을 직접 다뤄, 표준 검증 벤치마크 성능을 유지하면서 데이터 균형만으로 얻는 것 이상의 공정성 향상을 보였다.

**태그**: metric-learning, re-identification, fine-grained

---

### [Class Geometry as Supervision for Sample-Efficient Open-World Detection](https://arxiv.org/abs/2608.12698)

**한 줄 요약**: 클래스 간 관계 기하를 프로토타입 공간에 보존하도록 감독해, 소량 데이터 open-world 검출의 표본 효율과 신규 클래스 삽입을 강화하는 CGS.

**핵심 기여**: 프로토타입 기반 검출기가 클래스 프로토타입을 독립 앵커로 학습해 클래스 간 관계 구조를 무시하는 문제를 지적한다. CGS는 학습 데이터에서 추정한 시각·의미적 비유사도를 보존하는 dissimilarity-preserving 목적을 표준 task loss와 함께 최적화한다. 인식·few-shot 생의학 검출·open-set·신규 클래스 삽입·OWOD에서 표본 효율과 unknown recall을 개선했고, 무의미한 랜덤 기하보다 시각적 기하가 일관되게 유효함을 보였다.

**태그**: object-detection, metric-learning, fine-grained, open-vocab-detection

---

### [Towards Sparsely Annotated Open-World Object Detection](https://arxiv.org/abs/2608.12714)

**한 줄 요약**: 미라벨 영역이 known 객체의 누락 라벨인지 진짜 unknown인지 모호한 실전 상황을 위해, sparse 감독과 open-world를 결합한 새 과제(SA-OWOD)와 DPOD 프레임워크를 제안.

**핵심 기여**: 그동안 따로 다뤄진 Sparsely Annotated Object Detection과 Open-World Object Detection을 함께 고려하는 SA-OWOD 과제를 정의한다. DPOD는 미라벨 known을 복구·정규화하는 KTRM과 cross-view 의미 불일치로 신뢰할 만한 unknown 후보를 식별하는 DDTG로 모순된 감독 신호를 해소한다. sparse 주석 open-world 벤치마크에서 특히 unknown 검출 성능이 기존 방법을 앞선다.

**태그**: object-detection, open-vocab-detection

---

### [A Generative Approach for Improving Multi-Label Defect Classification in Photovoltaic Modules](https://arxiv.org/abs/2608.12725)

**한 줄 요약**: LaMa inpainting으로 결함을 제거해 단일 결함 학습 샘플을 생성함으로써, EL 이미지의 다중 라벨 태양광 셀 결함 분류에서 발생하는 학습 모호성을 완화하는 GDI.

**핵심 기여**: 여러 결함이 공존하는 이미지 학습이 특정 결함 특징의 분리를 어렵게 하고, 개별 클래스 예시 부족으로 악화되는 문제를 다룬다. Generative Defect Isolation(GDI)은 Fast Fourier Convolution 기반 LaMa로 선택한 결함을 제거해 현실적인 단일 결함 샘플을 만든다. ViT-S/L·EfficientNetV2-L에서 baseline을 크게 앞서고, 저데이터 상황에서 이득이 가장 커 희귀 클래스 F1을 최대 63.6% 올리고 공존 오분류를 26% 줄였다.

**태그**: defect-detection, industrial-inspection, anomaly-detection, generative

---

### [SPARED: Reasoning-Based AI-Generated Image Detection via Adversarially Edited Data](https://arxiv.org/abs/2608.12876)

**한 줄 요약**: diffusion 이미지 편집기와 추론형 MLLM을 적대적으로 맞붙여, 근거 있는 판정을 내리는 AI 생성 이미지 탐지기를 학습하는 강화학습 프레임워크.

**핵심 기여**: 기존 탐지기가 서로 다른 출처(provenance) 지름길, 템플릿화된 설명, 고정 위조 분포에 과적합되는 세 실패모드를 지적한다. 편집기는 같은 사진을 현재 탐지기를 속이는 가짜로 편집하고, MLLM은 free-form 추론 근거로 이를 폭로하는데 두 보상 모두 지름길을 원천 차단하도록 설계됐다(편집이 충실히 수행돼야 편집기가, 판정이 옳아야 방어자가 보상). 라운드마다 더 어려운 학습 풀을 생성해 세 외부 벤치마크에서 성능이 단조 개선되고, 설명 품질도 부수적으로 향상된다.

**태그**: forgery-detection, anomaly-detection, vlm

---

### [MergeOver: Post-Training Token Merging for Recursive Vision Transformers](https://arxiv.org/abs/2608.13141)

**한 줄 요약**: 재귀적 weight-sharing ViT에 token merging을 재학습 없이 결합해, 엣지 배포용 메모리·지연을 줄이는 post-training 기법.

**핵심 기여**: 파라미터를 줄이는 재귀 weight-sharing(SReT)과 연산·메모리를 줄이는 token merging(ToMe)을 재학습 없이 통합하는 미개척 문제를 다룬다. Unmerge 추적 스택, 제약 안전 merge-rate 조정, 공간 순열 간 token-mass 동기화로 통합의 공간·병합 제약을 해소한다. ImageNet-1K에서 top-1 1.47%p 하락만으로 GPU 활성 메모리를 37~38% 줄이고 Raspberry Pi 5(ARM CPU)에서 지연을 감소시켜, 재학습 없는 경량화 baseline을 제시한다.

**태그**: efficient-inference, foundation-model, token-merging

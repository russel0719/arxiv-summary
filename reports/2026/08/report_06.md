# arXiv cs.CV Daily Digest — 2026-08-06 (KST)

- **전체 신규 논문 수**: 146편 (new 123 + cross-list 23)
- **선별 수**: 10편

## 오늘의 트렌드

오늘 목록은 VLM/MLLM의 **효율화**(visual token pruning, 구조적 pruning, test-time adaptation)와 diffusion 기반 생성·편집·3D 생성, 그리고 원격탐사·의료영상 논문이 큰 비중을 차지했다. 표현·매칭 관점에서 눈에 띄는 흐름은 **DINOv3/SSL 백본의 재활용**이다 — 별도 학습 없이 open-vocabulary semantic segmentation을 수행하거나(DinoSplat-OV, PTC), frozen 백본의 coarse한 patch feature를 픽셀 단위로 업샘플해 dense 예측 정밀도를 끌어올리는(PixelUp) 방향으로 수렴하고 있다. 여기에 robust local feature matching(SGFormer), zero-shot 이미지 검색(SeCo-SBIR), near-duplicate 매칭 견고화(DualShield), 산업/의료 zero-shot anomaly detection의 경량화(KeepAD)가 더해져, 매칭·검증·이상탐지 파이프라인을 **더 강한 단일 백본 + 무학습/경량 어댑팅**으로 재구성하려는 시도가 두드러진다. 배포 최적화 축에서는 PEFT(MuRA)와 양자화(NAP)에서 "전체 파라미터를 건드리지 않고 저차원 고레버리지 부분공간만 조정"하는 공통 아이디어가 관찰된다.

---

### [SGFormer: Structure-Guided Transformer for Robust Local Feature Matching](https://arxiv.org/abs/2608.03423)

- **한 줄 요약**: LoFTR류 detector-free 매칭의 attention이 비오버랩 영역으로 분산되는 문제를 구조 인식 attention으로 억제한 semi-dense local feature matcher.
- **핵심 기여**: 표준 Transformer의 무제약 global attention이 관련 없는 영역의 유사 feature에도 동일한 가중치를 주어 유효 매칭 영역(오버랩) 밖에 high-confidence 매칭이 흩어지는 "attention divergence" 현상을 정의했다. 초기 얕은 레이어의 local feature로 salient structure 주변 표현을 강화하는 Triple-Structure-Attention(TSA) 모듈을 backbone에 삽입해, 이후 transformer 단계가 오버랩 영역의 구조에 집중하도록 유도한다. semi-dense coarse-to-fine 파이프라인 위에서 큰 시점 변화 상황의 매칭 정확도를 개선했다.
- **태그**: feature-matching, correspondence, detector-free

---

### [PixelUp: Zero-Shot Semantic Feature Upsampling for Fine-Grained Vision Tasks](https://arxiv.org/abs/2608.02792)

- **한 줄 요약**: 인코더에 종속되지 않는 zero-shot feature upsampler로, frozen SSL 백본의 coarse한 patch-token feature를 의미 인식하며 픽셀 단위로 복원한다.
- **핵심 기여**: SSL Vision Foundation Model의 patch-token feature가 dense 예측에는 너무 coarse하다는 한계에 대해, 인코더별 재학습이 필요한 learnable upsampler와 텍스처 아티팩트를 유발하는 image-guided 방식의 단점을 동시에 피하는 VFM-agnostic 접근을 제안한다. 다중 스케일 semantic feature로 가이드되는 windowed cross-attention의 coarse-to-fine 체인으로 의미 인식을 확보했다. 여러 VFM에서 semantic segmentation +1.2 mIoU, training-free open-vocab segmentation +1.3 mIoU 등 일관된 향상을 보였다.
- **태그**: ssl-backbone, segmentation, fine-grained, foundation-model

---

### [Standalone DINOv3 for Training-Free Open-Vocabulary Semantic Segmentation in Remote Sensing](https://arxiv.org/abs/2608.03023)

- **한 줄 요약**: DINOv3의 DINO.txt(image-text contrastive)를 활용해 파인튜닝 없이 open-vocabulary segmentation을 수행하는 training-free 프레임워크.
- **핵심 기여**: DINOv3가 제공하는 standalone 백본 + image-text contrastive 능력을 fine-tuning·추가 사전학습 없이 활용하는 DinoSplat-OV를 제안한다. 텍스트 의미 유사도와 local visual similarity를 결합해 patch 예측 노이즈를 줄이는 Text-aware Laplacian Propagation과, RGB-guided anisotropic aggregation·test-time 최적화로 픽셀 단위 feature를 복원하는 Gaussian Splatting Upsampling 모듈을 설계했다. 대형 이미지를 위한 global-anchor sliding-window 전략도 포함해 기존 training-free 기법 대비 경쟁력 있는 성능을 보였다.
- **태그**: ssl-backbone, segmentation, open-vocab-segmentation

---

### [Perceptual Anchoring: Prototype-Guided Text Calibration for Training-free Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2608.03991)

- **한 줄 요약**: 시각 프로토타입으로 텍스트 임베딩을 보정해 무학습 open-vocab segmentation의 마스크 완성도와 오분류를 개선하는 plug-and-play 모듈.
- **핵심 기여**: 기존 training-free OVSS가 시각 표현 개선에만 집중하고 generic 카테고리 개념을 담은 텍스트 임베딩을 고정 참조로 두어 생기는 semantic gap을 지적한다. Perceiving 단계에서 초기 매칭 점수로 신뢰할 만한 시각 증거를 골라 category-specific 프로토타입을 구성하고, Anchoring 단계에서 이 프로토타입으로 텍스트 임베딩을 시각 증거량에 비례해 적응적으로 보정한다. 추가 학습·외부 모델 없이 6개 대표 기법에 얹어 8개 벤치마크에서 일관된 향상을 냈다.
- **태그**: segmentation, open-vocab-segmentation, vlm

---

### [SeCo-SBIR: Semantically Consistent Prompt Learning for Zero-Shot Sketch-Based Image Retrieval](https://arxiv.org/abs/2608.03120)

- **한 줄 요약**: CLIP prompt learning을 도메인 갭에 적응시키면서도 seen 카테고리 과적합을 막아 unseen 일반화를 지키는 zero-shot 이미지 검색 프레임워크.
- **핵심 기여**: sketch-photo 도메인 갭을 좁히려는 task-specific 적응이 학습 카테고리에 과적합돼 CLIP의 zero-shot 일반화를 훼손하는 긴장을 양방향으로 해소한다. 텍스트 인코더를 거친 프롬프트 표현을 layer마다 visual 인코더로 주입해 전이 가능한 semantic 지식을 시각 경로에 넣고, frozen CLIP 참조 브랜치와의 asymmetric InfoNCE consistency로 학습 표현을 일반화 가능한 feature 공간에 고정한다. 세 개 표준 ZS-SBIR 벤치마크의 categorical·generalized·cross-dataset 설정에서 SOTA를 달성했다.
- **태그**: image-retrieval, metric-learning, vlm, peft

---

### [Double Down on Defense: Strengthening Deep Perceptual Hashes against Evasion Attacks without Retraining](https://arxiv.org/abs/2608.03101)

- **한 줄 요약**: 재학습 없이 deep perceptual hash 기반 near-duplicate 매칭을 적대적 회피 공격에 견고화하는 plug-in 방어(DualShield).
- **핵심 기여**: 시각적으로 유사한 이미지를 가까운 표현으로 매핑하는 deep perceptual hash가 적대적 perturbation으로 매칭을 회피당하는 문제를 다룬다. 매칭 시점의 randomized smoothing(perturbed reference-query 쌍에 대한 결정 집계)과 게시 시점의 hardening(reference 이미지에 최적화된 미세 perturbation 추가)을 결합해 certified·empirical 견고성을 동시에 제공한다. 8개 perceptual hash·3개 데이터셋에서 낮은 충돌률을 유지한 채 white/black-box 및 변형 공격 성공률을 크게 낮췄다.
- **태그**: image-retrieval, image-embedding, adversarial-robustness

---

### [Keep the Needle, Prune the Haystack: Defect-Preserving Token Pruning for Efficient Zero-Shot Anomaly Detection](https://arxiv.org/abs/2608.03681)

- **한 줄 요약**: 작은 결함 토큰을 보존하며 정상 토큰만 공격적으로 잘라내 CLIP 기반 zero-shot anomaly detection을 최대 7.9배 가속하는 프레임워크(KeepAD).
- **핵심 기여**: 정상 샘플이 지배적이고 이상은 작은 영역에만 존재하는데도 모든 토큰에 dense 연산을 하는 비효율을, "정상 토큰 제거=중복 연산 절감 / 이상 토큰 제거=탐지 근거 소실"이라는 비대칭 pruning 위험으로 정식화했다. 얕은 레이어에서는 2×2 이웃 커버리지 보존 + 결정적 anomaly rescue로 미세 결함 손실을 막고, 깊은 레이어에서는 frozen 정상/이상 프로토타입으로 image-adaptive 예산 하에 저위험 정상 토큰을 제거한다. 산업 6개·의료 7개 벤치마크에서 토큰 유지율 20% 미만에서도 image/pixel-level AUROC 저하를 평균 2.7%p 이내로 억제했다.
- **태그**: anomaly-detection, defect-detection, efficient-inference, industrial-inspection

---

### [FakeI2V-Bench: Benchmarking the Applicability of Image-level Deepfake Detectors for Deepfake Video Detection](https://arxiv.org/abs/2608.03096)

- **한 줄 요약**: image-level deepfake detector를 비디오 도메인에 적용·집계하는 프레임워크(IV-Bridge)와 97,548개 영상 규모의 딥페이크 탐지 벤치마크.
- **핵심 기여**: 최신 생성모델 콘텐츠를 폭넓게 담아 8개 video-level·12개 image-level detector를 체계적으로 평가했고, 최상위 image-level detector(80.16% AUC)가 최강 video-level detector(79.99%)를 근소하게 앞서는 것을 확인했다. 프레임 단위 예측을 통계 feature 기반 random forest로 집계하는 IV-Bridge를 제안해 11개 image-level detector가 SOTA video-level 기법을 상회하도록 만들었고, 최적 변형은 93.80% AUC를 달성했다. image-level 탐지기를 비디오로 확장하는 실질적 경로를 제시한다.
- **태그**: forgery-detection, dataset-benchmark, video

---

### [MuRA: Multi-Rank Adaptation for Efficient and Effective Test-Time Vision-Language Generalization](https://arxiv.org/abs/2608.03885)

- **한 줄 요약**: 고정 rank의 LoRA 한계를 극복해 입력의 시각 복잡도에 따라 adaptation 모듈 rank를 동적으로 선택·융합하는 test-time PEFT.
- **핵심 기여**: 고정 rank가 복잡한 장면에는 underfitting, 단순한 장면에는 overfitting을 강제한다는 병목을 지적하고, token-level 시각 복잡도에 따라 서로 다른 capacity의 adaptation 모듈을 동적으로 고르고 융합하는 MuRA를 제안한다. knowledge-preserving 초기화를 위한 Multi-Rank Orthogonal Decomposition과 continuous router로 semantic-to-rank 매핑을 지속 학습하는 Unified Component Fusion을 결합했다. 가장 깊은 visual layer에서 가장 짧은 gradient 경로를 활용해 계산·메모리 부담을 줄이며 도메인 일반화·cross-dataset에서 SOTA를 달성했다.
- **태그**: peft, vlm, foundation-model

---

### [Low-Dimensional High-Leverage Subspace Optimization: Beyond Full-Parameter Coupled Training for Neural Network Quantization](https://arxiv.org/abs/2608.03919)

- **한 줄 요약**: normalization affine 파라미터만 조정해 compact 네트워크의 저비트 양자화 정확도 붕괴를 회복하는 부분공간 최적화(NAP).
- **핵심 기여**: 저비트 양자화가 compact 네트워크에서 심하게 무너지는 원인을 전체 파라미터를 함께 학습하는 monolithic paradigm의 gradient coupling으로 진단하고, quantization 견고성을 지배하는 저차원 고레버리지 부분공간으로 normalization affine 파라미터를 지목한다. PTQ에서는 backbone을 freeze하고 fake-quant 그래프 아래 affine만 튜닝해 quantization friendliness를 선제적으로 높이고, QAT에서는 QAT-NAP 교대 스케줄로 feature 학습과 numerical calibration을 분리한다. 이론적으로 BN affine이 채널별 affine 왜곡을 상쇄함을 보였고 ImageNet·CIFAR-100에서 무너진 저비트 양자화를 회복시켰다.
- **태그**: quantization, efficient-inference, distillation

---

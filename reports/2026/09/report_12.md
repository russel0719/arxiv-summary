# arXiv cs.CV Daily Digest — 2026-09-11 (arXiv 공개일)

- **전체 신규 논문 수**: 89편 (new 75 + cross-list 14)
- **선별 수**: 10편

## 오늘의 트렌드

가장 두꺼운 군집은 생성·편집 모델과 그 평가로, 확산 transformer 제어·비디오 생성·통합 멀티모달 모델과 물리 일관성·조명 이해를 묻는 벤치마크가 함께 올라왔다. 의료 영상(분할·복원·정합)이 두 번째, 3D 재구성·Gaussian Splatting과 point cloud·radar 등 비(非)2D 입력 계열이 세 번째다. VLM 평가·환각 진단, 그리고 동결 backbone 위의 soft prompt·LoRA·KV 캐시 양자화 같은 경량 적응·배포 최적화 흐름도 반복된다.

---

### [TailProp: content-adaptive light- and heavy-tailed propagation for vision](https://arxiv.org/abs/2609.11081)

**한 줄 요약**: Gaussian(경꼬리)과 Cauchy(중꼬리) stable-process 전파를 상보적 basis로 두고 내용에 따라 채널별 계수로 섞는 계층적 vision backbone.

**핵심 기여**: 전파 동역학을 명시적으로 모델링하는 science-inspired 비전 모델은 대개 하나의 동역학 계열 안에서만 전파를 구성·적응시키는데, 실제 시각 표현은 샘플·채널·네트워크 단계마다 상당히 다른 공간적 상호작용을 요구한다는 문제의식에서 출발한다. Tail Propagation Operator(TPO)는 빠르게 감쇠하는 Gaussian 전파자와 중꼬리 Cauchy 전파자를 두 basis로 삼고, 내용 조건부 채널별 계수를 예측해 둘을 결합한다. 이 계수가 공간적으로 공유되기 때문에 두 응답을 DCT/IDCT 한 쌍만으로 DCT 도메인에서 직접 합성할 수 있어, 정방형 특징맵(N=HW)·고정 채널 폭 기준 O(N^1.5) 공간 혼합이 된다. TailProp-B는 ImageNet-1K Top-1 84.4%, Mask R-CNN 3x 스케줄에서 box/mask AP 50.3/44.8, ADE20K mIoU 50.8%를 기록하며, ablation에서 단일 basis·동일 계열 추가 branch·계열 내 적응만으로는 이득이 설명되지 않는다고 보고한다.

**코드**: 불명

**태그**: ssl-backbone, foundation-model, object-detection, segmentation, efficient-inference

---

### [FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation](https://arxiv.org/abs/2609.11486)

**한 줄 요약**: correlation volume·feature warping·반복 정제 같은 flow 전용 구성요소를 전부 제거하고, 세 종류의 attention만으로 구성한 단일 feed-forward encoder–decoder optical flow 모델.

**핵심 기여**: 기존 optical flow 방법은 correlation volume, feature warping, iterative refinement 같은 과제 특화 inductive bias에 정확도를 의존하는데, 이런 bias가 모델을 사전 정의된 휴리스틱에 묶어 표현력을 제한하고 파이프라인과 연산 비용을 키운다고 지적한다. FreeFlow는 flow 전용 모듈 없이 지역 처리용 window attention, window 간 정보 교환용 shifted-window attention, 축소 해상도에서 동작하는 global attention 세 가지만 조합한 계층적 transformer로 구성되며, 용량을 키울수록 정확도가 일관되게 오르는 스케일링을 보인다. Sintel Clean/Final EPE 0.68/1.48, KITTI-2015 Fl-all 3.23, Spring 1px 3.192로 주요 벤치마크 state-of-the-art를 달성하면서 1080p 추론에서 메모리 효율을 유지한다고 보고한다.

**코드**: 불명

**태그**: correspondence, feature-matching, optical-flow, foundation-model

---

### [Prototype Matters: Modality-unified Prototype Self-distillation for Unsupervised Visible-infrared Person Re-identification](https://arxiv.org/abs/2609.11514)

**한 줄 요약**: cross-modality 대조 대신 modality 통합 prototype 대조와 prototype 기반 self-distillation으로, 라벨 없는 가시광–적외선 person re-ID의 modality 불변 표현을 학습한다.

**핵심 기여**: 비지도 visible-infrared re-ID에서 optimal transport는 실용적인 cross-modality 연관 추정 수단이지만 hard label 할당이 경직돼 클러스터 잡음의 영향을 고려하지 못하고, cross-modality 대조만 강제하면 modality 내부와 modality 간 유사도 관계를 함께 최적화하지 못해 차선에 머문다는 문제를 제기한다. 제안 프레임워크는 cross-modality prototype과 대조하는 대신 modality 통합 prototype 대조를 써서 두 유사도 관계를 동시에 최적화하고, 자기 prototype을 안정적인 teacher로 삼아 instance–prototype 온라인 관계를 self-distillation으로 정제한다. 두 요소는 하나의 프레임워크에서 함께 최적화되며, 표준 VI-ReID 벤치마크에서 광범위한 비교·분석으로 효과를 검증한다.

**코드**: 공개([PoSeD](https://github.com/Terminator8758/PoSeD))

**태그**: re-identification, metric-learning, image-embedding, distillation

---

### [HiPerViT: A Hierarchical Perceiver-Vision Transformer Architecture for Multi-Scale Texture Recognition](https://arxiv.org/abs/2609.10917)

**한 줄 요약**: bilinear 2차 통계를 하나의 statistical token으로 인코딩해 Perceiver 방식 latent distillation으로 공간 token과 상호작용시키는, 비전 전용 texture 인식 아키텍처.

**핵심 기여**: texture 인식의 판별 근거는 물체 형태보다 고차 공간 통계에 실려 있는데, Vision Transformer의 표준 object-centric 표현은 그런 통계 구조를 명시적으로 드러내지 않아 fine-grained 설정에서 texture 민감도가 떨어진다는 문제의식에서 출발한다. HiPerViT는 전역·지역 view를 함께 쓰고 compact bilinear descriptor를 statistical token으로 인코딩한 뒤, Perceiver 스타일 latent distillation으로 1차 공간 표현과 통합해 멀티모달 사전학습이나 앙상블 없이 2차 공존 통계에 직접 접근하게 한다. 여섯 개 texture 벤치마크에서 vision-only 베이스라인 대비 DTD +3.05%p, GTOS-Mobile +10.48%p, 1200Tex +10.10%p의 향상을 보고하며, 2차 통계를 뽑는 backbone 깊이와 상호작용·distillation 단계 순서를 바꿔도 이득이 대체로 유지돼 특정 fusion 위상보다 2차 통계의 명시적 제공 자체가 이득의 원천이라고 분석한다.

**코드**: 불명

**태그**: fine-grained, image-embedding, texture-recognition, foundation-model

---

### [Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models](https://arxiv.org/abs/2609.11310)

**한 줄 요약**: 항공·산업·의료 등 도메인 외 few-shot object detection에서, 동결된 VLM에 연속 prompt token 1~3개만 학습시켜 LoRA 최고 설정과 동등한 정확도를 내면서 망각을 일으키지 않는다.

**핵심 기여**: 주석 이미지 10장만 주어지는 out-of-domain few-shot detection에서 기존 적응 방법은 이산 prompt 최적화와 LoRA 파인튜닝인데, 여기서는 backbone을 동결한 채 소수의 연속 prompt token만 최적화하는 soft prompting을 다시 검토한다. 두 가지 설계가 핵심으로, prompt token을 시각·텍스트 token 사이 cross-modal 경계에 두는 것이 다른 위치보다 낫고(10.0 대 8.4 mAP), empty space token으로 초기화하는 것이 의미 기반·무작위 초기화보다 낫다. 이 선택으로 평균 7,168개 파라미터에 해당하는 1~3개 token이 Roboflow20-VL 10-shot에서 최고 LoRA 설정과 같은 14.2 mAP에 도달하며 학습 파라미터는 2만 배 이상 적다. 동일 정확도의 LoRA rank가 NaturalBench VQA 정확도를 상대 35%(최대 rank에서 56%) 떨어뜨리는 것과 달리 soft prompting은 사전학습 성능을 그대로 두고, 학습된 token은 재학습 없이 다른 모델로 전이되며(Qwen3.5-9B +0.8 mAP) 읽을 수 있는 prompt로 언어화된다. 다만 seed 간 분산이 커 최적화가 더 어렵다는 한계를 함께 보고한다.

**코드**: 불명

**태그**: peft, open-vocab-detection, vlm, foundation-model, continual-learning

---

### [LAION-Mobile: Evaluating Deepfake Detectors On One Million Smartphone Photos](https://arxiv.org/abs/2609.11134)

**한 줄 요약**: 최신 스마트폰의 neural ISP로 촬영된 실사진 100만 장 규모 데이터셋에서 deepfake 검출기 12종을 재평가해, 임계값 재적합 시 실사진 오경보율이 17~91%까지 치솟음을 보인다.

**핵심 기여**: 대부분의 deepfake 검출기는 자체 벤치마크에서 AUC가 거의 완벽하다고 보고하지만, 다중 센서 융합·잡음/모션 블러 억제 같은 on-device neural ISP가 촬영을 단순 광학 투영에서 계산 사진술로 옮기면서 일반 폰 사진이 가짜로 판정될 위험이 커진다는 가설을 대규모로 검증한다. re-LAION-5B에서 EXIF 메타데이터를 갖춘 약 100만 장의 스마트폰 이미지를 정제해 LAION-Mobile을 구축하고, 원 논문 체크포인트를 그대로 쓴 검출기 12종을 9,115장 평가 표본(DIRE는 738장)에서 측정한다. 결과는 (i) 최신 AI 생성물에서 AUC가 0.624를 넘는 검출기가 없고 12개 중 5개는 우연 수준 이하, (ii) 실사진 오경보율은 임계값 캘리브레이션의 산물로, 레거시 GAN 데이터에 맞춘 임계값에서는 FPR 11% 미만처럼 보이던 검출기가 동일 기준을 최신 콘텐츠에 재적합하면 실사진의 17~91%를 가짜로 표시, (iii) 최신 AI 생성물에서 우연을 넘으면서 배포 가능한 오경보율을 유지하는 검출기는 없다는 것이다. 말뭉치가 웹 수집물의 기기 분포를 따르는 탓에 1세대 neural ISP(2018–2020) 위주이고 현행 플래그십은 사실상 빠져 있어, 최신 ISP 영역은 미해결로 남는다고 밝힌다.

**코드**: 불명

**태그**: forgery-detection, calibration, dataset-benchmark, sim2real

---

### [A Multi-View and Confusion-Guided Ensemble Framework for Robust Synthetic Image Attribution](https://arxiv.org/abs/2609.11188)

**한 줄 요약**: FFT-ConvNeXt·DINOv2·CLIP·Xception을 주파수·의미·포렌식 관점으로 앙상블하고, 혼동 쌍 전용 이진 전문가와 클래스 적응 신뢰도 캘리브레이션을 더한 생성 모델 출처 판별 시스템.

**핵심 기여**: 생성 이미지의 출처 모델을 식별하는 synthetic image attribution은 최신 diffusion 생성기들이 서로 비슷해지고 다양한 후처리가 섞이면서 난도가 높아졌다는 문제에서 출발한다. ICANN 2026 DLMMDD 워크숍 챌린지 제출 시스템으로, 주파수·의미·포렌식 단서를 각각 포착하는 네 아키텍처를 결합하고 압축·리사이즈·grayscale 변환·블러 같은 현실적 후처리를 모사하는 광범위한 증강으로 미지의 열화에 대한 강인성을 높인다. 앙상블의 혼동 패턴 분석에서 Stable Diffusion 3와 3.5 사이 심한 모호성을 확인하고, 신뢰도가 낮을 때만 선택적으로 작동하는 전용 이진 전문가 분류기를 도입했으며, Tencent Hunyuan 같은 까다로운 클래스에는 클래스 적응 신뢰도 캘리브레이션을 적용한다. public 리더보드 99.53%, private 99.20%를 기록했다.

**코드**: 공개([SIA](https://github.com/ZOMIN28/SIA))

**태그**: forgery-detection, calibration, image-embedding, foundation-model

---

### [Vision Transformer-Based Multi-Level Feature Fusion for Multi-Label Sewer Defect Classification](https://arxiv.org/abs/2609.11375)

**한 줄 요약**: 하수관 결함의 다중 라벨 분류를 위해 다단계 특징 융합 계층적 ViT와 경량 변형 두 종을 만들어, Sewer-ML에서 정확도와 연산량을 함께 다룬다.

**핵심 기여**: 하수관 결함 자동 분류는 인프라 상태 평가에 필수지만 기존 딥러닝 방법은 대규모 다중 라벨 상황에서 정확도와 연산 복잡도의 균형을 맞추기 어렵다는 문제를 제기한다. 다단계 특징 융합을 적용한 계층적 vision Transformer인 Sewer-Transformer-ML과, 자원 제약 점검 환경을 위한 Sewer-MobileNet-ML·Sewer-Mobile-TransNet을 함께 제시한다. Sewer-ML 테스트셋에서 Sewer-Transformer-ML-Base가 F2_CIW 65.68%, F1_Normal 92.68%로 공개 리더보드 1위이자 2위 대비 F2_CIW 7.6%p 우위를 보이고, Sewer-MobileNet-ML은 17M 파라미터(기본 모델 대비 약 95% 감축)로 F2_CIW 65.73%를 낸다. 학습셋을 1,177장으로 줄였을 때 Sewer-ML 사전학습이 일관되게 성능을 높였고, ablation에서 Transformer 특징에는 직접 concat이, 다중 스케일 CNN 특징에는 attention 기반 융합이 더 효과적이었다고 보고한다.

**코드**: 불명

**태그**: defect-detection, industrial-inspection, efficient-inference, fine-grained

---

### [Are We Really Doing Few-Shot Learning? A Critical Examination of Pre-Training Assumptions](https://arxiv.org/abs/2609.10851)

**한 줄 요약**: few-shot 평가에서 관례인 클래스 분리 in-domain 사전학습이 대상 도메인 정보를 남겨 성능을 9.66%p 낙관 편향시킨다는 것을 여덟 데이터셋에 걸쳐 정량화한다.

**핵심 기여**: few-shot 학습은 보통 대상 에피소드와 클래스가 겹치지 않지만 같은 시각 도메인에서 온 대규모 보조 집합으로 사전학습하는 프로토콜로 평가되는데, 이것이 실제 저데이터 학습을 반영하는지 묻는다. 사전학습 없음, 클래스 분리 in-domain, 지도 out-of-domain, 라벨 없는 out-of-domain 네 조건을 여덟 데이터셋·세 few-shot 아키텍처·여러 way-shot 설정에서 비교한 결과, 클래스 분리만으로는 대상 도메인 데이터의 영향을 제거하지 못해 in-domain 사전학습이 평균 33.41%p, 지도 out-of-domain이 23.75%p 향상을 주어 도메인 중첩에 기인한 9.66%p의 낙관 편향이 드러난다. 증강 기반 라벨 없는 전략이 평균 27.71%p로 지도 out-of-domain(27.97%p)에 근접해 라벨된 소스 데이터가 필수는 아님을 보이고, 사전학습 전에 소스 도메인 적합도를 추정하는 descriptor 기반 소스 선택 전략은 oracle 선택과의 중앙값 격차가 1.37%p에 그친다. out-of-domain 사전학습의 효과는 소스–타깃 도메인 호환성에 크게 의존한다는 한계를 함께 밝힌다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, dataset-benchmark, calibration

---

### [When is Test-Time Adaptation Identifiable From Unlabeled Evidence?](https://arxiv.org/abs/2609.11235)

**한 줄 요약**: 라벨 없는 증거만으로 어떤 test-time adaptation을 적용할지 고를 수 있는지를 식별 가능성 문제로 정식화하고, 완벽한 선택기로도 결정이 불가능한 경계를 규명한다.

**핵심 기여**: test-time adaptation은 라벨 없이 배포 모델을 갱신하는 여러 방법을 제공하지만 잘못된 갱신은 강한 소스 모델을 오히려 악화시키며, 최근 방법들은 라벨 없는 테스트 데이터로 어떤 적응이 통할지 예측하려 한다. 이 논문은 그 앞 단계 질문으로 선택기에 주어지는 증거가 애초에 최적 행동을 결정할 만큼의 정보를 담고 있는지 묻고, 관측 채널이 서로 다른 TTA 순위를 가진 두 배포를 동일하게 보이게 만들면 해당 채널로는 신뢰할 만한 선택이 불가능하며 관련 모호성을 해소하는 더 풍부한 증거가 있을 때만 결정이 복원된다는 것을 보인다. 유한 배치 Gaussian TTA 모델에서 이 경계를 정확히 규정해, 작은 shift에서는 아무것도 하지 않는 쪽이 평균 재중심화보다 낫고 고유한 임계 shift를 넘으면 재중심화가 이기며 경계가 1/√n로 줄어듦을 유도한다. CIFAR-100-C와 DomainNet-126의 공개 벤치마크 연구에서도 최신 TTA 방법들이 같은 실패 양상을 보여, 배포 구조만 바꿔도 oracle 행동이 뒤집히는 반면 순서에 둔감한 전역 증거는 변하지 않는다. 이로써 약한 선택기와 애초에 결정을 뒷받침할 수 없는 정보 채널이라는 두 실패 양상을 분리할 수 있다.

**코드**: 불명

**태그**: calibration, continual-learning, dataset-benchmark, foundation-model

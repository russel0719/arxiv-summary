# CV 연구 동향 보고서 — 2026-04-21

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| Diffusion Model Optimization | 학습 효율성 및 최적화 불안정성 해결 | Guiding Distribution Matching Distillation with Gradient-Based Reinforcement Learning |
| 3D Reconstruction & Editing | 희소 시점 데이터에서의 기하학적 일관성 확보 | AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model |
| Generative Control & Simulation | 물리적 타당성과 시공간적 일관성 유지 | CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis |

> 핵심 메시지: 확산 모델의 효율적 증류와 물리적 제약이 내재된 3D/비디오 생성 기술이 시각적 생성 AI의 실용성을 극대화하고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Generation | 패치 단위 적응형 샘플링 및 다중 보상 목표 최적화 | Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling |
| 3D Reconstruction | 인간-장면 상호작용 및 희소 시점 기반 3D 복원 | GRAFT: Geometric Refinement and Fitting Transformer |
| Segmentation | 의료 영상 분할을 위한 효율적 계층적 트랜스포머 | RF-HiT: Rectified Flow Hierarchical Transformer |
| Video Synthesis | 물리적 제약 조건 내재화 및 지리적 데이터 결합 | CityRAG: Stepping Into a City via Spatially-Grounded Video Generation |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Diffusion Transformer (DiT) | 다중 모달 제어 및 물리적 일관성 있는 영상 생성 | MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation |
| Reinforcement Learning for Distillation | 확산 모델의 증류 과정 최적화 및 신용 할당 | Learning to Credit the Right Steps: Objective-aware Process Optimization |
| Optimal Transport | 3D Gaussian Splatting의 의미론적 편집 및 정렬 | TransSplat: Unbalanced Semantic Transport for Language-Driven 3DGS Editing |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| Autonomous Driving & Robotics | 지리적 데이터와 RAG를 결합한 고충실도 도시 시뮬레이션 | 실제 데이터 수집 비용 절감 및 시뮬레이션 훈련 데이터 확장 |
| Medical Imaging | Rectified Flow 기반의 고효율 의료 영상 분할 | 임상 환경에서의 실시간 배포 및 진단 정확도 향상 |

---

## 5. 개별 논문 요약

### 1. GRAFT: Geometric Refinement and Fitting Transformer for Human Scene Reconstruction

- **arXiv**: https://arxiv.org/abs/2604.19624
- **Score**: 8.2 / 10
- **한줄 요약**: GRAFT는 인간-장면 상호작용(HSI) 재구성에서 최적화 기반 방식의 정확도와 피드포워드 방식의 속도 사이의 절충안을 해결하기 위해, 기하학적 피드백을 활용한 반복적 정제(Iterative Refinement) 트랜스포머를 제안합니다.
- **핵심 기여**: 기존 최적화 방식 대비 50배 빠른 속도로 물리적 타당성을 확보했으며, 기존 모델에 추가 학습 없이 결합 가능한 범용적 기하학적 사전(Plug-and-play prior)으로 활용 가능합니다.
- **방법론 개요**: 신체 중심 토큰과 장면의 기하학적 정보를 샘플링하는 'Geometric Probes'를 사용하여, 반복적인 트랜스포머 구조를 통해 인간 메쉬를 수정하는 보정값(Interaction Gradients)을 예측하고 물리적 정합성을 높입니다.
- **의의**: 기존의 느린 최적화 방식이나 부정확한 피드포워드 방식의 한계를 극복하여, 복잡한 실내 환경에서도 빠르고 물리적으로 자연스러운 3D 인간-장면 상호작용 재구성을 가능하게 합니다.

### 2. Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation

- **arXiv**: https://arxiv.org/abs/2604.19141
- **Score**: 8.2 / 10
- **한줄 요약**: 이미지 생성 과정에서 모든 영역을 동일하게 처리하는 대신, 패치 단위로 난이도를 평가하고 연산 자원을 차등 할당하는 적응형 생성 프레임워크인 Patch Forcing(PF)을 제안합니다.
- **핵심 기여**: 패치 단위의 노이즈 스케줄링과 난이도 기반의 적응형 샘플링을 도입하여, 생성 품질을 높이는 동시에 효율적인 연산 자원 배분을 가능하게 했습니다.
- **방법론 개요**: 패치별 난이도를 예측하는 헤드를 통해 쉬운 영역은 빠르게 디노이징하여 컨텍스트를 생성하고, 이를 어려운 영역의 디노이징에 활용하는 공간-시간적 적응형 샘플링 방식을 사용합니다.
- **의의**: 기존의 획일적인 디노이징 방식에서 벗어나 이미지 내 공간적 이질성을 활용함으로써, 생성 모델의 효율성과 품질을 동시에 개선할 수 있는 새로운 연구 방향을 제시합니다.

### 3. Guiding Distribution Matching Distillation with Gradient-Based Reinforcement Learning

- **arXiv**: https://arxiv.org/abs/2604.19009
- **Score**: 7.8 / 10
- **한줄 요약**: GDMD는 확산 모델 증류(Diffusion Distillation) 과정에서 발생하는 최적화 불안정성을 해결하기 위해, 원시 샘플 기반의 보상 대신 증류 그래디언트를 활용하는 강화학습 프레임워크입니다.
- **핵심 기여**: 기존의 노이즈 섞인 샘플 평가 방식을 그래디언트 수준의 가이드로 대체하여, 4단계 생성 모델에서 교사 모델을 능가하는 성능과 최첨단(SOTA) 수준의 생성 품질을 달성했습니다.
- **방법론 개요**: DMD(Distribution Matching Distillation)의 최적화 그래디언트를 강화학습의 보상 신호로 재해석하여, 정책 최적화 과정에서 증류 목표와 정렬되도록 적응형 가중치를 부여하는 방식을 사용합니다.
- **의의**: 기존 증류 방식의 고질적 문제인 최적화 충돌과 초기 학습의 불안정성을 극복함으로써, few-step 생성 모델의 효율성과 품질을 동시에 확보할 수 있는 확장 가능한 새로운 학습 패러다임을 제시했습니다.

### 4. CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation

- **arXiv**: https://arxiv.org/abs/2604.19636
- **Score**: 7.5 / 10
- **한줄 요약**: CoInteract는 인간-객체 상호작용(HOI) 영상 생성 시 발생하는 구조적 붕괴와 물리적 오류를 해결하기 위해, 구조적 제약 조건을 내재화한 통합형 확산 트랜스포머(DiT) 프레임워크를 제안합니다.
- **핵심 기여**: 인간의 손과 얼굴 등 민감한 영역을 전문적으로 처리하는 '인간 인식 MoE(Mixture-of-Experts)'와 학습 시에만 활용되는 '이중 스트림 구조'를 통해 추론 비용 증가 없이 물리적으로 타당하고 구조적으로 안정적인 영상을 생성합니다.
- **방법론 개요**: RGB 영상 생성 스트림과 보조적인 HOI 구조 스트림을 병렬로 학습시키는 '공동 생성(Co-Generation)' 패러다임을 채택하고, 특정 영역에 토큰을 할당하는 공간적 라우팅 메커니즘을 통해 세밀한 표현력을 확보합니다.
- **의의**: 기존 영상 생성 모델의 고질적인 문제인 손-객체 간의 관통 현상이나 구조적 왜곡을 효과적으로 해결함으로써, 단순한 아바타 생성을 넘어 제품 시연 등 정교한 상호작용이 필요한 산업 분야에 실질적인 해결책을 제시합니다.

### 5. RF-HiT: Rectified Flow Hierarchical Transformer for General Medical Image Segmentation

- **arXiv**: https://arxiv.org/abs/2604.19570
- **Score**: 7.5 / 10
- **한줄 요약**: 의료 영상 분할을 위한 효율적이고 고품질의 생성 모델 개발
- **핵심 기여**: 기존 확산 모델의 계산 병목 현상을 해결하고, 적은 추론 단계로도 높은 정확도의 분할 결과를 생성하는 Rectified Flow 기반의 계층적 트랜스포머 아키텍처 (RF-HiT) 제시
- **방법론 개요**: Hourglass Transformer 백본과 Rectified Flow를 통합하여, 고해상도에서는 효율적인 이웃(neighborhood) 어텐션을, 저해상도 병목 구간에서는 전역(global) 어텐션을 사용합니다. 또한, 별도의 특징 인코더를 통해 다중 스케일 해부학적 특징을 추출하여 생성 과정에 통합합니다.
- **의의**: 의료 영상 분할에서 효율성과 성능 간의 균형을 개선하여, 임상 환경에서의 실시간 또는 준실시간 배포를 가능하게 하고, 더 작고 가벼운 모델로도 최첨단 성능을 달성할 수 있습니다.

### 6. AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model

- **arXiv**: https://arxiv.org/abs/2604.19747
- **Score**: 7.2 / 10
- **한줄 요약**: AnyRecon은 비디오 확산 모델과 명시적 3D 기하학적 메모리를 결합하여, 임의의 순서 없는 희소 시점 입력으로부터 고품질의 3D 장면을 재구성하는 프레임워크입니다.
- **핵심 기여**: 기존 이미지 기반 생성 모델의 한계를 넘어, 비디오 생성의 시간적 일관성과 명시적 기하학적 제어를 통합함으로써 대규모 장면에서도 높은 공간적 일관성과 확장성을 확보했습니다.
- **방법론 개요**: 비디오 확산 모델을 기반으로 하며, 1) 기하학적 정보를 포함한 전역 장면 메모리 활용, 2) 희소 주의(sparse attention)를 통한 효율적 연산, 3) 생성과 재구성이 반복되는 폐루프(closed-loop) 통합 방식을 사용합니다.
- **의의**: 기존의 NeRF나 3DGS가 요구하는 조밀한 다중 시점 데이터 없이도, 실생활의 불규칙하고 희소한 데이터로부터 정교한 3D 환경을 복원할 수 있게 하여 3D 재구성의 실용성과 확장성을 크게 향상시켰습니다.

### 7. CityRAG: Stepping Into a City via Spatially-Grounded Video Generation

- **arXiv**: https://arxiv.org/abs/2604.19741
- **Score**: 7.2 / 10
- **한줄 요약**: CityRAG는 검색 증강 생성(RAG)과 지리적 데이터를 결합하여, 실제 도시 환경의 물리적 구조를 유지하면서도 시간적 일관성을 갖춘 장시간 비디오를 생성하는 세계 모델입니다.
- **핵심 기여**: 기존의 정적인 3D 재구성 방식(NeRF 등)의 한계를 넘어, 지리적 기반의 정적 환경과 가변적인 동적 요소를 분리하여 물리적으로 정확하고 제어 가능한 도시 시뮬레이션을 구현했습니다.
- **방법론 개요**: 지리적으로 정렬된 데이터셋에서 정보를 검색(Retrieval)하고, 카메라 궤적과 첫 프레임의 시각적 정보를 조건부 입력으로 사용하여, 정적 환경 구조와 동적 속성을 분리(Disentanglement)하는 확산 모델 기반의 생성 프레임워크입니다.
- **의의**: 자율주행, 로봇 공학 등 물리적 정확성이 필수적인 분야에서 대규모 실제 데이터 수집 없이도 고충실도의 가상 환경을 생성하여 훈련 데이터의 확장성과 시뮬레이션 효율성을 획기적으로 높일 수 있습니다.

### 8. MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation

- **arXiv**: https://arxiv.org/abs/2604.19679
- **Score**: 6.8 / 10
- **한줄 요약**: 다양한 시각적·청각적 제어 신호를 단일 확산 트랜스포머(DiT) 프레임워크에 통합하여, 정교하게 제어 가능한 오디오-비디오 동시 생성 기술을 제안함.
- **핵심 기여**: 시각적 구조, 캐릭터 정체성, 음성 음색을 동시에 제어할 수 있는 통합 다중 모달 제어 아키텍처를 구축하고, 사전 학습된 모델의 성능을 유지하면서 정밀한 교차 모달 정렬을 달성함.
- **방법론 개요**: 다중 모달 제어 유닛(MMCU)을 통해 이질적인 입력 신호를 동기화하고, 이중 스트림 바이패스 구조와 모달리티별 가이던스 스케일링을 사용하여 생성 과정에 외부 제어 신호를 효과적으로 주입함.
- **의의**: 기존의 분리된 제어 방식이 가진 한계를 극복하여, 복잡한 시청각적 요구사항을 단일 파이프라인에서 일관성 있게 구현함으로써 생성형 AI의 제어 가능성과 실용성을 크게 향상함.

### 9. TransSplat: Unbalanced Semantic Transport for Language-Driven 3DGS Editing

- **arXiv**: https://arxiv.org/abs/2604.19571
- **Score**: 6.8 / 10
- **한줄 요약**: 3D Gaussian Splatting(3DGS) 기반의 텍스트 주도 3D 장면 편집을 위해, 다중 뷰 간의 불균형 최적 운송(Unbalanced Optimal Transport)을 활용한 의미론적 정렬 프레임워크를 제안합니다.
- **핵심 기여**: 기존의 픽셀 단위 융합 방식에서 벗어나, 의미론적 프로토타입과 최적 운송을 통해 2D 편집 결과와 3D 표현 간의 대응 관계를 명확히 정의함으로써 편집 정밀도와 다중 뷰 일관성을 획기적으로 개선했습니다.
- **방법론 개요**: 2D 편집 결과로부터 '프롬프트 인식 프로토타입'을 추출하여 의미론적 요약을 수행하고, 이를 3D 가우시안과 매핑하는 과정을 불균형 최적 운송 문제로 공식화하여 노이즈에 강건한 3D 편집 필드를 구성합니다.
- **의의**: 기존 방식의 고질적인 문제인 편집 누출(edit leakage)과 뷰 간 불일치를 해결하여, 복잡한 3D 장면에서도 언어 지시에 따른 정교하고 안정적인 국소적 수정이 가능하게 합니다.

### 10. Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation

- **arXiv**: https://arxiv.org/abs/2604.19234
- **Score**: 6.8 / 10
- **한줄 요약**: 확산 모델의 생성 과정에서 발생하는 다중 보상 목표를 시간 단계별로 세분화하여 최적화하는 OTCA(Objective-aware Trajectory Credit Assignment) 프레임워크 제안.
- **핵심 기여**: 기존 GRPO의 전역적 보상 할당 방식이 가진 한계를 극복하고, 시간 단계별 기여도와 다중 목표 보상을 결합한 정교한 신용 할당(Credit Assignment) 메커니즘을 정립함.
- **방법론 개요**: 확산 모델의 노이즈 제거 과정을 순차적 의사결정으로 정의하고, 각 단계의 중요도(Timestep Contribution)와 다중 보상 목표의 가중치(Reward Composition)를 결합하여 정책 업데이트를 위한 구조화된 신호를 생성함.
- **의의**: 시각적 생성 모델의 학습 효율성을 높이고, 품질·모션·텍스트 정렬 등 상충하는 다중 목표를 효과적으로 조정하여 최종 생성물의 품질을 비약적으로 향상시킴.

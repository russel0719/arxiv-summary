# CV 연구 동향 보고서 — 2026-05-20

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| Diffusion Model Optimization | 연산 효율성 및 추론 속도 개선 | RoPeSLR: 3D RoPE-driven Sparse-LowRank Attention for Efficient Diffusion Transformers |
| 3D/4D Scene Reconstruction | 기하학적 일관성 및 실시간 재구성 | ROAR-3D: Routing Arbitrary Views for High-Fidelity 3D Generation |
| Generative Control & Alignment | 편집성-충실도 트레이드오프 해결 | Semantic Granularity Navigation in Image Editing |

> 핵심 메시지: 확산 모델의 연산 효율화와 3D/4D 생성의 기하학적 일관성 확보를 위한 아키텍처 최적화 및 제어 프레임워크 연구가 주류를 이룸.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Generation | 이산 확산 모델의 단일 단계 증류 및 AR 모델의 사후 학습 최적화 | One-Step Distillation of Discrete Diffusion Image Generators via Fixed-Point Iteration |
| 3D/4D Reconstruction | 가우시안 스플래팅 기반의 물리적 일관성 확보 및 피드포워드 추론 | Towards Physically Consistent 4D Scene Reconstruction for Closed-loop Autonomous Driving Simulation |
| Image Restoration | 회귀와 생성 과정의 시간적 분리를 통한 제어 가능한 복원 | Disentangling Generation and Regression in Stochastic Interpolants for Controllable Image Restoration |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Adaptive Routing | Diffusion Transformer의 층간 정보 흐름 및 연산 자원 동적 배분 | Rethinking Cross-Layer Information Routing in Diffusion Transformers |
| Hybrid Architecture | 어텐션 맵의 희소-저랭크 분해를 통한 효율적 비디오 생성 | RoPeSLR: 3D RoPE-driven Sparse-LowRank Attention for Efficient Diffusion Transformers |
| Co-evolution Strategy | 정책 모델과 디코더의 공동 최적화를 통한 잠재 공변량 변화 해결 | RankE: End-to-End Post-Training for Discrete Text-to-Image Generation with Decoder Co-Evolution |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| Autonomous Driving | 4D 가우시안 스플래팅의 물리적 일관성 확보 | 자율주행 시뮬레이션의 신뢰성 및 시각적 안정성 향상 |

---

## 5. 개별 논문 요약

### 1. RoPeSLR: 3D RoPE-driven Sparse-LowRank Attention for Efficient Diffusion Transformers

- **arXiv**: https://arxiv.org/abs/2605.20659
- **Score**: 8.5 / 10
- **한줄 요약**: RoPeSLR은 확산 트랜스포머(DiT)의 3D RoPE와 선형 어텐션 간의 구조적 충돌인 'RoPE 딜레마'를 해결하기 위해, 어텐션 맵을 고주파 희소 성분과 저랭크 배경 성분으로 분해하는 하이브리드 아키텍처를 제안합니다.
- **핵심 기여**: 3D RoPE가 적용된 어텐션 맵이 희소-저랭크 구조를 가짐을 수학적으로 증명하고, 이를 통해 비디오 생성 품질 저하 없이 90% 이상의 희소성을 달성하여 연산 복잡도를 획기적으로 줄였습니다.
- **방법론 개요**: 어텐션 매니폴드를 고주파 의미론적 스파이크(희소 성분)와 저랭크 배경 연속체로 분리하고, 헤드별 저랭크 파라미터화와 학습 가능한 3D 절대 위치 임베딩 주입을 통해 상대적 거리 정보를 보존하는 하이브리드 방식을 사용합니다.
- **의의**: 기존 선형 어텐션이 가진 위치 정보 손실 문제를 해결하여, 초장기 비디오 생성 시 고해상도와 시간적 일관성을 유지하면서도 연산 효율성을 극대화할 수 있는 이론적·실용적 토대를 마련했습니다.

### 2. One-Step Distillation of Discrete Diffusion Image Generators via Fixed-Point Iteration

- **arXiv**: https://arxiv.org/abs/2605.21484
- **Score**: 8.2 / 10
- **한줄 요약**: 이산 확산 모델(Discrete Diffusion Models)을 위한 고정점 증류(Fixed-Point Distillation, FPD) 프레임워크를 제안하여, 복잡한 보조 네트워크 없이 단일 단계 추론으로 고품질 이미지 생성을 가능하게 함.
- **핵심 기여**: 보조 네트워크나 다단계 파이프라인 없이, 학생 모델의 출력을 교사 모델의 정제 결과와 일치시키는 '고정점 매칭' 방식을 통해 학습 효율성과 생성 품질을 동시에 달성함.
- **방법론 개요**: 학생 모델의 출력을 부분적으로 마스킹한 뒤 교사 모델로 정제하여 학습 타겟을 생성하고, 이산 토큰을 연속 특징 공간으로 변환하여 다중 대역 드리프트 손실(Multi-Bandwidth Drift Loss)과 Straight-Through Estimator(STE)를 통해 기울기를 역전파함.
- **의의**: 기존 이산 확산 모델의 고질적인 문제인 느린 반복 추론 속도와 복잡한 학습 파이프라인 문제를 해결하여, 실시간 고해상도 생성 모델의 실용성을 크게 향상함.

### 3. RankE: End-to-End Post-Training for Discrete Text-to-Image Generation with Decoder Co-Evolution

- **arXiv**: https://arxiv.org/abs/2605.21195
- **Score**: 8.2 / 10
- **한줄 요약**: 이산적 자기회귀(AR) 이미지 생성 모델에서 발생하는 '잠재 공변량 변화(Latent Covariate Shift)' 문제를 해결하고, 정책과 디코더를 공동 최적화하여 충실도와 정렬 성능을 동시에 향상시키는 프레임워크입니다.
- **핵심 기여**: 기존의 '고정된 디코더' 관행을 깨고, 랭킹 기반의 공동 진화(Co-evolution) 전략을 통해 이산적 생성 모델의 충실도와 정렬 사이의 트레이드오프를 해결했습니다.
- **방법론 개요**: 정책(AR 모델)과 디코더(VQ)를 교대로 업데이트하는 공동 최적화 전략을 사용하며, 비미분 가능한 양자화 병목을 우회하기 위해 상대적 랭킹 기반 목적 함수와 파라미터 안정화 앵커를 도입했습니다.
- **의의**: 기존 AR 모델의 한계였던 학습 분포와 추론 분포 간의 불일치를 해소함으로써, 강화학습 기반의 사후 학습 과정에서도 이미지 품질 저하 없이 텍스트 정렬 성능을 극대화할 수 있는 경로를 제시했습니다.

### 4. ROAR-3D: Routing Arbitrary Views for High-Fidelity 3D Generation

- **arXiv**: https://arxiv.org/abs/2605.21121
- **Score**: 8.2 / 10
- **한줄 요약**: ROAR-3D는 사전 학습된 단일 뷰 3D 생성 모델을 경량화된 아키텍처로 확장하여, 카메라 포즈 정보 없이도 임의의 다중 뷰 이미지를 입력받아 일관성 있는 3D 모델을 생성하는 프레임워크입니다.
- **핵심 기여**: 외부 재구성 모듈 없이 기존 모델의 사전 학습된 지식을 활용하여, 입력 뷰의 개수와 상관없이 고품질의 3D 형상을 생성하는 유연하고 효율적인 플러그 앤 플레이(plug-and-play) 방식을 제안했습니다.
- **방법론 개요**: 토큰 단위의 뷰 라우팅(View Routing)을 통해 입력 이미지와 3D 잠재 토큰을 동적으로 대응시키고, 이중 스트림 어텐션(Dual-Stream Attention)과 방향 섭동(Orientation Perturbation) 학습을 통해 포즈와 형상 정보를 분리하여 기하학적 일관성을 확보했습니다.
- **의의**: 기존 3D 생성 모델의 고질적인 문제인 단일 뷰의 모호성과 외부 모듈 의존성을 해결함으로써, 스케치나 비디오 등 다양한 비정형 입력으로부터 더욱 정교하고 신뢰도 높은 3D 자산을 생성할 수 있는 실용적인 경로를 제시했습니다.

### 5. Rethinking Cross-Layer Information Routing in Diffusion Transformers

- **arXiv**: https://arxiv.org/abs/2605.20708
- **Score**: 8.2 / 10
- **한줄 요약**: 기존 Diffusion Transformer(DiT)의 고정된 잔차 연결 구조가 디노이징 과정의 동적 특성을 반영하지 못하는 문제를 해결하기 위해, 타임스텝에 따라 적응적으로 정보를 전달하는 'Diffusion-Adaptive Routing(DAR)'을 제안함.
- **핵심 기여**: DiT의 고질적인 문제인 활성화 값 팽창, 그래디언트 소실, 층간 중복성을 진단하고, 이를 DAR 구조로 개선하여 학습 효율을 8.75배 향상시키며 생성 품질을 크게 개선함.
- **방법론 개요**: 기존의 단순 합산 방식인 잔차 연결을 학습 가능한 동적 라우팅 메커니즘으로 대체하여, 디노이징 타임스텝에 따라 층간 정보 흐름을 유연하게 조절하는 구조를 도입함.
- **의의**: 생성 모델의 아키텍처 설계에서 '층간 라우팅'이라는 새로운 최적화 축을 제시하였으며, 대규모 모델의 학습 가속화 및 고해상도 이미지 생성 품질 향상을 위한 모듈형 아키텍처로서 높은 범용성을 가짐.

### 6. Disentangling Generation and Regression in Stochastic Interpolants for Controllable Image Restoration

- **arXiv**: https://arxiv.org/abs/2605.21381
- **Score**: 7.8 / 10
- **한줄 요약**: DiSI(Disentangled Stochastic Interpolants)는 회귀(Regression)와 생성(Generation) 과정을 독립적인 시간 축으로 분리하여 이미지 복원(IR) 모델의 성능과 유연성을 극대화하는 프레임워크입니다.
- **핵심 기여**: 기존 생성 모델의 고질적인 문제인 '왜곡-지각(Distortion-Perception) 트레이드오프'를 해결하고, 단일 모델 내에서 회귀적 정확도와 생성적 사실성을 자유롭게 조절할 수 있는 통합 제어 메커니즘을 제공합니다.
- **방법론 개요**: 회귀 시간(r)과 생성 시간(g)이라는 두 개의 독립적인 시간 변수를 도입하여, 결정론적 매핑과 확률적 노이즈 주입을 분리된 벡터 필드로 학습하고 이를 단일 신경망으로 통합 추론합니다.
- **의의**: 복원 작업마다 별도의 모델을 구축할 필요 없이, 하나의 모델로 고충실도 복원과 고품질 텍스처 합성을 동시에 달성할 수 있어 이미지 복원 분야의 효율성과 범용성을 획기적으로 개선합니다.

### 7. Semantic Granularity Navigation in Image Editing

- **arXiv**: https://arxiv.org/abs/2605.21190
- **Score**: 7.8 / 10
- **한줄 요약**: NaviEdit은 확산 모델의 편집 과정에서 '편집 진행도'와 '노이즈 스케일 이동'을 분리하여, 최적의 의미론적 변화와 구조적 보존을 동시에 달성하는 훈련 없는 추론 시간 제어 프레임워크입니다.
- **핵심 기여**: 기존 편집 방식의 고질적인 문제인 '편집성-충실도 트레이드오프'를 해결하기 위해 스케일 의존적 의미론적 영역을 규명하고, 이를 기반으로 계산 자원을 효율적으로 재배치하는 '디커플링 제어 원리'를 제시했습니다.
- **방법론 개요**: 누설 압력(Leakage Pressure)과 진동 통계량(Oscillation Statistic)을 통해 모델의 '효과적인 스케일 윈도우'를 진단하고, 고정된 계산 예산을 파괴적인 고노이즈 영역 대신 의미론적으로 반응성이 높은 중간 스케일 영역에 집중시키는 적응형 탐색 방식을 사용합니다.
- **의의**: 추가적인 학습이나 외부 마스크 없이도 기존 생성 모델의 구조를 유지하면서 정교한 국소적 편집을 가능하게 하며, 고정된 연산 비용 내에서 편집 품질을 극대화할 수 있는 범용적이고 효율적인 제어 원리를 제공합니다.

### 8. Towards Physically Consistent 4D Scene Reconstruction for Closed-loop Autonomous Driving Simulation

- **arXiv**: https://arxiv.org/abs/2605.21032
- **Score**: 7.8 / 10
- **한줄 요약**: 4D 가우시안 스플래팅(4DGS)에서 발생하는 공간-시간 파라미터 간의 '신용 할당 딜레마(Credit Assignment Dilemma)'를 해결하기 위해, 공간과 시간 표현을 수학적으로 분리하는 계층적 최적화 프레임워크를 제안함.
- **핵심 기여**: 단일 궤적 관측에서 발생하는 '단일 관측 실패(SOF)' 현상을 이론적으로 규명하고, 직교 투영 경사(OPG) 기법을 통해 공간적 무결성을 유지하면서 시간적 역동성을 학습하는 새로운 최적화 메커니즘을 제시함.
- **방법론 개요**: 공간 파라미터를 먼저 고정하여 학습한 뒤, 시간 파라미터를 공간 파라미터의 영공간(null space)으로 투영하여 업데이트하는 계층적 학습 전략과 물리적 일관성을 위한 시간적 정규화 기법을 결합함.
- **의의**: 기존 4DGS 모델이 겪던 형태적 붕괴와 새로운 시점 합성(NVS) 성능 저하 문제를 해결하여, 자율주행 시뮬레이션 등 고도의 물리적 정확성과 시각적 안정성이 요구되는 분야에서 신뢰성 있는 4D 장면 재구성을 가능하게 함.

### 9. AIR: Amortized Image Reconstruction Framework for Self-Supervised Feed-Forward 2D Gaussian Splatting

- **arXiv**: https://arxiv.org/abs/2605.20820
- **Score**: 7.8 / 10
- **한줄 요약**: 2D Gaussian Splatting의 반복적인 최적화 과정을 단일 패스 피드포워드 추론으로 대체하여 실시간 이미지 재구성을 가능하게 하는 학습 기반 프레임워크입니다.
- **핵심 기여**: 이미지별 최적화 없이 고품질의 2D 가우시안 재구성을 달성했으며, 기존 방식의 계산 병목 현상을 제거하고 추론 속도를 160~300ms 수준으로 획기적으로 단축했습니다.
- **방법론 개요**: 단계별 잔차 예측(Stage-wise Residual Prediction)을 통해 가우시안 프리미티브를 점진적으로 추가하고, 예측-최적화-증류(Predict–Optimize–Distill) 전략을 통해 최적화된 가우시안 정보를 모델에 학습시키는 방식을 사용합니다.
- **의의**: 기존의 비용이 많이 드는 테스트 타임 최적화 문제를 해결함으로써, 고품질 이미지 표현과 고속 추론이라는 두 마리 토끼를 잡아 실용적인 이미지 재구성 파이프라인을 구축했습니다.

### 10. Spatial Gram Alignment for Ultra-High-Resolution Image Synthesis

- **arXiv**: https://arxiv.org/abs/2605.20808
- **Score**: 7.8 / 10
- **한줄 요약**: 사전 학습된 잠재 확산 모델(LDM)의 고유한 생성 능력을 훼손하지 않으면서, 비전 파운데이션 모델의 거시적 구조적 사전 지식을 효과적으로 통합하는 비침습적 프레임워크인 SGA(Spatial Gram Alignment)를 제안함.
- **핵심 기여**: 직접적인 특징 증류 시 발생하는 '학습 가능성-충실도 상충(Learnability-Fidelity Conflict)' 문제를 해결하여, 초고해상도 합성에서 구조적 일관성과 미세한 디테일 보존을 동시에 달성함.
- **방법론 개요**: 픽셀 단위의 직접적인 특징 정렬 대신, 생성 모델의 내부 특징과 파운데이션 모델의 특징 간 '자기 유사성 행렬(Gram matrix)'을 정렬하는 공간적 제약 메커니즘을 도입함.
- **의의**: 기존의 강제적인 특징 정렬 방식이 초래하던 생성 품질 저하를 방지함으로써, 대규모 사전 학습 모델의 성능을 유지하면서도 정교한 구조적 제어가 가능한 효율적인 파인튜닝 경로를 제시함.

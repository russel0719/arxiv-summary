# CV 연구 동향 보고서 — 2026-04-22

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| 3D Reconstruction & HOI | 물리적 정합성 및 데이터 의존성 해결 | LEXIS: LatEnt ProXimal Interaction Signatures for 3D HOI from an Image |
| Generative Efficiency | 연산 병목 해소 및 실시간 추론 최적화 | DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion |
| Multimodal Integration | 이해와 생성을 통합하는 단일 모델 아키텍처 | LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model |

> 핵심 메시지: 확산 모델의 효율적 추론 최적화와 멀티모달 통합을 통해 물리적 정합성을 갖춘 3D 생성 및 능동적 비전 시스템으로 진화하고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| 3D/HOI | 단일 이미지 기반의 3D 인간-객체 상호작용 및 장면 복원 | FurnSet: Exploiting Repeats for 3D Scene Reconstruction |
| Generation | 확산 모델을 활용한 비디오, 벡터 그래픽 및 다목적 제어 생성 | ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control |
| Vision-Language | 이산 확산 모델을 통한 멀티모달 이해 및 생성 통합 | LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Diffusion Transformers (DiT) | 멀티모달 데이터 처리 및 3D 기하학적 재조명 | GeoRelight: Learning Joint Geometrical Relighting and Reconstruction with Flexible Multi-Modal Diffusion Transformers |
| Sparse Attention & Caching | 장편 비디오 및 월드 모델 추론 가속화 | X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference |
| Self-Feedback/Active Vision | 시각적 피드백을 통한 생성 품질 향상 및 능동적 이미지 탐색 | Render-in-the-Loop: Vector Graphics Generation via Visual Self-Feedback |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| Robotics & Simulation | 생성형 모델을 활용한 물리적 제어 정책 학습 및 실시간 시뮬레이션 | 고가의 모션 캡처 데이터 없이 복잡한 조작 기술 습득 및 대규모 시뮬레이션 효율 증대 |
| Computer Graphics | 시각적 피드백 루프를 통한 벡터 그래픽 생성 | 기하학적 정확도 및 구조적 일관성 확보 |

---

## 5. 개별 논문 요약

### 1. LEXIS: LatEnt ProXimal Interaction Signatures for 3D HOI from an Image

- **arXiv**: https://arxiv.org/abs/2604.20800
- **Score**: 8.2 / 10
- **한줄 요약**: 단일 RGB 이미지로부터 3D 인간-객체 상호작용(HOI)을 재구성하기 위해, 이산적인 접촉 라벨 대신 연속적인 'InterField'와 이를 학습하는 'LEXIS' 잠재 공간을 활용하는 일원화된 확산 모델 프레임워크입니다.
- **핵심 기여**: 희소한 이진 접촉 모델링의 한계를 극복한 밀집 연속적 상호작용 표현(InterField) 도입, 상호작용 우선순위를 학습하는 LEXIS 잠재 매니폴드 구축, 그리고 이를 통한 추론 단계에서의 물리적 정합성 강화입니다.
- **방법론 개요**: VQ-VAE를 통해 상호작용 패턴을 학습한 LEXIS 잠재 공간을 구축하고, 확산 모델을 통해 인간과 객체의 메쉬를 공동 추론하며, 추론 과정에서 InterField를 가이드로 활용하여 별도의 사후 최적화 없이 물리적으로 타당한 결과를 생성합니다.
- **의의**: 기존의 2단계(추정 후 최적화) 방식이 가진 복잡성과 일반화 한계를 해결하고, 단일 이미지에서 고충실도의 3D 상호작용을 직접 생성함으로써 HOI 재구성의 정확도와 효율성을 획기적으로 개선했습니다.

### 2. ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control

- **arXiv**: https://arxiv.org/abs/2604.20816
- **Score**: 7.8 / 10
- **한줄 요약**: 다중 목적 강화학습(MORL)을 활용하여 확산 모델이 단일 모델 내에서 다양한 보상 간의 최적 균형(Pareto front)을 실시간으로 조절할 수 있도록 하는 프레임워크 제안.
- **핵심 기여**: 정적 가중치 합산(early scalarization)의 한계를 극복하고, 선호도 벡터를 조건부 입력으로 사용하여 추론 시점에 다목적 최적화 균형을 동적으로 제어할 수 있는 ParetoSlider 개발.
- **방법론 개요**: 확산 모델을 순차적 마르코프 결정 과정(MDP)으로 정의하고, 보상별 이점을 독립적으로 정규화한 후 선호도 벡터에 따라 가중치를 적용하는 '후기 스칼라화(late-scalarization)' 및 선호도 조건부 학습 기법 도입.
- **의의**: 여러 모델을 유지하거나 재학습할 필요 없이 단일 모델만으로 사용자 요구에 따른 정밀한 다목적 제어가 가능하여, 생성형 AI의 유연성과 효율성을 획기적으로 개선함.

### 3. GeoRelight: Learning Joint Geometrical Relighting and Reconstruction with Flexible Multi-Modal Diffusion Transformers

- **arXiv**: https://arxiv.org/abs/2604.20715
- **Score**: 7.8 / 10
- **한줄 요약**: 단일 이미지로부터 조명 재구성(relighting)과 3D 기하학적 구조 추정을 동시에 수행하는 통합형 멀티모달 확산 트랜스포머(DiT) 프레임워크 제안.
- **핵심 기여**: 기존의 순차적 파이프라인을 탈피하여 기하학적 일관성과 물리적 타당성을 극대화한 공동 최적화 모델 구축 및 VAE 친화적 3D 표현 방식인 iNOD 도입.
- **방법론 개요**: 비디오 DiT의 시간 차원을 모달리티 차원으로 재해석하여 알베도, 법선, 깊이, 재조명 이미지를 병렬 처리하며, iNOD를 통해 왜곡 없는 3D 정보를 잠재 공간에 투영하고 합성/실제 데이터 혼합 학습을 수행.
- **의의**: 기존 방식의 고질적인 문제인 오차 누적을 방지하고, 단일 이미지 입력만으로도 고품질의 3D 복원과 사실적인 조명 효과를 동시에 구현하여 컴퓨터 비전 및 그래픽스 분야의 생성적 재조명 성능을 획기적으로 개선함.

### 4. FurnSet: Exploiting Repeats for 3D Scene Reconstruction

- **arXiv**: https://arxiv.org/abs/2604.20093
- **Score**: 7.5 / 10
- **한줄 요약**: 기존의 단일 뷰 3D 복원 방법이 객체를 개별적으로 처리하거나 암묵적인 맥락에 의존하는 한계를 극복하기 위해, 장면 내 반복되는 객체 인스턴스를 명시적으로 활용하여 기하학적 모호성을 해결하는 FurnSet 프레임워크를 제안합니다.
- **핵심 기여**: 장면 내 반복되는 객체 인스턴스를 식별하고 집계하는 '집합 인식(set-aware)' 메커니즘을 도입하여, 개별 객체의 기하학적 복원 정확도와 일관성을 향상시킵니다.
- **방법론 개요**: 객체별 CLS 토큰과 집합 인식 셀프 어텐션 메커니즘을 사용하여 동일한 객체 인스턴스를 식별하고 특징을 집계합니다. 또한, 장면 수준 및 객체 수준 컨디셔닝을 통합하고, 생성된 객체 포인트 클라우드를 사용하여 3D 및 2D 투영 손실을 최소화하는 레이아웃 최적화를 수행합니다.
- **의의**: 이 프레임워크는 독립적인 객체 추정에서 벗어나 집합 기반 추론 접근 방식을 취함으로써, 실제 환경의 내재된 중복성을 활용하여 3D 장면 복원의 충실도를 높이고, 특히 가려짐(occlusion) 상황에서의 아모달(amodal) 추론 문제를 해결하는 데 기여합니다.

### 5. DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation

- **arXiv**: https://arxiv.org/abs/2604.20841
- **Score**: 7.2 / 10
- **한줄 요약**: DeVI(Dexterous Video Imitation)는 고가의 3D 모션 캡처 데이터 없이도 생성형 비디오 모델을 활용해 복잡한 인간-객체 상호작용(HOI)을 물리적으로 구현 가능한 제어 정책으로 학습시키는 프레임워크입니다.
- **핵심 기여**: 3D 모션 데이터 의존성을 제거하고, 생성된 2D 비디오에서 추출한 하이브리드 타겟(3D 인간 포즈 + 2D 객체 추적)을 통해 미지의 객체에 대해서도 제로샷 일반화가 가능한 확장성 높은 HOI 학습 파이프라인을 구축했습니다.
- **방법론 개요**: 텍스트 조건부 비디오 확산 모델로 HOI 영상을 생성하고, 이를 3D 인간 포즈 추정 및 2D 객체 추적 기술을 통해 하이브리드 타겟으로 변환한 뒤, 강화학습(PPO)을 통해 물리 시뮬레이션 환경에서 제어 정책을 학습합니다.
- **의의**: 데이터 수집의 병목 현상을 해결하여 로봇 공학 및 캐릭터 애니메이션 분야에서 복잡하고 정교한 손-객체 조작 기술을 대규모로 생성하고 시뮬레이션할 수 있는 새로운 길을 열었습니다.

### 6. Render-in-the-Loop: Vector Graphics Generation via Visual Self-Feedback

- **arXiv**: https://arxiv.org/abs/2604.20730
- **Score**: 6.8 / 10
- **한줄 요약**: SVG 생성을 단순한 텍스트 나열이 아닌, 중간 결과물을 시각적으로 확인하며 단계적으로 그려나가는 'Render-in-the-Loop(RITL)' 폐루프 시각적 추론 과정으로 재정의함.
- **핵심 기여**: 기존의 '눈먼' 생성 방식이나 스칼라 보상 기반 강화학습의 한계를 극복하고, MLLM의 시각적 인지 능력을 활용해 기하학적 정확도와 구조적 일관성을 획기적으로 개선함.
- **방법론 개요**: SVG 생성 과정을 세분화하여 각 단계의 결과물을 렌더링하고, 이를 다시 MLLM의 입력으로 제공하는 시각적 피드백 루프와 추론 시 오류를 교정하는 'Render-and-Verify(RaV)' 메커니즘을 도입함.
- **의의**: 벡터 그래픽 생성에서 발생하는 공간적 정보 손실과 구조적 환각 문제를 해결함으로써, 복잡한 레이어 구성과 기하학적 관계를 정밀하게 제어할 수 있는 새로운 생성 패러다임을 제시함.

### 7. DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion

- **arXiv**: https://arxiv.org/abs/2604.20470
- **Score**: 6.8 / 10
- **한줄 요약**: DynamicRad는 장편 비디오 확산 모델의 연산 병목 현상을 해결하기 위해, 시공간적 에너지 감쇠 우선순위와 콘텐츠 적응형 라우팅을 결합한 효율적인 희소 어텐션(Sparse Attention) 프레임워크입니다.
- **핵심 기여**: 최대 2.5배의 추론 속도 향상과 80% 이상의 희소성을 달성하면서도, 정적/동적 모드를 통해 하드웨어 효율성과 생성 품질 간의 최적의 균형을 제공합니다.
- **방법론 개요**: 방사형 지역성 우선순위(Radial Locality Prior)를 기반으로 토큰을 선별하며, 오프라인 베이지안 최적화와 시맨틱 모션 라우터를 통해 실시간 연산 오버헤드 없이 최적의 희소성 패턴을 적용합니다.
- **의의**: 기존의 고정된 희소성 마스크가 가진 한계를 극복하고, 대규모 비디오 생성 모델(HunyuanVideo, Wan2.1 등)에서 연산 비용과 시퀀스 길이 간의 의존성을 성공적으로 분리하여 확장성을 확보했습니다.

### 8. Self-supervised pretraining for an iterative image size agnostic vision transformer

- **arXiv**: https://arxiv.org/abs/2604.20392
- **Score**: 6.8 / 10
- **한줄 요약**: 인간의 시각 시스템을 모방하여, 고해상도 이미지 처리 시 발생하는 연산 복잡도와 해상도 의존성 문제를 해결하는 반복적(iterative) 능동형 비전 트랜스포머 프레임워크 제안.
- **핵심 기여**: 입력 해상도와 무관하게 연산량을 일정하게 유지하는 '해상도 불변(resolution-agnostic)' 아키텍처를 구현하고, BPTT 없이 자기지도 학습(SSL)을 성공적으로 적용하여 범용 비전 백본으로서의 성능을 입증함.
- **방법론 개요**: 강화학습 기반의 시선 정책(gaze policy)을 통해 이미지 내 주요 영역을 순차적으로 탐색하고, 다중 줌(multi-zoom) 패치 추출 기법과 DINO 기반의 순차적-전역적 증류(sequential-to-global distillation)를 결합하여 학습.
- **의의**: 기존 ViT의 고해상도 입력 시 발생하는 성능 저하와 연산 비용 문제를 근본적으로 해결하며, 효율적인 능동형 비전 모델을 대규모 자기지도 학습으로 확장할 수 있는 새로운 패러다임을 제시함.

### 9. X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference

- **arXiv**: https://arxiv.org/abs/2604.20289
- **Score**: 6.8 / 10
- **한줄 요약**: X-Cache는 소수 단계(few-step) 자가회귀 월드 모델의 추론 속도를 높이기 위해, 기존의 단계 간(cross-step) 캐싱 대신 연속적인 생성 청크(chunk) 간의 잔차(residual)를 재사용하는 훈련 불필요(training-free) 가속 프레임워크입니다.
- **핵심 기여**: 기존 캐싱 기법의 한계를 극복하고, 블록별 잔차 캐싱과 이중 지표 게이팅을 통해 71%의 블록 스킵률과 2.6배의 추론 속도 향상을 달성하며 실시간 대화형 시뮬레이션의 효율성을 입증했습니다.
- **방법론 개요**: 각 트랜스포머 블록의 잔차를 캐싱하고, 구조 및 행동 인식 지문(fingerprint) 기반의 게이팅 메커니즘을 통해 재사용 여부를 동적으로 결정합니다. 또한, 누적 오차 방지를 위해 주기적으로 KV 캐시를 갱신하는 제어 로직을 포함합니다.
- **의의**: 기존의 시간적 외삽 방식이 통하지 않는 소수 단계 생성 환경에서 새로운 최적화 축을 제시함으로써, 자율주행 등 고충실도 실시간 인터랙티브 시뮬레이션의 계산 비용 문제를 해결하고 모델의 확장성을 확보했습니다.

### 10. LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model

- **arXiv**: https://arxiv.org/abs/2604.20796
- **Score**: 6.5 / 10
- **한줄 요약**: 텍스트와 시각 정보를 단일 이산 확산 모델(dLLM) 아키텍처 내에서 통합하여, 이해와 생성을 동시에 수행하는 범용 멀티모달 모델 LLaDA2.0-Uni 제안.
- **핵심 기여**: SigLIP-VQ 기반의 의미론적 토큰화와 MoE(Mixture-of-Experts) 구조를 통해 기존 멀티모달 모델의 이해력과 생성 품질 간의 성능 격차를 해소하고, 통합된 학습 파이프라인을 구축함.
- **방법론 개요**: SigLIP2-g 기반의 시각 토큰화, 16B 파라미터 규모의 MoE 확산 언어 모델 백본, 그리고 고충실도 이미지 복원을 위한 전용 확산 디코더를 결합하여 마스크 예측 기반의 통합 학습을 수행함.
- **의의**: 기존의 파편화된 멀티모달 아키텍처를 단일 모델로 통합함으로써, 복잡한 추론과 고품질 이미지 생성을 동시에 처리할 수 있는 확장 가능하고 효율적인 차세대 멀티모달 에이전트의 기반을 마련함.

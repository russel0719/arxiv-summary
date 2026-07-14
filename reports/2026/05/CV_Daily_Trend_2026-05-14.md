# CV 연구 동향 보고서 — 2026-05-14

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| 비디오 생성 및 정렬 | 자기회귀(AR) 모델의 누적 오차 및 학습-추론 간 분포 불일치 해결 | RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO |
| Embodied AI 및 로보틱스 | 비디오 생성 모델의 물리적 일관성 확보 및 로봇 조작 작업으로의 정렬 | CreFlow: Corrective Reflow for Sparse-Reward Embodied Video Diffusion RL |
| 생성 모델 효율화 및 기하학적 최적화 | 잠재 공간의 기하학적 구조 활용 및 연산 복잡도 개선 | Aligning Latent Geometry for Spherical Flow Matching in Image Generation |

> 핵심 메시지: 최신 컴퓨터 비전 연구는 자기회귀 비디오 생성의 누적 오차를 해결하기 위한 강화학습 기반 정렬과, 물리적 일관성을 확보한 Embodied AI 및 산업용 3D 생성 기술로 빠르게 진화하고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Video Generation | 장기 비디오 생성의 일관성 유지 및 실시간 대화형 생성 최적화 | Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation |
| 3D Generation | 산업 표준 토폴로지 준수 및 고충실도 3D 헤드 생성 | TOPOS: High-Fidelity and Efficient Industry-Grade 3D Head Generation |
| Autonomous Driving | 폐루프(Closed-loop) 가치 추정을 통한 주행 계획 및 안전성 최적화 | CLOVER: Closed-Loop Value Estimation & Ranking |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| GRPO (Group Relative Policy Optimization) | 비디오 생성 모델의 강화학습 기반 정렬 및 최적화 | KVPO: ODE-Native GRPO for Autoregressive Video Alignment |
| Flow Matching & Spherical Geometry | 잠재 공간의 기하학적 투영을 통한 생성 품질 및 학습 효율 개선 | Aligning Latent Geometry for Spherical Flow Matching in Image Generation |
| Linear Attention (O(N)) | 의미적 유사성 기반 토큰 그룹화를 통한 비전 트랜스포머 효율성 극대화 | Representative Attention For Vision Transformers |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| 로보틱스 & 비디오 생성 | LTL(선형 시간 논리) 제약 조건을 활용한 물리적 인과관계 학습 | 생성형 모델의 물리적 오류 감소 및 로봇 조작 성공률 향상 |
| 자율주행 & 강화학습 | 오프라인 데이터 기반의 폐루프 가치 평가 및 순위 결정 | 온라인 학습의 불안정성 없이 안전한 주행 계획 수립 |

---

## 5. 개별 논문 요약

### 1. RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO

- **arXiv**: https://arxiv.org/abs/2605.15190
- **Score**: 8.2 / 10
- **한줄 요약**: RAVEN은 자기회귀 비디오 생성 시 발생하는 학습-추론 간 분포 불일치(Distribution Shift)를 해결하기 위해, 모델이 스스로 생성한 이력을 학습에 직접 활용하는 '학습 시간 테스트(Training-time Test)' 프레임워크를 제안합니다.
- **핵심 기여**: KV 캐시 구성을 종단간(end-to-end)으로 최적화하고, 일관성 모델 기반의 CM-GRPO를 통해 복잡한 수치 해석 과정 없이 효율적인 강화학습 정책 최적화를 구현하여 장기 비디오 생성의 품질과 일관성을 획기적으로 개선했습니다.
- **방법론 개요**: 학습 시 '인터리브드 롤아웃(Interleaved Rollouts)'을 통해 깨끗한 과거 이력과 노이즈가 섞인 상태를 함께 학습하고, CM-GRPO를 사용하여 일관성 모델의 결정론적 전이 커널에 직접 강화학습을 적용함으로써 추론 환경과 동일한 최적화 목표를 설정합니다.
- **의의**: 기존 자기회귀 모델의 고질적인 문제인 누적 오차(Compounding Error)를 효과적으로 억제하며, 계산 비용이 높은 Euler-Maruyama 방식 없이도 고품질의 장기 비디오를 생성할 수 있는 수학적으로 우아하고 효율적인 솔루션을 제공합니다.

### 2. Head Forcing: Long Autoregressive Video Generation via Head Heterogeneity

- **arXiv**: https://arxiv.org/abs/2605.14487
- **Score**: 8.2 / 10
- **한줄 요약**: 자기회귀(AR) 비디오 확산 모델에서 어텐션 헤드의 기능적 이질성을 활용하여, 학습 없이도 장시간 비디오 생성의 일관성을 유지하는 'Head Forcing' 프레임워크 제안.
- **핵심 기여**: 어텐션 헤드를 로컬, 앵커, 메모리 헤드로 분류하는 기능적 분류 체계를 정립하고, 이를 통해 KV 캐시 할당을 최적화하여 추가 학습 없이 비디오 생성 길이를 분 단위로 확장함.
- **방법론 개요**: 헤드별 기능에 따라 KV 캐시 전략을 차등 적용하고, 계층적 메모리 시스템과 헤드별 RoPE 재인코딩을 도입하여 장기 문맥 유지 및 위치 정보 왜곡을 방지함.
- **의의**: 기존의 획일적인 KV 캐시 관리 방식이 가진 한계를 극복하여, 고비용 재학습 없이도 장기 비디오 생성의 일관성과 효율성을 획기적으로 개선함.

### 3. KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration

- **arXiv**: https://arxiv.org/abs/2605.14278
- **Score**: 8.2 / 10
- **한줄 요약**: KVPO는 스트리밍 자기회귀(AR) 비디오 생성 모델을 위해 노이즈 기반 탐색 대신 KV 캐시를 활용한 인과적-의미론적 탐색을 도입한 ODE 기반의 정렬 프레임워크입니다.
- **핵심 기여**: 기존 SDE 기반 노이즈 탐색이 가진 결정론적 ODE 모델과의 불일치 문제를 해결하고, KV 캐시 라우팅을 통해 데이터 매니폴드 상에서 의미론적으로 일관된 탐색을 가능하게 했습니다.
- **방법론 개요**: Causal History Routing(CHR)을 통해 과거 KV 캐시를 확률적으로 재구성하여 다양한 생성 경로를 생성하고, 이를 흐름 매칭(flow-matching) 속도장 공간에서 평가하여 최적화하는 GRPO 기반 방식을 사용합니다.
- **의의**: 기존 방식이 초래하던 시각적 품질 저하와 장기 일관성 문제를 해결함으로써, 효율적인 스트리밍 추론을 유지하면서도 인간의 선호도에 부합하는 고품질의 긴 영상 생성을 가능하게 합니다.

### 4. Aligning Latent Geometry for Spherical Flow Matching in Image Generation

- **arXiv**: https://arxiv.org/abs/2605.15193
- **Score**: 7.8 / 10
- **한줄 요약**: 잠재 공간(Latent Space)의 기하학적 구조와 확산 모델의 선형 경로 간의 불일치를 해결하기 위해, 잠재 토큰을 구면(Hypersphere)으로 투영하고 구면 선형 보간(SLERP)을 적용하는 Spherical Flow Matching(SFM)을 제안함.
- **핵심 기여**: 잠재 토큰의 의미론적 정보가 주로 각도 성분에 집중되어 있음을 규명하고, 모델 구조 변경 없이 구면 기하학을 도입하여 학습 효율을 2.2배 향상시키고 생성 품질을 개선함.
- **방법론 개요**: 사전 학습된 VAE의 잠재 토큰을 고정된 반지름의 구면으로 투영한 뒤, 기존의 유클리드 기반 선형 보간 대신 구면 선형 보간(SLERP)을 사용하여 속도 필드를 학습하고 디코더를 미세 조정함.
- **의의**: 고차원 공간에서 가우시안 노이즈와 잠재 데이터가 얇은 구면 껍질에 집중되는 현상을 기하학적으로 활용함으로써, 복잡한 추가 인코더 없이도 생성 모델의 학습 수렴 속도와 최종 성능을 동시에 최적화할 수 있는 원칙적인 접근법을 제시함.

### 5. Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation

- **arXiv**: https://arxiv.org/abs/2605.15141
- **Score**: 7.8 / 10
- **한줄 요약**: Causal Forcing++는 비디오 확산 모델의 증류 과정을 최적화하여 1~2단계 샘플링만으로 실시간 대화형 비디오 생성을 가능하게 하는 프레임 단위 자기회귀(AR) 증류 파이프라인입니다.
- **핵심 기여**: 기존의 복잡한 오프라인 궤적 생성 과정을 온라인 단일 단계 감독으로 대체하는 'Causal Consistency Distillation'을 도입하여 학습 비용을 4배 절감하고 첫 프레임 지연 시간을 50% 단축했습니다.
- **방법론 개요**: 기존의 다단계 ODE 궤적 저장 방식 대신, 인접한 타임스텝 간의 단일 온라인 교사 ODE 단계를 사용하여 학생 모델의 AR 조건부 흐름 맵을 정렬하는 방식을 채택했습니다.
- **의의**: 기존 증류 방식의 아키텍처 불일치와 오류 누적 문제를 해결함으로써, 고품질 비디오를 실시간으로 생성해야 하는 대화형 월드 모델 및 인터랙티브 시스템 구현의 핵심 토대를 마련했습니다.

### 6. CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous Driving Planning

- **arXiv**: https://arxiv.org/abs/2605.15120
- **Score**: 7.8 / 10
- **한줄 요약**: CLOVER는 자율주행의 훈련-평가 불일치 문제를 해결하기 위해, 단일 경로 모방 학습에서 벗어나 제안 생성기(Generator)와 평가기(Scorer)를 결합한 폐루프(Closed-loop) 가치 추정 및 순위 결정 프레임워크를 제안합니다.
- **핵심 기여**: 단일 경로 모방의 한계를 극복하고, 규칙 기반 평가기를 활용한 집합 수준의 커버리지 감독과 보수적 자기 증류(Self-distillation)를 통해 주행 성능과 안전성을 동시에 최적화했습니다.
- **방법론 개요**: 평가기 필터링을 거친 의사 전문가(Pseudo-expert) 궤적을 통해 생성기를 학습시키고, 계획 지표(안전성, 편의성 등)를 예측하는 평가기를 통해 최적의 궤적을 선택하는 2단계 구조를 채택했습니다.
- **의의**: 실제 주행 환경의 복잡한 다중 모달리티를 반영하면서도, 온라인 강화학습의 불안정성 없이 오프라인 데이터만으로도 높은 수준의 주행 성능과 안전성을 달성할 수 있는 실용적인 패러다임을 제시합니다.

### 7. Analogical Trajectory Transfer

- **arXiv**: https://arxiv.org/abs/2605.14393
- **Score**: 7.8 / 10
- **한줄 요약**: 서로 다른 3D 환경 간에 의미론적 맥락과 물리적 제약을 유지하며 모션 궤적을 전이하는 훈련 불필요(training-free) 프레임워크 제안.
- **핵심 기여**: 3D 파운데이션 모델 기반의 계층적 그래프 매칭 기법을 통해, 명시적인 레이블 없이도 공간적·의미론적 일관성을 갖춘 궤적 전이를 실시간으로 수행.
- **방법론 개요**: 3D 장면을 객체 중심 클러스터로 분할하고, 그래프 매칭 알고리즘을 통해 클러스터 간 대응 관계를 파악한 뒤, 이를 결합 및 최적화하여 물리적으로 타당한 궤적을 생성.
- **의의**: 로봇 공학 및 AR/VR 분야에서 복잡한 다단계 작업을 새로운 환경에 즉각적으로 일반화할 수 있게 하여, 데이터 수집 비용을 절감하고 시스템의 범용성을 크게 향상함.

### 8. CreFlow: Corrective Reflow for Sparse-Reward Embodied Video Diffusion RL

- **arXiv**: https://arxiv.org/abs/2605.14274
- **Score**: 7.8 / 10
- **한줄 요약**: CreFlow는 비디오 생성 모델(VGM)을 로봇 조작 작업에 정렬하기 위해 선형 시간 논리(LTL) 기반의 제약 조건과 공간-시간적 신용 할당을 결합한 온라인 강화학습 프레임워크입니다.
- **핵심 기여**: 전역적 시각 품질 평가에서 벗어나, 객체 지속성 및 인과관계와 같은 물리적·논리적 제약 조건을 검증하는 진단적 피드백을 도입하여 로봇 실행 성공률을 23.8% 향상시켰습니다.
- **방법론 개요**: LTL 기반의 제약 조건으로 보상을 모델링하고, 'Credit-Aware NFT Loss'를 통해 실패와 관련된 특정 시공간 영역에만 그래디언트를 집중시키는 마스킹 기법과 최적의 수정 방향을 제시하는 'Corrective Reflow Loss'를 사용합니다.
- **의의**: 시각적으로는 그럴듯하지만 물리적으로는 불가능한 비디오를 생성하는 기존 모델의 한계를 극복하여, 생성형 모델이 실제 로봇 조작과 같은 정밀한 Embodied AI 작업에 활용될 수 있는 실질적인 경로를 제시합니다.

### 9. Representative Attention For Vision Transformers

- **arXiv**: https://arxiv.org/abs/2605.14913
- **Score**: 7.2 / 10
- **한줄 요약**: 공간적 근접성이 아닌 의미적 유사성을 기반으로 토큰을 그룹화하여 효율적인 전역 문맥을 학습하는 선형 복잡도(O(N))의 'Representative Attention(RPAttention)' 메커니즘 제안.
- **핵심 기여**: 기존의 고정된 공간적 분할 방식에서 벗어나 표현 공간(representation-space) 중심의 동적 토큰 압축을 도입함으로써, 효율성과 의미적 표현력을 동시에 확보함.
- **방법론 개요**: 유사도 기반의 'Competitive Soft Gathering'으로 대표 토큰을 생성하고, 이 압축된 잠재 공간에서 상호작용을 수행한 뒤, 쿼리 기반의 'Distribution' 과정을 통해 원본 토큰으로 정보를 복원하는 3단계 구조.
- **의의**: 기존 선형 어텐션의 구조적 한계와 공간적 편향 문제를 해결하여, 고해상도 비전 작업에서 계산 효율성을 유지하면서도 객체의 의미적 구조를 효과적으로 포착할 수 있는 확장 가능한 아키텍처를 제공함.

### 10. TOPOS: High-Fidelity and Efficient Industry-Grade 3D Head Generation

- **arXiv**: https://arxiv.org/abs/2605.14594
- **Score**: 7.2 / 10
- **한줄 요약**: TOPOS는 고충실도 3D 헤드 생성과 산업 표준 토폴로지(topology) 유지라는 상충하는 요구사항을 동시에 해결하는 프레임워크입니다.
- **핵심 기여**: 임의의 입력 데이터를 고정된 스튜디오급 토폴로지로 변환하여, 리깅 및 애니메이션 등 후속 제작 파이프라인에 즉시 활용 가능한 일관된 3D 에셋 생성 기술을 제시했습니다.
- **방법론 개요**: Perceiver Resampler 기반의 TOPOS-VAE로 입력 데이터를 고정된 잠재 공간에 투영하고, TOPOS-DiT(확산 트랜스포머)를 통해 고해상도 형상과 재조명 가능한 UV 텍스처를 생성하는 2단계 생성 방식을 채택했습니다.
- **의의**: 기존의 고품질 생성 모델이 가진 토폴로지 비일관성 문제를 해결함으로써, 학술적 연구 성과를 실제 산업 현장의 디지털 휴먼 제작 파이프라인으로 직접 연결하는 가교 역할을 합니다.

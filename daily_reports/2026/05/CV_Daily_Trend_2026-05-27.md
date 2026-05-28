# CV 연구 동향 보고서 — 2026-05-27

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| 멀티모달 및 생성형 모델 | 모듈형 구조를 탈피한 네이티브 통합 아키텍처 및 실시간 상호작용 모델링 | From Pixels to Words -- Towards Native One-Vision Models at Scale |
| 로보틱스 및 보안 | VLA(Vision-Language-Action) 모델의 물리적 세계 상호작용 취약점 및 안전성 확보 | VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models |
| 기하학적 및 물리 기반 학습 | 수치 해석을 대체하는 신경 연산자 및 확산 모델의 수학적 최적화 | Geometry-Correct Diffusion Posterior Sampling with Denoiser-Pullback Curvature Guidance |

> 핵심 메시지: 컴퓨터 비전 연구는 모듈형 구조를 통합하는 네이티브 아키텍처로 진화하며, 물리적 세계와의 상호작용을 위한 기하학적 최적화와 보안성 강화에 집중하고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Generation | 다중 에이전트 시뮬레이션 및 실시간 오디오 기반 캐릭터 동작 생성 | Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players |
| Vision-Language | 시각적 언어 모델의 네이티브 통합 및 시각적 음성 인식(VSR)의 확산 모델 적용 | Diffusion Large Language Models for Visual Speech Recognition |
| 3D/Avatar | HMD 기반 실시간 전신 아바타 캡처 및 재조명 | EgoRelight: Egocentric Human Capture and Illumination Recovery |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Diffusion-Forcing & Denoising | 실시간 스트리밍 환경에서의 동작 생성 및 비자기회귀적 문장 복원 | DiscoForcing: A Unified Framework for Real-Time Audio-Driven Character Control |
| Probabilistic/Bayesian Learning | 대조 학습의 최적화 충돌 해결 및 해석 가능한 잠재 표현 생성 | Bayesian Gated Non-Negative Contrastive Learning |
| Geometric Optimization | 확산 모델의 역문제 해결을 위한 2차 최적화 및 매니폴드 정렬 | Geometry-Correct Diffusion Posterior Sampling with Denoiser-Pullback Curvature Guidance |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| 로보틱스 & 보안 | VLA 모델의 시각적 고유수용성 메커니즘을 악용한 적대적 공격 | 로봇 제어 시스템의 보안 기준 수립 및 강건성 강화 |
| 의료 영상 & 수치 해석 | 확산 모델의 기하학적 구조를 활용한 역문제 재구성 | 의료 영상의 정밀도 향상 및 비선형 역문제의 신뢰성 확보 |

---

## 5. 개별 논문 요약

### 1. From Pixels to Words -- Towards Native One-Vision Models at Scale

- **arXiv**: https://arxiv.org/abs/2605.28820
- **Score**: 8.2 / 10
- **한줄 요약**: 기존의 모듈형 VLM 구조를 탈피하여, 이미지, 비디오, 텍스트를 단일 시퀀스로 처리하는 네이티브(Native) 통합 아키텍처 'NEO-ov'를 제안합니다.
- **핵심 기여**: 외부 인코더 없이도 시공간적 추론과 정밀한 공간 인식을 동시에 수행하는 통합 백본을 구축하여, 모듈형 모델과 대등한 성능을 입증하고 아키텍처의 복잡성을 획기적으로 개선했습니다.
- **방법론 개요**: THW(Temporal, Height, Width)로 분해된 어텐션 메커니즘과 다차원 RoPE(Rotary Positional Embedding)를 도입하여, 텍스트와 시각 정보를 동일한 잠재 공간에서 처리하는 통합 직렬화 방식을 사용합니다.
- **의의**: 모듈 간 정보 손실과 파편화를 방지하고, 단일 모델로 다양한 시각적 입력(이미지, 비디오 등)을 처리할 수 있는 확장 가능하고 효율적인 차세대 멀티모달 학습 패러다임을 제시합니다.

### 2. Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

- **arXiv**: https://arxiv.org/abs/2605.28816
- **Score**: 8.2 / 10
- **한줄 요약**: 다중 에이전트 환경에서 상호작용과 물리적 제약을 효과적으로 모델링하는 확장 가능한 생성형 월드 모델(World Model) 프레임워크.
- **핵심 기여**: 순열 불변성(Permutation Symmetry)을 보장하는 Simplex RoPE와 선형 복잡도의 Sparse Hub Attention을 도입하여, 에이전트 수에 관계없이 고충실도의 실시간 다중 에이전트 시뮬레이션 및 제로샷 일반화를 구현함.
- **방법론 개요**: 양방향 교사 모델을 인과적 학생 모델로 증류(Distillation)한 구조로, Simplex RoPE를 통해 에이전트 ID를 처리하고, Sparse Hub Attention을 통해 에이전트 간 통신 복잡도를 O(N^2)에서 O(N)으로 최적화하며, KV 캐싱을 통해 실시간 스트리밍 생성을 지원함.
- **의의**: 기존의 고정된 슬롯 기반 모델이나 연산 비용이 높은 밀집 어텐션 모델의 한계를 극복하여, 복잡한 다중 에이전트 환경에서도 효율적이고 일관된 미래 예측 및 상호작용 시뮬레이션을 가능하게 함.

### 3. Geometry-Correct Diffusion Posterior Sampling with Denoiser-Pullback Curvature Guidance and Manifold-Aligned Damping

- **arXiv**: https://arxiv.org/abs/2605.27990
- **Score**: 8.2 / 10
- **한줄 요약**: 사전 학습된 확산 모델을 활용한 역문제 해결 시, 기존의 단순 스칼라 가중치 방식 대신 확산 모델의 기하학적 구조를 고려한 2차 최적화(Gauss-Newton) 기반의 사후 분포 샘플링 프레임워크(CLAMP)를 제안함.
- **핵심 기여**: 확산 모델의 비등방성 곡률을 보정하는 'Denoiser-pullback 곡률 가이드'와 '매니폴드 정렬 댐핑'을 도입하여, 복잡한 역문제에서도 안정적이고 고품질의 재구성을 가능하게 함.
- **방법론 개요**: 자동 미분을 활용한 행렬 연산 없는(matrix-free) GMRES 솔버를 통해 국소 2차 근사치를 계산하고, 이를 확산 모델의 노이즈 제거 단계와 결합하여 측정값과 데이터 매니폴드 간의 일관성을 최적화함.
- **의의**: 기존 확산 사후 샘플링의 고질적인 문제인 불안정성과 연산 효율성 한계를 수학적으로 엄밀하게 해결함으로써, 의료 영상 및 비선형 역문제 분야에서 보다 정밀하고 신뢰도 높은 재구성을 가능하게 함.

### 4. Resolution-free neural surrogates for geometric parameterization and mapping with spatially varying fields

- **arXiv**: https://arxiv.org/abs/2605.28551
- **Score**: 7.8 / 10
- **한줄 요약**: 공간적으로 변화하는 필드에 기반한 기하학적 매핑 문제를 해결하기 위해, 전통적인 수치 해석 기법을 대체하는 해상도 독립적(resolution-free) 신경망 대리 모델을 제안함.
- **핵심 기여**: 메시 기반의 반복적 수치 해석 없이도 복잡한 기하학적 매핑(준등각 사상, 밀도 균등화 등)을 수행할 수 있는 데이터 없는(data-free) 기하학적 신경 연산자 프레임워크를 구축함.
- **방법론 개요**: 좌표와 파라미터 필드를 결합한 다중 해상도 인코딩을 활용하며, 물리 기반 및 변분 에너지 원리를 손실 함수로 사용하는 자기지도 학습(self-supervised learning) 방식을 채택함.
- **의의**: 기존 수치 해석 기법의 높은 계산 비용과 도메인 종속성 문제를 해결하여, 고해상도 환경에서도 실시간에 가까운 효율적이고 확장 가능한 기하학적 변환 및 매핑을 가능하게 함.

### 5. Bayesian Gated Non-Negative Contrastive Learning

- **arXiv**: https://arxiv.org/abs/2605.28441
- **Score**: 7.8 / 10
- **한줄 요약**: BayesNCL은 결정론적 대조 학습(Contrastive Learning)에서 발생하는 최적화 충돌 문제를 해결하기 위해 확률적 게이팅 메커니즘을 도입한 표현 학습 프레임워크입니다.
- **핵심 기여**: 공통 배경 등 불필요한 특징으로 인한 그래디언트 진동을 억제하고, 의미론적으로 분리된(disentangled) 해석 가능한 잠재 표현을 생성하여 성능과 투명성을 동시에 확보했습니다.
- **방법론 개요**: 변분 추론(Variational Inference)을 기반으로 베르누이 사전 분포를 활용한 확률적 게이팅을 적용하고, Straight-Through Estimator(STE)를 통해 이산적 마스킹을 수행하며 희소성 정규화를 통해 핵심 특징만을 추출합니다.
- **의의**: 기존 대조 학습의 '블랙박스' 문제를 해결하고 안전이 중요한 도메인에서 모델의 의사결정 과정을 해석 가능하게 만들며, 의미론적 일관성을 획기적으로 향상시켰습니다.

### 6. EgoRelight: Egocentric Human Capture and Illumination Recovery for Relightable and Photoreal Avatar Rendering

- **arXiv**: https://arxiv.org/abs/2605.28401
- **Score**: 7.8 / 10
- **한줄 요약**: HMD 센서만을 활용하여 실시간으로 고품질의 재조명 가능한(relightable) 전신 아바타를 생성하고 가상 환경에 통합하는 엔드투엔드 프레임워크입니다.
- **핵심 기여**: 스튜디오 수준의 다중 카메라 장비 없이 단일 HMD만으로 정밀한 모션 캡처, 신경망 기반 외형 모델링, 그리고 실시간 HDR 환경 조명 복원을 통합하여 구현했습니다.
- **방법론 개요**: 스테레오 카메라 기반의 깊이 추정으로 신체 움직임을 추적하고, 신경망을 통해 외형을 확산 및 반사 성분으로 분리하여 학습하며, 테스트 타임 역렌더링을 통해 실제 환경의 조명을 추정합니다.
- **의의**: 기존의 제약된 환경에서만 가능했던 고충실도 아바타 텔레프레젠스를 일상적인 환경으로 확장하여, 혼합 현실(MR) 내에서 물리적으로 일관성 있는 몰입형 인간 상호작용을 가능하게 합니다.

### 7. DiscoForcing: A Unified Framework for Real-Time Audio-Driven Character Control with Diffusion Forcing

- **arXiv**: https://arxiv.org/abs/2605.28491
- **Score**: 7.2 / 10
- **한줄 요약**: DiscoForcing은 실시간 스트리밍 환경에서 오디오에 반응하여 고품질의 캐릭터 동작을 생성하는 인과적(causal) 생성 프레임워크입니다.
- **핵심 기여**: 오프라인 모델의 비인과적 제약 문제를 해결하고, 실시간 스트리밍 환경에서 긴 시간 동안의 동작 일관성과 오디오 비트 동기화를 보장하는 배포 가능한 솔루션을 제시했습니다.
- **방법론 개요**: 인과적 음악 인코더, 시점별 노이즈 수준을 다르게 학습하는 Diffusion-Forcing 시퀀스 모델, 그리고 실시간 반응성과 장기적 일관성 사이의 균형을 맞추는 하이브리드 샘플링 기법을 결합했습니다.
- **의의**: 기존 오프라인 생성 모델의 한계를 극복하여 인터랙티브 아바타 및 물리 기반 휴머노이드 제어와 같은 실시간 응용 분야에서 고품질 동작 합성을 가능하게 합니다.

### 8. Diffusion Large Language Models for Visual Speech Recognition

- **arXiv**: https://arxiv.org/abs/2605.28456
- **Score**: 7.2 / 10
- **한줄 요약**: 기존의 자기회귀(Autoregressive) 방식 VSR의 한계를 극복하기 위해 확산 기반 대규모 언어 모델(DLLM)을 활용한 반복적 마스크 디노이징 프레임워크를 제안함.
- **핵심 기여**: VSR 분야 최초로 DLLM을 도입하여 양방향 문맥을 활용한 비순차적 디코딩을 구현하고, 영상 길이를 활용한 길이 예측 전략으로 성능을 최적화함.
- **방법론 개요**: 시각적 인코더와 DLLM을 결합하여 마스크된 텍스트 캔버스를 반복적으로 복원하며, 2단계 학습(정렬 및 완성)과 영상 길이에 기반한 후보 디코딩 전략을 사용함.
- **의의**: 시각적 모호성이 높은 VSR 작업에서 고정된 순서의 디코딩으로 인한 오류 전파 문제를 해결하고, LRS3 데이터셋에서 SOTA 성능을 달성하여 비자기회귀 VSR의 새로운 가능성을 제시함.

### 9. VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking

- **arXiv**: https://arxiv.org/abs/2605.28083
- **Score**: 7.2 / 10
- **한줄 요약**: VLA-Hijack은 로봇의 시각적 자기 위치 추정(Visual Self-localization) 메커니즘을 악용하여, 적대적 패치를 통해 로봇의 신체 인식을 왜곡하고 제어 정책을 탈취하는 공격 프레임워크입니다.
- **핵심 기여**: 기존의 모델별 액션 헤드 종속성을 극복하고, 로봇의 공통적인 시각적-고유수용성 논리를 타겟팅함으로써 다양한 VLA 아키텍처 간의 높은 공격 전이성을 확보했습니다.
- **방법론 개요**: 로봇 팔의 시각적 특징을 억제하는 '고유수용성 억제'와 적대적 패치를 가짜 신체로 인식하게 하는 '고유수용성 주입'을 결합하여, 모델의 주의 메커니즘을 강제로 재설정합니다.
- **의의**: VLA 모델이 물리적 세계와 상호작용할 때 발생하는 근본적인 보안 취약점을 규명하였으며, 향후 로봇 제어 시스템의 안전성과 강건성을 평가하는 새로운 기준을 제시합니다.

### 10. AREA: Attribute Extraction and Aggregation for CLIP-Based Class-Incremental Learning

- **arXiv**: https://arxiv.org/abs/2605.28809
- **Score**: 6.8 / 10
- **한줄 요약**: CLIP 기반 클래스 점진적 학습(CIL)에서 발생하는 파멸적 망각을 해결하기 위해, 속성 추출(Attribute Extraction)과 속성 집계(Attribute Aggregation) 과정을 분리하여 안정화하는 AREA 프레임워크를 제안함.
- **핵심 기여**: CIL의 성능 저하 원인을 '추출 드리프트'와 '집계 드리프트'라는 두 가지 구조적 요인으로 정의하고, 이를 각각 PGA와 VIB로 해결하여 최신 성능(SOTA)을 달성함.
- **방법론 개요**: PGA를 통해 초구면상에서 클래스 속성을 고정하여 추출을 안정화하고, VIB로 정규화된 경량 태스크 전문가를 통해 속성을 집계하며, 최적 운송(Optimal Transport) 기반의 동적 라우팅으로 추론을 수행함.
- **의의**: 기존의 '블랙박스'식 유사도 매칭에서 벗어나, 모델의 의사결정 과정을 속성 단위로 분해함으로써 점진적 학습 환경에서 모델의 안정성과 해석 가능성을 동시에 확보함.

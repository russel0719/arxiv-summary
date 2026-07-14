# CV 연구 동향 보고서 — 2026-07-01

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| 멀티모달 파운데이션 모델 | 모달리티 간 간섭 최소화 및 확장성 확보 | Rosetta: Composable Native Multimodal Pretraining |
| 비전 아키텍처 최적화 | 명시적 위치 임베딩 제거 및 공간적 귀납적 편향 학습 | Active Spatial Guidance: Eliminating Injected Positional Mechanisms in Vision Transformers |
| 3D 공간 추론 및 로보틱스 | 2D-3D 간극 해소 및 실시간 기하학적 일관성 유지 | Structured 4D Latent Predictive Model for Robot Planning |

> 핵심 메시지: 최신 컴퓨터 비전 연구는 대규모 파운데이션 모델의 효율적 확장과 더불어, 구조적 표현 학습 및 물리적 공간 추론을 통해 모델의 해석 가능성과 실시간 제어 능력을 극대화하는 방향으로 진화하고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Video Generation/Super-Resolution | 메모리 효율적 장편 생성 및 해상도 독립적 초해상도 | Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption |
| Image Personalization | 피사체와 문맥 정보 분리를 통한 편집성 향상 | Decoupled Guidance: Disentangling Subject and Context Pathways in Text-to-Image Personalization |
| 3D Scene Understanding | 비파라메트릭 입자 기반 실시간 장면 그래프 생성 | NoPA: Non-Parametric Online 3D Scene Graph Generation |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| 정보 이론적 분해 (Information Decomposition) | 뇌 미세구조 데이터의 해석 가능한 표현 학습 | BrainFIBRE: A Foundation Model via Information Decomposition for Brain Microstructure |
| 파라미터 흡수 및 증류 (Parametric Absorption) | 비디오 생성 시 KV 캐시 메모리 절감 | Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption |
| 구조적 표현 학습 (Compositional Primitive Fields) | 일반화된 카테고리 발견(GCD)의 효율성 개선 | Identifying Latent Concepts and Structures for Generalized Category Discovery |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| 로보틱스 (Robotics) | 4D 잠재 공간 기반 동역학 예측을 통한 로봇 계획 수립 | 복잡한 환경에서의 기하학적 일관된 제어 및 작업 수행 능력 향상 |
| 의료 영상 (Medical Imaging) | 자기지도 학습 기반 뇌 미세구조 정보 분해 | 신경 퇴행성 질환 진단의 해석 가능성 및 임상적 통찰력 확보 |

---

## 5. 개별 논문 요약

### 1. LeVLJEPA: End-to-End Vision-Language Pretraining Without Negatives

- **arXiv**: https://arxiv.org/abs/2607.00784
- **Score**: 8.5 / 10
- **한줄 요약**: LeVLJEPA는 대조 학습(Contrastive Learning) 없이 교차 모달 예측과 분포 정규화를 통해 비전-언어 모델을 사전 학습하는 새로운 프레임워크입니다.
- **핵심 기여**: 음성 샘플(negative samples)이나 복잡한 학습 스케줄 없이도 고품질의 밀집(dense) 시각적 특징을 추출하며, 기존 대조 학습 모델 대비 다운스트림 작업(VQA, 세그멘테이션 등)에서 우수한 성능을 입증했습니다.
- **방법론 개요**: 이미지와 텍스트 인코더에 각각 예측기(predictor)를 결합하고, SIGReg(Isotropic-Gaussian Regularization)를 통해 임베딩의 붕괴를 방지하며, 교차 모달 간의 MSE 손실을 최소화하는 방식을 사용합니다.
- **의의**: 기존 대조 학습 방식의 한계인 배치 크기 의존성을 제거하고, 시각적 토큰의 밀집 정보를 보존함으로써 비전-언어 모델의 추론 능력과 공간적 이해도를 효과적으로 향상시킵니다.

### 2. Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption

- **arXiv**: https://arxiv.org/abs/2607.00712
- **Score**: 8.2 / 10
- **한줄 요약**: ISPA(Instance-Specific Parametric Absorption)는 스트리밍 비디오 생성 시 발생하는 KV 캐시의 선형적 메모리 증가 문제를 해결하기 위해, 과거 토큰을 삭제하는 대신 모델 가중치에 정보를 흡수시키는 파라미터 증류 기법을 제안합니다.
- **핵심 기여**: 토큰 삭제로 인한 정보 손실 없이 KV 캐시 메모리 사용량을 최대 50% 절감하며, 테스트 타임 적응을 통해 긴 문맥의 시간적 일관성을 유지하는 새로운 메모리 관리 패러다임을 확립했습니다.
- **방법론 개요**: 초기 워밍업 단계에서 전체 어텐션과 로컬 어텐션의 출력 차이를 계산하고, 이를 최소자승법을 통해 모델 가중치에 반영(Absorption)함으로써, 이후 추론 과정에서 과거 KV 캐시를 삭제하고도 문맥을 유지할 수 있도록 설계되었습니다.
- **의의**: 기존의 토큰 프루닝 방식이 가진 '파괴적 망각' 문제를 극복하여, 메모리 제약이 심한 환경에서도 고품질의 장편 비디오를 끊김 없이 생성할 수 있는 확장 가능한 솔루션을 제공합니다.

### 3. Identifying Latent Concepts and Structures for Generalized Category Discovery

- **arXiv**: https://arxiv.org/abs/2607.00620
- **Score**: 8.2 / 10
- **한줄 요약**: 기존의 일반화된 카테고리 발견(GCD)에서 발생하는 표현의 비효율성을 해결하기 위해, 시각적 토큰을 재사용 가능한 저차원 '시각적 원시 요소(visual primitives)'로 분해하는 구조적 표현 학습 프레임워크를 제안합니다.
- **핵심 기여**: GCD 문제를 단순한 클러스터링 최적화가 아닌 구조적 표현 학습 문제로 재정의하고, 백본과 분류기 사이에 'Compositional Primitive Fields(CPF)' 모듈을 도입하여 표현 공간의 기하학적 품질을 개선했습니다.
- **방법론 개요**: 비전 백본의 출력인 패치 토큰을 학습 가능한 원시 요소(primitives)와 할당 행렬(assignment matrix)로 저차원 분해하여, 노이즈를 제거하고 공간적으로 구조화된 표현을 생성하는 플러그 앤 플레이 모듈을 적용합니다.
- **의의**: 기존의 고차원적이고 얽힌 표현은 미지의 카테고리 발견에 한계가 있으나, 본 연구는 원시 요소 기반의 구성을 통해 모델이 새로운 카테고리를 더 명확하게 식별할 수 있는 일반화된 귀납적 편향을 제공합니다.

### 4. Active Spatial Guidance: Eliminating Injected Positional Mechanisms in Vision Transformers

- **arXiv**: https://arxiv.org/abs/2607.00580
- **Score**: 8.2 / 10
- **한줄 요약**: Vision Transformer(ViT)에서 명시적인 위치 임베딩(Positional Embedding) 없이도 학습 단계의 보조 좌표 예측 목표(Active Spatial Guidance)를 통해 공간적 귀납적 편향을 효과적으로 학습할 수 있음을 입증함.
- **핵심 기여**: 위치 정보 주입을 아키텍처 수준에서 학습 목표 수준으로 전환하여, 추론 시 별도의 위치 인코딩 없이도 기존 모델을 능가하는 성능과 해상도 변화에 대한 강건성을 확보함.
- **방법론 개요**: 학습 시에만 최종 레이어에 2D 좌표 회귀 헤드를 부착하여 모델이 공간적 조직화를 스스로 학습하게 유도하고, 추론 시에는 해당 헤드를 제거하여 순수한 ViT 구조만으로 동작하게 설계함.
- **의의**: 고정된 위치 임베딩의 제약을 제거함으로써 모델의 유연성을 높이고, 복잡한 아키텍처 수정 없이도 고성능의 공간 인식 능력을 갖춘 경량화된 ViT 설계가 가능함을 보여줌.

### 5. Rosetta: Composable Native Multimodal Pretraining

- **arXiv**: https://arxiv.org/abs/2607.00293
- **Score**: 8.2 / 10
- **한줄 요약**: Rosetta는 멀티모달 사전 학습 시 발생하는 '망각-시너지 딜레마'를 해결하기 위해, 모듈형 아키텍처와 새로운 최적화 기법을 결합하여 기존 지식을 보존하면서 새로운 모달리티를 확장하는 프레임워크입니다.
- **핵심 기여**: 기존 MoE 모델의 고질적인 문제인 파괴적 그래디언트 간섭과 지식 덮어쓰기를 방지하고, 모달리티 간의 시너지를 극대화하며 확장 가능한 멀티모달 통합 구조를 제시했습니다.
- **방법론 개요**: 통합 어텐션(Unified Attention)을 통해 문맥을 공유하고, FFN 계층을 모달리티별 전문가와 공유 전문가로 분리한 뒤, 모멘텀 기반 직교 투영(MAOP) 기법으로 충돌하는 그래디언트를 제거하여 학습 안정성을 확보했습니다.
- **의의**: 파라미터 효율성을 유지하면서도 언어, 시각, 생성 등 다양한 모달리티를 충돌 없이 통합할 수 있어, 더 크고 복잡한 범용 멀티모달 파운데이션 모델로 나아가는 핵심적인 확장 경로를 제공합니다.

### 6. Structured 4D Latent Predictive Model for Robot Planning

- **arXiv**: https://arxiv.org/abs/2607.01166
- **Score**: 7.8 / 10
- **한줄 요약**: 로봇 제어를 위해 2D 영상 예측이 아닌, 3D 공간의 물리적 일관성을 유지하는 구조화된 4D 잠재 공간(Latent Space) 기반의 동역학 예측 모델을 제안함.
- **핵심 기여**: 2D-to-3D 간극을 해소하여 복잡한 조작 환경에서도 기하학적으로 일관된 3D 장면 예측을 가능하게 하고, 이를 통해 로봇 계획의 정확도와 일반화 성능을 획기적으로 향상함.
- **방법론 개요**: 다중 시점 관측치를 희소 복셀 그리드(Sparse Voxel Grid) 형태의 구조화된 3D 잠재 표현으로 인코딩한 뒤, 시간 흐름에 따른 3D 구조 변화를 예측하고 이를 역동역학 모듈을 통해 로봇의 저수준 제어 명령으로 변환함.
- **의의**: 기존 2D 기반 모델의 공간 추론 한계를 극복하고, 고충실도 3D 표현과 효율적인 계획 수립을 통합함으로써 실제 로봇 환경에서의 복잡한 작업 수행 및 환경 변화에 대한 강건한 대응을 가능하게 함.

### 7. AVSR-Diff: Scale-Agnostic Diffusion Priors for Temporally Consistent Arbitrary-Scale Video Super-Resolution

- **arXiv**: https://arxiv.org/abs/2607.00987
- **Score**: 7.8 / 10
- **한줄 요약**: AVSR-Diff는 잠재 확산 모델(LDM)의 고품질 생성 능력과 암시적 신경 표현(INR)의 임의 배율 확장성을 결합하여, 해상도에 독립적인 효율적인 비디오 초해상도(VSR) 프레임워크를 제안합니다.
- **핵심 기여**: 확산 과정과 해상도 복원 과정을 분리하여 연산 효율성을 극대화하고, TGFR과 SAFR 모듈을 통해 기존 확산 모델의 고질적 문제인 시간적 깜빡임(flickering)과 과도한 평활화(over-smoothing)를 해결했습니다.
- **방법론 개요**: 저해상도 잠재 공간에서 확산 모델을 통해 노이즈를 제거한 후, 연속적인 좌표 기반 디코더를 사용하여 임의의 배율로 영상을 재구성하는 2단계 분리형 아키텍처를 채택했습니다.
- **의의**: 기존 VSR 모델의 고정 배율 한계와 높은 연산 비용 문제를 극복함으로써, 다양한 해상도 환경에서 일관되고 고품질의 비디오 복원을 가능하게 하는 실용적이고 확장 가능한 솔루션을 제시합니다.

### 8. Decoupled Guidance: Disentangling Subject and Context Pathways in Text-to-Image Personalization

- **arXiv**: https://arxiv.org/abs/2607.00766
- **Score**: 7.8 / 10
- **한줄 요약**: 기존 개인화 모델의 '충실도-편집성 트레이드오프'가 단일 조건화 경로 내에서 발생하는 '주의 집중 붕괴(Attention Collapse)' 현상 때문임을 규명하고, 이를 해결하기 위한 'Decoupled Guidance(DeGu)' 프레임워크를 제안함.
- **핵심 기여**: 피사체와 문맥 정보를 분리하는 아키텍처를 통해 주의 집중 경쟁을 해소하고, 기존 모델 수정 없이 플러그 앤 플레이 방식으로 성능을 개선하는 효율적인 개인화 기법을 제시함.
- **방법론 개요**: 피사체와 문맥을 독립적인 두 개의 경로로 처리하는 'Dual-Stream Guidance'와 각 경로를 공간적으로 제어하는 'Spatial Mixing' 메커니즘을 도입하여 정보 간섭을 원천 차단함.
- **의의**: 개인화된 이미지 생성 시 피사체의 정체성을 유지하면서도 복잡한 텍스트 프롬프트를 충실히 반영할 수 있게 하여, 기존 모델의 구조적 한계였던 편집성 저하 문제를 근본적으로 해결함.

### 9. BrainFIBRE: A Foundation Model via Information Decomposition for Brain Microstructure

- **arXiv**: https://arxiv.org/abs/2607.00573
- **Score**: 7.8 / 10
- **한줄 요약**: BrainFIBRE는 NODDI 기반 미세구조 맵(NDI, ODI, FWF)의 복잡한 상호작용을 정보 이론적으로 분해하여 학습하는 최초의 뇌 미세구조 파운데이션 모델입니다.
- **핵심 기여**: 자기지도 학습 기반의 부분 정보 분해(SPID) 프레임워크를 도입하여, 레이블 없이도 미세구조적 고유·중복·상승 정보를 명시적으로 분리하고 해석 가능한 표현을 학습합니다.
- **방법론 개요**: 반사실적 후보 생성(CCC) 전략을 통해 모달리티를 체계적으로 교란하고, 혼합 전문가(MoE) 아키텍처를 활용하여 각 전문가가 특정 정보 유형(고유, 중복, 상승)을 전문적으로 처리하도록 설계되었습니다.
- **의의**: 기존 블랙박스 모델과 달리 신경생물학적 해석 가능성을 제공하며, 노화 및 신경 퇴행성 질환 진단 등 다양한 임상 과제에서 뛰어난 일반화 성능과 임상적 통찰력을 확보했습니다.

### 10. NoPA: Non-Parametric Online 3D Scene Graph Generation

- **arXiv**: https://arxiv.org/abs/2607.00529
- **Score**: 7.8 / 10
- **한줄 요약**: NoPA는 기존 파라메트릭(가우시안) 기반 3D 장면 그래프 생성의 기하학적 손실과 파편화 문제를 해결하기 위해, 고정 크기의 비파라메트릭 입자(particle) 표현을 도입한 실시간 온라인 3D 장면 그래프 생성 프레임워크입니다.
- **핵심 기여**: 기하학적 충실도와 연산 효율성 사이의 최적 균형을 달성했으며, MMD 기반의 효율적인 병합 전략을 통해 실시간 환경에서 객체 파편화를 방지하고 시간적 일관성을 확보했습니다.
- **방법론 개요**: 각 객체를 고정된 수의 입자 집합으로 모델링하고, 커널 밀도 추정(KDE)과 최대 평균 불일치(MMD)를 활용하여 다중 뷰에서 관측된 객체 후보들을 효율적으로 병합 및 업데이트합니다.
- **의의**: SLAM 의존성을 제거하여 연산 비용을 낮추면서도 복잡한 3D 기하 구조를 정밀하게 유지함으로써, 로봇 내비게이션 및 조작과 같은 실시간 임베디드 AI 작업의 신뢰성을 크게 향상시킵니다.

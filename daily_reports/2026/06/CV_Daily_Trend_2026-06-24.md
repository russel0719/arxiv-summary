# CV 연구 동향 보고서 — 2026-06-24

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| Robotics & World Models | 환경 변화에 대한 실시간 적응 및 물리적 상호작용 | In-Context World Modeling for Robotic Control |
| Generative AI | 생성 효율성 최적화 및 비디오 생성의 일관성 확보 | Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe |
| Computer Vision Security | 딥페이크 방어 및 적대적 공격에 대한 강건성 | Transferable Attack against Face Swapping in an Extended Space |
| Representation Learning | 기하학적 구조 보존 및 클래스 점진적 학습 | Geometry-Anchored Transport Framework for Exemplar-Free Class-Incremental Learning |

> 핵심 메시지: 물리적 세계 모델링과 생성 효율성을 결합하여 실시간 적응형 로봇 제어 및 고품질 비디오 생성을 구현하는 연구가 주류를 이룸


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Robotic Control | 문맥 내 학습을 통한 물리적 환경 적응 | In-Context World Modeling for Robotic Control |
| Video Generation | 자가회귀 확산 모델을 통한 스트리밍 생성 최적화 | Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe |
| Anomaly Detection | 하이퍼그래프를 이용한 논리적 이상 탐지 | Hypergraph Normal World Models for Logical Visual Anomaly Detection |
| 3D Hand Pose | 생체 역학적 사전 지식을 활용한 미터법 좌표 추정 | ScaleHP: Estimating Hand Pose in Metric Space |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Diffusion Distillation | 비디오 생성 모델의 학습 속도 및 효율성 개선 | Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe |
| In-Context Learning | 로봇 제어의 환경 일반화 | In-Context World Modeling for Robotic Control |
| Hypergraph Modeling | 객체 간 관계 및 구조적 이상 탐지 | Hypergraph Normal World Models for Logical Visual Anomaly Detection |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| Robotics & Computer Vision | 물리적 역학 추론을 통한 로봇 제어 | 미세 조정 없는 범용 로봇 배포 가능 |
| Biometrics & Computer Vision | 생체 역학적 사전 지식의 3D 포즈 추정 적용 | 깊이 센서 없이 정밀한 미터법 좌표 획득 |

---

## 5. 개별 논문 요약

### 1. In-Context World Modeling for Robotic Control

- **arXiv**: https://arxiv.org/abs/2606.26025
- **Score**: 8.2 / 10
- **한줄 요약**: ICWM은 로봇의 시스템 식별(system identification)을 매개변수 업데이트 없이 문맥 내 학습(In-Context Learning)으로 해결하여, 다양한 환경 변화에 적응하는 새로운 로봇 제어 패러다임을 제안합니다.
- **핵심 기여**: 작업별 데이터 없이도 로봇이 스스로 생성한 탐색적 상호작용을 통해 물리적 환경(카메라 시점, 로봇 형태 등)을 실시간으로 추론하고 적응하는 일반화 프레임워크를 구축했습니다.
- **방법론 개요**: 작업 수행 전 로봇이 무작위로 움직여 얻은 관측-행동 데이터를 모델의 컨텍스트 윈도우에 입력함으로써, 모델이 현재의 물리적 역학을 암묵적으로 파악하고 이를 바탕으로 최적의 행동을 생성하도록 설계되었습니다.
- **의의**: 기존 VLA 모델의 고질적인 문제인 환경 변화에 따른 성능 저하를 해결하고, 별도의 미세 조정이나 인간의 시연 없이도 새로운 환경에서 즉각적인 적응이 가능하게 함으로써 범용 로봇 배포의 핵심 기술을 제공합니다.

### 2. MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation

- **arXiv**: https://arxiv.org/abs/2606.26016
- **Score**: 7.8 / 10
- **한줄 요약**: MIMFlow는 마스크드 이미지 모델링(MIM)과 정규화 흐름(Normalizing Flow)을 결합하여, 고차원 이미지 데이터의 효율적인 생성과 밀도 추정을 수행하는 통합 프레임워크입니다.
- **핵심 기여**: 학습 가능한 쿼리 토큰을 도입하여 MIM의 확률적 마스킹 문제를 해결하고, 생성 작업을 의미론적 구조(Flow)와 픽셀 세부 정보(Decoder)로 분리하여 모델 용량 병목 현상을 해소했습니다.
- **방법론 개요**: VAE 기반 인코더로 마스크된 입력에서 고정된 길이의 의미론적 잠재 표현을 추출하고, 이를 정규화 흐름으로 밀도 추정하는 동시에 전문화된 디코더로 픽셀을 복원하는 엔드투엔드 최적화 방식을 사용합니다.
- **의의**: 기존 생성 모델의 고질적인 문제인 픽셀 수준의 노이즈 처리 부담을 줄여 생성 효율성을 극대화했으며, 표현 학습과 생성 모델링을 통합하여 성능과 효율성(파라미터 대비 성능)을 동시에 확보했습니다.

### 3. Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models

- **arXiv**: https://arxiv.org/abs/2606.25473
- **Score**: 6.8 / 10
- **한줄 요약**: Causal-rCM은 오프라인 Teacher-Forcing과 온라인 Self-Forcing을 결합하여 자가회귀(Autoregressive) 비디오 확산 모델의 학습 효율과 생성 품질을 동시에 최적화하는 통합 프레임워크입니다.
- **핵심 기여**: 연속 시간 일관성 모델(sCM)을 활용한 10배 빠른 학습 수렴, 자가회귀 비디오 생성에서의 SOTA 성능 달성, 그리고 인터랙티브 월드 모델을 위한 확장 가능한 오픈소스 레시피 제공.
- **방법론 개요**: FlashAttention-2 JVP 커널을 활용한 Teacher-Forcing으로 초기 안정성을 확보하고, DMD(Distribution Matching Distillation) 기반의 Self-Forcing으로 온-폴리시(on-policy) 정교화를 수행하는 하이브리드 파이프라인입니다.
- **의의**: 기존 확산 모델의 학습 불안정성과 계산 복잡성 문제를 해결하여, 실시간 스트리밍 비디오 생성 및 복잡한 환경에서의 인터랙티브 월드 시뮬레이션을 가능하게 하는 실용적인 인프라를 구축했습니다.

### 4. Transferable Attack against Face Swapping in an Extended Space

- **arXiv**: https://arxiv.org/abs/2606.25376
- **Score**: 6.8 / 10
- **한줄 요약**: 주제 불변형(subject-agnostic) 얼굴 교체 모델을 무력화하기 위해 가산적 노이즈와 재조명(relighting) 함수를 결합한 새로운 적대적 공격 프레임워크 'AIR' 제안.
- **핵심 기여**: 적응형 변환 불변(ATI) 연산을 통해 공격의 전이성을 높이는 동시에, 시각적 왜곡을 최소화하여 공격 성공률(ASR)과 이미지 품질 간의 균형을 최적화함.
- **방법론 개요**: 얼굴 인식 모델 앙상블을 타겟으로 하는 '가산적 식별 공격(AIA)'과 이미지의 조명을 조작하여 모델의 특징 추출을 방해하는 '재조명 기능 공격(RFA)'을 결합한 이중 모달리티 접근법.
- **의의**: 기존의 쿼리 기반 공격이 가진 비효율성과 블랙박스 모델에 대한 낮은 전이성 문제를 해결하여, 딥페이크 생성으로부터 개인의 이미지를 보호하는 실용적이고 강력한 사전 방어 기술을 제공함.

### 5. Hypergraph Normal World Models for Logical Visual Anomaly Detection

- **arXiv**: https://arxiv.org/abs/2606.25368
- **Score**: 6.8 / 10
- **한줄 요약**: 개별 구성 요소는 정상이지만 전체적인 배치나 관계가 비정상인 '논리적 이상(logical anomaly)'을 탐지하기 위해 하이퍼그래프 기반의 세계 모델을 제안함.
- **핵심 기여**: 기존의 국소적 특징 매칭 패러다임을 넘어, 고차원적 구조 관계를 모델링하는 '관계적 정상성(relational normality)' 개념을 도입하여 MVTec LOCO 벤치마크에서 성능을 크게 향상함.
- **방법론 개요**: DINOv2 특징 추출기를 활용해 토큰을 계층화하고, 이를 하이퍼그래프로 구성하여 다중 관계를 모델링한 뒤, '정보 지수(Information Quotient)'를 통해 구조적 일관성을 평가함.
- **의의**: 단순한 픽셀 단위의 결함 탐지를 넘어, 객체의 개수나 공간적 배치 등 복잡한 논리적 오류를 효과적으로 식별함으로써 시각적 세계에 대한 고차원적 이해를 가능하게 함.

### 6. Geometry-Anchored Transport Framework for Exemplar-Free Class-Incremental Learning

- **arXiv**: https://arxiv.org/abs/2606.25347
- **Score**: 6.8 / 10
- **한줄 요약**: 예제 데이터 없이 클래스 점진적 학습(EFCIL)을 수행할 때 발생하는 표현 드리프트와 기하학적 왜곡 문제를 해결하기 위해, 학습 단계에서부터 기하학적 제약을 통합하는 'Geometry-Anchored Transport Framework(GATF)'를 제안함.
- **핵심 기여**: 사후 보정 방식에서 벗어나, 학습 과정 중에 분석적 기하학적 앵커(AGA)와 위상 보존 제약을 결합함으로써 기존 클래스의 매니폴드 구조를 안정적으로 유지하고 표현 드리프트를 근본적으로 억제함.
- **방법론 개요**: 마할라노비스 거리 기반의 분석적 가우시안 앵커(AGA)를 통해 전역적 이방성 드리프트를 보정하고, 학습 중 모델의 백본이 이전 클래스의 국소적 위상 구조를 유지하도록 강제하는 위상 인식 진화(Topology-Aware Evolution) 기법을 적용함.
- **의의**: 기존의 분리된 최적화 방식이 가진 기하학적 왜곡 한계를 극복하여, 메모리 버퍼 없이도 클래스 간 경계를 안정적으로 유지하고 점진적 학습 환경에서 모델의 분류 성능을 획기적으로 향상시킴.

### 7. ScaleHP: Estimating Hand Pose in Metric Space

- **arXiv**: https://arxiv.org/abs/2606.25619
- **Score**: 6.5 / 10
- **한줄 요약**: ScaleHP는 외부 깊이 센서 없이 인간의 골격 비율이라는 생체 역학적 사전 지식을 활용하여 단일 이미지로부터 손의 절대적인 미터법 크기와 위치를 추정하는 프레임워크입니다.
- **핵심 기여**: 기존의 상대적 좌표 추정 방식에서 벗어나, 손의 기하학적 구조와 척도를 직접 학습함으로써 단안 카메라 환경에서의 고질적인 척도 모호성(scale ambiguity) 문제를 해결했습니다.
- **방법론 개요**: 트랜스포머 기반의 '스케일 토큰'을 통해 다중 스케일 특징을 융합하고, 관절 수준의 기하학적 제약 조건을 활용하여 2D 이미지에서 3D 미터법 좌표로 변환하는 일체형(one-stage) 파이프라인을 구축했습니다.
- **의의**: 별도의 깊이 정보 없이도 정밀한 절대 좌표 추정이 가능해짐에 따라, 로봇 조작 및 원격 제어와 같이 실제 물리적 공간에서의 정확한 상호작용이 필수적인 분야에서 강력한 범용성을 제공합니다.

### 8. DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation

- **arXiv**: https://arxiv.org/abs/2606.26058
- **Score**: 6.2 / 10
- **한줄 요약**: 피사체 고유의 정체성과 도메인별 문맥을 분리하여, 높은 피사체 충실도와 유연한 도메인 간 변환(cross-domain adaptation)을 동시에 달성하는 새로운 S2V(Subject-to-Video) 프레임워크 제안.
- **핵심 기여**: 기존 S2V 모델의 고질적 문제인 '피사체 충실도'와 '생성 유연성' 간의 상충 관계를 해결하고, 다양한 도메인에서 일관된 피사체 유지가 가능한 오픈 도메인 비디오 생성 기술 확보.
- **방법론 개요**: 비디오와 참조 이미지의 특징을 분리 처리하는 Domain-MoT, 공간적 오정렬을 방지하는 DualRoPE, 그리고 피사체 고유 특징 추출을 강화하는 Cross-Pair Consistent Loss를 핵심 아키텍처로 구성.
- **의의**: 단순한 피사체 복제를 넘어, 사용자의 프롬프트에 따라 피사체의 정체성을 유지하면서도 스타일이나 환경을 자유롭게 변형할 수 있는 창의적이고 범용적인 비디오 생성 환경을 제공함.

# CV 연구 동향 보고서 — 2026-04-16

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| Efficient Vision Modeling | 기존 순차적 스캐닝 및 비선형 최적화의 비효율성 해결 | HAMSA: Scanning-Free Vision State Space Models via SpectralPulseNet |
| 3D Reconstruction & Generation | 카메라 광선 의존성 탈피 및 물리 기반의 고충실도 아바타 생성 | TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens |
| Machine Unlearning | 모델 내부 표현 수준에서의 근본적인 정보 삭제 및 신뢰성 확보 | Class Unlearning via Depth-Aware Removal of Forget-Specific Directions |
| Sensor Fusion & Robotics | 이질적 모달리티(이벤트/RGB)의 정렬 및 자율주행의 안전성 강화 | RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework |

> 핵심 메시지: 컴퓨터 비전 연구는 효율적인 비순차적 모델링, 물리 기반의 3D 생성, 그리고 내부 표현 수준의 신뢰성 높은 언러닝 기술로 패러다임이 전환되고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| 3D Reconstruction | 피드포워드 3DGS 재구성 및 3D 헤드 아바타의 물리적 변형 구현 | TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens |
| Imaging & Restoration | 스파이크 카메라를 활용한 고속 HDR 영상 복원 | High-Speed Full-Color HDR Imaging via Unwrapping Modulo-Encoded Spike Streams |
| Autonomous Driving | 생성 모델과 RL을 결합한 안전한 모션 플래닝 | RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Spectral/Frequency Domain Modeling | SSM의 순차적 스캐닝 문제를 FFT 기반의 병렬 처리로 대체 | HAMSA: Scanning-Free Vision State Space Models via SpectralPulseNet |
| Closed-form Algebraic Optimization | 반복적 최적화 없이 다항식 시스템을 통한 자세 추정 | Efficient closed-form approaches for pose estimation using Sylvester forms |
| Diffusion-based Generative Priors | 3D 형상 편집 및 HDR 영상 재구성의 사전 지식 활용 | Beyond Prompts: Unconditional 3D Inversion for Out-of-Distribution Shapes |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| Robotics & Autonomous Driving | 강화학습과 생성 모델의 결합을 통한 실시간 주행 정책 최적화 | 복잡한 도시 환경에서의 충돌률 감소 및 주행 안전성 확보 |
| Computer Vision & Physics | PBD(Position-Based Dynamics)를 활용한 3D 아바타 머리카락 변형 | 데이터 효율적인 원샷 아바타의 물리적 사실성 극대화 |

---

## 5. 개별 논문 요약

### 1. HAMSA: Scanning-Free Vision State Space Models via SpectralPulseNet

- **arXiv**: https://arxiv.org/abs/2604.14724
- **Score**: 8.8 / 10
- **한줄 요약**: 기존 상태 공간 모델(SSM)의 순차적 스캐닝 방식이 가진 비효율성과 인과적 편향 문제를 해결하기 위해, 주파수 도메인에서 FFT를 활용한 스캐닝 없는(scanning-free) 아키텍처 HAMSA를 제안함.
- **핵심 기여**: 순차적 스캐닝을 완전히 제거하여 $O(L \log L)$의 계산 복잡도를 달성하고, ImageNet-1K에서 85.7%의 SOTA 성능과 함께 기존 모델 대비 추론 속도 2.2배 향상 및 메모리 효율성을 입증함.
- **방법론 개요**: Fast Fourier Transform(FFT)을 통해 입력을 주파수 도메인으로 변환하고, 학습 가능한 복소수 커널을 사용하여 요소별 곱셈으로 공간적 의존성을 모델링하며, SpectralPulseNet과 SAGU를 통해 적응형 게이팅을 수행함.
- **의의**: 이미지의 비순차적 특성과 SSM의 순차적 구조 사이의 불일치를 근본적으로 해결함으로써, 복잡한 스캐닝 전략 없이도 더 높은 성능과 효율성을 동시에 확보할 수 있는 새로운 비전 모델링 패러다임을 제시함.

### 2. High-Speed Full-Color HDR Imaging via Unwrapping Modulo-Encoded Spike Streams

- **arXiv**: https://arxiv.org/abs/2604.14632
- **Score**: 8.5 / 10
- **한줄 요약**: 모듈로 인코딩된 스파이크 카메라 하드웨어와 확산 모델 기반의 비반복적 재구성 알고리즘을 결합하여 고속, 고대역폭 효율의 풀컬러 HDR 이미징을 구현함.
- **핵심 기여**: 기존 HDR 이미징의 고질적 문제인 모션 아티팩트와 정보 손실을 해결하고, 데이터 대역폭을 약 70% 절감하면서 1000 FPS의 고속 HDR 영상을 실시간으로 획득 가능하게 함.
- **방법론 개요**: 노출이 분리된 모듈로 센싱 프레임워크를 하드웨어에 적용하고, 확산 생성 모델의 사전 지식과 물리적 제약 조건을 결합한 반복 연산 없는 언래핑(unwrapping) 알고리즘을 통해 HDR 영상을 복원함.
- **의의**: 기존의 다중 노출 방식(모션 블러)과 단일 샷 방식(정보 손실)의 한계를 극복하여, 고속 동적 환경에서도 물리적으로 정확하고 고품질의 HDR 데이터를 효율적으로 획득할 수 있는 실용적인 솔루션을 제시함.

### 3. TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens

- **arXiv**: https://arxiv.org/abs/2604.15239
- **Score**: 7.8 / 10
- **한줄 요약**: TokenGS는 기존의 카메라 광선 기반 깊이 회귀 방식에서 벗어나, 학습 가능한 3D 가우시안 토큰을 사용하여 3D 좌표를 직접 회귀하는 인코더-디코더 기반의 피드포워드 3DGS 재구성 프레임워크를 제안합니다.
- **핵심 기여**: 입력 해상도와 뷰 수로부터 가우시안 표현을 완전히 분리하여, 카메라 포즈 노이즈에 대한 강건성을 높이고, 장면의 복잡도에 따라 가우시안을 유연하게 할당하며, 가시성 손실(Visibility Loss)을 통해 훈련 안정성을 확보했습니다.
- **방법론 개요**: 인코더가 입력 이미지와 카메라 파라미터를 토큰화하고, 디코더가 교차 어텐션을 통해 3D 가우시안 파라미터를 직접 예측합니다. 이때, 모든 뷰에서 벗어난 가우시안을 제약하는 가시성 손실(Visibility Loss)을 도입하여 훈련 중 발생하는 '제로 그래디언트' 문제를 해결하고 기하학적 정규화를 수행합니다.
- **의의**: 기존 방식의 고질적인 문제인 카메라 광선 의존성을 제거함으로써 복잡한 장면의 완성도를 높이고, 정적/동적 장면을 아우르는 범용적인 3D 재구성 성능을 달성하여 차세대 피드포워드 신경망 재구성의 새로운 표준을 제시합니다.

### 4. Class Unlearning via Depth-Aware Removal of Forget-Specific Directions

- **arXiv**: https://arxiv.org/abs/2604.15166
- **Score**: 7.8 / 10
- **한줄 요약**: 기존 머신 언러닝 기법들이 내부 표현을 제거하지 못하고 출력층만 가리는 '표면적 망각' 문제를 해결하기 위해, 모델 내부 표현 공간에서 망각 대상 클래스의 정보를 직접 제거하는 DAMP(Depth-Aware Modulation by Projection) 기법을 제안함.
- **핵심 기여**: 기존 기법들보다 월등한 선택성(Selectivity)을 확보하고, 재학습(Retraining)이라는 골드 스탠다드에 근접한 성능을 보이면서도 계산 효율성을 극대화한 폐쇄형(closed-form) 가중치 수술 기법을 개발함.
- **방법론 개요**: 망각 클래스와 유지 클래스의 프로토타입 차이를 기반으로 '망각 방향'을 추출한 뒤, 이를 투영(Projection)을 통해 제거함. 이때 층별 깊이에 따라 편집 강도를 조절하는 파라미터 없는 스케일링 규칙을 적용하여 모델의 유용성을 보존함.
- **의의**: 기존 방식들이 겪는 망각-유지 간의 성능 상충(trade-off) 문제를 효과적으로 해결하며, 단순 출력값 조작이 아닌 내부 표현 수준에서의 근본적인 정보 삭제를 가능하게 하여 언러닝의 신뢰성과 효율성을 동시에 달성함.

### 5. Beyond Prompts: Unconditional 3D Inversion for Out-of-Distribution Shapes

- **arXiv**: https://arxiv.org/abs/2604.14914
- **Score**: 7.8 / 10
- **한줄 요약**: 텍스트 기반 3D 생성 모델에서 발생하는 '잠재 싱크 트랩(latent sink traps)' 문제를 규명하고, 이를 해결하여 고충실도 3D 형상 편집을 가능하게 하는 프레임워크를 제안함.
- **핵심 기여**: 3D 생성 모델의 언어적 조건화와 기하학적 표현 능력 간의 불일치인 '싱크 트랩' 현상을 정의하고, 무조건적 사전(unconditional prior)을 활용한 궤적 안정화 기법을 통해 이를 극복함.
- **방법론 개요**: Rectified Flow 기반의 역방향 오일러 적분과 Null-Text 최적화(NTI)를 결합하여, 3D 에셋을 잠재 공간으로 정확히 역변환한 뒤 텍스트 프롬프트를 통해 형상을 편집함.
- **의의**: 외부 2D 모델이나 마스크 등 보조 도구 없이도 네이티브 3D 생성 모델만으로 고품질의 3D 형상 편집이 가능해져, 기존 3D 생성 파이프라인의 한계를 극복하고 편집 효율성을 획기적으로 개선함.

### 6. Bidirectional Cross-Modal Prompting for Event-Frame Asymmetric Stereo

- **arXiv**: https://arxiv.org/abs/2604.15312
- **Score**: 6.8 / 10
- **한줄 요약**: 이벤트 카메라와 RGB 프레임 간의 이질적인 데이터 특성(모달리티 격차)을 극복하기 위해 양방향 교차 모달 프롬프팅(Bi-CMPStereo)을 활용한 하이브리드 스테레오 매칭 프레임워크 제안.
- **핵심 기여**: 도메인별 고유 정보를 보존하면서도 두 모달리티를 정렬하는 '스테레오 정준화 제약(SCC)'과 '교차 도메인 임베딩 어댑터(CDEA)'를 도입하여 기존 비대칭 스테레오 매칭의 성능 한계를 극복함.
- **방법론 개요**: 이벤트와 프레임 데이터를 서로의 도메인으로 투영하는 양방향 프롬프팅 구조를 채택하고, 타겟 도메인을 정준 공간(Canonical Space)으로 설정하여 계층적 시각 변환 및 반복적 정제 과정을 통해 정밀한 시차(disparity)를 추정함.
- **의의**: 기존 방식의 정보 손실 문제를 해결하여 고속 이동 및 저조도 환경에서도 강인한 3D 인식 성능을 제공하며, 고가의 장비 없이도 이벤트와 프레임의 상호 보완적 강점을 극대화한 효율적인 뎁스 추정 솔루션을 제시함.

### 7. RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework

- **arXiv**: https://arxiv.org/abs/2604.15308
- **Score**: 6.8 / 10
- **한줄 요약**: RAD-2는 확산 모델 기반의 생성자와 RL 기반의 판별자를 결합하여, 자율주행 모션 플래닝의 안정성과 안전성을 극대화하는 하이브리드 프레임워크입니다.
- **핵심 기여**: 기존 모방 학습의 한계를 극복하고, TC-GRPO 최적화 기법과 BEV-Warp 시뮬레이션을 통해 충돌률을 56% 감소시키며 실시간 주행 성능을 획기적으로 개선했습니다.
- **방법론 개요**: 확산 모델로 다양한 궤적을 생성하고, 폐루프 환경에서 RL 판별자가 이를 평가 및 재순위화하며, TC-GRPO를 통해 시간적 일관성을 유지하며 정책을 최적화합니다.
- **의의**: 고차원 궤적 최적화의 불안정성과 희소 보상 문제를 해결함으로써, 복잡한 도시 환경에서 더 안전하고 인간과 유사한 주행 정책을 학습할 수 있는 확장 가능한 경로를 제시합니다.

### 8. KVNN: Learnable Multi-Kernel Volterra Neural Networks

- **arXiv**: https://arxiv.org/abs/2604.15141
- **Score**: 6.8 / 10
- **한줄 요약**: 표준 컨볼루션을 대체하여 고차 비선형 특징 상호작용을 효율적으로 학습하는 커널화된 볼테라 신경망(kVNN) 아키텍처 제안.
- **핵심 기여**: 고차 상호작용을 모델링하면서도 계산 복잡도를 획기적으로 낮춘 모듈형 레이어 설계 및 성능-효율성 간의 최적의 트레이드오프 달성.
- **방법론 개요**: 다양한 다항식 차수를 병렬 브랜치로 구성하고, 학습 가능한 커널 중심을 사용하여 볼테라 급수를 구조적으로 근사하는 플러그 앤 플레이 방식의 레이어 구현.
- **의의**: 기존 딥러닝의 선형적 한계를 극복하고, 고차원 특징 모델링의 계산 비용 문제를 해결함으로써 대규모 모델에서도 정교한 비선형 학습을 가능하게 함.

### 9. One-shot Compositional 3D Head Avatars with Deformable Hair

- **arXiv**: https://arxiv.org/abs/2604.14782
- **Score**: 6.8 / 10
- **한줄 요약**: 단일 이미지 기반의 고충실도 3D 헤드 아바타 생성을 위해 얼굴과 머리카락을 명시적으로 분리하고 각각에 최적화된 변형 모델을 적용하는 구성적(compositional) 프레임워크 제안.
- **핵심 기여**: 얼굴에는 FLAME 기반 리깅을, 머리카락에는 PBD(Position-Based Dynamics) 기반 케이지 변형을 적용하여 기존 일체형 모델의 부자연스러운 변형 문제를 해결하고 물리적으로 타당한 동적 애니메이션 구현.
- **방법론 개요**: 입력 이미지를 얼굴과 머리카락으로 분리하여 3D Gaussian Splatting으로 표현하고, 얼굴은 메쉬에 고정하며 머리카락은 PBD로 구동되는 케이지 구조를 통해 실시간 물리 기반 애니메이션을 생성하는 방식.
- **의의**: 기존 원샷 아바타 모델의 고질적인 문제인 '충실도와 일반화의 상충 관계' 및 '머리카락의 비현실적 변형'을 해결함으로써, 데이터 효율성과 시각적 사실성을 동시에 확보한 실용적인 아바타 생성 기술을 제시함.

### 10. Efficient closed-form approaches for pose estimation using Sylvester forms

- **arXiv**: https://arxiv.org/abs/2604.14747
- **Score**: 6.5 / 10
- **한줄 요약**: 비선형 최소자승법 기반의 자세 추정 문제를 다항 방정식 시스템으로 재구성하여 대수적 폐쇄형(closed-form) 해법을 제시함.
- **핵심 기여**: 실베스터 행렬 및 행렬 연필(matrix pencil) 구조를 활용해 계산 복잡도를 획기적으로 낮춘 효율적이고 수치적으로 안정적인 새로운 다항식 솔버 개발.
- **방법론 개요**: 매개변수 제거(elimination) 기법과 다항식의 차수 축소, 그리고 시스템을 일반화된 고유값 문제(generalized eigenvalue problem)로 변환하는 선형 대수적 접근 방식을 사용함.
- **의의**: 반복적인 비선형 최적화 방식의 지연 시간을 제거하여 실시간 컴퓨터 비전 작업(3D 등록, PnP 문제 등)에서 빠르고 정확한 자세 추정을 가능하게 함.

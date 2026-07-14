# CV 연구 동향 보고서 — 2026-05-22

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| 비디오 생성 및 편집 | 장기 일관성 유지 및 연산 효율성 확보 | EM-Vid: Training-Free Entity-Centric Memory for Efficient and Consistent Multi-Shot Video Generation |
| 3D 재구성 및 추적 | 실시간 스트리밍 환경에서의 드리프트 방지 및 기하학적 정밀도 | HorizonStream: Long-Horizon Attention for Streaming 3D Reconstruction |
| 생성형 모델 최적화 | 고해상도 합성 시 연산 비용 절감 및 구조적 충실도 개선 | PiD: Fast and High-Resolution Latent Decoding with Pixel Diffusion |
| 멀티모달 추론 | 시각적 증거를 활용한 논리적 추론 능력 강화 | ETCHR: Editing To Clarify and Harness Reasoning |

> 핵심 메시지: 최신 컴퓨터 비전 연구는 생성형 모델의 효율적 추론과 물리적 일관성 확보를 위해 메모리 최적화, 수학적 최적화 공간 재정의, 그리고 멀티모달 추론의 시각적 증거 활용에 집중하고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Video Generation | 희소 메모리 및 동적 어텐션을 통한 효율적인 일관성 확보 | DFSAttn: Dynamic Fine-grained Sparse Attention for Efficient Video Generation |
| 3D Reconstruction | 생성형 사전 지식을 활용한 다중 뷰 장면 복원 | GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction |
| Image Restoration | 소볼레프 공간 최적화를 통한 초해상도 복원 품질 향상 | Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution |
| Object Tracking | 손-객체 상호작용을 활용한 6DoF 포즈 추적 | ComPose: When to Trust Hands for Object Pose Tracking |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Sparse Attention & Memory | 비디오 생성 시 연산 복잡도 감소 및 장기 기억 유지 | DFSAttn: Dynamic Fine-grained Sparse Attention for Efficient Video Generation |
| Neural Operators | 의료 영상의 공간 가변적 디블러링 | Discontinuous Galerkin Neural Operator for Pathology Defocus Deblurring |
| Self-Supervised Motion Priors | 물리적 실재감 향상을 위한 비디오 생성 가이드 | LaMo: Self-Supervised Latent Motion Priors for Physical Realism in Video Generation |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| 의료 영상 분석 | 불연속 갤러킨 프레임워크를 활용한 병리 영상 디블러링 | 물리적 해석력을 갖춘 고정밀 의료 영상 복원 |
| Embodied AI (로보틱스) | 손-객체 상호작용 정보를 활용한 3D 포즈 추적 | 인간 행동 관찰을 통한 로봇 조작 기술의 실용화 |

---

## 5. 개별 논문 요약

### 1. HorizonStream: Long-Horizon Attention for Streaming 3D Reconstruction

- **arXiv**: https://arxiv.org/abs/2605.23889
- **Score**: 8.8 / 10
- **한줄 요약**: HorizonStream은 시공간적 기하학적 증거를 장기 및 단기 커널로 분리하여 처리함으로써, 실시간 3D 재구성에서 발생하는 정보 손실과 메모리 포화 문제를 해결하는 스트리밍 트랜스포머 아키텍처입니다.
- **핵심 기여**: 기하학적 영향 커널(Geometric Influence Kernel)의 인수분해를 통해 장기 기억의 안정성과 단기 매칭의 정밀도를 동시에 확보했으며, O(1)의 일정한 메모리 복잡도로 1만 프레임 이상의 장기 시퀀스에서도 드리프트 없는 추론을 가능하게 했습니다.
- **방법론 개요**: 채널별 감쇠율을 학습하는 '기하학적 선형 어텐션'으로 장기 의존성을 관리하고, 시공간적 RoPE를 활용한 '기하학적 로컬 어텐션'으로 정밀한 3D 매칭을 수행하며, Metric Readout Token을 통해 메트릭 스케일과 포즈를 추출합니다.
- **의의**: 기존 스트리밍 방식의 고질적인 문제인 포즈 지터, 스케일 불안정성, 상태 붕괴를 근본적으로 해결하여, 실시간 온라인 3D 재구성 분야에서 확장성과 정밀도를 새로운 수준으로 끌어올렸습니다.

### 2. PiD: Fast and High-Resolution Latent Decoding with Pixel Diffusion

- **arXiv**: https://arxiv.org/abs/2605.23902
- **Score**: 8.2 / 10
- **한줄 요약**: PiD(Pixel Diffusion Decoder)는 기존의 '디코딩 후 업샘플링'이라는 다단계 파이프라인을 단일 조건부 픽셀 확산 생성 과정으로 통합한 고해상도 이미지 합성 프레임워크입니다.
- **핵심 기여**: 별도의 업샘플링 단계 없이 잠재 표현에서 직접 고해상도 이미지를 생성하여 추론 효율성을 극대화하고, 기존 디코더가 놓치기 쉬운 고주파 세부 묘사 능력을 크게 향상시켰습니다.
- **방법론 개요**: 잠재 표현(latent)과 텍스트 조건을 입력으로 받아 픽셀 공간에서 직접 확산 모델을 수행하며, 증류(Distillation) 기법을 통해 4단계의 짧은 추론 과정만으로 고해상도 출력을 생성합니다.
- **의의**: 복잡한 다단계 파이프라인을 제거하여 연산 비용을 획기적으로 줄이면서도, 4K급 고해상도 이미지에서 우수한 시각적 품질을 보장하는 범용적인 차세대 디코딩 솔루션을 제시합니다.

### 3. Discontinuous Galerkin Neural Operator for Pathology Defocus Deblurring

- **arXiv**: https://arxiv.org/abs/2605.23282
- **Score**: 8.2 / 10
- **한줄 요약**: 병리 현미경 영상의 공간 가변적이고 불연속적인 디포커스 블러를 해결하기 위해, 전역적 연산자 대신 불연속 갤러킨(DG) 프레임워크를 도입한 신경 연산자(DGNO)를 제안함.
- **핵심 기여**: 기존 신경 연산자의 전역적 연속성 가정을 탈피하여, 요소별 국소 연산자와 경계면 플럭스를 통해 물리적 특성을 반영한 고성능·고효율 디블러링 아키텍처를 구축함.
- **방법론 개요**: 이미지 도메인을 국소 요소로 분할하고, 각 요소 내의 볼륨 연산자와 요소 간의 인터페이스 수치적 플럭스를 결합하여 공간적으로 변화하는 적분 커널을 모델링함.
- **의의**: 기존의 픽셀 기반 블랙박스 모델이 가진 물리적 해석력 부족과 공간 가변적 블러 처리의 한계를 극복하여, 의료 영상 복원 분야에서 더 높은 정밀도와 효율성을 제공함.

### 4. Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution

- **arXiv**: https://arxiv.org/abs/2605.23264
- **Score**: 8.2 / 10
- **한줄 요약**: ASASR은 생성형 초해상도 모델의 고질적인 문제인 '스펙트럼 불일치'를 해결하기 위해, 최적화 공간을 유클리드 공간에서 소볼레프(Sobolev) 공간으로 재정의하고 적대적 학습을 결합한 프레임워크입니다.
- **핵심 기여**: 기존의 주파수 무관적인 L2 손실 함수가 가진 한계를 이론적으로 규명하고, Riesz 표현 정리와 소볼레프 노름을 도입하여 자연스러운 이미지 통계와 일치하는 구조적 복원력을 확보했습니다.
- **방법론 개요**: 색상화된 가우시안 노이즈(Colored Gaussian Noise)를 통해 노이즈 커널을 자연 이미지의 스펙트럼 감쇠 특성에 맞게 조정하고, 적대적 학습을 통해 구조적 오류를 효과적으로 탐색하는 소볼레프 기반 최적화 기법을 적용했습니다.
- **의의**: 기존 생성 모델이 겪던 고주파 영역의 환각(hallucination) 현상과 구조적 왜곡을 근본적으로 해결함으로써, 생성적 사실성과 구조적 충실도를 동시에 달성하는 고성능 초해상도 복원 기술을 제시합니다.

### 5. LaMo: Self-Supervised Latent Motion Priors for Physical Realism in Video Generation

- **arXiv**: https://arxiv.org/abs/2605.23878
- **Score**: 7.8 / 10
- **한줄 요약**: LaMo는 외부 물리 엔진이나 추가 데이터셋 없이, 비디오 데이터 자체에서 잠재적 모션 패턴을 학습하여 비디오 생성 모델의 물리적 실재감과 시간적 일관성을 향상시키는 자기지도 학습 프레임워크입니다.
- **핵심 기여**: 외부 감독 없이도 잠재 공간 내에서 거시적(Macro) 움직임과 미시적(Micro) 움직임을 분리하여 학습함으로써, 기존 비디오 확산 모델의 구조 변경 없이 물리적 일관성을 개선하는 플러그 앤 플레이 솔루션을 제시했습니다.
- **방법론 개요**: 학습 단계에서는 'Motion Drift Loss'를 통해 잠재 공간의 프레임 간 변화를 정렬하고, 추론 단계에서는 'Motion Prior Guidance'를 통해 미시적 움직임 필드를 적용하여 생성 과정의 시간적 정교함을 높입니다.
- **의의**: 기존의 복잡한 물리 시뮬레이터나 외부 교사 모델 의존성을 제거하여, 범용적인 비디오 생성 모델이 물리 법칙을 내재화할 수 있는 효율적이고 확장 가능한 경로를 제공합니다.

### 6. DFSAttn: Dynamic Fine-grained Sparse Attention for Efficient Video Generation

- **arXiv**: https://arxiv.org/abs/2605.23445
- **Score**: 7.8 / 10
- **한줄 요약**: 비디오 확산 모델(DiT)의 3D 전체 어텐션 연산에서 발생하는 이차 복잡도 문제를 해결하기 위해, 하드웨어 효율적인 동적 블록 희소화(Dynamic Block Sparsification) 프레임워크인 DFSAttn을 제안함.
- **핵심 기여**: 훈련 없이도 고해상도 비디오 생성 품질을 유지하면서 최대 2.1배의 속도 향상을 달성했으며, 어텐션 리콜에 대한 이론적 하한을 도출하여 희소화 품질을 보장함.
- **방법론 개요**: 3D 힐베르트 곡선을 이용한 토큰 재정렬로 공간적 지역성을 보존하고, 계층적 블록 중요도 평가를 통해 핵심 블록을 선별하며, 희소 마스크 캐싱 및 적응형 비율 조정을 통해 연산 효율을 최적화함.
- **의의**: 기존의 정적/거친 희소화 방식이 가진 품질 저하 문제를 해결하고, 특수 커널 없이도 GPU 하드웨어 가속을 극대화하여 고품질 비디오 생성의 실용성을 크게 높임.

### 7. ETCHR: Editing To Clarify and Harness Reasoning

- **arXiv**: https://arxiv.org/abs/2605.23897
- **Score**: 6.8 / 10
- **한줄 요약**: ETCHR은 추상적인 시각적 추론을 구체적인 이미지 편집 작업으로 변환하여, MLLM이 중간 시각적 증거를 생성하고 검증하며 문제를 해결하도록 돕는 'Think with Images' 프레임워크입니다.
- **핵심 기여**: MLLM과 독립적으로 작동하는 모듈형 편집기 아키텍처를 제안하여, 기존 모델의 재학습 없이도 복잡한 공간 및 논리적 추론 성능을 4.6%~5.5% 향상시켰습니다.
- **방법론 개요**: 추론 지향적 편집을 위한 지도 미세 조정(Reasoning Imitation)과 강화 학습(Reasoning Enhancement)을 거친 후, 추론 시 '편집-검증-추론'의 순환 루프를 통해 신뢰할 수 있는 시각적 중간 상태를 생성합니다.
- **의의**: 기존의 텍스트 기반 Chain-of-Thought가 가진 공간적·시각적 추론의 한계를 극복하고, 다양한 범용 MLLM에 즉시 적용 가능한 범용적인 시각적 추론 강화 도구를 제공합니다.

### 8. GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction

- **arXiv**: https://arxiv.org/abs/2605.23888
- **Score**: 6.8 / 10
- **한줄 요약**: GenRecon은 3D 장면 재구성을 전통적인 최적화 방식이 아닌, 사전 학습된 생성 모델을 활용한 '조건부 3D 생성 작업'으로 재정의하여 고품질의 장면을 복원합니다.
- **핵심 기여**: 객체 수준의 강력한 생성 모델(Trellis.2)을 장면 수준으로 확장하여, 희소한 입력 데이터에서도 편집 가능한 고품질 PBR(물리 기반 렌더링) 메시를 생성하고 재구성 품질을 16% 향상시켰습니다.
- **방법론 개요**: 장면을 공간적으로 겹치는 청크(chunk) 단위로 분할하고, 다중 뷰 이미지 특징을 3D 공간에 투영하여 생성 모델의 조건으로 주입함으로써 전역적으로 일관된 3D 장면을 생성합니다.
- **의의**: 기존 재구성 방식의 한계인 뷰포인트 부족 및 불완전한 기하학적 구조 문제를 생성형 AI의 사전 지식으로 해결함으로써, 전문적인 콘텐츠 제작 및 몰입형 환경 구축에 필요한 고충실도 3D 자산 생성을 가능하게 합니다.

### 9. EM-Vid: Training-Free Entity-Centric Memory for Efficient and Consistent Multi-Shot Video Generation

- **arXiv**: https://arxiv.org/abs/2605.23610
- **Score**: 6.8 / 10
- **한줄 요약**: EM-Vid은 전체 프레임 대신 엔티티(인물, 객체) 중심의 희소 잠재 패치를 저장하는 메모리 아키텍처를 통해, 다중 샷 비디오 생성 시 일관성과 효율성을 동시에 확보하는 훈련 불필요(training-free) 프레임워크입니다.
- **핵심 기여**: 엔티티와 장면 맥락을 분리하여 '정체성 드리프트'와 '정보 누출' 문제를 해결하고, 희소 토큰 기반의 메모리 관리로 계산 효율성을 극대화하며 텍스트 프롬프트에 대한 높은 충실도를 보장합니다.
- **방법론 개요**: 스크립트 기반의 엔티티 식별자를 활용해 '엔티티 뱅크'를 구성하고, 생성 과정에서 필요한 엔티티의 시각적 특징만을 선택적으로 주입하는 메모리 조건부 생성 방식을 채택했습니다.
- **의의**: 기존의 복잡한 파인튜닝이나 고비용의 전체 프레임 메모리 방식 없이도 장편 비디오의 서사적 일관성을 유지할 수 있어, 실용적이고 확장 가능한 비디오 생성 기술의 새로운 표준을 제시합니다.

### 10. ComPose: When to Trust Hands for Object Pose Tracking

- **arXiv**: https://arxiv.org/abs/2605.23523
- **Score**: 6.8 / 10
- **한줄 요약**: ComPose는 3D 파운데이션 모델과 손-객체 상호작용 정보를 결합하여, 템플릿이나 깊이 센서 없이도 복잡한 환경에서 객체의 6DoF 포즈를 추적하는 프레임워크입니다.
- **핵심 기여**: 손의 움직임을 객체 추적의 보조 신호로 활용하는 적응형 게이팅 메커니즘을 도입하여, 심각한 가림(occlusion) 상황에서도 템플릿 없이 강건한 추적 성능을 달성했습니다.
- **방법론 개요**: 사전 학습된 3D 파운데이션 모델로 객체의 기하학적 정보를 추출하고, 손 관절 정보를 보조 데이터로 활용하여 적응형 가중치 네트워크를 통해 두 정보를 융합함으로써 객체의 3D 궤적을 추정합니다.
- **의의**: 기존의 CAD 모델 의존성을 제거하고 가림 문제에 대한 해결책을 제시함으로써, 인터넷 영상의 인간 행동을 실제 로봇 조작으로 전이하는 등 Embodied AI 분야의 실용성을 크게 확장했습니다.

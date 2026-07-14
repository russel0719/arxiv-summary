# 📅 2026년 3월 19일 AI 연구 트렌드 보고서

> **제목**: Variational Kernel Design for Internal Noise: Gaussian Chaos Noise, Representation Compatibility, and Reliable Deep Learning  
> **주요 내용**: 내부 노이즈를 원리 기반으로 설계하는 VKD 프레임워크와 Gaussian Chaos Noise(GCh)를 도입해 드롭아웃·마스킹보다 안정적이고 해석 가능한 노이즈를 제공한다.  
> **핵심 기여**: 1) 수학적 근거 제공, 2) 양의 평균‑1 게이트(GCh) 도입, 3) ImageNet‑C에서 NLL·캘리브레이션 개선, 4) 모듈형 프레임워크 확장.  

> **제목**: Mirror Descent on Riemannian Manifolds  
> **주요 내용**: 리만 다양체에서 직접 동작하는 RMD를 제안해 정규화된 가중치, 양의 정부호 행렬 등 다양체 제약 문제를 효율적으로 해결한다.  

> **제목**: Learning When to Attend: Conditional Memory Access for Long‑Context LLMs  
> **주요 내용**: 토큰‑레벨 라우팅 메커니즘 L2A를 도입해 128K 토큰까지 긴 컨텍스트를 3% 이하 성능 저하로 처리하면서 FlashAttention 대비 2배 속도 향상과 KV‑cache 50% 절감.  

> **제목**: VLM2Rec: Resolving Modality Collapse in Vision‑Language Model Embedders for Multimodal Sequential Recommendation  
> **주요 내용**: Weak‑Modality Penalized Contrastive Learning과 Cross‑Modal Relational Topology Regularization을 통해 모달리티 붕괴를 해결하고, 시각·텍스트 정보를 균형 있게 활용한다.  

> **제목**: Structured SIR: Efficient and Expressive Importance‑Weighted Inference for High‑Dimensional Image Registration  
> **주요 내용**: 샘플링 기반 Structured SIR 프레임워크를 도입해 고차원 의료 영상 정합에서 메모리·연산 효율을 동시에 달성한다.  

> **제목**: Gesture‑Aware Pretraining and Token Fusion for 3D Hand Pose Estimation  
> **주요 내용**: 손동작 정보를 활용한 사전학습과 토큰‑Fusion Transformer를 결합해 3D 손 포즈 추정 성능을 크게 향상시킨다.  

> **제목**: Beyond Outliers: A Data‑Free Layer‑wise Mixed‑Precision Quantization Approach Driven by Numerical and Structural Dual‑Sensitivity  
> **주요 내용**: 수치·구조 이중 민감도(NSDS)를 기반으로 레이어 단위 비트폭을 할당해 데이터 없이도 높은 압축·정확도 균형을 달성한다.  

> **제목**: EvoGuard: An Extensible Agentic RL‑based Framework for Practical and Evolving AI‑Generated Image Detection  
> **주요 내용**: RL 기반 에이전트가 도구를 동적으로 호출·조합해 AI‑생성 이미지 탐지 성능을 지속적으로 향상시키는 프레임워크.  

---

## 1. Overall Trend

| 분야 | 트렌드 | 핵심 포인트 |
|------|--------|-------------|
| **모델 안정성 & 해석 가능성** | 내부 노이즈 설계, Gaussian Chaos Noise | 원리 기반 노이즈 도입으로 드롭아웃 대체 |
| **다양체 최적화** | Riemannian Mirror Descent | 정규화된 가중치, 양의 정부호 행렬 등 다양체 제약 문제 해결 |
| **긴 컨텍스트 처리** | 토큰‑레벨 라우팅 (L2A) | 128K 토큰까지 효율적 처리, 메모리·속도 최적화 |
| **멀티모달 균형** | 모달리티 붕괴 해결 | VLM2Rec으로 시각·텍스트 균형 유지 |
| **고차원 불확실성 추정** | Structured SIR | 의료 영상 정합에서 메모리·연산 효율 극대화 |
| **사전학습 활용** | Gesture‑Aware Pretraining | 손동작 라벨을 활용해 3D 포즈 추정 성능 향상 |
| **양자화 혁신** | NSDS 기반 레이어‑레벨 양자화 | 데이터 없이 비트폭 할당, 대형 모델 압축 |
| **AI‑생성 이미지 탐지** | EvoGuard | RL 기반 에이전시 프레임워크로 지속적 성능 향상 |

> **핵심 메시지**: 오늘날 AI 연구는 **원리 기반 설계**(노이즈, 양자화), **다양체 최적화**, **긴 컨텍스트 처리**, 그리고 **멀티모달 균형**을 동시에 추구하며, **실시간 적응**(RL 기반 탐지)과 **불확실성 추정**을 강화하고 있다.

---

## 2. CV‑Related Themes

| 논문 | 핵심 아이디어 | 주요 성과 |
|------|--------------|-----------|
| **Variational Kernel Design for Internal Noise** | Gaussian Chaos Noise(GCh) 기반 내부 노이즈 설계 | ImageNet‑C에서 NLL·캘리브레이션 개선 |
| **VLM2Rec** | 모달리티 붕괴 해결 (WM‑PCL, CM‑RTR) | 시각·텍스트 임베딩 균형, 콜드‑스타트 성능 향상 |
| **Structured SIR** | 샘플링 기반 Importance‑Weighted Inference | 3D 뇌 MRI 정합에서 메모리·연산 효율 극대화 |
| **Gesture‑Aware Pretraining** | 손동작 라벨 활용 사전학습 + 토큰‑Fusion | 3D 손 포즈 추정 MPJPE 4.84 mm 개선 |
| **Beyond Outliers** | 수치·구조 이중 민감도 기반 양자화 | 데이터 없이 레이어‑레벨 비트폭 할당, 압축·정확도 균형 |

> **주요 트렌드**  
> - **노이즈 설계**: 원리 기반 노이즈(GCh)로 모델 안정성 강화.  
> - **멀티모달 균형**: VLM2Rec과 같은 기울기 재조정으로 모달리티 붕괴 방지.  
> - **불확실성 추정**: Structured SIR로 고차원 의료 영상 정합에서 효율적 추정.  
> - **사전학습 활용**: Gesture‑Aware Pretraining으로 3D 포즈 추정 성능 향상.  
> - **양자화 혁신**: NSDS 기반 레이어‑레벨 양자화로 대형 모델 압축.

---

## 3. NLP‑Related Themes

| 논문 | 핵심 아이디어 | 주요 성과 |
|------|--------------|-----------|
| **Learning When to Attend** | 토큰‑레벨 라우팅(L2A) | 128K 토큰까지 3% 이하 성능 저하, FlashAttention 대비 2배 속도, KV‑cache 50% 절감 |
| **Mirror Descent on Riemannian Manifolds** | RMD (리만 다양체 기반 Mirror Descent) | 정규화된 가중치 학습, 대규모 딥러닝에서 정규화된 가중치 적용 가능 |
| **EvoGuard** | RL 기반 도구 조합 프레임워크 | AI‑생성 이미지 탐지에서 라벨 비용 최소화, 새로운 탐지기 추가 시 재학습 불필요 |

> **주요 트렌드**  
> - **긴 컨텍스트 처리**: L2A로 128K 토큰까지 효율적 처리.  
> - **다양체 최적화**: RMD를 통해 정규화된 가중치 학습이 가능해짐.  
> - **적응형 탐지**: EvoGuard로 AI‑생성 이미지 탐지 성능을 지속적으로 향상.

---

## 4. Cross‑Domain Directions

| 영역 | 연결 포인트 | 기대 효과 |
|------|-------------|-----------|
| **CV ↔ NLP** | VLM2Rec (멀티모달), L2A (긴 컨텍스트) | 시각·언어 모델이 긴 문맥을 이해하고, 모달리티 균형을 유지하면서 성능 향상 |
| **CV ↔ Quantization** | NSDS 기반 양자화 + Structured SIR | 고차원 영상 모델을 효율적으로 압축·추론, 의료 영상 정합에 실시간 적용 가능 |
| **NLP ↔ RL** | EvoGuard (RL 기반 도구 조합) | 언어 모델이 동적으로 도구를 선택해 추론 성능을 향상, AI‑생성 이미지 탐지와 같은 실시간 서비스에 적용 |
| **CV ↔ RL** | L2A (토큰‑레벨 라우팅) | RL 기반 라우팅을 통해 시각 모델의 주의 메커니즘을 동적으로 최적화 가능 |
| **모든 영역 ↔ 내부 노이즈 설계** | VKD + GCh | 모델 전반에 걸쳐 안정성 및 해석 가능성 향상, 다양한 도메인에서 재사용 가능 |

> **통합 비전**  
> - **멀티모달**과 **긴 컨텍스트**를 동시에 다루는 모델이 등장하며, **RL**과 **양자화**가 결합해 실시간, 저전력 추론이 가능해진다.  
> - **내부 노이즈 설계**(VKD/GCh)는 CV·NLP 모두에서 모델 안정성을 보장하며, **다양체 최적화**(RMD)는 정규화된 가중치 학습을 가속화한다.  

---

## 📌 요약

- **안정성**: VKD와 GCh가 드롭아웃을 대체해 모델을 더 견고하게 만든다.  
- **효율성**: L2A와 Structured SIR이 메모리·연산을 크게 절감한다.  
- **멀티모달 균형**: VLM2Rec이 시각·텍스트 정보를 균형 있게 활용한다.  
- **양자화 혁신**: NSDS가 데이터 없이 레이어‑레벨 비트폭을 할당해 대형 모델을 압축한다.  
- **적응형 탐지**: EvoGuard가 RL 기반 도구 조합으로 AI‑생성 이미지 탐지를 지속적으로 향상시킨다.  

> **향후 연구 방향**  
> 1. **원리 기반 노이즈**를 다른 도메인(예: 음성, 시계열)에도 적용  
> 2. **RL 기반 라우팅**을 CV·NLP 모델에 통합해 동적 주의 메커니즘 개발  
> 3. **다중 모드 양자화**를 통해 멀티모달 모델의 실시간 추론 가능성 확대  
> 4. **다양체 최적화**를 활용한 정규화된 가중치 학습의 범위 확대  

---

## 개별 논문 요약

### Variational Kernel Design for Internal Noise: Gaussian Chaos Noise, Representation Compatibility, and Reliable Deep Learning
- Score: 8.7
- Reason: The paper introduces a principled, variational framework for designing internal noise (VKD) that derives Gaussian Chaos Noise from first principles, offering novel theoretical insights and rigorous proofs. Its technical depth is substantial, involving maximum‑entropy arguments, Dirichlet Laplacian geometry, and exact control of noise effects. The methodology has the potential to influence future research on regularization, robustness, and calibration in deep learning, indicating significant long‑term impact.
- Main Idea: Variational Kernel Design(VKD) 프레임워크를 통해 내부 노이즈를 설계 객체로 정의하고, Dirichlet 로그필드와 Wick 정규화를 이용해 Gaussian Chaos Noise(GCh)를 도출함으로써 기존의 휴리스틱한 드롭아웃·마스킹 방식 대신 원리 기반의 노이즈를 제공한다.
- Key Contribution: 1) 노이즈 설계에 대한 수학적 근거를 제공하고, 2) GCh라는 양의 평균-1 가중 게이트를 도입해 해석 가능한 상관 구조를 갖는 노이즈를 만들며, 3) GCh가 배포 변동(ImageNet‑C)에서 NLL과 캘리브레이션을 개선하고, 4) VKD를 일반화 가능한 모듈형 프레임워크로 확장한다.
- Method Overview: VKD는 (법칙군, 상관 커널, 주입 연산자) 세트로 내부 노이즈를 정의한다. 공간 서브패밀리에서는 양자 최대엔트로피 원리를 적용해 Dirichlet Laplacian을 정밀 행렬로 갖는 Gaussian 솔루션을 얻고, Wick 정규화를 통해 양의 평균-1 게이트(GCh)를 생성한다. 샘플‑별 게이트를 실험에 적용하며, 로그‑비율 변형, 마진‑감지 랭킹 안정성, 내재 거칠기 예산을 정밀히 증명한다.
- Why It Matters: 전통적 드롭아웃·하드 마스킹은 일관성 있는 의미 표현에 부적합하고, 분포 변동 시 캘리브레이션이 급격히 악화된다. GCh는 부드럽고 양의 멀티플라이어 노이즈로서 의미 표현의 상대 기하학을 보존하며, NLL과 캘리브레이션을 개선해 실제 환경에서의 신뢰성을 높인다. 또한 VKD는 특정 학습 목표에 맞춘 노이즈 설계를 가능하게 하여 향후 연구의 기초를 제공한다.

### Mirror Descent on Riemannian Manifolds
- Score: 8.5
- Reason: The paper introduces a novel generalization of Mirror Descent to Riemannian manifolds, providing both deterministic and stochastic variants with rigorous non-asymptotic convergence analysis. The technical depth is evident in the reparameterization framework and the derivation of guarantees, while the potential long-term impact lies in broadening scalable optimization tools for manifold-constrained problems, especially in large-scale machine learning and signal processing.
- Main Idea: 고전적인 Mirror Descent를 리만 기하학으로 확장해, 리만 다양체 상에서 직접 동작하는 Riemannian Mirror Descent(RMD)를 제안한다.
- Key Contribution: 1) 리만 다양체를 위한 통합 RMD 프레임워크와 재매개화 기법. 2) 대규모 문제를 위한 확률적 RMD와 비정상적 수렴 보장. 3) Stiefel 다양체에서 기존 CGD와의 통합 및 스토캐스틱 CGD 도입.
- Method Overview: RMD는 Bregman 다이버전스를 리만 기하학에 맞게 변형하고, Riemannian gradient와 메트릭을 사용해 업데이트를 수행한다. 스토캐스틱 버전은 미니배치 기울기를 활용하며, 리트랙션을 통해 지오데식 지도를 근사한다.
- Why It Matters: 다양체에 제약된 최적화 문제(예: 정규화된 가중치, 양의 정부호 행렬 등)를 효율적으로 해결할 수 있는 이론적 근거와 실용적 알고리즘을 제공하며, 대규모 딥러닝에서 정규화된 가중치 학습에 적용 가능하다.

### Learning When to Attend: Conditional Memory Access for Long-Context LLMs
- Score: 8.5
- Reason: Introduces token-wise conditional attention (L2A) that reduces quadratic cost while maintaining performance, demonstrates practical GPU optimizations, and offers a scalable approach for long-context LLMs, indicating strong technical depth and promising long-term impact.
- Main Idea: L2A는 각 토큰이 필요에 따라 전역 주의(attention)와 지역 주의(local attention)를 선택하도록 학습하는 토큰‑레벨 라우팅 메커니즘을 도입해, 128K 토큰까지의 긴 컨텍스트를 효율적으로 처리한다.
- Key Contribution: Qwen 2.5/3 모델의 컨텍스트 길이를 32K에서 128K로 확장하면서 3% 이하의 성능 저하를 보이고, 토큰의 80%가 전역 주의를 건너뛰어 FlashAttention 대비 2배 이상의 속도 향상과 KV‑cache 메모리 사용량을 50%까지 절감한다.
- Method Overview: L2A 레이어는 먼저 슬라이딩 윈도우(local attention)를 적용하고, 라이트웨이트 라우터가 토큰마다 0/1 결정을 내린다. 1인 토큰은 전체 시퀀스에 대해 정확한 전역 주의를 수행하고, 0인 토큰은 지역 표현만 유지한다. 트리톤 커널로 토큰‑레벨 패턴을 GPU에서 효율적으로 실행하며, 훈련 시 희소성 정규화와 함께 학습된다. 훈련 후에는 전역 주의 레이어를 희소화해 메모리 사용량을 추가로 절감한다.
- Why It Matters: 전통적 고정‑스파스 주의 방식은 토큰마다 필요한 정보를 적절히 반영하지 못해 성능 저하가 발생한다. L2A는 토큰별로 동적으로 전역 주의를 선택함으로써 계산 비용을 크게 줄이면서도 긴 문맥에서의 정확성을 유지한다. 이는 대규모 언어 모델이 실무에서 128K 토큰 이상의 컨텍스트를 활용할 수 있게 하여, 문서 요약, 대규모 검색, 장기 의존성 학습 등에서 실질적인 성능 향상을 가능하게 한다.

### VLM2Rec: Resolving Modality Collapse in Vision-Language Model Embedders for Multimodal Sequential Recommendation
- Score: 8.5
- Reason: The paper introduces a novel framework that tackles modality collapse in VLM-based multimodal sequential recommendation through Weak-modality Penalized Contrastive Learning and Cross-Modal Relational Topology Regularization, demonstrating significant technical depth and promising long-term impact on integrating high-capacity vision-language models with collaborative filtering signals.
- Main Idea: VLM2Rec는 시퀀스 기반 추천에서 Vision‑Language Model(VLM)을 활용하면서 발생하는 모달리티 붕괴(모달리티 불균형)를 해결하기 위해 모달리티별 기울기를 재조정하고, 모달리티 간 관계를 보존하는 정규화를 도입한 프레임워크이다.
- Key Contribution: 1) Weak‑Modality Penalized Contrastive Learning (WM‑PCL)로 약한 모달리티의 기울기를 명시적으로 제약해 균형을 맞추고, 2) Cross‑Modal Relational Topology Regularization (CM‑RTR)로 모달리티 간 관계 구조를 보존함으로써 VLM을 CF‑인식 멀티모달 인코더로 변환한다.
- Method Overview: VLM을 시퀀스 수준에서 fine‑tune하고, 내부/외부 융합 전략을 비교해 모달리티 붕괴 원인을 분석한다. WM‑PCL은 InfoNCE 기반 contrastive loss에 모달리티별 기울기 가중치를 부여해 균형을 맞추고, CM‑RTR은 지오메트릭 일관성 제약을 통해 모달리티 간 관계를 유지한다. 최종적으로 두 모달리티를 element‑wise 합산해 사용자·항목 임베딩을 생성한다.
- Why It Matters: 모달리티 붕괴는 VLM을 추천에 적용할 때 성능 저하와 부정적 전이의 주된 원인이므로, 이를 해결함으로써 시각·텍스트 정보를 균형 있게 활용하고, 콜드‑스타트 아이템에서도 높은 정확도와 견고성을 달성할 수 있다.

### Structured SIR: Efficient and Expressive Importance-Weighted Inference for High-Dimensional Image Registration
- Score: 8.5
- Reason: The paper introduces a novel memory‑efficient covariance parameterisation (low‑rank plus sparse Cholesky) within a Sampled Importance Resampling framework, enabling expressive, multi‑modal uncertainty quantification for high‑dimensional image registration. The technical contribution is substantial, addressing a key scalability bottleneck in probabilistic dense registration. Its implications for robust medical imaging and potential extensions to other high‑dimensional inference problems suggest significant long‑term impact.
- Main Idea: 고차원 의료 영상 정합에서 변분 추정의 한계를 극복하기 위해, 샘플링 기반의 Structured SIR(Importance Resampling) 프레임워크를 도입해 메모리와 계산 효율성을 동시에 달성한다.
- Key Contribution: 저차원 성분과 희소한 공간 구조를 갖는 Cholesky 정밀 행렬을 결합한 공변량 파라미터화로, 복잡한 다중 모드 불확실성을 정밀히 표현하면서도 계산 비용을 크게 줄인다.
- Method Overview: SIR 스킴을 통해 유연한 가우시안 제안분포에서 샘플을 추출하고, 중요도 가중치를 계산해 가장 높은 가중치를 가진 샘플만 역전파에 사용한다. 제안분포의 공변량은 저차원 랭크 + 희소 Cholesky 구조로 구성되어 3D 뇌 MRI 정합에 적용된다.
- Why It Matters: 전통적 변분 방법보다 정확도와 불확실성 보정이 우수하며, 고차원 변형 필드에서도 메모리와 연산 비용이 낮아 임상적 활용 가능성을 높인다.

### Gesture-Aware Pretraining and Token Fusion for 3D Hand Pose Estimation
- Score: 8.5
- Reason: Introduces a novel gesture‑aware pretraining scheme and token‑fusion Transformer that leverage gesture semantics as an inductive bias for 3D hand pose estimation, offering significant technical depth and promising long‑term impact on pose‑guided perception tasks.
- Main Idea: 흔한 손동작(gesture) 정보를 활용해 단일 RGB 이미지에서 3D 손 포즈를 추정하는 두 단계 파이프라인을 제안한다. 첫 단계에서는 손동작 분류를 통해 풍부한 임베딩 공간을 학습하고, 두 번째 단계에서는 이 임베딩을 토큰‑Fusion Transformer에 주입해 관절별 특징을 정제한다.
- Key Contribution: 1) 손동작 라벨을 인덕티브 바이어스로 활용해 Encoder의 표현력을 크게 향상시킨다. 2) Gesture‑aware pretraining이 다른 네트워크 백본에도 그대로 적용 가능해, 구조 변경 없이 성능을 끌어올린다. 3) 토큰‑레벨 Fusion과 다중 수준 손 구조 손실을 결합한 통합 프레임워크를 제공한다.
- Method Overview: Stage 1: HRNet 백본을 InterHand2.6M의 coarse/fine gesture 라벨로 hierarchical 분류 학습. Stage 2: Encoder에서 추출한 이미지 특징과 2.5‑D 볼륨을 결합해 관절 토큰을 생성하고, Gesture 임베딩을 중간 토큰으로 사용해 Transformer가 토큰을 정제. 정제된 토큰으로 MANO 파라미터(회전·모양)를 회귀하고, MANO 파라미터, 관절 위치, 구조 정규화 등 8개의 손실을 동시에 최적화.
- Why It Matters: 손동작 사전 지식이 3D 손 포즈 추정에 강력한 선행 정보를 제공함을 입증했다. 기존 EANet 대비 MPJPE가 4.84 mm로 현저히 개선되었으며, 백본 교체 없이 성능 향상이 가능해 연구·산업 현장에서 손쉽게 적용할 수 있다. 또한, sign‑language 인식과 3D 포즈 추정 사이의 연결 고리를 마련해 향후 다중 모달 인식 연구에 기여한다.

### Beyond Outliers: A Data-Free Layer-wise Mixed-Precision Quantization Approach Driven by Numerical and Structural Dual-Sensitivity
- Score: 8.5
- Reason: The paper introduces a novel dual-sensitivity framework (numerical + structural) with a robust MAD‑Sigmoid/Soft‑OR aggregation for layer‑wise mixed‑precision quantization, eliminating calibration data. It offers moderate technical depth through mechanistic decomposition and aggregation design, and its calibration‑free, fine‑grained bit allocation has potential long‑term impact on low‑bit neural network deployment.
- Main Idea: 모델 파라미터를 레이어 단위로 분해하고, 수치적 민감도와 구조적 표현력을 동시에 평가해 비트폭을 할당하는 NSDS(수치·구조 이중 민감도) 기반의 calibration‑free 양자화 프레임워크를 제안한다.
- Key Contribution: 1) 레이어를 Detectors와 Writers로 모듈별로 세분화해 모듈 간 차이를 반영한다. 2) 수치적 취약성(NV)과 구조적 표현력(SE)을 각각 계산해 두 차원의 민감도 프로필을 만든다. 3) MAD‑Sigmoid와 Soft‑OR 융합으로 극단값에 강건한 레이어‑레벨 민감도 지표를 도출한다. 4) 데이터 없이 모델 가중치와 구조만으로 비트폭을 할당해 효율적이고 정확한 양자화를 실현한다.
- Method Overview: 각 레이어를 Detectors(주요 기능)와 Writers(출력)로 분해하고, NV는 가중치의 극단값(예: 과도한 kurtosis)으로, SE는 SVD 기반의 스펙트럼 에너지와 엔트로피로 측정한다. 두 지표를 MAD‑Sigmoid로 정규화한 뒤 Soft‑OR 으로 결합해 레이어별 민감도 점수를 얻고, 이 점수를 기준으로 비트폭을 순위별로 할당한다.
- Why It Matters: 전통적 PTQ가 모든 레이어를 동일 비트폭으로 처리하거나 대규모 탐색을 필요로 하는 반면, NSDS는 모듈별 차이를 반영하고 calibration 데이터 없이도 높은 압축-정확도 균형을 달성한다. 이는 대형 언어 모델의 메모리·연산 비용을 크게 절감하면서 실제 하드웨어에 바로 적용 가능한 실용적 솔루션을 제공한다.

### EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection
- Score: 8.5
- Reason: The paper proposes a novel agentic framework that dynamically orchestrates heterogeneous detectors using a GRPO-based RL algorithm, enabling plug‑and‑play integration without costly annotations. The concept is technically deep, combining multi‑turn reasoning, capability awareness, and reinforcement learning, and offers a scalable, long‑term solution to evolving AI‑generated image threats.
- Main Idea: EvoGuard는 기존 AI‑생성 이미지(AIGI) 탐지기를 ‘도구’로 취급하고, RL 기반 에이전트가 상황에 맞게 동적으로 호출·조합하여 최종 판단을 내리는 에이전시 프레임워크이다.
- Key Contribution: 다중 모델을 플러그‑앤‑플레이 방식으로 동적으로 조율하고, GRPO로 이진 라벨만으로 정책을 학습해 재학습 없이 새로운 탐지기를 추가할 수 있으며, 최소한의 연산으로 최고 정확도를 달성한다.
- Method Overview: 1) 도구 캡슐화: 각 탐지기를 가벼운 인터페이스로 래핑한다. 2) 동적 오케스트레이션: 에이전트가 계획·반영 모듈을 통해 필요한 도구를 선택한다. 3) 다중 턴 추론: 여러 도구를 순차 호출해 중간 결과를 집계·반영하며 결정한다. 4) GRPO 학습: 이진 진짜/가짜 라벨만으로 정책을 강화학습한다.
- Why It Matters: 생성 모델이 급변하는 상황에서도 새로운 도구를 즉시 추가해 성능을 향상시킬 수 있고, 라벨 비용이 낮아 대규모 데이터셋이 필요 없으며, 실제 서비스에 바로 적용 가능한 경량화된 솔루션을 제공한다.


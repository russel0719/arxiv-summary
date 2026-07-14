# From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers  
*(Daily AI Research Trend Report – 2026‑02‑09)*  

---

## 1️⃣ 전체 트렌드  
| 트렌드 | 핵심 포인트 | 대표 논문 |
|--------|-------------|-----------|
| **인덕티브 바이어스(Inductive Bias) 주도 모델링** | 구조적 편향을 주입해 대규모 언어 모델이 물리 법칙을 내재화하도록 함 | *From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers* |
| **무한 차원 생성 모델** | Doob’s h‑transform을 활용해 목표 분포를 정확히 맞추는 확산 프레임워크 | *Infinite-dimensional generative diffusions via Doob's h-transform* |
| **추론‑시 최적화(Inference‑Time Rethinking)** | latent thought vector를 반복적으로 최적화해 작은 모델이 대형 모델을 능가 | *Inference‑Time Rethinking with Latent Thought Vectors for Math Reasoning* |
| **자기‑감시 메커니즘(Endogenous Steering Resistance)** | 모델이 스티어링에 반응해 자체적으로 정정하는 현상 | *Endogenous Resistance to Activation Steering in Language Models* |
| **위상수학 기반 TD 학습** | 비마코프 환경에서도 안정적인 정책을 학습 | *Cochain Perspectives on Temporal‑Difference Signals for Learning Beyond Markov Dynamics* |
| **음향 물리 기반 RLF** | 3‑D 장면에서 실시간 고품질 음향 재현 | *Reciprocal Latent Fields for Precomputed Sound Propagation* |
| **멀티‑오브젝트 정렬** | 목표 간 교차 간섭을 정량화하고 완화 | *Uncovering Cross‑Objective Interference in Multi‑Objective Alignment* |

> **핵심 메시지**  
> 대규모 모델이 단순히 데이터를 피팅하는 수준을 넘어, **물리, 수학, 인지** 등 다양한 도메인의 **규칙을 학습**하고 **자기‑조정**할 수 있는 방향으로 진화하고 있다. 인덕티브 바이어스와 **공간/시간/역학적 구조**를 주입하면 모델이 **내재적 법칙**을 인식하게 되며, 이는 과학적 발견 자동화와 안전한 LLM 개발에 직접 연결된다.

---

## 2️⃣ CV‑관련 테마  
| 주제 | 세부 내용 | 대표 논문 |
|------|-----------|-----------|
| **물리‑인정형 시각 모델** | 물리 법칙(뉴턴 역학)을 학습하도록 구조적 편향 주입 | *From Kepler to Newton* |
| **음향 시뮬레이션** | 3‑D 공간에서 잠재 임베딩 그리드를 활용해 실시간 음향 재현 | *Reciprocal Latent Fields* |
| **무한 차원 생성** | 시각 데이터(예: 3‑D 모델)에서도 목표 분포를 맞추는 확산 프레임워크 | *Infinite‑dimensional generative diffusions* |
| **강화학습 기반 시각** | 비마코프 환경에서 안정적인 정책을 학습 | *Cochain Perspectives* |

> **트렌드 포인트**  
> - **물리‑인정형 인코더/디코더**가 시각 모델의 해석성을 높이고, **실시간 시뮬레이션**이 가능해졌다.  
> - **잠재 그리드**를 활용한 **RLF**는 메모리와 계산 비용을 획기적으로 줄이며, 게임/VR 등 실시간 응용에 적합하다.

---

## 3️⃣ NLP‑관련 테마  
| 주제 | 세부 내용 | 대표 논문 |
|------|-----------|-----------|
| **추론‑시 최적화** | latent thought vector를 Gibbs‑style 루프에서 최적화 | *Inference‑Time Rethinking* |
| **자기‑감시 메커니즘** | 스티어링에 반응해 자체적으로 정정하는 ESR | *Endogenous Resistance to Activation Steering* |
| **멀티‑오브젝트 정렬** | 목표 간 교차 간섭을 완화해 LLM 정합성 향상 | *Uncovering Cross‑Objective Interference* |
| **물리‑인정형 언어 모델** | 물리 법칙을 내재화한 Transformer | *From Kepler to Newton* |

> **핵심 포인트**  
> - **Inference‑Time Rethinking**은 **모델 크기**를 줄이면서도 **수학 추론** 성능을 대폭 끌어올린다.  
> - **ESR**은 스티어링 기반 안전 조치가 내부 메커니즘에 의해 무력화될 수 있음을 경고하며, **자기‑감시**를 통한 안전성 향상 연구가 필요하다.  
> - **멀티‑오브젝트 정렬**은 LLM이 여러 목표를 동시에 만족하도록 **공분산 기반 가중치 조정**을 제안한다.

---

## 4️⃣ Cross‑Domain Directions  
| 방향 | 기대 효과 | 적용 사례 |
|------|-----------|-----------|
| **Physics‑Informed Transformers** | 물리 법칙을 학습해 과학적 시뮬레이션 자동화 | 천체 역학, 유체 역학, 재료 과학 |
| **Latent‑Space Diffusion** | 무한 차원에서도 목표 분포를 정확히 맞추어 복잡한 함수형 데이터 생성 | 기후 모델링, 신약 디자인 |
| **Inference‑Time Optimization** | 작은 모델이 대형 모델을 능가하도록 추론 시 반복적 최적화 | 모바일 AI, IoT, 실시간 문제 해결 |
| **Self‑Steering & Safety** | 모델이 스티어링에 반응해 자체적으로 정정 → 안전성 강화 | 자율주행, 의료 진단 |
| **Topological TD Learning** | 비마코프 환경에서도 안정적 RL | 로봇 공학, 게임 AI |
| **RLF‑Based Audio Rendering** | 실시간 고품질 음향 재현 → VR/AR, 게임 | 가상 현실, 실시간 시뮬레이션 |

> **전망**  
> - **인덕티브 바이어스**와 **공간/시간/역학적 구조**를 결합한 모델이 **다중 도메인**에서 공통적으로 활용될 전망이다.  
> - **Latent‑Space Diffusion**과 **Inference‑Time Rethinking**은 **모델 경량화**와 **생성 품질**을 동시에 달성할 수 있는 핵심 기술이다.  
> - **자기‑감시**와 **멀티‑오브젝트 정렬**은 **AI 안전성**과 **정합성**을 보장하는 필수 요소로 부상하고 있다.

---

## 📌 요약  
- **인덕티브 바이어스**가 대규모 모델의 **내재적 물리·수학적 이해**를 촉진.  
- **Latent‑Space Diffusion**과 **Inference‑Time Rethinking**이 **모델 경량화**와 **성능 향상**을 동시에 달성.  
- **자기‑감시**와 **멀티‑오브젝트 정렬**이 **AI 안전성**과 **정합성**을 강화.  
- **Cross‑Domain** 연구가 **물리, 음향, RL, NLP** 등 다양한 분야를 연결하며, **실시간 시뮬레이션**과 **안전한 AI** 개발에 핵심 기여.

> **다음 주제**: *Continuous‑time reinforcement learning: ellipticity enables model‑free value function approximation* – 이 논문이 어떻게 **연속‑시간 RL**에 새로운 이론적 기반을 제공하는지 살펴보자.

## 개별 논문 요약

### From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers
- Score: 8.7
- Reason: Introduces minimal inductive biases that enable generic Transformers to learn physical laws, offering a promising step toward automated scientific discovery.
- Main Idea: 일반적인 Transformer가 우주 물리학적 세계 모델(뉴턴 역학)을 학습하도록 최소한의 구조적 편향(공간적 부드러움, 안정성, 시간적 국소성)을 주입하는 방법을 제시한다.
- Key Contribution: 공간적 부드러움, 안정성, 시간적 국소성이라는 세 가지 인덕티브 바이어스를 도입함으로써, Transformer가 단순히 궤적을 피팅하는 대신 실제 물리 법칙(인버스‑스퀘어 중력)을 내재화하도록 만들었다는 실험적 증거를 제공한다.
- Method Overview: GPT‑2 규모의 Transformer를 2‑D 행성 궤적 데이터(≈20 B 토큰)로 autoregressive 학습하고, 토큰화는 좌표를 7,000개의 균일 구간으로 나눈다. 학습 중에 공간적 부드러움(연속성 패널티), 안정성(오버피팅 방지 정규화), 시간적 국소성(최근 몇 단계만을 주의하도록 어텐션 제한)을 각각 적용한다. 이후 모델의 내부 표현을 선형 프로빙으로 검사하고, 컨텍스트 길이에 따른 Keplerian(전역 궤적) vs Newtonian(동역학) 모델 구분을 실험한다.
- Why It Matters: 데이터 중심의 대규모 언어 모델이 실제 물리 법칙을 학습할 수 있음을 보여줌으로써, AI가 과학적 발견을 자동화하고 해석 가능한 물리 모델을 생성할 수 있는 가능성을 열어준다. 이는 AI 과학자(‘AI scientist’) 개발의 핵심 과제인 ‘세계 모델 학습’에 대한 실질적 진전을 의미한다.

### Infinite-dimensional generative diffusions via Doob's h-transform
- Score: 8.7
- Reason: The paper proposes a novel use of Doob’s h‑transform to construct infinite‑dimensional diffusion models, offering a rigorous and generalizable framework that extends beyond finite‑dimensional settings. The technical depth is evident in the rigorous derivation, verifiable conditions, and theoretical bounds. Its potential to enable generative modeling in high‑dimensional functional spaces suggests significant long‑term research impact.
- Main Idea: 무한 차원 힐베르트 공간에서 Doob의 h‑변환을 이용해 목표 분포에 도달하도록 강제하는 새로운 확산 프레임워크를 제시한다.
- Key Contribution: 1) 무한 차원에서도 잘 정의되는 h‑변환을 증명하고, 2) 목표 분포와의 근사 오차를 명시적으로 바운드하며, 3) 스코어 매칭 기반 학습으로 실제 구현이 가능한 유연한 모델을 제공한다.
- Method Overview: 기준 확산 X_t를 정의하고, h(t,x)=∫p(t,x;T,y)p_T(y)dμ(y) 를 통해 변환된 확률 측도를 만들며, 학습 단계에서는 스코어 매칭 목표를 최소화해 h‑함수를 근사한다. 이후 변환된 SDE를 전진 시뮬레이션해 T 시점에 목표 분포를 정확히 맞춘다.
- Why It Matters: 전통적 노이징‑리버스 방식은 무한 차원에서 수렴 문제와 차원 의존성을 갖는다. 본 방법은 수렴을 보장하고, 차원에 무관하며, 이론적 근거와 실험적 검증을 동시에 제공해 물리적 과정, 함수형 데이터 등 복잡한 무한 차원 생성 모델에 적용 가능하다.

### Inference-Time Rethinking with Latent Thought Vectors for Math Reasoning
- Score: 8.7
- Reason: Introduces a novel generative framework that decouples latent reasoning vectors from token generation, enabling iterative self-correction via Gibbs-style optimization. The method demonstrates substantial technical depth in combining continuous latent manifolds with inference-time refinement, and its potential to reduce parameter reliance could influence future research on efficient reasoning models.
- Main Idea: 추론 시 재고(Inference‑Time Rethinking) 프레임워크를 제안해, 추론 과정을 ‘무엇을 생각할지’(latent thought vector)와 ‘어떻게 표현할지’(decoder)로 분리하고, Gibbs‑style 루프를 통해 latent을 반복적으로 최적화함으로써 추론 품질을 향상시킨다.
- Key Contribution: 0.2B 파라미터 모델이 30번의 재고(iteration)만으로 GSM8K 등 수학 추론 벤치마크에서 10–15배 더 큰 모델을 능가하는 성능을 보였으며, latent thought vector와 dual‑rate 학습을 도입해 토큰 수준 노이즈를 제거하고 gradient‑based 최적화를 가능하게 했다.
- Method Overview: 1) Prior encoder가 노이즈를 continuous latent z로 매핑하고, 2) Decoder가 z를 조건으로 추론 트레이스를 생성한다. 추론 시 Gibbs‑style 루프가 번갈아가며 (Generate → Reflect) z를 gradient descent로 조정해 트레이스의 likelihood를 최대화한다. 학습은 fast local 업데이트(각 인스턴스별 latent 최적화)와 slow global 업데이트(모델 파라미터 학습) 두 단계로 구성된다.
- Why It Matters: 모델 크기 대신 추론 시 반복적 최적화를 활용해 파라미터 수를 크게 줄이면서도 높은 수학 추론 성능을 달성한다. latent workspace를 통해 추론 과정을 해석 가능하게 만들고, 오류 전파를 방지하며, 향후 다양한 추론 및 문제 해결 분야에 적용 가능한 경량화된 인공지능 설계 원칙을 제시한다.

### Endogenous Resistance to Activation Steering in Language Models
- Score: 8.5
- Reason: The paper introduces a novel concept of endogenous steering resistance (ESR) in large language models, providing causal evidence and demonstrating controllability through prompting and fine‑tuning. The technical depth is evident in the use of sparse autoencoder latents, ablation studies, and multi‑attempt analysis, offering new insights into internal consistency mechanisms. ESR has significant long‑term research implications for AI safety, interpretability, and controllability, making the work impactful beyond immediate benchmarks.
- Main Idea: SAE(희소 오토인코더) 잠재 벡터를 이용한 활성화 스티어링을 통해 대형 언어 모델이 스티어링에 반응해 스스로 정정(ESR)을 수행하는 현상을 발견하고, 이를 정량화하고 조절할 수 있는 방법을 제시한다.
- Key Contribution: 1) ESR(Endogenous Steering Resistance) 개념 도입 및 실험적 검증 2) ESR을 매개하는 26개의 SAE 잠재 공간 식별 3) 메타프롬프트와 파인튜닝으로 ESR을 강화·억제할 수 있음을 입증 4) 스티어링 기반 안전 조치가 내부 메커니즘에 의해 무력화될 수 있음을 시사
- Method Overview: SAE 잠재를 특정 깊이에서 스티어링하고, 오프‑토픽 감지 잠재(OTD)를 찾아 26개를 선정한다. ESR율(다시 시작해 더 나은 답변을 제공하는 비율)을 측정하고, 26개 잠재를 제거해 25% 감소를 확인한다. 메타프롬프트와 파인튜닝을 적용해 ESR을 4배 이상 증가시키며, Llama‑3.3‑70B, Llama‑3.1‑8B, Gemma‑2‑2B/9B/27B 등 다양한 모델에서 벤치마킹한다.
- Why It Matters: ESR은 모델이 스티어링에 반응해 내부 일관성을 스스로 검사하고 수정하는 메커니즘을 보여준다. 이는 스티어링 기반 안전 조치가 예상과 다르게 동작할 수 있음을 경고하고, 모델의 자가 감시 기능을 이해·제어함으로써 보다 안전하고 투명한 LLM 개발에 기여한다.

### Cochain Perspectives on Temporal-Difference Signals for Learning Beyond Markov Dynamics
- Score: 8.5
- Reason: The paper introduces a genuinely novel topological framework for interpreting TD errors as 1‑cochains and decomposing them via a Hodge‑type projection, leading to the HFPS algorithm that offers provable stability and sensitivity guarantees in non‑Markovian settings. The technical depth is substantial, involving advanced concepts from algebraic topology and differential geometry applied to RL theory. Its long‑term impact is promising, as it opens a new theoretical lens for designing algorithms beyond the Markov assumption and could inspire a broader class of topologically informed RL methods.
- Main Idea: 비마코프 환경에서 TD 학습을 위상수학적 관점으로 해석하고, TD 오류를 1-코체로 보아 Hodge 분해를 통해 마코프와 비마코프 성분을 분리한다.
- Key Contribution: 1) TD 오류의 Hodge‑형분해를 도입해 마코프와 비마코프 동역학을 명확히 구분한다. 2) Bellman–de Rham 투영을 이용해 통합 가능한 부분을 추출하고, 3) HodgeFlow Policy Search(HFPS) 알고리즘을 제안해 비마코프 환경에서도 안정적이고 민감도 보장된 정책을 학습한다.
- Method Overview: 디스크리트 de Rham 미분 d: C₀→C₁을 정의하고 그 아드조인트 d*를 계산한다. TD 오류 δ를 d의 닫힌 범위에 정사영해 통합 가능한 성분을 얻고, 직교 보완인 토폴로지 잔여를 남긴다. HFPS는 두 개의 네트워크(값 함수와 잠재 함수)를 사용해 이 정사영된 성분만으로 정책을 최적화한다.
- Why It Matters: 비마코프 동역학을 정량적으로 진단하고, 기존 TD 학습이 실패하는 상황에서도 안정적 성능을 보장한다. 또한, 이론적 안정성·민감도 보장을 제공함으로써 실제 환경에서의 RL 적용 범위를 크게 확장한다.

### Reciprocal Latent Fields for Precomputed Sound Propagation
- Score: 8.5
- Reason: The paper introduces a novel memory‑efficient framework (Reciprocal Latent Fields) that leverages volumetric latent embeddings and Riemannian metric learning to encode acoustic parameters while preserving reciprocity. The technical contribution is solid, with a clear architectural design and a principled decoding strategy, and the results suggest significant practical benefits for real‑time audio rendering. Its impact is promising for immersive media and could inspire further research in efficient physics‑based simulation.
- Main Idea: 3‑D 장면의 음향 파동을 실시간으로 고품질 재현하기 위해, 공간마다 학습 가능한 잠재 임베딩 그리드를 사용하고, 대칭 디코더를 통해 상호 대칭성을 보장하는 Reciprocal Latent Fields (RLF) 프레임워크를 제안한다.
- Key Contribution: RLF는 잠재 공간을 Riemannian 메트릭으로 학습하여 복잡한 음향 현상을 압축하면서도 메모리 사용량을 수십 배 줄이고, 물리 기반 시뮬레이션과 동일한 품질의 임펄스 응답을 실시간으로 재생한다.
- Method Overview: 1) 3‑D 그리드에 고차원 잠재 임베딩을 배치하고, 2) 대칭성을 갖는 디코더(특히 Riemannian 메트릭 학습 기반)를 설계해 소스↔수신 간의 상호 대칭성을 보장한다. 3) 잠재 임베딩을 통해 임펄스 응답과 전체 음향 파라미터를 예측하고, 4) 압축된 표현을 실시간으로 디코딩해 음향 파동을 렌더링한다.
- Why It Matters: 전통적인 파동‑코딩 방식은 모든 소스‑수신 쌍을 사전 계산해 저장해야 하므로 메모리와 계산 비용이 급격히 증가한다. RLF는 잠재 그리드로 압축해 메모리 사용량을 크게 줄이면서도 물리 기반 시뮬레이션과 동일한 청각 품질을 제공하므로, 게임, VR, 실시간 시뮬레이션 등 대규모 상호작용 환경에서 실용적이다.

### Continuous-time reinforcement learning: ellipticity enables model-free value function approximation
- Score: 8.5
- Reason: The paper introduces a novel Sobolev‑prox fitted Q‑learning algorithm that leverages ellipticity of continuous‑time diffusions to establish Hilbert‑space positive definiteness of Bellman operators, enabling rigorous oracle inequalities for function approximation. The technical depth is substantial, with detailed functional‑analytic proofs and complexity analysis. Its insights on ellipticity as a key structural property are likely to influence future continuous‑time RL research, indicating strong long‑term impact.
- Main Idea: 
- Key Contribution: 
- Method Overview: 
- Why It Matters: 

### Uncovering Cross-Objective Interference in Multi-Objective Alignment
- Score: 8.5
- Reason: The paper proposes a novel algorithmic idea (CTWA) grounded in a rigorous local covariance law and extends it to clipped objectives, coupled with a global convergence analysis under PL conditions. Its technical depth is substantial, offering new theoretical insights into cross‑objective interference. The concepts and methods have strong potential to influence future multi‑objective alignment research, making it a high‑impact contribution.
- Main Idea: 다중 목표 정렬에서 목표 간 교차 간섭을 정의하고, 이를 이론적 공분산 법칙과 실용적 가중치 조정(CTWA)을 통해 완화하는 연구
- Key Contribution: 교차 간섭의 체계적 평가, 목표 보상과 학습 신호 사이의 공분산 조건 도출, CTWA 가중치 조정 알고리즘 제안, Polyak–Łojasiewicz 조건 하에서의 전역 수렴 보장
- Method Overview: 다양한 스칼라화 기법을 LLM 정렬 과제에 벤치마킹하고, 목표 보상 변화를 일차 근사로 분석해 공분산 법칙을 도출, 이를 기반으로 CTWA를 설계해 가중치를 동적으로 조정, 전역 수렴을 증명
- Why It Matters: 다중 목표 정렬에서 목표 간 상호 간섭을 줄여 LLM의 정합성과 안정성을 높이며, 실용적 가중치 조정으로 기존 스칼라화 방법보다 우수한 성능을 제공함으로써 대규모 언어 모델의 신뢰성을 향상시킴


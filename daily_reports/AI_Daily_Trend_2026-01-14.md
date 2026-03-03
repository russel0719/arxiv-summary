# 📅 2026년 1월 15일 AI 연구 동향 보고서  
> **제목**: *Geometric Stability: The Missing Axis of Representations*  
> **주요 아이디어**: 기하학적 안정성(Geometric Stability)을 도입해 표현(Representation)의 기하학적 구조가 얼마나 견고하게 유지되는지를 정량화하고, 이를 다양한 모델·도메인에 적용할 수 있는 **Shesha** 프레임워크를 제시합니다.

---

## 1️⃣ 전체 트렌드

| 분야 | 주요 트렌드 | 핵심 포인트 |
|------|-------------|-------------|
| **Representation & Diagnostics** | 기하학적 안정성(Geometric Stability) | CKA와 같은 전통적 유사도 지표와 독립적으로 동작하며, 선형 조정 가능성, 구조적 드리프트 감지, 전이성(Transferability)과의 분리성 등 다중 축을 제공 |
| **Generative & Diffusion Models** | **Flow‑based**와 **Diffusion** 모델의 제약조건 적용 | TOCFlow(최적 제어 기반), MAD(모션‑외관 분리) 등, 고차원 과학 데이터와 자율주행 시뮬레이션에 특화 |
| **Multimodal Reasoning** | **Omni‑R1**과 같은 단일 모델이 시각적 기능을 생성 | 텍스트-이미지 사이의 중간 단계(Zoom, 마킹, 예측)를 생성해 해석 가능성을 높임 |
| **Model Compression & Fusion** | LLM 기반 적응형 프루닝, SimMerge 등 | 프루닝은 LLM 자체가 지식 보존을 판단하고, Merge는 유사도 기반 예측으로 연산량을 획기적으로 절감 |
| **Human‑Robot Interaction** | PAIR + D‑STAR를 통한 물리적 일관성 보장 | 인간-인간 상호작용 데이터를 로봇에 재현해 실시간 전체 몸체 상호작용 학습 |

> **핵심 메시지**  
> 오늘날 AI 연구는 **표현의 기하학적 견고성**을 새로운 진단 축으로 삼으며, **다중 모달**과 **생성 모델**을 결합해 실제 환경(자율주행, 로봇)에서의 **안전성**과 **효율성**을 동시에 추구하고 있습니다.

---

## 2️⃣ CV‑관련 테마

| 논문 | 핵심 기여 | 적용 분야 |
|------|-----------|-----------|
| **COMPOSE** | 하이퍼그래프 분할을 통한 다중 뷰 3‑D 포즈 추정 | 로봇, 스포츠 분석, 의료 영상 |
| **Omni‑R1** | 중간 기능 이미지 생성으로 시각적 추론 강화 | VQA, 다이어그램 해석, 시각적 질문응답 |
| **MAD** | 모션‑외관 분리로 드라이빙 시뮬레이터 구축 | 자율주행 연구, 가상 현실 |
| **Terminally Constrained Flow‑Based Models** | 최적 제어 이론으로 제약조건 만족 샘플링 | 과학 시뮬레이션, PDE 솔루션 |
| **Learning Whole‑Body Human‑Humanoid Interaction** | 물리적 일관성을 갖춘 인간‑로봇 상호작용 데이터셋 | 로봇 제어, 인간-로봇 협업 |

> **트렌드 포인트**  
> - **다중 뷰**와 **하이퍼그래프**를 활용한 **정밀 포즈 추정**  
> - **생성 모델**을 이용한 **시각적 추론 단계**의 명시화  
> - **모션‑외관 분리**로 **실제 환경 시뮬레이션**의 효율성 향상

---

## 3️⃣ NLP‑관련 테마

| 논문 | 핵심 기여 | 적용 분야 |
|------|-----------|-----------|
| **LLMs can Compress LLMs** | LLM 자체가 프루닝 오라클 역할 | 대규모 언어 모델 압축, 모바일/임베디드 배포 |
| **SimMerge** | 유사도 신호 기반 Merge 전략 예측 | 체크포인트 결합, 지속적 학습 |
| **Omni‑R1‑Zero** | 텍스트‑전용 데이터로 멀티모달 추론 학습 | 멀티모달 모델 초기화, 비용 절감 |
| **Shesha** | 표현 기하학적 안정성 측정 | 모델 진단, 안전성 모니터링 |

> **트렌드 포인트**  
> - **LLM 자체가 지식 보존을 판단**하는 **자기 주도 프루닝**  
> - **유사도 기반 Merge**로 **연산 비용**을 최소화  
> - **텍스트‑전용**으로 **멀티모달 모델**을 **효율적으로** 학습

---

## 4️⃣ Cross‑Domain 방향

| 논문 | 핵심 기여 | 교차 적용 가능성 |
|------|-----------|------------------|
| **Shesha** | 기하학적 안정성 → 모델 진단, 안전성 | CV, NLP, RL, 생물정보학(CRISPR, 신경 기록) |
| **TOCFlow** | 제약조건 만족 샘플링 → 과학 데이터, 로봇 경로 계획 | 물리학, 로봇공학, 재료 과학 |
| **Omni‑R1** | 중간 이미지 생성 → 시각적 추론 | CV + NLP + RL (시각적 의사결정) |
| **MAD** | 모션‑외관 분리 → 시뮬레이터, 게임 엔진 | CV + RL + 시뮬레이션 |
| **PAIR + D‑STAR** | 물리적 일관성 보장 → 로봇 제어 | CV + RL + 물리 엔진 |

> **통합 시나리오**  
> 1. **Shesha**로 모델의 기하학적 안정성을 평가 → **TOCFlow**로 제약조건을 만족하도록 샘플링  
> 2. **Omni‑R1**이 생성한 중간 이미지를 **MAD**가 렌더링 → **실제 환경 시뮬레이터** 구축  
> 3. **PAIR**를 통해 인간-인간 상호작용 데이터를 로봇에 재현 → **D‑STAR**가 실시간 반응 학습  

---

## 📌 핵심 Take‑away

- **표현의 기하학적 안정성**이 **전통적 유사도**와 **독립적인 진단 축**으로 부상  
- **멀티모달 추론**은 **생성 단계**를 명시화해 **해석 가능성**과 **효율성**을 동시에 달성  
- **LLM 기반 프루닝**과 **유사도 기반 Merge**는 **모델 경량화**와 **연산 비용 절감**을 가능하게 함  
- **다중 도메인**(CV, NLP, RL, 과학) 간 **교차 활용**이 가속화되고 있으며, **실제 환경**(자율주행, 로봇, 시뮬레이션)에서의 적용이 가시화되고 있음  

> **향후 연구 방향**  
> - 기하학적 안정성 지표를 **실시간 모니터링**에 통합  
> - **멀티모달 생성 모델**을 **강화 학습**과 결합해 **자율적 시뮬레이터** 구축  
> - **LLM 프루닝**을 **다중 언어** 및 **다중 도메인**에 확장  
> - **물리 기반 제약**을 **생성 모델**에 통합해 **과학 데이터** 생성의 정확성 향상  

---

## 개별 논문 요약

### Geometric Stability: The Missing Axis of Representations
- Score: 9
- Reason: The paper proposes a novel, well-motivated metric—geometric stability—distinct from traditional similarity measures, backed by a comprehensive framework (Shesha) and extensive cross-domain analysis. It offers deep technical insights into representational robustness and demonstrates actionable implications for safety, controllability, and model selection, indicating strong potential for long-term impact across AI and biological systems.
- Main Idea: Introduce geometric stability as a perturbation‑based metric that quantifies how faithfully a representation’s manifold geometry persists, and build Shesha, a framework that operationalizes this metric across diverse models and domains.
- Key Contribution: Show that geometric stability is empirically independent of traditional similarity measures (CKA), predicts linear steerability, detects structural drift twice as fast, decouples from transferability, and generalizes to biological systems such as CRISPR screens and neural recordings.
- Method Overview: Compute Shesha by measuring the consistency of representational dissimilarity matrices (RDMs) under perturbations (e.g., bootstrapping, data augmentation, principal‑component removal). Evaluate 2,463 encoder configurations across seven domains, compare Shesha scores with CKA similarity, and perform spectral deletion experiments to demonstrate orthogonality.
- Why It Matters: Provides a complementary, orthogonal diagnostic axis for auditing learned representations, enabling early safety monitoring, controllability assessment, and robust model selection beyond what similarity metrics can reveal.

### COMPOSE: Hypergraph Cover Optimization for Multi-view 3D Human Pose Estimation
- Score: 8
- Reason: Introduces a novel hypergraph partitioning framework for multi‑view pose correspondence, coupled with a clever geometric pruning strategy that reduces ILP complexity. The method demonstrates significant technical depth in formulating and solving a combinatorial optimization problem, and its generality suggests strong long‑term impact on multi‑view perception tasks.
- Main Idea: Reformulate multi‑view 3‑D human pose estimation as a hypergraph partitioning problem, where 2‑D detections are nodes and hyperedges encode higher‑order consistency across all cameras, enforcing global cycle consistency.
- Key Contribution: An optimization‑based framework (COMPOSE) that uses hypergraph partitioning with geometric pruning to solve an integer linear program, achieving up to 23 % AP improvement over prior optimization methods and 11 % over self‑supervised end‑to‑end approaches, while remaining scalable and robust to sparse views.
- Method Overview: Detect 2‑D keypoints per view, construct a weighted hypergraph with nodes as detections and hyperedges as multi‑view joint hypotheses, prune unlikely hyperedges via geometric consistency checks, solve the resulting ILP to partition the graph into disjoint 3‑D joints, and triangulate the selected correspondences to recover 3‑D poses.
- Why It Matters: Provides a principled, globally consistent alternative to pairwise matching, enabling accurate, scalable 3‑D pose estimation from few cameras without large 3‑D labeled datasets, which is critical for safety‑critical and high‑stakes applications such as robotics and medical monitoring.

### LLMs can Compress LLMs: Adaptive Pruning by Agents
- Score: 8
- Reason: Introduces a novel agent-guided pruning framework that leverages a foundation model as an adaptive pruning agent, combining weight-activation metrics with gradient importance and self-reflection to iteratively refine pruning decisions. The technical depth is moderate, involving statistical normalization, LLM-driven decision making, and rollback mechanisms. The approach opens a new research direction for model compression, suggesting high long-term impact.
- Main Idea: Use a large language model as an adaptive pruning oracle that decides per‑layer sparsity based on a layer‑wise sensitivity profile, self‑reflects on the impact of each pruning step, and rolls back if performance degrades, all without retraining.
- Key Contribution: First agent‑driven, adaptive pruning strategy that learns which layers to prune, preserving knowledge pathways and achieving >45% sparsity with substantial gains in MMLU accuracy and factual recall on Qwen‑3, while remaining model‑agnostic and retraining‑free.
- Method Overview: Compute a composite sensitivity score for each layer (Wanda‑style weight‑activation + gradient importance), normalize to z‑scores, feed the profile to an LLM agent that selects pruning ratios per layer. After pruning, evaluate perplexity and downstream accuracy; if degradation exceeds a threshold, rollback to the last good checkpoint and penalize the agent. Iterate this self‑reflection loop until desired sparsity is reached.
- Why It Matters: It dramatically reduces factual knowledge loss common in structured pruning, delivers measurable accuracy improvements, offers a safe, retraining‑free compression pipeline applicable to any LLM, and demonstrates that foundation models can guide the compression of other foundation models, paving the way for efficient large‑scale deployment.

### Omni-R1: Towards the Unified Generative Paradigm for Multimodal Reasoning
- Score: 8
- Reason: Omni‑R1 proposes a novel unified generative multimodal reasoning framework that generates intermediate images to bridge diverse reasoning skills, introduces perception alignment loss and reward in an SFT+RL setting, and offers a zero‑annotation variant. The technical depth is moderate, with a clear two‑stage training pipeline and novel loss/reward design. Its approach could significantly influence future multimodal reasoning research by reducing task‑specific engineering and annotation costs, warranting a strong impact score.
- Main Idea: Unify multimodal reasoning by generating intermediate functional images as part of a generative reasoning chain, allowing a single model to perform diverse visual operations (zoom, marking, prediction) across tasks.
- Key Contribution: Omni‑R1, a two‑stage (SFT + RL) framework that learns reusable visual skills and aligns perception with task outputs, plus Omni‑R1‑Zero which bootstraps the same pipeline from text‑only data, demonstrating that a single generative model can match or exceed task‑specific baselines.
- Method Overview: The model alternates text inference and image generation, producing intermediate images (e.g., zoomed crops, annotated boxes, imagined paths).  SFT uses a perception‑alignment loss to ground hidden states in a visual codebook, while RL refines the policy with a perception‑calibrated reward that encourages functional image quality.  Zero‑annotation training leverages text‑only reasoning data to generate step‑wise visualizations without multimodal supervision.
- Why It Matters: It removes the need for task‑specific pipelines and costly interleaved annotations, improves interpretability by making reasoning steps explicit, and scales to a broad range of multimodal tasks (VQA, diagram reasoning, grounding) with a single, versatile model.

### Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
- Score: 8
- Reason: The paper proposes two novel algorithmic contributions—Physics-Aware Interaction Retargeting (PAIR) for preserving contact semantics across morphology differences, and Decoupled Spatio-Temporal Action Reasoner (D-STAR) with phase attention and multi-scale spatial modules—both of which demonstrate significant technical depth and promise for advancing whole-body human-humanoid interaction. The integration of physics-aware retargeting with a hierarchical diffusion-based policy addresses key gaps in current imitation learning, suggesting a strong long-term impact on collaborative robotics research.
- Main Idea: Convert abundant human‑human interaction recordings into physics‑consistent human‑humanoid clips using a contact‑aware retargeting pipeline, then train a policy that learns synchronized whole‑body interactions.
- Key Contribution: PAIR, a two‑stage physics‑aware interaction retargeting framework that preserves morphology and contact semantics, and D‑STAR, a decoupled spatio‑temporal policy that learns intent‑aware, responsive interactions.
- Method Overview: PAIR first aligns human skeletons to a humanoid robot’s kinematic structure and then refines the motion with a contact‑centric loss. The resulting HHoI dataset trains D‑STAR, which uses phase attention, multi‑scale spatial encoding, and a diffusion head to generate synchronized motions executed by a whole‑body controller on a Unitree G1 robot.
- Why It Matters: It overcomes data scarcity and imitation limitations, enabling scalable, physics‑consistent learning of complex, contact‑rich interactions for humanoid robots, and demonstrates real‑time execution via text commands.

### Terminally constrained flow-based generative models from an optimal control perspective
- Score: 8
- Reason: The paper introduces a novel optimal-control framework for sampling from terminally constrained distributions using pre-trained flow-based generative models, deriving a Hamilton-Jacobi-Bellman characterization and a closed-form damping factor that captures second-order geometry without matrix inversions. The technical depth is substantial, involving control theory, differential geometry, and stochastic processes, and the method demonstrates significant improvements over existing guidance techniques. Its potential for broad applicability across scientific domains suggests a strong long-term research impact.
- Main Idea: TOCFlow applies optimal‑control theory to flow‑based generative models, enabling samples to satisfy hard terminal constraints without retraining the model.
- Key Contribution: A geometry‑aware, closed‑form damping factor that turns the optimal‑control proximal problem into a scalar line search, preserving Gauss–Newton accuracy while incurring only gradient‑level cost.
- Method Overview: The method casts constrained sampling as a finite‑horizon control problem, derives the HJB equation, and solves the control law in a terminal co‑moving frame. The resulting update applies a scalar damping to the Riemannian gradient, implicitly accounting for curvature and steering samples to the constraint manifold.
- Why It Matters: It allows high‑dimensional scientific generative models (e.g., PDE solutions, trajectory planning, turbulence) to enforce strict equality, inequality, and global statistical constraints efficiently, improving accuracy over Euclidean guidance and projection baselines while preserving generative quality.

### SimMerge: Learning to Select Merge Operators from Similarity Signals
- Score: 8
- Reason: Introduces a novel predictive merge-selection framework that replaces costly search with similarity-based predictions, demonstrating solid technical depth in feature engineering and bandit adaptation, and offers significant long‑term impact for scalable LLM composition.
- Main Idea: Predict the best merge operator and order for fine‑tuned LLM checkpoints using inexpensive probe‑based similarity features, eliminating costly merge‑and‑evaluate loops.
- Key Contribution: A lightweight, task‑agnostic similarity predictor that selects merge strategies and orders, generalizes to larger models and multi‑way merges, and supports continual learning via a bandit extension.
- Method Overview: Probe each checkpoint with a small unlabeled set, extract functional (logits, hidden‑state similarity) and structural (weight norms, layer statistics) features, feed them into a trained selector that predicts the optimal merge operator and, for multi‑way merges, the merge sequence, then execute a single merge pass.
- Why It Matters: It dramatically reduces the computational burden of composing large‑scale language‑model checkpoints, enables scalable checkpoint fusion when evaluation budgets are limited, and demonstrates that learned merge planning outperforms hand‑crafted averaging across diverse model sizes and tasks.

### MAD: Motion Appearance Decoupling for efficient Driving World Models
- Score: 8
- Reason: The paper introduces a novel two-stage motion-appearance decoupling framework that efficiently adapts generalist video diffusion models into controllable driving world models, demonstrating significant compute savings and strong performance. The technical depth is evident in the design of skeletonized motion learning and subsequent appearance synthesis, along with the integration of diverse control modalities. The approach offers a promising direction for scalable, physically consistent driving simulators, suggesting substantial long-term impact on autonomous vehicle research and simulation-based training.
- Main Idea: MAD (Motion‑Appearance Decoupling) transforms any general video diffusion model into a controllable driving‑world model by separating motion reasoning from appearance rendering in a lightweight two‑stage pipeline.
- Key Contribution: It achieves state‑of‑the‑art driving‑world performance while using <6 % of the compute and data of prior SOTA models, scales to large backbones (MAD‑LTX), and requires only minimal domain‑specific supervision.
- Method Overview: Stage 1: fine‑tune the backbone with a motion LoRA adapter on skeletonized videos to learn structured, physically plausible motion of all agents. Stage 2: reuse the same backbone with an appearance LoRA adapter to render photorealistic RGB frames conditioned on the motion sequence. Control signals (poses, ego‑motion, text) are projected into the model’s visual latent space via its pretrained VAE, enabling a chain‑of‑thought reasoning‑then‑rendering workflow.
- Why It Matters: MAD dramatically lowers the barrier to building high‑quality, controllable driving simulators—research labs can now train competitive models with a fraction of the GPU hours and data, enabling richer autonomous‑driving research and safer, more realistic scenario generation.


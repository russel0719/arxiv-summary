# 📅 2026년 3월 27일 AI 연구 동향 보고서  
(한국어 요약, Markdown 형식)

---

## 1️⃣ 전체 트렌드  
| 분야 | 핵심 이슈 | 대표 논문 |
|------|-----------|-----------|
| **보안·사이드채널** | 로컬 Vision‑Language Model(VLM)에서 동적 전처리 과정이 하드웨어 타이밍/캐시를 통해 민감 정보를 유출 | *Shape and Substance: Dual‑Layer Side‑Channel Attacks on Local Vision‑Language Models* |
| **양자·분자 시뮬레이션** | 딥러닝 VMC + GP를 결합해 강한 전자 상관 시스템의 PES를 저비용으로 탐색 | *Enabling ab initio geometry optimization of strongly correlated systems with transferable deep quantum Monte Carlo* |
| **의료·생체정보** | 3D 의료 영상 합성 및 컨트롤, 걸음걸이 기반 다중 체계 건강 예측 | *VolDiT: Controllable Volumetric Medical Image Synthesis with Diffusion Transformers*<br>*A Gait Foundation Model Predicts Multi‑System Health Phenotypes from 3D Skeletal Motion* |
| **멀티모달 비디오** | VLM 기반 제로‑샷 이상 탐지 및 자연어 설명 | *GridVAD: Open‑Set Video Anomaly Detection via Spatial Reasoning over Stratified Frame Grids* |
| **AI 안전성** | 디자인‑타임 검증, 개념 제거 프레임워크 | *Decidable By Construction: Design‑Time Verification for Trustworthy AI*<br>*Z‑Erase: Enabling Concept Erasure in Single‑Stream Diffusion Transformers* |
| **물리‑머신러닝** | Hessian‑인포메이션 활용 인터아토믹 포텐셜 | *Hessian‑informed machine learning interatomic potential towards bridging theory and experiments* |

> **핵심 메시지**  
> - **보안**과 **신뢰성**이 AI 모델 배포의 핵심 이슈로 부상.  
> - **멀티모달**(CV+NLP) 융합이 의료·보안·비디오 등 실세계 적용에서 큰 성과를 내고 있음.  
> - **물리 기반** 딥러닝(양자, 물리 시뮬레이션) 융합이 과학 연구의 비용을 획기적으로 낮추고 있음.

---

## 2️⃣ CV(Computer Vision) 관련 테마  
| 주제 | 핵심 내용 | 대표 논문 |
|------|-----------|-----------|
| **사이드채널 공격** | VLM 전처리 단계에서 이미지 패치 수·배열을 OS 타이밍으로 추정, perf_event_open 으로 시각적 밀도 구분 | *Shape and Substance* |
| **의료 영상 합성** | 3D 패치 토큰화 + 글로벌 셀프 어텐션, 타임스텝‑게이트 컨트롤 어댑터로 고해상도 의료 영상 생성 | *VolDiT* |
| **걸음걸이 기반 건강 예측** | MAE 기반 자가 지도 학습으로 걸음걸이 임베딩 생성, 3,210개 표현형 예측 | *A Gait Foundation Model* |
| **비디오 이상 탐지** | VLM으로 자연어 이상 설명 → Grounding DINO + SAM2로 픽셀‑레벨 마스크 생성 | *GridVAD* |
| **컨셉 제거** | 단일 스트림 확산 변환기에서 텍스트만 LoRA 적용, 라그랑주 가이드로 품질 보존 | *Z‑Erase* |

> **주요 트렌드**  
> - **전처리 단계** 자체가 보안 취약점이 될 수 있음 → 하드웨어‑레벨 모니터링 필요.  
> - **전역 어텐션** 기반 3D 모델이 기존 U‑Net 대비 성능 상승.  
> - **멀티모달**(VLM+SAM2) 융합으로 비디오 이상 탐지에서 라벨 없이도 정밀 마스크 생성 가능.

---

## 3️⃣ NLP(자연어 처리) 관련 테마  
| 주제 | 핵심 내용 | 대표 논문 |
|------|-----------|-----------|
| **VLM 기반 비디오 설명** | VLM이 자연어로 이상을 제안 → SCC로 일관성 확보 | *GridVAD* |
| **컨셉 제거** | 텍스트 토큰만 LoRA 적용해 개념을 안정적으로 제거 | *Z‑Erase* |
| **디자인‑타임 검증** | AI 모델 설계 단계에서 수학적 검증을 통해 안전성 확보 | *Decidable By Construction* |
| **멀티모달 통합** | CV(이미지) + NLP(텍스트) 융합으로 비디오 이상 탐지 및 설명 | *GridVAD* |

> **핵심 트렌드**  
> - **VLM**이 비디오 이상 탐지에서 핵심 역할을 수행하며, **자연어**를 통해 설명 가능성을 제공.  
> - **컨셉 제거**는 모델 안전성 확보를 위한 핵심 기술로 부상.  
> - **설계‑타임 검증**은 AI 시스템의 신뢰성을 보장하는 새로운 패러다임.

---

## 4️⃣ Cross‑Domain (다분야) 방향  
| 분야 | 융합 포인트 | 기대 효과 |
|------|-------------|-----------|
| **CV + 보안** | VLM 전처리 사이드채널 → 하드웨어 보안 설계 | Edge AI에서 개인정보 보호 강화 |
| **CV + 의료** | VolDiT + Gait Foundation Model | 고해상도 의료 영상 합성 + 비침습적 건강 모니터링 |
| **CV + NLP** | GridVAD (VLM + SAM2) | 라벨 없이도 정밀 비디오 이상 탐지 및 자연어 설명 |
| **CV + 물리‑머신러닝** | Hi‑MLIP + VMC+GP | 물리 기반 시뮬레이션과 머신러닝 융합으로 비용 절감 |
| **NLP + 보안** | Z‑Erase + Design‑Time Verification | 모델 안전성 및 편향 제거를 동시에 달성 |
| **NLP + 의료** | VLM 기반 자연어 설명 + 의료 영상 | 환자 상태를 자연어로 실시간 보고 가능 |

> **전망**  
> - **멀티모달** 융합이 AI 연구의 핵심 동력으로 자리 잡음.  
> - **보안**과 **신뢰성**이 설계 단계부터 고려되는 **Design‑Time** 접근이 표준화될 전망.  
> - **물리‑머신러닝** 융합으로 과학 연구의 비용과 시간 단축이 가속화될 것.

---

## 📌 요약  
- **보안**과 **신뢰성**이 AI 배포의 핵심 이슈로 부상.  
- **멀티모달**(CV+NLP) 융합이 의료·비디오·보안 등 실세계 적용에서 큰 성과를 내고 있음.  
- **물리 기반** 딥러닝 융합이 과학 연구의 비용을 획기적으로 낮추고 있음.  

> **다음 주 예고**  
> - **AI 모델의 해석 가능성**과 **설계‑타임 검증**에 대한 심층 연구.  
> - **전역 어텐션 기반 3D 모델**의 확장 가능성 탐색.  
> - **사이드채널 보안**에 대한 실시간 모니터링 프레임워크 발표 예정.  

---

## 개별 논문 요약

### Shape and Substance: Dual-Layer Side-Channel Attacks on Local Vision-Language Models
- Score: 8.7
- Reason: The paper introduces a novel dual‑layer side‑channel attack exploiting dynamic preprocessing in on‑device VLMs, demonstrating deep technical insight into timing and cache‑based leakage. Its findings highlight a fundamental architectural vulnerability with broad implications for secure edge AI, positioning it as a high‑impact contribution to future research on privacy‑preserving model design.
- Main Idea: 현대 Vision‑Language Model(VLM)의 동적 고해상도 전처리 과정이 알고리즘적 사이드채널을 생성한다는 점을 밝히고, 이를 이용해 이미지의 기하학적 구조와 시각적 밀도를 추론하는 두 단계 공격을 제시한다.
- Key Contribution: (1) 동적 전처리 기반 알고리즘 사이드채널을 실증하고, (2) OS 수준 타이밍과 하드웨어 성능 카운터를 결합한 실용적 이중 레이어 공격 프레임워크를 제안하며, (3) 공격이 민감 정보 유출에 미치는 영향을 정량화하고, (4) 패딩·캐시 블라인딩 등 완화 방안을 분석해 Edge AI 보안 설계 가이드를 제공한다.
- Method Overview: Tier 1에서는 비특권 프로세스가 OS에서 제공하는 CPU 타이밍을 측정해 이미지 패치 수와 배열(가로·세로 비율)을 추정한다. Tier 2에서는 perf_event_open을 통해 접근 가능한 하드웨어 성능 카운터(LLC 캐시 충돌)를 모니터링해 같은 기하학을 가진 이미지 중 시각적 밀도(예: 의료 스캔 vs. 문서)를 구분한다. 두 신호를 결합해 입력 이미지의 민감한 특성을 복원한다.
- Why It Matters: 동적 전처리를 채택한 최신 VLM은 로컬 실행에서도 하드웨어 공유 자원을 통해 입력 정보를 노출할 수 있음을 보여 주며, 이는 Edge AI 배포 시 개인정보 보호와 시스템 성능 사이의 균형을 재고하도록 요구한다. 또한, 기존의 메모리 격리만으로는 충분하지 않음을 시사해 새로운 보안 설계 원칙과 완화 기술의 필요성을 강조한다.

### Enabling ab initio geometry optimization of strongly correlated systems with transferable deep quantum Monte Carlo
- Score: 8.7
- Reason: The paper introduces a novel framework that couples transferable deep-learning VMC with on-the-fly Gaussian process regression to efficiently explore PESs of strongly correlated systems, a nontrivial algorithmic contribution. It demonstrates substantial technical depth through integration of stochastic wavefunction optimization, force and Hessian estimation, and sparse GP modeling. The approach promises long-term impact by enabling accurate ab initio studies of complex chemical processes in multi-reference regimes, potentially transforming computational chemistry workflows for strongly correlated materials and reactions.
- Main Idea: 전이 가능한 딥러닝 VMC와 가우시안 프로세스 회귀를 결합한 하이브리드 프레임워크를 개발해, 강한 전자 상관을 갖는 분자의 잠재 에너지 곡면(PES)을 효율적으로 고정밀 탐색한다.
- Key Contribution: 노이즈가 많은 VMC 출력을 확률적 GP 서브시트로 변환해, 한 번의 훈련으로 다양한 구조에서 에너지·힘·헤시안을 무조건 예측할 수 있는 스케일러블한 stochastic‑to‑deterministic 파이프라인을 제공한다.
- Method Overview: 1) 딥러닝 파동함수를 VMC로 한 번 훈련하고, 여러 핵구조에서 에너지·힘·헤시안을 추정한다. 2) VMC를 희소한 포인트에서만 평가하고, 그 데이터를 GP에 입력해 부드러운 PES 서브시트를 만든다. 3) GP의 예측과 불확실성을 이용해 기하학 최적화, 전이상 검색, 최소 에너지 경로를 수행한다.
- Why It Matters: 전통적인 DFT 기반 기하학 최적화가 실패하는 강한 상관·전자기상 시스템에서도, 전체 VMC 계산 없이도 고정밀 PES를 얻어 반응 동역학과 전이상 탐색을 저비용으로 수행할 수 있어, 복잡한 화학 과정의 예측력을 크게 향상시킨다.

### A Gait Foundation Model Predicts Multi-System Health Phenotypes from 3D Skeletal Motion
- Score: 8.7
- Reason: The paper introduces a novel foundation model that learns rich embeddings from 3D skeletal motion, achieving superior predictive performance across a wide range of health phenotypes. The technical depth is evident in the use of deep learning, extensive ablation studies, and multi-system analysis. Its long‑term impact is high, positioning gait as a scalable, passive vital sign that could be deployed via consumer‑grade video for broad health monitoring.
- Main Idea: 3D 골격 움직임 데이터를 자가 지도 학습으로 처리해, 걸음걸이 임베딩을 생성하고 이를 통해 다양한 건강 표현형을 예측하는 모델을 개발했다.
- Key Contribution: 학습된 걸음걸이 임베딩이 기존 엔지니어링된 특징보다 우수하며, 3,210개의 표현형 중 1,980개를 독립적으로 예측해 18개 체계에 걸친 건강 정보를 제공한다. 또한 다리와 몸통의 기여도를 해석해 생물학적 의미를 밝혀냈다.
- Method Overview: 3,414명의 성인을 대상으로 깊이 카메라로 5가지 동작을 기록한 3D 골격 데이터를 수집하고, 마스킹 오토인코더(MAE)를 이용해 자가 지도 학습으로 걸음걸이 임베딩을 학습했다. 학습된 임베딩을 선형 모델에 적용해 연령, BMI, VAT 등과 독립적으로 3,210개 표현형을 평가하고, 다리/몸통 마스킹 실험으로 해석성을 확보했다.
- Why It Matters: 이 접근법은 소비자용 비디오에서도 활용 가능한 저비용, 비침습적 다중 체계 바이오마커를 제공해 대규모 건강 모니터링과 조기 위험 탐지에 혁신을 가져올 수 있다.

### VolDiT: Controllable Volumetric Medical Image Synthesis with Diffusion Transformers
- Score: 8.7
- Reason: Introduces the first fully transformer-based 3D diffusion model with volumetric patch embeddings and a novel timestep‑gated control adapter for segmentation‑based conditioning, offering deep technical contributions and promising long‑term impact on volumetric medical image synthesis.
- Main Idea: 3D 의료 영상 합성을 위한 순수 트랜스포머 기반 확산 모델 VolDiT를 제안한다.
- Key Contribution: 첫 번째 순수 트랜스포머 백본과 3D 패치 임베딩, 글로벌 셀프 어텐션, 시계열-가변 컨트롤 어댑터를 도입해 U‑Net 기반 모델을 능가한다.
- Method Overview: 3D 패치를 토큰화해 시퀀스로 변환하고, 전역 셀프 어텐션으로 전역 의존성을 학습한다. 타임스텝-게이트 컨트롤 어댑터는 세그멘테이션 마스크를 토큰화해 각 디노이징 단계에서 조건부를 정밀하게 조절한다.
- Why It Matters: 전역 모델링과 정밀한 공간 조건부를 동시에 달성해 고해상도 의료 영상 합성의 품질과 일관성을 크게 향상시키며, 임상 및 연구에서의 활용 가능성을 확대한다.

### Z-Erase: Enabling Concept Erasure in Single-Stream Diffusion Transformers
- Score: 8.7
- Reason: The paper introduces a genuinely novel algorithmic framework—Stream Disentangled Concept Erasure combined with Lagrangian‑Guided Adaptive Modulation—that addresses a critical safety gap in single‑stream diffusion transformers. The technical depth is evident from the rigorous convergence analysis to Pareto stationary points and the careful balancing of erasure versus preservation. Its long‑term impact is substantial, as it opens a scalable path for concept erasure in the rapidly growing family of single‑stream T2I models, potentially influencing future safety‑centric design of generative systems.
- Main Idea: Z‑Erase는 텍스트와 이미지 토큰이 하나의 시퀀스로 결합된 단일 스트림 확산 변환기에서 개념을 제거하기 위한 최초의 프레임워크이다.
- Key Contribution: 스트림 분리 개념 제거 프레임워크와 라그랑주 가이드 적응형 조절을 도입해 기존 방법이 초래하던 생성 붕괴 없이 안정적으로 개념을 제거한다는 점이다.
- Method Overview: 시각 경로를 고정하고 텍스트에만 LoRA를 적용해 업데이트 동역학을 분리한 뒤, 제약 최적화에서 라그랑주 승수를 사용해 제거 강도와 이미지 품질 사이의 균형을 동적으로 조정한다.
- Why It Matters: 단일 스트림 모델에서 안전하고 품질을 유지한 채 개념을 제거할 수 있어, 저작권, NSFW, 편향된 콘텐츠를 방지하고 차세대 모델의 안전 정렬에 필수적인 솔루션을 제공한다.

### GridVAD: Open-Set Video Anomaly Detection via Spatial Reasoning over Stratified Frame Grids
- Score: 8.5
- Reason: GridVAD introduces a novel propose‑ground‑propagate framework that repurposes VLMs as anomaly proposers, coupled with self‑consistency filtering and grounding‑based propagation, offering a training‑free, efficient zero‑shot solution. The method integrates advanced vision‑language reasoning, grounding, and segmentation modules, demonstrating substantial technical depth. Its general, modular design and strong zero‑shot performance suggest significant long‑term impact on open‑set video anomaly detection and related zero‑shot perception tasks.
- Main Idea: VLM을 활용해 비디오에서 이상을 자연어로 제안하고, 그 제안을 바탕으로 정밀한 공간-시간 마스크를 생성하는 제안‑정착‑전파 파이프라인을 통해 오픈‑셋, 제로‑샷 이상 탐지
- Key Contribution: ① VLM을 이상 제안기로 활용해 사전 정의된 라벨 없이 자유로운 이상 설명 가능
② Self‑Consistency Consolidation(SCC)으로 가짜 제안을 통계적으로 제거
③ Grounding DINO와 SAM2를 결합해 정밀한 바운딩 박스와 픽셀‑레벨 마스크를 자동 생성
④ 영상 길이에 관계없이 고정된 VLM 호출 수로 비용 효율적
- Method Overview: 1) 스트래티파이드 그리드 샘플링으로 영상 전체를 몇 개의 그리드 이미지에 압축
2) 각 그리드 이미지에 VLM을 쿼리해 자연어 이상 설명과 임시 구간을 제안
3) 독립 샘플링 결과를 SCC로 교차 검증해 일관된 제안만 보존
4) Grounding DINO로 제안에 바운딩 박스 매핑, SAM2로 박스를 전역 픽셀 마스크로 전파
- Why It Matters: 제로‑샷으로 새로운 이상을 탐지하고, 오픈‑셋 자연어 설명을 제공하며, VLM 호출 수를 크게 줄여 실시간 인터넷 규모 적용이 가능해 기존 최고 성능을 초과한다.

### Decidable By Construction: Design-Time Verification for Trustworthy AI
- Score: 8.5
- Reason: The paper proposes a novel design‑time verification framework that leverages decidable algebraic constraints over finitely generated abelian groups, integrating type systems, hypergraph inference, and coeffect analysis. The technical depth is substantial, combining advanced type theory, Clifford algebra, and a connection to Solomonoff induction. If the claims hold, it could fundamentally shift AI reliability practices, offering a low‑overhead, formally grounded alternative to post‑hoc verification, indicating strong long‑term research impact.
- Main Idea: 
- Key Contribution: 
- Method Overview: 
- Why It Matters: 

### Hessian-informed machine learning interatomic potential towards bridging theory and experiments
- Score: 8.5
- Reason: Introduces a novel Hessian-informed MLIP with an efficient HINT training protocol, demonstrating deep technical innovation and promising long-term impact by enabling accurate curvature-aware predictions for complex materials.
- Main Idea: Hessian‑인포메이션을 활용한 기계학습 인터아토믹 포텐셜(Hi‑MLIP) 개발과, Hessian 정보를 효율적으로 슈퍼바이즈하기 위한 HINT 프로토콜 도입
- Key Contribution: Hessian 라벨을 2~4 차수 감소시키면서도 전이상, Gibbs 자유에너지, 강한 비조화성 하이드라이드의 음향 특성까지 정확히 예측할 수 있는 데이터 효율적 프레임워크 제공
- Method Overview: HINT는 Hessian 프리트레이닝, 대표 구조 샘플링, 커리큘럼 학습, 스토캐스틱 프로젝션 Hessian 손실을 결합한 4단계 프로세스이며, Hi‑MLIP은 에너지·힘·Hessian을 일관되게 예측하기 위해 분석적 미분을 사용
- Why It Matters: 첫 번째 원리 시뮬레이션과 실험 관측 사이의 정밀도를 크게 향상시키며, 고비용 DFT Hessian 계산 없이도 전이상 탐색, 자유에너지 계산, 비조화성 물리학 연구를 가능하게 함


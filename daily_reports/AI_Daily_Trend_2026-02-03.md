# **Conformal Reachability for Safe Control in Unknown Environments**  
*일일 AI 연구 동향 보고서 (2026‑02‑04)*  

---

## 📈 전체 트렌드  
- **데이터 기반 안전성 보장**: 컨포멀 예측과 도달성 분석을 결합해 모델이 알려지지 않은 연속 동역학에서도 확률적 안전 보장을 제공하는 연구가 주류를 이루고 있다.  
- **메모리‑기반 스케일링**: 파라미터 대신 ROM 기반 lookup 테이블을 활용해 모바일·엣지 디바이스에서도 대형 LLM을 실행할 수 있는 메모리‑기반 아키텍처가 부상하고 있다.  
- **비유클리드 최적화와 배치 크기 적응**: signSGD, specSGD 같은 비유클리드 기법에 맞춘 그라디언트 노이즈 스케일(GNS)을 활용해 배치 크기를 동적으로 조정하는 이론 기반 프레임워크가 주목받고 있다.  
- **반사실적 생성과 시뮬레이션**: 확산 모델을 활용해 원하는 미래 레지먼을 조건으로 한 반사실적 시장 데이터와 LOB를 생성하는 연구가 실무 적용 가능성을 높이고 있다.  
- **기호적 해석과 구조 인식**: 트리‑기반 트랜스포머와 강화학습을 결합해 PDE의 기호적 해를 자동으로 탐색하는 구조‑의식형 모델이 새로운 연구 방향을 제시한다.  

---

## 🖼️ CV‑관련 주제  
| 논문 | 핵심 아이디어 | 주요 기여 | 방법 개요 | 실용적 의미 |
|------|--------------|-----------|-----------|-------------|
| **3D‑Aware Implicit Motion Control for View‑Adaptive Human Video Generation** | 2D 드라이빙 비디오에서 3D 움직임을 암시적으로 학습해 텍스트‑기반 카메라 제어와 결합 | 1) 시점 독립 3D 움직임 표현 2) 비디오 디퓨전 모델과 cross‑attention 연동 3) 텍스트‑기반 카메라 제어 지원 | 드라이빙 프레임 → 두 개 인코더 → 시점 무관 토큰 → DiT 기반 디퓨전 모델에 cross‑attention 주입 → 재구성·교차‑시점 손실 | 2D 포즈/SMPL 기반 한계 극복 → 영화·게임·VR에서 실시간 인간 비디오 합성 가능 |
| **DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books** | 미래 시장 레지먼을 조건으로 한 확산 모델로 반사실적 LOB 생성 | 1) 원하는 레지먼 지정 가능 2) 컨트롤러블 리얼리즘·반사실적 유효성·활용성 평가 지표 제시 3) 실용적 도구 제공 | Wavenet‑스타일 잔차 블록 + FiLM + ControlNet‑유사 모듈 | 위험 관리·전략 검증에 필요한 가상 시장 데이터 제공, 기존 시뮬레이션보다 상황 기반 분석 가능 |

> **CV 영역**은 주로 시각적 데이터와 동작 생성에 초점을 맞추고 있으며, 3D‑모델링과 반사실적 생성이 핵심이다.

---

## 📚 NLP‑관련 주제  
| 논문 | 핵심 아이디어 | 주요 기여 | 방법 개요 | 실용적 의미 |
|------|--------------|-----------|-----------|-------------|
| **MeKi: Memory‑based Expert Knowledge Injection for Efficient LLM Scaling** | 토큰‑레벨 메모리 전문가를 Transformer 층에 도입해 ROM 기반 lookup 테이블에 지식 저장 | 4B 모델과 유사 성능을 1.7B 베이스라인과 동일 추론 속도로 달성 | 각 층에 메모리 전문가 추가 → 파라미터 재파라미터화 → 정적 lookup 테이블 활용 | 모바일 SoC에서 RAM·NPU 제약 극복, 추론 지연·전력 소비 대폭 감소 |
| **Bridging Online and Offline RL: Contextual Bandit Learning for Multi‑Turn Code Generation** | 오프라인 트레저리와 온라인 컨텍스트 밴딧 학습 결합 | 샘플 효율성과 온라인 성능 동시에 확보, COBALT 방법 제시 | LLM으로 트레저리 생성 → 프리픽스 분할 → 컨텍스트 밴딧 학습 → 보상 해킹 탐지 | 저비용·안정적 학습 파이프라인 제공, 실무 코드 생성 성능 향상 |
| **Bayesian Conformal Prediction as a Decision Risk Problem** | 베이지안 사후 예측밀도를 비준수성 점수로 사용, 위험‑최소화 기준으로 임계값 결정 | 고정 α 대신 기대 세트 크기 최소화, 80%+ 커버리지 보장 | 베이지안 사후 예측밀도 → 비준수성 점수 → Bayesian Quadrature → λ 최적화 | 고위험 분야에서 신뢰할 수 있는 불확실성 정량화 제공 |

> **NLP 영역**은 대형 언어 모델의 효율성, 코드 생성, 그리고 불확실성 정량화에 중점을 두고 있다.

---

## 🔗 교차‑도메인 방향  
| 논문 | 핵심 아이디어 | 주요 기여 | 방법 개요 | 실용적 의미 |
|------|--------------|-----------|-----------|-------------|
| **Conformal Reachability for Safe Control in Unknown Environments** | 컨포멀 예측으로 불확실성 구간 생성 → 도달성 분석에 통합 | 모델이 알려지지 않은 연속 동역학에서도 확률적 안전 보장 | 1) 컨포멀 예측 2) 유한 시점 도달성 분석 3) 정책 학습과 도달성 검증 결합 | 7개 벤치마크에서 최고 수준의 안전성·보상 동시에 달성 |
| **Adaptive Batch Sizes Using Non‑Euclidean Gradient Noise Scales for Stochastic Sign and Spectral Descent** | 비유클리드 GNS를 활용해 배치 크기 동적 조정 | 160M Llama 모델에서 66% 학습 단계 감소 | 비유클리드 GNS 식 도출 → 분산 환경에서 GNS 추정 → 배치 크기 실시간 조정 | 하드웨어 활용도 극대화, 대규모 모델 학습 시간 단축 |
| **SymPlex: A Structure‑Aware Transformer for Symbolic PDE Solving** | 트리‑기반 트랜스포머와 강화학습으로 기호적 PDE 해 탐색 | 데이터 없이 정확하고 해석 가능한 기호식 PDE 솔루션 생성 | 트리 구조 반영 어텐션 + 문법 제약 + 강화학습 보상 | 수치 해석·PINN 대신 기호식 해 제공, 물리·공학 문제에 대한 해석력 향상 |

> **교차‑도메인**은 안전성, 최적화, 기호적 해석 등 다양한 분야를 연결하며, 데이터 기반 불확실성 추정과 검증이 핵심 동력이다.

---

## 📌 핵심 Take‑away  
- **컨포멀 예측**과 **도달성 분석**의 결합은 안전성 보장에 새로운 표준을 제시한다.  
- **메모리‑기반 스케일링**은 모바일·엣지에서 LLM 배포를 현실화한다.  
- **비유클리드 최적화**와 **배치 크기 적응**은 대규모 모델 학습의 효율성을 크게 끌어올린다.  
- **반사실적 생성**과 **기호적 해석**은 실무 시뮬레이션과 과학 계산에서 새로운 가능성을 열어준다.  

> **향후 연구**는 안전성, 효율성, 그리고 해석 가능성을 동시에 만족시키는 **통합 프레임워크** 개발에 초점을 맞출 것으로 예상된다.

## 개별 논문 요약

### Conformal Reachability for Safe Control in Unknown Environments
- Score: 8.7
- Reason: The paper presents a novel combination of conformal prediction with reachability analysis to provide probabilistic safety guarantees for unknown dynamical systems, a significant algorithmic contribution. The technical depth is evident in the rigorous derivation of uncertainty bounds and the design of a policy training framework that balances reward and safety horizon. Its long‑term impact is promising, as it tackles a fundamental limitation in safe autonomy and offers a scalable approach for complex, uncertain environments.
- Main Idea: 알 수 없는(혹은 확률적) 동역학을 가진 시스템에서 안전한 제어를 보장하기 위해, 컨포멀 예측을 이용해 데이터 기반 불확실성 구간을 만들고, 이를 도달성 분석에 통합해 안전성 검증과 정책 학습을 동시에 수행하는 프레임워크를 제안한다.
- Key Contribution: 컨포멀 예측과 도달성 분석의 최초 통합으로, 모델이 알려지지 않은 연속 동역학에서도 확률적 안전 보장을 제공하며, 고차원 비선형 제어 문제에 확장 가능한 방법을 제시한다.
- Method Overview: 1) 컨포멀 예측으로 다음 상태 예측에 대한 유효한 불확실성 구간을 생성한다. 2) 이 구간을 사용해 유한 시점 도달성 분석을 수행해 모든 동역학 실현에서 안전 제약이 만족되는지 확인한다. 3) 정책 학습 알고리즘이 기대 보상을 최적화하면서, 도달성 검증이 보장되는 최대 계획 수평을 명시적으로 최대화한다.
- Why It Matters: 전통적 안전 강화학습은 모델 가정이나 유한 상태공간에 의존해 확률적 안전 보장이 어려웠다. 본 연구는 데이터 기반 불확실성 추정과 도달성 검증을 결합해, 실제 시스템에 적용 가능한 확률적 안전 보장을 제공하며, 실험에서 7개 벤치마크에서 최고 수준의 안전성과 높은 보상을 동시에 달성했다.

### DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books
- Score: 8.7
- Reason: DiffLOB introduces a novel regime-conditioned diffusion framework that enables controllable counterfactual generation in limit order books, a significant algorithmic advance. The paper demonstrates substantial technical depth through rigorous conditioning mechanisms and a comprehensive evaluation framework, while the approach offers promising long-term impact for stress testing, scenario analysis, and decision-making in financial markets.
- Main Idea: 미래 시장 레지먼(추세, 변동성, 유동성, 주문흐름 불균형)을 조건으로 한 확산 모델을 사용해 전체 한계 주문서(LOB) 트레저리의 반사실적 경로를 생성한다.
- Key Contribution: 1) 원하는 미래 레지먼을 지정해 현실적인 LOB 시나리오를 생성할 수 있는 최초의 제어 가능한 반사실적 생성 프레임워크. 2) 컨트롤러블 리얼리즘, 반사실적 유효성, 반사실적 활용성의 세 가지 평가 지표를 제시해 모델 성능을 체계적으로 측정. 3) 시뮬레이션·스트레스 테스트·전략 개발에 직접 활용 가능한 실용적 도구 제공.
- Method Overview: Wavenet‑스타일 잔차 블록과 FiLM 모듈을 결합한 확산 모델을 설계하고, 과거 LOB, 시각 정보, 4가지 미래 레지먼 변수를 조건으로 하여 노이즈를 제거한다. ControlNet‑유사 모듈을 통해 레지먼 변수를 1×1 컨볼루션으로 주입해 모델을 안정적으로 제어한다.
- Why It Matters: 반사실적 LOB 생성을 통해 ‘무엇이 일어날까’ 시나리오를 실험하고, 위험 관리·전략 검증에 필요한 가상 시장 데이터를 제공함으로써 기존의 수동 시뮬레이션을 넘어선 상황 기반 분석을 가능하게 한다.

### MeKi: Memory-based Expert Knowledge Injection for Efficient LLM Scaling
- Score: 8.7
- Reason: MeKi introduces a novel memory‑based scaling paradigm that decouples model capacity from FLOPs, leveraging token‑level memory experts and re‑parameterization to enable efficient on‑device LLMs. The concept is technically deep, requiring careful design of memory experts and parameter folding, and it has strong long‑term impact for edge AI deployments.
- Main Idea: MeKi는 토큰 수준 메모리 전문가를 각 Transformer 층에 도입해, 파라미터 대신 ROM 기반 정적 lookup 테이블에 지식을 저장함으로써 모델 용량을 확장하고 추론 비용을 유지하는 메모리‑기반 스케일링 패러다임을 제안한다.
- Key Contribution: 메모리 기반 스케일링을 통해 4B 대형 모델과 유사한 성능을 1.7B 베이스라인과 동일한 추론 속도로 달성하고, 모바일 엣지 디바이스에서 RAM·NPU 제약을 극복하는 실용적 아키텍처를 제공한다.
- Method Overview: 각 층에 토큰‑레벨 메모리 전문가를 추가하고, 학습 시 복잡한 파라미터 행렬을 재파라미터화해 추론 시에는 정적 lookup 테이블과 최소한의 가중치만 남도록 한다. 메모리에서 가져온 지식 벡터는 hidden state에 가감식으로 주입된다.
- Why It Matters: 컴퓨팅이 아닌 저장소를 활용해 모델 용량을 늘리면, 모바일 SoC의 메모리 대역폭이 낭비되는 상황을 방지하고, 추론 지연과 전력 소비를 크게 줄여 실제 디바이스에 배포 가능한 LLM을 가능하게 한다.

### Bayesian Conformal Prediction as a Decision Risk Problem
- Score: 8.7
- Reason: Introduces a principled Bayesian formulation of conformal prediction that integrates posterior predictive densities with Bayesian quadrature to directly minimize expected set size, offering both theoretical coverage guarantees and practical robustness to misspecification. The method is mathematically rigorous, extending conformal inference into a Bayesian decision‑risk framework, and demonstrates significant variance reduction in set size, indicating strong technical depth. Its generality across regression, classification, and distribution‑shift scenarios suggests potential for broad, long‑term impact on uncertainty quantification in machine learning.
- Main Idea: 베이지안 모델의 사후 예측밀도를 비준수성 점수로 사용하고, 분포-자유의 split‑conformal 예측에서 위험-최소화 기준으로 임계값을 결정하는 Bayesian Conformal Prediction(BCP) 프레임워크를 제안한다.
- Key Contribution: 임계값을 고정된 α가 아닌 기대 세트 크기를 최소화하는 의사결정‑위험 최적화 문제로 정의함으로써, 기존의 ad‑hoc 임계값보다 더 작고 안정적인 예측 세트를 제공하고, 모델이 잘못 지정되었을 때도 80% 이상의 실험적 커버리지를 달성한다.
- Method Overview: 1) 데이터셋을 학습·보정·테스트 세트로 분할하고, 2) 베이지안 사후 예측밀도를 이용해 후보 라벨마다 비준수성 점수 s(x,y)=−log p_b(y|x)를 계산한다. 3) Bayesian Quadrature를 사용해 입력 분포에 대한 기대 세트 크기 E[|C(x;λ)|]를 추정하고, 4) 커버리지 제약 Pr{Y∈C(x;λ)}≥1−α를 만족하면서 E[|C(x;λ)|]를 최소화하는 λ를 최적화한다.
- Why It Matters: BCP는 베이지안 모델이 불완전해도 분포-자유의 유효성을 유지하면서 예측 세트의 효율성을 크게 향상시켜, 고위험 분야에서 신뢰할 수 있는 불확실성 정량화와 낮은 실행 변동성을 제공한다.

### Adaptive Batch Sizes Using Non-Euclidean Gradient Noise Scales for Stochastic Sign and Spectral Descent
- Score: 8.7
- Reason: Introduces a principled, geometry-aware gradient noise scale for non-Euclidean optimizers, deriving new adaptive batch size rules and efficient variance estimation. The theoretical derivation and distributed implementation demonstrate substantial technical depth, and the approach promises broad impact on training large-scale models with sign-based and spectral descent methods.
- Main Idea: 비유클리드 최적화(예: signSGD, specSGD)에서 그라디언트 노이즈 스케일(GNS)을 활용해 배치 크기를 동적으로 조정하는 프레임워크를 제안한다.
- Key Contribution: 비유클리드 GNS를 이론적으로 도출하고, 분산 환경에서 가벼운 변동성 추정 방법을 제공하며, 이를 기반으로 한 적응형 배치 크기 전략을 최초로 제시해 160M 파라미터 Llama 모델에서 최대 66%까지 학습 단계 감소를 달성했다.
- Method Overview: 1) signSGD와 specSGD에 맞는 비유클리드 GNS 식을 도출한다. 2) 분산 데이터 병렬에서 서로 다른 랭크의 미니배치 그라디언트를 활용해 GNS를 효율적으로 추정한다. 3) 추정된 GNS를 목표 노이즈 수준에 맞춰 배치 크기를 실시간으로 조정한다.
- Why It Matters: 비유클리드 최적화와 배치 크기 조정 간의 기하학적 불일치를 해결함으로써 하드웨어 활용도를 극대화하고, 샘플 효율성을 유지하면서 대규모 모델 학습 시간을 크게 단축할 수 있다. 기존의 경험적 배치 스케줄링보다 이론 기반으로 튜닝이 필요 없으며, 기존 분산 훈련 파이프라인에 손쉽게 통합될 수 있다.

### SymPlex: A Structure-Aware Transformer for Symbolic PDE Solving
- Score: 8.5
- Reason: SymPlex introduces a novel tree‑structured RL framework with a structure‑aware transformer and grammar‑constrained decoding for symbolic PDE solving, demonstrating deep technical innovation and promising long‑term impact on interpretable analytic solutions.
- Main Idea: SymPlex는 강화학습과 구조화된 트리 기반 트랜스포머를 활용해 PDE의 정확한 기호적 해를 자동으로 탐색하는 프레임워크이다.
- Key Contribution: 트리‑상대 자기주의를 갖는 SymFormer와 문법 제약을 통한 자동 회귀 디코딩을 결합해, 데이터 없이도 정확하고 해석 가능한 기호식 PDE 솔루션을 최초로 생성한다.
- Method Overview: 표현식 트리를 순차적으로 구축하는 결정 과정으로 모델링하고, SymFormer가 트리 구조를 반영한 어텐션과 문법 제약을 적용해 유효한 기호식을 생성한다. 생성된 후보는 PDE 잔차와 경계 조건을 만족하는 정도에 따라 보상을 받아 강화학습으로 최적화된다.
- Why It Matters: 수치 해석이나 PINN과 달리 기호식 해를 직접 찾아내어 정확성, 메모리 효율성, 파라미터 일반화가 가능하며, 물리·공학 문제에 대한 해석력과 전역적 예측력을 동시에 제공한다.

### Bridging Online and Offline RL: Contextual Bandit Learning for Multi-Turn Code Generation
- Score: 8.5
- Reason: Cobalt introduces a novel contextual bandit framework that blends offline trajectory reuse with online single-step learning, offering a fresh algorithmic perspective for multi-turn code generation. The method demonstrates solid technical depth by reinterpreting the task as a recoverable MDP and addressing reward hacking via perturbed trajectories. Its potential to reduce training cost while maintaining performance positions it as a promising long‑term contribution to RL‑enhanced LLMs.
- Main Idea: 다중 턴 코드 생성 문제를 오프라인 트레저리와 온라인 컨텍스트 밴딧 학습을 결합해 효율적으로 해결하는 하이브리드 RL 프레임워크
- Key Contribution: 오프라인 RL의 샘플 효율성과 온라인 RL의 성능을 동시에 확보하고, 단계별 목표와 이론적 성능 보장을 제공하며, 인컨텍스트 보상 해킹을 완화하는 COBALT 방법을 제시
- Method Overview: 1) 참조 LLM으로 다중 턴 트레저리를 생성하고, 2) 트레저리를 부분 프리픽스로 분할해 컨텍스트로 사용, 3) 온라인 밴딧 학습에서 각 컨텍스트에 대해 단일 단계 코드 완성을 샘플링하고 보상을 평가, 4) 보상 해킹 탐지 시 변형 트레저리로 보강
- Why It Matters: 저비용·안정적인 학습 파이프라인을 제공해 다중 턴 코드 생성 성능을 크게 향상시키고, 학습 붕괴와 그라디언트 폭발 문제를 해결하며, 실무에서 바로 적용 가능한 실용적 솔루션을 제시

### 3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation
- Score: 8.5
- Reason: The paper proposes a novel implicit, view‑agnostic motion token framework that jointly trains a motion encoder with a pretrained video generator, injecting motion via cross‑attention and enforcing 3D awareness through view‑rich supervision and annealed SMPL guidance. This combination is technically deep, involving sophisticated encoding, attention mechanisms, and multi‑view consistency losses. The approach decouples motion control from explicit 3D models, enabling flexible camera control and high‑fidelity motion synthesis, which positions it for significant long‑term impact in 3D‑aware human video generation.
- Main Idea: 3DiMo는 2D 드라이빙 비디오에서 3D 움직임을 암시적으로 학습해, 텍스트 기반 카메라 제어와 함께 임의의 시점에서 고품질 인간 비디오를 생성하는 프레임워크이다.
- Key Contribution: 1) 카메라 시점에 독립적인 3D 움직임 표현 2) 프리트레인된 비디오 디퓨전 모델과의 교차 주의( cross‑attention) 연동 3) 텍스트 기반 카메라 제어 지원 4) 뷰‑리치 학습과 기하학적 보조 손실을 통한 3D 일관성 확보
- Method Overview: 드라이빙 프레임을 임의 시점 변형 후 두 개의 경량 인코더(몸통·손)로 인코딩해 시점 무관한 움직임 토큰을 생성하고, 이 토큰을 DiT 기반 비디오 디퓨전 모델에 cross‑attention으로 주입한다. 재구성, 교차‑시점 재현, 동일 3D 움직임 감독을 결합한 손실로 end‑to‑end 학습한다.
- Why It Matters: 전통적 2D 포즈나 SMPL 기반 방법은 시점 제약과 깊이 모호성으로 인한 움직임 왜곡이 발생하지만, 3DiMo는 이러한 한계를 넘어 실제 3D 동작을 보존하면서 자유로운 카메라 이동을 가능하게 하여 영화, 게임, 가상현실 등에서 실시간 인간 비디오 합성의 새로운 가능성을 열어준다.


# 📅 2026‑03‑09 AI 연구 트렌드 요약 (한국어)

> **주제**: 최신 논문들을 바탕으로 한 일일 AI 연구 트렌드 리포트  
> **형식**: Markdown  
> **구성**  
> 1. 전체 트렌드  
> 2. CV(Computer Vision) 관련 주제  
> 3. NLP(자연어 처리) 관련 주제  
> 4. Cross‑Domain(교차 분야) 방향  

---

## 1. 전체 트렌드

| 트렌드 | 핵심 내용 | 대표 논문 |
|--------|-----------|-----------|
| **Sparse MoE & 비균일 희소성** | 대규모 LLM에서 메모리·서빙 비용을 줄이면서 성능을 유지하기 위해 층별 희소성 비율을 동적으로 조정 | **EvoESAP** |
| **언어별 토크나이저** | 결합어 언어에 특화된 문법‑우선 토크나이저로 토큰 수를 크게 감소 | **VerChol** |
| **Kinetic‑Based Regularization** | 노이즈가 있는 이산 데이터에서 2차 정확도의 공간 미분을 추정 | **Kinetic-based regularization** |
| **Structure‑Aware MoE** | 대규모 WSI를 구조 인식과 선형 SSM으로 효율적으로 처리 | **MoEMambaMIL** |
| **Dynamic Chunking** | Diffusion Transformer에서 토큰 수를 동적으로 조정해 연산량을 절감 | **Dynamic Chunking Diffusion Transformer** |
| **잠재 공간 기반 적대적 공격** | Stable Diffusion VAE 잠재 공간에서 전이성이 높은 공격 생성 | **Latent Transfer Attack** |
| **Hierarchical Preference‑Conditioned Pruning** | VLM에서 사용자 선호를 반영한 구조적 프루닝 | **HiPP‑Prune** |
| **3D Instance‑Aware Referring Expression Segmentation** | 2D 시각적 의미와 3D 기하학을 결합한 멀티모달 분할 | **Hierarchical Collaborative Fusion for 3D Instance‑Aware Referring Expression Segmentation** |

> **핵심 메시지**  
> - **희소성 최적화**와 **구조 인식**이 대규모 모델의 효율성을 좌우한다.  
> - **언어‑특화** 토크나이저와 **잠재 공간** 활용이 NLP와 CV의 경계를 허물고 있다.  
> - **동적 연산**(Dynamic Chunking, Kinetic Regularization)으로 연산 비용을 크게 줄이는 연구가 주류를 이룬다.

---

## 2. CV‑관련 주제

| 주제 | 주요 아이디어 | 대표 논문 | 기대 효과 |
|------|---------------|-----------|-----------|
| **Sparse MoE 기반 프루닝** | 층별 희소성 비율을 비균일하게 최적화 | **EvoESAP** | 50% 희소성에서도 MATH‑500 19.6% 성능 향상 |
| **Structure‑Aware WSI 분석** | Mamba 기반 SSM + 정적·동적 MoE | **MoEMambaMIL** | O(N²) 비용을 선형 시간으로 감소, 병리학적 진단 정확도 향상 |
| **Dynamic Chunking Diffusion** | 토큰 수를 데이터와 타임스텝에 따라 조정 | **Dynamic Chunking Diffusion Transformer** | FLOP 30%↓, FID/IS 향상 |
| **Kinetic‑Based Regularization** | 로컬 커널 회귀로 2차 미분 추정 | **Kinetic-based regularization** | 물리적 보존 법칙 만족, 노이즈에 강인한 PDE 시뮬레이션 |
| **Hierarchical Collaborative Fusion** | 2D 인스턴스 마스크 + 3D 기하학 융합 | **Hierarchical Collaborative Fusion for 3D Instance‑Aware Referring Expression Segmentation** | 3D 인스턴스‑감지 성능 15%↑ |

> **트렌드 포인트**  
> - **MoE**와 **SSM**을 결합해 대규모 이미지 시퀀스를 선형 시간에 처리하는 연구가 증가.  
> - **동적 토큰화**와 **Kinetic Regularization**이 이미지 처리의 효율성과 안정성을 동시에 달성.

---

## 3. NLP‑관련 주제

| 주제 | 주요 아이디어 | 대표 논문 | 기대 효과 |
|------|---------------|-----------|-----------|
| **언어‑특화 토크나이저** | 문법‑우선(rule‑based) 토크나이저 | **VerChol** | 토큰 수 35–47%↓, 학습·추론 비용 절감 |
| **잠재 공간 기반 적대적 공격** | Stable Diffusion VAE 잠재 공간에서 공격 최적화 | **Latent Transfer Attack** | CNN & ViT에서 높은 전이성, 전처리 견고성 |
| **Hierarchical Preference‑Conditioned Pruning** | VLM 프루닝에 사용자 선호 반영 | **HiPP‑Prune** | 다목적 최적화(정확도, 압축, 견고성) |
| **멀티모달 융합** | 2D 시각적 의미 + 3D 기하학 + 언어 가이드 | **Hierarchical Collaborative Fusion for 3D Instance‑Aware Referring Expression Segmentation** | 3D 인스턴스‑감지 성능 향상 |

> **핵심 포인트**  
> - **언어‑특화 토크나이저**가 비결합어 언어에서도 성능을 크게 끌어올림.  
> - **잠재 공간**을 활용한 적대적 공격이 기존 픽셀‑공간 공격보다 견고함을 입증.  
> - **멀티모달 융합**이 NLP와 CV의 경계를 허물고 있다.

---

## 4. Cross‑Domain 방향

| 방향 | 핵심 아이디어 | 대표 논문 | 기대 효과 |
|------|---------------|-----------|-----------|
| **MoE + SSM 융합** | MoE와 Mamba 기반 SSM을 결합해 대규모 시퀀스 처리 | **MoEMambaMIL** | WSI, 비디오 등 긴 시퀀스에서 O(N²) 비용을 선형으로 감소 |
| **동적 토큰화 + Diffusion** | Diffusion Transformer에서 토큰 수를 동적으로 조정 | **Dynamic Chunking Diffusion Transformer** | 이미지 생성에서 연산량 30%↓, FID/IS 향상 |
| **잠재 공간 기반 공격 + VLM** | VLM 프루닝과 잠재 공간 공격을 결합 | **HiPP‑Prune** + **Latent Transfer Attack** | VLM의 견고성 강화와 동시에 압축률 향상 |
| **언어‑특화 토크나이저 + 3D 융합** | 결합어 언어 토크나이저를 3D 인스턴스‑감지에 적용 | **VerChol** + **Hierarchical Collaborative Fusion** | 다국어 3D 인스턴스 분할 성능 향상 |

> **전망**  
> - **MoE**와 **SSM**의 결합은 대규모 시퀀스 처리의 새로운 패러다임을 제시.  
> - **동적 토큰화**는 생성 모델뿐 아니라 비디오, 3D 데이터에서도 적용 가능.  
> - **잠재 공간**과 **언어‑특화 토크나이저**를 결합하면, 멀티모달 모델의 효율성과 견고성을 동시에 달성할 수 있다.

---

## 📌 마무리

- **희소성 최적화**와 **구조 인식**이 CV와 NLP 모두에서 핵심 기술로 부상.  
- **동적 연산**(Dynamic Chunking, Kinetic Regularization)과 **잠재 공간 활용**이 효율성과 견고성을 동시에 제공.  
- **멀티모달 융합**이 언어와 시각, 3D 공간을 통합하는 연구의 중심이 되고 있다.

> **다음 주 예고**  
> - **Sparse MoE**의 **멀티‑GPU** 최적화  
> - **언어‑특화 토크나이저**의 **다국어 지원 확대**  
> - **잠재 공간 기반 적대적 공격**의 **실시간 감지** 연구

---

## 개별 논문 요약

### EvoESAP: Non-Uniform Expert Pruning for Sparse MoE
- Score: 8.7
- Reason: EvoESAP introduces a novel two-stage pruning framework that decouples within-layer expert ranking from across-layer sparsity allocation, leveraging a speculative-decoding-inspired metric (ESAP) for efficient evaluation. The method demonstrates substantial technical depth through evolutionary optimization and a stable, bounded metric, and its non-uniform allocation strategy has the potential to influence future MoE deployment and sparsity research, indicating strong long-term impact.
- Main Idea: Sparse Mixture‑of‑Experts( SMoE ) 모델의 사후 학습 프루닝에서 각 층별 비균일한 희소성 배분을 최적화하는 EvoESAP 기법을 제안한다.
- Key Contribution: 1) ESAP( Expected Speculative Acceptance Proxy )라는 저렴하면서도 신뢰할 수 있는 프록시 지표를 도입해 프루닝 후보 모델의 성능을 빠르게 평가한다. 2) 전역 희소성 예산 하에서 진화 알고리즘을 활용해 층별 희소성 배분을 비균일하게 최적화한다.
- Method Overview: (1) 각 층에서 ESAP를 사용해 전문가들을 순위화하고(2) 전역 예산을 고정한 채 진화 탐색으로 층별 희소성 비율을 조정한다. 이 과정을 통해 Frequency, EAN, SEER, REAP 등 다양한 프루닝 기준과 결합할 수 있다.
- Why It Matters: 비균일한 희소성 배분이 Open‑ended 생성 성능을 크게 향상시키며(예: 50% 희소성에서 MATH‑500 19.6% 개선) 7B–30B SMoE LLM의 메모리·서빙 비용을 줄이면서도 다중 선택 과제에서 경쟁력 있는 정확도를 유지한다.

### VerChol -- Grammar-First Tokenization for Agglutinative Languages
- Score: 8.7
- Reason: The paper proposes a novel grammar-first tokenization framework tailored to agglutinative languages, addressing a clear limitation of BPE-based methods. The idea is algorithmically innovative and, if well-implemented, could reduce tokenization errors and improve downstream LLM performance. The technical depth appears substantial, as it requires formalizing morphological rules and integrating them into tokenization pipelines. Long-term impact is high, given the growing interest in multilingual LLMs and the need for efficient tokenization in morphologically rich languages.
- Main Idea: VerChol은 어휘형식이 풍부한 결합어 언어를 위해 문법 우선(rule‑based) 토크나이저를 설계한 언어-파라미터식 아키텍처이다. 전체 단어를 사전 조회 → 형태소 분해 → 음운학적 음절 분할 → 문자 단위 후속 단계의 4단계 파이프라인을 통해 토큰을 생성한다.
- Key Contribution: 1) 언어별 형태소 규칙·접사 사전을 입력으로 하는 언어-파라미터식 토크나이저를 제안하고, 2) 통계 기반 BPE와 비교해 토큰 수를 35%~47% 감소시킨다. 3) 타밀어 위키피디아 전체를 평가해 공개 벤치마크를 제공한다.
- Method Overview: ① 전체 단어 사전 조회: 사전에 존재하면 단일 토큰으로 처리. ② 규칙 기반 형태소 분해: 루트·접사 사전과 규칙을 적용해 형태소 단위로 분리. ③ 음운학적 음절 분할: 남은 부분을 언어의 음운 규칙에 따라 CV/CVC 음절로 분할. ④ 문자 수준 후속: 할당되지 않은 문자를 개별 문자 토큰으로 분할. 각 단계는 언어별 모듈(사전, 형태소 규칙, 음운 규칙, 문자 표)만 교체하면 재사용 가능하다.
- Why It Matters: 형태소 기반 토크나이저는 토큰 수를 크게 줄여 모델 학습·추론 비용을 낮추고, 토큰이 언어학적으로 의미 있는 단위이므로 해석 가능성을 높인다. 또한 훈련 데이터가 필요 없고, 새로운 결합어 언어에 빠르게 적용할 수 있어 연구·산업 현장에서 활용도가 높다.

### Kinetic-based regularization: Learning spatial derivatives and PDE applications
- Score: 8.5
- Reason: The paper introduces a novel, provably second‑order accurate derivative‑learning framework that extends kinetic‑based regularization to noisy, irregular data, and demonstrates its integration with conservative PDE solvers. The theoretical analysis, convergence proofs, and high‑dimensional formulation reflect substantial technical depth, while the potential to enable stable shock capture on irregular point clouds suggests significant long‑term impact on scientific machine learning and numerical PDE research.
- Main Idea: 노이즈가 있는 이산 데이터에서 Kinetic‑Based Regularization(KBR)을 활용해 2차 정확도의 공간 미분을 추정하는 새로운 학습 방법을 제안한다.
- Key Contribution: 노이즈에 적응하고, 단일 학습 파라미터만으로 2차 정확도를 보장하는 명시적·암시적 두 미분 추정 스킴을 도입하고, 이를 보존형 PDE 솔버에 적용해 안정적인 충격 포착을 가능케 한다.
- Method Overview: 각 목표 지점에서 작은 이웃을 이용해 로컬 커널 회귀를 수행하고, 회귀 계수를 통해 미분을 직접 추출한다. 명시적 스킴은 폐합식으로, 암시적 스킴은 작은 변형을 통해 선형 시스템을 푼다. 이 과정은 고차원 포인트 클라우드에서도 동일하게 적용된다.
- Why It Matters: 전통적 RBF/GP 기반 미분은 커널 미분 불안정과 대규모 전역 시스템 해결이 필요하지만, 이 방법은 계산량이 적고, 물리적 보존 법칙을 자연스럽게 만족하며, 노이즈에 강인해 실제 PDE 시뮬레이션에서 신뢰성과 효율성을 동시에 달성한다.

### MoEMambaMIL: Structure-Aware Selective State Space Modeling for Whole-Slide Image Analysis
- Score: 8.5
- Reason: Introduces a novel structure-aware state‑space framework that integrates multi‑resolution token sequencing with mixture‑of‑experts routing, offering deep technical innovation and promising long‑term impact on large‑scale histopathology analysis.
- Main Idea: WSI(Whole‑Slide Image)를 구조화된 패치 토큰 시퀀스로 변환해, 다중 해상도와 계층적 구조를 보존하면서 긴 시퀀스를 효율적으로 처리하는 MoEMambaMIL 프레임워크를 제안한다.
- Key Contribution: 1) 공간 계층을 유지하는 region‑nested selective scan을 도입해 구조 인식을 강화하고, 2) 정적·동적 Mixture‑of‑Experts(MoE)를 결합해 해상도별 특화와 지역별 적응형 컨텍스트를 동시에 학습하며, 3) Mamba 기반 SSM으로 선형 시간 복잡도로 대규모 WSI를 처리해 기존 MIL·Transformer 대비 성능과 효율성을 동시에 달성한다.
- Method Overview: (1) 다중 해상도 전처리 및 selective scanning으로 패치를 해상도별 그룹화하고 공간 포함 관계를 보존하는 1‑D 시퀀스 생성, (2) Mamba SSM을 각 해상도 레벨에 적용해 긴 시퀀스를 선형 시간에 처리, (3) 정적 전문가(해상도별)와 동적 전문가(가변 라우팅)를 두 층의 MoE로 구성해 토큰별 특화와 적응형 라우팅 수행, (4) Attention‑based MIL 헤드를 통해 토큰 특징을 집계해 슬라이드 수준 예측 수행.
- Why It Matters: WSI는 기가픽셀 규모와 해상도 다양성 때문에 기존 Transformer의 O(N²) 비용이 비효율적이다. MoEMambaMIL은 구조 인식과 선형 SSM, 동적 MoE를 결합해 계산량을 크게 줄이면서도 해상도와 지역 특성을 동시에 포착해, 병리학적 진단 정확도를 향상시키고 대규모 병원 데이터셋에서도 실시간 적용이 가능하도록 한다.

### Dynamic Chunking Diffusion Transformer
- Score: 8.5
- Reason: The paper introduces a genuinely novel dynamic chunking mechanism that adaptively compresses image tokens during diffusion, demonstrating significant efficiency gains and improved generation quality. The architectural design and end-to-end training showcase solid technical depth, while the approach’s applicability to various modalities suggests promising long-term impact.
- Main Idea: 이미지의 2‑D 토큰 시퀀스를 데이터에 따라 동적으로 압축해 Diffusion Transformer의 연산량을 줄이는 Dynamic Chunking Diffusion Transformer(DC‑DiT) 설계
- Key Contribution: 1) 학습 가능한 토큰 분할(Chunking) 모듈을 도입해 배경과 같은 단조로운 영역은 적은 토큰, 디테일이 풍부한 영역은 많은 토큰을 할당함으로써 효율성을 극대화
2) 타임스텝에 따라 토큰 수를 조절해 노이즈 단계에서는 적은 토큰, 세부 단계에서는 더 많은 토큰을 사용
3) 기존 DiT 체크포인트를 최소한의 추가 학습으로 DC‑DiT로 업사이클 가능
4) 학습 과정에서 토큰 경계가 시각적 세분화와 일치해 의미 있는 영역 인식이 가능
- Method Overview: Encoder‑Router‑Decoder 구조를 사용해 전체 토큰 시퀀스를 먼저 혼합한 뒤, Router가 인접 토큰 간 유사도를 기반으로 경계 토큰을 예측(STE를 통해 이산 결정)
경계 토큰만 남겨 단축된 시퀀스를 DiT 블록에 전달하고, 이후 De‑chunking으로 원래 길이로 복원하며 Residual을 게이트해 세밀 정보를 보존
타임스텝마다 Router가 토큰 수를 동적으로 조정해 노이즈 단계에서는 적은 토큰, 세부 단계에서는 더 많은 토큰을 활용
- Why It Matters: 연산량과 FLOP을 현격히 감소시키면서 FID·Inception Score에서 기존 DiT 대비 우수한 성능을 보임
프리트레인된 DiT를 손쉽게 업사이클할 수 있어 실무 적용이 용이
동적 토큰화가 시각적 세분화를 자연스럽게 학습해 비지도 영역 인식이 가능하며, 비디오·3‑D 등 다른 생성 분야로 확장 가능

### Latent Transfer Attack: Adversarial Examples via Generative Latent Spaces
- Score: 8.5
- Reason: Introduces a novel transfer attack that optimizes in a pretrained generative latent space, combining EOT and latent smoothing for robustness. The method demonstrates significant technical depth in integrating diffusion models with adversarial optimization, and offers a promising direction for future research on structured attack domains and cross-model transferability.
- Main Idea: Stable Diffusion VAE의 잠재 공간에서 적대적 변형을 최적화하여, 이미지 매니폴드에 부합하는 저주파, 공간적으로 일관된 공격을 생성한다.
- Key Contribution: 잠재 공간 기반 공격이 CNN과 Vision Transformer 모두에서 높은 전이성을 보이며, 일반적인 전처리(리사이징, 크롭, 보간)에 견고함을 제공한다.
- Method Overview: 1) 입력 이미지를 VAE 인코더로 잠재 코드로 변환. 2) 잠재 벡터를 EOT(랜덤 크롭·보간·리사이징)와 함께 최적화하여 surrogate 모델의 손실을 최대화. 3) 잠재 변동을 주기적으로 가우시안 스무딩하여 고주파 잡음 억제. 4) 최종 디코딩 시 픽셀 공간에서 부드러운 ℓ∞ 제약을 적용.
- Why It Matters: 생성 모델의 이미지 사전이 잠재 변형을 자연스러운 변형으로 제한함으로써, 기존 픽셀 공간 공격보다 견고하고 전이성이 높은 적대적 예시를 제공하며, 보안 평가와 최신 생성 모델 활용의 새로운 연결고리를 제시한다.

### HiPP-Prune: Hierarchical Preference-Conditioned Structured Pruning for Vision-Language Models
- Score: 8.5
- Reason: Introduces a novel hierarchical, preference‑conditioned pruning framework that jointly optimizes utility, hallucination robustness, and compression via policy‑based planning and visual sensitivity signals, demonstrating significant technical depth and promising long‑term impact on efficient, controllable deployment of vision‑language models.
- Main Idea: HiPP‑Prune는 비전‑언어 모델(VLM)의 구조적 프루닝을 사용자 선호(robustness, utility, compression)를 반영한 조건부 자원 할당 문제로 재정의한다.
- Key Contribution: 첫 번째로, 시각적 근거를 보호하면서 다목적(hallucination robustness, task performance, 압축 비율) 최적화를 수행하는 계층적 선호조건 프루닝 프레임워크를 제안하였다. 또한, 단일 정책으로 Pareto 효율적인 프루닝 계획을 실시간으로 생성할 수 있다.
- Method Overview: 프루닝 정책은 두 단계로 구성된다. 1) 전역 희소성 예산을 결정하고 2) 레이어별 할당 벡터를 출력한다. 정책은 시각-감도 신호(시각 토큰과 언어 hidden state 간의 attention 흐름)를 상태에 포함하고, Group Relative Policy Optimization(GRPO)으로 다목적 보상(작업 성능, POPE 기반 hallucination robustness, 압축 비율, SynFlow 기반 안정성)을 최적화한다.
- Why It Matters: VLM은 시각-언어 융합이 핵심이므로 프루닝 시 시각적 근거를 보호해야 한다. HiPP‑Prune은 이러한 요구를 충족하면서 압축률을 유지하고, 다양한 배포 시나리오에 맞는 견고한 모델을 한 번에 생성할 수 있어 실무 적용 가능성을 크게 높인다.

### Hierarchical Collaborative Fusion for 3D Instance-aware Referring Expression Segmentation
- Score: 8.5
- Reason: The paper introduces a novel hierarchical decomposition of visual semantics and a progressive multi‑level fusion strategy that jointly leverages 2D instance masks, CLIP embeddings, and 3D geometry. The technical depth is solid, combining state‑of‑the‑art vision models (SAM, CLIP) with cross‑modal adaptive weighting and language‑guided refinement. While the immediate impact is on 3D referring expression segmentation, the framework’s modular design and emphasis on preserving fine‑grained boundaries suggest broader applicability to multi‑modal 3D perception tasks, indicating substantial long‑term research value.
- Main Idea: 2D 시각적 의미를 계층적으로 분해하고 3D 기하학과 결합하여 3D 인스턴스‑감지 참조 표현 분할을 수행하는 HCF‑RES 프레임워크를 제안합니다.
- Key Contribution: SAM과 CLIP을 활용한 계층적 시각 의미 분해, 인트라‑모달·크로스‑모달 적응 가중치 및 언어 가이드형 정제 단계가 결합된 최초의 다중 모달 융합 전략을 도입하고, ScanRefer와 Multi3DRefer에서 최첨단 성능을 달성했습니다.
- Method Overview: 1) SAM으로 2D 인스턴스 마스크를 생성하고, 2) CLIP으로 픽셀‑레벨과 인스턴스‑레벨 특징을 추출합니다. 3) 특징을 카메라 변환을 통해 3D 공간에 투영하고, 4) 슈퍼포인트에 집계합니다. 5) 인트라‑모달 통합으로 2D 특징을 결합하고, 6) 크로스‑모달 적응 가중치로 2D 시각과 3D 기하학을 균형 있게 융합하며, 7) 언어 표현을 이용해 최종 마스크를 정제합니다.
- Why It Matters: 점군의 희소성과 텍스처 부족 문제를 해결하고, 객체 경계를 보존하면서 2D 시각적 풍부함을 3D 분할에 효과적으로 반영함으로써, 복잡한 장면에서의 참조 표현 이해와 실시간 3D 인스턴스 분할 성능을 크게 향상시킵니다.


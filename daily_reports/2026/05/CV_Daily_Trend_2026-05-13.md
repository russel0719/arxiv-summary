# CV 연구 동향 보고서 — 2026-05-13

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| Generative AI | 고차원 데이터 생성의 효율성 및 실시간 추론 최적화 | Asymmetric Flow Models |
| Video Synthesis | 장기 비디오 일관성 유지 및 카메라 제어의 기하학적 정밀도 향상 | Pyramid Forcing |
| Mechanistic Interpretability | VLM의 환각 현상에 대한 인과적 분석 및 제어 | Dual-Pathway Circuits of Object Hallucination in Vision-Language Models |
| Embodied AI | 데이터 부족 문제 해결을 위한 시뮬레이션-실제 환경 공진화 | RoboEvolve |

> 핵심 메시지: 생성 모델의 효율적 추론 최적화와 기하학적 제어 기술이 결합되어 실용적 도메인(의료, 로봇, AR)으로의 확장이 가속화되고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Generation | 확산 모델의 효율적 가이던스 및 비대칭 파라미터화를 통한 고품질 생성 | Asymmetric Flow Models |
| Video | Any-step 추론 및 장기 비디오 생성을 위한 KV 캐시 최적화 | AnyFlow |
| Robotics | VLM과 비디오 생성 모델을 활용한 로봇 조작 학습 | RoboEvolve |
| Medical Imaging | 베지에 트리 인코딩을 통한 망막 혈관의 반사실적 질병 분석 | A General Bézier Tree Encoding Counterfactual Framework |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Diffusion & Flow Models | 고차원 픽셀 생성 및 실시간 모션 복원 | EgoForce |
| Mechanistic Interpretability | VLM의 환각 경로 식별 및 억제 | Dual-Pathway Circuits of Object Hallucination in Vision-Language Models |
| Amortized Optimization | 추론 시간 최적화 비용을 줄이는 경량 가이드 모듈 학습 | Amortized Guidance for Image Inpainting |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| Medical AI | 기하학적 베지에 인코딩과 확산 모델의 결합 | 질병 예측의 임상적 해석 가능성 및 인과적 추론 강화 |
| Robotics | VLM(계획)과 VGM(시뮬레이션)의 폐쇄형 루프 공진화 | 데이터 효율성 극대화 및 물리적 환각 감소 |
| AR/VR | 인과적 확산 모델을 이용한 일인칭 모션 복원 | 실시간 환경에서의 안정적인 전신 트래킹 |

---

## 5. 개별 논문 요약

### 1. Asymmetric Flow Models

- **arXiv**: https://arxiv.org/abs/2605.12964
- **Score**: 8.8 / 10
- **한줄 요약**: 고차원 노이즈 예측의 복잡성을 줄이기 위해 속도(velocity) 타겟을 데이터 성분과 저차원 노이즈 성분으로 분리하는 비대칭 파라미터화(Asymmetric Parameterization) 기법을 제안합니다.
- **핵심 기여**: 기존 아키텍처 수정 없이도 고차원 픽셀 생성 성능을 극대화하여 ImageNet 256x256에서 1.57 FID라는 SOTA를 달성하고, 사전 학습된 잠재 공간 모델을 픽셀 공간으로 효과적으로 전이하는 프레임워크를 구축했습니다.
- **방법론 개요**: 데이터 성분은 전체 차원으로 유지하되, 노이즈 성분만을 학습 가능한 저차원 부분 공간(low-rank subspace)으로 제한하여 속도 필드를 해석적으로 재구성하는 방식을 사용합니다.
- **의의**: 고차원 데이터 생성 시 발생하는 연산 병목 현상을 해결하고, 대규모 잠재 모델을 픽셀 공간으로 확장함으로써 생성 모델의 효율성과 시각적 품질을 동시에 개선할 수 있는 범용적인 최적화 전략을 제시합니다.

### 2. AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation

- **arXiv**: https://arxiv.org/abs/2605.13724
- **Score**: 8.5 / 10
- **한줄 요약**: AnyFlow는 고정된 단계로만 생성하던 기존 일관성 증류(Consistency Distillation)의 한계를 극복하고, 추론 단계(NFE) 증가에 따라 성능이 비례해서 향상되는 'Any-step' 비디오 확산 모델 학습 프레임워크입니다.
- **핵심 기여**: 기존의 종단점(endpoint) 일관성 학습 대신 '플로우 맵(Flow-map) 전이 학습'을 도입하여, 대규모 모델(14B)에서도 FSDP와 호환되는 확장성을 확보하고 추론 단계에 따른 성능 스케일링을 가능하게 했습니다.
- **방법론 개요**: 전체 궤적을 '숏컷(shortcut)' 단위로 분해하는 플로우 맵 역방향 시뮬레이션과 온-폴리시(on-policy) 증류를 결합하여, 이산화 오차와 노출 편향을 최소화하는 2단계 학습 파이프라인을 사용합니다.
- **의의**: 기존 모델들이 적은 단계에서만 성능이 좋고 단계가 늘어나면 오히려 성능이 저하되던 문제를 해결하여, 효율성과 고품질 생성을 동시에 달성하고 비디오 생성 모델의 실용적 배포 가능성을 크게 높였습니다.

### 3. Dual-Pathway Circuits of Object Hallucination in Vision-Language Models

- **arXiv**: https://arxiv.org/abs/2605.13156
- **Score**: 8.2 / 10
- **한줄 요약**: Vision-Language Models (VLMs) exhibit object hallucinations due to a consistent, architecture-agnostic dual-pathway circuit, comprising a visual grounding pathway and a hallucination pathway, which undergoes a 'polarity flip' during erroneous generation.
- **핵심 기여**: The study provides the first mechanistic insight into VLM object hallucinations, identifying a universal 'polarity flip' hypothesis and demonstrating high-efficiency mitigation (up to 76% reduction) by suppressing the hallucination pathway, with selective transferability to relational hallucinations.
- **방법론 개요**: The research employs a mechanistic interpretability framework, including activation patching and causal probing, to isolate and analyze functional pathways within VLMs. A novel Conditional Pathway Analysis (CPA) is introduced to study the dynamic interaction between pathways, revealing the 'polarity flip' phenomenon, and targeted suppression is used for causal validation and mitigation.
- **의의**: This work moves beyond quantifying hallucinations to understanding their underlying causal mechanisms, offering a new theoretical perspective on VLM failures and enabling targeted, efficient debiasing strategies for improved model reliability and trustworthiness.

### 4. A General Bézier Tree Encoding Counterfactual Framework for Retinal-Vessel-Mediated Disease Analysis

- **arXiv**: https://arxiv.org/abs/2605.13015
- **Score**: 8.2 / 10
- **한줄 요약**: BTECF는 망막 혈관 구조를 3차 베지에 곡선으로 매개변수화하여, 혈관의 기하학적 특성을 독립적으로 제어하고 인과적 추론이 가능한 반사실적(counterfactual) 망막 영상을 생성하는 프레임워크입니다.
- **핵심 기여**: 픽셀 단위의 조작이 아닌 해부학적으로 해석 가능한 기하학적 매개변수(굴곡도, 반지름 등)를 직접 제어함으로써, 망막 혈관 구조 변화가 질병 예측에 미치는 인과적 영향을 정량적으로 분석할 수 있는 기반을 마련했습니다.
- **방법론 개요**: 망막 혈관을 베지에 트리로 인코딩하여 구조적 특징을 추출하고, 이를 VesselControlNet과 LoRA가 적용된 확산 모델(Diffusion Model)의 조건부 입력으로 사용하여 특정 혈관 특성만 변형된 고품질의 반사실적 영상을 생성합니다.
- **의의**: 기존의 '블랙박스'식 딥러닝 진단 모델을 넘어, 특정 혈관 구조 변화가 당뇨망막병증, 뇌졸중, 알츠하이머 등 전신 질환의 위험도에 어떻게 기여하는지 임상적으로 해석 가능한 근거를 제공합니다.

### 5. RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data

- **arXiv**: https://arxiv.org/abs/2605.13775
- **Score**: 7.8 / 10
- **한줄 요약**: RoboEvolve은 VLM(비전-언어 모델) 기반의 계획자와 VGM(비디오 생성 모델) 기반의 시뮬레이터 간의 상호 보완적인 공진화(co-evolution) 루프를 통해 로봇 조작 학습의 데이터 부족 문제를 해결하는 프레임워크입니다.
- **핵심 기여**: 500개의 비라벨링 이미지 데이터만으로 기존 지도 학습 대비 50배 높은 데이터 효율성을 달성했으며, 실패 사례를 학습 신호로 활용하여 물리적 환각을 줄이고 로봇의 조작 성능을 획기적으로 개선했습니다.
- **방법론 개요**: VLM이 고수준의 의미론적 계획을 수립하고, VGM이 이를 물리적으로 검증하는 폐쇄형 루프를 구축합니다. 특히 '낮 시간'의 탐색과 '밤 시간'의 실패 사례 분석을 결합한 인지 기반 학습 메커니즘을 통해 정책을 점진적으로 최적화합니다.
- **의의**: 고비용의 수동 데이터 수집 없이도 복잡한 물리적 조작 능력을 스스로 학습할 수 있게 함으로써, 로봇 학습의 데이터 병목 현상을 해결하고 범용 로봇 제어의 확장성을 크게 높였습니다.

### 6. Min Generalized Sliced Gromov Wasserstein: A Scalable Path to Gromov Wasserstein

- **arXiv**: https://arxiv.org/abs/2605.13753
- **Score**: 7.8 / 10
- **한줄 요약**: 기존 Sliced Gromov-Wasserstein(SGW)의 선형 투영 및 단조 매칭 한계를 극복하기 위해, 학습 가능한 비선형 슬라이서와 측정값 리프팅(lifting)을 활용한 새로운 최적 운송 계획(transport plan) 프레임워크를 제안함.
- **핵심 기여**: 비선형 슬라이싱을 통한 표현력 강화, 차원이 다른 공간 간의 정렬을 가능하게 하는 리프팅 메커니즘 도입, 그리고 반복적인 최적화 없이도 고품질의 운송 계획을 생성하는 효율적인 아모타이즈드(amortized) 추론 체계 구축.
- **방법론 개요**: 학습 가능한 비선형 함수를 통해 입력 측도(measure)를 1차원 공간으로 투영하고, 리프팅 함수를 통해 차원 불일치를 해결하며, 비선형 재배열과 단조 결합을 결합하여 최적 운송 계획을 직접 구성하고 최적화함.
- **의의**: 기존 GW 솔버의 높은 계산 복잡도와 SGW의 구조적 근사 오류를 동시에 해결함으로써, 복잡한 기하학적 데이터 매칭 및 도메인 적응 문제에서 계산 효율성과 정밀도를 획기적으로 개선함.

### 7. Pyramid Forcing: Head-Aware Pyramid KV Cache Policy for High-Quality Long Video Generation

- **arXiv**: https://arxiv.org/abs/2605.13111
- **Score**: 7.8 / 10
- **한줄 요약**: 자기회귀 비디오 생성 모델에서 어텐션 헤드의 기능적 이질성을 활용하여, 헤드별 특성에 맞춘 차등적 KV 캐시 관리 전략인 'Pyramid Forcing'을 제안함.
- **핵심 기여**: 어텐션 헤드를 Anchor, Wave, Veil 세 가지 유형으로 분류하고, 이를 통해 기존의 획일적인 캐시 압축 방식을 탈피하여 장기 비디오 생성 시 발생하는 시각적 왜곡과 일관성 문제를 효과적으로 해결함.
- **방법론 개요**: 오프라인 분석을 통해 헤드 유형을 식별한 뒤, 유형별로 최적화된 캐시 정책(슬라이딩 윈도우, 주기적 샘플링, 캐시 병합)을 적용하고, 이를 효율적으로 처리하기 위해 커스텀 커널 기반의 가변 길이(ragged) 텐서 구조를 도입함.
- **의의**: 비디오 생성 모델의 메모리 효율성을 극대화하면서도 장시간 생성 시의 품질 저하를 방지하여, 고품질의 긴 비디오를 생성할 수 있는 실질적인 기술적 토대를 마련함.

### 8. EgoForce: Robust Online Egocentric Motion Reconstruction via Diffusion Forcing

- **arXiv**: https://arxiv.org/abs/2605.13041
- **Score**: 7.8 / 10
- **한줄 요약**: EgoForce는 희소하고 노이즈가 많은 일인칭 시점(egocentric) 데이터를 사용하여 실시간으로 전신 동작을 복원하는 인과적 확산 모델 기반 프레임워크입니다.
- **핵심 기여**: 오프라인 확산 모델을 실시간 스트리밍 환경에 맞게 최적화하여, 미래 정보 없이도 과거 데이터만으로 안정적이고 일관된 전신 동작을 생성하는 인과적 추론 방식을 제안했습니다.
- **방법론 개요**: 시간적 비대칭 노이즈 스케줄과 확산 포싱(Diffusion Forcing)을 통해 현재 관측치와 과거 동작 이력을 결합하여 미래 동작을 점진적으로 정제하는 인과적 생성 방식을 사용합니다.
- **의의**: 기존 방식의 고질적인 문제인 실시간성 부족과 누적 오차로 인한 드리프트 현상을 해결하여, AR/VR 등 실제 환경에서 끊김 없고 정확한 전신 모션 트래킹을 가능하게 합니다.

### 9. Amortized Guidance for Image Inpainting with Pretrained Diffusion Models

- **arXiv**: https://arxiv.org/abs/2605.13010
- **Score**: 7.8 / 10
- **한줄 요약**: AID(Amortized Inpainting Diffusion)은 사전 학습된 확산 모델을 고정한 채, 별도의 최적화 과정 없이 고품질 인페인팅을 수행할 수 있는 경량 가이드 모듈을 학습시키는 프레임워크입니다.
- **핵심 기여**: 확산 모델의 결정론적 가이던스를 연속 시간 최적 제어 문제로 정립하고, 이를 강화학습의 액터-크리틱 구조로 해결할 수 있음을 이론적으로 증명하여 효율성과 성능을 동시에 확보했습니다.
- **방법론 개요**: 사전 학습된 확산 모델을 유지하면서, 마스킹된 입력에 대해 최적의 가이던스를 제공하는 경량 모듈을 학습시킵니다. 이때 가우시안 정책 기반의 보조 제어 문제를 도입하여 결정론적 가이던스 필드를 효과적으로 학습하는 최적화 알고리즘을 사용합니다.
- **의의**: 기존의 반복적인 추론 시간 최적화(test-time optimization)가 가진 높은 계산 비용 문제를 해결하면서도, 1% 미만의 추가 파라미터만으로 최첨단 성능을 달성하여 실시간 인페인팅 응용의 가능성을 크게 확장했습니다.

### 10. CRePE: Curved Ray Expectation Positional Encoding for Unified-Camera-Controlled Video Generation

- **arXiv**: https://arxiv.org/abs/2605.12938
- **Score**: 7.8 / 10
- **한줄 요약**: CRePE는 비핀홀(non-pinhole) 카메라 모델에서도 일관된 비디오 생성을 가능하게 하기 위해, 토큰의 위치를 고정된 점이 아닌 광선 위의 확률적 깊이 분포로 모델링하는 기하학적 위치 인코딩 프레임워크입니다.
- **핵심 기여**: 기존의 핀홀 카메라 제약에서 벗어나 광각 및 어안 렌즈와 같은 다양한 렌즈 기하학을 지원하며, 3D 기하학적 사전 정보를 사전 학습된 비디오 확산 모델에 효과적으로 통합하는 미분 가능한 메커니즘을 제안했습니다.
- **방법론 개요**: 토큰별 방사형 거리 분포를 예측하고, 이를 통합 카메라 모델(UCM)을 통해 3D 공간으로 투영한 뒤, 곡선 경로상의 기댓값을 분석적으로 계산하여 로터리 위치 임베딩(RoPE)에 반영하는 기하학적 어텐션 어댑터를 사용합니다.
- **의의**: 카메라 제어 비디오 생성에서 렌즈 왜곡 문제를 해결하고, 명시적인 3D 구조 정보 없이도 복잡한 카메라 움직임과 다양한 광학 환경에서 공간적 일관성이 높은 고품질 비디오 합성을 가능하게 합니다.

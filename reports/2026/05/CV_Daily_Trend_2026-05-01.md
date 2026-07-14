# CV 연구 동향 보고서 — 2026-05-01

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| Generative AI | 물리적 인과관계 및 구조적 일관성 확보 | Scale-Aware Adversarial Analysis: A Diagnostic for Generative AI in Multiscale Complex Systems |
| 3D Vision | 포즈 정렬 및 대규모 환경 생성의 효율성 | Pose-Aware Diffusion for 3D Generation |
| Multimodal Learning | 장문 맥락에서의 시각 정보 유지 및 범용성 | Persistent Visual Memory: Sustaining Perception for Deep Generation in LVLMs |

> 핵심 메시지: 생성형 AI의 물리적 인과관계 내재화와 3D/비디오 생성의 구조적 일관성 및 효율성 극대화가 최신 CV 연구의 핵심 동력으로 부상하고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Image Generation | 단일 단계 통합 학습을 통한 토크나이저 및 생성 모델 최적화 | End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer |
| 3D Generation | 초기 노이즈 최적화 및 세그먼트 맵 기반 대규모 환경 합성 | InpaintSLat: Inpainting Structured 3D Latents via Initial Noise Optimization |
| Video Generation | 통합 멀티모달 프레임워크를 통한 데이터 효율성 및 일관성 확보 | UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Diffusion & Latent Optimization | 3D 인페인팅 및 극단적 이미지 리스케일링 | InpaintSLat: Inpainting Structured 3D Latents via Initial Noise Optimization |
| Token Pruning & Compression | OCR 모델의 추론 속도 향상 및 시각 정보 압축 | RTPrune: Reading-Twice Inspired Token Pruning for Efficient DeepSeek-OCR Inference |
| Federated Learning | 의료 영상 분석을 위한 데이터 이질성 극복 | Federated Distillation for Whole Slide Image via Gaussian-Mixture Feature Alignment and Curriculum Integration |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| Medical Imaging (Pathology) | 연합 학습을 통한 프라이버시 보호 및 이기종 모델 간 지식 공유 | 기관 간 데이터 공유 없이 고성능 병리 진단 모델 구축 |
| Physics & Fluid Dynamics | 물리적 법칙을 따르는 다중 스케일 데이터 분해 및 진단 | 생성 모델의 물리적 인과관계 검증 및 일반화 성능 향상 |

---

## 5. 개별 논문 요약

### 1. End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer

- **arXiv**: https://arxiv.org/abs/2605.00503
- **Score**: 8.2 / 10
- **한줄 요약**: 기존의 2단계(tokenizer 학습 후 고정) 방식에서 벗어나, 이미지 토크나이저와 자기회귀(AR) 생성 모델을 단일 단계로 통합 학습하는 EOSTok 프레임워크 제안.
- **핵심 기여**: APR(Autoregressive-Pixel-Reconstruction) 손실 함수를 통해 토크나이저의 잠재 공간을 생성 작업에 최적화하고, ImageNet 256x256에서 FID 1.48이라는 SOTA 성능을 달성함.
- **방법론 개요**: 2D 공간적 편향을 제거한 1D ViT 토크나이저를 사용하며, Straight-Through Estimator를 통해 AR 생성 손실을 토크나이저로 역전파하여 재구성 품질과 생성 예측력을 동시에 최적화함.
- **의의**: 기존 방식의 잠재 공간 불일치와 토크나이저의 코드북 붕괴 문제를 해결함으로써, 비전 파운데이션 모델을 활용한 고품질 이미지 생성의 확장성과 효율성을 크게 향상시킴.

### 2. Scale-Aware Adversarial Analysis: A Diagnostic for Generative AI in Multiscale Complex Systems

- **arXiv**: https://arxiv.org/abs/2605.00510
- **Score**: 7.8 / 10
- **한줄 요약**: 물리적 법칙을 따르는 다중 스케일 데이터 분해(CDD)를 통해 생성형 AI 모델의 물리적 인과관계와 구조적 연속성을 진단하고 보강하는 프레임워크 제안.
- **핵심 기여**: 기존 XAI의 비물리적 섭동 문제를 해결하고, 생성 모델이 물리 법칙을 내재화했는지 검증하는 물리 기반 진단 도구 및 기하학적 데이터 증강 기법 개발.
- **방법론 개요**: 확산 모델(DDPM) 기반의 CDD를 활용하여 3D 볼륨 데이터를 스케일별로 분해하고, 결정론적 개입(Intervention)을 통해 물리적으로 일관된 섭동을 생성하여 모델의 반응을 분석.
- **의의**: 생성 모델이 단순한 통계적 보간(interpolation)을 넘어 유체 역학 등 복잡한 물리 시스템의 인과적 법칙을 실제로 학습했는지 엄밀하게 평가하고 모델의 일반화 성능을 높일 수 있음.

### 3. Pose-Aware Diffusion for 3D Generation

- **arXiv**: https://arxiv.org/abs/2605.00345
- **Score**: 7.8 / 10
- **한줄 요약**: 기존의 '표준 공간(canonical space) 생성 후 회전' 방식을 탈피하여, 관측 공간(observation space)에서 직접 포즈가 정렬된 3D 에셋을 생성하는 Pose-Aware Diffusion(PAD) 프레임워크 제안.
- **핵심 기여**: 포즈 추정 오류와 공간적 불일치를 근본적으로 해결하고, 단일 이미지로부터 고충실도의 포즈 정렬된 3D 모델을 생성하며, 복합적인 3D 장면 구성으로의 확장성을 확보함.
- **방법론 개요**: 단일 이미지에서 추출한 부분 점군(partial point cloud)을 3D 기하학적 앵커로 활용하여 확산 모델(Diffusion model)에 직접 주입함으로써, 별도의 사후 포즈 최적화 없이 관측 공간 내에서 즉각적인 3D 합성을 수행함.
- **의의**: 기존 방식의 고질적인 문제인 포즈 모호성(pose ambiguity)과 기하학적 불일치를 제거하여 3D 생성의 정확도와 정렬 품질을 획기적으로 개선하고, 복잡한 장면 재구성의 효율성을 높임.

### 4. InpaintSLat: Inpainting Structured 3D Latents via Initial Noise Optimization

- **arXiv**: https://arxiv.org/abs/2605.00664
- **Score**: 6.8 / 10
- **한줄 요약**: 구조화된 3D 잠재 확산 모델(Structured 3D Latent Diffusion Model)에서 초기 노이즈를 최적화하여 훈련 없이 정교한 3D 인페인팅을 수행하는 프레임워크 제안.
- **핵심 기여**: 초기 노이즈 제어를 3D 인페인팅의 독립적인 차원으로 정립하고, Rectified Flow의 선형적 특성을 활용하여 메모리 효율적인 역전파 근사 및 구조적 안정성을 확보함.
- **방법론 개요**: Rectified Flow 모델의 초기 노이즈를 최적화 변수로 설정하고, 역전파 비용을 줄이기 위해 궤적을 선형화(Linearization)하며, 주파수 도메인 파라미터화와 분포 정규화를 통해 기하학적 일관성을 유지함.
- **의의**: 기존 3D 생성 모델의 고질적인 문제인 초기 노이즈에 대한 높은 민감도와 구조적 붕괴 문제를 해결하여, 복잡한 3D 자산의 편집 및 완성도를 획기적으로 개선함.

### 5. UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors

- **arXiv**: https://arxiv.org/abs/2605.00658
- **Score**: 6.8 / 10
- **한줄 요약**: UniVidX는 비디오 생성 및 그래픽스 작업을 개별 모델이 아닌 하나의 통합된 멀티모달 프레임워크로 처리하여, 다양한 입력 조건 간의 일관성을 유지하는 범용 생성 모델을 제안합니다.
- **핵심 기여**: 작업별 전용 모델의 한계를 극복하고, 데이터 효율성(1,000개 미만 비디오)을 확보하면서도 내재적 분해 및 레이어 합성 등 다양한 그래픽스 작업에서 SOTA 성능을 달성했습니다.
- **방법론 개요**: 학습 시 입력을 무작위로 마스킹하는 SCM(Stochastic Condition Masking), 모달리티별로 독립적인 LoRA를 활성화하는 DGL(Decoupled Gated LoRA), 그리고 모달리티 간의 구조적 일관성을 유지하는 CMSA(Cross-Modal Self-Attention)를 핵심 기술로 사용합니다.
- **의의**: 기존의 파편화된 비디오 생성 파이프라인을 통합하여 데이터 효율성을 높이고, 서로 다른 시각적 모달리티 간의 복잡한 상관관계를 효과적으로 학습함으로써 생성형 AI의 범용성과 실용성을 크게 확장했습니다.

### 6. Map2World: Segment Map Conditioned Text to 3D World Generation

- **arXiv**: https://arxiv.org/abs/2605.00781
- **Score**: 6.5 / 10
- **한줄 요약**: Map2World는 사전 학습된 3D 자산 생성 모델(TRELLIS)을 확장하여, 사용자 정의 세그먼트 맵을 기반으로 대규모의 고해상도 3D 환경을 생성하는 계층적 프레임워크입니다.
- **핵심 기여**: 기존의 격자 기반 제한을 극복하고, 잠재 공간 융합(Latent Fusion)과 세부 묘사 강화 네트워크를 통해 대규모 공간에서도 전역적 일관성과 국소적 정밀도를 동시에 달성했습니다.
- **방법론 개요**: 사용자 입력 세그먼트 맵에 따라 3D 영역을 분할하고, 다중 윈도우 확산(Multi-window Diffusion)을 통해 잠재 공간을 결합한 뒤, 세부 묘사 강화 네트워크와 3D 가우시안 스플래팅을 통해 고품질의 3D 월드를 합성합니다.
- **의의**: 데이터 부족 문제를 해결하고 특정 도메인에 국한되지 않는 범용적인 3D 월드 생성 기술을 제시함으로써, 복잡하고 확장 가능한 고충실도 가상 환경 구축의 새로운 가능성을 열었습니다.

### 7. RTPrune: Reading-Twice Inspired Token Pruning for Efficient DeepSeek-OCR Inference

- **arXiv**: https://arxiv.org/abs/2605.00392
- **Score**: 6.5 / 10
- **한줄 요약**: DeepSeek-OCR 모델의 특수한 시각 인코더 구조를 고려하여, 정보 손실을 최소화하면서 시각 토큰을 효율적으로 압축하는 2단계 토큰 가지치기(Pruning) 프레임워크인 RTPrune을 제안함.
- **핵심 기여**: 최적 운송(Optimal Transport) 이론을 시각 토큰 병합에 도입하여 OCR 정확도를 유지하면서도 1.23배의 추론 속도 향상과 15.75%의 토큰 감소를 달성함.
- **방법론 개요**: 1단계에서는 토큰의 L2-norm을 기반으로 핵심 시각 정보를 선별하고, 2단계에서는 최적 운송 이론을 통해 나머지 토큰을 핵심 토큰에 병합하며, 입력 문서의 복잡도에 따라 가지치기 비율을 동적으로 조절함.
- **의의**: 기존의 범용 VLM 가지치기 기법들이 OCR의 고밀도 텍스트 재구성 요구를 충족하지 못하는 한계를 극복하고, 도메인 특화 모델에 최적화된 고성능 압축 솔루션을 제시함.

### 8. Persistent Visual Memory: Sustaining Perception for Deep Generation in LVLMs

- **arXiv**: https://arxiv.org/abs/2605.00814
- **Score**: 6.2 / 10
- **한줄 요약**: 대규모 시각-언어 모델(LVLM)에서 텍스트 시퀀스가 길어질수록 시각 정보에 대한 주의력이 급격히 감소하는 '시각 신호 희석(Visual Signal Dilution)' 현상을 규명하고 이를 해결하기 위한 구조적 접근법을 제시함.
- **핵심 기여**: 시각 주의력 감쇠를 수학적으로 증명한 '시각 신호 희석 정리'를 정립하고, 이를 해결하기 위해 시각 정보를 독립적으로 유지하는 '지속적 시각 메모리(PVM)' 모듈을 제안하여 모델의 장문 추론 성능과 시각적 충실도를 개선함.
- **방법론 개요**: 기존 어텐션 메커니즘의 병목 현상을 우회하기 위해 FFN과 병렬로 작동하는 경량화된 PVM 모듈을 도입함. 이는 거리와 무관하게 시각 임베딩에 직접 접근할 수 있는 게이트 기반의 독립적 경로를 제공하여 텍스트 길이에 따른 신호 간섭을 차단함.
- **의의**: 멀티모달 모델이 긴 문맥에서 시각적 세부 정보를 놓치는 구조적 한계를 극복함으로써, 복잡한 추론이 필요한 장문 멀티모달 작업에서 모델의 신뢰성과 정확도를 획기적으로 향상시킬 수 있는 아키텍처적 돌파구를 마련함.

### 9. Faithful Extreme Image Rescaling with Learnable Reversible Transformation and Semantic Priors

- **arXiv**: https://arxiv.org/abs/2605.00605
- **Score**: 6.2 / 10
- **한줄 요약**: FaithEIR은 16배 이상의 극단적인 이미지 리스케일링(Extreme Image Rescaling) 환경에서 발생하는 정보 손실과 환각 문제를 해결하기 위해, 학습 가능한 가역 변환과 확산 모델 기반의 복원 기법을 결합한 프레임워크입니다.
- **핵심 기여**: SVD 기반의 학습 가능한 가역 변환(LRT)을 도입하여 고정된 커널의 한계를 극복하고, 고주파 상세 정보 복원을 위한 적응형 사전(Adaptive Detail Prior)과 의미론적 조건부 주입을 통해 재구성의 충실도와 시각적 품질을 동시에 확보했습니다.
- **방법론 개요**: SVD 기반의 학습 가능한 가역 변환 모듈로 특징을 분해하고, 고주파 상세 정보를 보존하는 사전(Dictionary)을 활용하며, 사전 학습된 확산 모델에 의미론적 임베딩을 조건으로 주입하여 고해상도 이미지를 복원합니다.
- **의의**: 기존의 픽셀 단위 최적화 방식이 극단적인 축소 시 겪는 '과도한 평활화(Over-smoothing)' 및 정보 손실 문제를 해결함으로써, 생성 모델의 강력한 복원 능력과 구조적 충실도를 결합한 새로운 리스케일링 패러다임을 제시합니다.

### 10. Federated Distillation for Whole Slide Image via Gaussian-Mixture Feature Alignment and Curriculum Integration

- **arXiv**: https://arxiv.org/abs/2605.00578
- **Score**: 6.2 / 10
- **한줄 요약**: 병리 조직 슬라이드(WSI) 분석을 위한 아키텍처 독립적 연합 학습 프레임워크로, 모델 파라미터 대신 가우시안 혼합 모델 기반의 합성 특징을 공유하여 데이터 이질성을 극복함.
- **핵심 기여**: 기존 데이터 증류 방식의 과도한 압축 및 정보 손실 문제를 해결하고, 이기종 MIL 모델 간의 지식 공유를 가능하게 하여 임상적 진단 정확도와 프라이버시 보호를 동시에 달성함.
- **방법론 개요**: WSI의 복잡한 형태학적 분포를 가우시안 혼합 모델로 정렬하여 슬라이드별 특징을 증류하고, 로컬 학습 안정화를 위해 커리큘럼 기반의 합성 데이터 통합 전략을 적용함.
- **의의**: 의료 기관마다 상이한 컴퓨팅 환경과 모델 아키텍처를 가진 상황에서도 고품질의 병리 진단 모델을 협력적으로 구축할 수 있는 실용적이고 확장 가능한 해결책을 제시함.

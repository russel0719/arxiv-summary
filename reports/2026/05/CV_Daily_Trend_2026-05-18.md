# CV 연구 동향 보고서 — 2026-05-18

## 1. 전체 트렌드

| 분야 | 핵심 이슈 | 대표 논문 |
| ------ | --------- | --------- |
| Generative AI | 연산 효율성 및 물리적 일관성 확보 | Spectral Progressive Diffusion for Efficient Image and Video Generation |
| 3D Vision & Rendering | 3DGS 기반의 복잡한 광학 현상 및 공간 일관성 모델링 | RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting |
| Foundation Models | 비전 파운데이션 모델의 효율적 활용 및 토큰화 최적화 | Vision Foundation Models as Generalist Tokenizers for Image Generation |

> 핵심 메시지: 컴퓨터 비전 연구는 생성 모델의 물리적 일관성 강화와 3D 가우시안 스플래팅을 통한 고효율 렌더링 기술로 진화하고 있습니다.


## 2. CV 태스크별 분류

| 태스크 | 핵심 내용 | 대표 논문 |
| ------ | --------- | --------- |
| Generation | 물리적 계획(Planning) 기반 비디오 생성 및 효율적 확산 모델 | NEWTON: Agentic Planning for Physically Grounded Video Generation |
| 3D Reconstruction | 3D 가우시안 스플래팅을 활용한 실내 공간 및 반투명 객체 모델링 | PanoWorld: A Generative Spatial World Model for Consistent Whole-House Panorama Synthesis |
| Vision Sensing | 광학-알고리즘 공동 설계를 통한 초저지연 시선 추적 | Low Latency Gaze Tracking via Latent Optical Sensing |

## 3. 방법론 트렌드

| 방법론 | 적용 사례 | 대표 논문 |
| ------ | --------- | --------- |
| Agentic Planning | 비디오 생성의 물리적 정확도 개선 | NEWTON: Agentic Planning for Physically Grounded Video Generation |
| Spectral Decomposition | 확산 모델의 해상도 점진적 확장 및 연산량 절감 | Spectral Progressive Diffusion for Efficient Image and Video Generation |
| Gaussian Splatting | 반사/투과 모델링 및 실내 공간 생성 | RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting |

## 4. 크로스 도메인 융합

| 융합 분야 | 핵심 포인트 | 기대 효과 |
| --------- | ----------- | --------- |
| AR/VR 및 하드웨어 | 광학 센싱과 신경망의 결합을 통한 실시간 시선 추적 | 자원이 제한된 기기에서의 고성능 포비티드 렌더링 구현 |
| 물리 엔진 및 로보틱스 | 생성 모델 내 물리적 역학 루프 도입 | 물리적으로 정확한 비디오 생성 및 시뮬레이션 환경 구축 |

---

## 5. 개별 논문 요약

### 1. Domain Transfer Becomes Identifiable via a Single Alignment

- **arXiv**: https://arxiv.org/abs/2605.17918
- **Score**: 8.5 / 10
- **한줄 요약**: 도메인 전송(Domain Transfer)의 근본적인 비식별성(non-identifiability) 문제를 해결하고, 최소한의 정보로 의미론적 대응 관계를 보존하는 전송 매핑을 학습하는 방법론 제시.
- **핵심 기여**: 구조적 희소성(structural sparsity) 조건 하에서 단 하나의 앵커 샘플(anchor sample)만으로도 지면 진실(ground-truth) 매핑을 식별할 수 있음을 이론적으로 증명하고, 이를 위한 효율적인 희소성 정규화 기법을 제안함.
- **방법론 개요**: 데이터의 자코비안(Jacobian) 행렬에 구조적 희소성 제약을 부여하고, 무작위 마스킹된 유한 차분법(randomized masked finite differences)을 사용하여 고차원에서도 계산 가능한 효율적인 정규화 알고리즘을 구현함.
- **의의**: 기존의 분포 매칭 방식이 가진 의미론적 불일치(content misalignment) 문제를 해결하며, 대규모 레이블이나 보조 정보 없이도 이론적으로 보장된 정확한 도메인 전송을 가능하게 하여 실용적 범용성을 크게 확장함.

### 2. Vision Foundation Models as Generalist Tokenizers for Image Generation

- **arXiv**: https://arxiv.org/abs/2605.18390
- **Score**: 8.2 / 10
- **한줄 요약**: 고정된 비전 파운데이션 모델(VFM)의 풍부한 의미론적 표현을 활용하여 이미지 생성의 효율성과 품질을 극대화하는 새로운 시각적 토크나이저 'VFMTok' 제안.
- **핵심 기여**: 기존 토크나이저의 공간적 중복성을 제거하고 의미론적 밀도를 높여, 분류기 없는 안내(CFG) 없이도 고품질 합성이 가능하며 학습 수렴 속도를 3배 향상함.
- **방법론 개요**: 영역 적응형 양자화(Region-Adaptive Quantization)를 통해 공간적 중복을 줄이고, 대조 학습과 잠재 마스크 이미지 모델링(Latent-MIM)을 결합한 하이브리드 목적 함수로 VFM의 잠재 표현을 재구성함.
- **의의**: 픽셀 단위 재구성에 의존하던 기존 방식의 한계를 극복하고, 고차원 의미 정보를 활용함으로써 생성 모델의 계산 효율성과 추론 성능을 동시에 확보하는 새로운 패러다임을 제시함.

### 3. Spectral Progressive Diffusion for Efficient Image and Video Generation

- **arXiv**: https://arxiv.org/abs/2605.18736
- **Score**: 7.8 / 10
- **한줄 요약**: 확산 모델의 생성 과정에서 저주파 성분이 먼저 생성되고 고주파 성분이 나중에 생성된다는 '스펙트럼 자기회귀' 특성을 활용하여, 해상도를 점진적으로 높이는 효율적인 생성 프레임워크를 제안함.
- **핵심 기여**: 기존 확산 모델의 구조 변경 없이 플러그 앤 플레이 방식으로 적용 가능한 해상도 확장 기법을 통해, 이미지 및 비디오 생성 시 연산량을 획기적으로 절감(이미지 최대 7배, 비디오 2.5배)하면서도 고품질을 유지함.
- **방법론 개요**: 모델의 파워 스펙트럼 분석을 기반으로 해상도 전환 시점을 결정하고, 스펙트럼 노이즈 확장(Spectral Noise Expansion) 기법을 통해 노이즈 제거 과정 중 점진적으로 해상도를 높이는 방식을 사용함.
- **의의**: 고해상도 생성 시 발생하는 Diffusion Transformer(DiT)의 이차 연산 복잡도 문제를 해결하여, 대규모 모델의 연산 효율성을 극대화하고 실용적인 고품질 생성 환경을 구축함.

### 4. Generalize cross-ratios in n-dimensional Plane-Based Geometric Algebra

- **arXiv**: https://arxiv.org/abs/2605.18398
- **Score**: 7.8 / 10
- **한줄 요약**: 
- **핵심 기여**: 
- **방법론 개요**: 
- **의의**: 

### 5. NEWTON: Agentic Planning for Physically Grounded Video Generation

- **arXiv**: https://arxiv.org/abs/2605.18396
- **Score**: 7.8 / 10
- **한줄 요약**: 비디오 생성 모델의 물리적 일관성 부족 문제를 해결하기 위해, 단일 생성 방식에서 벗어나 에이전트 기반의 계획 및 검증 루프를 도입한 NEWTON 프레임워크 제안.
- **핵심 기여**: 물리적 역학을 생성 과정과 분리하여 계획(Planning) 단계에서 처리하고, Flow-GRPO를 통해 학습된 에이전트가 반복적인 검증과 재계획을 수행함으로써 비디오 생성 모델의 물리적 정확도를 획기적으로 개선함.
- **방법론 개요**: 사전 학습된 비디오 생성 모델을 수정 없이 활용하며, 물리 엔진 및 검증 모듈을 포함한 에이전트가 물리적 궤적을 계획하고, 피드백 루프를 통해 생성물을 반복적으로 최적화하는 구조.
- **의의**: 기존의 거대 모델들이 겪는 '물리적 명세 부족(specification bottleneck)' 문제를 해결하여, 복잡한 물리적 상호작용이 필요한 영상에서 정교한 동역학적 일관성을 확보할 수 있는 범용적인 솔루션을 제시함.

### 6. Improved Baselines with Representation Autoencoders

- **arXiv**: https://arxiv.org/abs/2605.18324
- **Score**: 7.8 / 10
- **한줄 요약**: RAEv2는 사전 학습된 비전 인코더를 활용하는 표현 오토인코더(RAE)의 구조와 학습 방식을 최적화하여, 재구성 품질과 생성 성능 간의 트레이드오프를 해결하고 학습 효율을 극대화한 통합 생성 프레임워크입니다.
- **핵심 기여**: 기존 대비 10배 빠른 학습 수렴 속도 달성, 새로운 효율성 지표인 EPFID@k 제안, 그리고 외부 모델 없이 내부 가이던스 메커니즘을 활용한 추론 효율성 및 생성 품질의 비약적 향상을 입증했습니다.
- **방법론 개요**: 다중 계층 표현 집계(Multi-layer Aggregation)를 통해 인코더 정보를 보강하고, RAE와 REPA를 통합하여 x-예측 기반의 자체 가이던스 메커니즘을 구현함으로써 추가적인 연산 비용 없이 고성능 생성을 가능하게 했습니다.
- **의의**: 기존 VAE 기반 모델의 복잡성과 연산 비용 문제를 해결하면서도, 텍스트-이미지 생성 및 월드 모델 등 다양한 도메인으로 확장이 가능한 범용적이고 확장성 높은 생성 아키텍처를 제시했다는 점에서 중요합니다.

### 7. Low Latency Gaze Tracking via Latent Optical Sensing

- **arXiv**: https://arxiv.org/abs/2605.17990
- **Score**: 7.8 / 10
- **한줄 요약**: 전통적인 고해상도 이미지 기반 시선 추적 방식에서 벗어나, 광학적 인코딩을 통해 시선 정보를 직접 추출하는 저지연 잠재 공간 센싱 프레임워크를 제안함.
- **핵심 기여**: 마이크로렌즈 어레이와 이진 마스크를 활용한 광학-알고리즘 공동 설계를 통해 3.4ms 미만의 초저지연 성능과 극도로 낮은 연산 비용(500 KFLOPs)을 달성함.
- **방법론 개요**: 마이크로렌즈 어레이와 이진 마스크로 시각 정보를 압축하고, 16개 요소의 저해상도 포토트랜지스터 배열로 캡처한 뒤 경량 MLP 신경망을 통해 시선 방향을 직접 회귀함.
- **의의**: 고해상도 이미지 처리의 병목 현상을 제거하여 AR/VR 기기 등 자원이 제한된 환경에서 실시간 시선 추적 및 포비티드 렌더링을 가능하게 하는 효율적인 하드웨어-소프트웨어 통합 솔루션을 제시함.

### 8. PanoWorld: A Generative Spatial World Model for Consistent Whole-House Panorama Synthesis

- **arXiv**: https://arxiv.org/abs/2605.17916
- **Score**: 7.8 / 10
- **한줄 요약**: PanoWorld는 평면도를 기반으로 전체 주택을 일관성 있게 생성하기 위해, 3D 가우시안 스플래팅(3DGS) 캐싱과 파노라마 기반의 자기회귀적 생성을 결합한 공간 월드 모델입니다.
- **핵심 기여**: 룸 인식 어텐션(Room-aware Attention)을 통해 방 간의 시각적 간섭을 차단하고, 점진적 3DGS 캐싱을 통해 대규모 공간에서도 계산 효율성과 3D 기하학적 일관성을 동시에 확보했습니다.
- **방법론 개요**: 평면도에서 추출한 3D 쉘을 기하학적 프록시로 활용하고, 파노라마 LRM(Large Reconstruction Model)을 통해 각 노드별로 3DGS를 점진적으로 업데이트하며, 방 단위의 위상 정보를 고려한 어텐션 메커니즘으로 전체 구조를 유지합니다.
- **의의**: 기존 2D 생성 모델의 3D 일관성 부족 문제와 전체 3D 생성의 높은 연산 비용 문제를 해결하여, 대규모 실내 환경을 위한 고품질의 VR 투어 생성 및 확장 가능한 공간 모델링의 실용적 토대를 마련했습니다.

### 9. PIXLRelight: Controllable Relighting via Intrinsic Conditioning

- **arXiv**: https://arxiv.org/abs/2605.18735
- **Score**: 7.2 / 10
- **한줄 요약**: PIXLRelight는 물리 기반 렌더링(PBR)의 제어 가능성과 신경망 렌더링의 고품질 합성을 결합한 피드포워드 트랜스포머 기반의 이미지 재조명 프레임워크입니다.
- **핵심 기여**: 조명 제어와 이미지 합성을 분리하여, 복잡한 최적화 과정 없이도 실시간으로 물리적으로 정확하고 고해상도의 재조명을 가능하게 하는 통합 인터페이스를 제공합니다.
- **방법론 개요**: 소스 이미지와 PBR 기반의 내재적 요소(알베도, 음영, 잔차)를 각각 비대칭 인코더로 처리한 뒤, 트랜스포머를 통해 융합하여 픽셀 단위의 아핀 변조를 수행하는 피드포워드 방식을 사용합니다.
- **의의**: 기존의 느린 최적화 기반 방식이나 품질이 낮은 인버스 렌더링의 한계를 극복하여, 실제 사진에 대해 100ms 이내의 실시간 성능으로 정밀한 조명 제어와 높은 시각적 충실도를 동시에 달성했습니다.

### 10. RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting

- **arXiv**: https://arxiv.org/abs/2605.18263
- **Score**: 7.2 / 10
- **한줄 요약**: RT-Splatting은 3D 가우시안 스플래팅을 확장하여 반사와 투과가 공존하는 복잡한 반투명 장면을 단일 통합 프레임워크 내에서 모델링하는 기법입니다.
- **핵심 기여**: 기하학적 점유와 광학적 불투명도를 분리한 통합 표현 방식을 제안하고, 반사-투과 최적화 시 발생하는 모호성을 해결하는 'Specular-Aware Gradient Gating'을 통해 시각적 품질과 재구성 안정성을 획기적으로 개선했습니다.
- **방법론 개요**: 가우시안 프리미티브를 기하학적 점유와 광학적 불투명도로 분리하고, 반사를 위한 디퍼드 셰이딩과 투과를 위한 볼륨 렌더링을 결합한 하이브리드 파이프라인을 구축하여 최적화 과정에서 발생하는 아티팩트(플로터)를 억제합니다.
- **의의**: 기존의 가우시안 스플래팅이 해결하지 못했던 반투명 표면의 반사와 투과 문제를 물리적으로 정확하게 모델링함으로써, 복잡한 실세계 장면의 고품질 실시간 렌더링 및 장면 편집 가능성을 크게 확장했습니다.

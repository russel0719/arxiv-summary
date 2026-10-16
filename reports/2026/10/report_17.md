# arXiv cs.CV Daily Digest — 2026-10-16 (arXiv 공개일)

- **전체 신규 논문 수**: 165편 (new 135 + cross-list 30)
- **선별 수**: 11편

## 오늘의 트렌드

비디오·월드 모델 생성과 그 추론 가속이 가장 두꺼운 군집으로, 학습 없는 캐싱·토큰 병합·희소 어텐션이 함께 묶인다. VLM·MLLM 쪽은 공간 추론과 언어 선입견·주장 편향을 진단하는 벤치마크가 이어지고, vision-language-action 모델과 3D Gaussian Splatting 재구성이 또 한 덩어리를 이룬다. 인식·표현 쪽에서는 동결된 DINOv3·CLIP 인코더를 LoRA·어댑터·학습 없는 라우팅으로 재활용하는 흐름과, 위조·딥페이크 판별이 축을 이룬다.

---

### [CLAD: Keypoint Matching Using Global Line Correspondences](https://arxiv.org/abs/2610.21409)

**한 줄 요약**: 키포인트를 매칭된 직선들과의 근접도 벡터로 기술해, 반복 패턴·약한 텍스처 장면에서 전역 기하 맥락으로 매칭하는 디스크립터.

**핵심 기여**: SIFT·ORB처럼 로컬 이미지 패치에서 계산하는 디스크립터는 반복 패턴이나 텍스처가 약한 장면에서 서로 다른 위치의 패치가 비슷해 보여 신뢰하기 어렵다는 문제의식이다. CLAD는 각 키포인트를 «매칭된 직선들에 얼마나 가까운가»를 원소로 갖는 벡터로 표현해, 장면 안 직선들에 대한 공간 관계 자체를 디스크립터로 삼는다. 선명한 선과 약한 선형 구조를 함께 검출하고 선-키포인트 연관을 충분히 확보하기 위해 Hough 공간 1차원 극값 매칭(HOME)을 사용한다. TUM RGB-D SLAM 데이터셋과 실외 영상 시퀀스 평가에서 전통적 로컬 디스크립터가 얻는 매칭을 보완하는 기하적으로 일관된 매칭을 제공하며, 계산이 가볍다고 보고한다.

**코드**: 불명

**태그**: feature-matching, correspondence, keypoint-descriptor

---

### [DLOSAC: Joint Spatial-Geometric Image Estimation via Delaunay-Guided Local Optimization RANSAC](https://arxiv.org/abs/2610.21215)

**한 줄 요약**: RANSAC의 local optimization에서 잔차뿐 아니라 inlier의 공간 분포까지 한꺼번에 보도록, Delaunay 삼각분할로 이웃 위상을 명시한 기하 추정 프레임워크.

**핵심 기여**: 잡음 섞인 매칭점에서 기하를 추정하는 기존 local optimization은 잔차 중심이고, 공간 균일성을 넣으려는 시도도 분포 최적화와 기하 정제를 순차 2단계로 분리해 둘 사이 절충이 되지 않는다는 문제의식이다. DLOSAC는 후보 inlier 위에 Delaunay 삼각분할을 세워 이웃 위상을 명시한 뒤, 기하 모듈은 엣지 기반 일관성 척도로 기하 오차를 재고 공간 모듈은 삼각형 면적과 엣지 속성에서 분포 기술자를 뽑아 inlier 뭉침 정도를 정량화한다. 엣지 기반 기하 제약, 공간 분포 정규화, 전통적 점 단위 기하 제약을 함께 결합한다. 세 종류 기하 추정 과제를 포함한 공개 실제 데이터셋 6개에서 state-of-the-art 성능을 보고한다.

**코드**: 불명

**태그**: feature-matching, correspondence, robust-estimation

---

### [Dense4D: Pixel-Level 4D Human Correspondence](https://arxiv.org/abs/2610.22325)

**한 줄 요약**: 단안 RGB 이미지 집합만으로 신체·의복·머리카락 표면의 픽셀 단위 4D 대응을 body template 없이 피드포워드로 예측하는 모델.

**핵심 기여**: 4D 인체 복원은 관절 운동·변형·가시성 변화를 거치면서 같은 표면 점을 식별해야 한다는 문제의식이다. Dense4D는 인물 중심 crop들을 이미지-crop 변환과 함께 묶어 처리하고, 각 이미지에 대해 Human Point Map(HPM)과 깊이를 예측한다. HPM은 인물 픽셀마다 공통 기준 시점에서 관측된 표면 점의 3D 위치를 부여하므로, 기준 이미지에서 가려진 점도 다른 프레임의 관측으로부터 위치를 찾는 amodal 대응이 성립한다. crop 간 HPM 좌표를 맞추면 카메라 포즈나 큰 장면 이동을 예측하지 않고도 대응이 서고, 이미지별 깊이가 이를 3D 트랙으로 끌어올린다. 실제 인물 대상 실험에서 비교 베이스라인보다 추적 정확도가 높고 스캔 표면과의 일치가 가깝다고 보고한다.

**코드**: 불명

**태그**: correspondence, pose, 3d, video

---

### [Teaching DINOv3 About Partial 3D Geometry: A Self-Supervised Geometry-Aware Approach](https://arxiv.org/abs/2610.21802)

**한 줄 요약**: LoRA 기반 자기지도 학습으로 DINO 특징을 다듬어, 일부만 관측된 형상에서도 흔들리지 않는 descriptor를 만드는 방법.

**핵심 기여**: 부분 형상 매칭에서 기존 descriptor는 부분 형상의 경계에서 어려움을 겪거나 형상의 공간적 위치에 크게 의존하고, DINO 특징을 끌어다 쓴 기존 접근도 부분 관측을 다루도록 만들어진 것이 아니라는 문제의식이다. 제안 방법은 LoRA 기반 자기지도 학습으로 DINO 특징을 정제해 partiality에 견고한 feature descriptor를 생성한다. 전통적 descriptor나 비전 foundation 특징을 그대로 쓸 때보다 부분 형상 매칭 성능이 크게 오르고, 기존 부분 형상 매칭 파이프라인에 끼워 넣었을 때 부분 형상 매칭·좌우(left-right) 예측 벤치마크에서 state-of-the-art를 달성한다고 보고한다.

**코드**: 불명

**태그**: ssl-backbone, correspondence, peft, 3d

---

### [CertEx: Exact Visual Retrieval at Scale by Certified Exclusion](https://arxiv.org/abs/2610.21325)

**한 줄 요약**: 모든 벡터의 거리를 전정밀도로 계산하는 대신 «이웃이 될 수 없다»는 저정밀 증명으로 걸러내, GPU에서 정확한 kNN 검색을 수행하는 방법.

**핵심 기여**: 이미지 디스크립터·임베딩에 대한 정확 kNN 검색은 완전 탐색이 모든 거리를 전정밀도로 계산해야 하고 근사 인덱스는 recall이 1에 못 미치는데, 정확 검색에 실제로 필요한 것은 제외되는 벡터가 이웃이 될 수 없다는 보수적 증명뿐이라는 관찰에서 출발한다. CertEx는 각 벡터의 하한 투영(lower-bounding projection)을 half precision으로 저장하고 반올림 인증서를 같은 tensor-core 내적 안에 접어 넣어, 제외 판정을 통과한 소수 벡터에 대해서만 정확 거리를 계산한다. 모든 질의에 대해 정확한 kNN을 반환함을 증명한다. 최대 1억 벡터 규모의 16개 데이터셋에서 H100 한 장 기준 가장 빠른 cuVS 검색 대비 7.1~18.0배 처리량을 보고하며, 모든 질의가 정확해야 하는 설정에서 양자화·그래프 인덱스를 앞선다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, efficient-inference

---

### [Flow-CLIP: Image-Conditioned Residual Scoring for Compositional Image-Text Matching](https://arxiv.org/abs/2610.21937)

**한 줄 요약**: 이미지 조건에서 토큰-패치 근거가 얼마나 달라지는지로 전역 image-text 점수를 보정해, 구성적 매칭과 속성-객체 결합을 구분하는 방법.

**핵심 기여**: 비전-언어 사전학습의 문장 단위 정렬은 같은 객체와 속성을 쓰면서 결합 방식만 다른 캡션을 구분하기에 부족하다는 문제의식이다. Flow-CLIP은 Global Compatibility Calibration으로 문장 수준 유사도 척도를 학습하고, Image-Conditioned Evidence Refinement로 시각 패치 맥락을 토큰 질의에 주입한 뒤 국소 매칭 근거의 변화량으로 전역 점수를 조정한다. 또 Cross-Image Margin Ranking은 같은 긍정-부정 캡션 쌍을 맞는 이미지와 틀린 이미지에서 비교해, 이미지가 올바른 설명을 뒷받침할 때 순위 마진이 커지도록 학습한다. 구성적 매칭과 속성-객체 결합 벤치마크에서 사전학습 CLIP과 학습된 전역 정렬 대비 결합 정확도가 오르고, cross-image 순위 지도가 언어 선입견 의존을 줄인다고 보고한다.

**코드**: 공개 예정

**태그**: image-retrieval, metric-learning, image-embedding, vlm

---

### [DINO-FIL: Multi-Layer Transformer Fusion for Generative Inpainting Forgery Localization](https://arxiv.org/abs/2610.21780)

**한 줄 요약**: 사전학습 DINOv3 ViT-H+/16의 여러 층 표현을 가벼운 융합 디코더로 합쳐, 생성형 인페인팅 위조 영역을 픽셀 단위로 찾는 프레임워크.

**핵심 기여**: 이미지 편집이 남기는 미세하고 공간적으로 국소적인 아티팩트는 단일 층 특징만 쓰는 표준 접근이 놓치기 쉽다는 문제의식이다. DINO-FIL은 사전학습된 DINOv3 ViT-H+/16 인코더의 여러 깊이에 걸친 중간 transformer 표현을 모아 의미 구조와 세밀한 텍스처 불일치를 함께 포착하고, 가벼운 융합 디코더로 픽셀 단위 위치를 예측한다. B-Free로 학습한 뒤 Beyond the Brush·CocoGlide·TGIF·SAGI-D에서 cross-dataset으로 평가했을 때 평균 성능과 다섯 중 네 데이터셋에서 기존 베이스라인을 앞서고, 조작되지 않은 원본 이미지에 대한 true negative rate도 높게 유지한다고 보고한다.

**코드**: 불명

**태그**: forgery-detection, ssl-backbone, foundation-model, segmentation

---

### [RLDF: A Region-Level Deepfake Dataset and Benchmark for Partial-Face Manipulation Detection](https://arxiv.org/abs/2610.21438)

**한 줄 요약**: 얼굴의 일부 영역만 교체한 200만 장 규모 deepfake 데이터셋과 평가 프로토콜, 그리고 mask-guided cross-attention 베이스라인.

**핵심 기여**: 기존 deepfake 검출 모델은 얼굴 전체를 교체하거나 합성한 이미지 위에 세워져, 조작이 국소 얼굴 하위 영역에 한정될 때도 잡아내는지가 열린 질문이라는 문제의식이다. RLDF는 region-aware partial swap 합성 모델로 8가지 face-swapping 기법을 써서, 눈·코·입·눈썹의 단일 영역 4개와 복합 영역 4개를 포함한 7개 얼굴 영역에 대해 200만 장 이상의 부분 교체 이미지를 생성하고, 평가 프로토콜 3가지를 정의해 12개 최신 검출기를 5개 표준 cross-dataset 설정·DF40·RLDF에서 벤치마크한다. 기존 검출기는 부분 얼굴 영역에 걸쳐 일관되게 일반화하지 못해 region-level 평가에서 AUC가 10.5%p, 정확도가 10%p 떨어지며, 논문은 region-level 조작을 검출하는 mask-guided cross-attention 모델을 베이스라인으로 함께 제안한다.

**코드**: 공개([RLDF](https://github.com/RLDF-Dataset/RLDF))

**태그**: forgery-detection, dataset-benchmark, face-swap

---

### [When Should a Low-Light Pipeline Generate? Auditable Risk Control for Selective Generative Enhancement](https://arxiv.org/abs/2610.21335)

**한 줄 요약**: 영역별로 생성 전문가로 갈아탈지를 결정하되, 분포 무관 harm-budget 인증서가 허용할 때만 교체하고 근거가 약하면 기권하는 라우팅 프레임워크.

**핵심 기여**: 생성형 저조도 보정기는 그럴듯한 텍스처를 복원하지만 구조를 지어낼 수 있고, 복원 네트워크는 구조를 지키지만 일부 영역이 덜 개선된 채 남으며, 두 장점 모두 공간적으로 균일하지 않다는 문제의식이다. 논문은 이를 «동결된 기본 전문가를 어디서 덮어쓸 것이며 근거가 부족하면 언제 교체를 거부할 것인가»라는 결정 문제로 공식화한다. VetoNet은 동결된 복원-생성 전문가 쌍의 상보성과 라우팅 방향을 먼저 측정한 뒤, 배포 시점에 얻을 수 있는 신호만으로 영역 교체의 효용을 예측하고, 분포 무관 harm-budget 인증서가 LPIPS 위험 예산을 허용할 때만 교체를 승인한다. 여러 전문가 쌍과 도메인 실험에서 상보성이 충분히 예측 가능할 때는 통계적으로 유의한 인증 이득을 얻고, 전문가 간 강약이 뒤집히면 라우팅 방향도 뒤집으며, 근거가 약하거나 도메인 이동이 있으면 보수적으로 교체를 기권한다고 보고한다.

**코드**: 불명

**태그**: calibration, abstain, risk-control

---

### [Pixels to Tokens: Token Space Efficient Active Learning for Low-Budget Semantic Segmentation](https://arxiv.org/abs/2610.20881)

**한 줄 요약**: 동결된 ViT의 네이티브 토큰 격자 위에서 직접 다양성 기반 선택을 수행해, 이미지당 한 픽셀 수준의 극저예산 능동학습으로 semantic segmentation을 학습하는 프레임워크.

**핵심 기여**: ViT 백본용 기존 능동학습은 대부분 패치·영역 단위로 동작해 픽셀 라벨링 부담이 크고, 이미지당 한 픽셀 수준으로 내리면 정보량이 큰 위치를 찾는 일과 극히 희소한 신호로 디코더를 학습하는 일을 동시에 해결해야 한다는 문제의식이다. TEAL은 동결 ViT 백본을 쓰며, 토큰 임베딩을 조밀한 픽셀 해상도로 보간할 때 생기는 아티팩트를 피하려고 네이티브 토큰 격자 위에서 선택을 수행하고, 다층 토큰 기술자에 2단계 MaxHerding을 적용해 대표 후보를 고른 뒤 더 조밀한 디코더 격자에서 margin 기반 불확실도로 다듬는다. CamVid·Cityscapes·ADE20K·Pascal Context에서 이미지당 1픽셀일 때 가장 강한 베이스라인 대비 최대 +24.36 mIoU, 10픽셀이면 완전지도 성능의 최대 97%에 도달하고, 모든 베이스라인에 같은 DINOv3 백본을 부여해도 개선이 유지된다고 보고한다.

**코드**: 불명

**태그**: segmentation, ssl-backbone, active-learning

---

### [LAMP: Layerwise Adaptive Mixing of Predictors for Training-Free Few-Shot Vision-Language Adaptation](https://arxiv.org/abs/2610.22182)

**한 줄 요약**: 동결 인코더의 여러 층에서 뽑은 전역·지역 정보를 학습 없이 혼합해 few-shot 분류를 개선하는 프레임워크.

**핵심 기여**: few-shot 적응은 대개 인코더의 마지막 전역 표현에만 의존해 중간 층의 보완 정보를 쓰지 않는데, 층마다 차원이 다르고 유용성도 과제마다 달라 결합이 쉽지 않다는 문제의식이다. LAMP는 뷰당 한 번의 forward로 모든 기술자를 얻고, 전역 예측기와 support로 보정한 지역 커널 예측기가 같은 라벨 잔차를 독립적으로 적합한 뒤 라벨된 검증 데이터로 클래스 점수 공간에서 둘의 혼합을 선택하며, 학습된 투영 없이 원래 특징 차원을 유지한다. 11개 데이터셋과 ViT·ResNet 백본 실험에서 비교 대상 학습 없는 ResNet-50 방법 가운데 4·8·16-shot 평균 정확도가 가장 높고 16-shot에서 78.73%에 도달하며, 변형 LAMP-F는 전역 특징만 쓰는 짝지은 대조군 대비 ViT-B/16에서 1.96%p, ResNet-50에서 2.54%p 평균 개선을 보고한다. 통제 실험은 개선의 주요 원인이 다층 통합임을 가리킨다.

**코드**: 불명

**태그**: training-free, foundation-model, image-embedding, few-shot

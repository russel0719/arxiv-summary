# arXiv cs.CV Daily Digest — 2026-09-30 (arXiv 공개일)

- **전체 신규 논문 수**: 284편 (new 233 + cross-list 51)
- **선별 수**: 12편

## 오늘의 트렌드

world model과 world-action model이 가장 두꺼운 군집으로, 주행·조작 환경의 미래 예측과 행동 정책을 함께 다룬다. 다음은 video diffusion의 few-step 가속과 on-policy self-distillation, multimodal LLM의 visual token pruning·예산 배분 같은 추론 효율화다. 장시간 비디오 이해의 메모리 구조와 감정 추론 평가가 각각 묶이고, AI 생성 이미지 판별과 편집 영역 국소화의 포렌식, 원격탐사·의료영상 응용이 나머지 축이다.

---

### [UltraMatch: Transport Path Routing for Ultra-Fast and Memory-Efficient Image Matching](https://arxiv.org/abs/2609.36980)

**한 줄 요약**: semi-dense matcher의 coarse matching 단계에서 전체 token-to-token 행렬을 만들지 않고 후보 매칭 경로 일부만 라우팅해, 매칭 정확도를 유지하면서 속도와 메모리를 줄인 프레임워크.

**핵심 기여**: 기존 semi-dense matcher는 coarse matching이 필수 단계지만 dense token-level 매칭 때문에 계산·메모리가 해상도에 제곱으로 늘어난다고 지적한다. 경량 Transport Path Router가 coarse block 표현 위에서 각 source block에 대한 target block 후보를 순위화해 소수만 남기고, 이후 token-level 매칭을 선택된 경로로 제한하며, 라우팅된 후보 위에서만 동작하되 전역 경쟁을 유지하는 sparse global Dual-Softmax를 함께 쓴다. 특징 추출에는 배포를 겨냥한 구조 재파라미터화를, fine matching head에는 파라미터 공유를 적용했다. SuperPoint+LightGlue보다 1.67배 빠르고 peak inference memory는 0.44 GiB이며, 기존 semi-dense matcher가 2K 이전에 메모리 부족으로 실패하는 조건에서 RTX 3090 한 장으로 6K 해상도까지 추론한다. 라우팅 전략 자체도 이식 가능해 EDM과 ELoFTR에 적용했을 때 정확도 손실 없이 end-to-end 약 2배 가속을 보고한다.

**코드**: 공개([UltraMatch](https://github.com/JiajunLe/UltraMatch))

**태그**: feature-matching, correspondence, efficient-inference

---

### [SCCM: Spherically Consistent Coarse Matching for ERP Dense Feature Correspondence](https://arxiv.org/abs/2609.36545)

**한 줄 요약**: 평면 이미지로 학습한 dense matcher가 equirectangular projection(ERP)에서 무너지는 원인을 위상·거리·면적 세 왜곡으로 나누고, 이를 coarse 단계의 attention과 covisibility 게이팅에서 각각 교정한 매칭 방법.

**핵심 기여**: 360도 영상의 표준 표현인 ERP는 chart가 위상·metric·area 왜곡을 동시에 유발하는데 기존 coarse matching과 가시성 추정은 이를 명시적으로 모델링하지 않는다고 본다. SCCM은 chart를 고려하지 않는 cross-attention/dual-softmax coarse matcher에 두 가지 구면 prior를 더하는데, Spherical Positional Attention은 yaw 주기성을 갖는 RoPE(위상)와 tangent-plane bias(거리)를 결합하고, Area-Aware Covisibility는 sigmoid 이전에 log-area 보정(면적)을 적용한다. RoMa V1 프레임워크에서 인코더·refiner 구조·손실을 동일하게 두고 coarse 단계만 바꿨을 때 Matterport3D의 PCK@1도가 0.229에서 0.275로 올랐고, ERP 전용 EDM(0.163)과 ERP로 재학습한 RoMa V1(0.198)도 상회한다. Stanford2D3D로 zero-shot 전이되며 실외 Holo360D로 학습한 경우에도 같은 경향을 보고한다.

**코드**: 불명

**태그**: correspondence, feature-matching, panoramic-erp

---

### [FM-ReID: Selective Competitive Token Routing for Object Re-Identification](https://arxiv.org/abs/2609.36560)

**한 줄 요약**: foundation model의 dense token에 들어 있는 국소 단서가 단일 holistic descriptor에서 희석되는 문제를 두고, 복수의 mining query가 DINOv3 token을 경쟁적으로 가져가도록 해 다중 query descriptor를 학습하는 re-identification 프레임워크.

**핵심 기여**: ReID에서는 서로 다른 개체가 전역 외형은 비슷하고 구분 단서는 국소적·이질적이며 특정 시점에서만 보이는데, 동물의 무늬·상흔, 사람의 소품, 차량의 국소 외형이 모두 이 성격을 갖는다고 정리한다. Competitive Fine-grained Mining 모듈이 복수의 mining query와 residual query를 두고 dense DINOv3 token을 두고 경쟁시키며, prior를 넘는 비율로 할당된 token만 각 query가 유지하고 검색 descriptor에서 배제된 token은 residual slot이 받는다. 결과로 얻은 다중 query descriptor는 holistic 표현과 함께 검색용으로 학습되며, 고정된 공간 분할이나 등면적 제약을 쓰지 않는다. 동물·사람·차량 ReID 벤치마크에서 경쟁력 있는 결과를 보고한다.

**코드**: 불명

**태그**: re-identification, image-retrieval, fine-grained, foundation-model

---

### [ResComEmb: Effective and Efficient Multimodal Embedding via Residual Homogeneity Compression](https://arxiv.org/abs/2609.37225)

**한 줄 요약**: 입력을 벡터 하나로 압축하면 표현력이 떨어지고 visual token 시퀀스를 그대로 남기면 저장·연산 비용이 커지는 절충을 두고, 다중 granularity 뷰를 잔차 기반으로 압축해 multi-vector 임베딩을 만드는 프레임워크.

**핵심 기여**: MLLM 기반 범용 멀티모달 표현학습이 단일 벡터 압축과 긴 token 시퀀스 유지 사이에서 하나를 택해 왔다는 문제의식에서 출발한다. ResComEmb는 각 입력을 native dynamic resolution으로 global·intermediate·fine-grained 세 단계 뷰로 인코딩한 뒤, 학습 가능한 Residual Homogeneity Compression 모듈이 명시적 visual token 예산 아래에서 같은 granularity 내 중복과 granularity 간 반복을 함께 줄인다. 점수화에는 양방향 late interaction을 쓰되 각 방향의 최강 token 매칭을 평균하고 양측의 유효 token 수로 두 점수를 가중 결합하는 길이 적응 방식을 쓴다. MMEB와 ViDoRe V1/V2에서 VLM2Vec-V2보다 높은 품질을 보고하고, 시각 문서 검색에서는 ColQwen2.5의 visual token 예산 37.5%만 쓰면서 이를 상회한다.

**코드**: 불명

**태그**: image-embedding, image-retrieval, vlm, efficient-inference

---

### [Procedural Core: A Compact Recurrent Initialization for Vision Transformers](https://arxiv.org/abs/2609.37631)

**한 줄 요약**: 절차적 생성 데이터로 얻는 일반적 귀납 구조를 모델마다 반복 사전학습하지 않고 작은 recurrent transformer의 가중치에 담아 두었다가, 임의 폭·깊이의 transformer 초기화로 확장해 재사용하는 방법.

**핵심 기여**: 소량의 추상적 절차 생성 데이터가 일반적 귀납 구조 습득에 도움이 된다는 선행 결과는 대상 모델마다 사전학습 단계를 반복해야 한다는 비용을 남긴다고 지적한다. Procedural Core는 최소 크기의 recurrent transformer를 절차 데이터로 학습한 뒤 그 가중치를 확장해 초기화에 쓰며, 분석에서 모델 간 전이되는 압축 가중치 학습에는 recurrence가 필수임을 짚는다. 1M 파라미터 core를 확장해 85M ViT-Base를 초기화하면 random init 대비 ImageNet top-1이 2.2 pp 오르고, self-supervised 학습(DINO)과 자연어·코드 모델링에서도 개선을 보고한다. ViT에서는 high-norm token 억제가 핵심 이득으로 지목되며 zero-shot segmentation(ImageNet-S mAP 32.3 → 42.9), object localization(VOC07 CorLoc 9.9 → 18.4), depth estimation(NYUv2 RMSE 1.104 → 0.998)이 함께 개선된다. 도메인·과제별 데이터를 쓰지 않는다는 점을 조건으로 제시한다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, foundation-model, segmentation

---

### [Losing the name before the box: measuring and repairing what narrow fine-tuning costs a detector outside its deployment vocabulary](https://arxiv.org/abs/2609.36426)

**한 줄 요약**: 넓은 코퍼스로 사전학습한 detector를 좁은 도메인에 fine-tuning할 때 배포 vocabulary 밖 객체의 제안 커버리지가 얼마나 무너지는지를 종단 프로토콜로 측정하고, 학습 없이 되돌리는 보정을 제시한 논문.

**핵심 기여**: 좁은 도메인 fine-tuning은 in-domain 정확도를 올리지만 vocabulary가 이름 붙이지 않는 객체의 커버리지 손실은 어떤 in-domain 테스트셋에도 예시가 없어 드러나지 않는다는 문제의식에서 출발한다. 사전학습 체크포인트와 그 fine-tuning 후손을 짝지어, 사전학습이 덮었고 vocabulary가 빠뜨린 범주에 대해 상위 K개 영역이 여전히 덮는 box 비율 $C_\tau$를 추적하는 종단 프로토콜을 제시한다. 4개 아키텍처·3개 도메인에서 in-domain 정확도가 오르는 동안 $C_\tau$는 1024 px² 이상 box 기준 5.12~63.35점 하락했고, detection AP는 놓친 box와 이름을 틀린 box를 같게 처리하기 때문에 이 하락을 드러내지 못한다. 손실은 구조적이어서 사전학습 이력을 공유하지 않는 세 아키텍처가 어느 범주에서 커버리지를 잃는지에 일치했고, 모델이 애초에 배우지 않은 범주에서는 손실이 없었다. 복구는 학습 없이 사전학습 상태를 정규화 통계까지 포함해 4분의 1 섞는 것으로, 모든 조건에서 커버리지가 오르고 in-domain 정확도 손실은 최대 2.47점이며 추가 평가 1회 비용으로 관측 가능하다.

**코드**: 불명

**태그**: open-vocab-detection, object-detection, continual-learning, calibration

---

### [Online Versatile Incremental Learning: Towards Class and Domain-Agnostic Adaptation at Any Time](https://arxiv.org/abs/2609.36442)

**한 줄 요약**: 클래스와 도메인이 경계 표시 없이 동시에 변하는 온라인 시나리오를 Online VIL로 정의하고, geodesic flow kernel 기반 대조학습과 전역 위상 보존으로 대응하는 continual learning 프레임워크.

**핵심 기여**: 기존 continual learning이 클래스 변화와 도메인 변화가 동시에·연속적으로 일어나는 상황을 다루지 못한다는 점을 지적하며, 명시적 task 경계 없이 두 축이 함께 진행되는 Online VIL 시나리오를 도입한다. 제안 프레임워크 TopFlow는 geodesic flow kernel을 대조학습에 통합해 도메인에 무관한 표현을 유도하는 Domain-agnostic Flow Matching과, 과거 예제를 저장하지 않고 특징 공간의 전역 구조를 유지하는 Global Topology Preservation을 함께 쓴다. Online VIL 설정 실험에서 기존 방법의 한계를 보완하며 state-of-the-art 성능을 보고한다.

**코드**: 공개([Online-VIL](https://github.com/KU-VGI/Online-VIL))

**태그**: continual-learning, metric-learning, image-embedding

---

### [FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection](https://arxiv.org/abs/2609.37314)

**한 줄 요약**: 결함 생성과 이상 이미지 합성을 분리해, 소수의 결함 패치를 한 번 만들어 은행에 저장한 뒤 정상 이미지 위에 반복 합성하는 산업 이상 탐지용 데이터 합성 프레임워크.

**핵심 기여**: 기존 합성 방식이 절차적 접근은 빠르지만 복잡한 이상을 표현하지 못하고 생성 모델 접근은 다양하지만 샘플마다 생성 비용이 든다는 양극단에 놓여 있다고 정리한다. FLASH는 정상 이미지만 주어진 상태에서 VLM 가이드와 이미지 생성 모델로 소수의 결함 이미지를 만든 뒤 재사용 가능한 결함 패치를 추출·검증해 저장하고, 합성 단계에서는 Object Boundary Suppression으로 host 이미지의 전경 객체 영역을 추정하고 Multi-Resolution Spectral Pyramid 노이즈로 크기 조절이 가능한 다양한 마스크를 만들어 결함을 배치·블렌딩한다. MVTec AD 2에서 합성 이상이 실제 결함과의 캘리브레이션 격차를 거의 메워 image-level F1 78.1%에 도달했고(실제 이상 상한 83.6%), 여러 detector 사이에서 가장 일관된 캘리브레이션 전이를 보였다. 샘플마다 생성하는 방식보다 11.95배 이상 빠르게 합성한다.

**코드**: 불명

**태그**: industrial-inspection, anomaly-detection, defect-detection, sim2real

---

### [Visual Anomaly Synthesis for Model Selection in Data Scarcity](https://arxiv.org/abs/2609.37360)

**한 줄 요약**: 대상 설비의 결함 샘플이 아예 없는 상황을 전제로, 심각도 등급이 매겨진 결함을 정상 이미지 위에 합성해 이상 탐지 모델의 선택·검증에 쓰는 프레임워크.

**핵심 기여**: 산업 상태 감시용 결함 탐지는 검증되어야 신뢰할 수 있는데 결함 샘플은 희귀하고 특정 설비에서는 존재하지 않는 경우가 많다는 점에서 출발한다. 문헌에서 공통 고장 모드 분류를 뽑아 심각도별 지시형 프롬프트로 정제하고, 정상 이미지에서 잘라낸 관심 영역을 사전학습 이미지 생성 모델(FLUX.2 [klein])로 편집한 뒤 색 정합·블렌딩으로 원본과의 구조적 일관성을 높이며, 생성물은 스코어러와 추정 탐지 난이도로 걸러낸다. MVTecAD 모델 선택 실험에서 테스트 데이터에 접근해 고른 최선의 고정 모델 대비 image AUROC 선택 후회를 거의 절반으로 줄였고, 심각도 등급이 필요하다는 점을 실험으로 보인다. 수력 Pelton 터빈 러너 현장 감시 사례에서는 합성 이미지로 선택·검증한 PatchCore 기반 모델이 최적 임계에서 정탐률 94%, AUROC 0.97을 보였으나 초기 단계 결함은 여전히 어렵다고 보고한다.

**코드**: 불명

**태그**: industrial-inspection, anomaly-detection, defect-detection, calibration

---

### [Scaling Full Conformal Image Classifiers](https://arxiv.org/abs/2609.37298)

**한 줄 요약**: 분포 무관 커버리지 보장을 주지만 테스트 시점마다 후보별 재학습이 필요해 대규모에서 쓰기 어려운 full conformal prediction을, zero-shot VLM으로 후보를 미리 쳐내 실행 가능하게 만든 방법.

**핵심 기여**: split conformal은 데이터 효율이 낮고 full conformal(FCP)은 통계 효율이 높지만 후보 라벨마다 모델 재적합이 필요해 큰 라벨 공간에서는 계산이 감당되지 않는다는 문제를 다룬다. Targeted Full Conformal Prediction은 경량 inductive conformal predictor로 가능성이 낮은 라벨을 먼저 잘라내고 남은 후보에만 FCP를 적용해, 결합된 conformal 절차의 형식적 보장을 유지하면서 계산량을 줄인다. 여기에 rank-one inverse-covariance 갱신 기반의 효율적 VLM 적응 솔버 Stabilized Online LDA를 함께 제안한다. ImageNet을 포함한 여러 벤치마크에서 완만한 테스트 시점 오버헤드로 full conformal 분류를 수행하며, split conformal 대비 더 작은 예측 집합과 더 안정적인 경험적 커버리지를 보고한다.

**코드**: 불명

**태그**: calibration, vlm, efficient-inference

---

### [RED: Reconstruction Evolution Dynamics for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2609.36822)

**한 줄 요약**: 재구성의 최종 결과만 비교하던 기존 판별 방식 대신, coarse-to-fine 재구성 과정에서 실제 이미지와 생성 이미지의 token 예측 가능성이 뒤집히는 현상을 근거로 중간 단계 증거를 모으는 AI 생성 이미지 판별 프레임워크.

**핵심 기여**: 생성기가 빠르게 바뀌는 상황에서 알려진 생성 방식을 넘어 일반화되는 포렌식 단서가 필요한데, 기존 판별기는 정적 표현이나 재구성 종점의 차이에 의존해 중간 단계를 활용하지 않았다고 지적한다. RED는 실제와 생성 이미지의 상대적 token 예측 가능성이 재구성 스케일에 따라 역전될 수 있다는 관찰에서 출발해, 고정된 multiscale VQ-VAE가 만든 재구성 궤적을 고정 CLIP 인코더의 공유 특징 공간에 표현하고, 고정 VAR 모델이 주는 스케일별 token negative log-likelihood로부터 이미지마다 적응적인 단계 가중치를 학습한다. cross-stage 증거 집계 모듈이 원본 표현과 가중된 재구성 특징을 함께 모델링해 궤적을 따라 상호작용하는 단서를 포착한다. 6개 벤치마크에서 평균 정확도 92.5%, 평균 정밀도 97.5%를 보고하고 일반적인 화질 열화에 대한 강건성도 함께 제시한다.

**코드**: 공개 예정

**태그**: forgery-detection, generative, foundation-model

---

### [From Sharp Eyes to Expert Mind: Internalizing Expert Knowledge in MLLMs for Tampered Text Detection](https://arxiv.org/abs/2609.36145)

**한 줄 요약**: 문서 위·변조 텍스트 탐지에서 전문 모델의 미세 흔적 감지력과 MLLM의 전이력을 합치되, 외부 모듈로 붙이지 않고 MLLM 내부에 전문가 지각을 내재화하는 2단계 학습 프레임워크.

**핵심 기여**: 전문 탐지 모델은 미세한 조작 흔적을 잘 잡지만 문서 도메인이 바뀌면 일반화가 떨어지고, MLLM은 의미 이해와 전이력이 강하지만 저수준 포렌식 아티팩트에 둔감하다는 상보성에서 출발한다. 두 특성을 합치는 데 걸림돌로 거친 visual token과 작은 변조 영역 사이의 Spatial Precision Mismatch, 의미 중심 사전학습과 저수준 포렌식 지각 사이의 Perceptual Granularity Mismatch를 지목한다. Expert Knowledge Internalization은 1단계에서 Text-Focused·Image-Focused 전략으로 작은 텍스트 영역에 공간적 초점을 맞추고, 2단계에서 Forensic-General Representation Alignment 손실로 얕은 LLM 표현을 사전학습된 포렌식 전문가의 표현과 정렬해 단서가 깊은 의미 추상화로 희석되기 전에 미세 아티팩트 지각을 획득하게 한다. in-domain·cross-domain 벤치마크에서 기존 전문가 기반·MLLM 기반 방법을 앞서며, 전문가 모델은 학습 시점에만 필요해 추론 효율은 원본 모델과 거의 같다.

**코드**: 불명

**태그**: forgery-detection, print-forensics, ocr-document, vlm


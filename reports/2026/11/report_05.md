# arXiv cs.CV Daily Digest — 2026-11-04 (arXiv 공개일)

- **전체 신규 논문 수**: 160편 (new 141 + cross-list 19)
- **선별 수**: 11편

## 오늘의 트렌드

MRI·내시경·병리·흉부 X-ray를 다루는 의료 영상이 가장 큰 군집이다. LiDAR·radar 융합과 sim2real LiDAR 검출, Gaussian Splatting 재구성이 그다음으로 두껍다. VLM·VLA·video world model의 벤치마크와 사후학습도 큰 덩어리를 이룬다. 방법론으로는 frozen DINOv2/v3·SAM3·CLIP 특징 위에 가벼운 모듈만 학습하는 설계와, Mamba 기반 장기 시퀀스 모델링이 반복해서 나타난다.

---

### [Manifold Embedding of Deep Image Features for Image Matching via Neural Adjoint Maps](https://arxiv.org/abs/2611.05083)

**한 줄 요약**: foundation model 특징으로 이미지 격자에 manifold 구조를 부여하고, 3D shape matching의 functional map·neural adjoint map을 이미지 dense correspondence에 옮긴 zero-shot 매칭 방법(NAMI).

**핵심 기여**: foundation model 특징의 nearest-neighbour 매칭은 정규화가 부족해, 특히 dense correspondence에서 노이즈가 많은 대응을 낸다는 문제의식이다. functional map은 저차원 선형 스펙트럼 표현으로 강력하지만 정의역에 의미 있는 기하가 있어야 한다. 그래서 딥 이미지 특징의 manifold embedding 위에서 유한요소 Galerkin 방법으로 이산 Laplace-Beltrami operator를 유도하고, 비선형 사상을 표현하는 neural adjoint map을 결합한다. 실세계 이미지의 여러 dense correspondence 벤치마크에서 zero-shot 대응 방법 중 새 state of the art를 보고한다.

**코드**: 공개([repo](https://github.com/NafieAmrani/NAMI))

**태그**: correspondence, feature-matching, training-free, foundation-model

---

### [CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching](https://arxiv.org/abs/2611.03932)

**한 줄 요약**: semi-dense 매처의 고정 격자 confidence 예측 대신, 연속 좌표 공간에서 대응 좌표를 반복 정제하는 실시간 local feature matcher.

**핵심 기여**: 기존 semi-dense 매처는 고정 격자 위에서 confidence를 예측해, 대응이 미리 정한 위치로 제한되고 정밀한 위치를 얻으려면 비싼 고해상도 격자가 필요하다는 문제의식이다. CoReMatch는 coarse 단계에서 Deep Aggregated Transformer로 전역 문맥을 모으며 대응 좌표를 반복 갱신하고, 가벼운 regression head로 위치를 더 날카롭게 다듬는다. 실내·실외 벤치마크에서 Efficient LoFTR보다 정확도가 높으면서, 임베디드 엣지 하드웨어에서 10배 이상 빠르게 동작한다고 보고한다.

**코드**: 불명

**태그**: feature-matching, correspondence, efficient-inference

---

### [Radial distortion homography estimation from affine-covariant or orientation-covariant features](https://arxiv.org/abs/2611.04822)

**한 줄 요약**: affine·orientation-covariant 특징의 국소 기하를 제약으로 써서, homography와 radial distortion을 더 적은 대응점으로 동시에 추정하는 minimal solver.

**핵심 기여**: 점 대응만 쓰는 기존 solver는 homography와 radial distortion을 함께 풀 때 대응점이 많이 필요하다는 문제의식이다. affine descriptor에 내재한 국소 특징 기하를 이용하는 새 제약식을 세워, point 기반 방법보다 적은 대응으로 풀리는 solver들을 만든다. 현대 robust estimation 프레임워크 안에서 outlier가 있을 때 현 state of the art 대비 큰 속도 향상을 보이면서 추정 정확도는 비슷하거나 더 낫다. 강한 fisheye 왜곡이 있는 합성·실제 영상 모두에서 시험했다.

**코드**: 불명

**태그**: feature-matching, correspondence

---

### [Generalizable AI-Generated Image Detection with Embedding-Space Explanations](https://arxiv.org/abs/2611.04111)

**한 줄 요약**: DINOv3 기반 탐지기를 먼저 학습·고정한 뒤, 그 표현을 텍스트 임베딩 공간으로 옮겨 경량 VLM이 포렌식 설명을 생성하게 하는 설명 가능한 AI 생성 이미지 탐지기(FOX).

**핵심 기여**: 탐지 분포로 백본을 적응시키면 생성기별 지문을 외워 일반화가 나빠지고, 분류와 언어 생성을 한 멀티모달 모델로 함께 학습하면 언어 목표가 시각 표현을 흔든다는 문제의식이다. 그래서 «설명 학습이 판정을 바꾸지 못한다»는 조건을 두고, DINOv3 specialist 탐지기를 먼저 만들어 잠근 뒤 joint-embedding predictor가 잠긴 시각 증거를 frozen 텍스트 인코더의 의미 공간으로 사상하고, 이 안내를 VLM이 필요할 때 말로 풀어낸다. 보지 못한 생성기 14종에서 평균 AUC 97.4, XPlainVerse BERTScore 69.8, LOKI 56.1을 보고한다. 지시 기반 AI 편집기처럼 국소 수정도 전체를 재합성해 splice 경계가 남지 않는 경우를 대상으로 삼는다.

**코드**: 불명

**태그**: forgery-detection, ssl-backbone, vlm

---

### [Learning to Falsify: Hierarchical Multiple Instance Learning for High Resolution AI-Generated Image Detection](https://arxiv.org/abs/2611.04529)

**한 줄 요약**: «가짜 패치 하나면 이미지 전체가 가짜, 진짜는 모든 패치가 진짜여야 한다»는 반증(falsification) 원리로 고해상도 AI 생성 이미지 탐지를 계층적 MIL로 푼 LTF와, 기존 탐지기에 붙이는 test-time 집계 모듈 FATAS.

**핵심 기여**: 이미지 전체를 한 번에 분류하는 기존 방법은 고해상도 이미지에서 국소 아티팩트를 놓친다는 문제의식이다. 이미지를 여러 공간 수준의 instance bag으로 나누고 반증 원리로 예측을 모으는 계층적 MIL 프레임워크를 제안하며, 학습 중 Cross-Shuffle로 이미지 수준 지름길 대신 국소 아티팩트 증거를 배우게 한다. 같은 원리를 패치 단위 예측 집계로 옮긴 plug-and-play 모듈 FATAS는 재학습 없이 기존 탐지기의 고해상도 성능을 크게 높인다고 보고한다. 여러 벤치마크에서 일반화와 강건성을 보였다고 주장하지만, 초록에 구체 수치는 없다.

**코드**: 공개([repo](https://github.com/HuiGuanLab/LTF))

**태그**: forgery-detection, training-free

---

### [Bounded AUKS: A Novel Evaluation Metric for Anomaly Detection via Bounded Area Under the Kolmogorov--Smirnov Curve](https://arxiv.org/abs/2611.04754)

**한 줄 요약**: 정상·이상 점수 분포의 분리도를 TPR−FPR(KS 곡선)의 부분 적분으로 재는 anomaly detection 평가 지표로, 적분 구간을 정상 테스트 점수 분포만으로 정한다.

**핵심 기여**: MVTec AD·VisA에서 AUROC·AUPRO가 100%에 가까워져 픽셀 수준 anomaly detection이 다 풀린 것처럼 보이지만, AUROC는 실제 운용에서 피할 수 없는 임계값 선택을 무시하고, AUPRO는 FPR을 너무 낮게 묶어 FNR이 커진다는 문제의식이다. KS 적분에서 출발한 AUKS로 두 점수 분포의 분리도를 직접 재고, 정상 테스트 표본의 점수 분포만으로 구간을 정한다. 하한은 정보가 없는 높은 FPR 영역을, 상한은 FPR을 0으로 몰아 recall이 무너지는 극단 영역을 뺀다. MVTec AD·VisA의 9개 모델 실험에서 기존 지표의 한계를 보완하고 비지도 anomaly detection 모델을 더 잘 평가한다고 보고한다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, calibration, dataset-benchmark

---

### [From Visual Matching to Textual Conditioning: Cross-Domain Few-Shot Segmentation via Reference Inversion](https://arxiv.org/abs/2611.04084)

**한 줄 요약**: SAM3를 고정한 채 참조 이미지에서 카테고리별 텍스트 토큰(약 12K 파라미터)을 역으로 학습해, 시각 매칭 없이 텍스트 조건만으로 cross-domain few-shot segmentation을 하는 RI-SAM3.

**핵심 기여**: SAM 기반 CD-FSS는 참조-대상 시각 매칭이 대상 외형 변화에 민감하고, SAM3의 text-conditioned segmentation에 카테고리 이름을 그대로 넣으면 큰 도메인 변화에서 성능이 불안정하다는 문제의식이다. frozen 텍스트 인코더 앞·뒤에 상보적인 토큰을 학습하는 Bi-level Reference Inversion, decoder 층마다 이 토큰을 다르게 조합하는 Layer-adaptive Textual Conditioning, query confidence와 대상 존재 여부를 함께 지도하는 Presence-aware Confidence Supervision으로 구성된다. 카테고리당 약 12K 파라미터만 최적화하고, 재사용 가능한 텍스트 조건으로 대상마다 forward 한 번에 분할한다. 널리 쓰이는 여러 CD-FSS 벤치마크에서 일관되게 우수한 성능과 효율·일반화를 보고한다.

**코드**: 불명

**태그**: segmentation, peft, foundation-model

---

### [Factorized MLLM Embeddings for Composed Image Retrieval](https://arxiv.org/abs/2611.05193)

**한 줄 요약**: 참조 이미지+수정 텍스트 질의를 MLLM 안에서 분해된 잠재 토큰으로 «목표 이미지를 상상»하게 한 뒤 검색 임베딩을 만드는 composed image retrieval 방법(FactEmbed).

**핵심 기여**: 기존 MLLM 기반 CIR은 합성 질의를 contrastive 지도만으로 바로 임베딩에 사상해, 의도한 시각 수정을 명시적으로 풀지 않으므로 MLLM의 조합 이해력을 덜 쓴다는 문제의식이다. 분해된 잠재(factorized latents)가 중간 목표 상상 목표로 목표 의미에 먼저 접지되게 하고, factor 수준 contrastive loss와 MLLM 깊은 attention 층으로의 증류로 이 표현을 퍼뜨린다. 추론 시에는 [EOS] 토큰으로 전역 임베딩을 만들고, 같은 forward에서 나온 평균 풀링 factor 임베딩으로 짧은 후보 목록을 거의 추가 비용 없이 재정렬한다. 여러 CIR 벤치마크에서 기존 방법을 앞선다고 보고한다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, metric-learning, vlm

---

### [Anchored Rank-Adversarial Fine-Tuning Pretrained Visual Place Recognition Models](https://arxiv.org/abs/2611.05286)

**한 줄 요약**: 공개된 VPR 모델을 listwise rank 적대 손실과 원본 descriptor에 대한 anchor로 미세조정해, 깨끗한 정확도 손실을 미리 정한 예산 안에 묶으면서 검색 순위 공격에 대한 강건성을 올리는 ARAFT.

**핵심 기여**: foundation model 기반 VPR은 도시·계절·조명 변화에는 강하지만, 1/255 예산의 white-box 순위 공격에서 SuperVLAD·BoQ의 top-1 recall이 네 벤치마크에서 최대 0.2%로 떨어진다는 문제의식이다. 적대 질의마다 가장 어려운 positive에 대한 listwise rank loss와, frozen 사전학습 모델의 clean descriptor에 대한 anchor로 미세조정하고, 체크포인트는 미리 고정한 clean 정확도 예산으로 고른다. 검증 R@1 5포인트 이내 비용에서 일반 적대학습은 허용 체크포인트가 없지만, ARAFT는 robust R@1을 SuperVLAD 0에서 47.3, BoQ 0에서 55.3으로 올린다. 4/255에서는 일반 적대학습이 robust R@1을 6~9포인트 앞서고, ARAFT는 clean R@1 약 10포인트 우위를 유지한다. SuperVLAD에서 정한 설정이 BoQ로 재조정 없이 옮겨지며, gradient masking 징후가 없다고 밝힌다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, foundation-model

---

### [Bridging CLIP with DINO: Cross-Modal Information Maximization for Online Test-Time Adaptation](https://arxiv.org/abs/2611.04489)

**한 줄 요약**: 손상된 입력에서 CLIP이 텍스트 앵커로 과신 오분류하는 «modality bias»를, frozen DINOv2 분기와의 logit 앙상블·gated 정보 최대화·online logit 보정으로 완화하는 online TTA 방법(CDIM).

**핵심 기여**: test-time 손상 아래에서 CLIP 시각 인코더가 왜곡된 특징을 틀린 텍스트 앵커에 높은 확신으로 사상하고, entropy minimization이 이 오류를 강화해 예측 분포가 붕괴한다는 문제의식이다. 표현 수준에서는 CLIP 텍스트 prototype을 텍스트 없는 SSL 백본(DINOv2) 특징 공간으로 투영해 cross-covariance logit 앙상블을 만들고, 최적화 수준에서는 표본별 sharpening과 배치 다양성을 짝지은 gated 정보 최대화 목표에 신뢰도 낮은 표본을 gradient에서 빼는 adaptive gate를 둔다. 예측 수준에서는 online logit adjustment로 남은 클래스 분포 치우침을 고친다. ImageNet-C·CIFAR10-C·CIFAR100-C에서 비교한 CLIP 기반 online TTA baseline들을 앞서고, continual·mixed-domain TTA에서도 경쟁력이 있다고 보고한다.

**코드**: 공개([repo](https://github.com/B1ueC1oud/CDIM))

**태그**: ssl-backbone, foundation-model, continual-learning

---

### [SPA-Q: Structure-Preserving Adaptive Post-Training Quantization for Monocular Depth Estimation](https://arxiv.org/abs/2611.04491)

**한 줄 요약**: Depth Anything의 4-bit PTQ에서 query·key 상호작용이 만드는 attention 분포를 보존하고, 층을 거치며 쌓이는 특징 분포 이동을 채널별 affine 변환으로 바로잡는 양자화 방법.

**핵심 기여**: Depth Anything 같은 transformer 기반 단안 깊이 추정 모델은 일반화가 강하지만 연산·메모리 비용이 크고, 저비트 PTQ에서 두 문제가 생긴다는 문제의식이다. 하나는 query·key projection의 양자화 오차를 따로 줄이면 둘의 상호작용으로 생기는 attention map이 보존되지 않는 것이고, 다른 하나는 오차가 층마다 누적되어 중간 특징 분포가 이동하는 것이다. Attention-Preserving Calibration은 full-precision attention 분포에 맞춰 query·key 양자화 파라미터를 정하고, Channel-Wise Distribution Alignment는 채널별 affine 변환을 학습한 뒤 가중치에 흡수해 추론 비용을 늘리지 않는다. 4-bit 양자화에서 NYUv2·KITTI 평균 AbsRel 25.9% 감소, δ1 17.3% 향상으로 기존 PTQ 방법을 일관되게 앞선다고 보고한다.

**코드**: 불명

**태그**: quantization, efficient-inference, depth, foundation-model

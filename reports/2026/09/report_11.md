# arXiv cs.CV Daily Digest — 2026-09-10 (arXiv 공개일)

- **전체 신규 논문 수**: 106편 (new 80 + cross-list 26)
- **선별 수**: 9편

## 오늘의 트렌드

최대 군집은 vision-language model로, 환각 진단·토큰 pruning과 물류·인프라·동작 이해 벤치마크가 몰려 있다. 의료 영상 분할·신뢰도 추정이 두 번째, 단안 3D 재구성·Gaussian Splatting·world model이 세 번째이고 원격탐사 탐지·분류도 크다. 방법론으로는 DINOv3·SAM3·CLIP·VGGT 같은 동결 foundation 표현을 probe·adapter·training-free로 재사용하는 흐름, conformal 기반 선택적 예측, diffusion 합성 데이터 증강이 반복된다.

---

### [RoMa-Ω: What Feed-Forward 3D Models Know About Image Matching](https://arxiv.org/abs/2609.09507)

**한 줄 요약**: feed-forward 3D 재구성 모델의 표현이 이미지 매칭에 무엇을 담고 있는지 세 시나리오로 분석하고, RoMa v2의 DINO 백본을 VGGT-Ω로 교체해 재학습한 dense matcher.

**핵심 기여**: RoMa 같은 matcher는 동결 DINO 특징에 강인성을 의존하는 반면 VGGT 같은 feed-forward 재구성 모델은 대규모 데이터로 dense point map과 카메라 pose를 회귀하며, MASt3R·VGGT-Ω처럼 matching loss까지 도입되면서 두 계열의 경계가 흐려졌다는 점에서 출발한다. (i) patch feature의 zero-shot 매칭, (ii) 3D point 예측의 직접 매칭, (iii) 학습된 표현 위에 full matcher 학습이라는 세 시나리오로 VGGT-Ω·VGGT·π³·DA3를 분석해, 후기 layer의 zero-shot 매칭은 상관 맵이 확산돼 약하지만 linear probing과 full matching pipeline에서는 오히려 후기 layer가 강한 표현을 제공함을 보인다. 학습 없이 raw 예측만으로도 중간 정도의 시점 변화·모달리티 갭에서는 경쟁력 있는 매칭이 가능하나(ScanNet 34.2 AUC@5°) 극단적 조명·모달리티 변화에서는 붕괴한다. 이 분석을 바탕으로 RoMa v2의 DINO를 VGGT-Ω로 바꿔 재학습한 RoMa-Ω는 WxBS mAA@10px 64.8→72.9(+8.1), HardMatch 46.5→50.0, RUBIK AUC@20° 85.6→88.0으로 기존 state-of-the-art matcher를 앞선다.

**코드**: 공개([RoMa-Omega](https://github.com/davnords/RoMa-Omega) · MIT)

**태그**: feature-matching, correspondence, ssl-backbone, foundation-model, 3d

---

### [Cross-Species Animal Re-Identification with Semantic Consistency Learning](https://arxiv.org/abs/2609.09705)

**한 줄 요약**: 종(species) 간 해부 구조가 크게 다른 동물 Re-ID에서, 영역 인식 spectral normalization과 종 간 이웃 모델링으로 외관 변화에 안정적이고 종 간 공유되는 의미 구조를 보존하는 표현을 학습한다.

**핵심 기여**: person ReID는 도메인이 달라도 신체 구조가 비슷하지만 동물은 종마다 해부 구조와 시각 패턴이 크게 달라 공유 대응을 세우기 어렵고, 종 간 학습된 표현이 파편화된 임베딩 공간을 이뤄 cross-species 일반화가 제한된다는 문제를 제기한다. Semantic Consistency Learning(SCL)은 두 요소로 구성되는데, Foreground-Background Decoupled Spectral Normalization(FDSNorm)은 전경·배경을 분리해 환경에서 유도된 스타일 변화를 영역 인식 방식으로 억제하며 특징 통계를 안정화하고, Cross-species Neighborhood Modeling(CNM)은 동적 특징 이웃을 통해 종 간에 전이 가능한 관계 구조를 포착한다. 11개 공개 animal ReID 데이터셋에서 여러 cross-species 평가 프로토콜 전반에 걸쳐 state-of-the-art를 일관되게 앞서고, 학습에 없던 종과 생태 도메인으로도 일반화된다고 보고한다.

**코드**: 공개([ECCV-26-SCL](https://github.com/Kemalau/ECCV-26-SCL))

**태그**: re-identification, metric-learning, image-embedding, fine-grained

---

### [Isotropic Embedding Perturbations for Robust Vision Language Encoders](https://arxiv.org/abs/2609.10292)

**한 줄 요약**: 픽셀 공간 대신 임베딩 공간에 diffusion식 등방성 random perturbation을 alpha-mixing으로 가하는 plug-in 증강 Aether로, vision·vision-language 인코더의 정규화를 강화한다.

**핵심 기여**: RandAug·CutMix·Mixup·RandErase·DropPath 같은 증강은 개별로는 강한 정규화 효과를 내지만 기능이 겹쳐 조합 성능이 포화됐고, 공격적인 픽셀 수준 조작은 섬세한 cross-modal alignment를 깨뜨릴 수 있다는 점을 문제로 삼아 입력 공간이 아닌 임베딩 공간이라는 새 증강 축을 찾는다. Aether는 통제된 alpha-mixing으로 임베딩에 diffusion-style random perturbation을 가해 의미 일관성을 유지하는 등방성 정규화를 제공하며, 언어 모델의 feature-space perturbation과 generative pretraining의 image degradation에서 착안해 vision-language 인코더에 필요한 세밀한 구조 정보를 손상시키지 않는 온화한 교란을 유도한다. 다양한 아키텍처와 여러 인식 과제에서 CutMix·Mixup·DropPath·RandAug를 결합한 고급 recipe 대비 일관된 이득을 보이고, 특히 픽셀 공간 증강이 실패하는 multi-modal alignment에서 효과가 두드러진다고 보고한다.

**코드**: 불명

**태그**: image-embedding, foundation-model, data-augmentation, vlm

---

### [What Makes Adversarial Examples Transfer Across Deepfake Detectors?](https://arxiv.org/abs/2609.10002)

**한 줄 요약**: 백본·사전학습·학습 데이터를 통제한 60개 deepfake 탐지기 사이에서, 전이 기반 black-box 공격의 성공률이 source–target 호환성에 따라 어떻게 달라지는지 측정한 대규모 평가.

**핵심 기여**: deepfake 탐지기는 surrogate에서 만든 adversarial example을 미지의 타깃 모델에 옮기는 전이 공격에 취약하지만, source–target 호환성이 공격 성공을 어떻게 좌우하는지는 기존 연구가 제한된 탐지기 풀만 다루고 아키텍처 요인과 학습 요인을 분리하지 않아 불명확했다. 6개 백본(ResNet34·Xception·EfficientNet-B4·DeiT-S·ViT-B/16·Swin-T), 2개 사전학습(ImageNet·얼굴인식), 5개 학습 데이터 구성(face-swapping·reenactment·entire-face-synthesis·face-editing·전체 합집합)을 조합한 60개 탐지기에 AutoAttack(AA)과 CW–EOT 두 공격을 적용해 짝지은 비교를 수행한다. source와 target이 동일 백본·아키텍처 계열·사전학습·학습 데이터를 공유할 때 전이가 유의하게 높으며, AA에서는 백본 일치 효과가, CW–EOT에서는 사전학습·학습 데이터 공유 효과가 가장 크다. 비타깃 source 전반 평균 ASR은 AA 7.21%, CW–EOT 19.52%인 반면 두 공격을 결합한 multi-source oracle은 백본·학습 데이터 일치를 제외해도 64.48%에 달해, source 평균이 타깃 취약성을 크게 과소평가함을 보인다. 교란 이미지 24만 장, 전체 pairwise 전이 결과, 탐지기 설정, 평가 코드를 공개한다고 밝힌다.

**코드**: 공개 예정 (본문에 double-blind 리뷰 종료 후 코드·벤치마크 자원 공개를 명시)

**태그**: forgery-detection, adversarial-robustness, dataset-benchmark

---

### [Hyperbolic Geometry for Open-World Object Detection in Remote Sensing Imagery](https://arxiv.org/abs/2609.09626)

**한 줄 요약**: 원격탐사 open-world object detection에 hyperbolic geometry를 도입해, 임베딩 반지름을 불확실성 단서로 미지 객체를 찾고 hyperbolic metric learning으로 증분 학습 시 망각을 완화한다.

**핵심 기여**: open-world object detection(OWOD)은 미지 객체를 식별하고 주석이 확보되면 증분 학습해야 하는데, 원격탐사 객체 범주는 잠재 계층 관계를 갖는 반면 기존 방법이 쓰는 Euclidean 공간은 이를 충분히 표현하지 못해 unknown recall과 증분 학습 성능이 제한된다고 지적한다. HyRS-OWOD는 두 단계 미지 객체 발견 기제를 두는데, Decoupled Objectness Learning(DOL)이 전경 지각을 의미 정보에서 분리해 전경 proposal을 배경에서 떼어내고, Hyperbolic Uncertainty Learning(HUL)이 hyperbolic 임베딩의 반지름을 known–unknown 판별용 불확실성 단서로 활용한다. 증분 학습에는 클래스 간 분리성을 높이는 Hyperbolic Metric Learning(HML)을 두어 새 범주를 편입하면서 catastrophic forgetting을 완화한다. 3개 원격탐사 벤치마크에서 state-of-the-art OWOD 대비 unknown recall과 증분 학습 성능이 일관되게 향상됐다고 보고한다.

**코드**: 불명

**태그**: object-detection, continual-learning, metric-learning, open-set-recognition

---

### [Distilling Image Prototypes for Guided Test-Time Adaptation](https://arxiv.org/abs/2609.09737)

**한 줄 요약**: 소량의 합성 이미지로 증류한 Distill Image Prototype을 source 지식의 재생성 가능한 anchor로 삼아, test-time adaptation의 pseudo-label 오류 누적과 catastrophic forgetting을 함께 억제한다.

**핵심 기여**: test-time adaptation(TTA)은 noisy pseudo-label로 인한 오류 누적과 source 지식의 파국적 망각이라는 두 난점을 안고 있는데, 불확실성 기반 접근은 과신하거나 계산 비용이 크고 prototype replay는 정적 표현이 모델 적응에 따라 어긋난다고 지적한다. DIPTTA의 핵심은 source 지식의 동적·재생성 anchor 역할을 하는 compact 합성 이미지 집합 Distill Image Prototype(DIP)으로, 현재 모델 상태에 맞춘 feature prototype을 계속 생성하는 dynamic feature replay로 망각을 막고, DIP를 기준으로 한 source-calibrated uncertainty estimation으로 덜 편향된 샘플 신뢰도를 얻어 오류 누적을 억제한다. 여러 벤치마크에서 state-of-the-art를 크게 앞서며 특히 심한 도메인 shift에서 격차가 두드러진다고 보고한다.

**코드**: 공개([DIPTTA](https://github.com/LiwenWang919/DIPTTA))

**태그**: continual-learning, test-time-adaptation, calibration, distillation

---

### [Low-Rank Prompt Learning for Vision-Language Models with Fixed-Token Bases](https://arxiv.org/abs/2609.09462)

**한 줄 요약**: CoOp의 dense prompt 행렬을 P=BA로 저랭크 분해하고 토큰 쪽 인자 B를 무작위 basis로 고정해도, 임베딩 쪽 인자 A만 학습하면 few-shot 성능이 유지된다.

**핵심 기여**: Context Optimization(CoOp)은 클래스당 소수 예시로 m×d 크기의 dense prompt 행렬을 학습하는데, 이 행렬이 과매개화돼 있는지를 묻는다. P=BA 분해로 학습 파라미터를 md에서 r(m+d)로, 토큰 쪽 인자 B를 고정하면 rd로 줄이고, 7개 few-shot 벤치마크와 2개 CLIP 백본에서 저랭크 prompt가 dense CoOp와 동등하거나 더 나으며 low-shot base-to-new 일반화에서 이득이 가장 뚜렷함을 보인다. 이어서 B는 학습할 필요조차 없어 Gaussian·orthogonal·SVD 유도·무작위 basis로 고정하고 A만 학습해도 완전 학습 분해와 동등하며, source에서 학습한 B가 무작위 B보다 낫지 않음을 확인한다. prompt-factor 비대칭과 local update-space dimension gap으로 B 고정이 A 고정보다 훨씬 덜 제약적인 이유를 설명하고, smoothness만 가정한 수렴 보증을 제시한다.

**코드**: 불명

**태그**: peft, foundation-model, vlm, few-shot

---

### [Layerwise Tunable Lifting Scheme for the Convolutional Neural Network](https://arxiv.org/abs/2609.09827)

**한 줄 요약**: biorthogonal wavelet filter bank의 lifting 단계를 학습 가능한 lattice 구조로 만들어 CNN에 넣는 세 가지 tunable lifting scheme으로, 텍스처 분류와 MVTec-AD 이상탐지에서 성능을 높인다.

**핵심 기여**: low-pass를 조정하는 LS-LayLatt-LP, high-pass를 조정하는 LS-LayLatt-HP, 저주파·고주파 branch를 순차적으로 함께 적응시키는 LS-LayLatt-Sequential의 세 lifting 전략을 제안한다. 모두 lattice 기반 lifting 구조로 정식화해 lifting 함수의 파라미터가 어떤 값을 갖더라도 가역성과 안정성이 보장된다. ResNet-18 백본에 통합해 Describable Textures Dataset(DTD) 분류, MVTec-AD hazelnut 이미지와 비공개 KRC102S 데이터셋의 이상탐지에서 평가했으며 모든 과제에서 일관된 성능 향상을 보고한다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, defect-detection, frequency-domain

---

### [UOT-Gap: A Variational Principle for the Modality Gap in Vision-Language Models via Unbalanced Optimal Transport](https://arxiv.org/abs/2609.10224)

**한 줄 요약**: 동결 CLIP 계열 임베딩의 modality gap을 unbalanced entropic optimal transport로 분해하는 training-free 진단으로, 쌍 인식 residual이 검색 성능 저하를 평균 gap보다 훨씬 잘 추적한다.

**핵심 기여**: CLIP 같은 모델은 이미지와 텍스트를 공유 공간에 임베딩하지만 모달리티별 분포가 분리돼 남는데, 기존 설명은 초기화·contrastive dynamics·정보 불균형에 연결하면서도 분포 수준과 쌍 수준 기여가 검색에 어떤 영향을 주는지는 풀지 못했다고 본다. UOT-Gap은 동결 이미지·텍스트 임베딩을 unbalanced entropic optimal transport(UOT)로 모델링해 최적해에서 transport·coupling complexity·marginal mass variation을 분리하고, 관측된 이미지–캡션 쌍을 UOT soft matching과 비교하는 pair-aware residual을 더한다. Flickr8K·COCO-1K에서 동결 CLIP·OpenCLIP·SigLIP으로 캡션을 열화시키면 Flickr8K Recall@1이 0.559에서 0.003으로 떨어지는데, 6개 데이터셋–모델 조건에서 pair-aware residual은 평균 절대 Spearman 0.973으로 검색 저하를 추적하는 반면 mean gap은 0.392에 그치고, COCO-1K 무작위 부분집합 5개에서도 0.954±0.026(최소 0.943)으로 안정적이다. UOT barycentric update는 transport 목적함수를 줄이면서도 검색을 악화시켜 기하 목적의 감소와 과제 개선이 다름을 보인다.

**코드**: 불명

**태그**: image-embedding, image-retrieval, training-free, vlm

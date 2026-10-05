# arXiv cs.CV Daily Digest — 2026-10-05 (arXiv 공개일)

- **전체 신규 논문 수**: 128편 (new 99 + cross-list 29)
- **선별 수**: 11편

## 오늘의 트렌드

비디오 생성·월드 모델과 VLA·로봇 정책이 가장 두꺼운 군집을 이루고, 3D Gaussian Splatting·메시 편집 등 3D 재구성, VLM 내부 표현 분석·스트리밍 추론, 확산 모델 샘플링 가속(캐싱·솔버·few-step 증류)이 그 뒤를 잇는다. 방법론으로는 DINOv3·SigLIP2 등 동결 파운데이션 모델을 다중 교사로 증류·정렬해 단일 백본에 모으는 흐름과, 사전학습 가중치를 고정한 채 소수 어댑터만 학습하는 training-light 적응이 여러 과제에서 반복된다.

---

### [GRAFT: Growing Agglomerative Foundation Models via Continual Teacher Distillation](https://arxiv.org/abs/2610.02597)

**한 줄 요약**: DINOv2·Multi-HMR·MASt3R·SigLIP2를 순차적으로 증류해 단일 ViT-B/14 백본에 능력을 누적하는 continual multi-teacher distillation 프레임워크.

**핵심 기여**: 다중 교사 증류로 여러 파운데이션 모델을 하나의 agglomerative 백본에 통합할 수 있지만 교사 집합이 고정돼 있어 새 교사를 추가하려면 전체 교사에 대한 공동 증류를 반복해야 한다는 문제를 다룬다. GRAFT는 새 교사가 도착하면 이전까지 증류된 모델을 기존 능력 보존용 교사로 삼아 현재 학생이 이전 모델과 새 교사 모두에서 학습하게 하고, 교사마다 공유 인코더의 독립 read-out을 주는 Teacher Specific Readout Tokens와 vision-language 교사를 원시 특징값이 아니라 이미지–텍스트 유사도 구조로 맞추는 Geometry Agnostic Relational Loss로 이질적 표현 기하를 조정한다. 448px ViT-B/14 학생이 DINOv2 → Multi-HMR → MASt3R → SigLIP2 순으로 증류돼 ImageNet-1K 81.1, ADE20K mIoU 46.0, 3D human pose F1 89, COCO 검색 T→I/I→T 52.3/69.7을 기록했으며, 새 능력마다 전체 재증류 없이 1회 증류 비용만 든다. 교사 대비 잔여 격차가 세밀한 포즈 정밀도에 집중되고, 비교 대상과 교사 수·규모·학습 코퍼스가 달라 엄밀한 동일 조건 비교는 아니라고 밝힌다.

**코드**: 불명

**태그**: ssl-backbone, foundation-model, distillation, continual-learning, image-embedding

---

### [ViTok: Improving Dense Semantics in AM-RADIO-Style Multi-Teacher Distillation with PHI-S and Masked Image Modelling](https://arxiv.org/abs/2610.02903)

**한 줄 요약**: SigLIP2와 DINOv3-L을 교사로 하는 AM-RADIO식 ViT-B 다중 교사 증류에서 전역 인식과 조밀 의미를 함께 지키기 위한 레시피 변경과 실패 사례를 정리한 보고.

**핵심 기여**: 같은 증류 레시피가 모든 목적을 고르게 최적화하지 못해 ImageNet-1K kNN 정확도를 올리는 변경이 ADE20K 분할을 떨어뜨릴 수 있다는 점을 중심 문제로 둔다. CLS·패치 토큰용 adaptor head 분리, 비대칭 cosine/MSE 손실, DINOv3-L 체크포인트 초기화, 교사 재가중, masked image modeling, PHI-S 특징 균형화를 순차적으로 더해 그 trade-off를 드러내고 다룬다. 결과 모델은 ImageNet-1K에서 patch kNN 83.2·CLS kNN 85.2로 DINOv3-L 교사(79.7/85.0)를 근소하게 넘겼고, PHI-S가 ADE20K를 46.5/58.1에서 48.5/61.0 mIoU/mAcc로 회복시켜 교사와 같은 수준이 됐다. ImageNet-22K로 증류 데이터를 키워도 일관된 이득이 없고 SAM3·HOG 같은 교사를 단순 추가하면 간섭이 생긴다는 부정적 결과를 함께 보고하며, 평가가 linear-probe 분할과 kNN 분류에 한정돼 검출·깊이 같은 downstream은 다루지 않았다고 밝힌다.

**코드**: 불명

**태그**: ssl-backbone, distillation, foundation-model, image-embedding, segmentation

---

### [Less Decoder is More Encoder: Geometric Representation Learning from Novel View Synthesis](https://arxiv.org/abs/2610.03717)

**한 줄 요약**: 디코더 표현력을 제한하고 잠재 공간 재구성을 목표로 삼아 novel view synthesis로 전이 가능한 기하 표현을 학습하는 자기지도 인코더-디코더 트랜스포머 SNAP.

**핵심 기여**: NVS는 원리상 3D 장면 구조를 추론해야 하므로 전이 가능한 다시점 기하 표현을 낳아야 하지만, 기존 인코더 기반 NVS는 공간적으로 표현력이 큰 디코더가 장면 인코더의 표현 능력을 희석하고 저수준 픽셀 공간 타깃이 특징 학습을 방해해 표현이 빈약하다고 진단한다. SNAP은 수용 영역 1×1의 포즈 조건 국소 디코더와 동결 DINOv3 ViT-B 특징을 타깃으로 하는 잠재 공간 재구성 목적으로 이를 해결하며, 16층 인코더를 RealEstate10K·DL3DV·Co3Dv2 약 11.7만 시퀀스(256×256)로 4만 스텝 학습했다. 시각 위치추정·포즈 추정·점 대응·깊이 추정·로봇 조작 다섯 과제에서 기하 지도학습 방법 및 자기지도 표현과 경쟁했고, RealEstate10K 점 대응 PCK@5/10px 15.48/36.29로 VGGT(12.85/32.78)를 앞섰으며, 패치 특징에 강한 지도학습 모델에 근접하는 시점 불변성이 나타나 카메라 이동 아래 2D 표현이 무너지는 상황에서 더 완만하게 성능이 떨어진다. 사전학습이 포즈가 있는 정적·질감 장면 비디오에 의존하고 고정 연산·데이터 예산 안에서 스케일링 법칙은 확인하지 못했다고 밝히며, 프로젝트 페이지가 공개돼 있다.

**코드**: 불명

**태그**: ssl-backbone, correspondence, image-embedding, 3d, depth

---

### [Decoding the Functional Roles of Register and High-Norm Patch Tokens in Vision Transformers](https://arxiv.org/abs/2610.03698)

**한 줄 요약**: DINOv2의 register 토큰과 high-norm outlier 패치 토큰 활성에 sparse autoencoder를 학습해 두 토큰의 의미적·기능적 역할 차이를 분석한 연구.

**핵심 기여**: 자기지도 ViT가 배경 영역에서 만드는 high-norm outlier 패치 토큰을 줄이려고 register 토큰이 도입됐지만, 두 토큰 유형의 의미·기능은 충분히 규명되지 않았다는 문제의식에서 출발한다. DINOv2의 register 토큰과 outlier 토큰 활성에 각각 SAE를 학습하고 자동 해석 파이프라인·UMAP 군집화·CLIP 공간 교차 검증으로 특징을 해석했다. register 토큰 특징은 고수준 의미 개념과, outlier 토큰 특징은 저수준 구조·배경·질감 위주 패턴과 더 강하게 연결됐고, 인과 절제에서 상위 활성 register 유래 특징을 교란하면 표현 cosine 유사도가 48.17% 떨어지는 반면 outlier 유래 특징 교란은 0.31%만 떨어져 큰 기능적 비대칭을 보였다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, interpretability

---

### [Geometry-Aligned Semantic Matching for Cross-Modal Planar Image Registration](https://arxiv.org/abs/2610.03167)

**한 줄 요약**: 기하 일관 cross-modal 패치 쌍으로 DINOv3를 점진 적응시키고 DINO 중심 특징 피라미드에 경량 CNN 가지를 붙여 교차 모달 평면 정합용 대응을 추정하는 매처 CDPM.

**핵심 기여**: 의미 표현은 모달리티 간 일관성을 주지만 의미 유사도가 기하 대응을 보장하지 않고, 세밀한 CNN 특징은 국소 정밀도는 높지만 안정적 정제를 이끌 전역 의미 안내가 없다는 문제를 다룬다. CDPM은 기하적으로 일관된 cross-modal 패치 쌍으로 DINOv3를 점진 적응시켜 특징 유사도가 실제 교차 모달 공간 대응을 반영하게 하고, 다중 스케일 DINO 표현이 안정적 대응을 유지하며 경량 CNN 가지가 보조 구조 세부를 주는 DINO-Centric Feature Pyramid로 정밀 국소 정제를 수행한다. 세 교차 모달 데이터셋에서 VIS-IR 기준 dense matcher RoMa 대비 AUC@3/5/10/20이 7.36/13.40/13.75/10.42%p 오르고 mACE가 5.83에서 2.78픽셀로 줄었으며, RoMa v2보다 모든 지표에서 앞서면서 FLOPs는 45.6% 적다. 온라인 데모와 PCB-Layout 데이터셋이 Hugging Face에 공개돼 있다.

**코드**: 공개([CDPM](https://github.com/warren-wzw/CDPM))

**태그**: feature-matching, correspondence, ssl-backbone, cross-modal

---

### [Revisiting Visual Representation Enhancement of VLMs via Kernel Canonical Correlation Analysis](https://arxiv.org/abs/2610.02718)

**한 줄 요약**: CLIP 이미지 인코더를 DINOv2·텍스트 인코더와 Kernel CCA로 부분공간 정렬해 fine-grained 시각 인식을 높이면서 zero-shot 검색을 유지하는 3-view 정렬 기법 3vKCCA.

**핵심 기여**: CLIP은 의미 일반화는 강하지만 fine-grained 시각 인식이 약하고, DINOv2와 커널 행렬을 원소별로 맞추는 기존 KUEA는 정렬 손실 비중을 줄여도 성능이 꼭 떨어지지 않아 커널 행렬 불일치만으로는 추가 개선이 어렵다는 관찰에서 출발한다. 저자들은 투영 상관을 최대화하는 KCCA로 특징 부분공간 위 표현 정렬을 정식화하고, KKT 조건에 기반해 고유값 문제를 피하는 end-to-end 학습 방식을 유도했으며, 사전학습 텍스트 인코더의 투영까지 넣은 3-view 공동 정렬 3vKCCA로 확장했다. CLIP ViT-L/14를 ImageNet-1K로 미세조정해 MMVP-VLM 정확도를 17.8에서 25.9로 올려 DIVA보다 2.9, KUEA보다 5.2점 높았고, zero-shot 이미지–텍스트 검색 집계 점수는 72.7에서 73.3으로, 9개 데이터셋 zero-shot 분류 평균은 68.08 대비 68.06으로 유지됐다. 연구가 CLIP–DINOv2 조합에 한정돼 다른 VLM 백본·교사·벤치마크는 향후 과제로 남긴다.

**코드**: 불명

**태그**: image-embedding, fine-grained, foundation-model, vlm, distillation

---

### [LAS-CLIP: A Lightweight Adapter Steering Approach for CLIP's Visual Encoder](https://arxiv.org/abs/2610.03370)

**한 줄 요약**: CLIP을 완전히 동결한 채 입력 마스크로부터 층·헤드별 어텐션 바이어스를 생성해 영역 수준 표현을 뽑는 약 12만~15만 파라미터 어댑터.

**핵심 기여**: CLIP 비전 인코더는 전역 표현만 내놓아 영역 수준 과제에 쓰기 어렵고, 기존 적응법(visual prompting·입력 마스킹·인코더 미세조정)은 사전학습 표현을 훼손한다는 문제를 다룬다. LAS-CLIP의 MaskAdapter는 입력 마스크에서 층별·헤드별 어텐션 바이어스를 만들어 동결 self-attention에 주입해 어텐션을 대상 영역으로 유도하며, 백본을 전혀 건드리지 않으므로 마스크가 없으면 원래 CLIP으로 그대로 돌아가 zero-shot 능력이 보존된다. 약 116K~145K 학습 파라미터와 10만 샘플, T4 GPU 2장으로 학습해, 인코더 전체를 수백만 샘플로 미세조정한 Alpha-CLIP과 ImageNet-S zero-shot 분류·RefCOCO 지시 표현 이해에서 대등하거나 우세했고, 잘못된 마스크 아래에서나 downstream 생성에서 표현 충실도가 더 높았다고 보고한다. ViT-B/16·ViT-L/14용 어댑터 체크포인트가 공개돼 있다.

**코드**: 공개([lasclip](https://github.com/AnhKhoa585/lasclip) · MIT)

**태그**: peft, foundation-model, image-embedding, segmentation, vlm

---

### [VisionMX: Unlocking Microscaling Post-Training Quantization for Vision Models](https://arxiv.org/abs/2610.03218)

**한 줄 요약**: Microscaling(MX) 포맷으로 비전 모델을 직접 변환할 때의 오차 원인 세 가지를 분석하고, 제한 가중치 반올림 최적화와 접어 넣을 수 있는 affine 활성 보정으로 W4A4 성능을 회복하는 post-training 양자화 기법.

**핵심 기여**: 저정밀 원소와 블록 공유 스케일을 결합한 MX 포맷은 하드웨어 지원이 확산되고 있지만 비전 모델에 미치는 영향은 거의 조사되지 않았다는 점에서 출발한다. 직접 변환 분석으로 블록 스케일 표현, 일부 작은 합성곱 가중치 텐서와 비균일 원소 격자의 부정합, 비음수 활성이 부호 코드를 활용하지 못하는 문제 세 가지를 오차 원인으로 짚고, 이를 바탕으로 bounded weight rounding 최적화와 추론 그래프에 접어 넣을 수 있는 활성 affine 보정을 제안한다. MobileNetV2·ResNet-18·ConvNeXt-T·DeiT-B·Swin-T 등 분류 모델과 Faster R-CNN·RetinaNet·FCOS 검출, DeepLabV3 분할, 저조도 향상에서 MXFP4-UE8M0·MXFP4-UE5M3·NVFP4 포맷으로 평가해, W4A4 직접 변환 시 0.40%로 붕괴하던 MobileNetV2 ImageNet 정확도를 65.48%로, Faster R-CNN R50-FPN COCO AP를 24.50에서 33.15로 회복시켰고 MX 변환에 민감한 구조일수록 회복 폭이 컸다. 분석이 충분히 작은 섭동과 Hessian 기반 근사를 가정해 큰 양자화 오차나 비평활 활성 경계에서는 성립하지 않을 수 있다고 밝힌다.

**코드**: 불명

**태그**: quantization, efficient-inference, object-detection, segmentation

---

### [FUSEye: Training-Light Fisheye Detection with Overlapping Views and Zero-Initialized Adapters](https://arxiv.org/abs/2610.02799)

**한 줄 요약**: 동결 백본 COCO 사전학습 YOLO26-x에 겹치는 격자 뷰 생성·zero-initialized 잔차 어댑터·교차 투영 합의 융합을 더해 약 22.7만 파라미터로 fisheye 검출기로 바꾸는 프레임워크.

**핵심 기여**: fisheye 카메라는 강한 방사 왜곡이 국소 구조를 비틀고 경계 압축이 객체를 거의 보이지 않을 만큼 줄여 COCO 사전학습 검출기가 실패하며, 완전 미세조정은 많은 fisheye 라벨과 연산을 요구한다는 문제를 다룬다. FUSEye는 입력 수준에서 겹치는 격자 뷰 생성과 박스 재매핑(GridViews)으로 압축된 경계 영역을 확대하고, 특징 수준에서 zero-initialized 잔차 어댑터(Z-Adapters)로 왜곡에 의한 특징 부정합을 보정하며, 결정 수준에서 학습된 교차 투영 합의 융합(AgreeFusion)으로 여러 뷰에서 일관된 근거가 있을 때만 저신뢰 검출을 승격시킨다. WoodScape에서 YOLO26-x mAP50을 0.148에서 0.266으로 올려 완전 미세조정 정확도의 84.3%를 유지했고, 라벨 이미지 25%만으로 0.2597 mAP50을 얻어 전체 라벨 성능의 97.6%를 유지했으며 YOLOv8~11에서도 일관되게 개선됐다.

**코드**: 공개 예정

**태그**: object-detection, peft, domain-adaptation, efficient-inference

---

### [Interpretable Deepfake Detection in Videos via Explicit Forensic Features and Temporal Modeling](https://arxiv.org/abs/2610.03380)

**한 줄 요약**: 얼굴 궤적의 프레임마다 photometric·textural·geometric·compression 4개 영역의 68개 명시적 포렌식 기술자를 뽑아 LSTM으로 시간 불일치를 잡는 해석 가능한 비디오 딥페이크 탐지 프레임워크.

**핵심 기여**: 조작 영상은 프레임 수준에서는 시각적으로 일관돼 보이면서 미묘한 시간적 불일치를 보이는데, 암묵적 표현에 의존하는 end-to-end 모델은 분석이 불투명하다는 문제를 다룬다. 파이프라인은 영상을 신원 일관 얼굴 궤적으로 변환해 고정 길이 시간 창으로 나누고, 각 프레임을 photometric·textural·geometric·compression 4개 영역의 68개 구조화 기술자로 표현한 뒤 LSTM으로 시간 의존성과 불규칙성을 포착한다. FaceForensics++·Celeb-DF v2·DFDC 큐레이션 부분집합·DeeperForensics에서 F1 98.0%·91.0%·97.6%·96.2%를 보고했고, 교차 데이터셋 일반화도 양호했다고 밝힌다.

**코드**: 불명

**태그**: forgery-detection, video, interpretability, hand-crafted-features

---

### [When Predicting Nothing Beats SAM 3: Revisiting Evaluation in Video Object Segmentation](https://arxiv.org/abs/2610.02946)

**한 줄 요약**: 대상이 간헐적으로만 보이는 긴 영상에서 표준 J&F가 부재 분류로 붕괴해 빈 마스크 예측기가 SAM 3를 이기는 현상을 보이고, 시공간 볼륨으로 평가하는 Volumetric J&F와 벤치마크 FaVOS를 제안.

**핵심 기여**: 기존 VOS 벤치마크는 영상 대부분에서 보이는 시간적으로 두드러진 객체에 집중해, 긴 영상에서 대상이 간헐적으로만 나타나는 상황을 평가하지 못한다고 지적한다. 낮은 시간 가시성 조건의 벤치마크 FaVOS를 구성해 표준 J&F가 대상 부재 프레임에서 빈 예측에 높은 보상을 줘 평가가 부재 분류로 붕괴함을 보였고, FaVOS-20에서 빈 마스크 예측기가 프레임 단위 J&F 80.0으로 SAM 3(78.7)를 앞섰다. 마스크 시퀀스를 시공간 볼륨으로 평가해 부재 보상의 지배력을 줄이면서 분할 품질·시간 구조 민감도는 유지하는 Volumetric J&F를 제안했으며, 이 지표에서는 SAM 3가 FaVOS-20 56.0, FaVOS-40 72.7을 기록하고 빈 예측기는 0.0이 된다. 데이터셋은 프로젝트 페이지에 공개 예정으로 표시돼 있다.

**코드**: 공개([FaVOS](https://github.com/AIDASLab/FaVOS))

**태그**: segmentation, video, dataset-benchmark, evaluation-protocol, foundation-model

---

# arXiv cs.CV Daily Digest — 2026-09-09 (arXiv 공개일)

- **전체 신규 논문 수**: 359편 (new 301 + cross-list 58)
- **선별 수**: 12편

## 오늘의 트렌드

가장 큰 축은 vision-language model로, 공간·물리 추론 벤치마크와 토큰 압축·KV 캐시 효율, 환각·jailbreak 안전성 진단이 몰려 있다. 3D·4D 재구성과 Gaussian Splatting, embodied world model이 두 번째 군집이고 의료 영상 분할·정합, 비디오 생성·편집도 크다. 방법론에서는 SAM3·DINOv3·CLIP 같은 동결 foundation 표현을 프롬프트·경량 어댑터·training-free 보정으로 도메인에 옮기는 흐름, 합성 데이터와 불확실성 기반 신뢰도 추정이 반복된다.

---

### [Back to the Feature: Zero-Shot 6DoF Pose Estimation via Dense Local Features](https://arxiv.org/abs/2609.06726)

**한 줄 요약**: 동결 DINOv3 하나만 사전학습 요소로 쓰는 학습 불필요 zero-shot 6DoF pose 추정으로, dense patch feature 위에서 고전적 local feature matching 패러다임을 되살린다.

**핵심 기여**: 처음 보는 객체의 6DoF pose를 RGB 이미지만으로, 과제별 미세조정 없이 추정하는 문제를 다룬다. 파이프라인 안의 유일한 사전학습 요소로 동결된 DINOv3 vision transformer를 두고 dense patch-level feature를 뽑아 synthetic-to-real 도메인 갭을 넘으며, 세 가지 구성 요소를 더한다. geodesic non-maximum suppression으로 시점이 다양한 템플릿 집합을 검색해 coarse-to-fine correspondence matching에 쓰고, Render-guided Re-Correspondence(RRC)는 추정된 pose에서 객체별 뷰를 합성해 dense 2D-3D 대응을 다시 세워 초기 추정을 다듬으며, multi-mask hypothesis selection은 경쟁하는 분할 후보를 함께 점수화해 분할 모호성을 해소한다. BOP 벤치마크의 7개 코어 데이터셋에서 refinement 없이 mean AR 40.7, refinement 포함 56.4를 기록해 training-free RGB 방법 중 최고 성능이며 GigaPose·GenFlow 같은 학습 기반 방법도 앞선다고 보고한다.

**코드**: 불명

**태그**: feature-matching, correspondence, ssl-backbone, training-free, pose

---

### [Radiation, Rotation and Scale Invariant Feature Descriptor for Multimodal Image Matching](https://arxiv.org/abs/2609.06343)

**한 줄 요약**: keypoint 이웃을 Cartesian과 Log-Polar로 동시 샘플링하고 교차모달 생성 재구성 제약을 걸어, 회전·스케일·비선형 방사 차이에 강인한 멀티모달 매칭용 특징 descriptor.

**핵심 기여**: 멀티모달 이미지 매칭이 기하 왜곡과 비선형 radiometric difference(NRD)로 크게 흔들린다는 문제를 제기한다. dual-head regional sampling(DHRS) 모듈이 keypoint 이웃에 Cartesian·Log-Polar 샘플링을 동시에 수행해 공간 구조를 유지하면서 회전·스케일 변화에 대한 강인성을 높이고, intra-modal·dual-head·inter-modal 영역에 걸쳐 기하 관계와 방사 관계를 하나의 심층 특징 공간에서 인코딩·상호작용·융합한다. 학습 시에는 양방향 교차모달 생성 재구성 제약을 두어 암묵 특징을 상대 모달리티의 구조 패치로 디코딩하게 하고, 이로써 추론 비용 증가 없이 modality-invariant 기하 topology를 고정한다. optical-infrared와 optical-SAR 데이터셋에서 경쟁력 있는 매칭 성능과 함께 0~360도 전 회전 범위, 최대 4배 스케일 변화를 지원하며 컴퓨터 비전·원격탐사·의료 영상의 멀티모달 이미지로도 일반화를 확인했다.

**코드**: 공개 예정([RRSI](https://github.com/yeyuanxin110/RRSI))

**태그**: feature-matching, correspondence, image-embedding

---

### [What Does Animal Re-Identification Learn? Linear Biological Concepts and Their Origins in Visual Representations](https://arxiv.org/abs/2609.06020)

**한 줄 요약**: triplet loss로 미세조정한 DINOv3 Re-ID 표현 안에 성별·연령이 선형 방향으로 나타나며, 그 방향이 예측에 인과적으로 쓰인다는 것을 activation steering으로 보인다.

**핵심 기여**: metric learning 목적함수는 생물학적 개념을 명시적으로 감독하지 않는데, ViT 기반 Re-ID 모델이 그럼에도 의미 있는 축을 따라 표현을 조직하는지 묻는다. 서부로랜드고릴라 Re-ID용으로 triplet-margin loss로 미세조정한 DINOv3 백본에서 성별과 연령이 held-out 개체까지 일반화되는 선형 방향으로 나타나 최대 0.91 AUROC에 이르고, 개체당 이미지 한 장에서도 복원된다. activation steering으로 성별 방향에 개입하면 상당 비율의 예측이 반대 성별로 뒤집혀 모델이 이 방향을 인과적으로 사용함이 확인되고, off-the-shelf 백본과 미세조정 백본을 비교하면 Re-ID 학습이 이 개념을 새로 만드는 것이 아니라 네트워크 안에서 위치를 옮긴다. data attribution 분석은 이 표현이 개체군 전반에 중복 부호화되고 시각적으로 모호한 개체에 의해 형성되는 점진적 축임을 보인다.

**코드**: 불명

**태그**: re-identification, ssl-backbone, metric-learning, fine-grained

---

### [TRAIL: Trajectory-Aware Visual Place Recognition against Unordered Databases](https://arxiv.org/abs/2609.07373)

**한 줄 요약**: 질의 시퀀스의 시각 유사도와 카메라 운동 일관성을 CRF로 결합해, 순서 구조가 없는 참조 데이터베이스에 대해 마지막 질의 이미지를 정합하는 VPR 후처리 계층.

**핵심 기여**: 기존 visual place recognition은 각 질의 이미지를 고립적으로 다뤄 실제 궤적이 담고 있는 순차 맥락을 버리며, 특징이 빈약한 환경에서 취약하다는 점을 지적한다. 질의 시퀀스가 주어졌을 때 순서 구조를 요구하지 않는 참조 데이터베이스에 대해 마지막 이미지를 정합하는 과제를 정식화하고, 시각 유사도와 카메라 운동 일관성에 대한 학습된 함수들을 conditional random field로 결합해 질의가 하나씩 도착할 때마다 후보 참조에 대한 분포를 정제하는 TRAIL을 제안한다. 사전학습된 임의의 VPR 백본 위에 얹는 경량 후처리 계층으로, 주 벤치마크에서 state-of-the-art baseline 대비 최대 8.3%p 향상하고 재학습 없이 처음 보는 데이터셋으로 전이되며 시각 단서가 부족할수록 이득이 커진다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, correspondence

---

### [TeMo: Temperature Modulation for Multimodal Contrastive Learning](https://arxiv.org/abs/2609.07540)

**한 줄 요약**: 대조학습의 temperature를 고정값이나 전역 학습값 대신 positive-negative 쌍의 유사도에 따라 조절하는 멀티모달 대조학습 프레임워크.

**핵심 기여**: temperature 하이퍼파라미터 τ는 negative 샘플에 가해지는 penalty 강도를 좌우하는 핵심 요소인데도 대부분의 방법이 이를 고정하거나 전역값 하나만 학습한다는 점을 문제로 삼는다. TeMo는 각 positive-negative 쌍의 유사도에 따라 temperature를 적응적으로 조정하는 유사도 기반 modulation을 도입해 더 세밀한 멀티모달 대조학습을 가능하게 하고, temperature가 조절된 멀티모달·단일모달 손실을 표준 멀티모달 대조 손실과 점진적으로 전환하며 결합해 학습 단계에 따라 거친 의미와 세밀한 의미를 함께 포착하도록 설계했다. 다양한 zero-shot 검색·분류 과제에서 각 구성 요소가 일관되게 성능을 높인다고 보고한다.

**코드**: 불명

**태그**: metric-learning, image-retrieval, image-embedding, foundation-model

---

### [Bigger Text Encoders Can Hurt CLIP Zero-Shot Performance](https://arxiv.org/abs/2609.05730)

**한 줄 요약**: CLIP의 vision·text 인코더 용량 배분을 분리해 학습하면 대부분의 vision 인코더에는 그 이상 키울수록 zero-shot 성능이 떨어지는 최적 text 인코더 크기가 존재한다.

**핵심 기여**: 기존 scaling law 연구가 CLIP 전체 모델 크기를 단일 변수로 다뤄 두 인코더 사이의 용량 배분이 downstream 성능에 미치는 영향을 보지 않았다는 점을 지적한다. vision·text 인코더 크기를 달리한 여러 CLIP을 학습해, 총 파라미터 수가 늘어나는데도 zero-shot 성능이 떨어지는 지점이 대부분의 vision 인코더에서 존재함을 확인하고, 이 성질을 이용해 표준 ViT-B/16과 동등한 zero-shot 성능을 최대 55% 적은 파라미터로 내는 구성을 얻는다. 성능 저하가 과대한 text 인코더로 인한 overfitting에서 비롯되며 modality별 weight decay 계수를 쓰면 저하된 모든 구성에서 회복을 넘어 개선된다는 것, 그리고 기하 분석에서 text 인코더 확대가 embedding uniformity는 높이되 cross-modal alignment는 악화시키는 trade-off가 있고 두 지표가 zero-shot 성능을 예측한다는 것을 함께 보인다.

**코드**: 불명

**태그**: image-embedding, metric-learning, foundation-model

---

### [Compensating for Scarce Historical Images in Cross-Domain Cultural Heritage Retrieval Using Synthetic Aging](https://arxiv.org/abs/2609.08766)

**한 줄 요약**: 열화 지향 변환으로 합성한 '오래된' 이미지가 희소한 역사 이미지를 대체할 수 있는지, 양방향 instance-level 검색에서 통제된 희소성 조건으로 측정한 연구.

**핵심 기여**: 문화유산 컬렉션은 같은 물체의 현대·역사 기록을 함께 담지만, 대응하는 이미지가 시점·촬영 조건·색 재현·프레이밍·해상도·열화에서 달라 연결이 어렵고 진짜 역사 이미지는 흔히 부족하다. 열화 지향 변환으로 old-domain 이미지를 합성해 EfficientNetV2-M 학습에 섞고, identity가 겹치지 않는 학습·검증·테스트 분할 3종과 시드 3개로 real-only baseline과 비교한다. 진짜 역사 이미지를 전부 합성으로 대체하면 양방향 평균 R@1이 86.56%에서 81.27%로 떨어져 합성 노화가 실제 old-domain 변이를 재현하지 못했고, 독립 생성한 합성 변형 수를 늘려도 일관된 개선은 없었다. 반면 통제된 희소성 아래에서는 진짜 역사 이미지 커버리지 25%에서 평균 R@1이 3.69%p, 50%에서 2.92%p 올랐고 75%에서는 2.00%p로 줄어, 합성 보완의 기여가 학습 노출량 증가보다 교차 도메인 identity 커버리지 확장에 있다고 해석한다.

**코드**: 불명

**태그**: image-retrieval, sim2real, metric-learning, fine-grained

---

### [Contrastive Knowledge Distillation for Anomaly Detection in Multi-Illumination/Focus Display Images](https://arxiv.org/abs/2609.05520)

**한 줄 요약**: teacher-student 특징 거리를 anchor 없이 직접 밀고 당기는 multiresolution contrastive distillation으로, 다중 조명·다중 초점 디스플레이 이미지의 미세 결함을 탐지한다.

**핵심 기여**: 디스플레이 표면의 미세 결함은 RGB 이미지에서 눈에 잘 띄지 않고 정상 데이터만으로 학습한 모델로도 잡아내기 어렵다는 문제를 다룬다. teacher와 student의 특징 유사도를 측정하는 Multiresolution Knowledge Distillation(MKD)을 baseline으로 삼고, anchor 기준 positive/negative 쌍을 요구하지 않고 teacher-student 특징 사이 거리를 당기고 미는 방식으로 동작하는 Multiresolution Contrastive Distillation(MCD)을 제안한다. 여기에 다중 채널 정보를 MCD의 3채널 입력층으로 변환·집계하는 blending 모듈을 더한다. 자체 수집한 다중 조명·다중 초점 디스플레이 이상탐지 데이터셋 MMdAD에서 AUROC와 정확도 모두 경쟁 방법들을 크게 앞선다고 보고한다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, defect-detection, distillation

---

### [Proximity-CLIP: Text-Guided Semantic Proximity Learning for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2609.07229)

**한 줄 요약**: 정상·이상 텍스트 프로토타입 사이의 의미 여백을 시각적으로 보정해 학습하고, 보정된 이상 프로토타입을 질의로 삼아 국소 결함 단서를 되찾는 zero-shot anomaly detection 프레임워크.

**핵심 기여**: VLM 기반 ZSAD는 object-centric bias 때문에 정상·이상 텍스트 프로토타입의 의미가 크게 겹치고, 둘 사이에 엄격한 직교성을 강제하면 판별력은 오르지만 연속적인 시각 입력을 급격히 직교인 프로토타입에 사상해야 하는 기하적 딜레마가 생겨 사전학습된 구조적 연속성이 깨진다고 지적한다. Proximity-CLIP은 bounded dynamic regularization으로 적절한 의미 여백을 학습하는 visually-calibrated semantic proximity learning으로 판별적 분리와 구조 정렬을 함께 확보하고, 보정된 이상 프로토타입을 semantic query로 쓰는 Anomaly Query Module(AQM)로 문맥 시각 패치에서 국소 결함 단서를 능동적으로 끌어와 global pooling 과정에서 미세 이상이 희석되는 문제를 완화한다. 구조 변경을 최소화한 채 여러 ZSAD 벤치마크에서 기존 state-of-the-art를 앞선다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, defect-detection, foundation-model

---

### [CoRe-SAM3: Conditional Semantic--Visual Reconciliation for SAM3 Crack Segmentation](https://arxiv.org/abs/2609.05816)

**한 줄 요약**: SAM3의 prompt-conditioned 의미 표현을 주 결정 경로로 유지한 채, 공간 정렬된 native 시각 증거로 zero-initialized 조건부 residual을 만들어 crack 예측을 선택적으로 교정한다.

**핵심 기여**: SAM3의 open-concept 분할 능력을 crack 도메인에 그대로 적용하면 약한 균열을 놓치고 균열과 닮은 배경을 활성화하며 국소 경계 오차를 낸다는 문제에서 출발한다. 다섯 개 crack 데이터셋에서 SAM3의 내부 prompt-conditioned 의미 표현과 native 시각 표현의 기능 차이를 진단해, 의미 표현이 이미 과제 정보의 대부분을 담고 시각 표현의 유용성은 현재 의미 상태에 의존하며 둘을 그대로 결합하면 일관된 이득이 없음을 확인했다. 이를 근거로 제안한 CoRe는 의미 예측을 주 결정 경로로 두고 경량 semantic calibration으로 목표 도메인 결정 사상을 조정한 뒤, 공간 정렬된 native 시각 증거로 zero-initialized·유계·정규화된 조건부 residual을 생성해 기존 예측을 선택적으로 교정한다. 학습 파라미터 18.914K만으로 다섯 도메인 평균 Crack IoU를 62.34%에서 70.47%로, clDice를 81.98%에서 89.24%로 올리고, native 오류의 평균 34.38%를 교정하는 동안 원래 맞게 분류된 픽셀의 손상률은 0.23%에 그친다.

**코드**: 공개 예정([CoRe-SAM3](https://github.com/xauat-liushipeng/CoRe-SAM3))

**태그**: segmentation, industrial-inspection, defect-detection, peft, foundation-model

---

### [Harnessing CLIP and DINO: An Uncertainty-Aware Cascaded Fusion Network for Generalizable Deepfake Image Detection](https://arxiv.org/abs/2609.07670)

**한 줄 요약**: CLIP의 언어 정렬 의미 prior와 DINO의 자기지도 시각 구조 prior를 Transformer 깊이별로 뽑아 entropy 기반 불확실성으로 가중 융합하는 deepfake 이미지 탐지 네트워크.

**핵심 기여**: foundation model 기반 deepfake 탐지기가 대개 단일 사전학습 표현에 의존해 특정 학습 분포에 과적합되기 쉽다는 점을 문제로 삼는다. UCF-Net은 두 인코더에서 Transformer 깊이 전반의 계층적 특징을 추출하고, 인코더별 layer-wise expert aggregation으로 다중 수준 단서를 적응적으로 결합한 뒤 entropy에서 유도한 불확실성을 기준으로 두 표현을 가중 융합한다. 공개 deepfake 데이터셋들을 약 400만 장 규모의 통합 벤치마크로 정리하고 최신 생성기 8종에서 얻은 8천 장 이상의 얼굴 이미지로 cross-generator 평가셋을 따로 구성했으며, 통합 벤치마크의 in-domain·cross-domain 평가 모두에서 비교 대상 중 가장 높은 평균 AUC를 기록한다. cross-generator 세트에서는 소량의 목표 도메인 데이터로 효과적으로 적응하지만 zero-shot 전이는 여전히 어렵다고 밝힌다.

**코드**: 불명

**태그**: forgery-detection, ssl-backbone, foundation-model, image-embedding

---

### [SAM3-O2D2: Zero-Shot Object Out-of-Distribution Detection by Object Class Prompting of the SAM3-Image Model](https://arxiv.org/abs/2609.08281)

**한 줄 요약**: 객체 탐지기가 예측한 클래스만으로 SAM3를 프롬프트해 같은 위치에서 객체가 검출되는지 비교하는 방식의 zero-shot 객체 OOD 탐지.

**핵심 기여**: 객체 탐지기는 배포 환경에서 학습에 없던 객체를 만나면 과신하기 쉬워 OOD 객체 탐지가 필요하지만, CLIP 같은 foundation model을 쓰는 기존 방법은 특징 공간에서 판정해 탐지기의 위치 오차와 외관 변화에 민감하고 현재 zero-shot state-of-the-art는 추론 시 비용이 큰 diffusion을 사용한다. SAM3-O2D2는 SAM3-image 모델에 탐지기의 예측 클래스만을 프롬프트로 주고 두 예측을 비교해, 해당 위치에서 SAM3도 객체를 검출하면 in-distribution으로, 검출하지 못하면 탐지기 예측과 이미지 내용의 불일치로 보아 OOD로 판정한다. ID 데이터셋 Pascal-VOC·BDD100K와 OOD 데이터셋 MS-COCO·OpenImages 조합 전반에서 기존 zero-shot state-of-the-art를 크게 앞서는 AuROC·FPR95를 기록한다.

**코드**: 불명

**태그**: open-vocab-detection, object-detection, calibration, foundation-model, training-free

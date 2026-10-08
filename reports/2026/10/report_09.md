# arXiv cs.CV Daily Digest — 2026-10-08 (arXiv 공개일)

- **전체 신규 논문 수**: 186편 (new 155 + cross-list 31)
- **선별 수**: 12편

## 오늘의 트렌드

의료영상 진단·합성과 3D Gaussian Splatting 재구성, 로봇용 world model·VLA가 가장 두꺼운 군집을 이루고 생성·편집 평가와 워터마크 검출, MLLM 토큰 축소가 뒤를 잇는다. 방법론에서는 동결된 자기지도 백본 위에 LoRA·프로토타입·cosine 유사도를 얇게 얹는 적응이 반복되고, 학습 목적함수를 정보이론·기하 관점에서 다시 유도하려는 시도와 합성 데이터·불확실성의 실제 효용을 통제 실험으로 검증하는 감사 연구가 함께 나타난다.

---

### [Scalable Patch-Level Self-Supervised Learning](https://arxiv.org/abs/2610.10013)

**한 줄 요약**: multi-view 가정에서 정보이론적 목적함수를 유도해 패치 단위로 뷰 간 표현을 정렬하는 student-teacher SSL 알고리즘 JEM.

**핵심 기여**: 대규모 SSL 방법 대부분이 여러 목적함수와 안정화 장치를 임기응변식으로 조합한다는 문제의식에서 출발해, 과제 관련 정보는 서로 다른 뷰가 공유하는 정보에 담긴다는 multi-view 가정만으로 해석 가능한 항들로 분해되는 정보이론적 목적함수를 구성한다. 여기서 도출된 JEM은 뷰 간 대응 패치 표현을 정렬하면서 정보 보존·구조 보존 손실로 명시적으로 정규화하는 student-teacher 방식이며, 300M에서 7B 파라미터까지 안정적으로 학습된다. 저자들이 아는 한 7B 규모에서 입증된 최초의 잠재공간 패치 단위 방법으로, 전 규모에서 global·dense probing 모두 강한 성능을 내고 segmentation 벤치마크에서 DINOv2 알고리즘을 일관되게 넘어선다. 7B에서는 12배 적은 데이터로 refinement 단계 없이 학습했음에도 panoptic segmentation에서 DINOv3를 상회한다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, foundation-model, segmentation

---

### [Global Average Precision for Representation Learning](https://arxiv.org/abs/2610.09863)

**한 줄 요약**: 쿼리별이 아니라 전체 쿼리-후보 쌍을 한 줄로 세워 AP를 계산하는 gAP의 미분 가능 대리 손실 gSAP.

**핵심 기여**: mAP나 InfoNCE·쿼리별 AP 대리 손실은 쿼리 하나씩 평가하므로 쿼리 간 유사도가 서로 비교 가능한지는 따지지 않는데, 단일 임계값으로 판정하는 시스템은 바로 그 비교 가능성에 의존한다는 문제의식이다. gAP는 모든 쿼리-후보 쌍을 하나의 순위 목록으로 놓고 AP를 한 번 계산하며, 제안하는 gSAP는 유사도 행렬과 양성 쌍 표시 이진 행렬만 입력으로 받아 기존 손실을 그대로 대체하고 인코더·모달리티·지도 방식에 무관하다. 배치 내 모든 쌍 비교를 함께 보기 때문에 쿼리별 대리 손실이 gradient를 잃는 낮은 temperature 영역에서도 학습이 유지되며, supervised metric learning·cross-modal alignment·자기지도 사전학습에 투입해 성능이 올랐고 뒤 두 경우에서 InfoNCE를 대체한 최초의 ranking loss라고 밝힌다. 같은 precision에서 가장 강한 AP 대리 손실 대비 최대 4배의 양성 쌍을 검색하고, 데이터베이스에 양성이 없는 쿼리가 추가될 때 성능 저하가 가장 작으며, transfer·kNN·zero-shot 정확도도 함께 높아진다.

**코드**: 불명

**태그**: metric-learning, image-retrieval, image-embedding, calibration, ssl-backbone

---

### [DisParQ: Self-Supervised Part Concepts for Interpretable Vision Foundation Models](https://arxiv.org/abs/2610.09802)

**한 줄 요약**: 동결된 vision-only 자기지도 백본에서 레이블·언어 없이 공간에 근거한 이산 part 개념과 양자화 속성을 학습하는 DisParQ.

**핵심 기여**: 개념 기반 모델이 고정된 범주에 묶이거나 개념 정의를 언어에 의존한다는 한계를 지적하며, 클래스 레이블과 언어 지도 없이 개념 표현을 학습한다. 각 이미지 패치를 학습 가능한 prototype dictionary의 개념 하나에 배정하고 이미지당 희소한 부분집합만 활성화하며, 개념이 이미지마다 어떻게 변하는지("wheel"의 종류 등)를 연속 residual로 포착한 뒤 이산 속성으로 양자화한다. spatial decoder가 개념과 속성만으로 백본 표현을 복원하도록 해 이산 표현이 백본 정보를 보존함을 확인하며, ImageNet·PartImageNet·Places부터 CUB·Cars·Dogs·Flowers까지 일곱 데이터셋에서 평가한다. 동결 DINOv2 teacher의 ImageNet linear probing에 근접한 83.2% top-1을 기록하고, 언어 정렬 모델보다 높은 개념 일관성을 보이며 범주를 가로지르는 part 기반 검색이 가능하다.

**코드**: 불명

**태그**: ssl-backbone, fine-grained, image-retrieval, foundation-model, image-embedding

---

### [What Makes Synthetic Hard Negatives Work in Vision-Language Pretraining?](https://arxiv.org/abs/2610.09700)

**한 줄 요약**: 표현공간 합성 hard negative가 vision-language 사전학습에서 실패하는 두 양상을 기하적으로 분석하고 이를 피하는 intra-modal 생성법 SNAP.

**핵심 기여**: 표현공간에서 합성한 hard negative는 단일 모달 자기지도 학습에서 효과가 입증됐지만 vision-language 사전학습으로의 이전이 단순하지 않다는 관찰에서 출발해, 여섯 가지 합성 전략을 분석한다. cross-modal 구성은 지나치게 쉬운 negative를 만들거나 negative를 쿼리 쪽으로 끌어당기고, intra-modal 구성은 매칭된 positive를 끌어들이는 두 실패 양상이 드러나며, 학습 가능한 temperature와 함께 쓸 때 logit-scale 포화가 관측돼 temperature를 고정하면 downstream 성능이 개선된다. 이 기하 분석을 바탕으로 한 SNAP은 어느 모달리티에서도 positive를 끌어들이지 않는 intra-modal hard negative를 생성해 두 실패를 모두 피하며, 모델 비의존적이고 외부 생성모델이 필요 없으며 학습 시간 증가는 10% 미만이다. CLIP과 FLIP 위에 여러 아키텍처·데이터셋에서 평가해 zero-shot 검색, zero-shot 분류, linear probe에서 일관된 개선을 보인다.

**코드**: 불명

**태그**: metric-learning, image-retrieval, image-embedding, vlm, ssl-backbone

---

### [Shared Geometry As A Rosetta Stone: Cross-Modal Alignment Without Paired Data](https://arxiv.org/abs/2610.09411)

**한 줄 요약**: 쌍 데이터 없이 직교 변환 하나를 추정해 독립적으로 학습된 두 모달리티 임베딩을 정렬하는 Wasserstein Procrustes 방법.

**핵심 기여**: 멀티모달 표현은 zero-shot 분류·검색을 가능하게 하지만 독립 학습된 모델을 정렬하려면 대량의 쌍 데이터가 필요했는데, Platonic Representation Hypothesis가 시사하듯 서로 다른 모달리티로 학습된 모델이 공유 표현 기하로 수렴한다면 쌍이 필요한지 자체를 다시 묻는다. 거친 기하 초기화를 붙인 단순한 Wasserstein Procrustes로 서로 겹치지 않는 두 임베딩 집합을 쌍 하나 보지 않고 직교 사상 하나만 추정해 정렬하며, 여러 데이터셋·모달리티·단일모달 모델에서 일관되게 정렬이 성립하고 표준 기하 정렬 지표가 언제 가능한지를 정확히 예측한다. 쌍이 아주 적은 영역에서는 기존 방법을 크게 앞서고 쌍을 더 넣어도 쌍 기반 방법과 경쟁력을 유지하며, 얻어진 정렬로 쌍 없는 text-to-image 생성까지 보인다.

**코드**: 불명

**태그**: image-embedding, metric-learning, correspondence, image-retrieval

---

### [BagDINO: Multi-View Baggage Re-Identification with DINOv3](https://arxiv.org/abs/2610.10160)

**한 줄 요약**: DINOv3 표현에 BNNeck re-id 헤드를 얹고 LoRA로 적응해 수하물을 인스턴스 단위로 검색하는 multi-camera re-identification.

**핵심 기여**: 공항의 수하물 분실 복구가 여전히 태그 기반 추적에 의존해 태그 증거가 없을 때 시각적 식별을 지원하지 못한다는 문제의식에서, 수하물 re-identification을 multi-camera 환경의 인스턴스 단위 검색 문제로 다룬다. DINOv3 foundation model 표현 위에 Torchreid 계열 BNNeck re-identification 헤드를 올리고 LoRA로 파라미터 효율 적응을 수행해, 쿼리 이미지를 등록된 수하물 이미지 갤러리와 매칭한다. MVB 벤치마크에서 완전 동결 백본과 LoRA, 전체 fine-tuning을 단계적으로 비교했으며, 학습 데이터가 제한된 조건에서 foundation model 특징의 파라미터 효율 적응이 효과적이고 안정적이라는 결과를 보고한다. 초록에 정량 수치는 제시되지 않는다.

**코드**: 불명

**태그**: re-identification, image-retrieval, peft, foundation-model, ssl-backbone

---

### [An Invariant Tangent-Angle Descriptor and a Band U-Net for 2D Fragment Adjacency Prediction](https://arxiv.org/abs/2610.09459)

**한 줄 요약**: 윤곽 접선각 프로파일 비교로 회전 불변 descriptor를 만들고 band U-Net으로 인접 구간까지 함께 내놓는 2D 조각 인접 판정.

**핵심 기여**: 두 2D 조각의 윤곽만으로 인접 여부를 예측하는 문제에서, 기존 2단계 구조는 회전 등변 Siamese CNN이 두 윤곽 위 국소 이미지 윈도우 쌍을 점수화하고 그 점수 행렬에서 ResNet이 인접을 드러내는 부분 반대각 band를 검출했다. 이 논문은 파이프라인을 유지한 채 국소 점수를 윤곽 윈도우의 접선각 프로파일 비교로 교체해 구성상 조각 회전에 불변이고 윤곽 시작점 선택에 무관하게 만들며, 학습이 필요 없는 likelihood ratio 또는 대응점으로 학습한 작은 1D 합성곱 모델 두 형태를 제시한다. 최종 분류기도 band를 분할하면서 쌍을 분류하는 band U-Net으로 바꿔 판정과 함께 공유 호(arc)를 얻는다. 원 논문의 합성 데이터셋에서 접선 descriptor가 모든 설정에서 이미지 윈도우 방식 이상이며 정확도 98%(평가를 바로잡은 기존 방식 93~95%)에 이르고, 합성 데이터만으로 학습한 모델을 PairingNet 벤치마크에 적용해 AUC 0.93, pair-searching 프로토콜의 실데이터에서 Recall@10 0.82(기존 최고 모델 0.56)를 얻는다.

**코드**: 불명

**태그**: feature-matching, correspondence, image-retrieval, sim2real, training-free

---

### [One-Shot Adaptive Segmentation For Scientific Images](https://arxiv.org/abs/2610.10306)

**한 줄 요약**: DINOv3 특징의 배경 적응형 직교화와 cosine 유사도로 후보 영역을 찾아 SAM에 넘기는 학습 없는 one-shot 분할 프레임워크.

**핵심 기여**: 과학 이미지 분할이 대량 주석과 과제별 학습에 의존해 촬영 모달리티와 실험 조건을 넘나드는 적응이 어렵다는 문제의식에서, 주석된 참조 이미지 한 장으로 vision foundation model을 특화하는 학습 불필요 프레임워크를 제시한다. DINOv3 표현에 배경 적응형 특징 직교화를 적용해 아티팩트 관련 특징 방향을 억제한 뒤 cosine 유사도로 후보 영역을 지역화하고, 그 영역을 SAM 분할에 넘긴다. 적혈구 현미경, structured-illumination pool boiling, 흉부 X선 세 과제에서 평가해 가장 강한 baseline 대비 현미경에서 mean IoU 5.91%, pool boiling에서 78.62% 개선을 얻고 흉부 X선에서는 동등한 수준을 보인다.

**코드**: 불명

**태그**: segmentation, training-free, ssl-backbone, foundation-model, correspondence

---

### [RT-DETR-World: Transferring Rich LLM Semantics to Real-Time Open-Vocabulary Detection](https://arxiv.org/abs/2610.09502)

**한 줄 요약**: 학습 시에만 LLM·설명 기반 의미를 주입하고 추론에서는 가벼운 query-text 매칭만 남기는 실시간 open-vocabulary DETR 검출기.

**핵심 기여**: 실시간 open-vocabulary detection은 어휘 커버리지와 효율적인 region/query-text 매칭에 집중해 왔지만, 엄격한 효율 제약 아래 소형 검출기가 풍부한 인스턴스 의미와 장면 맥락을 흡수하기 어렵다는 문제의식이다. 범주명, 인스턴스 단위 의미를 담은 객체 설명, 객체 관계·장면 맥락을 담은 이미지 설명의 3단계 지도를 갖춘 GroundingCapv2를 구축하고, 이 설명들은 학습 시 의미 지도로만 쓴다. Dual-Path Description Alignment는 배포와 일관된 MiniLM 경로와 학습 전용 LLM teacher를 결합해 query-category 지도와 객체 설명 정렬을 제공하고 사전 계산된 teacher 특징이 매칭된 query와 전역 시각 표현을 객체·이미지 수준에서 지도하며, teacher 측 모듈은 학습 후 제거된다. Relation-Aware Negative Relaxation은 teacher가 유도한 의미 유사도로 관련 있는 negative를 완화하면서 정확한 positive는 보존하며, 실험에서 경쟁력 있는 zero-shot 정확도와 정확도-효율 trade-off를 보고한다.

**코드**: 공개 예정

**태그**: open-vocab-detection, object-detection, distillation, efficient-inference, vlm

---

### [MOTIF: Person-of-Interest Deepfake Detection Beyond 3DMM Coefficients](https://arxiv.org/abs/2610.09830)

**한 줄 요약**: 3DMM 계수 중 어느 블록이 실제 신호를 담는지 해부하고 버려지던 dense surface까지 끌어들인 person-of-interest 딥페이크 검출기.

**핵심 기여**: 특정 인물을 겨냥한 영상 딥페이크는 피해가 가장 크고 공인은 진짜 영상이 풍부해 그것만으로 검출기를 만들 수 있는데, 기존 POI 검출기는 대상을 3D Morphable Model로 기술하고 계수 벡터를 통째로 쓰기 때문에 어느 부분이 신호를 담는지 측정된 적이 없다는 문제의식이다. 인코더·학습 코퍼스·등록 프로토콜을 고정하고 인코더가 관찰하는 대상만 바꿔 해부한 결과, 계수 그룹들은 대체로 중복적이어서 shape 블록만으로 전체 벡터의 정확도를 거의 회복하고 시간적 변화는 실재하지만 제한적인 기여를 한다. 같은 fitting이 돌려주지만 기존 검출기가 버리던 dense surface는 계수에 없는 identity 정보를 담고 계수가 가장 약한 지점을 정확히 보완한다. 최적 구성을 모은 MOTIF는 조작 영상도 POI별 데이터도 쓰지 않고 진짜 영상만으로 학습한 시각 전용 검출기로, 벤치마크의 모든 데이터셋·조작 유형과 두 화질 수준에서 기존 두 SOTA POI 검출기를 모두 앞선다.

**코드**: 공개 예정([MOTIF](https://github.com/polimi-ispl/MOTIF))

**태그**: forgery-detection, re-identification, video, metric-learning

---

### [MSU Team at the Explainable Deepfake Detection Challenge 2026: Grounded Artifact Evidence for Deepfake Detection](https://arxiv.org/abs/2610.09952)

**한 줄 요약**: 여러 DINOv3와 Mesorch 조작 지역화 특징을 묶은 다중 백본 검출기에 artifact evidence map 지도를 붙인 설명 가능 딥페이크 검출 챌린지 해법.

**핵심 기여**: 생성모델 발전으로 조작 이미지가 매우 사실적이 되면서 정확할 뿐 아니라 판단의 시각적 증거를 제시하는 검출기가 필요하다는 문제의식에서, XPlainVerse 데이터셋 기반 Explainable Deepfake Detection Challenge 해법을 검출-설명 모듈 분리 구조로 구성한다. real/fake 판정은 여러 DINOv3 모델과 Mesorch 조작 지역화 특징을 결합해 사전학습 시각 표현, DCT 기반 단서, 다중 스케일 포렌식 정보를 한데 모은 다중 백본 검출기가 맡는다. 설명 증거를 검출기에 주입하기 위해 Grounding-DINO 기반 pseudo-mask 생성 파이프라인으로 학습 설명문의 국소 아티팩트 서술을 patch 단위 약지도로 바꿔 Artifact Evidence Map을 학습시키고, 쌍 이미지나 픽셀 단위 조작 마스크 없이 아티팩트 증거와 진정성 증거를 특징 공간에서 분리하는 patch 단위 대조 손실을 도입한다. 언어 출력은 class-conditional Qwen3-VL과 GRPO로 최적화한 단순화 모델이 담당하며, 전체 test split에서 검출 정확도 0.9349, 설명 점수 0.5571, 최종 챌린지 점수 0.7456을 기록한다.

**코드**: 불명

**태그**: forgery-detection, ssl-backbone, open-vocab-detection, vlm

---

### [Inverting Multi-Vector Visual Document Indices](https://arxiv.org/abs/2610.09920)

**한 줄 요약**: 페이지당 수천 개 패치 벡터로 저장된 멀티벡터 문서 검색 인덱스만으로 원본 페이지 이미지를 복원할 수 있음을 보인 역전 공격.

**핵심 기여**: 멀티벡터 시각 문서 검색기는 한 페이지를 약 천 개의 패치 벡터로 저장하고 흔히 제3자가 운영하는 벡터 데이터베이스에 두는데, 벡터에서 페이지를 읽을 수 없다는 이유로 원문보다 덜 민감하게 취급된다는 점을 문제 삼는다. 인덱스가 패치당 벡터 하나를 raster 순서로 유지하고 각 벡터가 문서를 읽도록 사전학습된 vision-language model로 계산된다는 점에 착안해, 역전을 조건부 문서 이미지 생성으로 정식화하고 공격에 필요한 인코더·페이지 형태·(섞인 경우) 벡터 순서를 벡터로부터 추론한다. ViDoRe v3 벤치마크에서 원본 인덱스로부터 복원한 페이지가 단어의 47%와 민감 토큰의 45%를 회복하고, 이를 쿼리로 써서 원본 페이지를 98.4% 확률로 1위에 올린다. token pooling과 shuffling 두 저비용 방어는 단어 recall을 약 8%로 낮추지만 섞인 인덱스의 순서를 복원하는 모델은 1위 비율을 3.8%에서 93.5%로 되돌리며, pooling된 인덱스 역전은 미해결로 남는다. 동일 공격을 다른 멀티벡터 검색기에 그대로 적용해도 70.2%가 1위에 오른다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, ocr-document, vlm, forgery-detection

---

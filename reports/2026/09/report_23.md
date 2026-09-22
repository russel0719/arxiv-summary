# arXiv cs.CV Daily Digest — 2026-09-22 (arXiv 공개일)

- **전체 신규 논문 수**: 272편 (new 221 + cross-list 51)
- **선별 수**: 12편

## 오늘의 트렌드

world model·VLA로 로봇 행동과 영상 예측을 잇는 연구, Gaussian Splatting·feed-forward 기하 복원, 의료 영상 분할·합성이 가장 두꺼운 군집을 이룬다. MLLM 쪽에서는 시각 토큰 프루닝·라우팅 같은 추론 비용 절감과 진단용 벤치마크가 함께 늘었다. 방법론으로는 가중치를 동결한 채 검색·프롬프트·테스트타임 보정만으로 분포 변화에 대응하는 설계, 동결된 foundation feature 위에 경량 모듈만 얹는 구성이 반복된다.

---

### [Positive Pair Geometry Matters: Optimal Transport for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2609.24125)

**한 줄 요약**: 독립 샘플링한 두 증강 뷰 대신 원본과 증강본 사이를 entropic optimal transport로 보간한 중간 뷰를 positive로 쓰는 contrastive 표현학습 프레임워크.

**핵심 기여**: 기존 contrastive self-supervised learning은 확률적 증강을 독립적으로 샘플링해 positive pair를 구성하기 때문에 의미 내용이 바뀔 수 있고 데이터 분포의 내재적 기하를 반영하지 못한다고 지적한다. OTCLR은 두 무작위 증강 뷰를 직접 대조하는 대신, 원본 이미지와 그 증강본 사이의 entropic optimal-transport displacement interpolation으로 중간 뷰를 생성해 positive로 쓰고, 이 보간 뷰가 양 끝 이미지와 일관되도록 하는 Sinkhorn 정규화 항을 함께 평가한다. 인코더 구조를 바꾸지 않아 표준 contrastive 파이프라인에 그대로 삽입할 수 있으며, 여러 벤치마크에서 증강 기반 contrastive 베이스라인 대비 표현 품질과 전이 성능이 개선된다고 보고한다. 초록에는 구체적 정량 수치가 제시되지 않는다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, metric-learning

---

### [MotionJEPA: Preventing Temporal Feature Collapse by Capturing Visual Changes in Latent Space](https://arxiv.org/abs/2609.23881)

**한 줄 요약**: JEPA 학습이 느린 특징으로 쏠려 시간적 표현이 붕괴하는 문제를, 픽셀 복원 없이 차분 이미지 임베딩을 예측하는 정규화 항으로 완화한 잠재 표현학습 구조.

**핵심 기여**: Joint Embedding Predictive Architecture는 복원 없이 task-agnostic 잠재 world model을 학습하지만, 표준 학습이 느린 특징(slow feature)으로 강하게 편향돼 특징 억제와 표현 붕괴가 일어나며, 이를 막는 inverse dynamics 방식은 행동 레이블을 요구하고 레이블 없는 일반 동역학을 담을 유인이 약하다는 점을 문제로 삼는다. DISReg는 inverse-dynamics 형태의 모듈이 픽셀 복원 손실 없이 시간 차분 이미지의 임베딩을 예측하게 하는 정규화로, 임베딩 분포를 잡아 느린 특징을 유도하는 정적 항과 임베딩의 형태·분포에 제약을 주지 않고 동적 특징의 존재만 장려하는 동적 항으로 구성된다. 이를 표준 JEPA에 결합한 MotionJEPA는 latent probing에서 다른 방법보다 완전한 표현을 얻고, 궤적 분석에서 곡률이 낮은 기하적으로 단순한 잠재 궤적을 유지하며, 정적 배경 방해 요소가 있는 네 환경에서 downstream 계획 성공률이 향상된다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, video

---

### [Retrieval Geometry Shapes Cache-Based Clip Adaptation](https://arxiv.org/abs/2609.23409)

**한 줄 요약**: 캐시 기반 CLIP 테스트타임 적응에서 저장된 예시가 아니라 이미지-이미지 검색에 쓰이는 표현 공간 자체가 성능을 좌우함을 보이고, 예측은 CLIP·검색은 DINOv2로 분리한 학습 없는 구성을 제안한다.

**핵심 기여**: 캐시 기반 테스트타임 적응은 모델을 동결한 채 타깃 스트림의 예시를 저장·검색해 CLIP 예측을 보정하지만, 기존 방법들은 검색에 쓰는 특징 공간을 고정된 것으로 취급해 적응 이득이 검색 공간에 얼마나 의존하는지 검증되지 않았다고 지적한다. 메모리를 고정한 채 검색 인코더만 바꿔 16개 검색 공간을 비교한 결과 같은 메모리에서도 ImageNet-A 캐시 이득이 CLIP·MAE의 최대 +0.44점부터 DINOv2-L의 +19.7±0.4까지 벌어졌고, 레이블 없는 검색 공간 선택만으로 ImageNet-V2에서 oracle 이득의 98%를 유지했다. 이를 바탕으로 예측은 동결 CLIP, 검색은 DINOv2-B가 맡고 융합 가중치 하나만 두는 학습 없는 MARC를 제안하며, 단일 뷰 캐시가 베이스라인 오류 1074±21건을 고치는 데 비해 64뷰 앙상블은 878±4건에 그쳐 약 1/7 비용으로 앞선다. 네 종류의 ImageNet 분포 변화에서 OOD 평균 67.91%를 기록하고, 동일한 DINOv2-B 규모·8뷰 조건에서 그래프 기반 캐시의 62.75±0.15% 대비 64.17±0.31%를 2.6배 빠른 속도로 달성한다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, ssl-backbone, training-free

---

### [Graded-Relevance Composed Multimodal Retrieval for E-commerce Visual Search at Scale](https://arxiv.org/abs/2609.24152)

**한 줄 요약**: composed image retrieval의 이진 관련성 가정을 4단계 등급 관련성으로 바꾸고, VLM 자동 라벨링·하드 네거티브 마이닝·계층 인식 angular 목적함수로 bi-encoder 검색기를 학습한 방법론.

**핵심 기여**: 대규모 상품 카탈로그 시각 검색은 유사 이미지 질의와 이미지+수정문구 질의(CIR)를 함께 처리해야 하는데, 기존 CIR 방법은 관련성을 이진으로 보고 단일 정답 triplet으로 학습하기 때문에 다수 후보가 질의를 부분적으로 만족하는 실제 카탈로그의 순위 매기기에 맞지 않는다고 지적한다. GradCIR은 (i) VLM으로 질의(객체 검출 + 수정문구 합성)와 4단계 관련성 레이블을 수작업 주석 없이 생성하고, (ii) 학습 중인 검색기에서 하드 네거티브를 캐 학습셋을 넓히는 반복적 관련성 피드백 루프를 돌리며, (iii) 등급을 이진으로 뭉개지 않고 직접 학습하는 계층 인식 angular 목적함수를 쓴다. Walmart 카탈로그에서 만든 350만 등급 쌍으로 PaliGemma2 bi-encoder를 학습했고, 등급 대 이진 supervision만 바꾼 통제 ablation에서 NDCG@10이 4.9~5.9% 오르며 같은 방식을 다른 멀티모달 인코더에 적용하면 early-fusion 백본이 최대 8.5% 향상된다. 공개 FashionIQ에서는 fine-tuning 시 평균 recall 0.6703으로 비교 대상 지도학습 베이스라인을 약간 앞서고 CLIP-L급 zero-shot CIR 방법들과 같거나 그 이상이며, 시스템은 실제 서비스 트래픽에 배포돼 있다.

**코드**: 불명

**태그**: image-retrieval, metric-learning, image-embedding, vlm

---

### [AdaMerge: Tuning-Free Patch Compression for Multi-Vector Visual Document Retrieval](https://arxiv.org/abs/2609.22562)

**한 줄 요약**: ColPali 계열 multi-vector 임베딩 압축에서 데이터셋별로 튜닝하던 클러스터 예산을, 계층적 군집의 merge-cosine 곡선에 나타나는 문서별 절벽을 탐지해 자동으로 정하는 plug-and-play 압축기.

**핵심 기여**: ColPali·ColNomic 같은 multi-vector 시각 문서 검색 모델은 문서당 수백~수천 개의 patch 임베딩을 써 정확도는 높지만 저장·지연 비용이 크고, 최신 병합 기법 Prune-then-Merge는 pruning 기반보다 우수하지만 클러스터 예산 m을 데이터셋마다 grid search로 맞춰야 한다는 점을 문제로 삼는다. 저자들은 계층적 군집이 만드는 merge-cosine 수열에 병합 가능한 중복과 유의미한 신호를 가르는 뚜렷한 절벽이 있고 그 위치가 14개 데이터셋 11,000여 문서에 걸쳐 좁은 대역에 몰린다는 관찰에서 출발해, 병합 경계를 데이터셋별 튜닝이 아니라 문서별 탐지로 정할 수 있다고 본다. AdaMerge는 merge-cosine 궤적의 gap 분석으로 문서마다 자기 절벽을 찾고 attention 가중 클러스터 중심을 만들어 유의미한 신호를 보존한다. 장문서 벤치마크 ViDoRe-V2(4개 데이터셋, 백본 2종)에서 튜닝된 PtM을 운용 구간 전반에 걸쳐 유의하게 앞서고(p < 10^-4), 병합 기법들이 이미 거의 무손실인 단문서 ViDoRe-V1(10개 데이터셋)에서는 데이터셋별 튜닝 없이 튜닝된 PtM과 동등하며, 문서당 약 10 ms만 추가하고 전 데이터셋·백본 공용 하이퍼파라미터 하나만 노출한다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, training-free, efficient-inference, ocr-document

---

### [Vision Transformers versus convolutional neural networks for fine-grained orchid genus identification in a species-rich, data-poor flora: a controlled benchmark on the Orchidaceae of New Guinea](https://arxiv.org/abs/2609.24064)

**한 줄 요약**: 종당 사진이 극소수인 뉴기니 난초 상황에서 속(genus) 분류 후 FAISS 임베딩 검색으로 종 후보를 제시하는 2단계 시스템을 만들고, ViT·CNN 백본 4종을 동일 프로토콜로 비교한 통제 벤치마크.

**핵심 기여**: 종 수는 약 2,856종인데 대부분이 사진 몇 장뿐이라 종 단위 직접 분류가 어려운 데이터 빈곤 상황에서, 어떤 백본과 사전학습 전략이 fine-grained 식별을 지지하는지 불분명하다는 문제의식에서 출발한다. 120속 1,350종 16,701장을 종 계층화 고정 분할로 나누고 DINOv2·BioCLIP 2(ViT)와 ConvNeXt V2-L·EfficientNetV2-L(CNN)을 동일 프로토콜로 fine-tuning해 정확도·캘리브레이션·오류 구조·종 검색·미지 속 open-set 탐지를 함께 측정했다. DINOv2가 속 macro top-1 66.9%(95% CI 63.7-70.6), global top-1 88.9%로 가장 높았고 두 ViT가 두 CNN을 모두 앞섰으며, 범용 self-supervised 사전학습(DINOv2)이 도메인 정합 생물 사전학습(BioCLIP 2)을 macro top-1 기준 7.1점 앞섰다. DINOv2 임베딩은 종 Recall@5 86.6%·속 Recall@5 98.7%를 얻었고, temperature scaling으로 모든 백본의 ECE가 약 0.03까지 낮아졌으며, 거리 기반 open-set 게이트가 미지 속을 평균 AUROC 0.958로 걸러냈다. 오류는 개체수가 많은 두 속에 집중돼 error attractor로 작용했다.

**코드**: 불명 (초록에는 오픈 웹 애플리케이션 New Guinea Orchid Identifier 공개만 명시)

**태그**: fine-grained, image-retrieval, ssl-backbone, calibration, dataset-benchmark

---

### [InterHier: Learning Interconnected Hierarchical Semantics for Open-Vocabulary Object Detection](https://arxiv.org/abs/2609.24026)

**한 줄 요약**: open-vocabulary 검출에서 상위·하위 카테고리를 잇던 고정 connector 대신, 프롬프트 앞에 붙는 학습 가능한 context로 계층 관계 해석을 전역적으로 유도하는 표현 방식.

**핵심 기여**: 기존 방법은 base 카테고리와 미본 novel 카테고리의 의미 관계를 세우기 위해 인접한 상위/하위 카테고리 사이에 고정된 수작업 connector를 넣는데, 이런 고정 connector가 의미 계층 내부의 관계를 최적으로 담아내지 못한다는 한계를 짚는다. InterHier는 두 단계로 동작해, 먼저 상위·하위 카테고리를 통합하고 학습 가능한 context를 앞에 붙여 계층 인식 프롬프트를 구성한 뒤, 시각 영역 임베딩과 텍스트 임베딩을 정렬하도록 그 context를 최적화한다. 고정 connector에 의존하는 방법들보다 일관되게 성능이 오르고 기존 open-vocabulary 검출 모델에 그대로 결합할 수 있으며, open-vocabulary 검출 벤치마크에서 최신 방법들과 경쟁 가능한 성능을 보고한다. 초록에는 구체적 수치가 제시되지 않는다.

**코드**: 불명

**태그**: open-vocab-detection, object-detection, vlm

---

### [HyperCLIP++: Fine-tuning CLIP for Open-vocabulary Semantic Segmentation in Hyperbolic Space](https://arxiv.org/abs/2609.24564)

**한 줄 요약**: CLIP을 분할용으로 fine-tuning할 때 텍스트 임베딩의 hyperbolic 반지름이 줄어드는 현상을 관찰하고, 그 반지름을 직접 조정하는 것만으로 계층 정렬을 맞추는 파라미터 효율적 적응 전략.

**핵심 기여**: CLIP의 텍스트 인코더를 동결하면 일반화가 보존되지만 두 인코더를 함께 fine-tuning하면 open-set 클래스 분할이 크게 좋아진다는 상반된 관찰을, fine-tuning 중 이미지 임베딩의 계층 수준이 image-level에서 pixel-level로 이동하는 계층 정렬 관점으로 설명하고 계층 구조를 자연스럽게 담는 hyperbolic 공간을 도구로 쓴다. 핵심 관찰은 fine-tuning 동안 CLIP 텍스트 임베딩의 hyperbolic 반지름이 감소해 픽셀 수준 granularity와 더 잘 맞춰진다는 것이며, HyperCLIP++는 스케일링 변환으로 이 반지름을 직접 조정해 목표 과제에 계층을 정렬하고, 두 모달리티에서 조정이 일관되게 적용되고 학습 중 교차 모달 정렬이 보존되도록 Dual Cross-Relation Communication 모듈로 vision·text 경로를 동기화한다. CLIP 전체 파라미터의 약 5%만 fine-tuning하면서 세 벤치마크에서 최고 성능을 달성하고, 조정 후 텍스트 임베딩의 hyperbolic 반지름이 데이터셋에 걸쳐 비교적 고정된 값을 보여 해당 분할 과제가 요구하는 계층 수준을 반지름으로 정량화할 가능성을 제시한다.

**코드**: 불명

**태그**: segmentation, peft, vlm, foundation-model

---

### [SRPR-Net: Semantic and Relational Prompt Refinement for Automated SAM-based Instance Segmentation](https://arxiv.org/abs/2609.24226)

**한 줄 요약**: SAM 기반 자동 instance segmentation에서 검출기가 낸 박스를 시각-언어 의미와 같은 이미지 내 인스턴스 의존관계로 순차 보정한 뒤 SAM에 넣는 프롬프트 정제 구조.

**핵심 기여**: 프롬프트 기반 foundation model이 좋은 일반화를 보이지만 자동 프롬프트 생성은 의미 가이드가 부족하고 인스턴스 간 관계를 모델링하지 못한다는 점을 한계로 짚는다. SRPR-Net은 순차적 프롬프트 정제 메커니즘을 도입해 검출기의 기하 정보에 시각-언어 의미를 더하고 이어서 같은 이미지 안의 인스턴스 의존관계를 반영함으로써, SAM 분할 이전에 맥락을 고려한 박스 조정을 수행한다. 여러 표준 벤치마크에서 기존 최신 방법 대비 일관된 분할 성능 향상을 보고한다. 초록에는 구체적 수치가 제시되지 않는다.

**코드**: 공개([SRPR-Net](https://github.com/JeremyXSC/SRPR-Net))

**태그**: segmentation, foundation-model, object-detection

---

### [SAFe: Segment-guided Aggregation of Feature Densities for Anomaly-aware Segmentation](https://arxiv.org/abs/2609.24204)

**한 줄 요약**: 동결된 DINOv3 특징 위에 클래스 조건부 normalizing flow로 정규화된 likelihood를 추정하고, SAM3 기반 후처리로 위치별 점수를 공간적으로 일관된 세그먼트로 묶는 이상 인식 분할 방법.

**핵심 기여**: 분할 시스템이 배포 환경에서 학습 분포 밖 객체를 만나는 문제를 다루면서, self-supervised foundation model 위에 밀도 추정기를 학습하는 최근 방법들이 특징 의미가 빈약하거나 공간 일관성이 없어 후속 판단을 훼손한다고 지적한다. SAFe는 동결 DINOv3 특징에 대해 클래스 조건부 정규화 likelihood를 내는 경량 normalizing flow를 학습하고, transformer 특징의 밀도 추정과 다중 스케일 convolution 특징의 밀도 점수를 결합해 전역 의미와 국소 세부를 함께 잡는다. 여기에 SAM3를 쓰는 방법 비의존적 후처리를 더해 위치별 likelihood를 공간적으로 일관된 세그먼트로 연결하면서 false positive를 억제하고, 재학습 없이 인스턴스 단위 이상 탐지를 가능하게 하며, 유사도 기반 병합 군집화로 이상 객체 중 새로운 범주를 구분한다. PANIC·OoDIS·SMIYC ObstacleTrack에서 새로운 최고 성능을 세우고 ISSU 벤치마크에서도 강한 성능을 보고한다.

**코드**: 불명

**태그**: anomaly-detection, segmentation, ssl-backbone, foundation-model

---

### [Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection](https://arxiv.org/abs/2609.24359)

**한 줄 요약**: 특화 위조 탐지기들을 학습 없이 묶는 agentic 프레임워크에서 triage·프롬프팅·증거 중재 중 무엇이 실제로 성능을 만드는지 6개 구성과 3개 MLLM 백본으로 분해한 연구.

**핵심 기여**: 완전 합성 이미지부터 국소 편집·splicing·swapping까지 조작 유형이 넓어지는 open-world 상황에서 대부분의 포렌식 탐지기는 단일 조작 계열에 특화돼 있고, agentic AI가 개별 탐지기의 신뢰도를 평가하고 범위 밖 증거를 식별하며 상충 보고를 중재하는 해법으로 제시돼 왔지만 어떤 구성요소가 실제로 성능을 이끄는지, 그 이득이 분포 변화에서도 유지되는지 불분명하다는 문제의식에서 출발한다. 저자들은 특화 탐지기, 탐지기별 triage, 충돌 인식 증거 중재로 구성된 학습 없는 agentic 프레임워크를 6개 구성·3개 MLLM 백본으로 in-distribution과 out-of-distribution 모두에서 분해 분석한다. 단순한 탐지기 융합은 진짜 이미지에서 심각한 false positive를 내고, triage와 프롬프팅은 신뢰할 수 없는 증거를 걸러내며 탐지기 한계를 드러내 성능을 일관되게 높이지만, 지배적 요인은 추론 자체로 더 강한 judge가 특히 분포 변화에서 약한 judge를 크게 앞선다. 조작 재현율은 모든 구성에서 거의 포화돼, open-world 이미지 포렌식의 핵심 난점이 조작 탐지가 아니라 특화 도구에 대한 신뢰 보정과 상충 증거 중재임을 시사한다.

**코드**: 불명

**태그**: forgery-detection, calibration, vlm

---

### [MECAIL: Communication-Aware Incremental Learning for Object Detection with 14.6 KB Spatiotemporal Experts](https://arxiv.org/abs/2609.24455)

**한 줄 요약**: 엣지 기기에 V2X·Wi-Fi·2G~5G로 안정적으로 전송 가능한 14.6 KB 상한 안에서, 고정 base 검출기를 특정 시공간 맥락에 적응시키는 전문가 모듈 기반 증분학습 방법.

**핵심 기여**: 지능형 교통 시스템은 증분학습이 필요하지만 대부분의 엣지 기기가 온디바이스 학습 자원이 없어 중앙 서버에서 갱신을 전송받아야 하며, 저자들은 이 구조를 주차장·주유소·페리·공사 구간 같은 구체적 시공간 맥락마다 고정 base 모델을 적응시키는 조밀한 특화 모듈 커버리지를 얻는 데 쓰자고 제안한다. 다만 TCP·UDP·BTP를 V2X·Wi-Fi·2G~5G 하드웨어 위에서 신뢰성 있게 쓰려면 첫 TCP 윈도에 들어가고 UDP/BTP 단편화를 최소화해야 하므로 모듈당 14.6 KB라는 엄격한 상한을 설정한다. MECAIL은 이 요구를 충족하는 첫 방법으로, 새 도메인·환경마다 base 모델을 적응시키는 작은 전문가 네트워크를 두는 Mixture-of-Experts 구성을 쓴다. D-RICO와 ODinW-13에서 파라미터가 훨씬 큰 방법들의 성능에 대체로 근접하면서 대역폭 효율적인 대규모 배포를 가능하게 한다.

**코드**: 불명

**태그**: continual-learning, object-detection, peft, efficient-inference

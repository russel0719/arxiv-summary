# arXiv cs.CV Daily Digest — 2026-09-01 (arXiv 공개일)

- **전체 신규 논문 수**: 316편 (new 260 + cross-list 56)
- **선별 수**: 12편

## 오늘의 트렌드

목록에서 가장 큰 덩어리는 3D Gaussian Splatting 계열이다. 장기 볼류메트릭 비디오(ATGS), 동적 장면 분해(SMG, FractureFields), 재조명·스타일화(LightFuse, DReSG, OrnaStyler), sparse-view·feed-forward 재구성(GSPotential, ReconSplat, GeoRay)까지 표현 자체를 손보는 논문과 그 위에 편집·분할을 얹는 논문이 함께 몰려 있다. 두 번째 축은 video generation과 world model로, 자기개선 에이전트(CineForge, Matrix-Game 3.5), test-time noise/candidate 최적화(NoisEasier, diagnosis-guided recycling), 미관측 상태 추적 능력 검증(Can Video World Models Track Unobserved World States?)이 반복된다. VLM·MLLM 쪽은 hallucination 완화·span 검출·편향 감사(EviAnchor, SpanCalib-VLM, ContextBias, Guardrail-Agnostic Bias)와 visual token pruning(Cen-Prune, RegionCache, Elastic Token Compression)이 두 갈래로 나뉜다. 표현학습 계열에서는 동결된 foundation 백본(DINOv3, SAM 2, Depth Anything 3, CLIP)을 재학습 없이 재사용하거나 경량 어댑터만 붙여 태스크를 갈아 끼우는 흐름이 눈에 띄고, 검색·매칭 쪽에서는 실패 사례 기반 hard pair 생성, 쌍 단위 검증, open-set 임계값 보정처럼 임베딩 품질 자체를 겨냥한 논문이 나왔다. 응용에서는 산업 이상탐지·웨이퍼 결함, 위조·딥페이크·tamper localization, 의료 영상 분할, 원격탐사/UAV, document·OCR이 각각 군집을 이루며, 벤치마크와 감사 성격의 논문 비중이 전체의 상당 부분을 차지한다.

---

### [GramLoop: Training-Free Gram-Gated Replay for Robust Dense Prediction](https://arxiv.org/abs/2608.29113)

**한 줄 요약**: 동결된 DINOv3의 transformer 블록 일부를 추론 시 재실행하고 Gram 일관성으로 채택 여부를 판정해, 분포 변화 상황의 dense prediction을 학습 없이 개선한다.

**핵심 기여**: 가중치·태스크 어댑터·예측 헤드를 전혀 바꾸지 않고 백본 내부에 추론 연산만 추가해 분포 변화에 대응하려 하는데, transformer 블록을 반복 계산하면 DINOv3가 공간 구조를 유지하는 근거인 patch 간 관계가 깨진다는 점이 걸림돌이다. GramLoop은 짧은 transformer 구간을 replay한 뒤 각 제안을 동결된 후속 레이어로 전파해 최종 레이어의 cosine-Gram 일관성을 표준 DINOv3 경로와 비교하고, replay 구간 끝단에서 patch 단위 gate로 채택을 결정한다. corruption·perturbation·natural shift를 포함한 5개 변화 벤치마크 전부에서 동일 조건의 DINOv3 baseline을 앞서며, COCO-O에서 mAP +0.252, Effective Robustness +0.250을 기록하고 clean ADE20K 성능은 유지한다. 코드는 공개 예정이라고 밝혔다.

**태그**: ssl-backbone, foundation-model, segmentation, object-detection, efficient-inference

---

### [Evaluating 2D and 3D-Aware Vision Foundation Models for Vehicle Attribute Recognition](https://arxiv.org/abs/2608.29929)

**한 줄 요약**: 14개 2D·3D-aware vision foundation model을 동결 특징 추출기로 linear probing해 차량 type/make/model 인식 성능을 비교한 벤치마크.

**핵심 기여**: vision foundation model의 전이성은 널리 보고됐지만 fine-grained 차량 분류에서의 실효성, 특히 차량이 본질적으로 3차원 구조물이라는 점 때문에 3D-aware 모델이 표준 2D 구조보다 유리한지가 불명확하다는 문제를 다룬다. UFPR-VeSV 데이터셋에서 14개 모델을 동결한 뒤 linear probing으로 type·make·model 인식을 평가하고, 상위 모델들을 few-shot과 OOD 도메인 변화 조건에서 추가 검증한다. 표준 2D self-supervised 모델, 특히 DINOv3가 fine-grained 태스크에서 3D-aware 모델을 크게 앞서 make·model 인식 Macro-Accuracy 93% 이상을 달성했고, 반면 3D-aware Depth Anything v2는 차량 type 분류에서 시야각 변화에 더 강한 불변성을 보였다. 논문은 2D·3D prior를 결합하는 hybrid 접근을 후속 방향으로 제시하며 코드를 공개했다.

**태그**: ssl-backbone, foundation-model, fine-grained, image-embedding, dataset-benchmark

---

### [FoundYou: A Unified Model for Personalized Segmentation and Retrieval](https://arxiv.org/abs/2608.29917)

**한 줄 요약**: SAM 2가 프레임 간 객체 정체성을 유지하도록 학습된 성질을 이용해 독립된 이미지 사이의 인스턴스 정합으로 personalized segmentation과 retrieval을 한 프레임워크에서 처리한다.

**핵심 기여**: personalized segmentation과 personalized retrieval은 모두 서로 다른 이미지에서 동일한 물리적 객체를 찾는 인스턴스 수준 목표를 공유하는데도 별개 태스크로 발전해 왔다는 점에서 출발한다. FoundYou는 비디오 프레임 간 객체 정체성 보존을 학습한 SAM 2가 이미 인스턴스 수준 단서를 담고 있다고 보고, 이 성질로 독립 이미지 간 객체를 매칭해 분할과 검색이 동일한 인스턴스 정합 과정의 두 결과로 나오게 한다. PerMIS에서 +18.4 mIoU, ILIAS에서 +17.8 mAP를 얻고 category-level retrieval 벤치마크에서도 SOTA를 기록하며, few-shot personalized retrieval과 유연한 prompt 기반 promptable personalized segmentation으로 확장된다. SAM 2-small을 완전히 동결한 채 학습 파라미터 5.9M만 추가해 총 52M 규모이며, 기존 유일한 통합 방법 대비 75배 이상 빠르고 20배 작다. 코드가 공개돼 있다.

**태그**: image-retrieval, segmentation, correspondence, foundation-model, re-identification

---

### [XDG: Accelerated Visual Disambiguation](https://arxiv.org/abs/2608.29733)

**한 줄 요약**: Depth Anything 3에 LoRA를 붙이고 camera token을 쌍 단위 분류 토큰으로 재활용해, 이미지쌍이 같은 3D 표면을 보는지 판정하는 doppelganger 판별을 3배 이상 가속한다.

**핵심 기여**: 시각적으로 유사하지만 물리적으로 다른 표면이 잘못된 이미지 매칭을 만드는 visual aliasing(doppelganger) 문제는 SfM의 고질적 난점이고, 기존 완화책은 geometry-aware foundation 특징 위에 무거운 transformer 분류기를 얹어 대규모 처리 비용이 커진다. XDG는 3D foundation model이 이미 disambiguation에 필요한 cross-view 기하 추론을 수행하고 있으므로 별도 디코더에서 쌍 추론을 다시 배울 필요가 없다고 보고, Depth Anything 3를 경량 LoRA 어댑터로 미세조정한 뒤 camera token을 쌍 수준 분류 토큰으로 재해석해 compact MLP 헤드가 동일 표면 여부를 예측하게 한다. pairwise·reconstruction 벤치마크에서 SOTA 대비 경쟁력을 유지하면서 3배 이상의 추론 가속을 얻고, 수천 장 규모의 LaMAR 개별 장면에서 disambiguation 처리 시간을 10시간 이상 단축한다. 코드가 공개돼 있다.

**태그**: feature-matching, correspondence, foundation-model, peft, efficient-inference

---

### [DiffSAC: Diffusion-guided Sampling for Consensus-based Robust Estimation](https://arxiv.org/abs/2608.30603)

**한 줄 요약**: diffusion model로 유효한 minimal set의 분포를 학습해, RANSAC 계열의 가설 평가 횟수를 수만 개에서 수십 개로 줄이는 sampling 모듈.

**핵심 기여**: sample consensus 기반 robust estimation은 가설 평가 전에 좋은 minimal set을 골라내지 못해 샘플링이 비효율적이라는 한계를 지적한다. DiffSAC은 데이터 포인트를 순위 매기는 기존 방식 대신 각 포인트가 좋은 minimal set에 속하는지에 대한 confidence를 diffusion model로 refine하고, 정제 방향을 제약하기 위해 기하 특징을 diffusion의 조건으로 넣어 소수의 고품질 minimal set만 출력한다. 기존 방법이 1만 개 이상의 가설을 평가해야 하는 것과 달리 수십 개의 가설만으로 SOTA 성능에 도달하며, 5개 고전 비전 태스크에서 성능을 검증했다. diffusion sampling accelerator로 실시간 동작이 가능하고 기존 sample consensus 방법에 plug-and-play 모듈로 붙일 수 있다고 밝혔다.

**태그**: feature-matching, correspondence, robust-estimation, efficient-inference

---

### [RePair: Turning Retrieval Failures into Counterfactual Hard Pairs](https://arxiv.org/abs/2608.29604)

**한 줄 요약**: 검색 실패로 상위에 오른 false positive를 counterfactual 발판으로 삼아 최소 편집으로 hard positive/negative 쌍을 만들어 dual encoder를 학습한다.

**핵심 기여**: CLIP 계열 dual encoder의 실무 정확도는 상위 오답이 정답과 단 하나의 결정적 세부만 다른 국소적 의미 구분에서 갈리는데, hard-sample mining은 혼동 후보를 고를 뿐 교정된 짝을 만들지 못하고 합성 증강은 실제 실패에 조건화되지 않아 무관한 난이도 축을 건드린다는 점을 문제로 삼는다. RePair는 상위 false positive가 쿼리 의미 대부분을 공유하면서 실패를 유발하는 국소 residual만 다른 counterfactual 발판이라고 보고, Validity·Minimality·Locality 세 원칙 아래 false positive를 양방향으로 마이닝한 뒤 LLM 기반 counterfactual 편집으로 residual만 교정해 결정 경계를 가로지르는 hard pair를 만들고 local hard-pair contrastive 목적함수로 학습한다. Flickr30K와 COCO30K에서 합성 샘플 107K만으로 통제된 증강 baseline을 앞서며, 이는 비교 대상보다 26~75% 적은 양이다.

**태그**: image-retrieval, metric-learning, image-embedding, vlm

---

### [Hyper3-CLIP: Hierarchy-Conditioned Hyperbolic Vision-Language Training](https://arxiv.org/abs/2608.29313)

**한 줄 요약**: hyperbolic 임베딩의 entailment 목적함수와 query-conditioned visual pooling을 결합해 part-whole·parent-child 관계를 담는 CLIP 학습 방식.

**핵심 기여**: contrastive CLIP류 VLM은 강한 global image-text 표현을 배우지만 Euclidean 임베딩과 global pooling 때문에 part-whole·parent-child 같은 관계 구조를 담지 못하고, 이를 다루는 hyperbolic VLM과 text-conditioned 변형은 서로 분리된 채 발전해 왔다는 문제를 지적한다. Hyper3-CLIP은 전체 캡션·문장 조각·국소 부위 설명·추출 구절로 구성된 경량 query hierarchy를 텍스트에서 만들고, 각 query가 visual patch pooling을 조건화하도록 해 image-text, whole-part, parent-child entailment 손실을 함께 걸며 global·local·global-local contrastive 학습을 결합한다. query-conditioned pooling은 학습 시에만 활성화된다. COCO·Flickr에서 R@5·R@10 검색 성능과 VOC·COCO multi-label 분류가 개선되고 hierarchy 지표에서도 경쟁력을 유지하며, 고정 prompt 조건에서의 zero-shot prompt 민감도 감사와 학습에 쓰인 GRIT part budget의 영향을 함께 분석한다. 코드가 공개돼 있다.

**태그**: image-retrieval, image-embedding, metric-learning, vlm

---

### [Open-Set Cattle Muzzle Identification: A Leakage-Controlled Benchmark and Evaluation Protocol](https://arxiv.org/abs/2608.28663)

**한 줄 요약**: 소 비문 인식을 open-set gallery 기반 식별로 재정의하고, 누출 통제 평가 프로토콜에서 임계값 보정이 실제 성능을 크게 좌우함을 보인다.

**핵심 기여**: 기존 비문 인식 시스템은 등록된 개체의 closed set을 가정해 배포에 제약이 있다는 점에서, 미등록 개체를 거부하고 재학습 없이 점진적 등록을 지원하는 open-set gallery 식별 문제로 문제를 재구성한다. identity-disjoint split, fold별 재학습, held-out 임계값 보정, 중복 제거 검증, bootstrap 신뢰구간으로 구성된 누출 통제 프로토콜을 도입하고, CNN-ViT 하이브리드 metric learning 모델과 MegaDescriptor-L foundation model 두 임베딩 구성을 비교한다. oracle 임계값에서는 하이브리드가 FAR 10⁻¹/10⁻²/10⁻³에서 DIR 98.3%/96.4%/93.6%, MegaDescriptor-L이 99.3%/98.1%/96.1%를 기록하지만, 배포 가능한 임계값 보정에서는 목표 FAR 1%에 대해 하이브리드가 1.03%, MegaDescriptor-L이 2.44%를 보여 oracle과 보정 성능 사이에 큰 격차가 드러난다. 점진적 등록은 참조 이미지 1장으로 Rank-1 91% 이상, 8장으로 97.3%까지 오르며 재학습이나 기존 gallery 성능 저하 없이 동작한다.

**태그**: metric-learning, re-identification, image-embedding, image-retrieval, foundation-model

---

### [OPUS: A Simple yet Effective Unified Framework for Open-Vocabulary Detection](https://arxiv.org/abs/2608.30247)

**한 줄 요약**: DINOv3-ConvNeXt 백본과 prompt-aware 디코더만으로 텍스트·visual exemplar·혼합 prompt를 한 번에 처리하는 단순화된 open-vocabulary detector.

**핵심 기여**: 이질적 prompt를 지원하는 통합 OVD가 무거운 cross-modal fusion, 단계별 학습, 반복 주석 파이프라인 같은 복잡한 설계로 흐르고 있다고 보고, 더 강한 foundation model 시대에 그런 복잡성이 필요한지 재검토한다. OPUS는 DINOv3-ConvNeXt-B 기반의 semantic-rich visual encoder에 효율적 hybrid encoding을 붙이고, prompt별 분기를 두지 않는 prompt-aware 디코더로 텍스트·interactive visual·generic visual·혼합 prompt를 처리하며, Instance-level Contrastive Alignment을 쓰는 1단계 text-visual 학습과 SAM3 기반 single-pass 데이터 엔진으로 학습된다. COCO·LVIS-minival·ODinW35에서 Visual-I 성능 68.1/69.2/54.7 AP로 SOTA를 기록하면서 Text·Visual-G 정확도의 균형을 유지하고, 혼합 prompt가 간섭이 아니라 상호 보완으로 작동해 단일 prompt보다 개선된다고 보고한다.

**태그**: open-vocab-detection, object-detection, ssl-backbone, foundation-model

---

### [InspectorGPT: A Comparative Reasoning Enhanced VLM for Comprehensive Industrial Anomaly Detection](https://arxiv.org/abs/2608.29783)

**한 줄 요약**: 정상 참조 이미지와 쿼리 이미지를 비교하는 인간 검사 방식을 VLM에 내재화해 추론·판정·픽셀 단위 마스크를 함께 내는 산업 이상탐지 프레임워크.

**핵심 기여**: 정상 특징 분포를 모델링하는 비지도 방법은 미지 카테고리 일반화가 어렵고, VLM을 쓰는 zero-shot 방법도 문제가 있다고 지적한다. 특히 reasoning 지향 post-training이 이상 판별 능력을 붕괴시켜 미세조정된 모델이 base VLM보다 나빠지는 경우를 관찰하고, 기존 방법이 텍스트 판정이나 거친 박스만 주고 픽셀 단위 분할을 제공하지 않는다는 점도 문제로 든다. InspectorGPT는 정상 참조와 쿼리를 비교해 불일치를 찾는 comparative reasoning을 중심에 두고, Chain-of-Thought 미세조정과 검증 가능한 보상을 설계한 GRPO로 이 능력을 내재화하며, 픽셀 단위 마스크를 위한 InspectorGPT-Seg를 별도로 둔다. 분할 감독이 이상 판별을 개선하지만 의미 추론을 약화시키고 joint 학습으로는 균형이 안 잡혀 두 분기를 따로 학습한 뒤 task-vector fusion으로 결합했고, 미학습 벤치마크로의 일반화를 포함한 다차원 성능을 보고한다.

**태그**: anomaly-detection, industrial-inspection, defect-detection, vlm, segmentation

---

### [NFAD: Nuisance-Filtered Anomaly Detection Under Distribution Shift](https://arxiv.org/abs/2608.29112)

**한 줄 요약**: 조명·배경·시점 변화가 특징 공간에 만드는 nuisance 부분공간을 추정해 이상 residual에서 제거함으로써 촬영 조건 변화에 강한 이상탐지를 만든다.

**핵심 기여**: 산업 검사용 이상탐지 벤치마크 성능이 포화에 가까워졌지만 이 벤치마크들이 통제된 촬영 조건에서 수집돼, 조명·배경·시점 등 환경 변화가 정상 샘플을 학습된 정상 분포에서 밀어내면 오탐이 발생한다는 문제를 다룬다. NFAD는 이상 라벨이나 타깃 도메인 데이터 없이, 내용을 보존하는 perturbation이 유발한 특징 변위 쌍에서 nuisance 부분공간을 추정하고 추론 시 이 성분의 이상 residual 기여를 억제한다. 같은 부분공간이 이미지 수준 검출을 위한 full projection과 픽셀 수준 국소화를 위한 selective suppression 두 분기를 지원해 국소 결함의 증거는 남긴다. 촬영 조건 변화를 겨냥한 AeBAD-S에서 이미지 수준 AUROC 91.0%로 SOTA를 기록하면서 VisA·Real-IAD·MVTec AD 같은 표준 벤치마크에서도 경쟁력을 유지한다.

**태그**: anomaly-detection, industrial-inspection, defect-detection, image-embedding

---

### [Foundation and Multimodal Large Language Models for Face Presentation and Morph Attack Detection](https://arxiv.org/abs/2608.29802)

**한 줄 요약**: 16개 open-weight MLLM과 30개 vision encoder를 zero-shot prompting부터 fine-tuning까지 5단계 접근으로 비교해, 범용 사전학습 표현이 얼굴 PAD·MAD 정보를 담고 있는지 검증한다.

**핵심 기여**: 얼굴 인식 시스템의 presentation attack detection(PAD)과 morphing attack detection(MAD)은 기존 검출기가 일반화에 한계가 있어 cross-dataset 평가에서 성능이 떨어진다는 문제를 다룬다. 범용 foundation model과 MLLM이 PAD·MAD 관련 정보를 인코딩하는지, 그리고 어떤 방식으로 활용해야 하는지를 모델 내부 정보 접근 수준이 점차 높아지는 5개 접근(off-the-shelf MLLM zero-shot prompting, 출력 logit 확률 위의 shallow model 학습, 태스크별 QA 데이터로 PEFT해 텍스트 근거까지 내는 PADLLM·MADLLM, 동결 vision encoder linear probing, vision encoder fine-tuning)으로 비교한다. 16개 open-weight MLLM과 30개 vision encoder 백본을 PAD 4개(MSU-MFSD, CASIA-FASD, Replay-Attack, OULU-NPU)·MAD 4개(FFHQ, FRGC, FRLL, FERET) 데이터셋에서 벤치마킹했고, 미세조정 모델이 cross-dataset 평가에서 SOTA 검출 성능에 도달해 범용 사전학습 표현이 상당한 공격 관련 정보를 담고 있음을 보인다. 전 실험 소스코드는 공개 예정이라고 밝혔다.

**태그**: forgery-detection, foundation-model, peft, vlm, dataset-benchmark

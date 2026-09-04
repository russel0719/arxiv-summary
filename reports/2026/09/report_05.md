# arXiv cs.CV Daily Digest — 2026-09-04 (arXiv 공개일)

- **전체 신규 논문 수**: 112편 (new 102 + cross-list 10)
- **선별 수**: 11편

## 오늘의 트렌드

목록에서 가장 두꺼운 군집은 world model과 video generation이다. 물리 법칙 위반을 검증 가능한 의무 조항으로 컴파일해 감사하는 평가 시스템(VeriPhy, Principia), 세그먼트를 이어붙일 때 세계 상태가 유지되는지 묻는 벤치마크(Statebench/Stateagent), Unreal Engine 기반 사전학습 데이터 파이프라인, 카메라 조건부 world model의 보상 모델링(WorldReward), 네이티브 3D 상태를 갖는 통합 멀티모달 모델(Puffin-World)이 같은 날 올라왔고, 3D Gaussian Splatting 쪽에서도 학습 가속(Laplacian Frequency Hierarchies, TruncGradGS), 대규모 항공 표면 재구성(STARS-GS), 점 기반 표현의 기하·텍스처 편집(PointGT, P-CORE)이 별도 블록을 이룬다. 두 번째 축은 시각 토큰 예산을 어떻게 쓸 것인가다. 제거된 토큰의 대표성을 기준으로 삼는 pruning(CoverPruner), 프레임 선택·공간 압축·재투자를 하나씩 통제해 비교한 연구(Select, Compress, Reinvest), 인코딩 이전 단계로 필터링을 앞당긴 스트리밍 이해(CoFiE), 입력 적응형 해상도·폭 조절(ProgResViT), 생체 시각에서 착안한 foveation(Efficient Semantic Understanding from Digital Foveation)이 모두 같은 문제를 다른 지점에서 건드린다. VLM 계열은 성능 주장보다 진단·감사가 주류로, 의료 MCQ의 지름길 경로 분해(MedQA-MM), 동결 VLM이 이미지 없는 객체 토큰 편집에 반응하는 조건 탐색, 토큰 단위 안전 개입(SafeRI)이 나란히 등장했다. 산업 응용 쪽은 CAD로 축이 옮겨가 실제 설계 의도에서 파라메트릭 프로그램을 생성하는 벤치마크와 foundation model suite(RealCADBench, VisCAD)가 함께 공개됐고, 이상 탐지는 task 경계 없는 연속 학습과 few-shot 설정으로 세분화되는 흐름이다. 이 밖에 의료 영상(유방촬영 VLM, 각막 OCT, 뇌 MRI inpainting), 원격탐사 CLIP 확장, 검색·임베딩(생성형 크로스모달 검색, MLLM 임베딩의 구성적 추론), OCR 진단·복구 및 경량 문서 파싱이 각각 소규모 군집을 형성한다.

---

### [PL-SCEA: Reconfiguring Pretrained Attention for Few-Shot Industrial Anomaly Detection](https://arxiv.org/abs/2609.03655)

**한 줄 요약**: 동결된 vision foundation model의 attention 계산을 토큰 자기상관 기반으로 재구성해 few-shot 산업 이상 탐지의 국소 결함 위치추정을 개선한다.

**핵심 기여**: VFM의 attention은 semantic aggregation을 목표로 한 사전학습 목적함수에서 물려받은 것이라, semantic 인식을 뒷받침하는 토큰 관계가 이상 위치추정에 필요한 국소 텍스처·구조 편차를 충분히 드러내지 못한다는 불일치를 지적한다. PL-SCEA는 사전학습된 query-key attention의 semantic context를 유지한 채 contextualized value feature 위에서 토큰 적응적 자기상관을 구성하고, 양의 상관만 남기는 필터링과 power-law 재가중으로 각 토큰의 관계적 배경 대비 두드러진 관계를 강조한다. 학습 가능한 attention projection을 추가하지 않으며, 이렇게 얻은 특징을 경량 variational autoencoder로 모델링해 카테고리별 정상성의 고정 크기 재구성 표현을 만든다. MVTec AD와 VisA의 few-shot 설정에서 image-level 탐지는 경쟁력 있는 수준, pixel-level localization은 일관되게 강한 결과를 보고하며, ablation에서는 VAE 대신 memory bank를 써도 localization이 개선된다고 밝혔다.

**태그**: anomaly-detection, industrial-inspection, foundation-model, defect-detection

---

### [Neural-Collapse-guided Task-Free Continual Anomaly Detection](https://arxiv.org/abs/2609.03406)

**한 줄 요약**: task 경계 없이 흘러들어오는 산업 데이터 스트림에서 특징을 simplex ETF 프로토타입 공간에 정렬해 표현 드리프트를 억제하는 이상 탐지 프레임워크.

**핵심 기여**: 실제 제조 환경은 데이터 분포가 예측 불가능하게 변해 task 의존적 continual learning 가정이 성립하지 않는다는 문제의식에서, 산업 이상 탐지를 task-free continual learning 문제로 정식화한다. NC-TFAD는 사전학습 백본을 동결하고 스트리밍 특징을 neural collapse에서 착안한 simplex Equiangular Tight Frame 프로토타입 공간에 정렬해 비정상 스트림에서도 표현 기하를 안정화하며, 실제 이상 샘플이 없는 상황을 메우기 위해 합성 이상 샘플을 보조 앵커로 생성한다. 여기에 클래스 간·내 정규화와 Focal Neural Collapse Contrastive(FNCC) 손실을 더해 정상-이상 분리도를 높이고, 정상 patch 프로토타입 기반 localization 분기가 픽셀 단위 주석 없이 보정된 편차 맵과 약한 self-attention prior를 융합해 이상 히트맵을 만든다. MVTec AD와 VisA의 task-free continual 프로토콜에서 일반 비전에서 가져온 task-free continual learning 기법들과 통합 이상 탐지 baseline을 image-level 탐지·pixel-level localization 양쪽에서 앞선다고 보고한다.

**태그**: anomaly-detection, industrial-inspection, defect-detection, continual-learning

---

### [Catalogue Photography as a Cold Start: Toward Deployable Carbide Burr Recognition](https://arxiv.org/abs/2609.03995)

**한 줄 요약**: 라벨 이미지가 전혀 없는 상태에서 제조사 카탈로그 사진만으로 초경 로터리 버 인식을 학습했을 때 현장 사진으로 얼마나 전이되는지 측정한다.

**핵심 기여**: 밀링 공구·초경 로터리 버 배치가 생산 지시서와 일치하는지 검증하는 품질보증 작업은 대체로 수작업이며, 이를 자동화하려 해도 라벨된 이미지가 없어 카탈로그 사진이 유일한 감독 신호가 되는 cold-start 제약에 부딪힌다. 논문은 head shape과 tooth profile 두 속성에 대해 동결된 off-the-shelf 특징 추출기가 신뢰할 만한 분리를 만들지 못함을 보인 뒤 표적 표현학습으로 넘어가, metric learning이 카탈로그 이미지에서는 거의 완벽한 비지도 군집 발견(adjusted Rand index 0.94–0.97)을 달성하지만 그 이득의 절반 미만만 현장 사진으로 전이된다고 보고한다. 전이 이득이 가장 컸던 것은 모델 규모나 표현 복잡도가 아니라 도메인 민감도를 낮추는 단순한 조치로, grayscale 변환이 +0.22, 알려진 지시서를 이용한 Hungarian assignment 제약 검색이 +0.11을 더했다. 저자들은 카탈로그 사진을 배포 가능한 학습 도메인이 아니라 cold start 자원으로 규정하고, catalogue-to-field 전이를 위한 경험적 baseline과 평가 프로토콜을 제시한다.

**태그**: metric-learning, image-retrieval, fine-grained, industrial-inspection

---

### [CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation](https://arxiv.org/abs/2609.04083)

**한 줄 요약**: 같은 backbone을 cross-attentive reranker로 썼을 때의 세밀한 순위 판단을 listwise KL 목적함수로 임베딩 모델에 증류한다.

**핵심 기여**: MLLM 기반 임베딩 모델은 같은 개념이 등장하지만 속성-객체 결합이 다른 장면을 구분하지 못하는 반면, 동일한 backbone을 cross-attentive reranker로 사용하면 그 구분이 가능하다는 관찰에서 출발한다. CORE는 다섯 단계의 구성적 매칭 수준에 걸친 후보 리스트를 합성하고, reranker의 세밀한 순위를 임베딩 모델이 재현하도록 하는 Rank-KL 목적함수를 도입하며, 등급이 매겨진 평가 프로토콜 아래 동일한 데이터·튜닝 예산으로 contrastive learning, pairwise CoSENT, listwise Rank-KL을 비교해 다단계 감독을 Rank-KL이 가장 잘 활용함을 보인다. COLA·SUGARCREPE++·NEGBENCH 세 벤치마크에서 CORE-RERANKER-8B가 총평균 82.7%로 Jina-Reranker를 10.7점 앞서고, CORE-EMBED-8B는 평가된 임베딩 모델 중 최고 총평균 0.666을 기록한다. 개선은 MCMR 벤치마크로도 전이되며 COCO·Flickr30K 검색 성능은 유지된다.

**태그**: image-embedding, image-retrieval, metric-learning, distillation, vlm

---

### [WIDE: Wildcard Inference with Dynamic Expansion for Cross-Modal Generative Retrieval](https://arxiv.org/abs/2609.03554)

**한 줄 요약**: 생성형 크로스모달 검색에서 쿼리에 없는 세부를 억지로 생성하게 만드는 trie 제약 beam search 대신 wildcard를 내보내 탐색 공간을 동적으로 넓힌다.

**핵심 기여**: 생성형 검색을 크로스모달로 확장하면 짧은 텍스트 쿼리와 밀도 높은 시각 후보 사이의 정보 비대칭 때문에, 표준 trie 제약 beam search로 식별자를 생성하는 autoregressive 디코더가 쿼리에 없는 세부를 맞히지 못했다는 이유로 크게 페널티를 받아 무관한 후보가 상위 순위를 차지하는 forced hallucination이 발생한다. WIDE는 Adaptive Entropy Thresholding(AET)으로 레이어별 불확실성 경계를 오프라인에서 보정하고, 디코딩 단계에서 Asymmetry-aware Wildcard Decoding(AWD)이 의미적 사각지대를 감지해 확정적 식별자 대신 wildcard를 내보내 log-probability 페널티 없이 탐색 공간을 확장하며, Blind-Spot Re-ranking(BSR)이 이산 생성 신뢰도와 연속 의미 유사도를 결합한 하이브리드 점수로 확장된 후보 풀을 평가한다. M-BEIR 벤치마크에서 기존 state-of-the-art 생성형 검색 기법을 앞서면서 인덱스 구조는 compact하게 유지한다고 보고한다.

**태그**: image-retrieval, image-embedding, vlm

---

### [FoRIS: Progressive Foreground Refinement for Training-Free In-Context Segmentation](https://arxiv.org/abs/2609.03384)

**한 줄 요약**: in-context segmentation을 reference-query 매칭으로 마스크를 한 번에 예측하는 대신 전경을 점진적으로 정제하는 coarse-to-fine 과정으로 재해석한다.

**핵심 기여**: In-Context Segmentation은 주석된 시각 예시 한두 장으로 객체나 부위 같은 임의의 의미 개념을 분할하는 과제이며, 기존 접근은 reference-query 매칭을 통해 최종 마스크를 직접 예측한다. FoRIS는 이를 고전적 분할 관점의 점진적 정제 과정으로 다시 보고, Foreground Purification·Foreground Localization·Foreground Consolidation 세 단계로 배경 방해를 억제하고 판별력 있는 표적 영역을 찾은 뒤 semantic aggregation으로 완전한 전경 구조를 복원한다. 학습이 필요 없는 프레임워크로 semantic segmentation과 part segmentation에서 기존 기법 대비 1-shot 평균 4.5 mIoU, 5-shot 평균 4.8 mIoU 향상을 보고하며 코드를 공개했다.

**태그**: segmentation, correspondence, foundation-model

---

### [ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation](https://arxiv.org/abs/2609.03756)

**한 줄 요약**: 텍스트 프롬프트 분할 모델의 시간적 환각·공간 분절·의미 오분류를 시각 임베딩 매칭과 조건부 VLM 검증 계층으로 걸러낸다.

**핵심 기여**: SAM 3를 포함한 최신 텍스트 프롬프트 분할 모델이 대상이 화면 밖으로 나가도 부재를 보고하지 못하고, 극단적 클로즈업에서 객체 전체 대신 국소 텍스처를 분할하며, 조각상·그림·반사처럼 시각적으로 유사한 인공물을 표적 개체로 분할하는 실패 양상을 지적한다. ENEAS는 하나의 방법으로 두 갈래를 다루는데, 추적 쪽은 점 입력에만 대응하던 SeC 구조에 텍스트 프롬프트 어댑터를 붙여 시간 메모리를 활용함으로써 대상이 사라져도 distractor로 표류하지 않고 화면을 가득 채워도 전체를 유지하게 하고, 발견 쪽은 고속 시각 임베딩 매칭에 모호한 후보에 한해서만 VLM 추론을 호출하는 검증 계층을 결합해 지연을 낮게 유지하면서 시각 정보만으로는 구분할 수 없는 존재론적 오류를 걸러낸다. 영상뿐 아니라 시간·공간 순서가 없는 데이터 모음에도 적용되도록 설계했으며 코드와 모델을 공개했다.

**태그**: segmentation, image-embedding, vlm, video

---

### [ProgResViT: Progressive Resolution and Width for Adaptive Vision Transformers](https://arxiv.org/abs/2609.03216)

**한 줄 요약**: 저해상도·좁은 서브네트워크로 시작해 예측이 확신되면 멈추고 아니면 해상도와 폭을 키워 이어가는 입력 적응형 ViT.

**핵심 기여**: ViT는 상당수 이미지가 훨씬 적은 연산으로 분류될 수 있는데도 모든 입력을 고정 해상도·고정 폭으로 처리한다는 문제의식에서 출발한다. ProgResViT는 여러 라운드에 걸쳐 점진적으로 추론해 첫 라운드에서 저해상도 이미지를 좁은 서브네트워크로 처리하고, 예측이 충분히 확신되면 종료하며 그렇지 않으면 현재 라운드의 표현을 재사용해 더 높은 해상도와 더 넓은 서브네트워크로 예측을 정제한다. 모든 라운드가 단일 백본을 공유하므로 현재 라운드·블록·입력 해상도에 조건화해 토큰 융합과 레이어 출력을 조절하는 Progress-Conditioned Soft Gating(PSG)을 제안한다. DeiT에 적용하면 adaptive-width·adaptive-depth·dynamic-token baseline보다 나은 정확도-연산 트레이드오프를 얻고, 지식 증류를 결합한 DeiT 기반 ProgResViT는 비교 가능한 평가 설정에서 top-1 84.9%로 보고된 DeiT-III-S를 소폭 웃돈다. 동일한 설계가 self-supervised DINO 표현과 downstream semantic segmentation에서도 유리한 트레이드오프를 준다고 밝혔고 코드를 공개했다.

**태그**: efficient-inference, ssl-backbone, distillation, foundation-model

---

### [Who Speaks for the Pruned? Visual Token Pruning as Coverage Optimization](https://arxiv.org/abs/2609.03158)

**한 줄 요약**: 어떤 토큰을 남길지가 아니라 제거된 토큰을 어떤 생존 토큰이 대표하는지를 묻는 커버리지 최적화로 VLM 시각 토큰을 가지친다.

**핵심 기여**: 기존 visual token pruning은 대부분 유지할 토큰만 묻기 때문에, 점수가 높지만 중복된 토큰을 남기면서 버려진 근거는 가까운 대표 없이 사라질 수 있다. CoverPruner는 토큰이 제거된 뒤 대상 VLM 입장에서 어떤 원본 생존 토큰이 그것을 대표하는가라는 수요 측 질문을 던지고, 이를 Representational Coverage Maximization(RCM)으로 정식화해 쿼리 가중 수요를 반영하며 투영된 시각 토큰 집합 전체를 덮도록 한다. RCM은 projector 공간 커버리지와 경량 first-layer attention probe로 구현되며 별도 학습이 필요 없다. 여러 VLM 구조와 압축률에서 비교 대상 중 최고 평균 정확도를 얻고, 이득은 대체로 공격적인 압축 구간에서 가장 크게 나타난다.

**태그**: efficient-inference, vlm, foundation-model

---

### [The impact of phase information for few-shot fine-grained image classification](https://arxiv.org/abs/2609.03829)

**한 줄 요약**: 주파수 영역의 위상 정보를 진폭과 함께 결합하는 plug-and-play 모듈로 few-shot fine-grained 분류의 특징 기술자를 보강한다.

**핵심 기여**: Few-shot fine-grained image classification은 라벨된 예시가 적은 상태에서 서로 유사한 이미지를 구분해야 하는데, 이미지 내부의 구조적 관계를 담는 위상 정보가 충분히 활용되지 않았다고 지적한다. 논문은 국소·전역 주파수의 진폭과 위상 정보를 함께 결합해 더 포괄적인 특징 기술자를 얻는 plug-and-play amplitude-phase integration(API) 모듈을 제안하고, 위상 기반 공간 정보와 주파수 정보를 적응적으로 융합하는 PSF-Net을 구성해 표준 episodic training 구조에 넣어 처음부터 end-to-end로 학습할 수 있게 한다. 공개 데이터셋 5종 실험에서 기존 state-of-the-art 벤치마크를 앞선다고 보고하지만, 초록에는 구체적인 정량 수치가 제시돼 있지 않다.

**태그**: fine-grained, image-embedding, metric-learning

---

### [Preserving Knowledge across Space and Time for Continual Video Deepfake Detection](https://arxiv.org/abs/2609.03446)

**한 줄 요약**: 딥페이크 영상 특징을 주파수 영역에서 공간·시간·시공간 모달리티로 분해해 각각을 따로 보존하는 continual 탐지 프레임워크.

**핵심 기여**: 고품질 딥페이크 영상이 계속 등장해 탐지기가 새 위조 패턴에 지속적으로 적응해야 하지만, 기존 접근은 딥페이크 이미지용으로 설계돼 영상 고유의 단서를 포착하지 못한다. 공간 아티팩트만 남는 이미지와 달리 딥페이크 영상은 공간축과 시간축 양쪽에 서로 다른 증거를 남기므로 순차적 모델 갱신 과정에서 각 모달리티를 따로 보존해야 한다는 것이 출발점이다. MSFD는 영상 특징을 주파수 영역에서 공간·시간·시공간 모달리티로 명시적으로 분해해 딥페이크 유형마다 공간·시간 단서 의존도가 다르다는 점을 반영하고, 시공간 표현이 단일 모달리티 단서와 직교하도록 유도하는 cross-modality decorrelation 손실을 함께 사용한다. 다양한 continual 딥페이크 영상 시나리오에서 state-of-the-art 대비 더 나은 적응과 성능 유지를 보고한다.

**태그**: forgery-detection, video, continual-learning

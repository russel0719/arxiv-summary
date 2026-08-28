# arXiv cs.CV Daily Digest — 2026-07-21 (arXiv 공개일)

- **전체 신규 논문 수**: 219편 (new 191 + cross-list 28)
- **선별 수**: 12편

## 오늘의 트렌드

오늘은 219편으로 물량이 매우 많은 날이었고, 관심사에 맞는 굵직한 논문도 여럿 나왔다. 첫째, **JEPA 계열의 재조명**이 눈에 띈다 — 학습 후 버려지던 JEPA predictor를 frozen 연산자로 CLIP·DINOv2/v3·MAE에 이식하는 연구와 depth 정규화 JEPA world model이 함께 나와, SSL 아키텍처의 부속 모듈을 재활용·강화하는 흐름이 형성되고 있다. 둘째, **유사도·매칭 축이 풍성하다**: 텍스트로 유사도 기준을 조건화하는 지각 metric(TPIPS), segment 수준 correspondence(MuViSeg), LightGlue 검증을 결합한 동물 re-ID 파이프라인, 열화 쿼리 임베딩 복구(DARA) 등 retrieval–verification 스택 전반을 커버한다. 셋째, **위조·조작 탐지 클러스터** — ChatGPT·Gemini류 VLM 편집 도구발 tampering에 대응하는 domain generalization 레시피, monocular 기하 단서를 쓰는 GFrame 등이 집중적으로 나왔다. 마지막으로 임베딩 모델 압축(Eddy-VL), depth foundation model의 tiny 모델화(DepthART) 등 **엣지 배포·증류** 연구도 꾸준하다.

---

### [The JEPA Predictor: A Transferable Operator for Occluded Feature Completion](https://arxiv.org/abs/2607.16274)

- **한 줄 요약**: JEPA 학습 후 버려지던 predictor를 frozen feature-completion 연산자로 재활용해, 선형 사영 하나로 CLIP·DINOv3·DINOv2·MAE 등 non-JEPA 백본에도 이식하는 연구.
- **핵심 기여**: predictor가 본래 visible-context feature에서 masked 위치 feature로 가는 학습된 연산자라는 점에 착안, I-JEPA/V-JEPA 2의 frozen predictor를 ImageNet 500장으로 closed-form fit한 선형 사영만으로 4개 non-JEPA 백본에 연결했다. mask 비율이 커질수록 이득이 단조 증가하며, heavy occlusion에서 CLIP+I-JEPA predictor 조합이 fine-grained Stanford Dogs 정확도를 15.9%에서 52.1%로 (+36pp) 끌어올렸다.
- **태그**: ssl-backbone, image-embedding, foundation-model, fine-grained

---

### [The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric](https://arxiv.org/abs/2607.18237)

- **한 줄 요약**: "어떤 측면(색·형태 등)에서 유사한가"를 텍스트 프롬프트로 조건화할 수 있는 지각적 이미지 유사도 metric(TPIPS)과 이를 위한 대규모 인간 triplet 판단 데이터셋.
- **핵심 기여**: 이미지 triplet마다 자유 형식의 여러 의미적 측면에 걸쳐 인간 유사도 판단을 수집한 대규모 데이터셋을 구축하고, frontier VLM들이 인간 합의에 크게 못 미침을 벤치마크로 보였다. 이 데이터로 VLM을 fine-tune한 TPIPS는 인간 지각과 더 잘 정렬되고 학습 분포 밖으로도 일반화하며, text-guided retrieval·compositional search·생성모델 평가라는 새 활용처를 연다. 코드·데이터·모델 공개.
- **태그**: image-retrieval, metric-learning, image-embedding, fine-grained, vlm

---

### [MuViSeg: Multi-View Segment Correspondences from Dense Geometry Priors](https://arxiv.org/abs/2607.17938)

- **한 줄 요약**: keypoint·픽셀이 아닌 instance segment 수준의 이미지 간 correspondence를 LightGlue 스타일 학습 matching head로 푸는 프레임워크 — 여러 뷰를 동시에 매칭하는 joint attention 확장 포함.
- **핵심 기여**: frozen MASt3R descriptor 위의 LightGlue식 attention head(DoubleSoftmax 스코어링), VGGT feature를 pooling 전에 살려 쓰는 DPT식 multi-scale fusion, 그리고 여러 뷰의 segment에 대한 joint self-attention으로 pairwise matcher가 못 잡는 transitive correspondence를 복원하는 multi-view 확장을 제안했다. 0~180도 시점 차 zero-shot 평가에서 Sinkhorn matcher 대비 Replica +4.85, Virtual KITTI 2 +25.9 AUPRC.
- **태그**: feature-matching, correspondence, segmentation, foundation-model

---

### [DS@GT ARC at AnimalCLEF 2026: Species-Aware Graph Construction for Multi-Species Animal Re-Identification](https://arxiv.org/abs/2607.16453)

- **한 줄 요약**: global descriptor 검색 + LightGlue local feature 재검증 + LightGBM pair scoring + Leiden clustering을 결합한 다종(多種) 동물 개체 re-ID 파이프라인.
- **핵심 기여**: re-ID를 species-aware graph construction으로 정식화하고, 높은 점수의 false pair가 bridge edge가 되어 서로 다른 개체를 transitive closure로 합쳐버리는 clustering 기반 re-ID의 핵심 실패 모드를 conservative edge admission으로 방어했다. ablation으로 local feature 검증, foreground 인지 전처리, 종별 백본 선택이 pair evidence를 강화함을 보였고 public ARI 0.733을 달성했다.
- **태그**: re-identification, feature-matching, image-retrieval, fine-grained

---

### [DARA: Degradation-Aware Low-Rank Residual Adaptation with Original-to-Corrupted Distillation for Corruption-Robust Animal Re-Identification](https://arxiv.org/abs/2607.16644)

- **한 줄 요약**: blur·noise·압축으로 열화된 쿼리의 임베딩을 feature-space에서 직접 복구하는 routed low-rank residual adapter — frozen re-ID 백본에 파라미터 0.49%만 추가하는 retrofit.
- **핵심 기여**: corruption-robust re-ID를 입력 조건부 feature 복구 문제로 재정의하고, corruption 종류 라벨 없이 라우팅되는 low-rank residual expert를 학습시켰다. 원본 이미지를 보는 teacher로 개체 임베딩과 retrieval 관계를 보존하는 original-to-corrupted distillation을 결합해, 4개 데이터셋에서 corrupted-query mAP gap의 77.0%를 회복하면서 FLOPs 증가는 0.05%에 그친다.
- **태그**: re-identification, image-retrieval, peft, distillation, image-embedding

---

### [Miles: Metric Learning with Expandable Subspace for Pre-Trained Model-Based Class-Incremental Learning](https://arxiv.org/abs/2607.17593)

- **한 줄 요약**: pre-trained model 기반 class-incremental learning에서 확장 가능한 subspace와 central loss로 새 클래스를 프로토타입 중심으로 클러스터링하는 metric learning 접근.
- **핵심 기여**: 학습 모듈을 백본에서 decouple하고 중간 feature의 prior 정보로 파라미터 확장을 유도해, 단일 파라미터 공간의 forgetting과 task별 branch 추가의 연산 비용 사이 트레이드오프를 해소했다. central loss로 새 카테고리를 새 task subspace의 프로토타입으로 모으면서 distance regularization으로 task 간 metric 균형을 유지해 6개 벤치마크에서 SOTA를 보고했다.
- **태그**: metric-learning, image-embedding, foundation-model

---

### [Eddy-VL 1.9B: Structural Pruning and Layered Distillation for Edge-Deployable Multimodal Embedding](https://arxiv.org/abs/2607.16316)

- **한 줄 요약**: Qwen3-VL-Embedding-2B를 CKA 기반 layer pruning과 계층적 distillation으로 압축한 1.9B 엣지 배포용 멀티모달 임베딩 모델 — teacher 성능의 91.7% 유지.
- **핵심 기여**: 인접 layer 선형 CKA로 중복 text-decoder layer 4개를 제거하고, hole-covering teacher-student 매핑 + 중간 layer attention-map CKA + 최종 layer MSE/cosine 손실의 layered KD로 pruning 손실 12.1점 중 6.4점을 회복했다(MMEB-V2 63.2 vs teacher 68.9). Matryoshka 차원 {128~2048}을 지원하며 이미지당 latency도 약 10% 줄였다.
- **태그**: image-embedding, distillation, efficient-inference, image-retrieval, vlm

---

### [DepthART: Scaling Foundation Monocular Depth to Tiny Models](https://arxiv.org/abs/2607.17099)

- **한 줄 요약**: Depth Anything류 monocular depth foundation model의 성능을 온디바이스용 tiny 모델로 가져오는 배포 특화 설계 — bias 저항 샘플링과 camera-conditioned fine-tuning의 조합.
- **핵심 기여**: tiny 모델의 병목을 (i) 데이터셋 분포 bias 과적합과 (ii) 카메라 변화 시 불안정한 metric 적응(full fine-tuning이 전이 가능한 기하를 망가뜨림)으로 진단했다. distilled encoder를 freeze하고 카메라 intrinsics 조건부로 metric scale만 조정하는 프로토콜로 cross-dataset 일반화를 보존하며, NYUDv2 zero-shot δ1=0.964, RTX A6000에서 347FPS, Orin NX 8GB에서 102FPS를 달성했다.
- **태그**: distillation, depth, efficient-inference, foundation-model

---

### [O-VAD: Industrial Video Anomaly Detection through Object-Centric Tracking and Reasoning](https://arxiv.org/abs/2607.18142)

- **한 줄 요약**: 객체별 상태 변화 궤적을 추적한 뒤 그 위에서 추론해 산업 공정 비디오의 이상을 잡는 training-free agentic 프레임워크 — 정상 클립 학습도 도메인 지식 주입도 불필요.
- **핵심 기여**: VLM 기반 anomaly reasoning이 복잡한 객체 변형·물리·절차 제약이 있는 산업 환경에서 무너지는 문제를 지적하고, 인간 검사자처럼 검출된 객체의 시공간 상태 진화를 추적한 뒤 객체별 시간 궤적 위에서 추론해 이상 객체를 frame 단위로 특정하는 구조를 제안했다. 3개 IVAD 데이터셋에서 frontier VLM, agentic 프레임워크, 해당 데이터로 fine-tune한 전통 VAD를 모두 능가하며 해석 가능한 리포트를 제공한다.
- **태그**: anomaly-detection, industrial-inspection, vlm, video

---

### [Does Super-Resolution Preserve Defect Evidence? A Low-False-Call Benchmark for Semiconductor Inspection](https://arxiv.org/abs/2607.17401)

- **한 줄 요약**: super-resolution이 반도체 검사 이미지의 결함 증거를 실제로 보존하는지를 저오탐률 운영점에서 검증한 벤치마크 — 재구성 충실도와 검사 유용성이 갈라짐을 실증.
- **핵심 기여**: 재구성과 탐지를 분리하고 사전 선언된 낮은 false-positive rate에서 평가하는 프로토콜을 설계해 10회 독립 반복 실험을 수행했다. 학습형 SR 모델 2종이 SSIM은 최고지만 결함 픽셀 탐지는 bicubic 보간보다 낮음을 전 반복에서 확인했고, clean calibration 통과가 held-out 결함 형태로의 전이를 보장하지 않으며 weak defect recall은 모든 방법에서 0에 가깝다는 점도 드러냈다.
- **태그**: industrial-inspection, defect-detection, dataset-benchmark

---

### [When 2D Cues Fail: Improving Image Manipulation Localization with Reliable 3D Geometry](https://arxiv.org/abs/2607.18040)

- **한 줄 요약**: 외형이 완벽히 blend되어 2D forensic 단서가 사라진 조작을 monocular depth·surface normal의 기하 구조 위반으로 잡는 image manipulation localization 프레임워크(GFrame).
- **핵심 기여**: 조작 이미지 위에서 monocular 재구성 기하는 본질적으로 noisy하다는 문제를 정면으로 다뤄, depth·normal을 직접 증거로 쓰지 않고 신뢰도를 추정해 선택적으로 활용하는 원칙을 세웠다. 신뢰 가능한 기하 단서를 RGB feature와 융합하고 스케일 간 전파해 fine-grained localization을 달성하며, 제한된 연산 budget에서 우수한 성능을 보고했다.
- **태그**: forgery-detection, depth, segmentation

---

### [Simple Domain Generalization for Strong Pixel-Level Image Tampering Detection in Modern VLMs](https://arxiv.org/abs/2607.18230)

- **한 줄 요약**: ChatGPT·Gemini·Qwen-Image 등 최신 VLM 편집 도구가 만드는 조작에 대한 픽셀 단위 tampering 탐지를 위한 단순하고 강력한 domain generalization 학습 레시피.
- **핵심 기여**: (1) tampered/real 이미지를 minibatch마다 전략적으로 균형 샘플링해 조작 artifact나 clean prior 한쪽으로의 편향 최적화와 학습 붕괴를 막고, (2) 대규모 base 데이터로 먼저 안정 수렴시킨 뒤 신흥 VLM 분포의 소량 데이터를 늦게 주입하는 late-injection 전략으로 과적합 없이 적응력을 높였다. cross-model·OOD 조작 분포에서 강건한 pixel-level localization을 달성했다.
- **태그**: forgery-detection, segmentation, vlm

---

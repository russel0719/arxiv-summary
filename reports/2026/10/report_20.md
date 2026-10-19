# arXiv cs.CV Daily Digest — 2026-10-19 (arXiv 공개일)

- **전체 신규 논문 수**: 126편 (new 106 + cross-list 20)
- **선별 수**: 9편

## 오늘의 트렌드

비디오 생성과 월드 모델이 가장 두꺼운 군집으로, 화면 밖 장면을 유지하는 지속 메모리와 기하·물리 일관성 보정이 함께 묶인다. VLM·MLLM 쪽은 공간 추론·환각·속성 결합을 진단하는 벤치마크와 시각 토큰 가지치기가 이어지고, feed-forward 3D Gaussian Splatting 재구성과 one-step 생성·편집 증류가 또 한 덩어리를 이룬다. 의료 영상(MRI·병리·안저)과 원격탐사 분할도 비중이 크며, 동결된 foundation model을 LoRA·프롬프트로 재활용하는 흐름이 전반에 걸쳐 있다.

---

### [A100: A Hybrid Vision Foundation Model for Agricultural Plant Image Analysis](https://arxiv.org/abs/2610.22991)

**한 줄 요약**: 100여 종 작물의 무라벨 이미지 300만 장에 DINO·iBOT·KoLeo를 결합해 사전학습한 CNN-Transformer 하이브리드 농업용 self-supervised 백본.

**핵심 기여**: 작물 모니터링·병해 진단·표현형 분석용 비전 모델은 전문가 라벨 데이터가 부족해 발전이 막힌다는 문제의식이다. A100은 로컬 특징을 뽑는 MBConv 단계와 전역 맥락을 잡는 Transformer 단계를 섞은 하이브리드 백본을, 100종 이상 작물을 담은 무라벨 이미지 300만 장에 DINO self-distillation·iBOT masked patch reconstruction·KoLeo 균일성 정규화를 함께 적용해 사전학습한다. 백본을 동결한 상태로 작물 분류 95.37%를 얻어 ImageNet-12K 지도학습 표현보다 2.56%p 높고, GroMo25 잎 개수 오차를 10.4% 줄여 같은 백본이 분류와 회귀에 모두 쓰임을 보인다. 라벨 1%(클래스당 약 284장)만으로 식물 분류 98.01%를 얻고, 동일 프로토콜에서 공개 농업 foundation model인 FoMo4Wheat·LeafVision보다 14점 이상 높다고 보고한다.

**코드**: 공개 예정

**태그**: ssl-backbone, foundation-model, image-embedding, fine-grained

---

### [Stuck on Shuffle: On Attribute-Object Binding in Vision-Language Models](https://arxiv.org/abs/2610.22602)

**한 줄 요약**: 이미지·텍스트 네 가지 모달리티 조합에서 속성-객체 결합(binding)을 평가하는 벤치마크 SABER와, 합성 텍스트만으로 MLLM 기반 임베더의 결합 능력을 높이는 파인튜닝.

**핵심 기여**: 검색용 공유 임베딩은 어떤 개념이 있는지뿐 아니라 어떤 속성이 어느 객체에 붙는지도 담아야 하는데, 기존 벤치마크는 일부 모달리티 조합·두 객체 교환·작은 속성 집합만 다룬다는 문제의식이다. SABER는 이미지↔텍스트 네 가지 조합 전부에서 다양한 속성 유형과 최대 10개 객체 장면으로 결합을 평가하며, CLIP 계열 dual encoder와 최근 MLLM 기반 임베더 모두에서 큰 결합 실패를 드러낸다. 이미지 대신 hard negative를 정밀하게 통제할 수 있는 합성 속성-결합 텍스트만으로 Qwen3-VL-Embedding(2B·8B)을 LoRA 파인튜닝하며, 본문 기준 8B 모델은 이미지 감독 없이도 ILIAS image-image mAP 58.5→68.4, Sculptures6K 50.8→59.6 등 인스턴스 검색 전반과 NegBench 부정문 평가에서 향상되고 일반 멀티모달 임베딩(MMEB-v3) 변화는 ±0.5에 그친다. 한계로 합성 이미지의 의도하지 않은 외형·배치 변화와, 쿼리 결합의 상위 집합을 인식하는 containment 문제가 남는다고 밝힌다.

**코드**: 공개 예정 (SABER·학습용 텍스트 데이터·파인튜닝 모델 공개 명시, 프로젝트 페이지 [stuck-on-shuffle.github.io](https://stuck-on-shuffle.github.io/))

**태그**: image-retrieval, image-embedding, vlm, dataset-benchmark

---

### [Micro-Localization: High-Precision Mobile Robot Localization Using Microscopic Ground Texture](https://arxiv.org/abs/2610.22563)

**한 줄 요약**: 현미경 광학으로 바닥의 자연 텍스처를 촬영하고 로컬 특징 매칭으로 수십 μm 정밀도의 전역 위치를 추정하는 이동 로봇 측위 시스템.

**핵심 기여**: 바닥 텍스처 기반 측위를 고배율 영역으로 끌어올리려는 연구로, 먼저 광학 배율·이미지 공간 측위 불확실성과 실제 물리 측위 정밀도의 관계를 정식화한다. 이를 바탕으로 고배율 촬영이 낳는 캘리브레이션·카메라 모델링·초점 문제를 다룬 현미경 측위 시스템을 만들며, 본문 기준 SIFT 디스크립터를 PCA로 16차원까지 줄여 근사 최근접 탐색 DB에 넣고 특징 스케일 검사·포즈 투표 클러스터링·RANSAC으로 평면 SE(2) 포즈를 구한다. 정밀 gantry로 여러 표면을 평가해 표면당 held-out 쿼리 1,007개를 모두 측위하고 translation RMSE 28~73 μm를 얻었으며, 독립적인 photometric 정합 결과와 약 9 μm RMSE 이내로 일치한다. 한계로 gantry 기준값 자체 오차(약 26~31 μm)가 측위 오차와 비슷한 수준이고, 얕은 피사계 심도 때문에 autofocus가 필요하며, DB가 커질 때의 검색 정확도·지연은 아직 측정하지 않았다고 밝힌다.

**코드**: 공개 예정 (본문에 데이터셋·코드 공개 명시, 링크 미기재)

**태그**: feature-matching, correspondence, visual-localization, pose

---

### [Knowledge-Guided Distributional Prompt Learning with Visual Hierarchy for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2610.23172)

**한 줄 요약**: 프롬프트 토큰을 가우시안 분포로 모델링하되 이상 프롬프트 분포를 정상 기준 분포로부터의 편차로 매개화하고, 전역·지역 계층으로 특화한 zero-shot anomaly detection 프레임워크 HiDist.

**핵심 기여**: 보조 이미지로 학습해 처음 보는 클래스의 이상을 찾는 zero-shot anomaly detection(ZSAD)에서, 기존 VLM 기반 분포형 프롬프팅은 정상 기준 분포 모델링과 계층별 프롬프트 특화를 명시적으로 결합하지 못해 이미지 단위 검출과 픽셀 단위 위치 추정을 함께 다루기 어렵다는 문제의식이다. HiDist는 각 프롬프트 토큰을 대각 가우시안으로 두고 Monte Carlo 샘플링으로 확률적 프롬프트 변형을 만들며, 이상 프롬프트 분포를 정상 분포와 따로 학습하지 않고 학습된 정상 기준으로부터의 편차로 매개화해 둘의 의존성을 명시한다. 이 분포를 이미지 단위 검출용 전역 표현과 픽셀 단위 위치 추정용 지역 표현으로 특화하고, 적응된 전역 시각 표현이 계층적 정렬을 이끈다. 산업·의료 데이터셋 7개에서 cross-dataset 이상 검출·위치 추정 성능이 높다고 보고한다 (초록에 구체 수치는 없음).

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, defect-detection, peft

---

### [COMET: Decoupled Distillation, Routing, and Capacity Control for Task-Agnostic Continual Vision--Language Learning](https://arxiv.org/abs/2610.22907)

**한 줄 요약**: 과거 데이터·태스크 ID 없이 CLIP을 순차 적응시키는 task-agnostic continual learning에서, 증류·전문가 라우팅·용량 제어를 구조적으로 분리한 mixture-of-experts 프레임워크.

**핵심 기여**: 태스크가 순차로 오고 과거 데이터가 없으며 태스크 정체를 모르고 백본도 재학습할 수 없는 설정에서, VLM은 stability-plasticity 상충을 넘어 모달 일관성 drift·표현 공간 간섭·태스크별 용량 부족이라는 세 압력 때문에 실패한다는 문제의식이다. COMET는 동결 teacher를 공유 이미지-텍스트 풀의 특징 기준으로만 쓰고, Tri-Affinity Distillation으로 image-image·text-text·image-text 기하를 보존하며, Student-Aware Cross-Expert Distillation으로 새 전문가를 호환되는 기존 전문가에 맞춰 라우팅 오류가 나도 성능이 완만하게 떨어지게 한다. 용량과 추론을 분리해 contextual bandit이 학습 후 신호로 태스크별 전문가를 유지·병합하고, 테스트 시에는 reconstruction router가 teacher 의미 정보 없이 희소 전문가를 고른다. X-TAIL 벤치마크에서 각 구성요소가 continual learning 성능을 개선함을 보인다 (초록에 구체 수치는 없음).

**코드**: 불명

**태그**: continual-learning, distillation, vlm, foundation-model

---

### [Query-adaptive Recurrent Tokenization](https://arxiv.org/abs/2610.22957)

**한 줄 요약**: 동결 인코더 특징에서 출발해 텍스트 쿼리에 필요한 만큼만 시각 토큰을 순환적으로 추가하는 backbone-agnostic 토크나이저 QART.

**핵심 기여**: 이미지에서 뽑을 정보와 필요한 토큰 수는 텍스트 쿼리에 따라 다른데, 현재 비전·VLM 모델은 쿼리와 무관하게 이미지를 인코딩하고 모든 입력에 고정 토큰 예산을 쓴다는 문제의식이다. QART는 동결 인코더 특징에서 압축 표현을 순환적으로 구성하면서 쿼리 관련 영역의 재구성 품질을 기준으로, 관련 시각 특징이 충분한 충실도로 표현될 때까지 토큰을 더 할당한다. Visual7W·VQAv2에서 약 29개 시각 토큰으로 81.96%·76.37% 정확도를 얻어 dense VLM 입력 대비 토큰 수를 20~25배 줄이고, CORE에서 P@1 92.0%, PODS에서 PR-AUC 36.3%를 기록해 PODS에서 SteerViT보다 8.4% 높다고 보고한다.

**코드**: 불명

**태그**: image-embedding, efficient-inference, image-retrieval, vlm

---

### [MaskMerge: Structure-aware Token Merging for Efficient Instance Segmentation](https://arxiv.org/abs/2610.22921)

**한 줄 요약**: 중간 단계의 거친 마스크 예측으로 특징 기반 토큰 병합을 제약해, 같은 클래스의 인접 인스턴스 토큰이 하나로 섞이는 것을 막는 instance segmentation용 ViT 토큰 병합.

**핵심 기여**: 특징 유사도로 병합할 토큰을 정하는 기존 token merging은 semantic segmentation에서는 통하지만, 같은 클래스의 인접 객체가 매우 비슷한 특징을 갖는 instance segmentation에서는 서로 다른 인스턴스 토큰이 합쳐지는 cross-instance token fusion이 생긴다는 문제의식이다. MaskMerge는 거친 중간 마스크 예측으로 특징 기반 병합을 제약해 인스턴스 경계를 보존한다. SOTA 병합 기법 ALGM 대비 PanNuke에서 mAP 30.1→32.1·GFLOPs 229→153·1.18배 속도, iSAID에서 mAP 33.1→36.2·GFLOPs 198→182·1.23배 속도를 얻고, Cityscapes에서는 더 적은 FLOPs로 ALGM과 같은 성능을 낸다. 이득은 MAE 사전학습 백본에도 전이된다고 보고한다.

**코드**: 불명

**태그**: segmentation, efficient-inference, token-merging

---

### [Replay Pruning and Few-Bit Integer Inference for Hardware-Efficient Speed-Sign Recognition](https://arxiv.org/abs/2610.22811)

**한 줄 요약**: 반복 pruning이 찾은 채널 삭제를 원본 네트워크에 재적용(replay)한 뒤 한 번의 증류로 복구하는 검출기 압축과, 정수 연산 전용 W4A8 분류기를 결합한 차량용 SoC 속도 표지 인식 시스템.

**핵심 기여**: 차량 카메라 SoC의 메모리·연산·에너지 예산 안에 검출기와 분류기를 함께 넣어야 한다는 문제의식이다. YOLO 계열 검출기는 channel replay로 압축하는데, 반복 pruning 단계로 제거할 채널을 찾고 기록된 삭제를 원래 태스크 학습 네트워크(parent)에 재적용한 뒤 연속 knowledge distillation 한 번으로 복구하며, YOLOv5n에서 parent 정확도를 유지한 채 파라미터 60.3%를 제거해 5개 시드 mAP50-95에서 반복 pruning과 scratch 학습을 앞서고 YOLOv8n에서는 unpruned parent보다도 높다. 18k 파라미터 5층 CNN 분류기와 검출 head 후처리는 정수 연산만 쓰고, W4A8에서 12.1 KB 온칩 메모리로 FP32 정확도와 같다. 공개 데이터만으로 학습한 0.72M 파라미터 전체 시스템이 held-out 차량 카메라에서 정밀도 90% 기준 표지의 95.2%를 94 FPS로 인식하며, Jetson AGX Orin에서는 TensorRT implicit 방식에서만 INT8이 FP16보다 빠르다고 보고한다.

**코드**: 불명

**태그**: quantization, efficient-inference, distillation, pruning, object-detection

---

### [Diversity Without Labels: Task-Agnostic Coreset Selection Across Perception and Action](https://arxiv.org/abs/2610.23642)

**한 줄 요약**: 비전 foundation model의 뉴런 활성을 이미지별·데이터셋별 분포로 모아 비교해, 라벨·proxy 학습 없이 태스크 무관 coreset을 고르는 방법 CoreDNA.

**핵심 기여**: 대규모 수집 데이터에서 학습용 부분집합을 고르는 기존 coreset 기법은 proxy 모델 학습·대량 주석·태스크별 설계를 요구하고, 비지도 대안은 foundation model 특징 공간에서 이미지 쌍 비교나 고정 부분집합과의 비교에 머문다는 문제의식이다. CoreDNA는 vision foundation model 여러 층의 뉴런 활성을 이미지별 분포와 데이터셋 전체 분포로 풀링하고, 둘을 비교해 저수준 시각 구조와 고수준 의미를 함께 포착한다. 고품질 샘플이 마지막 층 활성 통계의 꼬리에 몰린다는 관찰을 학습 기반 coreset 기법과의 관계로 검증하고, 이를 바탕으로 selective annotation·학습용 coreset을 계산 효율적으로 구성한다. 이미지 분류·semantic segmentation·depth 추정과 end-to-end 주행·모바일 조작 imitation learning 전반에서 state-of-the-art와 같거나 높은 성능을 보고한다.

**코드**: 불명

**태그**: foundation-model, data-selection, image-embedding

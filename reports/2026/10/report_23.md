# arXiv cs.CV Daily Digest — 2026-10-22 (arXiv 공개일)

- **전체 신규 논문 수**: 138편 (new 121 + cross-list 17)
- **선별 수**: 9편

## 오늘의 트렌드

의료 영상이 가장 두꺼운 군집으로, 병리 WSI·흉부 X선·뇌 MRI 판독문 생성과 촬영 장비별 분포 이동 감사가 이어진다. 월드 모델·로봇 조작용 표현이 두 번째 흐름이며 V-JEPA 2.1 기반 예측 표현과 행동 조건 월드 모델이 두드러진다. 비디오 diffusion의 스트리밍·자기회귀 생성과 few-step 선호 정렬, VLM의 시각 증거 활용·공간 추론 진단이 별도 덩어리를 이루고, 3D Gaussian Splatting·NeRF 장면 표현도 꾸준하다.

---

### [ALPS: Visual State Encoders for World Models](https://arxiv.org/abs/2610.30120)

**한 줄 요약**: 언어 정렬·픽셀 복원·공간 대응 목적함수로 ViT-B/16을 처음부터 사전학습한 뒤 cross-view self-distillation으로 다듬어, 하나의 patch token 집합에 물리 상태·언어·복원 정보를 함께 담는 월드 모델용 시각 인코더.

**핵심 기여**: 월드 모델은 고정된 이미지 인코더의 잠재 공간에서 계획을 세우는데, 기존 인코더는 물리 상태(물체 위치)·언어 정렬·픽셀 복원 중 한두 가지에만 강하고, 이미지-텍스트 인코더를 상태 정보 쪽으로 추가 학습하면 SigLIP 2·CLIP 기준 ImageNet zero-shot·image-to-text 검색이 4~12점 떨어진다는 문제의식이다. 1단계에서 DataComp-1B 웹 캡션과 Recap-DataComp-1B 합성 캡션으로 image-text contrastive·캡션 생성·conv 디코더 픽셀 복원·random crop/flip 뷰 간 patch 대응 InfoNCE를 함께 학습하고(외부 비전 모델 target 없음), 2단계에서 고정한 1단계 인코더를 teacher로 두고 local/global crop을 본 student가 4-layer predictor와 위치·스케일 기하 query로 teacher patch를 예측하게 한다. 15개 공개 인코더 비교에서 LIBERO state-probe 오차(1단계=1.000 기준)가 0.829로 ViT-B 중 가장 낮아 ViT-L인 V-JEPA 2-L/16과 같고(DINOv3-B 0.870, C-RADIOv3-B 0.864), ImageNet zero-shot 73.4%(SigLIP 2-B 77.6%), 자체 text tower와 결합한 LIBERO 평균 정책 성공률 85.5%(SigLIP 2 84.8%)이며, 부록 기준 DAVIS-2017 J&F는 0.533으로 DINOv3-B(0.699)보다 낮다. 한계로 ViT-B/16과 시뮬레이션 벤치마크만 다뤘고, 비디오 감독이 없어 미세한 시간적 동작에 덜 민감하다고 밝힌다.

**코드**: 공개([UCSC-VLAA/ALPS](https://github.com/UCSC-VLAA/ALPS) · Apache-2.0), 가중치는 [Hugging Face](https://huggingface.co/UCSC-VLAA/ALPS)에 공개

**태그**: ssl-backbone, image-embedding, foundation-model, world-model

---

### [Hyperspherical Simplex Representations for Backward-Compatible Retrieval](https://arxiv.org/abs/2610.29550)

**한 줄 요약**: softmax 출력·logit을 정규 simplex 위로 투영한 표현을 써서, 호환성 전용 학습·매핑 없이 독립적으로 학습된 모델 간에도 gallery 재색인 없이 검색이 되게 하는 backward-compatible retrieval.

**핵심 기여**: 배포된 검색 모델을 갱신하면 특징 표현이 바뀌어 gallery 전체를 재색인해야 하고, 기존 backward-compatibility 기법은 호환성 전용 학습·학습된 매핑·구조 변경이 필요하며 대개 이전 모델에 명시적으로 의존한다는 문제의식이다. one-hot 라벨 softmax cross-entropy 학습이 만드는 simplex 구조를 모델 갱신 간 공통 기하 기준으로 삼아, softmax 출력을 고정 centering 투영 후 ℓ2 정규화하는 PSP와 logit을 바로 정규화하는 LSP를 제안하고, 클래스가 추가되면 고정 선형 변환으로 이전 클래스 prototype과 다시 정렬하며, von Mises–Fisher 클래스 분포 가정에서 호환성 부등식이 기댓값으로 성립하는 두 기하 조건을 보인다. CIFAR-100 50단계 갱신에서 PSP·LSP의 compatibility accuracy(ACA)가 10.76·11.25%로 CoReS 3.91%, BCT 0.84%보다 높고, Google Landmarks v2 5단계에서 PSP ACA 7.21%(LCE 3.80%), 공개 사전학습 ViT-B/32→ViT-B/16→ViT-L/16 갱신에서는 모든 갱신 쌍이 호환성 기준을 만족하며 ACA 80.53%(기준선 0)다. 한계로 softmax cross-entropy가 만드는 simplex 구조와 갱신 간 일관된 라벨 공간에 의존하고, 표현 차원이 클래스 수에 비례해 늘며(top-k 희소화로 저장량 절감), 이론은 vMF 가정에 기댄다고 밝힌다.

**코드**: 공개 예정 ([miccunifi/PSP](https://github.com/miccunifi/PSP) 저장소는 있으나 README에 "code will be released soon"만 있음)

**태그**: image-retrieval, image-embedding, backward-compatible-retrieval, metric-learning

---

### [LocalAgent: Collaborative Agentic Verification for Fine-Grained Instance-Level Consistency](https://arxiv.org/abs/2610.29174)

**한 줄 요약**: MLLM이 의심 영역을 지목하면 DINO 기반 외형 일치·XFeat 기반 기하 대응 도구가 수치 증거를 돌려주는 방식으로, 두 이미지가 같은 물리적 개체인지 판정하는 instance-level 일관성 검증 에이전트.

**핵심 기여**: 시점·조명·배경이 달라도 두 이미지가 정확히 같은 물리적 물체인지 판정하려면 전역 의미와 국소 미세 증거를 함께 봐야 하는데, MLLM은 이미지-텍스트 정렬용 비전 인코더 탓에 전역 의미에 기대고 작은 국소 단서를 놓친다는 문제의식이다. Qwen3-VL-4B(LoRA)가 먼저 전체를 보고 불확실하면 의심 영역 box를 tool call로 내보내고, Local Appearance Consistency(DINO 특징, 색·흑백·flip 변형 간 patch cosine 유사도)와 Local Geometric Correspondence(XFeat keypoint·descriptor와 강건 기하 추정의 inlier 비율·매칭 수·coverage)가 구조화된 스칼라 증거를 돌려주며, 정답 보상이 도구 사용·형식 보상을 압도하도록 상한을 둔 GRPO 기반 RFT로 언제 검증할지를 학습한다. TWIN-Eval·ILIAS·Landmarks·MET·CUB·Inquire 약 12k 쿼리에서 평균 정확도 80.7%로 도구 없는 CoT-RFT 75.8%, 기반 모델 73.3%보다 높고(GPT-4o 86.1%, Gemini 2.5 Flash 82.2%는 더 높음), 도구 호출은 샘플의 12.13%이며 추론 시간은 샘플당 258 ms에서 337 ms(+30.5%)로 늘어난다. 한계로 MLLM이 제안한 영역만 검증해 국소화 품질에 좌우되고, 객관식에서 후보 간 증거를 결합하지 않으며, in-distribution인 TWIN-Eval에서는 74.5%로 기반 모델(82.9%)보다 낮다고 밝힌다.

**코드**: 공개([Firefly-zoo/LocalAgent-main](https://github.com/Firefly-zoo/LocalAgent-main)), LICENSE 파일은 아직 placeholder이고 학습된 가중치는 미공개

**태그**: feature-matching, correspondence, vlm, instance-verification

---

### [Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative Tasks](https://arxiv.org/abs/2610.28889)

**한 줄 요약**: 고정된 diffusion 모델에서 판별 태스크용 특징을 뽑을 때 timestep·block·채널 부분집합을 채널 예산 조건 정책으로 함께 고르고, 선택된 특징을 학생 모델로 증류하는 프레임워크.

**핵심 기여**: frozen diffusion 특징의 유용한 신호는 denoising 궤적·네트워크 깊이·채널에 흩어져 있는데, 기존 방법은 이 선택을 손으로 고정하거나 timestep 등 일부 하이퍼파라미터만 최적화해 입력·예산과 무관하게 같은 규칙을 쓴다는 문제의식이다. SD-1.5 U-Net을 teacher로 두고 예산 조건 정책이 timestep·block(범주형)과 채널(Gumbel top-b로 정확히 b개)을 REINFORCE로 함께 고르며, 채널 항 log-probability를 선택 채널 수로 나눠 세 head의 학습 규모를 맞추고, 학생 모델은 태스크 손실과 마스킹된 특징 증류로 학습돼 추론 시 단독으로 동작한다. 128채널 예산에서 ADE20K mIoU 38.9로 Fisher-proxy 36.4, 고정 (t,l)의 전체 1280채널 37.4보다 높고, CIFAR-100 top-1 75.4%(RepFusion 74.1%, 전체 폭 DDAE 76.8%), SPair-71k PCK@0.1 76.3이며(SPair 기준선 수치는 없음), PixArt-Σ·SD3.5 MMDiT에도 U-Net 채널 대신 이미지 토큰 hidden 차원을 써서 적용한다. 한계로 예산 변화가 선택 특징과 증류 손실 규모를 함께 바꿔 두 효과가 분리되지 않고, ablation·예산 sweep이 단일 seed라고 밝힌다.

**코드**: 불명

**태그**: correspondence, segmentation, distillation, diffusion-features

---

### [Latent space configuration for neural network finetuning, fast ranking, and embedding dimensionality reduction](https://arxiv.org/abs/2610.29295)

**한 줄 요약**: ArcFace 사전학습 IResNet50을 고정 prototype 정렬로 미세조정해 잠재 공간을 구조화하고, prototype 인덱스 기반 해시로 후보만 탐색해 top-K 임베딩 검색을 빠르게 하는 방법.

**핵심 기여**: 대규모 임베딩 gallery의 top-K 검색은 전수 탐색이 O(n)이고 근사 색인도 비용이 커서 GPU가 거의 없는 저예산·엣지 환경에 부담이 된다는 문제의식이다. Latent Space Configuration(LSC)으로 각 신원의 평균 임베딩을 +1·−1 한 쌍과 0으로 이뤄진 고정 prototype 중 하나에 cosine 손실로 맞추고(직교 초기화 FC로 차원 축소 가능), 임베딩에 가장 가까운 prototype 인덱스 쌍을 키로 하는 해시 테이블(CPU)·배치 boolean 인덱스 매칭(GPU)으로 평균 100개 남짓의 후보만 탐색한다. MS-Celeb-1M 부분집합(약 148만 장, 24.3k 신원)에서 512차원 기준 전체 질의 시간이 GPU 17.5 s→5.6 s(R1 0.944→0.942), CPU 336.4 s→12.5 s이고, 160차원으로 줄이면 GPU 12.9 s→4.3 s에 R1 0.97을 유지한다. 한계로 잠재 공간이 구조화되지 않은 모델에는 쓸 수 없고(LSC 미세조정 없이는 R1 0.266), K가 클래스 수보다 크고 클래스 수가 작으면 기대대로 동작하지 않을 수 있으며, 50 epoch에서 학습이 수렴하지 않았다고 밝힌다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, efficient-inference, face-recognition

---

### [MINER: Modeling Inter- and Intra-Person Variance for Reidentification](https://arxiv.org/abs/2610.28941)

**한 줄 요약**: 닮은 타인(hard negative)과 옷차림이 가장 다른 본인 이미지(hard positive)를 골라 대조하고, 사람 간·사람 내 분산 비율에 맞춰 배치 구성을 온라인으로 조절하는 model-agnostic 옷 변경 ReID 학습법.

**핵심 기여**: 옷 변경 person ReID(CC-ReID)는 옷이 바뀌면 외형이 크게 달라지는데, 기존 연구는 segmentation mask 같은 생체 신호 추출 휴리스틱으로 사람 간 분산을 키우는 데 집중하고 같은 사람의 옷차림 간 분산은 통제하지 않았다는 문제의식이다. MINER Sampler가 centroid 유사도 softmax로 닮은 신원을, 같은 사람의 가장 다른 옷차림 cross-camera 쌍을 각각 soft hard negative·positive로 뽑고, block-diagonal target의 multi-positive 대칭 InfoNCE로 학습하며, Variance Controller가 projection head에서 EMA로 추정한 사람 간/사람 내 gradient 분산 비율로 배치의 신원 수×이미지 수를 grid search 없이 정한다. EVA-CLIP 백본에서 R@1/mAP가 PRCC 74.5/70.0, LTCC 60.2/34.4이고 4개 백본 평균 R@1 +6.7·mAP +4.6이며, TVRID 2026 챌린지 RGB·Depth·RGB-Depth 세 트랙 모두에서 3위 안에 든 유일한 팀이다. 한계로 옷 ID 라벨과 신원당 2벌 이상의 옷차림이 필요하고, LTCC처럼 옷 다양성이 낮으면 hard positive mining 효과가 약해진다고 밝힌다(WACV 2027 채택).

**코드**: 불명

**태그**: re-identification, metric-learning, image-retrieval, clothes-changing-reid

---

### [Beyond Shortcut Learning: Hierarchical Spatial Prototype Regularization for Face Forgery Detection](https://arxiv.org/abs/2610.29442)

**한 줄 요약**: 공간 patch 특징을 학습 가능한 prototype의 가중 조합으로 재구성하고 prototype 직교성·할당 균형을 강제해, 딥페이크 검출기가 데이터셋 특유의 shortcut 단서로 붕괴하지 않게 하는 plug-in 정규화(HSP).

**핵심 기여**: 단순 미세조정한 비전 모델은 학습 데이터셋 특유의 불안정한 아티팩트에 얽힌 단서를 배워 법의학적 표현이 소수 지배 단서로 붕괴(forensic representation collapse)하고, 이 때문에 보지 못한 조작 기법에 일반화되지 않는다는 문제의식이다. CLIP ViT-L/14의 1/4·1/2 깊이 두 지점에 prototype 128개짜리 모듈을 붙여 각 patch token을 prototype의 soft 가중 조합으로 재구성하고, 재구성 손실(stop-gradient)·prototype 직교성·2차 할당 균형 손실로 위조 요인 간 기하적 독립성과 높은 effective rank를 유지하며, FaceForensics++(c23)로 학습한다. cross-dataset video-level AUC 평균 94.5%(최고 기준선 χ²-DFD 91.9%), frame-level 평균 90.8%(FSgD 85.2%), DF40 face-swap 6종 cross-manipulation frame-level 평균 93.1%(FSgD 87.8%)이고, 기존 검출기 Effort에 plug-in하면 video-level 평균 AUC가 93.5%→95.3%로 오른다. 한계로 prototype 구조가 명시적 감독이 아닌 표현 제약에서 나와 물리적으로 해석 가능한 조작 흔적과 정렬된다는 보장이 없다고 밝히며, 파라미터·연산량은 보고하지 않는다.

**코드**: 불명

**태그**: forgery-detection, deepfake-detection, foundation-model, domain-generalization

---

### [Region-Aware Multi-View Inspection Using Deep Learning and Domain-Informed Decision Fusion](https://arxiv.org/abs/2610.29398)

**한 줄 요약**: 연료 분사 니들의 seat 영역은 instance segmentation, shaft 영역은 이미지 분류로 검사하고, 표준작업절차(SOP)를 규칙으로 옮긴 결정 융합층으로 360° 회전 촬영 프레임의 검출을 부품 단위 합불 판정으로 바꾸는 외관 검사 프레임워크.

**핵심 기여**: 반사가 강한 곡면 정밀 부품의 미세 결함은 시점마다 다르게 보여 민감한 검출기가 과잉 불량 판정을 내기 쉽고, 같은 부품이라도 영역마다 허용 기준이 달라 '이상 검출'과 '허용 기준 위반'은 다르다는 문제의식이다. PLC 동기 회전 스테이션이 20° 간격 18개 위치에서 seat·shaft 카메라로 부품당 36장을 찍고, seat은 Mask R-CNN(ResNet-50-FPN V2, 결함 8종), shaft는 EfficientNetV2-S 이진 분류로 판정한 뒤, 계측 reticle로 보정한 픽셀 크기 한도와 영역(tip·하부·sealing line)별 허용 결함 종류·개수 규칙 R1~R10을 적용하고 shaft는 18장 중 3장 이상 불량이면 NOK로 둔다. 380개 부품(OK 276·NOK 104)에서 모델 출력의 단순 합집합은 NOK recall 100%에 부품 단위 false rejection rate(FRR) 57.6%였고, 전체 결정층을 넣으면 recall 100%를 유지하면서 FRR 10.9%·정확도 92.1%로 오탐 부품이 159개→30개(81.1% 감소)로 줄며, 수동 검사 대비 cycle time이 27.3% 짧다. 한계로 seat 모델 단독 instance recall이 37.19%로 낮아 후보 생성 단계로 쓰이고, 성능 유지가 안정된 광학 조건과 새 결함 형태에 대한 적응에 달려 있다고 밝히며, 외부 방법과의 비교는 없다.

**코드**: 미공개 (데이터셋·코드가 Bosch 소유로 비공개라고 명시)

**태그**: industrial-inspection, defect-detection, segmentation, decision-fusion

---

### [Open-Vocabulary Models and Label Propagation for Uncertainty-aware Pseudo-Labeling of Object Detection Datasets](https://arxiv.org/abs/2610.29788)

**한 줄 요약**: Grounding DINO 제안 영역 특징으로 객체 단위 유사도 그래프를 만들고 소수의 수동 라벨을 확률적으로 전파해, 불확실성을 담은 soft label로 객체 검출 데이터셋을 반자동 주석하는 프레임워크.

**핵심 기여**: 주석 불확실성을 반영한 soft label은 객체마다 여러 주석자(흔히 10명 이상)가 필요해 비용이 매우 크고, 그래프 기반 반지도 라벨링은 분류에서는 자리 잡았지만 불확실성 인지 검출 주석에는 검증되지 않았다는 문제의식이다. zero-shot Grounding DINO의 제안(점수 0.2 이상)을 노드로, 마지막 decoder 256차원 hidden state의 kNN Gaussian kernel을 간선으로 삼아 Probabilistic Label Spreading으로 배경을 포함한 C+1 클래스 soft label을 전파하고, isotonic 보정한 Grounding DINO 점수와 결합하는 Bayesian 변형을 두며, soft label 엔트로피(aleatoric)와 전파받은 라벨 수(epistemic)로 다음 수동 질의 대상을 고른다. COCO 1% 라벨 반지도 검출에서 Faster R-CNN AP 40.50%로 전체 수동 라벨 40.9%에 근접하고 PseCO 22.43%·Soft Teacher 20.46%보다 높으며, Grounding DINO pseudo-label만 쓴 경우는 40.14%다. 한계로 KITTI(1% 라벨 10.9 vs 전체 라벨 65.7 AP)·Cityscapes 같은 복잡한 거리 장면에서 성능이 떨어지고, 성능 상한이 주로 Grounding DINO의 검출 능력에 묶이며, 평가 프로토콜이 원본 데이터셋 쪽으로 편향돼 있다고 밝힌다.

**코드**: 불명 (본문은 [JonathanKlees/lpod](https://github.com/JonathanKlees/lpod) 공개를 명시하나 작성 시점에 해당 URL 접근 불가)

**태그**: open-vocab-detection, object-detection, pseudo-labeling, label-propagation

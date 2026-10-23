# arXiv cs.CV Daily Digest — 2026-10-23 (arXiv 공개일)

- **전체 신규 논문 수**: 114편 (new 102 + cross-list 12)
- **선별 수**: 10편

## 오늘의 트렌드

로봇 조작·주행용 월드 모델과 VLA가 가장 두꺼운 군집으로, 픽셀 예측 대신 정책 개선·물리 상태·객체 관계를 겨냥해 잠재 표현을 학습하는 흐름이 이어진다. 3D/4D Gaussian Splatting·feed-forward 재구성의 장기·스트리밍 확장과 비디오 diffusion의 few-step 생성·카메라 제어가 뒤를 잇는다. VLM이 텍스트 단서에 기대 시각 증거를 덜 쓰는 문제를 다룬 in-context learning·추론 연구와 3D·영상 제작을 LLM 에이전트로 나누는 agentic 프레임워크도 별도 덩어리다.

---

### [CODI: Improving Self-Supervised Vision Transformers with Cross Distillation](https://arxiv.org/abs/2610.30639)

**한 줄 요약**: masked patch의 teacher target에 teacher [CLS] 분포를 소량(α=0.1) 섞어, 구조 변경 없이 self-supervised ViT의 dense 표현과 image-level 표현을 함께 끌어올리는 self-distillation 기법.

**핵심 기여**: Self-supervised ViT는 image-level 표현은 강하지만 patch 표현은 dense prediction에서 불안정한데, 논문은 image-level self-distillation gradient가 [CLS]-to-patch attention 질량에 비례해 전달되어(attention 질량과 DINO gradient norm의 Spearman 상관 0.925) attention이 낮은 patch가 약한 학습 신호만 받는다는 점을 원인으로 든다. DINOv2식 구성(EMA teacher, DINO [CLS] loss, iBOT masked-patch loss, KoLeo, register 4개)은 그대로 두고 각 masked patch의 teacher target만 (1−α)·patch 분포 + α·[CLS] 분포(α=0.1, α=0이면 iBOT과 동일)로 바꿔 attention과 무관한 전역 의미 보정을 준다. ImageNet-1K만으로 사전학습한 ViT-L/14(200 epoch)에서 linear probe ADE20K mIoU 40.6, VOC 80.1, COCO 58.1로 같은 설정에서 재학습한 DINOv2(39.1·78.0·56.1)보다 높고, ImageNet k-NN·linear도 81.2·82.6(DINOv2 80.4·81.6)이며, ViT-S COCO 검출 box/mask AP 50.4/43.6(DINOv2 49.9/43.0), ViT-L DAVIS J&F 66.0(DINOv2 64.2)이다. 한계로 다중 객체 장면에서는 [CLS] target이 여러 객체 의미를 섞어 α가 크면 patch 판별력이 떨어지고, α=0.1이 보편적 최적값은 아니며, ImageNet-22K 학습은 100K iteration만 수행했다고 밝힌다.

**코드**: 공개 예정 ([EldercatSAM/CODI](https://github.com/EldercatSAM/CODI) 저장소는 있으나 README에 "Coming soon"만 있음)

**태그**: ssl-backbone, image-embedding, dense-prediction, segmentation

---

### [Learning from Next-Frame Prediction: Towards Unified and Scalable Visual Representation Learning](https://arxiv.org/abs/2610.30724)

**한 줄 요약**: 고정된 DINOv2 임베딩 공간에서 다음 프레임 전체의 표현을 예측하는 next-frame prediction으로, 이미지와 비디오를 하나의 1B ViT-g 인코더로 함께 사전학습하는 self-supervised 프레임워크 VANE.

**핵심 기여**: masked video 사전학습은 미래를 예측하기보다 주변 맥락으로 빠진 내용을 복원하고, autoregressive 사전학습은 token 단위로 예측해 joint-embedding 계열의 표현 품질에 못 미친다는 문제의식에서 미래 예측의 단위와 공간을 다시 설계한다. frame-causal ViT-g(1B)가 과거 프레임을 요약하면 12-layer state predictor가 과거 프레임을 key/value로만 쓰는 cross-attention으로 다음 프레임 전체의 frozen DINOv2 ViT-L/14 patch 임베딩을 L1 loss로 예측하고(EMA teacher 없음), flow matching 기반 보조 decoder가 미래 프레임 patch를 복원하며, 정지 이미지는 local→global 3개 crop 시퀀스로 바꿔 같은 목적함수로 학습한다(ImageNet-21K·SA-1B·SSv2·K710·HowTo100M 기반 데이터, 약 57k GPU-hour). frozen 인코더 probe 기준 EPIC-KITCHENS-100 action anticipation recall@5가 45.5로 V-JEPA 2.1(38.4)보다 7.1점 높고, IN1K/K400/SSv2 분류 87.5/88.6/75.9(V-JEPA 2 84.6/86.5/75.5), ADE20K linear mIoU 51.0(V-JEPA 2.1 47.8, DINOv2-g 49.5)이며, 같은 조건의 ViT-L ablation에서 ADE20K 45.1로 V-JEPA 2.1식 masked 목적함수(38.4)보다 높고 target을 픽셀로 바꾸면 24.1로 떨어진다. 별도 한계 절은 없으며, 표에서 ADE20K·IN1K 성능은 DINOv3 ViT-H+(54.8·88.2)보다 낮다.

**코드**: 불명

**태그**: ssl-backbone, video, foundation-model, world-model

---

### [WovenAnchor Matcher: Specialized Intra- and Inter-Image Context Modeling for Feature Matching](https://arxiv.org/abs/2610.30799)

**한 줄 요약**: 이미지 내부 문맥은 가로→세로 순서의 Mamba 스캔으로, 이미지 간 문맥은 window별 anchor끼리의 cross-attention으로 나눠 모으는 semi-dense local feature matcher.

**핵심 기여**: semi-dense 매칭의 문맥 집계에서 이미지 내부 집계는 2D 구조를 유지하며 공간 증거를 퍼뜨려야 하고 이미지 간 집계는 대응 가능성이 있는 영역에서만 정보를 가져와야 하는데, LoFTR식 attention이나 JamMa의 JointMamba는 하나의 일반 연산자로 두 역할을 함께 처리한다는 문제의식이다. JamMa 구조(경량 ConvNeXtV2식 encoder, 1/8 coarse·1/2 fine)를 바탕으로, WovenMamba는 가로 SSM 스캔 뒤 세로 스캔을 적용해(행·열 경계 separator token, 3×3 depthwise conv) 2D receptive field 편향을 주고, AnchorCrossAttention은 8×8 window(stride 4)마다 soft-cluster anchor 4개를 만들어 두 이미지의 같은 anchor끼리만 cross-attention을 수행한다. MegaDepth-1500 pose AUC@5/10/20이 66.1/78.9/87.7로 JamMa(64.1/77.4/86.5)·ELoFTR(63.7/77.0/86.4)보다 높고 파라미터 4.5M·35.4 ms(JamMa 5.7M·43.8 ms)이며, zero-shot ScanNet AUC@5는 23.2(JamMa 18.5)지만 Aachen v1.1 야간 localization에서는 LoFTR보다 낮다. 한계로 문맥 모듈 자체는 JointMamba보다 느리고(14.0 vs 2.9 ms, 전체 속도 향상은 coarse matching 최적화에서 나옴), AnchorCrossAttention이 window 수에 대해 이차 비용이라 고해상도에 제약이 있으며, nearest-neighbour 매칭의 다대일 대응과 반복 패턴 영역 실패를 든다.

**코드**: 공개([mmaiLab/WovenAnchorMatcher](https://github.com/mmaiLab/WovenAnchorMatcher) · MIT), MegaDepth 학습 가중치(outdoor)는 GitHub release에 CC BY-NC 4.0으로 공개

**태그**: feature-matching, correspondence, state-space-model, efficient-inference

---

### [MVLoMa: Multi-View Local Feature Matching with Any Geometry Foundation Model](https://arxiv.org/abs/2610.31321)

**한 줄 요약**: 기준 이미지 하나와 이웃 이미지 여러 장(star graph)을 frozen multi-view geometry 모델 특징으로 한꺼번에 기술하고, 한 번의 forward로 기준-이웃 전체를 매칭하는 LoMa의 multi-view 확장.

**핵심 기여**: SfM·visual localization에서는 기준 이미지 하나를 검색된 이웃 여러 장과 매칭하는데, pairwise matcher를 쌍마다 돌리면 기준 이미지 쪽 계산이 반복되고 다른 시점이 줄 수 있는 기하 증거를 쓰지 못한다는 문제의식이다. LoMa의 frozen DINOv2-L descriptor 경로를 frozen 3D foundation 인코더(기본 DA3-Giant, π³·VGGT·VGGT-Ω도 시험) 토큰으로 바꿔 VGG 특징과 합친 뒤 이미지당 DaD keypoint 4096개에서 descriptor를 뽑고, 9개 층에서 view별 self-attention과 기준-이웃 양방향 cross-attention(이웃끼리는 attention 없음)을 수행하며, depth가 유효하고 서로 보이는 dense warp에서만 positive를 만들고 epipolar 오차 3 px를 넘는 고신뢰 매칭에 벌점을 준다. HyperSim·ScanNet++·Mip-NeRF 360·Tanks and Temples의 25-view star에서 macro relative-pose AUC@1/5/10이 58.65/85.41/90.99로 LoMa-L(57.40/84.44/90.06)·RoMa v2(56.95/84.87/90.97)보다 높고, 24개 쌍 순차 매칭보다 2.20배 빠르지만(203 vs 447 ms) 최대 메모리는 979 vs 176 MiB로 늘어난다. 한계로 frozen foundation 특징 품질에 의존하고, 이웃끼리 직접 정보를 교환하지 않으며, view·keypoint 수에 따라 메모리가 늘고, relative pose만 평가해 전체 SfM은 다루지 않았다고 밝힌다.

**코드**: 공개 예정 (논문에 출판 시 구현·평가 설정 공개 명시, 프로젝트 페이지 [kosmoresearch.github.io/MVLoMa](https://kosmoresearch.github.io/MVLoMa/))

**태그**: feature-matching, correspondence, multi-view-matching, 3d

---

### [LACToS: Local Anomaly Detection via Conditional Typicality of Superpixels](https://arxiv.org/abs/2610.31538)

**한 줄 요약**: 정상 데이터로 학습한 diffusion 모델의 posterior 재구성 분포 아래에서 superpixel 픽셀들의 통계적 전형성(typicality)을 재서, 정상 분포가 다양한 영역에서도 국소 이상 영역을 찾는 local anomaly detection.

**핵심 기여**: PatchCore·EfficientAD·GLASS·DDAD 같은 픽셀 단위 이상 탐지는 산업 벤치마크에서는 강하지만 CT·얼굴·X선 수하물처럼 정상 이미지 분포가 다봉(multimodal)일 때 성능이 크게 떨어진다는 문제의식이다. superpixel 안의 픽셀이 나머지 이미지에 조건부로 i.i.d.라고 보고 |평균 negative log-likelihood − entropy|를 전형성 점수로 쓰며, 이를 정상 이미지로만 학습한 diffusion 모델의 posterior 샘플(DPS) M개에서 superpixel별 히스토그램으로 근사하고(근사 오차 상한으로 최적 노이즈 수준 σ를 유도), 픽셀 특징은 RGB에 frozen ImageNet ResNet-101 특징을 autoencoder로 3차원 압축한 값을 붙이고 superpixel은 marker-controlled watershed로 만든다. pixel AUROC/AP/AUPRO가 CHAOS CT(합성 간 종양) 0.962/0.432/0.876(DDAD 0.971/0.316/0.868, PatchCore 0.930/0.059/0.681), FFHQ 얼굴 0.852/0.118/0.532로 세 지표 모두 최고, DVXray 수하물 0.961/0.057/0.818(PatchCore 0.964/0.055/0.814)이고, 부록의 MVTec AD 15개 범주 평균은 0.973/0.608/0.872로 EfficientAD(0.986/0.636/0.943)보다 낮다. 한계로 정형화된 산업 데이터에서는 전용 기법이 앞설 수 있고, diffusion 샘플링 때문에 이미지당 비용이 feedforward 방식보다 크며, 큰 superpixel에서는 i.i.d. 가정이 깨질 수 있고, 하이퍼파라미터가 많아 테스트 이미지 20장으로 grid search했다고 밝힌다.

**코드**: 공개([voilalab/LACToS](https://github.com/voilalab/LACToS)), diffusion 체크포인트·테스트 데이터는 README의 Google Drive 링크로 제공

**태그**: anomaly-detection, ood-detection, industrial-inspection, superpixel

---

### [WildFakeToolBench: Benchmarking AI-Generated Image Detectors with Web-Sourced Image Processing](https://arxiv.org/abs/2610.31152)

**한 줄 요약**: 웹에 공개된 이미지 처리 요령 220건을 LLM으로 실행 가능한 CPU 도구 156개로 바꿔, AI 생성 이미지 탐지기가 비전문가 수준의 후처리로 얼마나 우회되는지 재는 벤치마크.

**핵심 기여**: 포럼·저장소·사진 튜토리얼에 퍼진 정보를 LLM 코드 변환으로 옮기면 전문 지식이나 GPU 없이도 탐지기 우회 도구를 만들 수 있다는 위험을 평가하려는 문제의식이며, 새로운 공격 알고리즘이 아닌 강건성 평가 자원으로 제시된다. GPT-4o-mini와 Tavily 검색으로 142개 도메인 220개 출처에서 방법을 추출·중복 제거해 코드로 만들고 문법·실행·출력 변화·SSIM 검사를 통과한 도구 156개(10개 범주)를 남겼으며(평가 대상 탐지기의 피드백은 쓰지 않음), 5개 생성기(SD 2.1·Qwen-Image-2.0·Midjourney·GPT Image 2·Nano Banana 2) 이미지 105장 중 6개 탐지기(FakeVLM·SIDA-13B·FakeShield·GPT-5.6-luna·CommForensics·AIDE)가 가짜로 판정한 이미지를 처리해 SSIM 0.75 이상을 유지하면서 real로 뒤집힌 비율을 공격 성공률(ASR)로 잰다. 탐지기별 최강 단일 도구의 ASR은 25.25%(SIDA-13B)~100%(AIDE)로 노이즈·스펙트럼 억제·카메라 처리 시뮬레이션 등 6개 기준 처리의 최고치(SIDA-13B 12.12%, AIDE 55.29% 등)를 모두 넘고, 도구별 평균 ASR은 3.22~23.10%이며, 8개 도구 풀의 최선 부분집합 coverage는 모든 탐지기에서 80%를 넘는다. 한계로 이미지 수가 적고 탐지기마다 평가 이미지 수가 달라 비교가 제한되며, coverage는 one-shot 성공과 다르고, 도구 풀을 평가 ASR로 골랐으며, print-and-scan은 소프트웨어로만 시뮬레이션했다고 밝힌다.

**코드**: 불명 (초록에 [TrustAIRLab/WildFakeToolBench](https://github.com/TrustAIRLab/WildFakeToolBench) 저장소가 명시돼 있으나 확인 시점에 페이지가 열리지 않음)

**태그**: forgery-detection, dataset-benchmark, adversarial-robustness

---

### [Residual Calibration via Local Feature-Space Refinement](https://arxiv.org/abs/2610.30652)

**한 줄 요약**: 기존 전역 calibrator 출력을 anchor로 두고, feature 공간에서 가까운 calibration 샘플들의 라벨 빈도로 개별 예측을 잔차 보정하는 post-hoc calibration 모듈 LAPE.

**핵심 기여**: temperature scaling·vector scaling·Dirichlet 같은 전역 score 변환은 score가 비슷한 샘플에 같은 보정을 적용해 feature 공간 영역마다 다른 miscalibration을 놓치고, local TS는 과적합되며 순수 비모수 방법은 데이터 효율이 낮다는 문제의식이다(NeurIPS 2026 채택). 학습된 feature 공간에서 L2 거리로 이웃 calibration 샘플 m개를 찾아 Laplace 평활 라벨 빈도를 구하고 전역 calibrator 출력과 (1−α):α로 섞되 (m, α)는 테스트 샘플마다 Gaussian kernel 가중 leave-one-out NLL로 고르며, calibration 셋의 anchor는 5-fold cross-fitting으로 만들어 전역 calibrator에 쓴 데이터를 그대로 재사용하고, 확장인 CFAF는 이미지+메타데이터처럼 view마다 분류기가 있는 입력에서 view별 보정 출력을 NLL 기준 simplex 가중치로 합쳐 anchor로 삼는다. 결과는 대부분 상대 변화로 보고되며, CIFAR-100(frozen ResNet50 linear probe)에서 보정 전 모델을 anchor로 한 LAPE가 NLL −19.08%·ECE −27.28%, FC anchor 위에서 ECE −23.63%지만 TS anchor 위에서는 NLL −0.03%·ECE +0.60%로 변화가 거의 없고, HAM10000 다중 view 설정에서 CFAF-LAPE의 NLL/ECE/Acc는 0.224/0.014/0.907(late fusion 0.255/0.023/0.896)이다. 한계로 feature 기하 품질에 의존해 이웃의 라벨 분포가 다르면 국소 추정이 편향되고 고차원·구조적 노이즈에서 이득이 줄어든다고 밝히며, CIFAR-10-C에서는 여러 anchor에서 ECE가 오히려 악화됐다.

**코드**: 공개([AltonWongsource/residual-calibration](https://github.com/AltonWongsource/residual-calibration))

**태그**: calibration, post-hoc-calibration, knn

---

### [LoRA Superposition across Pretrained Models](https://arxiv.org/abs/2610.30691)

**한 줄 요약**: 같은 과제에 대해 서로 다른 CLIP ViT-B/16 백본 7개에서 따로 학습한 LoRA를 그대로 더한 adapter 하나를 모든 백본에 적용해도 개별 LoRA와 거의 같은 정확도가 나온다는 관찰과 그 분석.

**핵심 기여**: LoRA는 학습된 백본에 묶여 있어 백본 M개·과제 T개면 adapter M×T개가 필요한데, 같은 구조의 서로 다른 사전학습 백본에서 독립 학습한 LoRA를 합쳐 모든 백본에 공통으로 쓸 수 있는지를 묻는다. OpenCLIP ViT-B/16 7종(OpenAI·LAION-400M·LAION-2B·DataComp-1B·DFN-2B·MetaCLIP-400M·MetaCLIP-2.5B)에 Q·V projection rank 16 LoRA를 8개 분류 과제(Cars·DTD·EuroSAT·GTSRB·MNIST·RESISC45·SUN397·SVHN)마다 학습한 뒤, 각 LoRA의 ΔW=BA를 그대로 더한 exact sum(rank ≤112, 추가 데이터·최적화 없음)과 대상 백본 자신의 LoRA를 뺀 leave-one-model-out(LOMO) sum을 비교한다. exact sum의 평균 정확도는 90.06%로 개별(solo) LoRA 90.34%보다 0.28점 낮고 미적응 백본 59.85%보다 30.21점 높으며 56개 백본-과제 쌍 모두에서 향상되지만 LOMO sum은 59.91%로 사실상 효과가 없고, 다른 백본 LoRA 간 평균 절대 cosine 유사도는 1.34×10⁻³(같은 백본·다른 seed 0.424), 다른 백본의 LoRA를 적용했을 때 정확도 변화는 −0.2~+0.3점에 그친다. 이를 근거로 frozen 백본이 명시적 routing 없이 자기 성분에만 반응한다는 성분별 비간섭 가설을 제시하며, 한계로 near-orthogonality만으로는 현상이 설명되지 않고, ViT-B/16 단일 구조만 시험했으며, 합산 rank가 백본 수에 비례해 커지고 더 많은 백본으로의 확장성은 확인되지 않았다고 밝힌다.

**코드**: 불명

**태그**: peft, model-merging, foundation-model

---

### [WeVisOne-VL: Unified Visual Perception from Objects to Pixels](https://arxiv.org/abs/2610.31329)

**한 줄 요약**: Qwen3-VL(2B·4B)에 `<OBJ>` token과 약 9.6M 파라미터 pixel decoder를 붙여 detection·referring·counting·OCR·segmentation·matting을 하나의 next-token 예측으로 처리하는 통합 perception VLM.

**핵심 기여**: VLM은 없는 객체를 만들어내고 낯선 묘사를 잘못 읽으며 덜 두드러진 인스턴스를 놓치는 등 세밀한 시각 인지에서 신뢰하기 어렵다는 문제의식이다. 박스·점을 `<0>`~`<1000>` 좌표 token으로 출력하고 대상이 없으면 "None"을 내며, 각 박스 뒤 `<OBJ>` token의 hidden state와 Fourier 인코딩 박스를 deformable query decoder·dynamic mask head에 넣어 인스턴스 mask와 alpha matte를 만들고, 1억 장 이상·약 36억 박스 데이터로 3단계 curriculum SFT(과제 정렬 → 고해상도·밀집 → token-to-pixel) 후 IoU 기반 grounding 보상과 부재 대상 거절 보상을 둔 GRPO로 학습한다. 4B 모델의 COCO/LVIS 검출 mean F1(IoU 0.5–0.95 평균)이 57.1/55.3으로 Qwen3-VL-4B(48.7/44.0)·GroundingDINO-T(56.6/38.8)보다 높고, RefCOCOg referring detection val 80.8(Qwen3-VL-8B 74.6), RefCOCO val referring segmentation cIoU 81.4(UniPixel-7B 80.8), Ref-ZOM 거절률 86.0(UniPixel-7B 0.3), AM-2K matting MAD 5.0×10⁻³(SAM2-Matting 최고 설정 11.0×10⁻³)이다. 한계로 일반 목적 학습 데이터가 적어 base 모델보다 일반 능력이 약해질 수 있고, chain-of-thought 없이 바로 출력해 복잡한 추론에 제약이 있으며, 단일 턴 예측만 지원한다고 밝히고, 구성 요소별 ablation과 일반 벤치마크 비교는 보고하지 않는다.

**코드**: 공개([Tencent/WeVisOne-VL](https://github.com/Tencent/WeVisOne-VL) · Apache-2.0, 추론·데모·평가 코드만 있고 미세조정 코드는 미공개), 2B·4B 가중치는 [Hugging Face](https://huggingface.co/tencent/WeVisOne-VL-4B)에 공개

**태그**: vlm, open-vocab-detection, segmentation, image-matting

---

### [ReCoG: Relational Concept Graph for Training-Free Personalization](https://arxiv.org/abs/2610.31282)

**한 줄 요약**: 개인화 개념을 노드로, 개념 쌍 간 구별 단서를 frozen VLM이 미리 생성한 방향 간선으로 두고, 추론 시 후보 쌍별 비교의 round-robin으로 헷갈리는 fine-grained 개념을 판별하는 training-free 개인화 기법.

**핵심 기여**: training-free 개인화는 frozen VLM이 몇 장의 예시만으로 사용자 정의 개념을 인식하도록 추론 시 개념 항목을 검색하는데, RAP·R2P 같은 기존 retriever 기반 방법은 개념마다 독립적으로 설명을 붙여 그럴듯하지만 비슷한 개념끼리는 구별하지 못하는 증거를 가져온다는 문제의식이다. 데이터베이스 구축 시 frozen VLM(기본 MiniCPM-o-2.6)이 두 개념의 support 이미지를 함께 보고 서로를 구별하는 특징을 JSON으로 내놓아 방향 간선 두 개를 만들고, 추론 시에는 CLIP ViT-L 유사도로 후보를 추린 뒤 모든 후보 쌍에 대해 쿼리·두 support 이미지·간선을 주고 어느 쪽에 가까운지 판정하게 해 가장 많이 이긴 개념을 고르며, 개념이 많을 때는 CLIP top-k 이웃 사이에만 간선을 두는 sparse 변형을 쓴다. 헷갈리는 개념 집합으로 새로 만든 FINGER(CUB-Easy·CUB-Hard·CLEVR, 각 20개 개념, 총 1,000장)에서 양성·음성 평균 정확도가 98.1/92.8/93.3으로 R2P(93.6/81.0/79.6)보다 높고, CUB-Hard 양성 정확도는 86.3(R2P 63.8)이며, MyVLM·PerVA에서도 99.3·98.8(R2P 97.4·91.8), CUB 200종에서는 sparse 변형이 양성 정확도 56.2(R2P 48.6)를 쿼리당 평균 VLM 호출 2.46회(R2P 3회)로 얻는다. 한계로 개념 수가 크게 늘거나 데이터베이스가 온라인으로 갱신될 때의 확장성을 든다.

**코드**: 공개 예정 (논문에 채택 시 코드·데이터 공개 명시), FINGER 벤치마크는 [Hugging Face](https://huggingface.co/datasets/ssun0626/FINGER)에 공개

**태그**: vlm, fine-grained, training-free, personalization

# arXiv cs.CV Daily Digest — 2026-10-26 (arXiv 공개일)

- **전체 신규 논문 수**: 133편 (new 107 + cross-list 26)
- **선별 수**: 8편

## 오늘의 트렌드

의료 영상(병리 WSI·내시경·분할 loss·의료 VLM)이 가장 두꺼운 군집이고, 스트리밍 비디오 이해·시각 grounding·안전성을 다루는 VLM 연구가 뒤를 잇는다. T2I 생성·편집의 정렬·평가·보상 모델과 단일 이미지에서 3D 장면·아바타를 만드는 생성 연구가 또 다른 덩어리이며, action 조건 world model·VLA 정책 학습과 위성 임베딩을 증류·멀티모달 결합으로 재사용하는 geospatial foundation model 연구도 여러 편 묶인다.

---

### [FlexGlue: Sparse-to-Dense Feature Matching and Visual Disambiguation](https://arxiv.org/abs/2610.32976)

**한 줄 요약**: 첫 이미지의 query 점 좌표를 주면 두 번째 이미지의 dense grid에서 대응점을 sub-pixel로 찾고, 동시에 겉보기만 닮은 비공시(non-covisible) 이미지쌍을 거부하는 asymmetric sparse-to-dense matcher.

**핵심 기여**: sparse keypoint 매칭은 빠르지만 keypoint 재현성(repeatability)에 묶이고 dense 매칭은 강건하지만 비싸며, 두 방식 모두 매칭되는 쌍만으로 학습돼 대칭 구조가 닮은 서로 다른 장소(doppelganger) 쌍을 걸러내지 못해 SfM을 망가뜨린다는 문제의식이다. frozen DINOv3 ConvNeXt-B 특징을 stride-8 token grid로 합쳐 9-layer self/cross-attention Transformer로 문맥을 모은 뒤, query마다 cosine 유사도 위의 1.5-entmax windowed soft-argmax로 위치를 읽고 소형 MLP로 sub-cell 보정하며, 층마다 covisibility head를 감독해 추론 시 확실한 비공시 쌍은 조기 종료한다(8개 데이터셋 학습 후 Doppelgangers·좌우반전 hard negative로 미세조정, H200 약 4 GPU-day). dense 모드는 ScanNet-1500 AUC@5/10/20 33.6/56.4/73.8로 RoMa v2(33.6/56.2/73.8)와 같은 수준에 11.8 ms(RoMa v2 42.4 ms)이고, ETH3D SfM에서 disambiguation 포함 시 pose AUC@1/3/5° 68.9/86.8/92.3(RoMa v2+DG++ 62.0/80.6/85.1, 처리량 30 vs 4 pairs/s), 새로 만든 실내·교차기기 doppelganger 벤치마크 LaMAR-DG에서 AUROC 88.8(DG++ 78.6)이다. 한계로 MegaDepth-1500에서는 dense refiner를 쓰는 RoMa v2보다 낮고(AUC@5 58.1 vs 62.8), grid 셀 간 보간 때문에 query 간 오차가 주로 epipolar line 방향으로 상관되며, depth 불연속 부근에서 PCK@5px가 90% 이상에서 약 75%로 떨어진다고 밝힌다.

**코드**: 공개([cvg/flexglue](https://github.com/cvg/flexglue) · MIT), 가중치 `flexglue.pth`도 공개(matcher·descriptor head는 MIT, 포함된 DINOv3 ConvNeXt-B backbone은 DINOv3 License)

**태그**: feature-matching, correspondence, visual-disambiguation, structure-from-motion

---

### [SemGeo-Gen: Unsupervised Generation of Approximate Cross-Instance Semantic-Geometric Correspondences](https://arxiv.org/abs/2610.32663)

**한 줄 요약**: 대략 정렬된 3D 물체 모음에서 DINOv2 특징과 CPA 변형 정합으로 서로 다른 인스턴스 간 근사 대응을 사람 라벨 없이 만들어, 2D semantic correspondence 모델의 합성 사전학습 데이터로 쓰는 방법.

**핵심 기여**: 서로 다른 인스턴스 사이의 정확한 점 대응은 정의 자체가 모호하고 수작업 라벨은 비싸고 희소해, 대응 학습에 쓸 감독 신호를 규모 있게 얻기 어렵다는 문제의식이다. 카테고리 단위 회전 정렬만 된 3D 모델(KeypointNet, Objaverse-OA 100여 rigid 카테고리)을 여러 시점에서 렌더링해 DINOv2 dense 특징을 3D 점으로 올리고(시점 평균 후 PCA 64차원), 6×6×6 grid의 continuous piecewise-affine(CPA) 변형을 Chamfer 거리+smoothness로 최적화해 nearest-neighbour 대응을 얻은 뒤 특징 cosine 유사도 0.575 미만은 버리고, 남은 3D 대응을 렌더 이미지에 투영해 3D-3D·3D-2D·2D-2D 감독을 만든다(쌍당 1.13 s, RTX A6000). KeypointNet 사람 라벨 대비 PCK@0.10/0.15가 0.93/0.97이고, 이 합성 쌍(카테고리당 12K)으로 사전학습한 뒤 SPair-71k에 미세조정하면 rigid 9개 카테고리 PCK@0.10이 GeoAware-SC 79.36→83.73, MARCO 86.34→89.30, 18개 전체 카테고리 GeoAware-SC는 82.09→84.48(DenseMatcher 사전학습 81.83)로 오른다. 한계로 감독 없는 CPA 변형이 인스턴스 간 큰 구조 차이를 다 담지 못하고, 필터링이 DINOv2에 의존하며, rigid·대략 정렬된 물체만 다루고 합성-실제 도메인 갭이 남는다고 밝힌다.

**코드**: 공개 예정 ([프로젝트 페이지](https://bgu-cs-vil.github.io/SemGeo-Gen/)에 Code·Data "soon" 표기)

**태그**: correspondence, semantic-correspondence, sim2real, synthetic-data

---

### [Flownomaly: Single-Step Conditional-Mean Recovery for Few-Shot Anomaly Detection](https://arxiv.org/abs/2610.32964)

**한 줄 요약**: frozen DINOv2 patch token 공간에서 conditional flow matching으로 정상 분포를 학습하고, 한 번의 velocity 평가로 query token의 정상 대응물을 복원해 그 잔차로 결함을 찾는 few-shot industrial anomaly detection 기법.

**핵심 기여**: 정상 이미지 몇 장만으로 카테고리별 정상성을 모델링해야 하는 few-shot 설정에서, 기존 방법은 저장된 exemplar에 추론이 묶이거나 선형 subspace 같은 경직된 구조를 가정하거나 reconstruction이 이상 부분까지 복원해 버린다는 문제의식이다. frozen DINOv2 ViT-g/14-reg(672×672, 16·20·24·28·32번 블록 평균, 48×48 token)의 정상 support token만으로 카테고리별 residual MLP velocity field(23.2M)를 직선 경로 conditional flow matching으로 학습하고, query에 시점 t의 노이즈를 섞은 뒤 한 스텝 x̂ = z + (1−t)·v(z,t)로 깨끗한 정상 token의 사후 평균을 구해 제곱 잔차를 pixel·image 점수로 쓰며, 이상 샘플 없이 t를 고르도록 정상 support만으로 계산하는 Jacobian gain-to-noise(JGN) 기준을 제안한다. 1-shot image/pixel AUROC가 MVTec-AD 97.8/98.0(ANoCo 97.9/97.7), VisA 95.3/98.7(SubspaceAD 93.2/98.2, ANoCo 92.7/98.7)이고 Real-IAD 1-sample image AUROC는 88.2(SubspaceAD 85.2)이며, 카테고리당 학습 중앙값 24~28 s, 이미지당 추론 60.9 ms(H100, 그중 velocity 네트워크 2.2 ms)다. 한계로 token 단위 점수라 부품 개수 오류 같은 logical anomaly(MVTec cable 전선 뒤바뀜, VisA pcb3 부품 누락)는 놓치고, JGN이 고른 t는 최적 t 대비 VisA에서 최대 4.82 pp 손해가 난다고 밝힌다.

**코드**: 공개([b-rbmp/Flownomaly](https://github.com/b-rbmp/Flownomaly) · Apache-2.0), 학습 가중치는 미공개

**태그**: anomaly-detection, industrial-inspection, defect-detection, few-shot, flow-matching

---

### [Spectra: Multi-Scale Implicit Decomposition for Deepfake Detection](https://arxiv.org/abs/2610.31979)

**한 줄 요약**: hypernetwork로 이미지마다 SIREN INR을 예측하고, 그 은닉층 활성에서 뽑은 다층 reconstruction heatmap을 CLIP 의미 특징과 양방향으로 융합하는 딥페이크 판별기.

**핵심 기여**: RGB 외형·주파수 artifact 기반 판별기는 특정 생성기에 묶인 단서를 배워 새 조작 기법·압축·데이터셋 변화에 일반화가 약하다는 문제의식에서, 이미지가 어떻게 보이는지가 아니라 implicit neural representation(INR)으로 어떻게 복원되는지를 단서로 쓴다. 이미지별 최적화 비용을 피하려고 hypernetwork가 SIREN 파라미터를 바로 예측하고, 첫 3개 은닉층 활성을 PCA로 이미지 공간에 투영한 heatmap과 층 간 차이 맵(5채널)을 spatial·frequency(log FFT) encoder로 처리한 뒤, frozen CLIP ViT-L/14(11·17·23층) 의미 token과 양방향 cross-attention·gating으로 융합하며 FF++ c23로 학습한다(CE+mixup+SupCon). cross-dataset frame AUC가 Celeb-DF v1/v2 0.829/0.841, FaceShifter 0.858로 각 열의 최고 baseline(MUF 0.807, TGFD 0.794, WaveletCLIP 0.732)보다 높고 DFD는 0.896으로 TGFD(0.905)보다 낮으며, face presentation attack detection leave-one-out 평균 AUC는 97.17%(CA-FAS 95.04%)다. 본문 표에는 압축·perturbation 강건성 실험과 추론 비용이 없고, hypernetwork 구조·학습 방식과 ablation은 supplementary로 미뤘으며, 별도 한계 서술은 없다.

**코드**: 불명

**태그**: forgery-detection, deepfake, implicit-neural-representation, face-anti-spoofing

---

### [Learning Fine-Grained Visual Classification with Text as Privileged Information via Multimodal Distillation](https://arxiv.org/abs/2610.32442)

**한 줄 요약**: 학습 때만 속성 텍스트 설명을 gated cross-attention으로 넣은 multimodal teacher를 만들고, prediction·patch·attention 세 수준 증류로 이미지 전용 ViT student에 옮기는 fine-grained 분류 기법 FG-LUPI.

**핵심 기여**: 속성 텍스트는 fine-grained 구분에 유용한 의미 감독을 주지만 기존 multimodal 방법은 추론 때도 텍스트를 요구한다는 문제의식에서, 텍스트를 학습 전용 privileged information(LUPI)으로 쓴다. teacher는 ViT-B/16 이미지 token이 frozen BERT 텍스트 token을 gated cross-attention으로 참조하는 구조(216.5M)이고, student는 같은 ViT-B/16(86.7M)으로 EMA teacher의 softened 예측(KL)·최종층 patch 임베딩(1−cosine)·patch-to-patch attention 분포(KL)를 함께 맞추며, 텍스트는 CUB만 사람 작성 설명이고 나머지 데이터셋은 Gemma가 학습 이미지에서 생성했다. 이미지 전용 추론에서 top-1이 CUB 92.8·Dogs 95.1·NABirds 92.3·Aircraft 94.0·Cars 89.2·iNat21 76.46으로 ViT baseline(90.3·91.6·89.6·90.3·83.6·74.08)과 같은 네트워크의 증류 기법 최고치인 DKD보다 모두 높고, ECE는 CUB 5.44→1.92%, iNat21 22.32→11.29% 등 6개 벤치마크 모두에서 낮아지며, CUB ablation에서 세 손실을 모두 쓸 때(92.8)가 두 개 조합(최대 92.3)보다 높다. Cars에서는 A2Q-Trans(90.8)보다 낮고, 한계로 설명문의 구체성·정확도에 성능이 좌우되며(Cars가 어려운 사례) teacher 때문에 학습 비용이 약 1.9배 늘어난다고 밝힌다.

**코드**: 불명

**태그**: fine-grained, distillation, calibration, privileged-information

---

### [Rethinking Representation Geometry in Supervised Contrastive Learning under Long-Tailed Data](https://arxiv.org/abs/2610.32039)

**한 줄 요약**: long-tailed 데이터에서 SupCon·BCL의 최적 표현이 regular simplex를 이루지 못함을 증명하고, 클래스 단위로 손실을 균형화해 regular simplex 최적성을 보장하는 Fully Balanced Contrastive Learning(FBCL).

**핵심 기여**: supervised contrastive learning과 균형 변형들의 최적 표현이 regular simplex(클래스 중심이 등간격·최대 분리)라는 기존 분석이 long-tailed 데이터에서도 성립하는지 불분명하다는 문제의식에서, 클래스 중심 기반 하한으로 SCL·BCL을 분석해 anchor별 손실을 합칠 때 클래스가 배치 내 샘플 수 비율(B_y/B)로 가중되므로 regular simplex가 전역 최소가 아님을 보인다. 이를 고치는 structural balancing(클래스 안에서 1/B_y로 평균한 뒤 클래스마다 1/K 동일 가중)을 BCL에 적용한 FBCL은 표현이 regular simplex일 때에만 최솟값에 도달함을 증명한다(배치에 모든 클래스 포함, K≤h+1, τ=1 등 가정). ResNet-50 기준 ImageNet-LT/iNaturalist 2018 top-1이 BCL 56.0/71.3 → FBCL 56.6/72.2, ProCo 57.1/72.3 → ProCo+SB 57.4/72.7이고, ImageNet-LT 사전학습 후 11개 데이터셋 transfer 평균은 linear 69.1(BCL 68.7)·fine-tuning 84.5(GPaCo 84.3)이며, ImageNet-LT 클래스 중심 간 평균 cosine 유사도는 0.124→0.103으로 낮아진다. 한계로 이론이 모든 클래스가 배치에 들어 있다는 가정과 K≤h+1 조건(iNaturalist에서는 불성립)에 기대고, 대규모 학습에서 실제로 최적점에 도달하는지는 다루지 않으며, SOTA 달성이 목표가 아니라고 밝힌다.

**코드**: 불명

**태그**: metric-learning, contrastive-learning, long-tailed, image-embedding

---

### [Complementing DINO Features with Image Structure for Part Discovery](https://arxiv.org/abs/2610.32293)

**한 줄 요약**: low-level edge 기반 영역 분할로 DINOv2 patch 특징을 영역 단위로 pooling해, 학습 없이 객체를 의미 있는 part로 나누는 training-free part discovery 기법 Part-DINO.

**핵심 기여**: DINO 특징 clustering 기반 part discovery는 ViT patch grid가 part 경계를 가로질러 여러 part의 픽셀을 섞기 때문에 경계가 부정확하다는 문제의식으로, PartImageNet 전경 patch 26,459개 분석에서 21.9%가 여러 part를 포함하고 경계에 가까울수록 특징 entropy는 높고 할당 확신(top-2 margin)은 낮음을 보인다(경계 거리와 Spearman −0.38·+0.36). DINO를 재학습하는 대신 frozen DINOv2 ViT-B/14(register)의 patch 특징을 픽셀 단위로 upsample한 뒤 RAMP edge 변환+watershed로 만든 영역(이미지당 약 560개)마다 평균 pooling하고, SAM3로 얻은 전경 안에서 카테고리별 K-Means prototype에 영역을 할당한다. CUB(K=16) keypoint NME/NMI/ARI가 4.35/65.45/46.00으로 training-free baseline(Amir et al.+SAM 전경, 4.87/56.92/35.10)보다 좋고 NME는 비지도 학습 기법 MPAE(5.14)보다도 낮지만 NMI/ARI는 MPAE(79.00/66.56)가 앞서며, PartImageNet-Seg(K=8) NMI/ARI 37.21/66.10은 MPAE(33.51/65.05)보다 높고, 처리 시간은 이미지당 680 ms(A40, 대부분 SAM3)다. 한계로 part 수 K를 미리 정해야 하고, edge가 국소 대비에 의존해 저대비 장면은 과소 분할되고 강한 조명·그림자는 가짜 경계를 만든다고 밝힌다.

**코드**: 불명

**태그**: ssl-backbone, segmentation, training-free, part-discovery

---

### [Consommé: Conditioned Token Merging for Split Inference](https://arxiv.org/abs/2610.32794)

**한 줄 요약**: split inference에서 frozen ViT는 그대로 두고, CLS token을 압축한 latent로 patch를 정확히 k개 token으로 soft merge해 전송량을 줄이는 소형 adapter.

**핵심 기여**: ViT를 edge 기기와 서버로 나눠 돌리는 split inference는 중간 token 전송 비용이 크고 endpoint마다 미세조정 backbone을 배포하기도 비싸며, ToMe식 bipartite matching(BPM)은 층마다 최대 50%만 줄일 수 있어 얕은 split 지점에서는 강한 압축이 불가능하다는 문제의식이다. variational information bottleneck이 CLS token을 latent z(DeiT-S 기준 192차원)로 압축해 전체 CLS 대신 전송하고, z로부터 만든 k개 anchor에 patch를 softmax soft-assignment로 가중평균 병합해 한 번에 정확히 k개 token을 만들며, backbone은 frozen이고 VIB와 gate만 학습한다(DeiT-S k=8 기준 0.82M, backbone 대비 3.7%). ImageNet-1K top-1이 9번째 층 split·k=8에서 DeiT-S 78.4(원본 79.8, ToMe 70.39, 미세조정 기법 SPOT 74.68)·DeiT-T 69.23(ToMe 56.66)이고 6번째 층 split·k=8에서는 DeiT-S 71.45(ToMe 19.63)이며, k=64에서는 DeiT-S 79.2로 미세조정 기법 SPOT(79.51)·DynamicViT(79.3)와 비슷하고, k=8 전송 값 수는 DeiT-S 기준 3,264개로 전체 activation(75,648개)의 약 4%다. 한계로 CLS token readout backbone을 전제하고, 완만한 예산에서도 정확도 손실이 남으며, 예산·split 층 변경에 덜 유연하고, 비용 이점은 공유 backbone이 공개 호스팅된다는 가정에 기댄다고 밝힌다.

**코드**: 공개([Borakleon/Consomme](https://github.com/Borakleon/Consomme)), 저장소에 라이선스 파일 없음

**태그**: efficient-inference, token-merging, split-inference, peft

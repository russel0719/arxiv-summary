# arXiv cs.CV Daily Digest — 2026-11-03 (arXiv 공개일)

- **전체 신규 논문 수**: 395편 (new 333 + cross-list 62)
- **선별 수**: 12편

## 오늘의 트렌드

MRI·병리·초음파·수술 영상을 다루는 의료 영상이 가장 두꺼운 군집이고, 장기(long-horizon) 영상 생성과 video world model, VLM 추론·벤치마크가 뒤를 잇는다. 3D Gaussian Splatting 재구성과 자율주행 계획·인지도 큰 덩어리를 이룬다. 방법론으로는 frozen DINOv3·CLIP 특징 위에 얹는 training-free 추론 모듈과, 벤치마크·평가 절차의 가정을 반례로 검증하는 감사(audit)형 연구가 두드러진다.

---

### [Déjà Vu: Cycle-Consistent Re-ranking for Semantic Correspondence](https://arxiv.org/abs/2611.00328)

**한 줄 요약**: semantic correspondence의 최종 단계를 greedy top-1 대신 「후보 회수 → cycle-consistency 재정렬」로 바꾸는, 기존 similarity matrix만 쓰는 test-time decoding 모듈.

**핵심 기여**: 사전학습 특징의 zero-shot 대응 능력은 강한데 최종 매칭이 top-1 nearest neighbor로 끝나 정답이 상위 후보에 있어도 놓친다는 문제의식이다(SD+DINO 특징의 top-30 recall이 PCK@0.10 기준 94.9로, 지도학습 모델 top-1 87.55를 넘는다). similarity 분포의 softmax 누적 확률(p=0.9)로 후보 수를 1~30 사이에서 적응적으로 정하고, 각 후보를 source로 역매칭해 원래 keypoint와의 거리만큼 감점하는 graded cycle-consistency 점수로 재정렬한다. SPair-71k PCK@0.10에서 TLR 69.4→71.2, CleanDIFT 69.9→71.5, DIY-SC 74.3→74.6 등 세 baseline을 모두 높이고, PF-Pascal PCK@0.15에서 최대 +3.4, Keypoint Average Precision에서 +4.9를 보고한다. 한계로 정답이 후보에 있으나 1위가 아닌 keypoint 중 7.1%만 바로잡아 recall과의 격차가 크게 남고, 좌우 대칭 부위처럼 거울 대칭인 대응은 cycle-consistency로 구분하지 못한다고 밝힌다.

**코드**: 불명

**태그**: correspondence, feature-matching, training-free

---

### [Pair-Relative Partial Equivariance for Rotation-Robust Keypoint Descriptor Matching](https://arxiv.org/abs/2611.02751)

**한 줄 요약**: frozen keypoint descriptor에 붙이는 steerer를 정확한 SO(2) 표현에서 풀어, 이미지쌍의 실제 상대 회전 분포에 맞춘 부분 등변성(partial equivariance)으로 회전 강건 매칭을 높이는 PaSteer.

**핵심 기여**: upright 영상으로 학습한 descriptor는 큰 in-plane 회전에 무너지는데, Steerers처럼 descriptor 공간에 단일 정확한 군 표현을 강제하면 각도별 응답이 그 표현을 따르지 않는 descriptor에는 너무 경직되다는 문제의식이다. 고정된 비등변 descriptor에 대한 각도별 최적 선형 steerer가 군 합성 법칙을 일반적으로 따르지 않음을 보이고, identity 보존 residual steerer(PaSteer-soft)와 자유형 Fourier steerer(PaSteer-free, 약 0.85M 파라미터)를 제안한다. frozen DeDoDe-B에서 exact steerer 대비 MegaDepth-1500 C4 AUC@5 32.5→36.4, IMC-PT SO2 AUC@20 41.1→50.6, Roto-360 92.0→93.4, AIMS AP 48.6→50.1이며, C8 steering map을 미리 계산해 추론 비용은 exact steerer와 같다. 한계로 DeDoDe descriptor에서만 평가했고, descriptor와 steerer를 함께 학습하면 이득이 거의 사라져(DeDoDe-G에서는 upright가 49.7→45.8로 떨어짐) 사실상 frozen descriptor 개조용이라고 밝힌다. WACV 2027 채택.

**코드**: 불명

**태그**: feature-matching, correspondence, training-free

---

### [Object-Only Is Not Context-Free: A Counterfactual Diagnostic for Context Removal in Object Retrieval](https://arxiv.org/abs/2611.01962)

**한 줄 요약**: 배경을 mask하고 pooling한 object descriptor가 실제로는 주변 문맥을 이미 흡수하고 있음을 반사실(counterfactual) 실험으로 재는 진단 프로토콜(KAP)과, 그 의존도를 줄이는 경량 adapter.

**핵심 기여**: object-centric 검색 파이프라인은 배경을 가린 뒤 특징을 pooling하면 물체만의 descriptor가 된다고 가정하지만 이를 검증한 적이 드물다는 문제의식이다. COCO·ADE20K panoptic mask로 pooling 영역은 고정한 채 영역 밖 픽셀만 바꾸는 Keyhole Aperture Probe를 만들어 backbone의 문맥 의존도를 한 수치로 요약한다. 10개 최신 backbone에서 object-only descriptor는 전체 이미지 정확도의 약 1/4~2/3만 유지하고, 배경을 빈 값으로 채우면 descriptor가 자기 물체가 아니라 무지 배경 이미지와 매칭되며, 이 현상은 Transformer뿐 아니라 CNN에서도 나타난다. 문맥 제거에도 descriptor가 안정되도록 유도하는 adapter는 의존도를 낮추고 INSTRE instance retrieval을 높이며 ILIAS로도 정확도를 유지·개선하는 반면, 같은 조건의 contrastive fine-tuning 대조군은 이 이득을 재현하지 못한다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, dataset-benchmark

---

### [Balancing Representations by Identifying and Generating Under-represented Data](https://arxiv.org/abs/2611.02952)

**한 줄 요약**: SSL encoder가 스스로 커버리지가 얇은 이미지를 kNN 거리로 골라 frozen image-to-image diffusion으로 변형본을 추가하고 사전학습을 이어가는 label-free 데이터 보강 루프(BRIDGE).

**핵심 기여**: 비라벨 corpus가 long-tailed이면 SSL 표현이 빈번한 mode 주변에만 촘촘해지고, 기존 long-tailed SSL 목적함수는 이미 있는 이미지의 가중치만 바꿀 뿐 새 이미지를 더하지 않는다는 문제의식이다. 현재 encoder가 모든 source 이미지를 평균 kNN 거리로 점수화하고, 지지(support)가 얇으면서 생성기가 충실한 변형을 만들 수 있는 점수 구간에서 예산 내 anchor를 골라 diffusion으로 국소 변형을 추가한다. 이를 recoverability 가중 할당 문제로 정식화해, 유한 예산에서 극단 tail을 뺀 희소 구간을 택해야 하는 조건과 매 보강 후 재할당이 최적인 조건을 유도한다. 다섯 가지 long-tailed·web-scraped·합성 source 조건에서 7개 과제 linear-probe·kNN 평균이 비교 방법 중 가장 높고, ViT-S의 contrastive·self-distillation 목적, low-label fine-tuning, semantic segmentation으로도 이득이 이어지며, 생성 보강은 제외한 실제 이미지를 되돌린 oracle과 맞먹는다. masked reconstruction 목적에서는 linear-probe 이득이 더 작다고 밝힌다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, generative

---

### [Accurate automated photo-identification of Near Eastern and European fire salamanders](https://arxiv.org/abs/2611.01601)

**한 줄 요약**: SuperPoint+LightGlue zero-shot local-feature 매칭으로 도롱뇽 개체를 반점 무늬로 재식별하는, 종별 학습 없는 photo-identification 파이프라인.

**핵심 기여**: 포획-재포획 모니터링에서 참조 라이브러리가 커질수록 수작업 개체 식별이 느려지고 오류가 늘어난다는 문제의식이다. 노란 반점 패턴을 분리한 뒤 고신뢰 keypoint 매칭 수로 유사도를 매기고(반점이 많은 개체가 가짜 매칭을 쌓는 교란을 줄임), 2단 clustering으로 데이터베이스 전체에 identity를 부여한다. 이스라엘 북부 야외 사진 2,440장에서 held-out 개체 query의 95.2%가 정답 개체를 1위로 찾고 ARI 0.958을 보이며, 파이프라인 보조 전문가 검토로 기존 오식별을 고쳐 identity 수가 약 1/4 줄었다. 수정 없이 European fire salamander 두 데이터셋에서 top-1 95.1%·91.7%, 재포획 인식 93.7%(기존 프로그램 5종 38~77%, 육안 93.9%)를 기록한다.

**코드**: 불명

**태그**: feature-matching, re-identification, fine-grained, training-free

---

### [VLM-as-a-Judge for Person Re-Identification](https://arxiv.org/abs/2611.03027)

**한 줄 요약**: frozen ReID 전문 모델들의 짧은 후보 목록을 범용 VLM이 zero-shot judge로 재정렬해 옷 바뀜(cloth-changing) ReID 성능을 크게 높이고, 전문가 간 불일치 시에만 VLM을 부르는 gate로 비용을 줄인 연구.

**핵심 기여**: cloth-changing ReID는 방법마다 의존하는 identity 단서가 달라 한 벤치마크의 선두가 다른 벤치마크에서 무너진다는 문제의식이다. 공개 ReID 모델이 학습한 적 없는 장기 CC-ReID 벤치마크 CHIRLA 4개 시나리오에서, 두 frozen expert의 후보를 VLM이 재정렬하면 rank-1이 최고 expert 대비 평균 12.9 point, 두 expert의 단순 ensemble 대비 9.4 point 오르며 대상 데이터로 fine-tuning한 구성요소는 없다. 파이프라인 FLOPs 대부분이 VLM에서 나오므로, 두 expert의 rank-1이 다를 때만 VLM을 호출하는 threshold 없는 gate를 두어 호출의 40%를 없애고 rank-1은 유의한 하락 없이 유지하되 mAP는 1.8~3.8 point 내준다.

**코드**: 공개([bdager/JudgeReID](https://github.com/bdager/JudgeReID))

**태그**: re-identification, image-retrieval, vlm, training-free

---

### [PRISM-Net: Dynamic Routing Network with VLM-Guided Disentangled Attribute Distillation for Explainable Fine-Grained Product Retrieval](https://arxiv.org/abs/2611.00458)

**한 줄 요약**: 상품 이미지 특징을 윤곽(line)·색(color) expert 경로로 분리하고 SigLIP zero-shot prompt로 속성 라벨 없이 지도한 뒤 meta-router로 다시 합치는 fine-grained 상품 검색 구조.

**핵심 기여**: 대규모 e-commerce 검색은 거시 카테고리와 윤곽·색 같은 미세 속성을 함께 가려야 하는데 CNN·ViT backbone은 특징 얽힘(entanglement)과 shortcut 학습을 겪는다는 문제의식이다. 1단계에서는 gradient를 끊은 routing gate와 SigLIP zero-shot text prompt의 sigmoid 의미 증류로 구조·색 expert를 따로 지도하고, 2단계에서는 분리된 expert 임베딩을 학습된 meta-router gate로 base 특징과 적응적으로 섞어 카테고리 경계를 보정한다. 18개 카테고리 275,454장 5-fold 교차검증과 55,091 query 대 220,363장 gallery 검색에서 SwinV2·ConvNeXt-V2·DINOv3 모두 개선되며, SwinV2 기준 product mAP@10 80.98→83.90%, line mAP@10 +5.74%, color mAP@10 +9.12%다. router gate 분석에서는 가전·하드웨어에 구조 가중치가 최대 6.8배 높고 의류에는 색 가중치가 96% 이상 배정된다.

**코드**: 불명

**태그**: fine-grained, image-retrieval, metric-learning, distillation

---

### [Beyond the Last Layer: Global Inter-Layer Aggregation for AI-Generated Image Detection](https://arxiv.org/abs/2611.00017)

**한 줄 요약**: frozen encoder의 여러 깊이에서 global 표현을 뽑아 inter-layer self-attention으로 상호작용시키고 적응적으로 합치는 AI 생성 이미지 검출기(GILA).

**핵심 기여**: 사전학습 vision encoder 기반 검출기 다수가 마지막 층 global 표현만 써서 중간층 정보를 활용하지 못하고, 생성기 갱신·분포 변화에 따른 cross-dataset 일반화가 약하다는 문제의식이다. 서로 다른 깊이의 global 표현을 layer token으로 두고 층 간 self-attention으로 문맥화한 뒤 적응 가중으로 aggregation하며, encoder는 fine-tuning하지 않고 특정 사전학습 목적에도 묶이지 않는다. 사전학습 목적이 다른 3개 backbone, 학습에 본 10개 생성기, 3개 외부 데이터셋에서 검출 성능과 cross-dataset 일반화가 개선된다고 보고한다(초록에 구체 수치는 없음).

**코드**: 불명

**태그**: forgery-detection, foundation-model, image-embedding

---

### [Out-of-distribution AI-generated image detection with zero-phase deconvolution for residual whitening](https://arxiv.org/abs/2611.00043)

**한 줄 요약**: 이미지 noise residual의 공간 상관을 zero-phase deconvolution으로 백색화(whitening)해 생성기별 지문을 지우고, 학습에 없던 생성기로의 일반화를 높이는 AI 생성 이미지 검출 전처리.

**핵심 기여**: AI 생성 이미지 검출기는 학습에 포함되지 않은 생성기 이미지에서 성능이 크게 떨어지는데, 실제·생성 이미지 출처 간 forensic bias가 그 원인이라는 문제의식이다. 생성기 특유의 상관된 noise 패턴을 제거하는 학습 과정을 deconvolution 전처리로 근사해, noise residual의 공간 분포를 백색화한 입력으로 검출기를 학습한다. 백색화한 residual로 end-to-end 학습한 CNN은 원본 이미지로 학습한 경우보다 학습에 없던 생성기에서 검출 성능이 평균 12.6% 높다.

**코드**: 불명

**태그**: forgery-detection, print-forensics

---

### [VerdictAD: Few-Shot Anomaly Detection via Decision-Guided Refinement](https://arxiv.org/abs/2611.02654)

**한 줄 요약**: 기존 few-shot anomaly detector의 점수·map을, 소수 정상 참조 대비 query와 국소 영역을 판정하는 typed decision model의 확률로 다듬는 training-free plug-and-play 프레임워크.

**핵심 기여**: query와 정상 참조 간 특징 차이로 이상을 재는 방법은 정상 외관 변동에도 높은 점수를 주고, 구조·논리 이상처럼 국소 특징 차이가 약한 결함은 놓친다는 문제의식이다. 텍스트 생성 없이 구조화된 decision 확률을 직접 내는 typed decision model로 이미지 전체와 국소 영역을 정상 참조와 비교하고, Global Verdict Refinement(GVR)는 이미지 수준 판정으로 anomaly score를, Local Verdict Refinement(LVR)는 영역 판정을 모아 anomaly map을 보정한다. 단순한 DINOv2 기반 detector와 결합해 one-shot·few-shot에서 경쟁력 있는 성능을 내고, MVTec AD·VisA·MVTec LOCO AD에서 기존 detector들을 일관되게 개선한다고 보고한다.

**코드**: 공개([sgstq0811/VerdictAD-Jev-AD](https://github.com/sgstq0811/VerdictAD-Jev-AD))

**태그**: anomaly-detection, industrial-inspection, defect-detection, training-free

---

### [Reproducing INP-Former: Reconstructing Intrinsic Normal Prototypes for Industrial Anomaly Detection](https://arxiv.org/abs/2611.01230)

**한 줄 요약**: memory bank 없이 test 이미지 자체에서 정상 prototype을 뽑아 재구성하는 INP-Former를 재현하고, MVTec AD 2에서 원 논문의 결론이 얼마나 이어지는지 검증한 재현 연구.

**핵심 기여**: 공개 코드로 MVTec AD·VisA 보고 성능을 재현한 뒤 평가를 MVTec AD 2로 넓히면, 기본 설정의 image AUROC가 MVTec AD 99.7에서 63.4로 떨어진다. MVTec AD 5-seed ablation에서는 성능 대부분이 INP 메커니즘에서 오고 두 보조 loss는 지표에 따라 방향이 바뀌는 작은 변화만 주며, 두 loss를 끈 paired 비교로 MVTec AD 2에서도 INP의 이득을 확인한다. 기본 prototype 6개는 MVTec AD·VisA에서는 4개 이후 plateau가 재현되지만 MVTec AD 2에서는 prototype 1개가 public split과 두 hidden test split 모두에서 AU-PRO가 더 높다. 해상도·backbone 크기·학습 길이·LoRA 적응의 trade-off와 결함 크기·조명 조건·더 엄격한 AU-PRO 한계별 성능도 측정해, 원 벤치마크의 여러 결론이 어려운 데이터로 이어지지 않는다고 밝힌다.

**코드**: 공개([garasnote/Repro-INPFormer](https://github.com/garasnote/Repro-INPFormer))

**태그**: anomaly-detection, industrial-inspection, dataset-benchmark

---

### [Circumventing Magnitude Collapse via Modular Two-Stage Open-Set Recognition](https://arxiv.org/abs/2611.03421)

**한 줄 요약**: open-set recognition을 표현학습과 후처리의 2단 모듈로 보고 둘의 상호작용을 체계적으로 조사해, known-unknown 데이터를 쓰는 표현학습이 대규모에서 특징 크기 정보를 망가뜨리는 magnitude collapse를 밝힌 연구.

**핵심 기여**: OSR 연구가 표현학습과 후처리 방법을 따로 발전시켜 왔고 둘의 상호작용은 조사되지 않았다는 문제의식이다. 데이터셋 규모와 known-unknown 데이터 사용 여부를 바꿔 가며 조합을 실험한 결과, known-unknown 데이터를 쓰는 표현학습은 소규모에서는 뛰어나지만 대규모에서는 판별 정보를 되돌릴 수 없게 파괴하는 magnitude collapse로 성능이 떨어진다. 이를 피하는 단순한 K+1 class classifier와 magnitude-aware 후처리 조합으로 state-of-the-art를 달성하며, known-unknown 데이터를 쓴 소규모 평가가 대규모 성능을 예측하지 못해 현재 OSR 평가 관행이 유효하지 않다고 주장한다.

**코드**: 공개([TwoDigitsOneNumber/Two-Stage-OSR](https://github.com/TwoDigitsOneNumber/Two-Stage-OSR))

**태그**: calibration, open-set-recognition, dataset-benchmark

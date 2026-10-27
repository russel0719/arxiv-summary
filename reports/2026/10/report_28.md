# arXiv cs.CV Daily Digest — 2026-10-27 (arXiv 공개일)

- **전체 신규 논문 수**: 290편 (new 235 + cross-list 55)
- **선별 수**: 10편

## 오늘의 트렌드

3D Gaussian Splatting의 압축·학습 효율 개선과 VGGT류 feed-forward 3D 재구성이 가장 두꺼운 군집이고, MRI·OCT·병리·수술 영상을 다루는 의료 연구가 뒤를 잇는다. 상호작용형 video world model·VLA 정책과 MLLM visual token pruning·압축의 신뢰성 점검이 또 다른 덩어리이며, frozen encoder의 특징·가중치 변화를 probe로 해부하는 표현 분석 연구도 여러 편 묶인다.

---

### [The Locality Trade-off in Masked Patch Self-Distillation](https://arxiv.org/abs/2610.33223)

**한 줄 요약**: DINOv2/v3의 핵심 구성요소인 iBOT식 masked patch self-distillation이 patch 특징의 국소 정보(외형 복원 가능성·공간 대응)를 모델 크기에 따라 다른 형태로 잃는다는 것을 두 가지 무라벨 진단으로 보인 분석 연구.

**핵심 기여**: masked patch self-distillation이 의미적 이득을 주지만 국소 시각 정보에 미치는 영향은 불분명하다는 문제의식이다. ImageNet-1K 300 epoch로 ViT-S/B/L/H(patch 16, register 4개)를 DINO와 DINO+iBOT으로 짝지어 학습하고(총 약 3,964 H200 GPU-hour), frozen patch token에서 RGB 평균·히스토그램·HOG·DCT·LBP를 ridge로 복원하는 Local Appearance Decodability와 patch 매칭·region IoU로 재는 Local-to-Global Correspondence를 진단으로 쓴다. iBOT을 더하면 VOC2012 분할 mIoU가 ViT-L 71.93→79.63, ViT-H 72.88→81.95로 오르지만, patch 매칭 정확도는 ViT-S/B에서 약 11.8/16.9 point 떨어지고 ViT-L/H에서는 약 3.3/4.0 point 오르는 대신 깊은 층에서 픽셀·texture 정보의 선형 접근성이 낮아지며, ViT-B의 Gram anchoring은 DAVIS J&F를 55.5→57.6(표준)·61.4(DINO-Gram), patch 매칭을 24.8→30.1·40.8%로 회복시키지만 patch 관계 보존이 두 성질의 동시 개선을 보장하지는 않는다고 분석한다. 한계로 ImageNet-1K·300 epoch에 한정되고, iBOT 가중치 1 고정·선형 probe만 사용·비교마다 단일 run이며, 규모 간 차이가 drop-path·batch 크기와 섞여 있고 masking 효과와 loss 효과를 분리하지 않았다고 밝힌다.

**코드**: 공개([winci-ai/jea](https://github.com/winci-ai/jea) · Apache-2.0, `gram_loss.py`는 DINOv3 License), 사전학습 체크포인트는 미포함(논문에 공개 계획 명시)

**태그**: ssl-backbone, correspondence, representation-analysis, dense-prediction

---

### [Improving Signals, Declining Encoder: A Known-Answer Test of Label-Free Monitoring in Self-Supervised Learning](https://arxiv.org/abs/2610.35766)

**한 줄 요약**: 생성 요인을 아는 합성 이미지로 LeJEPA encoder를 학습해, encoder가 이미 배운 정보를 잃는 동안에도 loss와 무라벨 특징 통계(RankMe 등 11종)는 계속 '개선'으로 읽힌다는 사례를 보인 known-answer 시험.

**핵심 기여**: SSL 학습은 loss와 학습된 특징의 통계로 라벨 없이 감시하지만, 자연 이미지에서는 정답을 모르므로 이 신호들이 encoder의 퇴행을 잡는지 검증할 수 없다는 문제의식이다. calorimeter 시뮬레이터 기반 4채널 64×64 합성 이미지(epoch마다 새로 64k장)로 축소된 two-view LeJEPA를 ViT-Nano(0.7M)·ViT-Tiny(5.4M)로 300 epoch 학습하고, 생성 요인(형상 z1·z2, log-energy)의 ridge probe R²를 정답 지표로 삼아 RankMe·LiDAR·α-ReQ 등 11개 무라벨 신호와 CUSUM·EWMA·Page–Hinkley 변화점 검출을 대조한다. 기본 설정 10 seed 중 9개에서 요인 가독성이 급락한 뒤 회복되지 않았지만 loss는 계속 내려갔고 RankMe는 확인한 13 run 모두에서 올랐으며, 퇴행 시작 이후 11개 중 8개 신호가 퇴행 run을 비퇴행 run보다 좋게 평가했고, 사후에 고른 최선의 신호·방법도 26건 중 9건만 10 epoch 안에 경보했으며, loss·RankMe·LiDAR로 고른 checkpoint는 마지막 checkpoint와 같은 수준의 손실(가독성 중앙값 0.21)을 보였다(MAE는 10 run 중 퇴행 0건). 한계로 생성기 하나·소형 encoder·축소된 LeJEPA 설정만 다뤄 자연 이미지·대규모에서의 빈도는 보이지 못하고, probe 가독성 저하가 곧 정보 소실을 뜻하지는 않으며, 검토한 변화점 검출 3종 밖의 방법으로는 탐지될 수도 있다고 밝힌다.

**코드**: 불명 (논문에 [nilotpal09/improving-signals-declining-encoder](https://github.com/nilotpal09/improving-signals-declining-encoder) 저장소와 Zenodo 체크포인트가 명시돼 있으나 확인 시점에 두 링크 모두 열리지 않음)

**태그**: ssl-backbone, training-monitoring, representation-analysis

---

### [Learning Discriminative Prototypes via Boundary Repulsion MixUp for Object Re-Identification](https://arxiv.org/abs/2610.34305)

**한 줄 요약**: 신원마다 학습 가능한 prototype을 두고, 혼동되는 신원 쌍 사이에 만든 경계 proxy에서 특징을 밀어내는 Boundary Repulsion MixUp으로 DINOv3 기반 object ReID 임베딩의 신원 간 경계를 날카롭게 하는 방법(PBR-ReID).

**핵심 기여**: ReID의 가장 어려운 오류는 비슷한 신원끼리 맞닿는 경계에서 생기는데 pairwise loss는 이 영역을 간접적으로만 다루고, 일반 MixUp은 오히려 그 경계를 흐린다는 문제의식이다. DINOv3 ViT-B/16과 신원별 L2 정규화 prototype을 함께 학습하며, prototype 유사도(τ=0.7)로 혼동 쌍을 찾아 두 prototype을 섞은 경계 proxy를 만들고 원래 특징을 그 proxy에서 margin만큼 밀어내는 BRM을 batch-hard triplet·prototype triplet·center loss와 묶어, prototype warmup 10 epoch 후 EMA(0.999) joint fine-tuning을 한다(단일 RTX 4090, 추론 시 prototype은 버리고 cosine 최근접 검색). mAP/Rank-1이 Market-1501 94.0/97.1(SOLIDER 93.9/96.9), DukeMTMC 86.1/93.1(DRFormer 85.5/92.5), MSMT17 79.7/91.2(HPL 79.0/91.0), VeRi-776 88.0/98.1(VehicleMAE 87.6/97.4)이고, BRM을 빼면 Market/Duke mAP가 92.9/84.9, warmup을 빼면 51.4/50.9로 떨어지며 ViT-H+/16 backbone에서는 95.3/90.8이다. 별도 한계 서술은 없고 비지도 ReID 확장을 향후 과제로 든다.

**코드**: 공개([psaltaath/pbr-reid](https://github.com/psaltaath/pbr-reid) · MIT, 포함된 DINOv3 submodule은 DINOv3 License), 학습 가중치는 미공개

**태그**: re-identification, metric-learning, image-retrieval, image-embedding

---

### [Whispers from the Neighbors: Rethinking Caption Consensus as Inference-Time Evidence for Vision-Language Retrieval](https://arxiv.org/abs/2610.33798)

**한 줄 요약**: 검색 대상 이미지에 이미 붙어 있는 다른 caption들을 추론 시점 증거로 써서 frozen dual encoder의 이미지 유사도에 caption 유사도를 더하는 training-free text-to-image 검색 기법과, 그 이득이 어디서 오는지에 대한 분석.

**핵심 기여**: COCO·Flickr30K처럼 이미지마다 caption이 여러 개 붙은 컬렉션에서도 CLIP·SigLIP 같은 dual encoder는 이미지-caption 쌍을 하나씩 따로 채점해, 후보 이미지의 다른 caption을 증거로 쓰지 않는다는 문제의식이다. 후보 이미지의 support caption 임베딩 합(c_i)과 query의 유사도(consensus), 이미지 임베딩에서 c_i 방향을 뺀 잔차와 query의 유사도(residual)를 기본 유사도에 가중합하고(가중치 β·γ만 COCO tune2500에서 grid search), fold마다 support 구성을 고정해 누출 없이 평가한다. 사람이 쓴 support로 9개 frozen encoder의 T2I R@1이 3.4~16.8 point 오르며(OpenCLIP-B/32 COCO 46.90→58.41·Flickr30K 66.76→80.42, SigLIP-B/16 COCO 54.60→60.02), Qwen2.5-VL-3B가 생성한 caption으로는 COCO에서 +2.11~+6.05, 다른 출처의 annotation으로는 최대 1 point이고, residual 항의 겉보기 큰 이득은 leave-one-out 평가에서 정답·오답 후보의 support 구성 차이(집합 크기와 query 제거가 각각 약 절반)에서 생기며 고정 support index에서는 caption 정보의 재가중으로 환원된다. 한계로 DB 이미지마다 설명 텍스트가 있다고 가정하고 alt text 같은 자연 메타데이터는 시험하지 않았으며, 짧은 영어 crowd caption만 다뤘고, 강한 모델(BLIP-2 ITM rerank COCO T2I@1 73.74→74.83)이나 support가 적을 때 이득이 줄어든다고 밝힌다.

**코드**: 공개([nhatkhangcs/clip_consensus](https://github.com/nhatkhangcs/clip_consensus)), 저장소에 라이선스 파일 없음

**태그**: image-retrieval, cross-modal-retrieval, training-free

---

### [Does VGGT Know What It Does Not Know?](https://arxiv.org/abs/2610.35806)

**한 줄 요약**: VGGT의 frozen 특징에 선형 probe를 얹으면 VGGT 자체 confidence로는 드러나지 않는 이미지쌍 상대 pose 실패를 예측할 수 있고, 그 정보는 두 시점을 섞는 aggregator 층에서 계산된다는 분석.

**핵심 기여**: VGGT 같은 feed-forward 3D 재구성 모델은 한 번의 forward로 카메라와 기하를 회귀하지만 예측한 pose의 불확실성을 내놓지 않아, 틀린 상대 pose와 맞는 pose를 구분할 수 없다는 문제의식이다. 사람이 대응점을 단 어려운 이미지쌍 벤치마크 HardMatch(903쌍·97 카테고리, VGGT가 34.9%에서 median epipolar 오차 50 px 초과로 실패)에서 frozen VGGT(1B)의 마지막 global(cross-frame) attention block token을 평균해 128차원 PCA 후 logistic regression으로 실패 여부를 예측하고, 카테고리 단위 10-fold로 처음 보는 카테고리에서 평가한다. 실패 예측 ROC-AUC가 probe 93.5로 VGGT point-map confidence 79.7, VGGT 전체 출력으로 학습한 분류기 77.7보다 높고 per-image encoder block에서는 59.3~65.0에 그치며, 50%만 남기는 기권(abstain)에서 남은 쌍의 실패율이 3.8%(confidence 12.4%, oracle 0%)이고, 재학습 없이 PhotoTourism 회전 실패(15° 초과)에 ROC-AUC 97.5로 전이되며 π³에서도 probe 91.7 대 자체 confidence 62.2로 재현된다. 한계로 HardMatch에 정답 pose가 없어 실패 라벨이 회전·이동·내부 파라미터 오차를 섞고, 이미지쌍만 다뤄 다시점에서는 이점이 분명하지 않으며, probe 학습에 실패 라벨이 필요하고 ScanNet의 짧은 baseline 이동 실패는 confidence보다 못 잡는다(ROC-AUC 44~48 vs 61~64)고 밝힌다.

**코드**: 공개 예정 (논문에 코드 공개 명시, 저장소 URL 없음)

**태그**: 3d, correspondence, failure-prediction, abstention

---

### [Printed and Scanned: Exposing the Fragility of Single-Image Morphing Attack Detectors under Print-Scan Degradation](https://arxiv.org/abs/2610.35682)

**한 줄 요약**: SYN-MAD22의 bona fide·morph 이미지를 실제로 인쇄하고 300/600 DPI로 재스캔한 MAD22-PS를 만들어, 디지털 데이터로만 학습된 single-image 모핑 공격 탐지기(S-MAD) 8종의 평균 EER이 3배 이상 오름을 보인 벤치마크 연구.

**핵심 기여**: 일부 국가의 여권 발급 절차는 신청자 사진을 인쇄·재스캔하는데, 이 과정의 halftoning·resampling·색공간 변환·센서 노이즈가 S-MAD 모델이 의존하는 고주파 artifact를 가릴 수 있음에도 공개 벤치마크는 디지털 이미지만 다룬다는 문제의식이다. SYN-MAD22의 5,687장(bona fide 204, 6개 모핑 알고리즘의 morph 5,483)을 Xerox PrimeLink C9065로 70×100 mm 광택지에 인쇄하고 Konica Minolta bizhub C250i(300/600 DPI)와 교차 확인용 C450i로 무손실 스캔해 5개 조건 28,435장을 만든 뒤, 공개 가중치로 SMDD 디지털 데이터에서만 학습된 8개 탐지기를 추가 조정 없이 평가한다. 평균 EER이 디지털 11.00%에서 PS600 41.85%·PS300 41.72%로 오르고(두 번째 스캐너 38.96~39.78%), FD-MAD는 5.10→77.51%, MADation ViT-B는 11.89→53.56%, 가장 덜 떨어진 SelfMAD++도 1.06→7.27%이며, 스캔 해상도에 따른 평균 EER 차이는 0.13 pp에 그친다. 한계로 프린터 하나·용지 하나만 써서 다른 하드웨어·용지에서는 열화 양상이 다를 수 있고, print-scan을 고려한 학습은 다루지 않아 결과는 디지털 학습 탐지기의 일반화 측정이라고 밝힌다.

**코드**: 공개 예정 (논문에 채택 시 공개 명시, URL 없음)

**태그**: forgery-detection, print-forensics, dataset-benchmark, face-morphing

---

### [SGDB: Semantic-Geometric Decoupling and Evidence Binding for Logical Anomaly Detection](https://arxiv.org/abs/2610.34897)

**한 줄 요약**: 부품의 정체와 길이 같은 기하 측정을 따로 읽고, 측정값을 해당 부품에 묶은 뒤 정상 데이터로 정한 규칙을 실행해 판정하는 logical anomaly detection 프레임워크.

**핵심 기여**: logical anomaly 검출은 부품 인식과 측정이 함께 필요한데, 정체와 개수가 맞아도 기하가 틀릴 수 있고 깨끗해 보이는 mask 조각이 잘못된 길이를 줄 수 있다는 문제의식이다. ImageNet 초기화 WideResNet50-2 기반 frontend(center·box·mask·endpoint head)와 별도의 2층 Transformer semantic decoder를 부품 annotation이 있는 정상 이미지로 학습하고, 같은 클래스 안의 부분 일대일 Hungarian 대응으로 기하 증거를 정체에 묶되 대응되지 않은 물체도 개수에 남기며, 품질·소유권 검사를 통과한 PCA 축만 길이 측정에 쓰고, 정상 데이터에 맞춘 구간 규칙 점수를 별도 정상 calibration 점수의 95 percentile 임계로 판정한다(설명 문장은 frozen Qwen3-VL-8B가 text-only로 작성하고 수치는 executor가 유지). MVTec LOCO 논리 이상 5개 카테고리에서 image AUROC/F1 98.19/94.52(SALAD 96.42/86.45, LogiCo 94.49/87.84), VID-AD 50개 과제에서 93.56/92.76(Qwen3-VL-8B 88.44/77.11, ComAD 83.60/70.22)이며, 고정 임계에서 정상 이미지 오경보율은 LOCO 1.43%, VID-AD 11.36%다. 별도 한계 절은 없으나 낯선 장면 확장과 부품 감독 축소를 향후 과제로 들고, 신뢰구간이 다중비교 보정 없이 test cohort 변동만 반영한다고 밝힌다.

**코드**: 공개([Qybc/SGDB](https://github.com/Qybc/SGDB)), 저장소에 라이선스 파일 없음, semantic decoder 가중치 15개는 포함되나 visual frontend 가중치는 미포함

**태그**: anomaly-detection, industrial-inspection, logical-anomaly, explainability

---

### [Do Words Matter? What Text Contributes to Few and Full-Shot Vision-Language Anomaly Detection](https://arxiv.org/abs/2610.34610)

**한 줄 요약**: few/full-shot vision-language anomaly detector에서 고정된 정상·이상 text anchor가 기여하는 것은 문장의 의미가 아니라 두 anchor 차이 벡터의 크기(effective scale)와 카테고리 간 anchor 배치뿐임을 증명과 실험으로 보인 분석.

**핵심 기여**: VL anomaly detector의 이득은 흔히 정상·이상 설명문의 의미 덕으로 여겨지지만, few/full-shot에서는 학습된 visual adapter가 끼어 있어 이를 분리해 본 적이 없고 설명을 바꾸면 의미와 기하가 함께 바뀐다는 문제의식이다. 점수가 두 anchor를 차이 벡터로만 읽고 adapter가 어떤 대체 방향으로든 회전할 수 있으므로 차이 벡터 길이(λeff = τ√(2−2ρ))가 같은 대체 anchor는 정확히 같은 확률 맵과 loss를 허용함을 증명하고, CLIP ViT-L/14·DINOv2-L·DINOv3-L backbone과 linear·MLP·Transformer adapter로 의료 7개 데이터셋과 MVTec-AD·VisA에서 scale을 맞춘 random·직교 anchor를 정답 prompt와 비교한다. 의료 K=16에서 정답 prompt·scale-matched random·matched 직교 anchor가 모두 image AUROC 96.3이고 scale을 맞추지 않은 직교 anchor만 95.6(MVFA에서는 94.8→73.7)으로 떨어지며, 한 adapter가 여러 카테고리를 맡는 full-shot에서는 거의 일직선으로 모인 CLIP prompt 축을 의미 없는 카테고리별 회전으로 흩으면 image/pixel AUROC가 VisA 86.2/91.7→91.8/96.1, MVTec-AD 96.2/93.6→97.4/96.6으로 오르고 전체를 같이 회전하면 변화가 0.1 이내다. 한계로 보장은 고정 anchor·회전에 닫힌 adapter·cosine 기반 이진 맵에만 성립하고(MVFA·MadCLIP 결과는 경험적), 모든 anchor가 한 text encoder에서 나와 축이 일직선으로 모이는 현상이 그 encoder에 특유할 수 있으며, 흩뜨림 이득의 간섭 메커니즘은 측정하지 않았다고 밝힌다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, vlm, representation-analysis

---

### [A Canary in the Neural Mine: Catching an Image Classifier's Silent, Confident Failures](https://arxiv.org/abs/2610.33063)

**한 줄 요약**: penultimate 특징의 PCA 잔차 공간에서 클래스별 kNN 거리를 재고 percentile로 보정해 MSP와 가중치 하나로 융합하는, 학습 없는 분류기 고신뢰 오류(silent failure) 탐지기 CANARY.

**핵심 기여**: 배포된 분류기는 신뢰도 높은 예측을 자동 승인하므로 고신뢰 오류가 조용히 전파되는데, 표준 실패 예측기인 MSP는 classifier head에서 읽은 스칼라라 confidence gradient에 직교하는 특징 변화를 1차적으로 보지 못하고, ViM·Mahalanobis 같은 특징 공간 탐지기는 MSP에 이미 담긴 클래스 분리 기하를 재는 탓에 융합해도 보완이 안 된다는 문제의식이다. ID 정답 샘플의 penultimate 특징에서 상위 K(최대 512, 잔차 128차원 이상 유지) PCA 부분공간을 제거한 잔차로 예측 클래스별 k=100 kNN 거리를 구하고, 검증 정답 입력의 경험적 CDF로 percentile 보정한 뒤 S = w·ln s_MSP + (1−w)·ln s_res로 융합하며 w(0.70~0.95)는 clean 검증 데이터 cross-fitting으로 한 번 정한다(임계 없는 순위용 점수, RTX 4080에서 query당 약 50 μs). ViT-B/16·ResNet-50·Swin-B·ConvNeXt-B·EfficientNet-B4와 ImageNet-C·A·R·ObjectNet의 385개 shift cell 중 e-AURC 기준 382개(AUROC 기준 379개)에서 MSP와 같거나 낫고 최악 하락은 −0.0002 AUROC이며(차순위 SIRC는 289개, 최악 −15.0), 이득은 MSP 품질이 낮을수록 커져 e-AURC×10³가 EfficientNet-B4 87.5→78.0, ViT-B/16 58.2→57.8이다. 한계로 순수 on-manifold 고신뢰 실패는 구조적으로 못 잡고, 이득 크기를 예측하는 'headroom law'는 유도된 것이 아닌 경험적 규칙성이라고 밝힌다.

**코드**: 불명

**태그**: calibration, failure-prediction, training-free, ood-detection

---

### [Semantic Concept Steering Breaks the Explanation Drift Loop in Continual Learning](https://arxiv.org/abs/2610.33877)

**한 줄 요약**: 모델 자신의 saliency를 목표로 삼는 설명 정규화 대신, 오프라인으로 찾아 SAM 3로 위치를 잡은 클래스 공통 개념 영역에 relevance를 고정해 continual learning의 망각과 설명 drift를 함께 줄이는 방법(C³L).

**핵심 기여**: continual learning의 망각은 정확도 하락뿐 아니라, 정확도는 유지한 채 진단적 특징에서 spurious 상관으로 주의가 옮겨 가는 explanation drift로도 나타나는데, 기존 pixel 단위 saliency 정규화는 모델 자신의 frozen saliency에서 목표를 만들어 drift를 오히려 강화하는 자기참조 고리를 만든다는 문제의식이다. GPT-4o-mini로 클래스 속성(예: 'curved beak')을 생성·필터링하고 SAM 3로 개념별 mask를 잡아 모델 상태와 무관한 목표를 만든 뒤, replay buffer(기본 1,000장) 샘플에 한해 LRP(ViT는 AttnLRP) relevance를 개념 영역 안에서 1로 미는 BCE 항과 배경 relevance 안정화 항을 더해 class-incremental 설정(대부분 10 task)에서 ResNet-18·ViT-B/16을 학습한다. ViT-B/16의 ACC/forgetting이 ImageNet-R 82.74/1.89(MOS-R 80.92/2.43), CUB 83.65/2.92(MOS-R 78.82/3.84)이고, ResNet-18 CUB는 79.73/5.32(RRR-LRP 73.25/8.42), 설명 품질 mIoU는 ViT-B CUB 59.86(MOS 54.17), ObjectNet OOD 정확도는 58.04(RRR-ViT 34.49)다. 한계로 foundation model에 의존해 비시각적·모호한 개념은 grounding에 실패하고, 개념 품질 검사가 단순하며 전처리 비용이 추가되고, 배경 기준 saliency가 모델 자신에서 나와 기존 spurious 단서를 없애지 못하고 약화만 한다고 밝힌다.

**코드**: 공개([yonisGit/concept_consistent_continual_learning](https://github.com/yonisGit/concept_consistent_continual_learning) · Apache-2.0), 학습 가중치는 미공개(실행에 SAM 3 gated 가중치와 OpenAI API 키 필요)

**태그**: continual-learning, explainability, spurious-correlation, replay

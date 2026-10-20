# arXiv cs.CV Daily Digest — 2026-10-20 (arXiv 공개일)

- **전체 신규 논문 수**: 346편 (new 289 + cross-list 57)
- **선별 수**: 11편

## 오늘의 트렌드

비디오 생성과 월드 모델이 가장 두꺼운 군집으로, autoregressive video diffusion의 drift 억제·sparse attention 가속과 행동 조건 월드 모델이 이어진다. 장시간 비디오 이해에서는 MLLM 에이전트의 멀티모달 메모리·프레임 선택과 시각 토큰 가지치기가 한 덩어리를 이룬다. 의료 영상(MRI·병리·흉부 X-ray)과 feed-forward Gaussian Splatting·인체-객체 4D 복원도 비중이 크며, 확산 샘플링 가속·one-step 증류가 별도 흐름을 이룬다.

---

### [Your Self-Supervised Projection Head Captures Object Co-Occurrence Statistics](https://arxiv.org/abs/2610.23915)

**한 줄 요약**: SSL 모델에서 백본은 객체 범주를, projection head는 범주 간 동시 출현(co-occurrence) 통계를 계층적으로 인코딩한다는 분석과, 사전학습 데이터의 동시 출현을 통제해 범주 표현 학습을 돕는 실험.

**핵심 기여**: SSL이 의미 있는 시각 표현을 배우는 원리가 충분히 규명되지 않았다는 문제의식에서, 흔한 pretext task가 객체 동시 출현 통계를 암묵적으로 모델링한다는 가설을 세운다. 최신 분할 모델로 COCO·ADE20K·LVIS에서 객체를 잘라낸 데이터셋 3종(최대 1,002개 범주·약 11.8만 장)을 만들고 MoCoV3·BYOL·VICReg·DINO 등을 분석해, 백본은 범주를 담고 projection head는 범주 간 동시 출현을 담는 계층 구조를 보이며, 그 결과 사람의 범주 간 유사도 판단과의 정렬(RSA Kendall's τ)에서 projection head가 백본을 앞선다(본문 기준 BYOL 18.3→22.7, VICReg 17.7→23.5, DINO는 30.5→31.1로 차이가 작음). ImageNet-1k 100 epoch 사전학습에서 동시 출현 비율을 통제하면 최적 비율에서 정확도가 기준 대비 최대 5.52%p 오르고, 비율이 더 커지면 다시 떨어진다. 한계로 아키텍처·SSL 방법별 차이의 원인은 설명하지 못했고, DINOv2 등은 projection head 가중치를 공개하지 않아 검증하지 못했다고 밝힌다.

**코드**: 공개 예정 (본문에 채택 후 공개 명시)

**태그**: ssl-backbone, image-embedding, representation-analysis

---

### [LateMatch: Breaking the Interaction Bottleneck via Cacheable Matching for Efficient Visual Localization](https://arxiv.org/abs/2610.25358)

**한 줄 요약**: deep feature matcher의 이미지 간 상호작용을 마지막 층으로 미뤄, 이미지 내부 처리는 오프라인에 캐시하고 온라인에서는 소수의 Interaction Block만 실행하는 cacheable matching.

**핵심 기여**: SOTA deep matcher는 매 층에서 이미지 내부 문맥 구축과 이미지 간 매칭을 엮기 때문에, 쿼리 1장을 DB 이미지 K장과 맞춰 측위하려면 네트워크 전체를 K번 돌려야 하고 캐시할 여지가 없다는 문제의식이다. LateMatch는 LightGlue·MambaGlue 같은 sparse matcher를 재구성해 이미지 내부 처리를 캐시 가능한 Context Block으로 떼어내고 이미지 간 상호작용은 마지막 Interaction Block에서만 수행하며, 후반 층의 Shannon entropy가 줄어드는 점을 이용해 교차 이미지 상호작용 직전에 토큰 수를 동적으로 줄이는 E-SToRE를 더한다. HPatches·ScanNet·MegaDepth·ETH-3D·Aachen에서 표준 matcher 대비 유효 연산량을 2배 이상 줄이고 E-SToRE로 10~14%를 추가 절감하며, 본문 기준 Aachen(K=50)에서 LightGlue 대비 1,619 ms→721 ms, Day/Night recall 96.0/90.6→94.9/90.6이다. 한계로 9층 원본 LightGlue보다 정확도가 약간 낮고(MegaDepth AUC@10 0.6525→0.6392), 캐시 때문에 사전 매핑된 환경에만 쓸 수 있으며 K=1에서는 오히려 느리고, dense matcher 적용은 향후 과제로 남긴다.

**코드**: 공개([UTAustin-SwarmLab/LateMatch](https://github.com/UTAustin-SwarmLab/LateMatch))

**태그**: feature-matching, correspondence, efficient-inference, visual-localization

---

### [STLQ: Spatio-Topological Linkage Quantization for Approximate Nearest Neighbor Search](https://arxiv.org/abs/2610.23931)

**한 줄 요약**: IVF 클러스터를 directed forest로 조직해 재구성된 부모 벡터 기준의 상대 잔차를 다시 양자화하는 multi-codebook quantization 기반 근사 최근접 탐색(ANNS) 기법.

**핵심 기여**: 대규모 벡터 압축·ANNS에 쓰이는 shallow multi-codebook quantization(MCQ)은 각 IVF 클러스터 안에서 벡터를 독립적으로 인코딩해, 주변 벡터의 재구성 정보를 활용하지 못한다는 문제의식이다. STLQ는 기본 인코딩 단계에서 벡터를 독립 양자화한 뒤, linked 인코딩 단계에서 선택된 재구성 부모 벡터에 대한 상대 잔차를 스케일 계수와 함께 다시 인코딩해 더 정밀한 표현을 얻고, 이에 맞춘 linked-ADC(asymmetric distance computation)로 선형 스캔 복잡도를 유지한다. 스케일 계수와 forest 구조 자체도 압축해 위상 정보 오버헤드를 제어하며, 같은 비트 예산에서 평가한 shallow MCQ들보다 recall이 높고 deep MCQ와는 recall-QPS 상충에서 경쟁력 있는 수준이다. 한계로 오프라인 구축 비용이 더 크다고 밝힌다.

**코드**: 공개([ighxiy/STLQ](https://github.com/ighxiy/STLQ))

**태그**: vector-search, vector-quantization, image-retrieval

---

### [SL-Ground: Sentence-Level Grounding for Fine-Grained Open-Vocabulary Object Detection](https://arxiv.org/abs/2610.24814)

**한 줄 요약**: Grounding DINO 기반 검출기의 토큰 단위 점수화를, 범주 설명 문장 전체의 표현과 객체 쿼리를 직접 비교하는 문장 단위 grounding으로 바꾼 fine-grained open-vocabulary detection.

**핵심 기여**: grounding 기반 open-vocab 검출기는 객체 쿼리를 개별 텍스트 토큰에 정렬하고 토큰 점수를 모아 클래스 점수를 만드는데, 목표 범주가 고립된 단어가 아니라 조합적 설명 전체로 정의되는 fine-grained OVOD에서는 이 설계가 병목이 된다는 문제의식이다. SL-Ground는 각 범주 설명을 CLIP 텍스트 인코더로 문장 단위 표현으로 만들고 객체 쿼리를 이 표현과 직접 점수화해, 프롬프트를 반복 분할(chunking)할 필요를 없앤다. 차종·브랜드·차량 모델 단위로 나눈 다중 granularity Stanford Cars 벤치마크를 구축해 가장 세밀한 차량 모델 단위에서 토큰 단위 변형 대비 AP를 14.5→70.6(동일 후보 샘플링), 전체 어휘 학습 시 86.0으로 높이고, FG-OVD에서는 파인튜닝 시 평균 AP 61.6으로 비교 기법 중 가장 높다(본문 기준 DSAA 54.0). 한계로 파인튜닝 후 open-vocab 유지력이 zero-shot 체크포인트보다 떨어지고, 한 granularity로 학습한 모델이 다른 granularity로 거의 전이되지 않으며, referring expression처럼 단어 단위 대응이 필요한 태스크에는 토큰·하이브리드 설계가 필요할 수 있다고 밝힌다.

**코드**: 불명

**태그**: open-vocab-detection, fine-grained, object-detection

---

### [CorrCLIPv2: Harnessing Unlabeled Images for Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2610.24757)

**한 줄 요약**: class-agnostic 마스크·SSL 특징 기반 attention·마스크 내 투표에, 무라벨 이미지 메모리 뱅크에서의 교차 이미지 객체 검색을 더한 training-free open-vocabulary semantic segmentation.

**핵심 기여**: CLIP은 open-vocab 인식 잠재력이 크지만 클래스 간 패치 상호작용이 잡음을 일으켜 분할 성능이 떨어진다는 문제의식이다. CorrCLIPv2는 class-agnostic 마스크 생성기로 클래스 간 상호작용을 명시적으로 분리하고, self-supervised 모델의 공간적으로 일관된 특징으로 attention 점수를 계산해 마스크 오류를 완화하며, 특징의 공간 디테일과 의미를 함께 정제한 뒤 마스크별 투표로 예측을 통일한다. 여기에 무라벨 이미지로 만든 CorrCLIP 강화 특징 메모리 뱅크와 multi-CLIP 앙상블을 더해, 다양한 맥락에서 검색한 의미적으로 일관된 객체 특징을 모아 맥락에 의한 간섭을 적은 추가 연산으로 줄인다. 표준 벤치마크 10종에서 SOTA를 기록하고, 22개 다중 도메인 데이터셋에서는 완전 지도 open-vocab 기법도 앞선다고 보고한다.

**코드**: 공개([zdk258/CorrCLIP](https://github.com/zdk258/CorrCLIP))

**태그**: segmentation, open-vocab-segmentation, training-free, image-retrieval

---

### [RiSE: Residual Subspace Expert for Generalizable Text-Centric Image Forgery Localization](https://arxiv.org/abs/2610.24480)

**한 줄 요약**: 사전학습 가중치의 주성분 SVD 성분을 동결하고 잔차 부분공간만 위조 유형별 전문가로 적응시키는 텍스트 중심 이미지 위조 위치 추정(TFL) 모델.

**핵심 기여**: 금융·법률 문서의 신뢰를 위해 텍스트 중심 위조 위치 추정이 중요한데, 기존 검출기는 full-parameter fine-tuning으로 low-rank feature collapse와 학습 아티팩트 과적합이 생겨 보지 못한 위조 유형에 일반화하지 못하고, 다양한 위조 흔적을 단일 표현으로 잡아 미세한 흔적이 얽힌다는 문제의식이다. RiSE는 ViT 전용 segmentor에서 주성분 SVD 성분을 동결하고 잔차 부분공간만 적응시키며, 위조 유형별 학습 부분집합으로 독립 학습한 residual expert를 두어 전문가 수가 늘수록 cross-domain 위치 추정 성능이 꾸준히 오른다. 추론 시에는 latent 섭동 출력을 해석적으로 계산하는 Latent Perturbation Confidence(LPC)로 단일 forward pass에서 가장 확신하는 전문가를 고른다. 합성 위조 데이터로만 학습해 전문가 1개로 실제 위조 이미지에서 기존 기법보다 20.4% 높고 학습 step은 1/10이며, 전문가 9개로는 35.8% 향상되고, RGB 사전학습 파라미터 대부분을 동결한 채 DCT 특징을 써도 효과가 유지된다고 보고한다.

**코드**: 공개([KahimWong/RiSE](https://github.com/KahimWong/RiSE) · MIT)

**태그**: forgery-detection, peft, segmentation, ocr-document

---

### [A New Hope for PRNU on Modern Smartphones? Evidence That Device-Specific Fingerprints Survive Computational Photography](https://arxiv.org/abs/2610.25438)

**한 줄 요약**: 최신 스마트폰에서 PRNU 지문이 다른 기기와도 높게 상관되는 원인을 같은 모델의 공통 성분으로 보고, 나머지 후보 카메라들과의 평균 sPCE를 빼는 ΔsPCE로 기기 단위 출처 식별을 복원.

**핵심 기여**: PRNU(Photo Response Non-Uniformity)는 출처 카메라 식별의 가장 신뢰받는 표지지만, 최근 연구들이 최신 스마트폰에서 서로 다른 기기의 이미지와 지문이 높게 상관된다고 보고해 판별력이 의심받는다는 문제의식이다. 3개 브랜드·4개 모델·8개 소프트웨어 버전의 스마트폰 30대를 디지털 줌 없이 통제 촬영(기기당 기준 20장·시험 20장)해, 같은 모델의 모든 지문이 공유하는 성분이 표준 signed peak-to-correlation energy(sPCE)를 부풀린다는 것을 찾고, T-norm 점수 정규화처럼 후보 지문과의 sPCE에서 나머지 후보 지문들과의 평균 sPCE를 빼는 ΔsPCE를 제안한다. 본문 기준 FPR 5%에서의 TPR이 모든 모델·버전에서 오르며, iPhone 17 Pro Max(iOS 26.1)에서 11.2%→93.8%로 가장 크게 오른다. 한계로 데이터셋이 작고, ΔsPCE가 후보 카메라 집합에 의존해 진짜 기기가 후보에 있다고 가정하며, 질의 이미지의 모델·소프트웨어 버전을 알아야 하고, 안정된 임계값의 1:1 검증에는 아직 맞지 않으며 야간·인물·줌 모드는 시험하지 않았다고 밝힌다.

**코드**: 불명

**태그**: camera-forensics, source-attribution, score-normalization

---

### [Predicted Class Correction: Conformal Thresholds for Classes with No Calibration Data](https://arxiv.org/abs/2610.25349)

**한 줄 요약**: 보정(calibration) 예제가 없는 희귀 클래스에도, 분류기 head 가중치의 기하 서술자로 클래스별 conformal 임계값 보정량을 예측해 자체 임계값을 부여하는 Predicted Class Correction(PCC).

**핵심 기여**: class-conditional conformal prediction은 클래스마다 라벨 있는 보정 예제가 필요한데, long-tail 배포에서는 희귀 클래스에 보정 예제가 거의 없어 기존 방법은 정의되지 않거나 공유 marginal 임계값으로 돌아간다는 문제의식이다. PCC는 클래스별 분위수와 marginal 분위수의 차이를 분류기 head의 기하 서술자로 회귀하고, 라벨 있는 클래스에서 고른 스칼라로 예측을 수축한 뒤 단일 marginal offset을 다시 맞추며, 서술자가 가중치에만 의존해 보정 예제가 0개인 클래스도 자체 임계값을 받고 보정 대상이 스칼라 하나라 split conformal의 marginal 보장이 유지된다. ImageNet에서 이런 클래스의 worst-class coverage를 같은 평균 집합 크기에서 0.058 [0.006, 0.110] 높여 test 라벨을 보는 oracle의 42%에 이르는데, 같은 분할의 기준선 8개 중 6개는 변화가 0이고 최선도 0.016(구간이 0 포함)이며, 1,000개 중 100개 클래스만 라벨이 있어도 이득이 유지된다. 또 클래스당 test 예제가 약 35개 미만이면 oracle조차 개선을 보일 수 없어 worst-class coverage는 달성 불가능해지기 전에 측정 불가능해짐을 보이고, 이 깊이 이상으로 평가를 제한하면 Pl@ntNet-300K에서도 유의한 개선이 드러난다.

**코드**: 불명

**태그**: calibration, conformal-prediction, long-tail

---

### [SAGE-CP: When Marginal Coverage Hides Route-Conditional Failures in Adaptive VLM Ensembles](https://arxiv.org/abs/2610.23864)

**한 줄 요약**: 쉬운 이미지는 일찍 멈추고 어려운 이미지는 상위 모델로 넘기는 적응형 VLM 앙상블에서, 라우터가 만든 경로별로 Mondrian split conformal을 따로 보정해 경로 단위 coverage를 보장하는 파이프라인.

**핵심 기여**: 적응형 VLM 앙상블에 conformal 임계값 하나를 쓰면 최종 예측기는 marginal하게 유효해도 개별 연산 경로에서 심하게 실패할 수 있으며, 비중 π인 경로의 조건부 coverage가 max{0, 1−α/π}까지 떨어질 수 있음을 정식화한다. SAGE-CP는 개발 데이터로 라우터를 학습해 라우팅 선택을 고정하고, early exit와 escalation 입력의 반환 점수를 Mondrian split conformal로 따로 보정해 교환가능성 하에서 경로별 유한 표본 coverage를 얻는다. 벤치마크 10종·동결 VLM 4종·5개 분할에서 전역 보정과 SAGE-CP 모두 0.90 목표에 marginal coverage 0.900을 달성하지만, SAGE-CP는 평균 최악 경로 coverage를 0.623→0.887로 올리고 경로 간 coverage 격차를 0.324→0.025로 줄인다. 대가로 평균 예측 집합 크기가 1.893→2.212로 커지지만 전체 앙상블(2.486)보다 작고 원천 모델 호출을 70.6% 줄이며, 드문 경로(세밀한 exit 깊이 그룹)에는 보정 데이터가 더 필요하다고 밝힌다.

**코드**: 불명

**태그**: calibration, conformal-prediction, vlm, efficient-inference

---

### [TriScore: Post-Hoc Out-of-Distribution Detection with Energy, Boundary Probes, and Transform Consistency](https://arxiv.org/abs/2610.26323)

**한 줄 요약**: 동결 분류기에서 energy·결정 경계 취약성·변환 일관성의 세 점수를 ID 검증 데이터로 표준화하고 입력 의존 게이트로 결합하는 post-hoc OOD 검출기.

**핵심 기여**: post-hoc OOD 검출은 보통 confidence·energy·특징·gradient 중 단일 신호에 의존하는데, 분류기 수준의 adversarial shift는 검출기가 고른 단서는 보존한 채 모델의 결정 행동을 바꿀 수 있어 이 방식이 취약하다는 문제의식이다. TriScore는 같은 동결 백본에서 energy prior, boundary-fragility 점수, transform-consistency 점수를 뽑아 ID 검증 데이터로 표준화하고 입력 의존 ID-residual 게이트로 융합하며, OOD 라벨·보조 모델·학습·특징 뱅크 저장이 필요 없다. ImageNet 규모 백본 4종에서 non-adaptive adversarial-shift 프로토콜 하에 post-hoc 기준선 15종 중 평균 AUROC가 가장 높고 표준 OOD 벤치마크에서도 경쟁력을 유지하며, ablation에서 이득이 단일 신호 최적화가 아니라 상보적 단서 결합에서 온다고 보인다.

**코드**: 공개([gursoyege/TriScore](https://github.com/gursoyege/TriScore))

**태그**: ood-detection, open-set, calibration, training-free

---

### [Confidence-Guided Pseudo-Label Refinement for Unsupervised Cross-Domain Person Re-Identification](https://arxiv.org/abs/2610.25633)

**한 줄 요약**: 비지도 cross-domain person re-ID에서 샘플별 신뢰도로 클러스터 적응형 상·하한 임계값을 정해, 의사 라벨을 유지·재할당·보류(defer)의 3-way로 나누는 정제 프레임워크 CGPLR.

**핵심 기여**: 비지도 도메인 적응 re-ID는 도메인 차이로 생긴 잡음 의사 라벨이 반복 적응 중에 강화되고, 기존 클러스터링 기법은 제한된 신뢰도 단서나 전역 기준에 의존해 모호한 샘플에도 hard identity 감독을 준다는 문제의식이다. CGPLR은 centroid 호환성·지역 이웃 일관성·가장 강한 경쟁 클러스터와의 분리도·시간적 할당 안정성을 함께 모델링해 샘플 신뢰도를 추정하고, 이 분포로 클러스터별 상·하한 임계값을 정해 신뢰 할당은 유지하고, 회복 가능한 샘플은 대안 클러스터가 기하·이웃 근거를 충분히 받을 때만 재할당하며, 매우 모호한 샘플은 hard 감독에서 보류한다. 학습 목표도 이에 맞춰 유지 샘플에는 신뢰도 가중 감독, 재할당 샘플에는 보수적 가중, 보류 샘플에는 라벨 없는 표현 일관성 손실을 쓴다. Market-1501→MSMT17에서 Rank-1 76.4%·mAP 47.6%, MSMT17→Market-1501에서 Rank-1 95.1%·mAP 87.7%를 얻는다.

**코드**: 공개([Sundas058/CGPLR](https://github.com/Sundas058/CGPLR))

**태그**: re-identification, domain-adaptation, metric-learning

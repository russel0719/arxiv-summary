# arXiv cs.CV Daily Digest — 2026-10-30 (arXiv 공개일)

- **전체 신규 논문 수**: 233편 (new 197 + cross-list 36)
- **선별 수**: 11편

## 오늘의 트렌드

video world model과 agent harness 기반 이미지·영상 생성·편집이 가장 두꺼운 군집이고, feed-forward 3D Gaussian Splatting과 PET·CT·MRI 의료 영상이 뒤를 잇는다. MLLM의 시각 추론·계수·기억을 재는 벤치마크와 deepfake 탐지의 공정성·일반화 연구도 한 덩어리를 이룬다. 방법론으로는 one-step diffusion distillation과, 기존 벤치마크·평가 프로토콜의 숨은 편향을 감사(audit)하는 흐름이 두드러진다.

---

### [FDSML: Formula-Driven Supervised Metric Learning with Parameter-Aware Triplet Loss](https://arxiv.org/abs/2610.39423)

**한 줄 요약**: fractal 생성 파라미터 사이의 거리로 triplet의 positive/negative를 정해, 실제 이미지 없이 검색용 embedding을 사전학습하는 formula-driven metric learning(FDSML).

**핵심 기여**: 기존 formula-driven supervised learning(FDSL)은 생성 과정이 연속적인데도 이산 클래스 분류로 사전학습해 그 연속성을 버린다는 문제의식이다. 클래스당 perturbation을 1,000개로 늘리고 아핀 변환에 엄격한 수축 제약을 걸며 점유 픽셀 0.05% 미만 샘플을 제거한 FineFractalDB(1,000 클래스 × 1,000장)를 만들고, 각 이미지의 IFS 아핀 파라미터 가중 기댓값(6차원) 사이 거리로 anchor에 더 가까운 쪽을 positive로 두는 Parameter-Aware Triplet loss로 ResNet-50·ViT-Tiny·ViT-Base를 학습한다. ResNet-50 Recall@1은 FractalDB-1k(FDSL) 사전학습 대비 Stanford Online Products 65.6→74.0%, Stanford Cars 56.2→78.4%, In-Shop 87.3→89.2%로 오르고(ImageNet-1k 지도 사전학습은 79.1/87.7/91.1%), ImageNet-C 오류는 다섯 corruption 군 모두에서 줄지만 CIFAR-100 분류는 70.21→68.74%로 낮아지고 ViT-Tiny에서는 Noise·Digital corruption 오류가 늘어난다. 한계로 IFS fractal에서만 검증했고, 100만 장을 넘는 규모에서 이득이 유지되는지와 triplet 구성의 추가 비용은 분석하지 않았다고 밝힌다.

**코드**: 공개([ShineiArakawa/fdsml](https://github.com/ShineiArakawa/fdsml) · CC BY-NC-SA 4.0), FineFractalDB와 ResNet-50·ViT-Tiny·ViT-Base 가중치는 [Hugging Face](https://huggingface.co/fdsml)에 공개(별도 라이선스 표기 없음)

**태그**: metric-learning, image-retrieval, image-embedding, synthetic-pretraining

---

### [Luggage re-identification: A study of strategies towards a real-world application](https://arxiv.org/abs/2610.40643)

**한 줄 요약**: 공항 세관 구역의 다중 카메라 영상에서 수하물을 검출·추적한 뒤, 여러 프레임을 골라 합쳐 재식별하는 end-to-end luggage re-ID 파이프라인 연구.

**핵심 기여**: 기존 수하물 ReID는 깨끗하게 잘린 이미지 매칭에 머물러, 가림·혼잡·복잡한 배경이 있는 실제 장면에서 여러 shot·view를 쓰는 전략이 다뤄지지 않았다는 문제의식이다. CoDETR 검출, 장면별 tracking, 대규모 수하물 데이터셋 MVB로 사전학습한 TransReID(256×256 입력, 유클리드 거리)를 잇고, 실제 공항 세관 구역에서 수하물 116개를 갤러리 카메라 5대·쿼리 카메라 6대로 찍은 데이터(갤러리 트랙 579개·쿼리 트랙 745개, 트랙당 평균 약 18장)에서 프레임 선택·병합 방식과 학습 환경 조합을 비교한다. 검출 신뢰도 상위 5프레임 집계가 Q→G R@1 0.812·mAP 0.784로 무작위 단일 프레임(0.742/0.732)과 전체 프레임 집계(0.792/0.769)보다 높고(bbox 크기 기준 상위 5프레임은 0.815/0.794), 두 번째 환경 테스트에서 MVB만으로 학습한 모델의 0.663/0.646이 두 환경 데이터로 미세조정하면 0.831/0.830으로 오른다. 한계로 트롤리에 쌓인 가방 등에서 검출이 불안정하고, 환경 간 도메인 격차 때문에 새 환경마다 미세조정이 필요하며, 데이터가 한 공항 한 구역에서만 수집됐고 검출·추적에 장면당 약 6.1초가 걸린다고 밝힌다.

**코드**: 불명

**태그**: re-identification, image-retrieval, object-detection, video

---

### [Cross-Encoder Anchor Refinement for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2610.39727)

**한 줄 요약**: 산업 제품 인식으로 미세조정한 별도 CNN encoder의 메모리를 ViT patch anchor가 cross-attention으로 읽어, prototype을 만들기 전에 anchor를 보정하는 zero-shot anomaly detection 방법(CEAR).

**핵심 기여**: zero-shot anomaly detection에서 미세 결함을 국소화하려면 문맥 표현과 국소 증거를 함께 담은 기준(reference)이 필요하다는 문제의식이다. frozen MoonViT-SO-400M(672×672 입력, 48×48 grid)의 선택 층 patch 특징에서 spatial anchor를 읽고, 정상/이상 라벨·마스크 없이 Real-IAD 30개 제품 카테고리 인식으로 미세조정한 frozen ConvNeXt V2-Base가 만든 이미지별 메모리(7,056 token, 1,152차원)를 cross-attention으로 질의해 residual로 보정한 뒤, 이미지 조건 normal/anomalous query로 anchor를 gating해 prototype을 만든다(MVTec AD와 VisA가 보조/대상 도메인을 번갈아 맡고, 대상 카테고리의 정상 참조 이미지는 쓰지 않음). 13개 산업·의료 데이터셋의 68개 평가 중 57개, pixel-level 44개 비교 중 41개에서 가장 높고 11개 localization 데이터셋 평균 pixel F1-max +4.45·AP +3.79 point이며, MVTec AD pixel AUROC/F1-max/AP는 91.2/46.3/45.0(VisualAD 90.8/43.9/41.2)이지만 MVTec AD image F1-max·AP와 VisA pixel PRO는 VisualAD가 더 높다. 한계로 공유 메모리가 추가 연산을 만든다고 밝히며, 파라미터 수·추론 시간 수치는 제시하지 않는다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, defect-detection, zero-shot

---

### [RADIOlogy: A Single-Pass Approach to Training-Free Zero-Shot Anomaly Detection](https://arxiv.org/abs/2610.40580)

**한 줄 요약**: C-RADIOv4의 multi-head attention pooling(MAP) 헤드가 patch 단위로 텍스트와 정렬된다는 성질을 이용해, 학습 없이 한 번의 forward로 이상을 탐지·국소화하는 zero-shot anomaly detection 방법.

**핵심 기여**: 기존 zero-shot anomaly detection은 CLIP [CLS]·patch pooling의 약한 국소 정렬을 메우려고 보조 데이터셋 마스크로 prompt를 학습하거나 sliding window를 여러 번 돌린다는 문제의식이다. SigLIP2-g·DINOv3·SAM3를 증류한 C-RADIOv4-h(ViT-H/16)의 MAP 전역 임베딩과 patch 특징을 WinCLIP 22개 템플릿 기반 정상/이상 텍스트 앵커와 비교해 두 유사도의 차이(margin)로 점수를 매기고, 문맥 풀링·RADIO 특징 affinity 확산·SAM3 정렬 특징의 spherical k-means 부품 풀링을 평균하고 테두리 색 Otsu 임계와 어휘 게이트로 전경을 가려 pixel map을 다듬으며, 의료 영상에는 상태 어휘만 임상 용어로 바꾼다. 산업 데이터셋 평균 image AUROC 92.6(FADE 80.5·WinCLIP 79.9), pixel AUROC 95.2(FADE·DIVAD 91.7), 의료 데이터셋 평균 image AUROC 97.3·pixel AUROC 87.3이고, H100에서 CLIP baseline을 제외한 비교 방법보다 최소 2배 빠르다(MPDD AP는 CLIP baseline이 근소하게 높음). 한계로 배경이 테두리에 있다는 전경 가정이 테두리에 닿는 객체에서 깨질 수 있고, 탐지와 국소화 성능 사이에 격차가 남는다고 밝힌다.

**코드**: 공개([jacomof/RADIOlogy](https://github.com/jacomof/RADIOlogy) · Apache-2.0, 실행 시 받는 RADIO 모델은 NVIDIA 별도 라이선스)

**태그**: anomaly-detection, industrial-inspection, training-free, foundation-model

---

### [Uncertainty-aware Feedback Loop Diagnosis: integrating reinforcement learning and conformal prediction for reliable wafer defect classification](https://arxiv.org/abs/2610.40421)

**한 줄 요약**: wafer map을 patch 단위로 순차 스캔하면서 RL policy가 다음 patch를 고르고, conformal prediction 임계로 스캔 중단 시점을 정하는 결함 분류 방법(UFLD).

**핵심 기여**: CNN 기반 wafer 결함 분류는 표면 전체 스캔이 필요해 고처리량 검사를 막고, 기존 적응형 획득 방법(SupConWI-RL)은 중단 판단에 별도 confidence estimator 망을 둔다는 문제의식이다. 52×52 wafer map을 4×4 patch 169개로 나누고, 위치·순서 embedding을 더한 causal Transformer가 획득한 patch만으로 multi-label 결함을 예측하며, PPO policy가 다음 patch를 고르고, 라벨별 positive/negative conformal 임계(최종 스텝 기준 → 학습된 policy의 실제 중단 시점 기준의 두 단계 calibration)로 모든 라벨의 prediction set 크기가 1이 되면 멈춘다. MixedWM38(약 38,000장)에서 단일 UFLD-large는 patch 61.4%만 보고 정확도 97.88%(단일 SupConWI-RL 95.58%·59.3%, 전체 스캔 ResNet-34 98.79%)이고, 끝까지 확신이 서지 않는 wafer를 CNN에 넘기는 hybrid 설정에서는 98.38%이며, 미포함률 α를 0.05→0.1로 올리면 스캔 비율(56.3→70.1%)과 정확도(97.72→98.03%)가 함께 오르고 coverage는 97.34→93.34%로 내려간다. 한계로 refined 임계를 중단 규칙에 다시 쓰면 split conformal의 유한 표본 coverage 보장이 정확히 성립하지 않는다고 밝힌다.

**코드**: 공개([adekhovich/UFLD](https://github.com/adekhovich/UFLD) · MIT), MixedWM38 데이터와 hybrid용 ResNet-34 가중치는 미포함

**태그**: industrial-inspection, defect-detection, calibration, conformal-prediction, efficient-inference

---

### [FYC: FPR-Disparity Weight Perturbation and Youden Calibration for Fair Deepfake Detection](https://arxiv.org/abs/2610.37882)

**한 줄 요약**: 학습된 deepfake 탐지기의 가중치를 real 이미지 FPR 격차 기준으로 섭동한 뒤, 인구집단별 Youden 임계를 따로 정하는 2단계 사후(post-hoc) 공정성 보정법.

**핵심 기여**: deepfake 탐지기는 전체 정확도가 높아도 성별·피부색 집단 간 FPR이 두 자릿수로 차이 나는데, 기존 해결책은 전면 재학습이나 인구통계 주석이 달린 학습 데이터를 요구한다는 문제의식이다. 1단계는 SAM 방식으로 가중치를 ρ=0.05만큼 상승 방향으로 섭동한 뒤, 그룹 가중 BCE에 real(y=0) 이미지만으로 계산한 그룹 평균 예측 확률의 최대-최소 차(FPR-disparity) 패널티를 더해 15 epoch 갱신하고(단일 A100에서 구조당 약 10~15시간), 2단계는 학습셋에서 떼어낸 50K장 보정 데이터로 그룹별 TPR−FPR을 최대화하는 임계를 구해 logit 이동으로 적용한다. AI-Face v2(테스트 329,309장, 성별 × 피부색 6개 교차 그룹)에서 Xception·EfficientNet-B4·DAG-FDD·PG-FDD 네 구조 모두 FMEO·FPR·AUC가 함께 좋아지고(예: DAG-FDD FMEO 12.18→3.65, FPR 14.84→1.26%, AUC 98.77→99.92) 21개 공정성·성능 지표 중 18개에서 벤치마크의 12개 탐지기보다 앞서며, 기존 Demographic Parity 기준으로 섭동하면 PG-FDD가 크게 나빠지는 등 구조마다 결과가 엇갈렸다고 보고한다. 한계로 그룹별 보정에 인구통계 라벨이 필요하고, 일부 seed에서 특정 그룹(M-Light)의 FPR이 보정 후 오히려 오르며, ρ 민감도 분석은 남은 과제라고 밝힌다.

**코드**: 불명 (본문에 코드 공개 언급은 있으나 URL 미기재)

**태그**: forgery-detection, calibration, fairness, post-hoc

---

### [PairCLIP-SWA: Similarity-Guided Balancing and Stochastic Weight Averaging for Generalized Deepfake Image Detection with OpenCLIP](https://arxiv.org/abs/2610.37874)

**한 줄 요약**: OpenCLIP ViT-L/14를 점진적으로 unfreeze해 미세조정하고 학습 궤적을 SWA로 평균한 단일 backbone deepfake 이미지 탐지기와, validation 기준 checkpoint 선택의 불안정성 분석.

**핵심 기여**: deepfake 탐지기는 보통 validation 최고 checkpoint 하나로 배포되지만 그 선택이 얼마나 믿을 만한지는 거의 측정되지 않는다는 문제의식이다. 각 real 이미지에 CLIP 공간에서 가장 가까운 미사용 fake를 1:1로 짝지은 균형 corpus(42,690쌍)에서 학습 블록 수를 epoch마다 늘리며(2→11블록) 미세조정하고 epoch 13~19의 가중치를 평균한다. DF-Wild-Cup에서 정확도 97.04%·AUROC 98.64%·EER 4.07%로 3-backbone ensemble CAE-Net(94.46%·97.60%·5.00%)보다 높고, OpenForensics 기반 실험에서는 validation 정확도로 고른 checkpoint(98.43%)가 별도 테스트 10,905장에서 88.85%로 떨어지며 real 사진의 21.1%를 거부한 반면 validation 순위가 꼴찌였던 최종 평균은 94.76%였고, 22개 구성 비교에서 정확도는 ensemble보다 CLIP 사전학습이 좌우하며(ImageNet CNN 71.70~75.79% vs OpenCLIP 93.36~97.04%) FFT 입력은 49.61%로 chance 수준이었다. 논문은 early stopping에 쓰지 않은 분할에서 balanced accuracy·MCC 같은 클래스별 기준으로 고를 것을 권고하며, 한계로 단일 seed, DF-Wild-Cup 수치가 선택·임계 조정에 쓴 분할의 값이라는 점, 적대적 평가 부재, 304M 파라미터·약 81 GMACs의 크기를 든다.

**코드**: 불명

**태그**: forgery-detection, foundation-model, model-selection

---

### [Venus-DefakerOne2: A Vision-Forensics Foundation Model with Broader Coverage](https://arxiv.org/abs/2610.37918)

**한 줄 요약**: 디지털 조작과 물리적 spoofing, 이미지와 영상을 한 모델로 판별하는 Qwen3.5-2B 기반 vision-forensics foundation model.

**핵심 기여**: 실제 위조는 디지털 조작뿐 아니라 물리적 spoofing으로도, 이미지뿐 아니라 영상으로도 나타나는데 이를 아우르는 단일 anti-forgery foundation model이 없다는 문제의식이다. Qwen3.5-2B MLLM에 픽셀 국소화용 보조 encoder(DINOv3-Large 기반 Anomaly Magnifier, LoRA)를 붙여 공개·자체 합성·수작업 주석 온라인 공격 샘플 약 5천만 개(AI 생성 이미지 약 16M, deepfake 약 24.4M, 문서 변조 약 3.3M 등 9개 영역)로 학습하며, LoRA만 학습 → LoRA 병합 후 전체 파라미터 학습 → 새 LoRA로 어려운·신규 샘플 학습을 교대하는 Tide-Style-Tuning과, 영상을 비디오·프레임 두 방식으로 예측해 엔트로피가 낮은 쪽을 고르는 Entropy-based Test Adaptation을 쓴다. 초록 기준 deepfake 얼굴 96.7%(AUC), AI 생성 이미지 93.3%, 문서 변조 87.6%(DTD 대비 +28.5), 자연 이미지 조작 89.6%, AI 생성 영상 96.0%이고 탐지 53개 중 40개, 국소화 14개 중 11개 벤치마크에서 최고라고 보고하며, 물리 위조는 초록이 93.1%로 적지만 본문 표의 이미지 영역 값(CASIA-FASD·DLC2021·SCVD 평균 정확도)은 87.2%(이전 DefakerOne 50.7%)다. 학습 데이터의 상당 부분은 공개되지 않은 저자 측 자체(in-house) 데이터다.

**코드**: 공개([inclusionAI/DefakerOne2](https://github.com/inclusionAI/DefakerOne2) · README상 Apache-2.0, 저장소에는 점수 변환 스크립트만 있음), 가중치는 [ModelScope](https://www.modelscope.cn/models/DanceText/DefakerOne2)에 공개(모델 카드 조건), RRVBench는 비상업 연구용

**태그**: forgery-detection, foundation-model, vlm, face-anti-spoofing

---

### [CASE: Concept-Aware Segmentation from Positive and Negative Visual Exemplars](https://arxiv.org/abs/2610.39396)

**한 줄 요약**: positive·negative visual exemplar(박스)로 대상 개념을 지정하는 few-shot segmentation 설정(SVPS)과 COCO·PACO 기반 벤치마크 CASE, SAM 3용 LoRA 적응 baseline(CPA).

**핵심 기여**: positive 예시만으로는 '빨간 차'나 '차를 뺀 탈것' 같은 요청이 모호하므로, 포함 근거(positive)와 배제 제약(negative)을 함께 줘야 한다는 문제의식이다. COCO(카테고리)·PACO(속성) 주석으로 exclusion·isolation·union과 그 속성판 3종 등 6개 task family, 개념 406개, 학습 후보 episode 461,390개·고정 평가 episode 23,216개를 만들고, support·query 이미지를 1008×1008 canvas 하나에 합쳐 박스로 SAM 3에 프롬프트한다. frozen SAM 3는 negative 박스를 더하면 1-shot mIoU가 30.61→18.62로 오히려 떨어지며, encoder·decoder에 LoRA(rank 16, 학습 파라미터 약 1.13M)를 넣고 positive-only 조건에서는 원본 SAM 3 출력을 보존하는 손실을 둔 CPA는 positive+negative 1-shot 35.83·5-shot 42.15이고, COCO-20i positive-only에서 1-shot 61.6(FSS-SAM3 66.6)·5-shot 74.8(71.8)이다(보존 손실을 빼면 CASE는 37.9로 오르지만 COCO-20i 1-shot이 50.8로 떨어짐). 한계로 미묘한 색·재질 속성과 여러 카테고리에 걸친 속성 union이 어렵고, 벤치마크가 COCO·PACO의 카테고리·마스크·속성에 묶인다고 밝힌다.

**코드**: 공개([WongKinYiu/FSS-CASE](https://github.com/WongKinYiu/FSS-CASE)), 저장소 자체 라이선스 파일 없음(포함된 SAM 3 코드는 원 라이선스), CASE 데이터는 릴리스로 별도 배포하고 SAM 3 가중치와 COCO·PACO 이미지는 미포함

**태그**: segmentation, foundation-model, peft, dataset-benchmark

---

### [Parametric Gaussian Noise Mixer (PGNM): Unified Synthesis of Camera Noise and Film Grain](https://arxiv.org/abs/2610.39868)

**한 줄 요약**: 깨끗한-노이즈 이미지 쌍에서 직접 맞춘 명시적 통계 모델로 카메라 노이즈와 film grain을 한 정식화로 합성하는 Parametric Gaussian Noise Mixer.

**핵심 기여**: 노이즈 합성은 보통 영상 형성의 물리 모델이나 노이즈 이미지를 생성하는 신경망으로 접근하는데, 그 중간 지점으로 쌍 데이터에서 직접 맞춘 명시적 통계 모델을 탐구한다는 문제의식이다. normalized convolution으로 표준 Gaussian field를 픽셀·색 채널 사이에 상관시키고, lookup이 각 Gaussian 값을 clean 강도에 따른 residual로 매핑하며, field가 표준 Gaussian으로 유지되므로 두 구성 요소를 따로 맞춘다(물리 과정 재현이나 신경 생성기 학습 없음). SIDD 카메라 노이즈와 Newson 방식으로 시뮬레이션한 film grain에 같은 정식화를 적용해 SIDD에서 평가한 방법 중 평균 분포·상관 오차가 가장 낮고 film grain에서도 비교 방법과 대등하며, 이 노이즈로 학습한 denoiser가 real noise로 학습한 denoiser에 가장 가깝고, GPU에서 1080p 프레임 하나를 10ms에 렌더링한다고 보고한다.

**코드**: 불명

**태그**: sim2real, noise-synthesis, camera-isp

---

### [You Don't Need Aligned Representations: Knowledge Distillation via Random Prototype Spaces](https://arxiv.org/abs/2610.37937)

**한 줄 요약**: teacher와 student를 공유된 고정 random prototype bank에 비춰 비교함으로써, 두 특징 공간을 직접 정렬하지 않고 이종 구조 사이에서 knowledge distillation을 하는 방법(RPKD).

**핵심 기여**: knowledge distillation은 teacher·student 표현이 호환되거나 명시적으로 정렬돼야 한다고 가정해 왔다는 문제의식이다. 표준 Gaussian에서 뽑아 L2 정규화·고정한 prototype 500개(256차원)에 teacher는 학습 파라미터 없는 고정 random projection으로, student는 학습되는 2층 MLP projector로 사상한 뒤, prototype cosine 유사도 분포를 온도 KL(T=4)로 맞추는 logit branch와 7×7 prototype activation map을 cosine loss로 맞추는 feature branch를 둔다. CIFAR-100 ConvNeXt-T→DeiT-T 83.74%(OFA 75.76%), ImageNet-100 ResNet50→DeiT-T 81.00%(OFA 68.56%), ImageNet-1K DeiT-T→MobileNetV2 72.67%(OFA 71.39%)이고, 클래스 10개짜리 ImageNet 부분집합(DeiT-T→ResNet18)에서는 95.40%로 OFA 92.60%·scratch 90.80%보다 높은 반면 logit 기반 KD·CRD는 scratch보다 낮았다. 한계로 loss 계수에 grid search가 필요하고, ImageNet-1K는 CNN student 4쌍만 평가했으며, 분류 외 과제는 시험하지 않았고 MLP-Mixer teacher에서 성능이 떨어진다고 밝힌다.

**코드**: 공개([HamzaEtcibasi/RPKD](https://github.com/HamzaEtcibasi/RPKD) · MIT), teacher checkpoint는 OFA 배포본(비상업 연구용)

**태그**: distillation, efficient-inference, heterogeneous-architecture

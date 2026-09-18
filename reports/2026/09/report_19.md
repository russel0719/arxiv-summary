# arXiv cs.CV Daily Digest — 2026-09-18 (arXiv 공개일)

- **전체 신규 논문 수**: 125편 (new 101 + cross-list 24)
- **선별 수**: 11편

## 오늘의 트렌드

Gaussian Splatting·SLAM 등 3D 복원, 멀티모달 LLM의 세밀 지각·추론 벤치마크, 의료 영상 분할·진단, 로봇·자율주행 embodied 인지가 두꺼운 군집을 이룬다. 방법론으로는 backbone을 동결한 채 어댑터·라우터·선택기만 얹어 적응하는 설계, 대형 foundation model을 소형 학생으로 증류하고 양자화해 엣지에 올리는 배포 최적화, 그리고 held-out 데이터로 보정한 임계값으로 적용 여부를 사례 단위로 결정하는 캘리브레이션 절차가 반복된다.

---

### [Automated Goldsmith's Mark Retrieval in Silverware](https://arxiv.org/abs/2609.20509)

**한 줄 요약**: 은세공품의 각인(goldsmith mark) 검색을 각인 지역화와 metric learning 미세조정의 조합으로 풀고, 백본 세 종과 크롭 전략 세 가지의 상호작용을 체계적으로 비교한 파이프라인.

**핵심 기여**: 미술사 전문가가 유물 식별·연대 추정을 위해 질의 각인을 수백 개의 문헌 예시와 수작업으로 대조해야 하고, 이 과정이 지루하며 전문 지식 의존도가 높다는 점을 문제로 삼는다. 제안 파이프라인은 각인 지역화와 metric learning 미세조정을 결합하고, ImageNet 사전학습 ResNet-50·지도학습 ViT-S/16·자기지도 DINOv2 ViT-S/14 세 백본에 대해 크롭 없음·수동 정답 크롭·학습된 검출 기반 크롭을 교차 평가한다. 가장 강한 구성인 DINOv2 ViT-S/14 + 수동 크롭 + metric learning 미세조정이 mAP 62.63%, Top-1 정확도 73.74%를 얻는다. 자기지도 사전학습과 각인 지역화가 가장 영향이 큰 두 요인이며, 학습된 크롭이 추론 시 정답 주석 없이도 수동 크롭 이득의 대부분을 회복한다고 보고한다.

**코드**: 공개(초록에 URL 미명시 · 수동 주석 데이터셋과 코드베이스 공개, 공개 웹 인터페이스 배포)

**태그**: ssl-backbone, image-retrieval, metric-learning, fine-grained, object-detection

---

### [SCOUT: Sim-to-Real Text-Based Person Retrieval by Embedding-Space Prediction over Frozen Video Features](https://arxiv.org/abs/2609.19483)

**한 줄 요약**: 동결된 비디오 인코더의 patch token을 동결 텍스트 인코더의 임베딩 공간으로 사상하는 predictor만 학습해, 합성 학습 데이터와 실사 갤러리 사이의 sim-to-real 격차 아래 텍스트 기반 인물 검색을 수행하는 시스템.

**핵심 기여**: sim-to-real 격차가 있는 텍스트 기반 인물 검색은 보통 비싼 cross-encoder 미세조정으로 다뤄지는데, 동결 인코더 시스템이 이에 견줄 수 있는지 묻는다. SCOUT은 cross-modal 검색을 임베딩 공간에서의 예측으로 정식화해, V-JEPA 비디오 인코더와 EmbeddingGemma 텍스트 인코더를 모두 동결한 채 Qwen3.5-0.8B 디코더로 초기화한 predictor만 양방향 InfoNCE로 학습한다. 최적의 동결 텍스트 인코더는 비디오 특징과 기하가 가장 잘 맞는 것이며, 학습 없는 정렬 점수가 후보 세 종의 검색 정확도 순위를 그대로 재현하지만(Spearman ρ=1.0) LLM 기반 인코더에서는 지표 의존적임을 보인다(neighborhood-overlap ρ=0.8, linear probe ρ=-0.2). 비디오 인코더의 ExPLoRA 적응과 학습 없는 속성 분해 reranker가 leaderboard R@1을 2.2점 더하며, AI City Challenge 2026 Track 4에서 retrieve-fuse-rerank 전체 시스템이 84.25 mAP@10, 단일 동결 모델 단독 제출이 60.63을 기록한다. 학습된 구성요소의 비용은 약 95 GPU-hour다.

**코드**: 공개([SCOUT-ECCV](https://github.com/abtraore/SCOUT-ECCV))

**태그**: image-retrieval, image-embedding, sim2real, peft, re-identification

---

### [Queries Knew More Than We Thought: Uncovering Latent Knowledge in Segmentation Models](https://arxiv.org/abs/2609.20283)

**한 줄 요약**: 동결된 DETR 계열 분할 모델이 이미 계산해 놓고도 노출하지 않는 마스크 후보 중에서, 보정된 margin이 충분할 때만 기본 선택을 바꾸는 경량 선택기 HYDRA.

**핵심 기여**: 분할 모델은 비싼 연산이 끝난 뒤에 실패하는 경우가 많다 — 쓸 만한 마스크가 query-conditioned 후보 안에 있는데 배포된 선택 규칙이 그것을 드러내지 못한다는 output-selection 병목을 지적하고, 정답만 보는 oracle로 이미 계산된 마스크 제안 안에 상당한 잠재 여유가 있음을 먼저 보인다. HYDRA는 동결 모델의 캐시된 출력만으로 학습되는 작은 선택기로, 추론 시 후보들을 명시적인 keep-baseline 선택지와 함께 점수화하고 held-out 데이터로 보정한 margin이 선택 후보가 충분히 낫다고 할 때만 개입하며, query 추가·새 마스크 생성·backbone 재실행·가중치 갱신을 요구하지 않는다. ADE20k와 COCO에서 Mask2Former·MaskDINO·OneFormer를 최대 +7.41 mIoU 개선하고, SAM 3를 8개 도메인 평균 +9.4 class-macro prompt-IoU 개선한다. 짝지은 LoRA 대조군은 병목을 제거하지 못해 노출된 예측이 평탄하거나 더 나빠지는 반면 적응된 후보 위에서의 라우팅은 여전히 정확도를 회복하며, 이 효과를 bipartite matching 하의 query 특화와 연결해 TinyDETR 통제 실험으로 검증한다.

**코드**: 불명

**태그**: segmentation, calibration, foundation-model, open-vocab-detection

---

### [Not All Layers Are Equal: Dynamic Layer Routing for Reliable CLIP OOD Detection](https://arxiv.org/abs/2609.20299)

**한 줄 요약**: 층별 정보를 어떻게 융합할지 대신 입력마다 어떤 층을 신뢰할지를 학습 문제로 바꿔, CLIP의 깊이에 걸쳐 최종층에 고정된 희소 전문가를 고르는 경량 라우터 기반 OOD 탐지.

**핵심 기여**: 층 간 정보 집계가 OOD 탐지를 개선한다는 최근 결과에서 출발하되, 층별 융합 기법을 새로 설계하는 대신 층 선택 자체가 학습 가능한 문제인지를 묻는다. 기존 최신 기법의 기제보다 효과적인 것으로 제시된 일반화 가능한 weak OOD context 생성으로 지도 신호를 만들고, CLIP의 층 깊이 위에서 final-layer-anchored 희소 전문가를 고르는 경량 라우터를 학습하는 방식(Voyager)을 정식화한다. 서로 다른 세 벤치마크에서 개선을 보이며 ImageNet-1K 평균 FPR@95가 18.86으로, 비교 가능한 가장 강한 prompt-learning 방법보다 8.8점 낮다. 기존 최신 prompt-learning 기법이 쓰는 것을 포함해 여러 지도 신호 출처에서도 이득이 유지돼 핵심 이점이 지도 출처가 아니라 학습형 라우터에서 온다고 결론짓고, 라우터 학습이 1GB 미만 메모리로 약 2분 걸려 기존 prompt-learning 대비 약 20배 효율적이라고 보고한다.

**코드**: 공개([익명 저장소](https://anonymous.4open.science/r/Voyager/))

**태그**: calibration, anomaly-detection, foundation-model, efficient-inference

---

### [Should This Case Be Adapted? Prediction Fragmentation Controls Test-Time Adaptation](https://arxiv.org/abs/2609.20700)

**한 줄 요약**: 원본 모델과 적응된 마스크 사이의 불일치 기하만으로, 라벨이나 추가 역전파 없이 이 사례를 test-time adaptation에 넘길지 사례 단위로 결정하는 라우터.

**핵심 기여**: 사례마다 동결 분할기를 원본 가중치로 되돌린 뒤 고정 step 수만큼 적응하는 방식은 "얼마나 적응할지"라는 코호트 수준 질문과 "이 사례를 적응시켜야 하는지"라는 환원 불가능한 사례별 질문을 뒤섞고, 코호트 평균이 그 결정을 가린다 — cross-vendor 심장 MRI에서 평균 ΔDice는 0과 통계적으로 구분되지 않는데도 58.7%의 사례가 개별적으로는 나빠진다. 이 피해를 컨트롤러가 편집한 영역 중 해로운 비율(harmful accepted area, HA)로 정량화하고, 원본 M0와 적응 마스크 Mk의 불일치 기하인 prediction fragmentation이 결정 시점에 라벨·추가 역전파 없이 HA를 예측함을 세 벤치마크에서 보인다(Spearman ρ 0.50–0.60, gradient-norm의 1/4 지연). 설계에 관여하지 않은 벤치마크에서 설계를 고정한 채 cut-point만 재보정해 HA를 0.228에서 0.139로 낮추고, 설계를 고른 심장 벤치마크에서는 동일 Dice·1.10회 갱신에서 0.129를 0.013으로, 58.7%를 20.0%로 줄인다. 유지된 사례가 순이득이 아닌 prostate에서는 HA는 줄지만 정확도를 양보한다는 경계를 함께 보고하며, nnU-Net→SegFormer·Cityscapes→ACDC로 구조·도메인 이식성을 확인한다.

**코드**: 불명

**태그**: calibration, segmentation, test-time-adaptation

---

### [AI or Real: Detecting Partially Altered Videos Under Resource-Constrained Environments](https://arxiv.org/abs/2609.20263)

**한 줄 요약**: DINOv2-Base 교사를 동결 MobileNetV3-Small 학생으로 증류해, 얼굴 검출 전처리 없이 전체 프레임만으로 부분 조작된 AI 생성 영상을 엣지에서 판별하는 경량 검출기.

**핵심 기여**: 생성 영상 모델이 퍼지면서 실질적 탐지 대상이 완전 조작 클립에서 부분 조작 영상으로 옮겨갔지만, 400M 이상 파라미터의 foundation backbone을 쓰는 최신 검출기는 자원 footprint 때문에 엣지 배포가 불가능하다는 점을 문제로 삼는다. 제안 시스템은 temperature-annealed soft-label 전달, attention-diversity 정규화, 프레임 단위 지도, ImageNet 특징을 아티팩트 탐지용으로 조건화하는 residual feature adapter를 결합한 파이프라인으로 교사를 증류한다. 부분 조작 특유의 두 실패 모드도 표적으로 삼아, 정상적인 장면 전환에서의 오탐은 영상 내부 temporal hard negative로, 지배적인 순수 실사 클래스에서의 임계값 오보정은 calibration-aware sampling으로 다룬다. fake-frame 비율 6.2~31.2%에 걸친 55,393 샘플 spliced 테스트셋에서 학생 모델이 DINOv2-Base 교사(AUC 0.766)와의 격차를 58% 좁히면서 RTX A4000에서 16프레임 클립당 3.65ms로 동작하고, 체크포인트는 150.4MB다.

**코드**: 불명

**태그**: forgery-detection, distillation, ssl-backbone, efficient-inference, calibration

---

### [Compact Vision Models for Iris Presentation Attack Detection under Presentation Attack Instrument Shift and Environmental Degradation](https://arxiv.org/abs/2609.20386)

**한 줄 요약**: 파라미터 0.26M 이하의 scratch 학습 소형 모델 세 종을 미지의 제시공격 도구와 환경 열화 아래 벤치마크하고, 검증셋에서 고른 임계값을 그대로 옮겼을 때의 오류 증가를 정량화한 연구.

**핵심 기여**: 홍채 presentation attack detection은 개발 단계에서 신뢰할 만해 보이던 서브시스템이 검증 데이터에 없던 제시공격 도구(PAI)나 촬영 조건을 만나는 상황에서 보안상 결정적이라는 점에서 출발한다. LivDet-Iris 2017의 Notre Dame 부분집합에서 외부 사전학습과 데이터 증강 없이 다섯 개 시드로 세 모델을 학습하고, 검증셋에서 선택한 임계값을 known-attack·unknown-attack·corrupted·pooled 분할에 변경 없이 전이해 평가한다. known에서 unknown 공격 제시로 넘어갈 때 APCER는 17.11~30.47%p, Detection EER은 7.38~12.73%p 증가하며, 검증셋 선택 임계값에서 ZACH-ViT가 unknown-attack APCER 47.69±4.84%와 D-EER 38.87±0.93%로 가장 낮고 Compact-TransMIL이 BPCER가 가장 낮다. 논문은 절대 오류가 높아 최고 소형 모델의 상대적 우위가 미지 PAI 하에서의 배포 준비를 뜻하지는 않는다고 명시한다.

**코드**: 불명

**태그**: forgery-detection, calibration, efficient-inference, dataset-benchmark

---

### [Earth Surface Immune System for Rapid Monitoring of Unknown Anomalies](https://arxiv.org/abs/2609.20662)

**한 줄 요약**: 시계열 위성영상에서 범주를 가정하지 않고 이상을 국소화한 뒤, 걸러낸 텍스트 프롬프트를 국소 패치와 매칭해 미지 이상의 범주·면적·심각도까지 개방 어휘로 인식하는 2단계 구조.

**핵심 기여**: 지표 이상은 역사적 데이터가 적고 예측 불가능해 통상적인 원격탐사 대상과 근본적으로 다른데, 기존 방법은 특정 이상 범주에 국한되거나 국소화에서 멈춰 탐지와 실행 가능한 정보 사이에 간극이 남는다는 점을 문제로 삼는다. ESIA는 생물 면역계의 세 원리를 구조적 제약으로 삼아, 비특이적 innate 단계가 이상을 시계열 위성영상의 미관측 변화로 취급해 범주 가정 없이 14.51 km²/s로 이진 국소화 맵을 만들고, 특이적 adaptive 단계가 negative selection으로 텍스트 프롬프트를 거른 뒤 살아남은 프롬프트를 멀티모달 foundation model로 국소 패치와 매칭한다. 테스트 시 최소한의 임베딩만 조정하는 mutation 기제가 참조 이미지 쌍 하나로 3.26초 만에 장면에 적응한다. 6개 이상 범주·19,801.60 km²의 전역 데이터셋에서 22개 모델과 비교해 국소화 F1이 가장 강한 일반 baseline보다 37% 높고 인식 F1은 80%를 넘으며, Kakhovka 댐 붕괴 후 농지 훼손 정량화와 2025 Palisades Fire 연소 심각도 평가에 적용된다.

**코드**: 불명

**태그**: anomaly-detection, open-vocab-detection, foundation-model, segmentation

---

### [Enhanced Knowledge Distillation for Detection Transformer via Teacher Prediction Refinement](https://arxiv.org/abs/2609.19964)

**한 줄 요약**: DETR 증류에서 정렬 지점 대신 교사 지도 자체의 품질을 문제 삼아, 단계별 예측 정보를 이용해 열화된 양성 예측을 복원하고 과신된 음성 예측을 억제한 뒤 증류하는 plug-and-play 모듈.

**핵심 기여**: DETR는 검출 성능이 강하지만 연산 비용 때문에 엣지 배포가 어렵고, 기존 DETR 증류 기법은 증류 지점 정렬에 집중하면서 교사 지도의 품질은 대체로 간과한다는 점을 지적한다. DETR의 단계별 비단조 예측 거동 탓에 앞 단계에서 잘 지역화·분류된 예측이 뒤 단계에서 나빠지고 일부 음성 예측은 점점 과신되어, 현재 단계 예측만 쓰면 부정확하고 일관성 없는 지도가 된다는 관찰이 근거다. TPRD는 앞 단계의 더 정확한 예측을 되살려 지역화·분류 신호를 신뢰할 수 있게 만드는 Positive Prediction Correction, 과신된 음성 예측의 영향을 억제하는 Negative Prediction Suppression, 비목표 클래스 관계를 유지한 채 목표 클래스 logit만 선택적으로 다듬어 dark knowledge를 보존하는 Maximum Dark Knowledge Preservation으로 교사 예측을 증류 전에 정제한다. MS COCO와 PASCAL VOC 실험으로 효과와 강건성을 보고한다.

**코드**: 공개([TPRD](https://github.com/xingyitong1/TPRD))

**태그**: distillation, object-detection, efficient-inference

---

### [A Smaller Transformer in Your Transformer](https://arxiv.org/abs/2609.20100)

**한 줄 요약**: ViT가 국소적으로 유사한 계산 단계에 안착한다는 관찰을 블록 중복성의 통일된 관점으로 정식화하고, 인접한 중복 층 묶음을 학습된 대리 층 하나로 사후 융합하는 압축 기법.

**핵심 기여**: Vision Transformer가 국소적으로 유사한 계산 단계에 자리 잡아 깊이 방향 계산 중복이 존재한다는 최근 발견에도, 이를 이용하려는 기존 방법은 추론 연산을 실제로 줄이지 못하거나 모델 표현력을 심하게 훼손한다는 점을 문제로 삼는다. 이 논문은 특정 대리 개입에서 기하를 분리하는 블록 중복성의 통일된 관점을 세우고, 연속된 중복 층 그룹을 학습된 대리 층 하나로 융합하는 사후 기법 Transformer-Within-Transformer(TWT)를 제시한다. TWT는 파라미터 수와 추론 연산을 함께 줄이면서 자연 이미지에서 원본 깊이의 절반으로도 원 모델과 경쟁력을 유지하고, 여러 histopathology 다운스트림 설정에서는 원 baseline과 같거나 더 나은 성능을 보인다고 보고한다.

**코드**: 불명

**태그**: efficient-inference, foundation-model, distillation

---

### [Distance to Class Prototypes: Active Learning for Object Detection](https://arxiv.org/abs/2609.20248)

**한 줄 요약**: supervised contrastive 항으로 거리가 클래스 소속을 표현하는 객체 단위 임베딩 공간을 만들고, 예측 범주가 차지한 영역으로부터의 거리에 신뢰도를 가중해 라벨링할 이미지를 고르는 단일 forward pass 획득 기준.

**핵심 기여**: 새 환경에 검출기를 배포할 때의 제약은 구조보다 주석 비용이며, 능동학습의 성능은 라벨 없는 이미지를 채점하는 신호의 품질에 달려 있다 — 통상 쓰이는 클래스 posterior는 값이 싸지만 보정이 나쁘고, 여러 모델·확률적 패스 간 불일치는 더 낫지만 라벨셋보다 훨씬 큰 pool 위에서 추론을 여러 배로 늘린다는 점을 문제로 삼는다. 제안 기준은 학습 목적에 supervised contrastive 항을 더해 거리가 클래스 소속을 인코딩하는 객체 단위 임베딩 공간을 형성하고, 라벨 없는 검출을 예측 범주 영역으로부터의 거리에 신뢰도를 곱해 점수화하며, 앙상블·보조 예측기·반복 추론 없이 총 2.89M 파라미터(맨 검출기 대비 8.3% 증가)만 든다. PASCAL VOC와 MS-COCO에서 선택이 일어난 모든 라운드에서 동일 검출기의 posterior를 최대 1.08% mAP50 차로 앞서며(실행 간 편차 0.02~0.18%), 무라벨 이미지당 3~50회 forward pass를 쓰는 앙상블·Monte Carlo dropout 기준과 경쟁력을 유지한다. 선택 결정을 검출기 성능에서 분리하기 위해 비교 대상들이 결과를 보고한 단일 단계 검출기를 그대로 사용한다.

**코드**: 불명

**태그**: metric-learning, image-embedding, object-detection, calibration

# arXiv cs.CV Daily Digest — 2026-10-06 (arXiv 공개일)

- **전체 신규 논문 수**: 285편 (new 231 + cross-list 54)
- **선별 수**: 11편

## 오늘의 트렌드

비디오 생성·월드 모델과 VLA·embodied 정책이 가장 두꺼운 군집을 이루고, 3D Gaussian Splatting 기반 재구성·렌더링, 의료영상 분할·보고서 생성, VLM의 공간추론 진단과 토큰 예산 축소가 그 뒤를 잇는다. 방법론으로는 동결된 CLIP·DINOv3 특징을 추가 학습 없이 다시 읽어내는 training-free 판독, 토큰 선별·가지치기로 연산을 줄이는 효율화, 벤치마크의 포화·누출을 감사하고 평가 지표 자체를 다시 세우는 재평가 연구가 반복된다.

---

### [From Pixels, Without Pre-training: Joint Generative and Self-Supervised Representation Learning in One Model](https://arxiv.org/abs/2610.05711)

**한 줄 요약**: 레이블도 사전학습 모델도 쓰지 않고 대조학습 표현과 flow matching 생성을 단일 픽셀 공간 인코더에서 함께 학습하는 자기지도 모델 SCION.

**핵심 기여**: 강한 이미지 생성 모델은 클래스 레이블, 동결 사전학습 인코더와의 정렬, 혹은 따로 학습한 오토인코더에 기대고 있어 생성이 지도 신호나 사전학습에 종속된다는 문제의식에서 출발한다. 두 목적은 서로 어긋나는데 — 대조학습은 깨끗한 증강 뷰를 받아 거칠고 불변한 의미를 선호하는 반면 flow matching은 잡음 이미지를 받아 세부와 공간 배치를 지켜야 한다 — SCION은 flow timestep과 조건 임베딩으로 조건화된 단일 픽셀 공간 인코더 하나로 이를 묶는다. 표현학습에서는 조건 임베딩이 이미지 전체에 공유되는 학습된 전역 벡터이고 인코더의 [CLS] 토큰이 대조 손실로 학습되는 의미 표현이 되며, 생성학습에서는 조건 임베딩을 이미지 자신의 [CLS] 표현으로 바꾸고 패치 토큰이 디코더를 지나 이미지를 예측한다. 참조 이미지 없이 샘플링하기 위해 임베딩에 대한 prior를 함께 학습하고 gradient-norm 균형화와 stop-gradient로 한 번의 학습에서 공동 최적화하며, ImageNet 256×256·JiT-B 레시피에서 guidance 없이 FID 8.92로 동결 DINOv2에 정렬하는 class-unconditional iREPA(46.44)와 그에 조건화하는 RCG(14.27)를 앞서고, JiT-L에서는 guidance 없이 5.89, representation guidance 적용 시 3.47을 기록했다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, foundation-model, generative

---

### [FLASHSWIN: Unlocking Large Windows and Dense Tokens in Swin Vision Transformers with Memory Efficient Attention](https://arxiv.org/abs/2610.04664)

**한 줄 요약**: 윈도우 어텐션의 점수 행렬 구체화를 FlashAttention으로 없애고 상대 위치 바이어스를 윈도우-지역 2D RoPE로 대체해 큰 윈도우와 조밀 토큰을 함께 쓰는 Swin 백본.

**핵심 기여**: 계층적 Swin은 윈도우마다 M²×M² 점수 행렬을 만들어 O(M⁴) 메모리를 쓰고 학습형 상대 위치 바이어스를 점수에 원소별로 더하므로 행렬과 그 gradient를 전부 들고 있어야 해서, 작은 윈도우(M=8,16)와 거친 토큰(패치 4×4) 영역에 묶여 세밀한 과제에서 손해를 본다고 진단한다. FLASHSWIN은 점수 행렬을 만들지 않고 정확한 softmax 어텐션을 계산해 윈도우당 메모리를 O(M²)로 낮추고, 그 대가로 쓸 수 없게 된 위치 정보를 윈도우-지역 학습형 2D RoPE로 복원한다. 32×32 윈도우에서 FLASHSWIN-T의 학습 메모리는 12.4GB로 8×8일 때와 같은 반면 SwinV2/V1-T는 각각 70/90GB가 들며, 패치 2×2·윈도우 32에서 ImageNet-1K 84.1%, COCO box AP 44.1, ADE20K mIoU 47.28로 M=16 SwinV2-T 대비 +1.3, +5.1, +1.82를 기록했다. 윈도우를 32로 고정한 채 패치 크기를 절반으로 줄이면 mIoU보다 경계 품질에서 약 3배 큰 이득이 나타난다.

**코드**: 불명

**태그**: vision-backbone, efficient-inference, segmentation, object-detection

---

### [A Strong Baseline for Evaluating Vision Encoders in Multimodal Large Language Models](https://arxiv.org/abs/2610.05413)

**한 줄 요약**: 교차 모달 최근접 이웃 검색만으로 MLLM 안에서의 비전 인코더 downstream 성능을 예측하는 학습 불필요 평가 지표 RAVEL.

**핵심 기여**: 비전 인코더 평가에는 MLLM downstream 성능을 신뢰성 있게 예측하는 지표가 필요하고 교차 모달 지표가 이를 더 잘 포착한다는 보고가 있었음에도 실무에서는 여전히 단일 모달 지표가 지배적이라는 데서 출발한다. 대규모 실험으로 기존 교차 모달 평가 방식의 실험 설계와 방법론적 정식화에 있는 한계를 짚고, 이를 보완한 뒤 교차 모달 최근접 이웃 검색에 기반한 학습 불필요 방법 RAVEL을 제안한다. 구성은 단순하지만 실험 전반에서 기존 방법을 큰 폭으로 앞서는 성능을 기록해, 신중하고 포괄적인 설정 아래에서는 단순한 교차 모달 지표가 비전 인코더 평가의 기반이 될 수 있음을 보인다.

**코드**: 불명

**태그**: image-embedding, image-retrieval, foundation-model, vlm

---

### [From Transformation to Target State: Rethinking Query Representation for Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2610.05993)

**한 줄 요약**: composed image retrieval의 질의를 '변환 서술'이 아니라 '목표 상태 재구성'으로 다시 정식화한 학습 불필요 zero-shot 검색 프레임워크 ASAP-CIR.

**핵심 기여**: CIR은 참조 이미지와 수정 텍스트로 목표 이미지를 찾는 과제인데, 수정 텍스트는 참조 상태로부터의 전이를 기술하는 반면 검색 후보는 완료된 목표 상태를 담고 있어서 사전학습 비전-언어 공간을 변환 지향 언어로 그대로 질의하는 zero-shot 방식에는 표현 불일치가 생긴다고 진단한다. ASAP-CIR은 이를 목표 상태 재구성 후 검색으로 바꾸어, 동결 MLLM으로 정적 목표 표현을 재구성하되 복수의 전체적 서술과 중요도 가중된 가변 개수의 원자적 의미를 결합해 목표의 전체 정체성과 세밀한 시각 제약을 함께 보존하고, 검색 단계에서 전체 상태 정렬·원자 제약 접지·캘리브레이션된 목표 상태 증거 통합을 합친다. 텍스트 전용 통제 진단에서 목표 측 정적 질의가 동적 합성 질의보다 신뢰도 높은 검색을 보였고 특히 원천 상태 의미를 억제하거나 변환해야 할 때 차이가 컸으며, FashionIQ·CIRR·CIRCO 실험에서는 다중 정답 벤치마크인 CIRCO에서 이득이 가장 뚜렷했다.

**코드**: 불명

**태그**: image-retrieval, training-free, image-embedding, vlm

---

### [TRIM-ReID: Duplication-Aware Token Reduction and Modality-Aligned Interaction for Multi-Modal Object Re-Identification](https://arxiv.org/abs/2610.04361)

**한 줄 요약**: DINOv3 조밀 특징으로 정체성 단서를 보존하고 중복 토큰을 걸러 RGB·NIR·TIR 간 교차 모달 상호작용 비용을 줄인 다중 모달 객체 re-identification 프레임워크.

**핵심 기여**: 기존 다중 모달 ReID는 전역 image-text 정렬에 최적화된 비전 인코더를 쓰고 학습된 중요도 점수로 토큰을 고르기 때문에 세밀한 정체성 단서를 보존하지 못하고 토큰 중복을 명시적으로 다루지 않아, 국소 증거가 과소 표현되고 중복 토큰이 교차 모달 상호작용을 잡음 많고 비싸게 만든다고 본다. TRIM-ReID는 DINOv3를 활용해 의미가 풍부하고 공간적으로 일관된 패치 특징을 뽑는 Dense Identity Representation, 반복되는 패치를 억제하면서 상보적인 국소 증거를 남겨 모달별 compact 토큰 집합을 만드는 Token Diversity Mining, 남은 토큰을 융합하는 Modal Relational Interaction을 하나로 묶고, 독립적으로 토큰을 고르는 상황에서도 교차 모달 의미 일관성이 유지되도록 삼각 정렬 손실로 결합 관계를 정규화한다. RGBNT201·RGBNT100·MSVR310에서 state-of-the-art 성능을 보고한다.

**코드**: 불명

**태그**: re-identification, fine-grained, image-embedding, efficient-inference

---

### [JLD: Perceptual Distance Through A Jacobian Lens](https://arxiv.org/abs/2610.05967)

**한 줄 요약**: 동결 비전 인코더의 Jacobian에서 지각 기하를 끌어내 사람 라벨 없이 정의한 이미지 지각 거리 JLD.

**핵심 기여**: 픽셀 오차는 사람이 보는 방식을 반영하지 못하고 정확도가 높은 지각 거리들은 사람의 판단에 맞춰 적합돼 특정 데이터와 해상도에 묶이는데, 예컨대 해상도를 두 배로 하면 TID2013에서 DISTS와 사람 점수의 상관이 0.815에서 0.717로 떨어진다. JLD는 인코더 Jacobian으로 초기 특징 공간에서 인코더 출력에 가장 크게 영향을 주는 방향을 찾아 고정 계량 텐서 E[JᵀJ](Jacobian lens)를 만들고, 초기 패치 특징의 국소성과 후기 표현이 담은 지각 민감도를 결합해 픽셀 공간의 pullback metric으로 해석되는 거리를 정의한다. 렌즈는 라벨 없는 이미지 100장으로 약 35초에 한 번만 적합되며, 표준 지각 데이터베이스 4종에서 LPIPS·DISTS·PieAPP·DreamSim을 일관되게 앞서고 TID2013에서 해상도를 두 배로 해도 렌즈 항 상관이 0.850에서 0.845로 거의 유지된다. LPIPS-VGG보다 4배 빠른 JLD-fast는 평균 상관 0.911을 내고, 비디오로 확장하면 Waterloo IVC 4K에서 0.786(VMAF 0.611)에 이른다.

**코드**: 불명

**태그**: image-embedding, metric-learning, training-free, foundation-model

---

### [Watermarks and Fingerprints as Soft Bindings for Content Provenance: An Open-Licence Benchmark for Images, Audio and Video](https://arxiv.org/abs/2610.04151)

**한 줄 요약**: C2PA soft binding 수단인 보이지 않는 워터마크와 레지스트리 핑거프린트를 하나의 프로토콜·공개 라이선스 모델 범위에서 비교하고 오매칭률을 캘리브레이션한 벤치마크.

**핵심 기여**: C2PA 같은 콘텐츠 출처 표준은 제거된 manifest를 콘텐츠에서 읽는 워터마크나 레지스트리 조회로 찾는 핑거프린트를 통해 복원하는데, 두 계열을 같은 조건에서 견준 기준이 없었다. 라이선스를 감사한 공개 모델만으로 이미지 25·오디오 7·비디오 7 구성(12개 방법)의 워터마크를 지각 품질·강건성·오탐·비용 축에서, 핑거프린트 35종을 최대 98,985장 레지스트리와 부분 편집·적대적 공격에서 평가하며, 오매칭률은 held-out negative로 캘리브레이션하고 성능은 소스 수준 bootstrap 구간으로 보고한다. 이미지·비디오 워터마크는 PixelSeal, 오디오는 AudioSeal이 가장 균형이 좋았으나 TrustMark 계열의 오류 정정 검출기는 표시가 없는 이미지의 5.9~15.3%에서 발화해 검증자가 기대 payload를 함께 확인해야 하며, 핑거프린트에서는 비상업 데이터로 학습된 copy detector가 쌍 단위 오매칭률 10⁻⁷에서 변형 이미지의 최대 75.5%를, 허용적 라이선스 중 최선인 DINOv2가 65.0%를 검출했다. 오매칭은 상품 카탈로그 안의 near-copy가 지배했고, 캘리브레이션을 맞춘 오결합 제약 아래에서는 평가된 이미지 파이프라인에서 기하 검증에 의한 검출 개선이 관찰되지 않았다.

**코드**: 불명

**태그**: forgery-detection, image-retrieval, calibration, dataset-benchmark

---

### [Certification of Real Images through Calibrated Content Authentication](https://arxiv.org/abs/2610.05870)

**한 줄 요약**: 알려진 생성기가 그 콘텐츠를 충실히 재구성할 수 있는지를 기준으로 '진위를 그럴듯하게 부인할 수 있는가'를 캘리브레이션된 예측으로 내놓는 검출 패러다임.

**핵심 기여**: 최근 4년 사이 공개된 생성기 10종에 대해 딥페이크 검출기 20종을 평가하면 정확도가 99.5%에서 76%로 시간에 따라 떨어지고, 적대적 섭동을 더하면 모든 기준선이 2% 미만으로 무너져 검출기가 부여하는 라벨이 사실상 뒤집힌다. 저자들은 이 불안정성이 생성기가 암기 등을 통해 진짜 콘텐츠를 그대로 재현할 수 있다는 근본적 모호성에서 온다고 보고, 생성기가 만든 콘텐츠는 그 생성기에 의한 충실한 재구성을 허용해야 한다는 성질을 뒤집어, 그런 재구성을 찾으면 합성 출처가 그럴듯해지고 진위는 부인 가능해진다는 판단을 캘리브레이션해 출력한다. 생성된 콘텐츠가 잘못 인증되는 비율을 최대 1%로 묶는 작동점에서 대부분의 기준선은 재현율이 0에 가까웠고(정확도 93%인 최강 기준선 포함), 공격 샘플에 더 엄격한 보안 임계를 캘리브레이션하면 평가된 유계 섭동 공격 범위 안에서는 적응형 공격자에게도 경계가 유지되지만 임의의 적대적 변환까지 포괄하지는 않는다고 밝힌다. 사후 검증 가능성 자체가 약해지고 있어, Reddit 이미지 3,000장 중 1,116장이 2022년 생성기의 재현에 저항한 반면 2024년 생성기에 저항한 것은 55~79장뿐이었다.

**코드**: 불명

**태그**: forgery-detection, calibration, generative

---

### [Detecting Defects that Matter: An Application-Driven Benchmark for Anomaly Detection in Manufacturing and Retail Logistics (VAND 4.0 Challenge)](https://arxiv.org/abs/2610.04392)

**한 줄 요약**: 산업 제조와 소매 물류 두 트랙에 걸친 hidden-test 이상 탐지 벤치마크와, 효율을 1급 지표로 삼은 챌린지 결과 분석.

**핵심 기여**: 기존 이상 탐지 벤치마크가 포화됐고 현실과 동떨어져 있다는 문제의식에서 배포가 중요한 두 영역에 hidden-test 벤치마크를 구성했다. 산업 트랙(MVTec AD 2)에서는 비지도 이상 분할의 최고 성능이 픽셀 수준 SegF₁ 약 57%에 그치고 zero-shot 접근이 약 15 SegF₁ 뒤처져 정상 데이터에 대한 과제별 학습이 정밀한 결함 위치 추정에 여전히 필수임을 보였으며, 분포 이동에 대한 강건성이 미해결 과제로 남은 가운데 DINOv3 백본이 이 트랙을 분명히 지배했다. 소매 트랙(Kaputt 2)에서는 흔한 결함 유형의 지도 검출이 포화에 가까워진 반면 최고 성능 off-the-shelf VLM 접근이 전용 모델보다 약 28 AP 뒤졌고, 희소 결함에서 성능이 무너졌으며(유출 약 53 AP, 수량 누락 약 27 AP) 참조 이미지는 상위 방법에 도움이 되지 않았다. 저유병률 소매 이상 탐지 데이터셋 Kaputt-Rare를 추가로 제공하고, 성능·처리량·메모리·전력 소비를 묶은 새 효율 지표로 평가해 상위 방법들이 무거운 구조에 의존하며 효율은 대체로 방치돼 있음을 보고한다.

**코드**: 불명

**태그**: anomaly-detection, defect-detection, industrial-inspection, dataset-benchmark

---

### [Selective Backpropagation for Efficient Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2610.04003)

**한 줄 요약**: 미리 할당한 파라미터 부분집합에만 gradient 갱신을 제한해 망각 억제와 적응 비용을 함께 잡은 few-shot class-incremental learning 기법 SBP.

**핵심 기여**: FSCIL은 제한된 샘플로 새 클래스를 계속 배우면서 이전 지식을 지켜야 하고 연산·메모리 제약도 엄격한데, 단순 미세조정은 효율적이지만 파국적 망각이 크고 replay 기반은 망각을 줄이는 대신 연산·메모리를 많이 쓰며 exemplar-free 방법은 백본 대부분을 동결해 효율을 얻는 대신 적응성을 잃는 trade-off가 있다. SBP는 결정론적 파라미터 예산 프레임워크로, gradient 갱신을 사전 할당된 파라미터 부분집합으로 제한해 과거 지식을 동결하고 미래 학습을 위한 용량을 편향 없이 남겨 비싼 마스크 최적화 없이 빠르게 적응한다. 표준 FSCIL 벤치마크 전반에서 naive 미세조정에 가까운 학습 시간으로 강한 성능을 내고 기존 SOTA보다 학습 시간이 크게 짧으며, 짧고 분포가 일정한 벤치마크 성능이 분포 이동이나 훨씬 긴 학습 지평에서의 거동을 예측하지 못한다는 평가상의 한계를 드러내 교차 도메인 설정과 80세션 ImageNet-1K 스트림에서 추가로 평가했다.

**코드**: 공개([sbp-main-public](https://github.com/PaInt-Lab/sbp-main-public))

**태그**: continual-learning, peft, efficient-inference

---

### [A General Pipeline for Dense Illuminant Estimation via Physically Based Synthetic Data](https://arxiv.org/abs/2610.06508)

**한 줄 요약**: 물리 기반으로 렌더링한 3D 장면에서 픽셀 단위 조명 색도 맵을 유도해 조명 추정 모델을 사전학습하는 재사용 가능한 합성 데이터 파이프라인.

**핵심 기여**: 조명 추정은 조명 조건에 따른 색 편차를 보정하게 해 주는 계산사진의 기본 문제지만, 정확한 조명 정답을 갖춘 대규모 데이터셋이 드물어 학습 기반 방법의 진전이 막혀 있다. 기존 3D 장면 모음을 재활용해 통제된 조명 조건 아래 픽셀 단위 조명 주석을 체계적으로 생성하는 일반적이고 재사용 가능한 파이프라인을 제안하고, 이를 통해 74,321장 규모의 합성 데이터를 만들어 단일 조명과 다중 조명 추정 모델을 모두 사전학습했다. 최신 구조들을 대상으로 한 실험에서 합성 사전학습이 일관되게 성능을 올렸고, 특히 데이터가 부족한 영역에서 단일 조명 추정 최대 28%, 다중 조명 추정 최대 57%의 개선을 보였다.

**코드**: 불명

**태그**: sim2real, synthetic-data, dataset-benchmark

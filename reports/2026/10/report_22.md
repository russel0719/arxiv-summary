# arXiv cs.CV Daily Digest — 2026-10-21 (arXiv 공개일)

- **전체 신규 논문 수**: 183편 (new 154 + cross-list 29)
- **선별 수**: 8편

## 오늘의 트렌드

월드 모델이 가장 두꺼운 군집으로, 행동 조건 비디오 월드 모델·실시간 게임 월드·JEPA 계열 잠재 월드 모델이 이어진다. feed-forward 3D/4D Gaussian Splatting 복원과 단안 4D 재구성이 두 번째 흐름이며, 의료 영상(MRI·병리 공간전사체·의료 VLM)도 비중이 크다. 비디오·멀티모달 모델 평가 벤치마크와 다중분광·SAR 원격탐사 검출이 별도 덩어리를 이룬다.

---

### [LocaLeJEPA: Maximum Entropy Representations under Geometric Priors](https://arxiv.org/abs/2610.28458)

**한 줄 요약**: LeJEPA의 전역 등방 가우시안 분포 매칭을 국소 유클리드 분포 매칭으로 바꿔, 쌍곡·등변 같은 비유클리드 임베딩 기하에서도 붕괴 없이 학습되는 JEPA 자기지도학습.

**핵심 기여**: JEPA 계열 SSL은 표현 붕괴(representation collapse)에 취약하고, 이를 해결한 LeJEPA는 임베딩을 전역 등방 가우시안으로 맞추는 분포 매칭 목적함수를 쓰지만 유클리드 가정에 묶여 있어 equivariant CNN·hyperbolic ViT 같은 비유클리드 임베딩 기하를 반영하지 못한다는 문제의식이다. LeJEPA의 엔트로피 최대화 성질을 다양체 관점에서 재정식화한 LocaLeJEPA와, 이를 안정적이고 확장 가능하게 구현하는 국소 유클리드 분포 매칭 정규화항 LocaLeReg를 제안한다. ImageNet-1K 사전학습에서 hyperbolic ViT-S/8·equivariant ResNet-50뿐 아니라 일반 유클리드 ViT-S/8·ViT-L/14에서도 linear probe·k-NN 정확도와 다운스트림 태스크 성능이 LeJEPA보다 높으며, 저장소 README 기준 ViT-S/8(100 epoch, frozen encoder)에서 linear probe 40.7%→49.6%, k-NN 24.3%→34.1%다. README는 각 결과가 단일 사전학습 run이고 두 방법의 학습률 등 레시피가 달라 차이 일부가 최적화 설정에서 올 수 있다고 밝힌다.

**코드**: 공개([alessioborgi/LocaLeJEPA](https://github.com/alessioborgi/LocaLeJEPA) · MIT), 사전학습 가중치는 미공개

**태그**: ssl-backbone, image-embedding, jepa, hyperbolic-embedding

---

### [In PRAISE of Attributes: Grounding Retrieval Geometry with Query-Conditioned Subspaces for Person Re-Identification](https://arxiv.org/abs/2610.27944)

**한 줄 요약**: 속성 프롬프트 뱅크로 쿼리마다 저차원 부분공간을 만들어 query–gallery 유사도를 재구성하는, VLM 기반 person ReID용 쿼리 측 test-time adaptation.

**핵심 기여**: VLM 기반 ReID에서는 시점·조명·가림 변화(I2I)나 불완전한 텍스트 설명(T2I) 때문에 오답 후보가 정답보다 가까워지고, 옷 색·소지품 같은 속성 프롬프트 유사도를 그대로 점수로 쓰면 템플릿 편향·상관·캘리브레이션 문제로 신뢰하기 어렵다는 문제의식이다. PRAISE는 Qwen2.5-VL로 생성한 보행자 설명에서 추린 전이 가능한 속성 프롬프트 뱅크로 쿼리와 가장 잘 맞는 속성 방향들의 저차원 부분공간(Attribute-Conditioned Subspace)을 만들고, 이 기하로 query–gallery affinity를 재구성하면서 신원·속성 라벨 없이 정규화 층의 affine 파라미터만 추론 시 갱신한다. 본문 기준 PLIP 백본에서 mAP/R1이 Market-1501 35.0/62.6→46.5/71.1, MSMT17 10.5/34.2→18.2/38.5, CUHK-PEDES 46.4/55.9→49.6/58.4, RSTPReID 23.1/34.5→27.6/37.6이며, CLIP·CLIP-ReID 등 다른 백본에서도 일반 TTA·ReID 전용 TTA보다 높다. 대신 샘플당 시간이 I2I 기준 1.8 ms에서 약 42.8 ms로 늘고, 고정 속성 뱅크라 어휘 밖의 희귀한 외형 단서나 가림이 심한 쿼리에서는 효과가 제한된다고 밝힌다.

**코드**: 공개([rB080/praise](https://github.com/rB080/praise))

**태그**: re-identification, image-retrieval, vlm, test-time-adaptation

---

### [FocusOVD: Geometric and Contextual Feature Refinement for Open-Vocabulary Small-Object Detection](https://arxiv.org/abs/2610.27479)

**한 줄 요약**: 고정된 CLIP 백본은 그대로 두고 FPN 융합·고해상도 국소 기하·RoI 판별력을 보강해 소형 객체 검출을 개선한 open-vocabulary detector.

**핵심 기여**: 기존 open-vocabulary detector는 고해상도 디테일 보존, 특징 레벨 간 정보 집계, 영역 수준 판별력이 부족해 소형 객체에 약하다는 문제의식이다. FocusOVD는 frozen CLIP 기반 2단계 검출기(RPN·RoIAlign·Fast R-CNN 헤드)에 레벨별 가중치를 학습해 얕은 외형 정보와 깊은 의미 정보를 섞는 Reweighted Cross-scale Feature Fusion, 고해상도 특징의 국소 기하 반응을 키우는 Residual Pinwheel-shaped Gated Convolution, RoI 예측 전에 배경 위주 활성을 억제하는 Residual Convolutional GLU를 더한다. COCO-OVD novel AP 36.3%로 CORA·UniDetector·SAMP보다 각각 1.3·1.1·1.5%p 높고 LVIS-OVD 전체 AP는 33.7%이며, 본문 기준 COCO-OVD novel APs는 24.3%(UniDetector 22.4%)다. 파라미터 수·연산량·추론 속도는 보고하지 않는다.

**코드**: 불명

**태그**: open-vocab-detection, object-detection, small-object-detection

---

### [Efficient SAM3 Adaptation for Multi-Class Semantic Segmentation via Dense Competitive Representations](https://arxiv.org/abs/2610.27960)

**한 줄 요약**: SAM3를 다중 클래스 semantic segmentation에 맞게 바꿔, 개념별 독립 추론 대신 한 번의 추론에서 클래스 간 경쟁을 강제하는 어댑테이션 프레임워크(DCR-SAM).

**핵심 기여**: SAM3는 짧은 명사구 하나에 대한 Promptable Concept Segmentation에 강하지만, 여러 개념을 동시에 분할하면 의미가 겹치는 개념끼리 오분류·중복 마스크가 생기고 개념 수만큼 추론을 반복해 지연이 선형으로 늘어난다는 문제의식이다. DCR-SAM은 교차 모달 상호작용을 분리해 지연을 줄이고, 텍스트 개념을 시각 표현에 동적으로 정렬한 뒤 dense competition head로 클래스 간 경쟁을 명시적으로 강제하며, 학습 가능한 배경 토큰이 대상 외 객체를 흡수하게 한다. 본문 기준 SAM3 백본 가중치는 고정하고 프롬프트 시퀀스·경량 교차 어텐션·배경 토큰만 학습하며, ADE20K 68.7, Cityscapes 89.1, Potsdam 90.2 mIoU로 기존 SOTA 대비 2.3~10.7% 높고, RTX 4090에서 ADE20K 이미지당 8,038 ms→244 ms로 SAM3보다 33배 빠르다. 한계로 클래스 간 경쟁이 학습하지 않은 개념의 인식을 약화시킬 수 있다고 밝힌다.

**코드**: 공개([set-path/DCR-SAM](https://github.com/set-path/DCR-SAM))

**태그**: segmentation, foundation-model, efficient-inference, sam

---

### [WildAIGC-Bench: Can AI Image Detectors Handle the Wild? A Benchmark of Generated and Edited Images in Online Circulation](https://arxiv.org/abs/2610.28087)

**한 줄 요약**: 뉴스·팩트체크·SNS에서 실제로 유통된 AI 생성·편집 이미지 407장을 압축·스크린샷·재촬영 상태 그대로 모은 AI 이미지 검출 벤치마크.

**핵심 기여**: 기존 AI 생성 이미지 검출 벤치마크는 온라인 유통 과정에서 생기는 압축·스크린샷·재촬영 같은 조건을 반영하지 못한다는 문제의식이다. 뉴스 사이트·팩트체크 출처·관련 SNS를 주기적으로 수집해 자동 선별·예비 주석을 거친 뒤 이미지별 증거를 사람이 검토하는 파이프라인으로, 출처 링크와 증거 요약이 붙은 407장을 구축했다. 전용 검출기 10종과 MLLM 6종을 평가하면 모든 구성에서 recall이 기존 벤치마크 평균보다 21.87~70.41%p 낮고, 본문 기준 PE-Core-L/14를 미세조정한 PE-518 baseline은 외부 벤치마크 BAcc 95.0%이지만 이 벤치마크의 processed recall은 23.10%다. 한계로 실제(real) 이미지 대조군이 없어 오탐률을 평가할 수 없고, 규모가 작으며 뉴스·팩트체크 맥락에 치우쳐 있다고 밝힌다.

**코드**: 공개([YuZijian/WildAIGC-Bench](https://github.com/YuZijian/WildAIGC-Bench), 데이터셋)

**태그**: forgery-detection, dataset-benchmark, ai-generated-image-detection

---

### [Using Set Learning to Improve Set-Valued Classifiers on Long-tailed Data](https://arxiv.org/abs/2610.27443)

**한 줄 요약**: 배치 안의 샘플 집합 단위로 학습하는 odd-K-out(OKO) 손실을 경량화해, long-tailed 데이터에서 top-k·average-k·conformal 집합값 분류기의 macro 정확도를 높이는 학습법.

**핵심 기여**: 입력마다 예측 집합 크기를 바꾸는 집합값 분류(set-valued classification)는 불확실성 표현에 쓰이지만 long-tailed 데이터의 macro 평가에서 성능이 크게 떨어지고, 보통 사후 캘리브레이션 단계에서 만들어져 학습 방식의 영향은 잘 알려져 있지 않다는 문제의식이다. label smoothing·class balancing과 함께 집합 단위 손실인 OKO를 조사하고, 한 번 순전파한 배치 안에서 집합을 구성하고 희귀 클래스용으로 이전 배치 logit을 저장하는 메모리 뱅크를 더한 IB-OKO_MB로 연산 부담을 cross-entropy 대비 3.2배에서 1.36배로 줄였다. 본문 기준 Pl@ntNet-300k(4개 아키텍처 평균)에서 macro-accuracy가 CE 대비 top-5 67.6→75.7%, average-k 72.5→82.0%, 임계값 기반(THR) 56.1→67.0%로 오르고, 예측 집합 크기는 크게 늘지 않는다. 한계로 집합 내 샘플을 균등 무작위로 고르는 단순한 구성이며, 저자가 수정한 BIOSCAN-5M 분할은 검증·테스트 클래스가 달라 conformal prediction의 오류율 보장이 깨진다고 밝힌다.

**코드**: 불명

**태그**: calibration, conformal-prediction, long-tail, set-valued-classification

---

### [From Generic to Dedicated: A Novel Optimizer for Online Continual Learning](https://arxiv.org/abs/2610.27835)

**한 줄 요약**: 빠르게 움직이는 가소성(plasticity) 시퀀스와 적응형 안정성(stability) 시퀀스를 보간해, 기존 online continual learning 방법의 SGD·AdamW를 그대로 대체하는 전용 옵티마이저 SPIN.

**핵심 기여**: 단일 패스 비정상 스트림에서 학습하는 online continual learning(OCL)은 파국적 망각에 취약한데, 데이터·구조 측면 연구에 비해 옵티마이저는 SGD·AdamW 같은 범용 방법을 그대로 써 왔다는 문제의식이다. Polyak-Ruppert averaging을 가소성, Primal averaging을 안정성의 동력으로 재해석해 두 시퀀스를 보간하는 SPIN을 제안하고, 이것이 암묵적으로 역 Hessian 근사와 Tikhonov 정규화를 수행해 노이즈가 큰 단일 샘플 Hessian 추정을 완화함을 이론적으로 보인다. 본문 기준 ER·DER++·OCM·GSA 등 11개 OCL 방법의 평균 정확도가 Split CIFAR-100에서 SGD 32.66→36.54%, AdamW 36.23→38.49%, Split Tiny-ImageNet에서 AdamW 24.95→26.56%로 오르며, rehearsal-free·메모리 제약 설정에서도 향상된다. 한계로 이론 분석이 smoothness·quasi-steady-state 가정에 의존하고, 두 iterate 시퀀스를 유지하느라 optimizer state가 늘며(GSA·CIFAR-100 기준 155.86 MB→240.75 MB), 사전학습 ViT·CLIP과의 결합은 향후 과제로 남긴다.

**코드**: 불명

**태그**: continual-learning, optimizer, catastrophic-forgetting

---

### [Reusing Assurance Evidence in AI Pipelines: Validity Conditions, a Fail-Closed Release Gate, and a Replay of 714 Public Data Version Control Pipelines](https://arxiv.org/abs/2610.27672)

**한 줄 요약**: AI 파이프라인에서 이전 거버넌스 검사 결과(서명된 evidence)를 재사용해도 되는 조건을 정식화하고, fail-closed 배포 게이트와 공개 DVC 파이프라인 714개 replay로 선언 누락 의존성 문제를 측정한 연구.

**핵심 기여**: 파이프라인이 바뀔 때마다 모든 거버넌스 검사를 다시 돌리기 어려워 이전 결과를 재사용하는데, 이는 각 검사의 선언된 의존성이 결과에 영향을 주는 모든 것을 덮고 게이트가 재사용 evidence가 배포 후보를 설명하는지 확인할 때만 안전하다는 문제의식이다. 서명된 evidence 기록이 후보에 대해 유효한 조건(서명·계약/컨텍스트 다이제스트·의존성 다이제스트·유효기간·통과 상태)과 변경 국소 재실행이 전체 재실행과 같은 배포 결정에 이르는 충분조건을 정의하고, Ed25519 서명 기반 참조 게이트가 조작 시나리오 9개 중 8개를 막음을 보인다(planner를 신뢰하는 게이트는 1개, 서명만 검증하는 게이트는 3개). 714개 공개 DVC 파이프라인의 커밋 38,083개를 replay하면 선언 의존성 기반 재사용이 stage 실행의 83.4%를 줄이지만 3.3%의 커밋에서 import 코드나 참조 설정이 바뀐 stage를 재사용하고(파이프라인의 31%가 해당) 평가 stage가 가장 많이 노출되며, stage별 정적 import closure를 의존성에 더하면 stale 재사용이 0.4%로 줄면서 실행 절감 81.6%가 유지된다. 한계로 선언되지 않은 의미적 의존성(예: 코호트 정의 변경)은 어떤 게이트도 막지 못하고, 정적 분석이 동적 import·저장소 밖 데이터를 놓치므로 보고된 stale 비율은 하한이라고 밝힌다.

**코드**: 공개 (분석 코드·프로토타입을 arXiv 부속 파일로 제공한다고 명시, 별도 저장소 URL 없음)

**태그**: deployment-gate, mlops, evidence-reuse

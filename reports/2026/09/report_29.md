# arXiv cs.CV Daily Digest — 2026-09-28 (arXiv 공개일)

- **전체 신규 논문 수**: 114편 (new 87 + cross-list 27)
- **선별 수**: 10편

## 오늘의 트렌드

3D Gaussian Splatting 복원과 novel view synthesis, world model·vision-language-action으로 행동을 잇는 연구, 의료영상 분류·분할, vision-language model의 능력과 실패를 재는 벤치마크가 두꺼운 군집을 이룬다. 방법론으로는 동결된 foundation model에 프롬프트·어댑터·라우팅만 얹어 적응시키는 설계와 diffusion prior를 증류해 추론 비용 없이 옮기는 설계가 반복된다. AI 생성 이미지의 출처를 화소만으로 가려내는 포렌식 계열도 함께 올라왔다.

---

### [Conditional Predictive Sufficient Statistics for Visual Representation Learning](https://arxiv.org/abs/2609.30647)

**한 줄 요약**: 시각 표현학습의 요구를 "미래 패치와 공유하는 잠재 요인만 남기는 조건부 예측 충분통계(CPSS)"로 형식화하고, stop-gradient와 회귀 대상 선택이 표현 기하에 남기는 흔적을 소규모 진단 실험으로 분해한 분석.

**핵심 기여**: 유용한 시각 표현은 관측된 과거에서 미래와 공유하는 잠재 요인을 남기고 패치 고유의 잡음을 버려야 한다는 요구를 조건부 예측 충분통계(CPSS)로 형식화한다. 패치 공유요인 모델 아래에서 다음 패치 임베딩을 코사인 손실로 예측하는 것이 그 임베딩 방향에 대한 von Mises-Fisher 모델의 최대우도이며 따라서 예측 정보량의 다루기 쉬운 대리 목적이 되지만, 같은 모집단 손실이 상수 임베딩으로도 최소화되므로 stop-gradient 자체는 충분통계를 골라 주지 않고 상수해로 가는 대칭 그래디언트를 한 스텝에서 막을 뿐이라고 주장한다. MNIST·CIFAR-10의 작은 causal Transformer를 리더보드가 아닌 진단 도구로 써서, 회귀 대상이 얕은 임베딩이기 때문에 충분통계가 출력이 아닌 중간 블록에 남고(CPSS 출력이 자신의 최적 중간 블록보다 나쁜 readout), stop-gradient를 제거하면 pretext 손실이 정상으로 보여도 임베딩의 유효 랭크가 붕괴함을 보고한다. CIFAR-10에서는 짧은 학습 예산과 증강 없음 조건에서 모든 목적함수가 픽셀 선형분류기 수준에 머물렀다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, predictive-coding

---

### [Structure-Guided Masked Autoencoders for Ultra-High Resolution Scientific Image Understanding](https://arxiv.org/abs/2609.30682)

**한 줄 요약**: 기가픽셀 이미지에 MAE 사전학습을 적용하기 위해 내용 적응형 quadtree 토크나이저와 구조 조건부 마스킹을 결합한 self-supervised 프레임워크.

**핵심 기여**: ViT 기반 Masked Autoencoder 사전학습은 기가픽셀 과학 이미지에서 두 가지로 막힌다 — 무작위 마스킹이 구조적·다중 스케일 형태와 어긋나고, 균일 토큰화가 $O(N^2)$ 어텐션을 감당할 수 없는 길이의 시퀀스를 만든다. SGMA는 기가픽셀 이미지를 고정 길이 시퀀스로 압축하는 내용 적응형 quadtree 토크나이저와, 공간적으로 정보량이 큰 영역 쪽으로 재구성을 편향시키는 구조 조건부 마스킹을 결합하고, 트리 전체에 걸쳐 신호 의존 반응을 누적해 마스킹을 안내하는 구조 캔버스를 만드는 Damped Accumulation으로 스케일 간 과정을 안정화한다. 표준 ViT 인코더와 MAE 방식 재구성과 호환되는 형태를 유지하면서, 전자현미경·전슬라이드 광학현미경·X선 CT 데이터셋에서 MAE 베이스라인을 일관되게 넘어 8K×8K×28K SpringXCT에서 Dice 95.68%(동일 구조 MAE 대비 +13.00점), 32K² WSI PAIP에서 83.21%(+16.84점)를 기록했고 추론은 최대 24.8배 빨랐다.

**코드**: 불명

**태그**: ssl-backbone, segmentation, efficient-inference

---

### [Forensic Twins: Self-Supervised Residual Learning for AI-Generated Image Forensics](https://arxiv.org/abs/2609.31514)

**한 줄 요약**: 포렌식 잔차에서 뽑은 서로 겹치지 않는 두 crop을 정렬시키는 self-supervised 사전학습으로 촬영 파이프라인 지문을 학습하고, 실제 이미지만 보고도 미지의 생성기를 잡아내는 프레임워크.

**핵심 기여**: AI 생성 이미지 탐지기는 잡아야 할 모든 생성 구조의 샘플로 학습되기 때문에 새 구조가 등장하면 무너지고, 대안으로 쓰인 표준 self-supervised 프레임워크는 증강이 이미지 형성의 미시 통계를 덮어써 포렌식 과제와 상충한다는 문제에서 출발한다. Forensic Twins는 각 이미지를 동결된 기성 포렌식 잔차 추출기에 통과시킨 뒤 픽셀을 전혀 공유하지 않는 두 crop을 뽑는 Self-Supervised Residual Learning(SSRL) pretext를 써서 거시적 내용 가용성을 억제하며, 두 view가 맞출 의미 구조가 거의 없으므로 중복 감소 목적이 붙잡는 지배적 공통 신호가 촬영 파이프라인의 정상(stationary) 지문이 되게 한다. 학습에는 실제 이미지만 쓰고 AI 생성 이미지를 어느 단계에서도 보지 않으며, 생성기 출처 귀속 정확도 56.61%로 기존 zero-shot 최고 기법보다 6.13% 높으면서 지연은 375배 낮았고, 이 표현에서 뽑은 실제 이미지 임베딩만으로 오프라인에서 Gaussian Mixture Model을 적합하면 GAN·diffusion·상용 시스템을 포함한 미지의 생성기 27종에서 AUC 97.99%의 zero-shot 탐지기가 된다고 보고한다.

**코드**: 공개 예정

**태그**: ssl-backbone, forgery-detection, image-embedding, anomaly-detection

---

### [FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders](https://arxiv.org/abs/2609.31620)

**한 줄 요약**: 사전학습 인코더 레이어의 무작위 부분집합으로 학습해 고정 layer fusion 선택을 없앤 representation autoencoder 정규화 기법.

**핵심 기여**: representation autoencoder(RAE)는 사전학습 시각 인코더의 특징을 재구성·diffusion latent로 재사용하는데, 어느 인코더 레이어를 공유 latent로 묶을지 고르는 문제에서 얕은 레이어는 미세한 픽셀 디테일을, 깊은 레이어는 생성 지표를 각각 유리하게 만드는 상충이 생기고 고정 휴리스틱 융합은 요구가 다른 두 단계를 하나로 묶어버린다. FuseReg는 휴리스틱 특징 선택을 인코더 레이어의 무작위 부분집합에 대한 학습으로 대체하며, 부분집합 샘플링이 레이어 간 불일치에 대한 민감도를 명시적으로 벌점화한다는 기제를 이론적으로 분석한다. DINOv3-L을 쓴 ImageNet-256에서 단일 FuseReg 디코더가 재학습 없이 전체·희소·단일 레이어 융합 모두에서 재구성하며 고정 융합에 특화된 디코더보다 높은 PSNR을 얻었고, RAEv2 DiT-XL 생성기를 바꾸지 않고 디코더 교체만으로 unguided gFID가 27% 줄었으며 같은 정규화를 diffusion 학습까지 확장해 두 단계를 함께 정규화하면 DiT-Base에서 29% 줄었다.

**코드**: 불명

**태그**: image-embedding, foundation-model, generative

---

### [Preserve-and-Compose Training for Composed Image Retrieval](https://arxiv.org/abs/2609.31202)

**한 줄 요약**: 타깃 캡션 감독만 쓰던 zero-shot composed image retrieval에 소스 이미지의 시각 근거를 함께 학습시키고, 동결된 이미지 공간에서의 방향 일치를 더해 재채점하는 학습 기법.

**핵심 기여**: composed image retrieval(CIR)은 참조 이미지에서 보존해야 할 시각 내용을 유지한 채 사용자가 지정한 수정을 만족하는 이미지를 찾아야 하지만, 타깃 이미지 수집 비용 때문에 타깃 캡션을 감독으로 쓰는 zero-shot 방식이 동원되고 이때 캡션이 보존돼야 할 소스 세부를 빠뜨린다는 문제가 있다. Preserve-and-Compose Training(PACT)은 타깃 이미지도 갤러리 갱신도 없이 image–text–text 삼중항으로 학습해 합성된 질의를 타깃 캡션에 정렬시키면서 시각 감독으로 소스 근거를 보존하고, 동결된 이미지 공간에서 타깃 유사도와 소스 기준 방향 일치를 결합하는 Chord scoring을 함께 제안한다. ZS-CIR 벤치마크 4종에서 데이터셋·백본 규모·외부 갤러리에 걸쳐 검색 성능이 개선됐다고 보고한다.

**코드**: 공개([PACT](https://github.com/sehyunkwon/PACT))

**태그**: image-retrieval, image-embedding, metric-learning, vlm

---

### [Query-Conditioned Prototype Adaptation for Cross-Domain Few-Shot Learning: Single-Query Inference, Controlled Comparisons, and Failure Modes](https://arxiv.org/abs/2609.30769)

**한 줄 요약**: 동결 ViT 위에서 라벨 없는 질의 하나와 support 임베딩을 함께 변환해 질의별 프로토타입을 만드는 test-time 적응을, 다섯 시드 반복과 rescue/break 분해로 통제해 재검증한 연구.

**핵심 기여**: cross-domain few-shot 학습은 타깃 시점 파라미터 갱신 없이 소수 라벨만으로 새 도메인에 적응해야 하는데, 고정된 전역 표현 아래에서 질의–support 결합 적응이 프로토타입 구성에 무엇을 보태는지를 분리해 묻는다. Within-Instance Prototypical Transformer(WIPT)는 라벨 없는 질의 하나와 라벨된 support 임베딩을 함께 변환한 뒤 질의별 클래스 평균을 만드는 단일 질의 test-time 프로토타입 적응이며, 공유 동결 ViT-S/16 인코더와 miniImageNet 소스 학습, CUB·EuroSAT·ISIC 타깃으로 다섯 개의 독립 학습 시드에서 핵심 비교를 재현한다. 1-shot에서 CUB(+0.21%p)와 EuroSAT(+2.07%p)은 모든 시드에서 frozen ProtoNet을 넘었으나 ISIC은 -0.22%p로 떨어졌고, 5-shot에서는 ProtoNet이 전반적으로 가장 강한 가운데 WIPT는 용량을 맞춘 support-only Transformer를 ISIC에서 일관되게 앞섰다(+0.99). 질의 다섯 개를 함께 처리해도 신뢰할 만한 정확도 이득은 없었고(어텐션 토큰쌍 73%·최대 할당 메모리 29% 감소에 그치며 지연은 단조롭지 않음), WIPT가 ProtoNet의 확신 있는 결정보다 불확실한 결정을 훨씬 많이 바꾼다는 분해와 함께 이득이 보편적이지 않음을 소스 이동·채점기 통제로 덧붙인다.

**코드**: 불명

**태그**: metric-learning, image-embedding, few-shot, training-free

---

### [FARE: Forensic Acceptance Region Estimation for Catching Bait-and-Switch Image Generators](https://arxiv.org/abs/2609.30982)

**한 줄 요약**: 인증된 생성기의 샘플로 수용 영역(acceptance region)을 추정해, 배포 중 다른 생성기로 몰래 바뀌었는지를 이미지 한 장만으로 판정하는 배포 시점 무결성 감사 기법.

**핵심 기여**: AI 이미지 생성기가 가중치·구조를 볼 수 없는 불투명 API로 배포되면서, 공급자가 한 생성기로 거버넌스 인증을 통과한 뒤 더 싸고 품질이 낮은 생성기로 조용히 바꿔치기할 수 있다는 실질적 위험을 배포 시점 무결성 감사 문제로 정식화한다. FARE는 인증된 생성기에서 샘플링한 이미지로 학습해 그 생성기를 등록(enroll)하고, 배포 후에는 생성 이미지 한 장만으로 그것이 등록된 생성기와 일관되는지 판정하며, 특징은 포렌식 용도로 제안돼 온 생성기 고유 아티팩트에 기반하되 수용 영역을 좁히고 인증된 생성기의 미세한 변화에 대한 민감도를 높이는 hard sample 탐색으로 학습 중 이를 증폭한다. 유사 버전·모델 변형으로의 치환을 포함한 생성기 교체 전반에서 교체를 효과적으로 탐지해 엄격한 동작점 기준 기존 베이스라인을 일관되게 앞섰고, 논문이 평가한 exact-model 및 decision-only 공격 아래에서도 유효했다고 보고한다.

**코드**: 불명

**태그**: forgery-detection, calibration, anomaly-detection

---

### [Can Pixels Alone Reveal Image Origin? Minimax Limits and Learnable Interfaces for Passive Provenance](https://arxiv.org/abs/2609.30997)

**한 줄 요약**: 화소만으로 이미지 출처를 가리는 문제의 최적 로버스트 성능 한계를 총변동거리로 규정하고, 배포된 공개 검증기가 그 한계에 닿기 전에 무너지는 이유를 대리 모델 공격으로 설명한 이론·실증 연구.

**핵심 기여**: 수동적 이미지 provenance(사람·AI 클래스·특정 생성기 구분)를 적대적 분포 이동 아래의 source–target 검증 문제로 놓는다. 첫 결과로, 이미지만 보는 어떤 검증기든 달성 가능한 최대 로버스트 타깃 수용 격차가 타깃 분포와 공격된 소스 분포 집합 사이의 최소 총변동거리와 정확히 같음을 보이며, 이 값은 검증기 구조가 아니라 소스·타깃·편집 클래스에만 의존한다. 둘째로, 검증기를 공격 영역에서 오차 $\varepsilon$로 모사할 수 있으면 대리 블랙박스 공격이 화이트박스 최적해의 $2\varepsilon$ + 최적화 오차 이내로 타깃 수용에 도달하고, 공개 특징 위의 logistic·softmax 헤드처럼 점수를 드러내는 구조는 식별 가능하며 근사적 점수 접근만으로도 안정적 복원 한계가 성립한다고 주장한다. 양변이 계산 가능한 유한 상태 실험으로 minimax 등식을 확인했고, 같은 프롬프트의 실제/diffusion 벤치마크에서 평가한 공개 CLIP 검증기는 표적 픽셀 공격에 무너진 반면 ResNet-18 피해자는 부분적인 fake→real 전이를 보였다. 기권(abstention)을 허용한 이진 피드백은 측정된 공격 성공률을 낮췄으나, 양의 경험적 격차 상한이 로버스트성을 입증하지는 않는다는 한계를 함께 적는다.

**코드**: 불명

**태그**: forgery-detection, calibration, adversarial-robustness

---

### [Geometric Inconsistency Localization in Multi-View Image Sets](https://arxiv.org/abs/2609.31247)

**한 줄 요약**: 넓은 베이스라인 이미지 쌍에서 기하 불일치를 화소 단위로 국소화하는 포렌식 과제를 정의하고, 교차 시점 특징 관계를 쓰는 경량 분류기와 주석 데이터셋을 함께 제시한 연구.

**핵심 기여**: novel view synthesis(NVS)가 만든 뷰들은 서로 기하적으로 일관되지 않을 수 있고, multi-view 일관성은 NVS 모델 평가 도구로는 쓰였으나 멀티미디어 포렌식, 특히 넓은 베이스라인 이미지 쌍에서 기하 불일치를 국소화하는 용도로는 거의 탐색되지 않았다는 문제를 다룬다. 화소 단위 기하 불일치 주석을 가진 넓은 베이스라인 multi-view 데이터셋 DeformView를 만들어 최신 multi-view 일관성 점수화 기법을 평가한 결과, NVS 평가용으로 개발된 접근은 이 포렌식 과제로 잘 전이되지 않았다. 이에 제안한 DEFECt3R은 교차 시점 특징 관계로 화소 단위 기하 불일치를 국소화하는 경량 학습 기반 분류기로, 기하적으로는 일관되지만 변형된 뷰를 hard negative로 포함한 명시적 감독으로 학습해 기존 일관성 점수화 기법 대비 국소화 성능을 높이고 오탐을 크게 줄였으며, ablation은 특징 표현과 대응(correspondence) 품질이 모두 성능에 기여함을 보인다.

**코드**: 공개([DeformView-DEFECt3R](https://github.com/IDLabMedia/DeformView-DEFECt3R))

**태그**: correspondence, feature-matching, forgery-detection, dataset-benchmark

---

### [CSCWD: Cross-Scale Channel-wise Knowledge Distillation for Lightweight Tiny Object Detection on Edge Devices](https://arxiv.org/abs/2609.30395)

**한 줄 요약**: 고해상도 P2 teacher의 표현을 student의 P3로 옮기는 교차 스케일 채널 증류로, 추론 구조를 바꾸지 않고 경량 검출기의 초소형 객체 성능을 올리는 학습 단계 기법.

**핵심 기여**: 항공 영상의 실시간 초소형 객체 검출은 아주 작은 객체의 공간 증거가 약하고 경량 검출기가 고해상도 디테일을 잃는다는 제약을 받는다. CSCWD는 YOLO11m-P2 teacher의 고해상도 공간 표현을 YOLO11n student로 옮기는 학습 단계 프레임워크로, 동일 스케일 특징 증류와 달리 특징 정렬 후 teacher의 P2에서 student의 P3로 감독을 전달하고 더 깊은 피라미드 레벨에서는 동일 스케일 증류를 유지하며, student의 추론 구조는 그대로 둔다. 통합 7-시퀀스 Drone-vs-Bird 검증 프로토콜에서 mAP@0.5 50.17%·recall 59.73%로 조건을 맞춘 CA-YOLO11n 베이스라인 대비 각각 2.92·3.55%p 높았고, 교차 스케일 정렬만으로 대응하는 동일 스케일 채널 증류 설정보다 mAP@0.5가 2.09점 더 올랐으며, DUT-Anti-UAV zero-shot 평가에서는 타깃 도메인 미세조정 없이 48.29%에서 50.06%로 올랐다. Raspberry Pi 5에서 NCNN-FP16·640×640 기준 258만 파라미터 student가 mAP@0.5 50.32%를 평균 82.32ms(12.15 FPS)에 내며 베이스라인과 사실상 같은 실행시간·메모리를 유지했다.

**코드**: 불명

**태그**: distillation, object-detection, efficient-inference

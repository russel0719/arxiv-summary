# arXiv cs.CV Daily Digest — 2026-10-01 (arXiv 공개일)

- **전체 신규 논문 수**: 224편 (new 187 + cross-list 37)
- **선별 수**: 12편

## 오늘의 트렌드

비디오 생성·월드 모델과 VLA/로봇 정책이 가장 두꺼운 군집을 이루고, 그 뒤를 VLM의 공간 추론·그라운딩, 멀티모달 모델의 on-policy 자기증류, 3D Gaussian Splatting 계열 재구성이 잇는다. 적대적 공격·워터마킹·생성물 판별을 다루는 포렌식 군집도 별도로 형성됐다. 방법론 흐름으로는 학습 없이 추론 시점에만 개입하는 training-free 보정, 에이전트가 도구를 호출해 증거를 모으는 구성, 자기지도 표현학습을 멀티뷰·연속 스트림 같은 비 i.i.d. 데이터로 확장하려는 시도가 두드러진다.

---

### [Masked Swingers: Harnessing Data Augmentation to Advance Autoencoders for Self-Supervised Learning](https://arxiv.org/abs/2609.38278)

**한 줄 요약**: 한 이미지의 두 증강 뷰 사이에서 CLS 토큰을 맞바꾼 뒤 마스킹된 패치를 복원하게 해 MAE의 전이 성능을 끌어올린 자기지도 사전학습 기법.

**핵심 기여**: MAE는 재구성 목표 때문에 뷰에 종속된 표현을 학습하기 쉽다는 문제의식에서 출발한다. Masked Swingers는 이미지를 서로 다른 두 방식으로 증강해 각 뷰를 따로 마스킹·인코딩한 다음, 디코딩 직전에 두 뷰의 전역 표현(CLS 토큰)을 교환함으로써 뷰에 무관한 요약을 학습하도록 설계했다. ImageNet-1K kNN에서 MAE 대비 +3~5%p, fine-grained 과제에서는 instance retrieval 상대 +45%, 동물 re-ID +22%, Omniglot 문자 인식 +76%의 상대 향상을 보고했고, 새로 구성한 세 개의 state-probing 데이터셋에서는 오차를 상대 -64% 줄였다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, image-retrieval, fine-grained, re-identification

---

### [Emergent Multi-View Geometry Through Self-Distillation](https://arxiv.org/abs/2609.39227)

**한 줄 요약**: RGB 재구성 대신 자기증류로 멀티뷰에서 표현을 학습해 대응 추정·카메라 포즈에서 DINOv3를 앞선 자기지도 백본 Poincar3.

**핵심 기여**: 기존 시각 표현학습은 단일 이미지에 머물거나, 멀티뷰를 쓰더라도 RGB 재구성에 의존해 기하와 외형이 뒤섞인다는 점을 지적한다. Poincar3는 추가 뷰를 관찰하는 teacher를 두고 마스크 패치 수준과 이미지 수준의 자기증류를 결합해, 명시적 3D 감독 없이 처음부터(from scratch) 학습한다. correspondence 추정, 카메라 포즈 추정, 3D 재구성에서 DINOv3·MuM·Muskie 등 단일/멀티뷰 자기지도 기법을 모두 상회했고, 경량 Poincaré 어댑터를 붙이면 학습된 특징이 기존 자기지도 표현보다 카메라 움직임을 더 정확히 담고 있음을 확인했다.

**코드**: 불명

**태그**: ssl-backbone, correspondence, feature-matching, pose

---

### [FAST: Flow Any Scene Transformer](https://arxiv.org/abs/2609.39748)

**한 줄 요약**: 단일 뷰 비전 파운데이션 모델의 query-key 투영을 그대로 재활용해 cross-view 매칭기로 바꾸는, 확장 가능한 dense correspondence 모델.

**핵심 기여**: 정밀 대응 매칭 분야에서는 스케일링의 효과가 충분히 탐구되지 않았다는 문제의식에서 출발한다. 저자들은 단일 뷰 파운데이션 모델 내부의 query-key 투영이 이미 cross-view 매칭에 쓸 수 있는 거친 사전지식을 담고 있음을 보이고, 선택된 self-attention 층을 파라미터 추가 없이 cross-attention으로 재배선(zero-parameter rewiring)해 ViT 기반 매칭기를 구성한다. 이렇게 하면 쌍(pair) 전용 사전학습 단계를 건너뛰고 단일 뷰 백본의 발전에 그대로 올라탈 수 있으며, 600만 쌍 규모의 일반 목적 2D 변위 추정 코퍼스로 학습해 다양한 벤치마크에서 SOTA를 달성하고 백본 크기·데이터 양 모두에 대해 유리하게 스케일링된다.

**코드**: 불명

**태그**: feature-matching, correspondence, foundation-model

---

### [Spherical Interpolation for Backward-Compatible Multimodal Representations](https://arxiv.org/abs/2609.39836)

**한 줄 요약**: 갤러리 재색인 없이 모델을 교체하기 위해, 정렬된 신규 쿼리와 구 모델 쿼리 사이의 구면 측지선을 보간해 검색 성능을 회복하는 방법.

**핵심 기여**: 독립적으로 학습된 contrastive VLM은 표현 공간이 호환되지 않아, 배포 모델을 교체하면 갤러리 전체 임베딩을 다시 계산해야 하는 비용 문제가 생긴다. 직교 사후 정렬(orthogonal post-hoc alignment)로 신규 쿼리를 구 공간에 사상할 수 있지만 미세 구조 차이 때문에 잔여 각도 오차가 남는데, 이 논문은 두 정규화된 쿼리 표현 사이의 구면 측지선 위에 양 끝점보다 검색 최적 방향에 가까운 내부 지점이 존재하는 조건을 특성화하고 이를 지역 마진 기반 인증 결과로 Recall@K와 연결한다. 여러 벤치마크·모델 계열 실험에서 직교 정렬 단독 대비 개선을 보였고, 쿼리별 oracle 분석에서도 검색에 유리한 내부 지점이 빈번히 존재함을 확인했다.

**코드**: 공개([SLERP_backward_compatibility](https://github.com/miccunifi/SLERP_backward_compatibility))

**태그**: image-retrieval, image-embedding, metric-learning, foundation-model

---

### [I Have a Stream: Making Self-Supervised Learning Work on Continuous Video](https://arxiv.org/abs/2609.40333)

**한 줄 요약**: 셔플 없이 시간 순서대로 들어오는 연속 비디오 스트림에서 자기지도 사전학습을 성립시키는 StreamMAE와 95시간 규모 데이터셋 WT++.

**핵심 기여**: 표준 자기지도 학습은 이미지를 독립 샘플링해 전역 셔플하지만, 실제 시각 발달은 연속 스트림에 가깝다는 간극을 다룬다. 저자들은 전역 재셔플·다중 epoch 재생 없이 슬라이딩 윈도 배치로만 소비하는 설정을 정의하고 95시간 도시 보행 영상 WT++를 구축했는데, contrastive·distillation 계열은 크게 무너지고 MAE가 상대적으로 견고하나 i.i.d. 사전학습에는 못 미쳤다. 원인은 배치 간 유사도가 아니라 배치 내 프레임이 거의 중복이라는 점(intra-batch similarity)이었고, 이를 스트림 인지 정규화와 모션 기반 crop 선택으로 완화한 StreamMAE는 동일 영상으로 학습한 i.i.d. MAE와 동등한 수준에 도달하며 스트림 길이를 12시간에서 95시간으로 늘릴수록 성능이 올라갔다.

**코드**: 불명

**태그**: ssl-backbone, continual-learning, video, image-embedding

---

### [TED: Text-Axis Evidence Decomposition for Prompted Anomaly Localization](https://arxiv.org/abs/2609.39033)

**한 줄 요약**: 결함 증거와 '어려운 정상' 증거를 텍스트 축 위에서 분해해, 백본·프롬프트를 그대로 둔 채 이상 위치 추정 점수를 사후 보정하는 방법.

**핵심 기여**: 프롬프트나 경량 모듈로 적응시킨 CLIP 기반 이상탐지기는 민감도가 올라가도 도메인 변화 아래에서 실제 결함과 시각적으로 복잡한 정상 영역 모두에 높은 점수를 주는데, 저자들은 이를 결함 증거와 hard-normal 증거를 같은 값으로 디코딩하는 지역 점수 규칙의 문제로 규정한다. TED는 모호한 반응이 소스의 결함 패치와 정상 패치 중 어느 쪽에 더 잘 지지되는지를 정상-이상 텍스트 응답 아래에서 비교하는 사후(post-hoc) 점수로, 대상 도메인 학습을 요구하지 않으며 동결 VLM 백본의 train-free 점수로도, 적응된 CLIP-AD 호스트의 소스 보정 잔차 보정으로도 쓸 수 있다. 픽셀 단위 P-AUROC·P-PRO·P-AP 대부분에서 개선됐고, hard-FP 경쟁이 약한 구간의 평균 +5.0에서 중·강 경쟁 구간의 약 +10.9로 이득이 커졌다.

**코드**: 공개 예정

**태그**: anomaly-detection, defect-detection, training-free, calibration

---

### [DCM-SAM: Defect-Conditioned Mixture of LoRA Experts for NPU-Deployed AM Defect Segmentation](https://arxiv.org/abs/2609.38811)

**한 줄 요약**: 동결 SAM 백본에 결함 종류별 Conv-LoRA 전문가 뱅크를 붙여 합성 데이터만으로 학습하고, 모바일 NPU에서 FP16 실행까지 확인한 결함 분할 모델.

**핵심 기여**: 금속 적층제조(AM) 부품의 X선 CT 검사는 라벨이 희소하고 문제가 되는 기공·개재물이 수 픽셀 크기이며 장비 옆에서 추론해야 한다는 제약을 갖는다. DCM-SAM은 하나의 동결 Segment Anything 백본 위에 결함 클래스별 Conv-LoRA 전문가 뱅크와 마스크 디코더를 두고 프롬프트 없이 합성 슬라이스만으로 클래스별 개별 학습을 수행하며, 전체 파라미터의 4.4%만 갱신한다. ViT-B 백본으로 XCT-SAM의 ViT-H 기준 모든 베이스라인을 상회했고 실제 이미지를 전혀 보지 않고도 NIST 실측 스캔에서 기공 IoU 64.2%를 얻었다. 배포 단계에서는 Qualcomm Hexagon NPU에서 ViT-H·ViT-L이 1024×1024 해상도에서 가중치가 아닌 활성값 때문에 메모리 할당에 실패했고, 어텐션을 수치적으로 동일하게 재작성한 뒤에야 전체 모델이 CPU 폴백 없이 FP16으로 동작하며 FP32 기준 대비 픽셀의 0.01% 이내 차이를 보였다.

**코드**: 공개([DCM-SAM](https://github.com/MushfiqShovon/DCM-SAM))

**태그**: defect-detection, industrial-inspection, segmentation, peft, efficient-inference

---

### [Seeing as Humans Do: Learning from Motion to Segment Anything Without Supervision](https://arxiv.org/abs/2609.39785)

**한 줄 요약**: 라벨 없는 영상의 모션에서 다중 granularity 의사 라벨을 만들어 objectness 사전지식을 학습하고, 이를 이미지용 프롬프트 기반 분할로 전이한 비지도 SAM.

**핵심 기여**: SAM은 대규모 수작업 라벨에 의존하고 기존 비지도 모션 기반 방법은 움직이는 물체에 과적합돼 정지 물체로 일반화되지 않는다는 문제의식에서 출발한다. MoSA는 (1) 대규모 영상에서 다중 granularity 모션 의사 라벨을 자동 생성하고, (2) contrastive learning으로 Perceptual Grouping Model을 학습해 외형 기반의 일반화된 객체 개념을 내재화한 뒤, (3) 이 사전지식을 프롬프트 기반 구조로 옮겨 이미지에 대해 segment-anything 방식으로 추론한다. COCO·ADE20K를 포함한 7개 벤치마크의 zero-shot 평가에서 기존 비지도 방법을 크게 앞섰고, 수작업 라벨을 전혀 쓰지 않고도 완전지도 SAM에 필적하는 분할 성능을 보고했다.

**코드**: 불명

**태그**: segmentation, ssl-backbone, open-vocab-detection, video

---

### [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)

**한 줄 요약**: 점과 박스를 공유 어휘의 양자화 좌표로 생성하는 4B 그라운딩 파운데이션 모델로, 34개 벤치마크 평균 73.68%와 하류 백본 성능을 함께 보고한다.

**핵심 기여**: VLA·world-action 모델이 범용 비전-언어/비디오 백본에서 지각을 가져다 쓰기 때문에 혼잡한 장면이나 작은 객체에서 실패한다는 점을 문제로 삼는다. GroundingPI는 멀티모달·공간 사전학습, 지도 미세조정, GRPO 강화학습을 결합하고 공개 데이터셋과 전용 데이터 엔진의 감독을 사용해, 11가지 지각 능력에 걸친 34개 벤치마크·44개 베이스라인 비교에서 평균 73.68%로 더 큰 GPT-6 Astra(71.54%)를 상회했다. 하류 백본으로 쓸 때 RoboTwin 2.0의 네 가지 OOD 설정 모두에서 최강 백본 대비 최대 상대 24.8% 개선, RoboCasa-GR1에서는 시연의 50%만으로 75%를 쓴 베이스라인을 넘었으며, nuScenes 개루프 L2 오차는 평균 0.296 m였다. 사전학습 데이터 구성 분석에서는 dense grounding의 기여가 크고 OCR이 지각 학습의 촉매가 될 수 있음을 보고한다.

**코드**: 불명

**태그**: open-vocab-detection, foundation-model, object-detection, vlm

---

### [GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed](https://arxiv.org/abs/2609.39600)

**한 줄 요약**: 그라운딩을 좌우 순서가 없는 증거 추출로 보고, 블록 단위 디노이징으로 병렬 디코딩과 정밀 위치추정을 함께 얻은 4B 모델.

**핵심 기여**: 자기회귀 그라운딩 모델은 공간 예측을 직렬화해 지연이 생기고 출력 토큰에 인과적 순서를 강제하지만, 객체·위치·공간 관계의 의존성에 본래적인 좌→우 생성 순서는 없다는 관찰에서 출발한다. GroundAnything은 양방향 diffusion이 이 구조에 적합하다고 보고, 그라운딩 사전학습·AR에서 diffusion으로의 직접 변환(AR과 diffusion 목적 동시 학습)·지도 미세조정·GRPO 후학습을 결합한다. 30개 그라운딩 벤치마크에서 자기회귀 변형이 동급 규모 모델 중 72.42%로 최고를 기록했고(GPT-6 Astra 71.35%), 엔트로피 유도 디코딩을 쓴 병렬 버전은 61.75%로 기존 고속 MTP 기반 LocateAnything(53.32%)을 앞섰다. self-speculative 모드는 COCO F1mIoU 0.74%p 손실로 AR 대비 4.51배 가속을 보였다.

**코드**: 불명

**태그**: open-vocab-detection, object-detection, efficient-inference, foundation-model

---

### [Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066)

**한 줄 요약**: 7개 영역 22종 포렌식 도구를 에이전트가 다회차로 호출해 이미지 위조를 탐지·지역화하고 근거까지 생성하는 프레임워크.

**핵심 기여**: 기존 위조 탐지는 이진 점수나 픽셀 마스크만 내놓고, MLLM 기반 방법은 이미 정해진 분류 결과를 사후에 설명할 뿐 증거에서 추론하지 않는다는 점을 지적한다. ATAR는 의심 영역을 확대해 정밀 검사하는 상위 의미 이상 경로와 포렌식 도구로 객관적 증거를 추출하는 하위 아티팩트 경로를 결합한 Dual-Stream Forensic Reasoning을 쓰고, 교사-학생 멘토링으로 다회차 도구 사용 궤적을 합성하는 SFT 단계와 도구 사전 커리큘럼·구조화 증거 보상을 쓰는 강화학습 단계로 학습한다. 6개 zero-shot IMDL 벤치마크에서 이미지 수준 평균 F1 78.5%로 최강 MLLM 베이스라인 대비 11.8%p 앞섰고, Deepfake·DMDL·AIGC 탐지에서는 전용 탐지기와 경쟁 가능한 수준을 유지했다.

**코드**: 불명

**태그**: forgery-detection, anomaly-detection, vlm, foundation-model

---

### [Curating Synthetic Data for Task-Specific Visual Perception](https://arxiv.org/abs/2609.38476)

**한 줄 요약**: '얼마나 더 생성할까'가 아니라 '무엇을 생성할까'를 중심에 놓고 세 가지 합성 데이터 큐레이션 패러다임을 정리한 글.

**핵심 기여**: 범용 데이터셋이 과제별 사전지식을 주지 못하고 수작업 주석이 비싸거나 불가능한 영역에서 합성 데이터의 가치가 가장 크다는 전제에서, 장면 내용·외형 변이·센싱 특성·주석을 과제에 맞춰 설계하는 '큐레이션된 합성 데이터'를 논한다. 절차적 렌더링은 장면 파라미터를 명시적으로 제어하고 주석이 구성상 따라오며, 물리 기반 시뮬레이션은 관측 효과의 메커니즘을 인코딩해 정확히 정렬된 감독 쌍을 만들고, 생성형 AI는 소량의 실제 시드에서 센서별 외형을 학습하지만 환각과 부정확한 주석에 취약하다고 정리한다. 산업 표면 결함 검출, 열화된 오토크롬 건판 복원, RGB·이벤트 기반 6DoF 포즈 추정 사례로 데이터 체계와 합성·실제 혼합 학습 전략을 분석하며, 통제 가능한 감독과 학습된 외형을 결합한 하이브리드 파이프라인을 sim-to-real 전이의 방향으로 제시한다.

**코드**: 불명

**태그**: sim2real, industrial-inspection, defect-detection, dataset-benchmark

---

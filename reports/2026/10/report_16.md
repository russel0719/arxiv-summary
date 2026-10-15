# arXiv cs.CV Daily Digest — 2026-10-15 (arXiv 공개일)

- **전체 신규 논문 수**: 143편 (new 114 + cross-list 29)
- **선별 수**: 9편

## 오늘의 트렌드

world model과 action-conditioned 비디오 예측이 가장 두꺼운 군집으로, 메모리·슬롯 구조, 잠재 행동 학습, 롤아웃 가속이 함께 묶인다. MLLM 쪽은 공간 추론 벤치마크와 grounding·agentic 파이프라인이 이어지고, 3D Gaussian Splatting 압축과 feed-forward 재구성이 또 한 덩어리를 이룬다. 인식·표현 쪽에서는 joint-embedding 자기지도 목적함수와 잠재 토크나이저, 산업 결함 검출과 이상 합성이 축을 이룬다.

---

### [Dataset-Level Regularization for Joint-Embedding Self-Supervised Learning](https://arxiv.org/abs/2610.20158)

**한 줄 요약**: 미니배치 안에서만 계산하던 joint-embedding 자기지도 정규화를 CPU에 유지하는 데이터셋 수준 상태로 바꿔, 작은 배치에서도 전체 데이터셋 정규화 그래디언트를 충실히 근사하는 방법.

**핵심 기여**: joint embedding 자기지도 학습은 증강 뷰의 표현을 정렬하면서 표현 분포를 정규화해 붕괴를 막는데, 정규화는 표현 분포 전체를 겨냥하면서도 계산은 현재 미니배치로 제한돼 있다는 문제의식이다. out-of-batch regularization은 데이터셋 수준 상태를 CPU 메모리에 유지하고 전역으로 구성한 인스턴스별 타깃을 미니배치 학습에 사용한다. 자연 이미지와 생물의학 데이터셋에서 이 앵커는 작은 배치일수록 기존 in-batch 추정보다 전체 데이터셋 정규화 그래디언트를 더 충실히 근사하며, 대조(SimCLR)·비대조(SIGReg) 양쪽에서 이미지 분류, 통제된 불균형 하 소수 클래스 성능, instance retrieval, 자기지도 추가 사전학습이 일관되게 개선된다. 논문은 이로써 배치 크기가 정규화의 기하를 바꾸지 않는 최적화 선택이 된다고 주장한다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, image-retrieval, metric-learning

---

### [Generative Representation Learning for Scalable Latent Tokenization](https://arxiv.org/abs/2610.20533)

**한 줄 요약**: 학습된 생성 모델의 조건부 예측 차이로 pointwise mutual information을 분해해 자기지도 표현을 학습하고, 이를 생성 모델의 latent tokenizer로 쓰는 방법.

**핵심 기여**: DINO나 LeJEPA 같은 기존 자기지도 목적은 dimensional collapse와 feature suppression이 일어나는 경우가 있다는 문제의식이다. 제안 목적함수는 데이터의 pointwise mutual information을 인수분해해 표현 손실을 지도하며, 이를 학습된 생성 모델의 조건부 예측 간 정보 차이로 추정한다. 토크나이저와 생성 모델의 결합 FLOP 효율을 분석해 pixel-space 직접 확산 대비 compute-optimal 개선임을 보이고 JiT-L에서 FID-50K 2.18을 얻으며, diffusability에 대한 토크나이저 인코더 스케일링 법칙을 제시해 ImageNet에서 DINOv2보다 7배, 텍스트-이미지 데이터셋 GPIC에서 WebSSL보다 8배 적은 FLOPs로 같은 수준의 표현에 도달한다고 보고한다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, foundation-model, generative

---

### [Train to Stitch: Topology-Preserving Regularization for Interoperable Representations](https://arxiv.org/abs/2610.19401)

**한 줄 요약**: 독립적으로 학습한 두 오토인코더의 잠재 공간을 topology 보존 정규화로 정렬해, 학습 중 조율 없이 인코더와 디코더를 서로 맞물리게 하는 방법.

**핵심 기여**: 오토인코더 기반 압축처럼 인코더와 디코더의 구조를 독립적으로 고르고 따로 학습하면서도 서로 동작하게 하려면 지금은 학습 시 조율이 필요하다는 문제의식이다. 제안 방법은 topological regularization으로 독립 학습된 두 모델의 잠재 공간을 정렬하며, 정규화가 유도하는 구조적 일치가 근사적 기하 호환으로 이어지는 조건부 이론 분석을 함께 제시한다. 여러 데이터셋의 재구성 실험에서 상호운용성 격차가 크게 줄어든다.

**코드**: 불명

**태그**: image-embedding, model-stitching, foundation-model

---

### [Discriminative Score Function: Turning Pretrained Models into Functional Generative Priors](https://arxiv.org/abs/2610.19743)

**한 줄 요약**: 사전학습된 판별 모델의 손실 그래디언트 기하에서 이미지 공간 생성 필드를 뽑아, 재학습 없이 생성·편집·양자화 캘리브레이션에 쓰는 training-free 방법.

**핵심 기여**: 분류·검출·표현학습으로 학습된 판별 모델이 과제 라벨 너머 데이터 매니폴드의 흔적을 내재하고 있는지, 그 흔적을 과제별 guidance 없이 생성 신호로 드러낼 수 있는지를 묻는다. Discriminative Score Function(DSF)은 사전학습 판별 모델의 loss-gradient 기하에서 이미지 공간 생성 필드를 추출해, 재학습이나 과제별 타깃 없이 이미지를 모델 일관 영역으로 옮기는 갱신 규칙을 제공한다. ResNet 분류기, DETR 검출기, DINOv2 ViT 인코더에 적용해 노이즈로부터의 무조건 생성과 조건부 guidance, 편집·인페인팅·설명을 같은 필드로 지원하며, 실제 이미지나 라벨이 없을 때 zero-shot 양자화 캘리브레이션 샘플로 쓰면 data-free 캘리브레이션 기준선보다 특징 기하를 더 잘 보존한다.

**코드**: 불명 (프로젝트 페이지: [junhoo.me/dsf](https://junhoo.me/dsf))

**태그**: training-free, quantization, foundation-model, image-embedding

---

### [Cross-Scenario Industrial Defect Detection via Domain-Robust Training and Metric-Aligned Selection](https://arxiv.org/abs/2610.19540)

**한 줄 요약**: 조명·오염·라인 조건이 바뀌는 산업 기판 결함 검출을 도메인 일반화 문제로 보고, 견고 학습·소결함 학습·점수 캘리브레이션·지표 정렬 체크포인트 선택 네 모듈을 묶은 방법.

**핵심 기여**: 산업 기판 자동 결함 검출은 조명·표면 오염·생산라인 조건이 바뀌어도 신뢰도를 유지해야 하며, 미지 시나리오에서 결함을 검출·위치추정·분류하면서 정상 기판의 오경보를 억제해야 한다는 문제의식이다. IDA 2026 Track 1용으로 cross-scenario robust normalization과 DSU 방식 통계 섭동·점진적 random convolution, NWD와 파라미터 없는 공간 어텐션, VFL 학습 목적, Track 1 지표를 대리 지표로 삼는 SWAD 변형 체크포인트 선택을 결합한다. RTX 4090 한 장에서 테스트셋 Track 1 점수 0.564, screening 점수 0.696을 얻는다.

**코드**: 공개([GZHU-DVL/Dikai](https://github.com/GZHU-DVL/Dikai))

**태그**: defect-detection, industrial-inspection, calibration, object-detection

---

### [CORE: Contrast-and-Reflect for Self-Supervised Prompt Optimization in Anomaly Synthesis](https://arxiv.org/abs/2610.19610)

**한 줄 요약**: 대형 멀티모달 모델의 프롬프트를 자기지도 contrast-and-reflect로 스스로 다듬어, 학습 없이 zero-shot·one-shot 산업 이상 샘플을 합성하는 프레임워크.

**핵심 기여**: 산업 이상 검출은 이상 샘플 부족이 병목이라 고품질 이상 합성이 중요한데, 기존 방법은 희소한 실제 이상 참조나 보조 데이터에 기대고 open-set 상황에서 사실적인 결함을 만들 복잡한 추론·반복 최적화 능력이 없다는 문제의식이다. CORE는 Anomaly Context Grounding 모듈로 희박한 사용자 맥락을 결함 인지 생성 맥락으로 바꾸고, 이를 정상 영역 보존과 이상 변형을 분리하는 구조적 프롬프트로 구체화한 뒤, contrast-and-reflect 자기지도 메커니즘으로 프롬프트를 스스로 정제한다. MVTec-AD와 VisA에서 다양하고 사실적인 이상을 합성해 다운스트림 이상 검출 성능을 개선하며, 과제별 학습 없이 여러 LMM에 그대로 붙는 plug-and-play 구성이다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, training-free, vlm

---

### [TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering](https://arxiv.org/abs/2610.19551)

**한 줄 요약**: 생성된 한자 이미지를 "주어진 목표 문자가 제대로 렌더링됐는가"라는 target-conditioned 판정 문제로 정식화하고, 문자 구조 기술 수열(IDS)을 텍스트 입력으로 쓰는 검증기.

**핵심 기여**: text-to-image 모델이 읽을 수 있는 한자를 만들어도 획이 하나 더 있거나 빠지는 국소 렌더링 결함이 남는데, 인식용으로 학습된 OCR과 비전-언어 모델은 바로 그 구조적 편차에 불변이라 이를 보지 못한다는 문제의식이다. TextVerifier는 문자 하나를 단일 심볼 대신 Ideographic Description Sequence로 텍스트 타워에 넣고, 1,270만 crop-IDS 쌍과 텍스트 영역 인페인팅 모델의 학습 궤적에서 샘플링한 라벨 없는 "같은 문자·다른 품질" hard pair로 학습한다. 위치·정체·정오를 문자 단위로 주석한 7,358자 규모 벤치마크 TextRenderBench-ZH에서 F1 0.844를 기록해 OCR 신뢰도 0.526, 일반 VLM 0.329, TextPecker 0.590을 웃돌며, Flow-GRPO 사후학습의 문자 단위 보상으로 쓰면 렌더링 오류가 더 줄어든다.

**코드**: 불명

**태그**: text-detection, fine-grained, ocr-document, dataset-benchmark

---

### [A Valid Watermark Is Not a Valid Identity: Spatial-Spectral Adversarial Face Evasion with Watermark Preservation](https://arxiv.org/abs/2610.20278)

**한 줄 요약**: 워터마크는 그대로 복원되면서 얼굴 인식 유사도만 떨어뜨리는 black-box 적대적 회피 공격으로, 워터마크 기반 얼굴 인증의 구조적 공백을 드러낸 연구.

**핵심 기여**: 얼굴 이미지 워터마킹은 생체 파이프라인의 추적성과 인증을 뒷받침하지만, 출처나 변조 검출만으로는 생체 신원의 신뢰성이 보장되지 않는다는 문제의식이다. 워터마킹 구성요소에 접근하지 않는 black-box 설정에서, 공간·스펙트럼 보존 항으로 PGD-L_2 섭동을 유도해 픽셀 수준 왜곡과 숨은 워터마크 단서를 건드릴 수 있는 고주파 변화를 억제하면서 얼굴 인식 유사도를 낮춘다. 워터마킹 기법 2종, 얼굴 인식 모델 2종, 데이터셋 2종에서 운영 임계 기준 회피율 92% 이상을 달성하면서 워터마크 복원율은 StegaFormer 93% 이상·FaceSigns 99.7% 이상, epsilon_2=2.0에서 PSNR 47dB 이상을 유지한다. 논문은 이미지가 워터마크상 유효하고 시각적으로 충실하면서도 생체 인식 측면에서는 신뢰할 수 없게 될 수 있음을 지적한다.

**코드**: 불명

**태그**: forgery-detection, face-verification, adversarial-attack, watermarking

---

### [Quantifying Annotation Agreement in Object Detection with Optimal Transport](https://arxiv.org/abs/2610.19912)

**한 줄 요약**: 박스 겹침을 임계로 이진화하지 않고 최적수송 비용으로 주석 집합 간 일치도를 재는 객체 검출 평가 지표.

**핵심 기여**: 모델 검증은 정답으로 취급되는 주석 테스트셋에 의존하지만 주석에는 잡음과 모호성이 있고, 객체 존재·박스 위치·클래스에서 출처마다 판단이 갈린다. 기존 일치도 지표는 박스 겹침을 이진화한 뒤 요약 점수를 내기 때문에 불일치의 정도와 구조를 가린다는 문제의식이다. 제안 지표는 매칭된 박스와 매칭되지 않은 박스 모두에 등급화된 비용을 부여하는 최적수송 기반 측도로, 이론 분석과 함께 제시된다. 실제 주석과 합성으로 교란한 주석 실험에서 일치도의 점진적 변화를 포착하고 임계 기반 지표가 동일하게 채점하는 주석 쌍을 구분하며, 작거나 모호한 객체가 많은 도메인에서 차이가 두드러진다.

**코드**: 불명

**태그**: object-detection, calibration, dataset-benchmark

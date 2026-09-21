# arXiv cs.CV Daily Digest — 2026-09-21 (arXiv 공개일)

- **전체 신규 논문 수**: 98편 (new 74 + cross-list 24)
- **선별 수**: 9편

## 오늘의 트렌드

Gaussian Splatting·SLAM 계열 3D 복원, VLA·world model로 로봇 행동을 잇는 연구, MLLM용 영상 이해 벤치마크가 두꺼운 군집을 이룬다. 방법론으로는 가중치를 동결한 채 프롬프트·앙상블·테스트타임 최적화만으로 분포 변화에 대응하는 설계, diffusion prior를 복원·센싱·편집에 끌어오는 설계가 반복된다. 제조 결함 검사와 주석 불확실성·라벨 오류를 다룬 논문도 함께 올라왔다.

---

### [MAGIC: Marginal-Guided Compression with Optimal Transport for Efficient Visual Document Retrieval](https://arxiv.org/abs/2609.21018)

**한 줄 요약**: ColPali 계열 multi-vector 페이지 임베딩을 재학습 없이 압축하면서, MaxSim 검색이 실제로 쓰는 patch 사용 분포를 두 개의 marginal로 반영하는 optimal transport 압축기.

**핵심 기여**: multi-vector 페이지 임베딩은 patch 단위 근거 매칭을 가능하게 하지만 인덱스 저장 용량과 MaxSim 점수 계산 비용이 크고, 기존 post-hoc 병합은 균일 복원 목적을 쓰기 때문에 late-interaction 검색이 유도하는 희소·비균일 patch 사용과 어긋나 공격적 압축에서 거의 쓰이지 않는 patch를 보존하고 검색 활동을 소수 대표 벡터에 몰아넣는다고 지적한다. MAGIC은 동결된 임베딩에 대해 학습 없이 적용되는 압축기로, MaxSim에서 유도한 압축 대리 목적을 two-marginal entropic optimal transport로 최적화하며, 사용량이 높은 patch를 우선하는 retrieval-demand source marginal과 보존된 facet 사용을 고르게 하는 balanced target marginal을 함께 쓴다. ViDoRe 벤치마크에서 여러 keep ratio와 검색 백본에 걸쳐 기존 post-hoc 압축기를 상회하며 공격적 압축 구간에서 이득이 특히 크고, 구성요소 ablation으로 두 marginal의 상호 보완 효과를 확인한다.

**코드**: 공개([MAGIC](https://github.com/xandery-geek/MAGIC))

**태그**: image-retrieval, image-embedding, training-free, efficient-inference, ocr-document

---

### [Extending Decoupled Attention to Dense Prediction and Masked Training for Multi-Channel Images](https://arxiv.org/abs/2609.21629)

**한 줄 요약**: 채널마다 독립적으로 마스킹된 multi-channel 이미지에서 채널 간 patch 대응을 linear assignment로 복원해, decoupled attention을 표준 masked training 및 dense prediction과 함께 쓸 수 있게 한 정식화.

**핵심 기여**: multi-channel imaging은 각 채널이 색 밴드가 아니라 의미가 다른 신호를 담고 있어, 채널별로 토큰화한 뒤 전체 channel-patch 토큰에 제약 없는 self-attention을 걸면 개별 채널의 특징이 희석된다는 문제를 다룬다. 기존 Decoupled ViT는 채널 내 갱신과 채널 간 갱신을 분리하고 채널별 표현을 먼저 만들어 이를 통제하지만, 토큰을 공간 위치로 짝짓기 때문에 모든 채널에서 동일한 가시 토큰을 요구한다. 제안 정식화는 채널별로 남은 patch 사이의 linear assignment를 풀어 대응을 복원하고, 그 결과 decoupled attention을 제한된 설정이 아닌 표준 masked multi-channel 학습 구성에 결합한다. 형광 현미경·imaging mass cytometry·위성 영상에 걸친 분류 3종과 분할 3종 벤치마크에서, 높은 채널 수의 dense prediction을 포함해 가장 강한 MC-ViT 베이스라인을 상회한다.

**코드**: 불명

**태그**: ssl-backbone, correspondence, segmentation, multi-channel-imaging

---

### [P$^3$-SAM: SAM with Perceptual Parallel Prompt for Few-Shot Strip Steel Surface Defect Segmentation](https://arxiv.org/abs/2609.21424)

**한 줄 요약**: 저대비·조명 불균일·미세 텍스처라는 강판 표면 결함 영상의 특성에 맞춰 SAM의 입력 인코딩과 프롬프트 생성을 함께 바꾼 few-shot 결함 분할 모델.

**핵심 기여**: 강판 표면 결함의 few-shot 분할은 국소 대비가 낮고 조명이 고르지 않으며 텍스처 패턴이 미세해 자연 영상과 성질이 다르고, SAM의 사전학습 표현을 그대로 가져오는 기존 few-shot 분할 방법은 이런 산업 영상 특성 때문에 성능이 떨어진다는 점을 문제로 삼는다. P$^3$-SAM은 두 전략으로 이를 다루는데, Perceptual-Optimized Encoding은 국소 대비를 높이고 결함 분할에 중요한 텍스처 세부를 보존하며, Parallel Prompt Generator는 의미 프롬프트와 공간 프롬프트를 동시에 생성해 영상이 달라져도 SAM 디코더에 함께 제공한다. few-shot 강판 결함 벤치마크 3종에서 최고 성능을 보고하며, Surface Defects-4i에서 mIoU 12.00% 향상을 얻는다.

**코드**: 불명

**태그**: segmentation, defect-detection, industrial-inspection, foundation-model

---

### [Balanced Prompt Adaptation against Entropy-Induced Collapse for Test-Time Binary Segmentation](https://arxiv.org/abs/2609.21743)

**한 줄 요약**: 불균형 이진 분할에서 엔트로피 최소화가 마스크를 붕괴시키는 현상을 이론적으로 짚고, 클래스별 앵커 균형과 텍스트 프롬프트 잔차만 갱신하는 테스트타임 적응 방법.

**핵심 기여**: 엔트로피 최소화는 테스트타임 적응의 표준 목적이지만, dense 분할은 수천 개의 픽셀 예측을 합산하기 때문에 예측 면적이 큰 클래스가 갱신을 지배해 소수 예측을 끌어당기고, 예측이 포화되며 엔트로피 기울기가 사라져 퇴화된 마스크가 나온다고 지적하고 이 붕괴를 shared-shift 모델에서 이론적으로 확립한다. BAPA는 두 모듈을 결합하는데, Class-Balanced Anchors는 예측된 각 클래스에서 고신뢰 앵커를 따로 뽑아 전경과 배경에 동일한 총 손실 가중치를 주고, Dynamic Prompt Adaptation은 예측 갱신마다 앵커를 갱신하면서 vision-language 인코더를 동결한 채 텍스트 측 프롬프트 잔차만 최적화해 사전학습된 dense 시각 표현을 건드리지 않고 전경-배경 결정 경계만 조정한다. 네 도메인 실험에서 비교 방법 중 가장 높은 평균 Dice를 얻고, factorized ablation으로 두 모듈의 역할이 상호 보완적임을 확인한다.

**코드**: 불명

**태그**: segmentation, peft, test-time-adaptation, vlm

---

### [A Principled Approach to Unsupervised Anomaly Detection](https://arxiv.org/abs/2609.21800)

**한 줄 요약**: 비지도 이상탐지를 "관측을 만든 가장 그럴듯한 손상(corruption)을 추론하는" Bayesian 역문제로 재정식화하고, 추론된 손상 파라미터의 에너지를 이상 점수로 쓰는 프레임워크.

**핵심 기여**: 기존 비지도 이상탐지는 정상 분포에서의 이탈을 표시하거나 국소화하는 데 초점을 두어 이상을 만들어낸 생성 기제를 무시하지만, 이상의 성질은 존재 여부만큼 중요하다는 문제의식에서 출발한다. 제안 프레임워크는 각 관측에 대해 가장 확률이 높은 손상을 추론하는 역문제로 문제를 다시 쓰고, 추론된 손상 파라미터의 에너지를 확률적 이상 점수로 삼으며, 기존 여러 방법이 모델링 선택만 다른 동일 에너지 점수의 특수 사례로 유도됨을 보인다. 통제된 설정에서 구성요소를 분석한 뒤 손상 모델을 바꿔 MVTec AD의 object-class AUROC를 2.3% 개선하고, 뇌 MRI 벤치마크에서 검출 성능과 함께 병변의 강도·bias·기하 추정치를 산출한다.

**코드**: 공개([inverse-uad](https://github.com/jgmyles/inverse-uad))

**태그**: anomaly-detection, industrial-inspection, defect-detection

---

### [Hand-Aware Transition Modeling for Bimanual Procedural Anomaly Detection](https://arxiv.org/abs/2609.21207)

**한 줄 요약**: 양손 조립 작업에서 손별 이벤트 전이를 marked temporal point process로 모델링해 의미·시간 surprisal을 손별 이상 사후확률로 바꾸고, 복구 동작에 대한 오경보율을 운영점에서 보고하는 절차 이상탐지 모델.

**핵심 기여**: 양손 조립의 절차 이상탐지는 각 손 동작을 지금까지의 수행 이력에 견주어 판정해야 하며, 교정 동작은 단독으로 보면 이상해 보이고 시각적으로 그럴듯한 동작은 절차 순서를 위반할 수 있다는 점을 문제로 삼는다. HACT는 예측된 손별 이벤트 위의 전이 모델로, 역할을 보존하는 이력으로 두 손의 동시 책임을 유지하고 marked temporal point process로 관측된 전이마다 의미·시간 surprisal을 부여한 뒤, 지도학습 evidence head와 2-state 필터로 이를 손별 이상 사후확률로 변환한다. 예측 이벤트와 참가자 분리 fold 위의 recovery-aware 프로토콜로 검증 참가자에서 고른 운영점에서의 복구 오경보율을 보고하며, 두 전동공구 조립 절차에서 비교 방법 중 가장 높은 AUPRC·F1과 가장 적은 복구 경보를 얻고, 같은 제품의 다른 조립 순서에 재학습 없이 적용해도 최고 AUPRC·F1을 유지한다.

**코드**: 공개([HACT](https://github.com/Kratos-Wen/HACT))

**태그**: anomaly-detection, industrial-inspection, video, calibration

---

### [Morphology-Aware Ambiguity Learning for Wafer Defect Decision Support](https://arxiv.org/abs/2609.21866)

**한 줄 요약**: 웨이퍼 맵 결함을 단일 클래스로 강제하지 않고, 형태가 비슷한 클래스 쌍을 담은 ambiguity matrix로 자동 판정·2클래스 보조 판정·전체 재검토 중 하나로 라우팅하는 학습 프레임워크.

**핵심 기여**: 웨이퍼 맵 결함 인식은 보통 고정 taxonomy의 단일 클래스 분류로 정식화되지만, 클래스 경계 근처의 형태를 보이는 웨이퍼에서는 하나의 예측을 강제하는 것이 그럴듯한 진단 대안을 제시하는 것보다 정보량이 적다는 점을 문제로 삼는다. 제안 프레임워크는 학습 웨이퍼 맵의 방사·각도·기하 특성으로 형태가 유사하고 진단 대안이 될 수 있는 결함 클래스 쌍을 나타내는 클래스 수준 ambiguity matrix를 구성해, 모든 오분류 클래스를 동등하게 취급하는 대신 그럴듯한 대안 클래스를 학습하도록 유도하고, 추론 시 이 matrix로 불확실한 예측을 의미 있는 2클래스 진단 집합으로 표현할지 전체 재검토로 올릴지 결정한다. WM-811K 실험에서 결함 인식과 진단 의사결정 지원 모두 기존 방식을 상회하고, 예시 비용 분석으로 라우팅 전략의 비용 이점을 제시하며, 백본 아키텍처를 바꿔도 진단 거동이 일관됨을 보고한다.

**코드**: 불명

**태그**: industrial-inspection, defect-detection, calibration

---

### [Beyond Exact Match: Task-Aware GRPO for Cross-Domain PCBA Visual Question Answering](https://arxiv.org/abs/2609.21276)

**한 줄 요약**: 규격 기반 샘플과 실제 생산 라인 영상 사이의 도메인 격차를 겨냥해, 선택형·계수형 출력에 맞춘 보상을 쓰는 GRPO와 추론 시 합의·중재를 결합한 PCBA 검사 VQA 프레임워크.

**핵심 기여**: 자동 PCBA 검사에서 규격에 따른 판정은 미세한 시각 단서, 부품 의미, 제조 지식을 함께 추론해야 하는데, 대형 VLM을 쓰려 해도 규격에서 유도된 샘플과 실제 생산 라인 영상 사이의 도메인 이동, 그리고 선택형과 수치 계수형이 섞인 이질적 출력 공간이 배포를 가로막는다고 지적한다. 제안 프레임워크는 규격 유래·실제·보조 PCB 데이터를 하나의 instruction 형식으로 통합하고 시각 근거·질문 의미·후보 선택지·정답에 정렬된 검증된 추론 trace를 구성하며, Task-Aware GRPO로 exact-match 지도를 넘어 선택형에는 다중 구성요소 의미 보상, 계수형에는 거리 인식 보상, 출력 유효성에는 형식 보상을 통합한다. 추론 시에는 선택지 의미 일관성 보정, self-consistency 투표, 다중 모델 중재를 결합하며, PCBA Standard-to-Real Grand Challenge 공식 리더보드에서 Overall Score 83.24를 기록한다.

**코드**: 불명

**태그**: vlm, industrial-inspection, fine-grained

---

### [Object Detection Benchmarks are Incomplete: The Role of Label Errors and Annotation Uncertainty](https://arxiv.org/abs/2609.21822)

**한 줄 요약**: COCO·VOC·Cityscapes·KITTI를 재주석해 누락 주석이 라벨 오류의 주된 원인임을 보이고, 소프트 라벨 기반의 불확실성 인식 검출 벤치마크와 실제 라벨 오류 검출 벤치마크를 제시한 연구.

**핵심 기여**: 객체 검출이 아키텍처와 open-vocabulary 모델로 발전해 왔지만 벤치마크 품질 자체가 주석 불완전성에 의해 제한된다는 증거를 제시한다. 널리 쓰이는 데이터셋 네 종을 재주석하면 주석 객체 수가 크게 늘고(KITTI 최대 +60%, COCO +40%) 그 증가분은 주로 이전에 라벨되지 않은 작고 가려지거나 밀집한 인스턴스에서 오며, 데이터셋별 주석 관례 차이도 일부 있으나 모든 데이터셋에서 누락 주석이 라벨 오류의 주된 원인으로 일관되게 나타난다. 이를 위해 높은 recall을 지향하고 객체당 최소 11명의 주석자로부터 집계한 소프트 라벨로 모호성을 담는 확장 가능한 주석 파이프라인을 도입해, 불확실성 인식 객체 검출 벤치마크와 실제 라벨 오류에 기반한 라벨 오류 검출 벤치마크를 만든다. 벤치마크 성능은 주석 품질에 매우 민감하지만 모델 순위는 대체로 안정적이며, 합성 노이즈에서 잘 동작한다고 보고된 기존 라벨 오류 검출 방법은 실제 라벨 오류에서 높은 recall·precision을 달성하지 못한다.

**코드**: 불명

**태그**: object-detection, dataset-benchmark, calibration

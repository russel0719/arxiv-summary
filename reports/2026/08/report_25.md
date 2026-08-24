# arXiv cs.CV Daily Digest — 2026-08-25 (KST)

- **전체 신규 논문 수**: 103편 (new 82 + cross-list 21)
- **선별 수**: 11편

## 오늘의 트렌드

오늘은 AI 생성 콘텐츠 판별(forgery detection)이 두드러진 하루다. 이미지 레벨(LoRC), 픽셀 레벨 조작 위치 추정(GAP-SAM), 비디오의 물리적 일관성 기반 판별(MotionPhys), 설명 가능한 deepfake 탐지까지 서로 다른 각도의 접근이 동시에 나왔고, 공통적으로 unseen generator에 대한 일반화를 강조한다. SSL 백본 쪽에서는 JEPA 계열의 변형이 계속 이어지는 가운데, 인물 중심 비디오 사전학습으로 pose·re-identification을 동시에 잡는 Human-JEPA가 주목할 만하다. 그 외 DINOv2를 교사로 쓰는 cross-domain detection 증류, training-free 멀티모달 re-ranking, VLM 기반 anomaly scoring의 readout 설계 문제 등 foundation model을 실무에 붙이는 기법 논문이 고르게 분포했다.

---

### [Human-JEPA: A Human-Centric Vision Model that Perceives and Anticipates](https://arxiv.org/abs/2608.21160)

**한 줄 요약**: 인물 중심 비디오에서 anchored forecasting으로 사전학습해 정적 인식과 미래 예측을 한 모델로 해결하는 human-centric JEPA 백본.

**핵심 기여**: 기존 human-centric 백본은 이미지 사전학습이라 motion·anticipation을 다루지 못하는데, Human-JEPA는 비디오에서 past-to-future split 예측으로 학습하되 dense target을 초기화 모델의 frozen copy에 고정(anchored)해 dense perception의 붕괴를 막는다. 무작위 block masking 대신 순수 과거→미래 분할을 써서 action 성능 5점 하락과 re-identification 17점 붕괴 문제를 회피했다. Frozen probe 기준으로 pose와 person re-identification에서 픽셀 앵커 기반 전문 모델을 2.7배 적은 파라미터로 능가한다.

**태그**: ssl-backbone, re-identification, image-embedding, pose, video

---

### [EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking](https://arxiv.org/abs/2608.20886)

**한 줄 요약**: 멀티모달 검색 쿼리를 6개 semantic slot의 구조화된 제약(evidence package)으로 파싱해 검증 방식으로 재랭킹하는 training-free 프레임워크.

**핵심 기여**: "이 셔츠를 핑크색으로" 같은 합성적 쿼리를 opaque embedding이나 hallucination이 잦은 free-form CoT 대신, entity·attribute·relation 등 6개 슬롯의 required/forbidden/ignorable 제약으로 명시 파싱한 뒤 rubric 기반 결정적 채점과 listwise 비교로 재랭킹한다. text-to-image, image-to-image, composed retrieval 5개 벤치마크에서 SOTA를 달성했고, 구조화된 evidence를 supervision으로 써서 경량 student를 증류하면 교사 성능의 90% 이상을 훨씬 낮은 비용으로 유지한다. 검색 시스템의 재랭킹 단계에 바로 붙일 수 있는 실용적 설계다.

**태그**: image-retrieval, vlm, distillation, metric-learning

---

### [Semantically Compatible Knowledge Distillation for Cross-Domain Object Detection with Vision Foundation Models](https://arxiv.org/abs/2608.20916)

**한 줄 요약**: DINOv2에 경량 SLE Adapter를 붙여 student detector와 공간·의미적으로 호환되는 dense feature를 만들어 도메인 적응 detection을 증류하는 프레임워크.

**핵심 기여**: VFM 교사와 student detector 간 feature map의 spatial-scale 불일치가 feature alignment와 pseudo-label 학습을 모두 약화시킨다는 점을 지적하고, DINOv2에 local-texture prior를 주입하는 SLE Adapter로 이를 해소한다. DINOv2-B 교사만으로 훨씬 큰 DINOv2-G 교사와 경쟁하거나 능가하는 성능을 내며 3개 DAOD 벤치마크에서 SOTA를 달성했다. Foundation model을 작은 detector로 옮기는 실무 증류 파이프라인 설계에 참고 가치가 크다.

**태그**: distillation, object-detection, foundation-model, ssl-backbone

---

### [LoRC: Detecting AI-Generated Images via Low-Rank Collapse in Semantic Residuals](https://arxiv.org/abs/2608.20882)

**한 줄 요약**: 생성모델이 semantic-residual 직교 부분공간에서 보이는 low-rank collapse를 아키텍처 불문 시그니처로 삼는 AI 생성 이미지 탐지법.

**핵심 기여**: 최신 생성기가 semantic 방향은 잘 보존하지만 그 직교 잔차 공간에서 rank 퇴화(구조적 평탄화)를 보이며, 이것이 디코딩 최종 단계에서 아키텍처 공통으로 발생하는 병목임을 기하학적으로 규명했다. 이 시그니처를 포착하는 LoRC는 여러 벤치마크에서 평균 7.0% 정확도 향상을 보였고, 특히 학습에 없던 39개 unseen generator에서 97.0% 정확도를 달성해 cross-model 일반화가 뛰어나다. 실서비스 위조 판별에서 가장 중요한 미지 생성기 대응력을 원리 수준에서 확보한 점이 강점이다.

**태그**: forgery-detection, foundation-model, image-embedding

---

### [GAP-SAM: A Global Artifact Prior for Generalizable AI-Generated Image Manipulation Localization](https://arxiv.org/abs/2608.20929)

**한 줄 요약**: 이미지와 frozen VAE 재구성본에서 뽑은 global artifact token을 SAM3에 주입해 semantic boundary shortcut 없이 조작 영역을 찾는 localization 모델.

**핵심 기여**: 픽셀 supervision이 forensic 증거와 데이터셋 고유의 mask 기하를 뒤섞어 OOD 성능을 떨어뜨리고, fine-tuned segmentation 모델이 실제 조작 경계 대신 물체 윤곽에 달라붙는 boundary adhesion 문제를 짚었다. 공간 영역을 직접 지정하지 않는 global artifact token을 zero-gated FiLM으로 SAM3 feature pyramid에 주입해 이를 억제한다. 6개 데이터셋 평균 Pixel-F1 79.8로 기존 최강 대비 12.6점 앞서고, JPEG 압축·blur·resize 등 모든 열화 강도에서 최고 성능을 유지해 실환경 강건성이 좋다.

**태그**: forgery-detection, segmentation, foundation-model

---

### [MotionPhys: Detecting AI-Generated Videos via Physical Consistency of Optical-Flow Trajectories](https://arxiv.org/abs/2608.20770)

**한 줄 요약**: 외관 artifact 대신 optical-flow 궤적의 물리적 일관성을 증거로 삼는 경량·해석 가능한 AI 생성 비디오 탐지 프레임워크.

**핵심 기여**: 생성 비디오가 짧은 구간에서는 시각적으로 그럴듯해도 완결된 물체 동작 전체에서는 관성·연속적 힘·궤적 기하 같은 물리 제약을 지키지 못해 궤적 통계에 체계적 불일치가 남는다는 관찰에서 출발한다. Sparse motion trajectory의 기하학적 변화를 다중 시간 스케일로 모델링해 compact한 표현으로 변환하며, generator별 trace에 의존하지 않아 다양한 비디오 생성기에 잘 일반화된다. 외관 기반 탐지와 상호 보완적이라 앙상블 구성 요소로도 유용하다.

**태그**: forgery-detection, video, efficient-inference

---

### [Explainable Deepfake Detection with Feature-robust Augmentation and Evidence-grounded Explanation Optimization](https://arxiv.org/abs/2608.20913)

**한 줄 요약**: 열화 강건 augmentation + contrastive 학습으로 탐지를, 증거 기반 preference optimization으로 설명의 사실성을 잡은 explainable deepfake 탐지 프레임워크.

**핵심 기여**: 저화질 샘플에서의 성능 붕괴와 설명 모델의 hallucination이라는 두 실무 문제를 겨냥한다. 열화 인지형 augmentation에 supervised contrastive learning과 mean-teacher 구조를 결합해 augmentation에 따른 feature drift를 억제하고, 증거 누락·무관 정보 주입으로 만든 rejected 샘플과의 chosen-rejected 쌍으로 preference optimization을 수행해 설명이 실제 조작 흔적에 근거하도록 유도한다. 포렌식 분석가에게 판단 근거를 제시해야 하는 서비스 시나리오에 직접적으로 유용하다.

**태그**: forgery-detection, vlm, metric-learning

---

### [Breaking High Confidence: Practical Face Impersonation under High-Security Thresholds](https://arxiv.org/abs/2608.20884)

**한 줄 요약**: 고보안 threshold와 엄격한 rate limit 하에서도 성공하는 최초의 score-based 얼굴 인식 impersonation 공격.

**핵심 기여**: 기존 얼굴 인식 시스템 보안 분석이 중간 수준 threshold에 머물렀던 것과 달리, 고보안 설정에서의 공격 파이프라인 각 단계 gap을 수학적으로 분석하고 실용적 공격을 설계했다. LFW에서 신원당 confidence score 조회 100회 예산만으로 Amazon Rekognition의 threshold 99(법집행 권장 설정)에 대해 92% 이상의 impersonation 성공률을 달성했다. 얼굴 verification 기반 인증 서비스를 운영·설계하는 입장에서 방어 요건을 재점검하게 하는 결과다.

**태그**: re-identification, forgery-detection, metric-learning

---

### [A VLM Answer Is Not an Anomaly Score: Rank Compression in Training-Free Video Anomaly Detection](https://arxiv.org/abs/2608.21244)

**한 줄 요약**: VLM 기반 training-free anomaly detection에서 생성 답변 대신 답변 확률분포를 읽어내면 rank compression이 사라져 5~13점 향상된다는 분석.

**핵심 기여**: VLM으로 anomaly score를 얻을 때 최빈 답변 하나만 쓰는 generated readout은 세그먼트 간 상대 순서를 뭉개는 rank compression을 일으킨다는 것을 규명했다(91개 답변 스케일에서도 실제로는 4~18개의 distinct score만 생성). 허용 답변 전체의 확률분포를 쓰는 probability readout은 4개의 7~8B VLM, 모든 벤치마크·metric 조합에서 일관되게 우수하며 AUROC/AP 기준 평균 5~13점 개선된다. VLM을 scoring에 쓰는 모든 파이프라인(검사·이상탐지)에 바로 적용 가능한 저비용 교훈이다.

**태그**: anomaly-detection, vlm, industrial-inspection, video

---

### [Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs](https://arxiv.org/abs/2608.21134)

**한 줄 요약**: 모델 스스로 생성한 데이터로 캘리브레이션하는 2.7-bit VLM 양자화 포맷으로 Llama 3.2 11B Vision을 3.7GB까지 압축.

**핵심 기여**: 원 학습 셋업에 접근하지 않고 모델 자신이 생성한 데이터를 양자화 학습에 쓰는 파이프라인과, Arm CPU에서 효율적으로 실행되는 새로운 2.7-bit-per-parameter 포맷을 제안했다. Llama 3.2 11B Vision Instruct를 8-bit activation과 함께 3.7GB로 압축하면서 표준 VQA 태스크 성능을 유지한다. 모바일·엣지에서 VLM을 서빙해야 하는 배포 시나리오의 실용적 레퍼런스다.

**태그**: quantization, vlm, efficient-inference, foundation-model

---

### [ES-VP: Energy-Shaped Dynamic Visual Prompting for Efficient Model Adaptation](https://arxiv.org/abs/2608.21194)

**한 줄 요약**: 보조 네트워크 없이 pre-trained 모델 자체로 이미지별 prompt를 생성하는 low-rank + energy-guided visual prompting 적응 기법.

**핵심 기여**: 고정 prompt의 경직성과 보조 네트워크 기반 동적 prompt의 파라미터 증가·overfitting이라는 기존 VP의 trade-off를, low-rank 초기화와 energy-guided 동적 적응으로 해소한다. 5개 아키텍처, 15개 데이터셋에서 기존 single/diverse VP SOTA를 일관되게 능가하며, CLIP 기준 DAM-VP 대비 평균 2.6% 정확도 향상을 더 적은 파라미터로 달성했다. Frozen backbone을 다운스트림에 붙이는 PEFT 옵션으로 검토할 만하다.

**태그**: peft, foundation-model, efficient-inference


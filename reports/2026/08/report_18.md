# arXiv cs.CV Daily Digest — 2026-08-18 (KST)

- **전체 신규 논문 수**: 89편 (new 67 + cross-list 22)
- **선별 수**: 9편

## 오늘의 트렌드

오늘 목록은 생성모델(diffusion T2I·video, world model, 3D Gaussian splatting)과 VLM/MLLM 추론,
의료·원격탐사·자율주행 응용이 수적으로 압도한다. 표현학습·매칭·검증 관점에서 건질 만한 흐름은
세 갈래다. 첫째, foundation model을 **학습 없이 또는 최소 비용으로 적응**시키는 계열이 두드러진다
— training-free inference operator, source-free test-time adaptation, closed-form weight injection,
특권 정보 없는 self-supervised distillation이 한꺼번에 나왔다. 둘째, 얼굴·모핑 등 **검증/위조 탐지**에서
feature-space 유사도 변화나 CLIP 의미 정렬을 단서로 쓰는 접근이 여럿 보인다. 셋째, frozen 임베딩이
실제로 스타일을 이해하는지 개체를 외우는지 **평가 프로토콜을 재검토**하는 비판적 연구가 등장해
retrieval/metric-learning 평가 설계에 시사점을 준다.

---

### [Self-Supervised Visual On-Policy Distillation](https://arxiv.org/abs/2608.14144)

- **한 줄 요약**: teacher에 특권 정보를 더하는 대신 **학생 입력에서 정보를 빼서** 비대칭을 만들어, 별도 teacher·라벨·보상 없이 on-policy distillation을 수행한다.
- **핵심 기여**: 원본 이미지에 조건화된 teacher 분포를, 같은 이미지의 강증강 뷰에 조건화된 student로 on-policy distill하는 S²VOPD를 제안한다. 비대칭이 핵심이며(대칭 self-distill은 오히려 성능을 떨어뜨림), 증강 강도는 중간이 최적이고, 질문 관련 시각 증거를 완전히 지우면 학습 신호가 무의미해진다는 설계 원칙을 도출했다. 6개 fine-grained perception 벤치마크에서 4B 모델을 70.7→77.4%로 끌어올려, 특권 정보를 쓰는 방법이 얻는 개선의 96%를 데이터 추가 없이 회복했다.
- **태그**: ssl-backbone, distillation, fine-grained, foundation-model

---

### [Style or Signature? Artist-Disjoint Evaluation of Style Classification in Frozen Vision Embeddings](https://arxiv.org/abs/2608.14435)

- **한 줄 요약**: frozen CLIP/SSL 임베딩의 미술 스타일 분류 정확도가 진짜 "스타일 이해"인지 "화가(개체) 식별"인지 artist-disjoint 프로토콜로 재검증한다.
- **핵심 기여**: 같은 화가 작품이 train/test 양쪽에 섞이는 random split이 개체 인식만으로 성능을 부풀림을 지적한다. 화가 단위로 hold-out하면 5-NN 스타일 정확도가 0.87→0.77로 떨어지고, 하락폭이 사조별로 크게 불균등하다(초현실주의 20점 급락, 인상주의·큐비즘은 거의 불변). 언어 없는 vision-only SSL 모델을 포함한 4개 인코더에서 패턴이 일관돼, 효과가 언어가 아닌 시각 구조에 기인함을 보인다.
- **태그**: image-embedding, image-retrieval, ssl-backbone, metric-learning, fine-grained

---

### [AlignFace: Human-Aligned Face Similarity Metric with Interpretable Concept Relations](https://arxiv.org/abs/2608.14130)

- **한 줄 요약**: 인지심리학의 얼굴 유사도 원리(featural/configural 속성, 비선형 반응, own-group bias)를 반영해 인간 지각과 정렬된 **해석가능 얼굴 유사도 metric**.
- **핵심 기여**: 얼굴 이미지쌍과 텍스트 속성을 VLM으로 인코딩하고, gated cross-attention으로 속성별 차이 표현을 추출한 뒤, concept bottleneck으로 해석가능 속성에 추론을 제약하고 neural GAM으로 비선형 영향을 모델링한다. FACETS 데이터셋을 함께 제안하며, 최신 domain-free 학습형 지각 metric을 포함한 기준선 대비 인간 하위집단 지각과의 정렬을 크게 개선했다.
- **태그**: metric-learning, re-identification, image-embedding, fine-grained, vlm

---

### [Face Re-morphing: Differential Morphing Attack Detection via Feature-Space Similarity Changes](https://arxiv.org/abs/2608.13858)

- **한 줄 요약**: 문서 이미지에 morphing을 한 번 더 가했을 때의 **feature-space 유사도 변화량**을 위조(모핑) 탐지 단서로 사용하는 differential MAD.
- **핵심 기여**: 문서–라이브 코사인 유사도와 라이브–재모핑 유사도의 변화를 탐지 점수로 쓴다. 정적 feature 차이·구성얼굴 복원·다중단서 융합에 의존하는 기존 D-MAD와 달리, 추가 morphing 연산에 대한 feature-space 응답 자체를 단서화한 것이 핵심이다. FRLL-Morphs·FEI Morph에서 다양한 모핑 조건·재모핑 방법·얼굴인식 모델에 걸쳐 효과적이고 보완적임을 확인했다.
- **태그**: forgery-detection, re-identification, metric-learning, image-embedding

---

### [CMCNet: Aligning Ultrasound Image Embeddings with Textual TI-RADS Representations for Fine-Grained Thyroid Classification](https://arxiv.org/abs/2608.13939)

- **한 줄 요약**: 표준화된 특징 설명의 **고정 텍스트 임베딩에 이미지 임베딩을 Center-Margin Contrastive로 정렬**해, 추론 시 이미지만으로 fine-grained 등급을 예측한다.
- **핵심 기여**: 구조화된 특징 설명에서 얻은 텍스트 임베딩이 위험 등급의 안정적 대리 표현이 됨을 보이고, intra-class 응집과 inter-class 분리를 동시에 촉진하는 center-margin contrastive loss로 이미지→고정 텍스트 임베딩 정렬을 학습한다. 직접 multitask 학습보다 데이터 효율·강건성이 높고, InfoNCE·center loss·강한 multitask·VQA형 멀티모달을 특히 불균형 상황에서 능가했다(초음파 도메인 검증이나 기법은 일반적).
- **태그**: metric-learning, image-embedding, fine-grained, vlm

---

### [XSA-MAD: Cross-modal Semantic Alignment for Morphing Attack Detection](https://arxiv.org/abs/2608.13861)

- **한 줄 요약**: 모핑 개념을 identity·기하·텍스처·일관성 4속성의 구조화된 텍스트로 표현하고 **CLIP 이미지 인코더를 이 텍스트 공간에 점진 정렬**해, 미지의 생성기법에 일반화되는 모핑 탐지.
- **핵심 기여**: 시각 단서만 쓰는 기존 image-based MAD가 unseen 생성기법에 약하다는 점을 지적하고, bona-fide와 모핑 얼굴의 의미적 불일치를 명시적으로 모델링한다. 속성 인식 텍스트 표현과의 정렬로 생성-불변·개념 수준의 차이를 포착한다. SMDD로 학습 후 MAD22·MorDIFF에서 다양한 모핑 원리에 강하게 일반화하며, GAN 기반 모핑에서 EER 2.92%를 달성했다.
- **태그**: forgery-detection, vlm, foundation-model, image-embedding

---

### [Rethinking Auxiliary Modalities in Multimodal Zero-shot Anomaly Detection: From Semantic Fusion to Conditional Modulation](https://arxiv.org/abs/2608.13973)

- **한 줄 요약**: 보조 모달리티를 공유 의미공간에 융합하지 않고, RGB 이미지-텍스트 매칭 경로는 보존한 채 보조 관측을 **RGB feature 정제의 조건 신호로만** 쓰는 plug-and-play zero-shot anomaly detection.
- **핵심 기여**: 직접 융합이 RGB foundation model의 텍스트 정렬 이상(anomaly) 의미를 교란한다는 문제를 지적한다. 경량 meta-learning 모듈이 전역 RGB·보조 표현으로 샘플적응 low-rank residual 업데이트를 생성하고, 불확실성 인식 공간 변조로 국소 업데이트를 강화/억제해 원 RGB 이상 의미를 보존하면서 선택적으로 보강한다. MVTec 3D-AD·Eyecandies에서 여러 RGB 기반 ZSAD 탐지기를 일관 개선하며 SOTA를 달성했다.
- **태그**: anomaly-detection, defect-detection, foundation-model, peft

---

### [PISA: A Pseudo-Individual Source-Domain Feature Adaptation Framework for Test-Time Open-Vocabulary Object Detection](https://arxiv.org/abs/2608.14142)

- **한 줄 요약**: 소스 데이터 없이 **CLIP 시각 feature의 corruption 불변성**을 활용해 pseudo-individual 소스 도메인 feature를 복원, 도메인 시프트 하 open-vocab 검출 성능 저하를 test-time에 회복한다.
- **핵심 기여**: 재스코어링/의사라벨 자기학습에 기대는 기존 source-free OVOD-TTA가 초기 예측이 나쁘면 크게 무너지는 점을 지적한다. Corruption-Invariant Feature Extractor로 CLIP 시각 feature의 손상 불변성을 활용하고, Feature Alignment·multi-scale alignment로 이를 원 소스 도메인에 가까운 dense feature로 변환해 불안정한 의사라벨 대신 supervision으로 쓴다. 손상된 VOC-C·COCO-C·LVIS-C에서 소스 데이터 없이 SOTA(COCO-C AP@50 +3.92%)를 달성했다.
- **태그**: open-vocab-detection, object-detection, foundation-model, domain-adaptation

---

### [CAST: Closed-form Analytic Semantic Transfer for Zero-Shot Classifier Extension](https://arxiv.org/abs/2608.13751)

- **한 줄 요약**: 학습·이미지 없이 텍스트 의미정보만으로 사전학습 분류기에 미지 클래스를 **weight injection으로 추가**하는 closed-form zero-shot 확장 프레임워크.
- **핵심 기여**: 반복 최적화·타깃 분포 예시 없이 새 클래스로 분류기를 확장한다. 이론적 근거와 함께 semantic extrapolation residual ρ_u라는 계산가능·모델 불가지 지표를 유도해 데이터셋 큐레이션·벤치마크 설계의 원칙적 기준을 제시한다. 표준 ZSL 벤치마크에서 기존 image-free 기법을 매칭/능가하고 few-shot 적응 성능에 근접한다.
- **태그**: zero-shot, foundation-model, image-embedding, fine-grained

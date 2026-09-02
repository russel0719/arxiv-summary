# arXiv cs.CV Daily Digest — 2026-09-02 (arXiv 공개일)

- **전체 신규 논문 수**: 152편 (new 116 + cross-list 36)
- **선별 수**: 11편

## 오늘의 트렌드

목록에서 가장 큰 축은 VLM·MLLM의 실패 양상을 진단하는 논문들이다. 시각 근거를 쓰지 않고 언어 prior로 답하는 현상(Beyond Language Priors, The Visual Insensitivity Gap), attention 설명의 충실성(Visual Attention Faithfulness), ego-motion·스케일·물리 추론의 결손(Dyn-3D, MeRoPE 이전 단계의 metric reasoning 논문들), 그리고 conformal·introspective 신호로 사실성을 보증하려는 시도(IntroConformal, Reliability Challenges in Diffusion VLM)가 함께 몰려 있다. 두 번째 축은 MLLM 추론 비용 절감으로, visual token pruning(SinkPruner, S$^2$Prune, RaDiCal)과 speculative decoding·토큰 표현 부호화(GLANCE, Compressing AI Traffic)가 각각 토큰 선택 기준과 디코딩 경로를 겨냥한다. 생성 쪽에서는 flow matching의 이론적 재정리와 응용이 두드러지고(A Lagrangian View of Flow Matching, ReBridge-Flow, ReFlowSET, CQF-HMR), 4D world model과 카메라 제어 비디오 생성(Streaming4D, H3-World, MeRoPE, ZimaBlue)이 별도 군집을 이룬다. 표현학습 계열에서는 self-supervised 사전학습의 목적함수를 다시 손보는 논문(ViTAMINS의 합성 hard negative, cross-view completion의 co-visibility 신호)과 학습된 표현을 layer-wise로 해부하는 probing 논문(V-JEPA 2·VideoMAE-v2 spatiotemporal probing, CLIP modality gap 분석)이 나란히 등장한다. 얼굴 도메인은 임베딩 해석·저품질 인식·쌍둥이 verification·위조 판별로 하루치에 네 편 이상이 모였고, 응용 군집은 의료 영상(보고서 생성·분할·염색 정규화)과 원격탐사/UAV(산불·산사태·초분광)가 각각 20편 안팎으로 가장 두껍다. 그 밖에 벤치마크·감사 성격의 논문(OOD, OCR 조합 일반화, 차량 속성, 스케일 추론)이 전체에서 상당한 비중을 차지한다.

---

### [ViTAMINS: An Empirical Study of Training Self-Supervised Vision Transformers with Synthetic Hard Negatives](https://arxiv.org/abs/2609.01041)

**한 줄 요약**: 합성 hard negative를 contrastive ViT 사전학습에 통합해 표현 품질을 끌어올린 self-supervised 백본 학습 연구.

**핵심 기여**: SSL 백본 학습의 주류가 generative·self-distillation 계열로 옮겨간 상황에서, contrastive learning이 더 단순하면서도 강한 대안일 수 있는지를 다시 검토한다. 기존 contrastive 프레임워크에 합성 hard negative를 넣는 간단한 변경만 적용하고 ImageNet 분류, transfer learning, image retrieval, copy detection, 이미지·비디오 분할에 걸쳐 벤치마크한다. 제안한 negative가 표현 안에 이미지의 semantic content를 명시적으로 담는 emergent property를 낳아 baseline 대비 최대 +11.3%의 분류 성능을 보이고, ViT-B가 ViT-L 규모의 V-JEPA를 앞서면서 자원 효율도 더 높다고 보고한다.

**태그**: ssl-backbone, image-embedding, image-retrieval, metric-learning, foundation-model

---

### [Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison](https://arxiv.org/abs/2609.01530)

**한 줄 요약**: cross-view 재구성 오차를 masked autoencoder 오차와 비교해 co-visibility 신호를 스스로 만들어내는 self-supervised 사전학습 Gekko.

**핵심 기여**: cross-view completion은 이미지쌍의 co-visible 영역에서 강한 특징을 학습하지만, 비-co-visible 패치에서는 참조 뷰가 재구성에 거의 정보를 주지 못해 사실상 monocular 학습 신호만 남는다. Gekko는 cross-view 재구성 오차가 MAE 오차 대비 얼마나 개선되는지를 co-visibility의 self-supervised proxy로 삼아, cross-view completion·masked autoencoding·이 상대 개선량의 픽셀 단위 예측을 하나의 네트워크에서 처음부터 함께 학습하며 3D ground truth를 요구하지 않는다. 동일 구조·동일 학습 데이터 조건에서 CroCo를 zero-shot correspondence estimation, relative pose estimation, pointmap regression 전부에서 앞서고, 가장 엄격한 relative-pose 임계값에서 최대 6배 높은 정확도와 ETH3D end-point error 22% 감소를 기록한다. 추가 학습된 채널 자체가 미지 장면에서 co-visibility detector로 동작하고, 동결 특징이 동급 이상 크기의 공개 cross-view 백본을 능가하며, 3D 전처리 없이 raw video에서 stride 기반 curriculum으로도 학습된다. 코드와 사전학습 모델이 공개돼 있다.

**태그**: ssl-backbone, correspondence, feature-matching, pose, foundation-model

---

### [CrossFeat: Bridging Imaging Modalities in Feature Descriptor Space](https://arxiv.org/abs/2609.00272)

**한 줄 요약**: 기존 monomodal keypoint descriptor를 그대로 두고 descriptor 공간의 변환 함수만 학습해 이종 모달리티 간 매칭을 가능하게 한다.

**핵심 기여**: keypoint description 연구는 대부분 시점·조명·대비 변화만 다루는 monomodal 설정에 머물러 있고, multispectral·RGB-depth·위성·의료 영상처럼 센싱 과정이 근본적으로 다른 이미지 간 매칭은 모달리티 쌍마다 descriptor를 재학습하거나 대형 모델을 써서 런타임을 크게 늘리는 방식으로 대응해 왔다. CrossFeat은 한 모달리티의 특징을 다른 모달리티와 호환되는 표현으로 옮기는 crossing function을 descriptor 공간에서 학습하고, geometry-appearance disentanglement을 도입해 원 descriptor가 담은 기하 정보는 유지하면서 appearance만 변경한다. 여러 도메인과 데이터셋 실험에서 multimodal 매칭 성능이 향상됨을 보인다.

**태그**: feature-matching, correspondence, image-embedding

---

### [Unmasking Face Embeddings: Reading, Rendering and Naming with Foundation Models](https://arxiv.org/abs/2609.00411)

**한 줄 요약**: 선형 변환 하나로 face recognition 임베딩을 foundation model 임베딩 공간에 연결해, 텍스트 질의 검색·얼굴 이미지 복원·이름 식별을 추가 학습 없이 수행한다.

**핵심 기여**: FR 모델의 identity 임베딩은 생체 매칭에는 매우 효과적이지만 의미적 해석이 거의 불가능한 반면, 광범위한 시각·비전-언어 태스크로 사전학습된 foundation model은 기술·검색·생성·조직화 인터페이스를 제공한다는 대비에서 출발한다. 임베딩 호환성 연구를 이어받아, 쌍으로 확보한 임베딩만으로 추정한 사전 계산 선형 변환으로 기존 FR 모델과 off-the-shelf foundation model을 연결하며 두 모델 어느 쪽도 수정하거나 학습하지 않는다. 정렬된 face 임베딩은 자연어로 읽혀 FR 임베딩 갤러리에 자유형 텍스트 질의를 걸 수 있고, 수정 없는 diffusion decoder를 통해 인물의 외형을 복원하는 얼굴 이미지로 렌더링되며, 등록된 얼굴 갤러리가 없는 상황에서도 이름으로 변환해 식별이 가능하다. 논문은 이 상호운용성이 해석성·검색·복원과 함께 template security에 직접적 함의를 갖는다고 정리한다.

**태그**: image-embedding, image-retrieval, re-identification, foundation-model

---

### [When Modality Gap Reduction Fails: Prediction-Level Hubness in CLIP](https://arxiv.org/abs/2609.01103)

**한 줄 요약**: CLIP의 modality gap을 줄이는 보정이 zero-shot 정확도를 항상 개선하지 못하는 이유를 예측이 소수 클래스로 몰리는 prediction-level hubness로 설명한다.

**핵심 기여**: 이미지·텍스트 표현 간 modality gap 축소는 cross-modal alignment와 downstream 성능을 개선할 것으로 널리 기대되지만, 평균 image-text gap이 작아지는 것이 일관된 정확도 향상으로 이어지지는 않는다. 논문은 zero-shot 분류를 가장 유사한 클래스 텍스트 prototype을 고르는 결정 구조로 보고, 정확도가 평균 alignment뿐 아니라 클래스별 decision margin에도 의존한다는 관점에서 해석 가능한 Linear correction을 사례로 gap 보정이 클래스 간 상대적 결정 구조를 바꿔 예측을 소수 클래스 부분집합에 집중시킬 수 있음을 보인다. 여러 데이터셋 실험에서 Linear correction과 학습 기반 보정 모두 정확도 하락이 예측 집중도 증가와 일관되게 동반되며, gap 보정은 평균 alignment만이 아니라 downstream 예측 구조에 대한 영향으로 함께 평가돼야 한다고 제안한다.

**태그**: image-embedding, vlm, metric-learning

---

### [From Saliency to Discriminability: Rank-Preserving Visual Token Pruning for VLM Rerankers](https://arxiv.org/abs/2609.00667)

**한 줄 요약**: attention saliency가 순위 기여도와 어긋난다는 관찰에서, attention entropy로 saliency 신뢰 구간을 판별해 VLM reranker의 visual token을 학습 없이 pruning한다.

**핵심 기여**: listwise reranker로 쓰이는 대형 VLM은 질의당 수십 개 후보의 visual token을 함께 처리해야 해 token pruning이 배포의 전제조건인데, 기존 saliency 기준이 고르는 시각적으로 두드러진 토큰은 후보 간 공유되는 order-neutral 패턴을 담는 경우가 많아 순위 기여도와 체계적으로 불일치한다. 논문은 이 불일치가 레이어 의존적이고 normalized attention entropy가 신뢰도 전환을 진단한다는 점(Pearson r=0.87)을 보인 뒤, entropy로 saliency를 믿을 시점을 판단해 attention-free rank-discriminative prior와 융합하고 같은 지표로 pruning 레이어까지 선택하는 학습 불필요 프레임워크 RaDiCal을 제안한다. 세 검색 벤치마크와 복수 VLM 구조에서 토큰 20% 예산으로 Flickr30K의 Dense MRR@10을 따라잡고 MSCOCO에서는 이를 넘어서며, FashionIQ에서 모든 pruning 기법 중 1위, 10% 유지 조건에서도 Flickr30K·MSCOCO 1.2pp 이내를 지킨다. FLOPs를 39~45% 줄이고 두 VLM 구조에서 1.28~1.45배 실측 가속을 데이터셋별 재튜닝 없이 얻는다.

**태그**: image-retrieval, vlm, efficient-inference, foundation-model

---

### [Low-Quality Face Recognition using Center Aligned Representations and Local Margin Constraints](https://arxiv.org/abs/2609.01014)

**한 줄 요약**: 샘플 난이도 기반 margin, 저랭크 attention 어댑터, 품질 게이팅을 결합해 하나의 모델로 저품질부터 고품질까지 전 구간 얼굴인식을 처리한다.

**핵심 기여**: 최근 FR 모델은 고품질 영상에서 잘 동작하지만 SNR이 극히 낮은 저품질 이미지에서 정확도가 크게 떨어지고, 저품질 데이터로 fine-tuning하면 고품질 일반화를 희생하는 상충이 여러 품질 수준을 아우르는 최근 평가 설정에서 더 두드러진다. 제안 프레임워크는 모델의 판별 지형에서 샘플별 난이도를 직접 추정하는 Local Probability Margin, 선택된 transformer 레이어 내부에 self-attention을 심은 저랭크 어댑터 Nested Attention Module, off-the-shelf 화질 추정기가 테스트 시 어댑터 기여도를 조절하는 Quality Gating Protocol 세 요소로 구성된다. 감시 영상(TinyFace, SurvFace)과 표준(IJB-B, IJB-C) 벤치마크에서 identification과 verification 모두 일관된 향상을 보고하며, 코드와 모델을 공개할 예정이라고 밝혔다.

**태그**: re-identification, metric-learning, peft, image-embedding

---

### [Revisiting Face Recognition for Monozygotic Twins: The Celeb Twins Test Set](https://arxiv.org/abs/2609.01141)

**한 줄 요약**: 일란성 쌍둥이 80세트의 얼굴 이미지쌍 테스트셋을 구성해, 현재 매처가 피부 표식이나 좌우 비대칭 단서를 활용하지 않음을 보인다.

**핵심 기여**: 일란성 쌍둥이 얼굴인식 연구는 facial mark와 mirror asymmetry를 정확도 개선의 단서로 지목해 왔지만, 이를 검증할 메타데이터를 갖춘 테스트셋이 없었다. Celeb Twins Test Set(CTTS)은 유명인 쌍둥이 80세트의 웹 수집 이미지쌍을 LFW·CALFW·CPLFW·CFP-FP·AgeDB-30 같은 verification 테스트셋 형식으로 정리하고, 구별 가능한 피부 표식과 mirror asymmetry 가능성에 대한 메타데이터를 함께 제공하는 유일한 쌍둥이 테스트셋이라고 밝힌다. 현행 deep CNN 매처는 CTTS의 동일인/타인 이미지쌍 분류에서 76% 이상 정확도를 얻지만 피부 표식이나 비대칭을 사용하지 않음을 보이고 그 이유를 논의하며, Grok·ChatGPT·Gemini 같은 생성 AI 도구로 가상의 일란성 쌍둥이 이미지를 만들어 학습셋 내 쌍둥이 표현을 늘리는 방안의 타당성을 함께 다룬다.

**태그**: fine-grained, re-identification, dataset-benchmark

---

### [Benchmarking Spatial, Spectral, and Self-Supervised Cues for Face Forgery Detection under Realistic Degradation](https://arxiv.org/abs/2609.01511)

**한 줄 요약**: 열화 조건을 포함한 얼굴 위조 판별 벤치마크에서 동결 DINOv3에 선형 헤드만 얹은 구성이 열화 분할 최고 성능을 낸다.

**핵심 기여**: 얼굴 위조 판별기는 통제된 벤치마크에서 강한 결과를 내지만 현실적인 이미지 열화 하에서의 신뢰도는 여전히 제한적이다. MFFI 데이터셋으로 clean·degraded 분할을 나눈 표준 벤치마크를 만들고, CNN·transformer·동결 DINOv3 백본을 포함한 여섯 모델 계열을 spatial·spectral·hybrid 입력 표현에 걸쳐 비교한다. clean 성능이 압축·리사이즈·블러 하 견고성의 지표가 되지 못하며, Xception+RGB가 clean에서 mean ROC-AUC 0.884로 최고인 반면 선형 분류 헤드만 학습한 동결 DINOv3가 degraded 분할에서 mean ROC-AUC 0.726으로 가장 강하다. Fourier 도메인 단서는 RGB와 결합할 때 가장 유용하고 순수 spectral 입력은 일관되게 spatial보다 낮으며, attribution map은 convolutional 판별기가 국소 artifact에, DINOv3는 더 넓은 얼굴 구조에 반응함을 시사한다. 소스 코드가 공개돼 있다.

**태그**: forgery-detection, ssl-backbone, foundation-model, dataset-benchmark

---

### [SAM3-LoRA: Parameter-Efficient Adaptation of a Concept-Promptable Foundation Model for Multi-Class Structural Defect Segmentation](https://arxiv.org/abs/2609.00469)

**한 줄 요약**: SAM3에 LoRA를 붙여 구조물 결함 다중 클래스 분할에 적응시키고, positive prompt만으로 학습할 때 발생하는 presence 예측 붕괴를 hard-negative prompting으로 막는다.

**핵심 기여**: SAM3처럼 open-vocabulary 텍스트 concept를 받아 일치하는 모든 인스턴스를 반환하는 promptable 분할 모델은 전체 fine-tuning 비용이 커서, 정작 이득이 큰 조직들이 특화 도메인에 적응시키기 어렵다. 논문은 COCO 형식 클래스 라벨 인스턴스 분할 데이터에서 카테고리 이름 자체를 프롬프트로 사용해 prompt template·동의어 확장·학습된 클래스 임베딩 없이 concept-promptable 모델을 감독하는 절차를 제시하고, 통상적 어노테이션 파일이 positive prompt만 제공하기 때문에 presence 예측이 텍스트 조건과 분리돼 어떤 프롬프트에도 반응하는 붕괴가 발생하며 이것이 positive prompt만으로 계산한 모든 지표에서 보이지 않는다는 실패 양상을 지적한다. 이미지에 없는 데이터셋 카테고리 전부를 zero-detection 질의로 내보내는 exhaustive hard-negative prompting으로 이를 어노테이션 비용 없이 해결하고, 파라미터의 0.121%와 1.341%를 갱신하는 두 어댑터 배치를 동일 프로토콜로 비교한다. 자체 구축 터널 라이닝 데이터셋에서 pixel IoU가 0.017에서 0.338로, instance recall이 0.375에서 0.672로 올랐고, 공개 Structural Defects Dataset에서는 0.017에서 0.855, 0.574에서 1.000으로 올라 두 데이터셋 열 개 지표에서 방향이 일치했다.

**태그**: segmentation, peft, defect-detection, industrial-inspection, foundation-model

---

### [Vision-Language-Guided Pseudo-Labels for Unsupervised Domain Adaptation in Semantic Segmentation for Waste Sorting](https://arxiv.org/abs/2609.00898)

**한 줄 요약**: SAM의 클래스 무관 영역 제안과 EVA-CLIP의 region-text 유사도로 pseudo-label을 만들어, 타깃 도메인 라벨 없이 분할 모델을 도메인 적응시킨다.

**핵심 기여**: 산업 폐기물 선별처럼 실제 적용 환경에서 semantic segmentation 라벨을 확보하는 비용이 크고 규모 확장이 사실상 불가능하다는 문제에서 출발한다. SAM이 클래스 무관 영역 제안을 생성하고 EVA-CLIP이 region-text 유사도로 semantic 라벨을 부여한 뒤 confidence filtering으로 신뢰 가능한 pseudo-label만 self-training에 사용하는 cross-modal 파이프라인을 구성하고, 선택적 확장으로 모호한 영역에는 BLIP의 언어 기반 검증을 덧붙여 파이프라인 구조를 바꾸지 않고 pseudo-label 품질을 높인다. synthetic-to-real 자율주행과 lab-to-factory 산업 폐기물 선별 두 도메인 변화에서 source-only baseline 대비 일관된 향상을 얻으며, 도메인 변화 하 self-training에서는 pseudo-label의 양보다 품질이 결정적 요인이라고 보고한다.

**태그**: segmentation, industrial-inspection, foundation-model, vlm

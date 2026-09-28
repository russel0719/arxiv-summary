# arXiv cs.CV Daily Digest — 2026-09-24 (arXiv 공개일)

- **전체 신규 논문 수**: 128편 (new 106 + cross-list 22)
- **선별 수**: 12편

## 오늘의 트렌드

3D Gaussian Splatting 기반 복원·렌더링, vision-language-action과 world model로 로봇 행동을 잇는 연구, 의료영상 foundation model, 원격탐사 변화탐지·grounding이 두꺼운 군집을 이룬다. 방법론으로는 동결된 foundation model에 깊이·기하 같은 보조 신호를 주입하거나 추론 시점 보정만으로 성능을 끌어올리는 설계, diffusion prior를 복원·합성에 끌어오는 설계가 반복된다. 표현 구조와 평가 프로토콜 자체를 다시 측정하는 분석 논문도 함께 올라왔다.

---

### [Two Global Crops Suffice: Locating Semantic Emergence in DINO-Style Self-Supervised Learning](https://arxiv.org/abs/2609.28187)

**한 줄 요약**: DINO 계열의 의미 표현이 어느 학습 목적에서 생기는지 통제된 재학습으로 분해해, 기하적으로 다른 두 global view 간 일관성이 그 근원임을 보인 실증 분석.

**핵심 기여**: DINO 계열 self-supervised ViT가 보이는 emergent 의미 표현의 발생 기제가 불분명하다는 문제에서 출발해, DINO 계열 목적함수를 구성요소별로 분리해 재학습하는 통제 실험을 수행한다. 같은 이미지의 기하적으로 구별되는 global view 사이의 일관성 강제가 의미 표현의 앵커 역할을 하며, patch 단위 masking 목적(iBOT)은 이 global alignment와 함께 학습될 때만 의미를 강화한다 — 즉 기존 의미 구조를 정교화·조밀화할 뿐 독립적으로 만들어내지는 않는다는 결과를 보고한다. 반면 local-to-global view alignment는 동일 연산량 기준에서 순수 global alignment 대비 의미 품질을 크게 개선하지 않았다. 평가 축에 대해서도, 표준 검증 지표인 분류 정확도보다 semantic correspondence가 downstream 성능을 더 안정적으로 예측한다고 주장한다.

**코드**: 불명

**태그**: ssl-backbone, correspondence, image-embedding, foundation-model

---

### [MINER: Multi-crop INference-time Enhancement for Rare-Object Retrieval with Frozen Dual Encoders](https://arxiv.org/abs/2609.27142)

**한 줄 요약**: 동결된 dual encoder의 global 임베딩에 region 임베딩 뱅크와 hubness 보정 재채점을 붙여, 혼잡한 장면 속 작은 객체 질의의 text-to-image 검색을 학습 없이 개선하는 추론 프레임워크.

**핵심 기여**: 질의가 혼잡한 장면 안의 작고 부수적인 객체를 지목할 때 단일 global 이미지 임베딩이 국소 시각 근거를 과소표현해 검색 성능이 떨어진다는 문제를 다룬다. MINER는 학습이 필요 없는 추론 단계 기법으로, 동결된 dual encoder의 global 임베딩에 소규모 region 임베딩 뱅크를 추가하고 hubness를 보정하는 유사도 재채점을 적용해 global pooling이 낮게 반영하던 근거를 복원한다. 평가를 위해 Flickr30K·MS COCO의 고혼잡 부분집합을 낮은 salience 객체 하나를 지목하도록 재캡션한 ROCS 벤치마크를 함께 제안하며, CLIP·SigLIP·SigLIP 2 모든 백본에서 ROCS와 표준 split 양쪽의 검색 성능이 향상됐다고 보고한다. 분석에 따르면 이득은 정밀한 crop 위치보다 넓은 공간 커버리지에서 주로 나온다.

**코드**: 공개([MINER](https://github.com/aalquwayfili/MINER) · 데이터셋 [ROCS](https://huggingface.co/datasets/aalquwayfili/ROCS))

**태그**: image-retrieval, image-embedding, training-free, foundation-model

---

### [Geometry-Conditioned Visual Place Recognition in Natural Environments](https://arxiv.org/abs/2609.27370)

**한 줄 요약**: depth 센서 없이 geometric foundation model이 추론한 기하로 vision foundation model의 토큰 표현을 채널 단위 조건화하는 증류 기법(DAD)을 자연 환경 place recognition에 적용한 연구.

**핵심 기여**: 자연 환경의 visual place recognition은 반복적인 식생, 희소한 랜드마크, 주행 간 외관·시점 변화 때문에 어렵지만 같은 장소의 공간 구조는 외관보다 지속적이라는 관찰에서 출발한다. Depth-Aware Distillation(DAD)은 기하를 별도 입력 모달리티로 다루는 대신, geometric foundation model이 추정한 이미지 정합 깊이를 vision foundation model의 토큰 공간으로 투영해 채널 단위로 시각 표현을 선택적으로 변조하며, 두 단계 teacher-guided 학습으로 먼저 사전학습된 외관 공간에 앵커링한 뒤 장소 판별용으로 정교화한다. WildCross 벤치마크에서 외관만 쓰는 대응 베이스라인 대비 시퀀스 간 평균 Recall@1을 61.41%에서 66.37%로, Recall@5를 65.86%에서 72.49%로 높였고, 역방향 주행과 장기 외관 변화 구간에서 이득이 가장 컸다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, distillation, foundation-model, depth

---

### [Depth-Guided Contrastive Learning for 2D Representations with 3D Spatial Awareness](https://arxiv.org/abs/2609.28159)

**한 줄 요약**: 깊이로 얻은 3D 근접성을 대조 유사도로 변환해, 기존 contrastive 프레임워크에 끼워 넣을 수 있는 보조 목적함수.

**핵심 기여**: 표준 contrastive learning은 주로 의미 관점에서 설계돼 있어 2D 표현이 3D 공간 구조를 보존하도록 유도하지 못한다는 문제를 지적한다. DGCL은 깊이를 이용해 3D 공간에서 가까운 픽셀이 더 유사한 표현을 갖도록 강제하되, 절대 깊이 값 대신 무작위 표본 픽셀 간 상대 3D 거리 비교로 감독 신호를 구성해 깊이 스케일에 불변이고 계산이 가벼우며 기존 프레임워크에 통합하기 쉽게 만든다. 여러 데이터셋과 모델에 걸쳐 2D 표현학습이 일관되게 개선되고 공간·기하 이해가 필요한 의미 downstream 과제에서 이득이 있었다고 보고한다.

**코드**: 공개([DGCL](https://github.com/LeungTsang/DGCL))

**태그**: ssl-backbone, image-embedding, metric-learning, depth

---

### [Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces](https://arxiv.org/abs/2609.27988)

**한 줄 요약**: ViT 특징 공간의 거리로 코사인·유클리드 대신 디코더 Jacobian에서 유도한 pullback metric을 저랭크로 학습하고, 그 학습 가능성을 미리 판정하는 진단량을 제시한 연구.

**핵심 기여**: ViT 특징 공간을 다루는 방법들이 모든 방향이 동등하다고 가정하는 유클리드 거리·코사인 유사도에 의존한다는 점을 문제로 삼고, 과제 민감 기하를 디코더 출력의 Jacobian으로 정의한 pullback metric $g(F)=J(F)^\top J(F)$로 규정한다. 전체 metric 저장이나 dense 출력에서의 Jacobian 형성이 비현실적이므로, 적은 수의 Jacobian-vector product로 계산되는 matrix-free 진단량 $\kappa_{cap}(r)$로 모델-디코더 쌍마다 저랭크 근사 가능 여부를 판정하고, 가능한 쌍에는 randomized power iteration으로 저랭크 metric을 학습하는 Spectral Pullback Network(SPN)를 학습한 뒤 310K 파라미터 토큰 중요도 헤드로 증류한다. DPT·DINOv2·CLIP·VGGT 백본에서 $\kappa_{cap}(r)$이 어떤 학습 metric 구조가 가능한지 예측했고, 중요도 헤드는 DINOv2 CLS에서 Spearman $\rho=0.998$, 기하 기반 토큰 pruning은 ViT 미세조정 없이 prune ratio 0.5에서 ToMe 기반 토큰 선택의 추가 depth 오차를 25% 줄였다. Jacobian 스펙트럼이 너무 퍼져 저랭크 근사가 어려운 경우에는 디코더 입력 특징을 VAE 병목에 통과시켜 다룰 수 있다고 덧붙인다.

**코드**: 공개([TaskInducedViTs](https://github.com/abond19/TaskInducedViTs/))

**태그**: metric-learning, image-embedding, foundation-model, efficient-inference, distillation

---

### [Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM](https://arxiv.org/abs/2609.27509)

**한 줄 요약**: 특징점을 버리는 대신 의미·panoptic·모션 prior를 대응 비용으로 환산해 연속적으로 가중하는 feature matching 확장.

**핵심 기여**: 지역 descriptor 기반 stereo visual SLAM은 의미 모호성, 인스턴스 혼동, 독립 운동 객체가 데이터 결합을 훼손해 궤적 드리프트로 누적되는데, 기존 semantic·dynamic SLAM은 이를 이진 특징 거부로 처리해 대응 밀도를 희생한다는 점을 문제로 삼는다. KYS-SLAM은 ORB-SLAM3의 모듈식 확장으로, 맥락적 비개연성을 배제 기준이 아닌 등급화된 양으로 보고 특징 매칭 단계에서 대응 비용을 변조하며 기하 백엔드는 수정하지 않는다 — 각 키포인트에 의미·panoptic·모션 prior를 계층적 호환성 정식화로 융합하고, 배경 optical flow에 깊이 인지 ego-motion 모델을 맞춰 자기 보정 임계로 panoptic 세그먼트를 분류하는 학습 불필요 모듈에서 모션 점수를 얻는다. 시퀀스·데이터셋별 계수 재조정 없이 단일 설정으로 21개 stereo 시퀀스에서 KITTI ATE RMSE 17.4%, EuRoC 27.7% 감소를 회귀 없이 달성했고, KITTI Tracking 동적 부분집합에서 6.6%, Virtual KITTI 2에서 17.8%(최대 31.2%)를 줄였다.

**코드**: 불명

**태그**: feature-matching, correspondence, segmentation, training-free

---

### [What Converges in the Platonic Representation Hypothesis? Structure over Geometry](https://arxiv.org/abs/2609.27252)

**한 줄 요약**: 표현 수렴 논쟁에서 국소/전역이라는 구조 스케일과 관계 구조/계량 기하라는 비교 대상을 2×2로 분리해, 수렴하는 것은 관계 구조 쪽임을 보인 분석.

**핵심 기여**: Platonic Representation Hypothesis를 국소 이웃 관계로 좁힌 선행 연구가 구조 스케일(국소 대 전역)과 비교 대상(어떤 표본이 관계되는지를 뜻하는 관계 구조 대 거리·유사도 같은 계량 기하)을 혼동했다고 지적한다. 이를 분리하기 위해 두 요인을 국소·전역 스케일에서 각각 평가하는 통제된 2×2 프레임워크를 구성하고, mutual $k$-nearest neighbors의 전역 대응물로 $H_0$ skeleton overlap과 거리 인지 변형을 도입한다. vision-language 모델 전반에서 관계 구조는 보정 후 두 스케일 모두에서 견고한 수렴을 보인 반면, 거리 일치를 엄격하게 요구할수록 정렬이 약해지고 용량 의존 추세가 평탄해졌으며, Riemannian metric 근사 하에서의 거리 일치 평가와 video-text 표현에서도 같은 패턴이 재현됐다.

**코드**: 불명

**태그**: image-embedding, foundation-model, vlm, metric-learning

---

### [Diverse by Design: Architectural Constraints for Prototype-Based Interpretability](https://arxiv.org/abs/2609.27194)

**한 줄 요약**: 명시적 정규화 대신 attention head와 prototype을 일대일로 묶는 구조적 제약으로 prototype 다양성을 강제하고, Coverage·Diversity 지표로 정량 평가한 fine-grained 분류 모델.

**핵심 기여**: prototype 기반 신경망은 사례 기반 추론으로 내재적 해석가능성을 제공하지만 prototype이 중복된 특징으로 수렴하고 다양한 의미 부위를 포착하지 못하며 해석가능성의 정량 평가가 없다는 한계를 지적한다. DAPL은 multi-head self-attention에서 attention-prototype을 엄격히 일대일로 대응시키는 구조적 제약으로 각 prototype이 서로 다른 시각 특징에 특화되도록 하고, foreground-aware 학습으로 prototype을 의미 있는 영역에 집중시키며, Coverage와 Diversity라는 평가 지표를 함께 제시한다. CUB-200-2011에서 foreground-aware 학습을 적용한 DAPL이 정확도 81.69%, Coverage 0.596, Diversity 0.427을 기록했다.

**코드**: 공개([DAPL](https://github.com/xinmiaolin/DAPL))

**태그**: fine-grained, image-embedding, interpretability

---

### [Damnatio Memoriae: Adversarially and Selectively Forgetting Identities in the Embedding Space of Face Recognition Models](https://arxiv.org/abs/2609.27115)

**한 줄 요약**: 모델을 나머지 인구에 대해 계속 쓰면서 선택한 신원만 서로 다른 촬영 간 연결 불가능하게 만드는 임베딩 공간 조작 손실함수 세 가지.

**핵심 기여**: 얼굴인식 모델은 임베딩 유사도가 운영 임계를 넘을 때 두 촬영의 동일인을 연결하는데, 학습에 없던 신원도 인식하므로 이미지를 지우고 재학습해도 선택적 망각이 되지 않는다는 점을 open-set adversarial forgetting 문제로 정식화한다. 한 신원의 임베딩을 중심에서 흩뜨리는 손실 하나와, 각 이미지를 분류 헤드로 학습하거나 거의 정규직교인 프레임으로 미리 고정한 개별 근직교 타깃에 사상하는 손실 둘을 제안하고, 각 신원 이미지 일부에 대해 분류 목적과 함께 미세조정한다. 검증·식별 과제에서 선행 4개 방법과 두 가지 망각 규모, 세 백본에 걸쳐 비교했으며, 임베딩 기하에 작용하는 모든 손실이 대상 신원을 거의 식별 불가능하게 만들고 그중 정규직교 프레임만으로도 강한 망각이 성립해 해당 부분집합의 이미지가 비교에 들어오는 모든 경우에 유지되며 서로 다른 망각 신원 간에도 연결 불가능성이 유지된다고 보고한다.

**코드**: 불명

**태그**: re-identification, image-embedding, metric-learning, machine-unlearning

---

### [Pro-Bench: Prompt-Robust Open-Vocabulary Visual Grounding Across Real-World Heterogeneous Environments](https://arxiv.org/abs/2609.27076)

**한 줄 요약**: 실제 로봇 운용 환경 5종에서 수집한 13k 프레임에 8가지 의미 유형의 질의를 붙여, open-vocabulary grounding 모델 16개 구성의 프롬프트 강건성을 zero-shot으로 측정한 벤치마크.

**핵심 기여**: 기존 open-vocabulary grounding 벤치마크가 짧은 카테고리 라벨과 웹 수집 이미지에 의존해 실제 배치 조건에서 다양한 질의와 시각 조건을 견디는지 알 수 없다는 문제를 제기한다. Pro-Bench는 지하·산업·실내·실외·도심의 독립 로봇 도메인에서 얻은 13k+ RGB 프레임에 74.5k 수작업 인스턴스 주석과 범주·속성·관계·affordance·상태·부분전체·부정·합성 의미를 아우르는 515개 타깃 질의를 붙였고, 16개 모델 구성을 엄격한 zero-shot 추론으로 IoU 임계별 위치추정 정확도, 종단간 추론 지연, 프롬프트 유발 성능 변동, 타깃 재현 일관성 기준으로 측정한다. 프롬프트 강건성이 구조에 크게 의존해 16개 중 10개 구성이 짧은 카테고리 라벨에서 가장 좋고 자유형 질의가 최고 정확도를 주는 구성은 하나뿐이었으며, 비슷한 총계 mAP가 질의 재구성 간 일관된 타깃 재현의 큰 차이를 가릴 수 있음을 보인다.

**코드**: 공개([Pro-Bench](https://pro-bench.github.io/))

**태그**: open-vocab-detection, dataset-benchmark, vlm, object-detection

---

### [TEEP-RCNN: Texture-Enhanced Edge-aware Perception for Steel Surface Defect Detection via Improved Convolutional Block Attention in Faster R-CNN](https://arxiv.org/abs/2609.28077)

**한 줄 요약**: CBAM에 dropout·batch normalization을 추가하고 차등 학습률과 TTA+WBF 추론 보정을 결합한 강재 표면 결함 2단계 검출기.

**핵심 기여**: 강재 표면 결함 검출은 클래스 간 텍스처 차이가 미묘하고 클래스 불균형이 심하다는 점을 문제로 삼는다. TEEP-RCNN은 FPN 백본을 쓰는 Faster R-CNN 위에 개선된 CBAM을 얹어 채널 attention MLP에 dropout 정규화를, 공간 attention 분기에 batch normalization을 추가해 공적응을 줄이고 게이팅 로짓을 안정화하며, 사전학습 ResNet-101 백본과 검출 헤드의 갱신 속도를 분리한 차등 학습률과 cosine annealing warm-up으로 학습하고, 추론에서는 Test-Time Augmentation을 Weighted Box Fusion으로 융합해 길쭉하거나 경계에 붙은 결함의 위치 안정성을 높인다. NEU-DET 6개 결함 범주에서 단일 GPU·10 epoch 학습만으로 mAP@50 73.3%, mAP@50-95 37.9%를 기록해 100 epoch을 쓴 YOLOv11m(mAP@50 76.2%)에 근접했고 rolled-in-scale 범주에서는 COCO 지표 기준으로 앞섰다. 공간 attention 분기는 patches·scratches 같은 길쭉한 텍스처 결함에서 가장 효과적이었고, 비국소적으로 분포하는 crazing은 두 방식 모두에서 미해결로 남았다.

**코드**: 불명

**태그**: industrial-inspection, defect-detection, object-detection

---

### [RAMP: Robust Adaptive Mixed-Precision Quantization for Edge CPU Vision Models](https://arxiv.org/abs/2609.28262)

**한 줄 요약**: 층별 INT8 양자화 민감도 지표 13종을 네 모델·두 ARM64 플랫폼에서 실측 비교해, Jensen-Shannon Divergence와 K-Means 임계 결정을 결합한 할당 정책을 제시한 연구.

**핵심 기여**: mixed-precision 양자화는 층 유형마다 영향이 달라 정확도 손실이 최소이고 지연 감소가 최대인 지점을 찾아야 하는데, 널리 쓰이는 민감도 지표들이 최신 구조에서 체계적으로 실패한다는 점을 문제로 삼는다. 네 개의 서로 다른 신경망에 대해 층별 INT8 양자화 민감도 지표 13종을 실증 비교하고 결과 정책을 두 ARM64 플랫폼에서 검증한 결과, gradient 기반 방법은 8개 모델-하드웨어 조합 중 4개에서, weight 통계 기반은 2개에서 실패한 반면 Jensen-Shannon Divergence는 치명적 실패가 없었다. 지표만으로는 정책이 결정되지 않고 통상 쓰는 고정 임계가 편향된 분포에서 취약하므로 K-Means 클러스터링으로 임계를 정해 거의 무손실 정확도와 full-precision 대비 평균 1.81배 속도 향상을 얻었으며, 속도 이득이 미미한 층을 민감도와 무관하게 양자화에서 제외하면 계산 그래프가 파편화돼 연산자 융합이 막히므로 역효과가 날 수 있다는 점도 보고한다. GPU 접근이나 gradient 계산 없이 적용되는 정책이다.

**코드**: 불명

**태그**: quantization, efficient-inference, edge-deployment

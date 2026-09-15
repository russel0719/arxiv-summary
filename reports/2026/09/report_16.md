# arXiv cs.CV Daily Digest — 2026-09-15 (arXiv 공개일)

- **전체 신규 논문 수**: 233편 (new 195 + cross-list 38)
- **선별 수**: 11편

## 오늘의 트렌드

의료 영상(분할·리포트 생성·모달리티 변환)이 가장 두꺼운 군집이고, 장영상 이해·GUI 에이전트·affordance 등 VLM 벤치마크, Gaussian Splatting·SLAM·feed-forward 재구성 등 3D 계열, AI 생성 이미지·오디오-비디오 탐지와 포렌식, 원격탐사·항공 소형 객체 검출이 뒤따른다. 방법론으로는 동결 foundation model 위에 경량 모듈을 얹는 구성, wavelet·주파수 단서 결합, 물리 기반 시뮬레이션·검증, 누출 통제·반사실 설계로 기존 평가 프로토콜을 재검토하는 흐름이 반복된다.

---

### [Diffusion Trajectory Modeling for Semantic Correspondence](https://arxiv.org/abs/2609.15357)

**한 줄 요약**: diffusion 모델의 중간 feature를 특정 timestep의 정적 스냅숏이 아니라 spatial patch별 시간 궤적(trajectory)으로 해석하고, 그 궤적을 모델링해 semantic correspondence를 구하는 프레임워크.

**핵심 기여**: diffusion 과정의 중간 feature map이 풍부한 시각 표현을 담아 여러 downstream 과제에 쓰이지만, 기존 접근은 특정 timestep의 단일 feature map을 쓰거나 여러 timestep의 feature를 집계하는 데 머물러 있다는 점에서 출발한다. 각 spatial patch의 표현이 생성 과정 전체에 걸쳐 점진적으로 진화하며 정적 스냅숏으로는 포착하기 어려운 의미를 담는다는 관찰에 근거해, Diffusion Trajectory Modeling(DTM)은 여러 timestep에 걸친 patch별 표현 변화를 하나의 궤적으로 보고 이를 대응 추정에 활용한다. 공간적으로 대응하는 patch들이 diffusion 과정 전반에서 유사한 궤적 패턴을 형성함을 실증해 시간 축이 의미 정보를 지닌다고 보인다. SPair-71k, SPair-U, AP-10K에서 강한 성능을 보고하며, 정량 수치는 초록에 제시되지 않는다. BMVC 2026 채택 논문이다.

**코드**: 불명

**태그**: correspondence, feature-matching, generative, image-embedding

---

### [PACE: Progressive Angular-to-Norm Contrastive Embedding](https://arxiv.org/abs/2609.15152)

**한 줄 요약**: cosine 대조 목적과 low-rank adaptation으로 각도 기하를 먼저 안정화한 뒤 dot-product 유사도와 full fine-tuning으로 전환해, embedding 방향과 norm이 함께 의미를 인코딩하도록 하는 2단계 멀티모달 임베딩 학습 프레임워크.

**핵심 기여**: 대부분의 멀티모달 임베딩 모델은 cosine 기반 대조 목적으로 학습되어 안정적이지만 의미 호환성이 각도 기하에 묶여 embedding norm을 추가 의미 신호로 쓸 수 없고, 반대로 각도와 norm을 모두 쓰는 dot-product 유사도를 직접 최적화하면 성능이 떨어지고 학습이 불안정하다는 문제를 제기한다. 이 차이를 최적화 공간의 조기 확장에 따른 angular-norm entanglement와 directional anisotropy로 진단하고, full-parameter fine-tuning이 이를 악화시킨다고 분석한다. PACE는 Stage I에서 cosine 목적과 low-rank adaptation으로 제한된 공간 안에서 신뢰할 수 있는 각도 기하를 세우고, Stage II에서 dot-product 유사도와 full-parameter fine-tuning으로 전환해 표현 공간과 학습 파라미터 공간을 점진적으로 확장한다. 또한 positive 검색 신뢰도가 높은 query의 가중치를 낮추고 경쟁 negative가 있는 모호한 query를 강조하는 confidence-adaptive 목적인 Focal Embedding Loss를 도입한다. 여러 backbone 규모와 다양한 멀티모달 임베딩 과제에서 일관된 효과를 보고하며, 정량 수치는 초록에 제시되지 않는다.

**코드**: 불명

**태그**: image-embedding, metric-learning, image-retrieval, vlm, peft

---

### [Learning Continuous Source Responses For Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2609.14316)

**한 줄 요약**: AI 생성 이미지 판별의 backbone 적응을 이진 분류 대신 실제-생성 혼합 비율 회귀로 재정식화하고, 압축된 source-response 부분공간으로 분류기의 shortcut 단서 접근을 제한해 cross-generator 일반화를 높인 CuRe.

**핵심 기여**: 기존 AI 생성 이미지 판별기는 in-domain에서는 잘 동작하지만 강건성과 cross-generator 일반화가 제한되며, 그 원인으로 shortcut 단서 과적합이 지목되어 왔다. 여러 방법이 shortcut 학습 억제를 시도했지만 대부분 이진 분류라는 학습 과제 자체가 표현을 어떻게 형성하는지는 재고하지 않았다는 점을 문제로 삼는다. CuRe는 backbone 적응을 real-generated mixing ratio의 회귀로 바꿔 이진 양 끝점 분리를 넘어 진위 관련 변화를 포착하는 더 세밀한 지도를 제공하고, compact한 source-response subspace를 선택해 nuisance 변동을 억제하면서 최종 분류기가 잠재적 shortcut 단서에 접근하는 것을 제한한다. 10개 공개 벤치마크에서 평균 balanced accuracy 89.7%로 2위 방법을 5.2%p 앞서고, 여러 시각 backbone에서 일관된 일반화 이득과 일반적인 이미지 열화에 대한 강건성을 보고한다.

**코드**: 공개([CuRe](https://github.com/manic-cui/CuRe))

**태그**: forgery-detection, foundation-model, image-embedding

---

### [Lightweight Generalized DeepFake Face Detection with WAVIE: Wavelet Augmented Vision Intermediate Embeddings](https://arxiv.org/abs/2609.14437)

**한 줄 요약**: 동결 CLIP backbone의 중간 transformer embedding을 경량 모듈로 투영한 뒤 3-level Daubechies-6 DWT로 저주파 branch만 정제하고 고주파는 보존해 재구성하는, 미학습 조작 기법에 일반화되는 경량 deepfake 얼굴 판별기.

**핵심 기여**: deepfake 판별기는 학습한 forgery 방식에서는 잘 동작하지만 미학습 조작 파이프라인에서 정확도가 급락해 실제 멀티미디어 환경에서의 신뢰성이 제한된다는 문제에서 출발한다. WAVIE는 frozen CLIP 위에서 중간 transformer embedding을 학습 가능한 경량 모듈로 투영하고, 3-level db6 discrete wavelet transform을 적용해 저주파 branch를 정제하면서 고주파 branch는 보존한 뒤 inverse DWT로 feature를 재구성해 분류하는 end-to-end 구조로 공간·주파수 단서를 결합한다. FaceForensics++만으로 학습해 frame-level AUROC가 Celeb-DF-v1 0.852, Celeb-DF-v2 0.852, WildDeepFake 0.831로 여러 일반화 베이스라인을 상회하며, ablation에서 wavelet 모듈과 중간 feature 집계가 cross-dataset 성능에 모두 필요함을 확인한다. IEEE SMC 2026 채택 논문이다.

**코드**: 불명

**태그**: forgery-detection, foundation-model, efficient-inference

---

### [Beyond Natural Images: Rethinking AI-Generated Image Detection in Documents](https://arxiv.org/abs/2609.14352)

**한 줄 요약**: AI 생성 문서 이미지에서 기존 판별기의 성능 저하를 진단 벤치마크로 드러내고, 지역 간 아티팩트 불일치와 텍스트 밀도 의존이라는 문서 고유 특성을 분석한 뒤 다중 생성·편집 모델로 만든 대규모 문서 중심 데이터셋 AIGDoc을 구축한 연구.

**핵심 기여**: AI 생성 이미지 판별 평가가 자연 이미지에 집중되어 청구서·경비 보고서·증명서·의료 기록처럼 민감한 상황에 등장하는 문서 이미지는 거의 다뤄지지 않았다는 점을 문제로 삼는다. 통제된 진단 벤치마크 AIGDoc-Pilot에서 기존 판별기의 mean AUC가 7% 이상 하락함을 보이고, 그 배경으로 생성 아티팩트가 지역 간에 강한 공간적 불일치를 보인다는 점과 텍스트 밀도가 실제-합성 분리성에 크게 영향을 미쳐 text-dense 영역이 더 강한 판별 증거를 제공한다는 두 특성을 밝힌다. 이에 기반해 다양한 실제 문서와 여러 최신 생성·편집 모델로 만든 합성 문서로 구성된 더 큰 데이터셋 AIGDoc을 구축한다. AIGDoc 실험에서 기존 판별기는 여전히 AI 생성 문서를 안정적으로 식별하지 못하며, 문서 기반 학습이 격차를 부분적으로 줄인다고 보고한다.

**코드**: 공개 예정

**태그**: forgery-detection, ocr-document, dataset-benchmark

---

### [GaugeDefect: Detecting Surface Anomalies by Curvature of Feature Transport](https://arxiv.org/abs/2609.13282)

**한 줄 요약**: feature lattice에서 인접 local feature frame 간 orthogonal transport를 작은 닫힌 루프로 누적한 holonomy 행렬의 identity 이탈, 즉 feature-transport curvature로 표면 이상을 국소화하는 기하적 anomaly localization 방법.

**핵심 기여**: feature·reconstruction·distillation 기반 산업 anomaly localization은 어떤 영역의 지역 외관이나 feature가 정상 학습 이미지 대비 얼마나 특이한지를 점수화하는데, 얇은 스크래치·작은 덴트·반복 패턴의 붕괴는 각 patch가 개별적으로 이상하지 않고 인접 feature들이 변화·연결되는 방식을 교란한다는 점에 착안한다. GaugeDefect는 feature lattice의 각 노드에서 local feature frame을 추정하고 인접 frame 간 orthogonal transport를 계산한 뒤, 작은 닫힌 루프를 따라 누적한 transport로 holonomy 행렬을 얻어 identity와의 편차를 curvature로 정의한다. 정상 학습 이미지로 캘리브레이션한 뒤 유난히 큰 curvature를 feature field의 지역 불일치로 판정한다. 이 curvature는 물체의 물리적 곡률이 아닌 표현 공간의 이웃 불일치 척도이므로 곡면·텍스처 재질·비평면 산업 물체에 적용 가능하다고 밝힌다. 주된 역할은 미세한 표면 교란의 localization 개선이며, curvature 신호의 성질상 결함 경계 근처에서 더 선명한 응답이 나온다고 설명한다. 정량 수치는 초록에 제시되지 않는다. PRCV 2026 채택 논문이다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, defect-detection

---

### [ViCo-SAM3: Vision-Conditioned Alignment for Open-Vocabulary Camouflaged Object Segmentation](https://arxiv.org/abs/2609.15418)

**한 줄 요약**: SAM3의 텍스트 embedding을 전역 시각 문맥으로 동적으로 변조하는 vision-conditioned 모듈과 cross-modal binding 모듈을 얹어, text encoder 전체를 fine-tuning하지 않고 open-vocabulary 위장 객체 분할의 의미 격차를 줄이는 프레임워크.

**핵심 기여**: 텍스트 안내로 미학습 위장 객체를 분할하는 open-vocabulary camouflaged object segmentation(OVCOS)에서 SAM3는 전역 텍스트 의미와 세밀한 픽셀 수준 시각 단서 사이의 의미 격차가 크고, text encoder를 전체 fine-tuning하면 파라미터 부담이 크고 학습 카테고리에 과적합해 open-vocabulary 표현의 유연성이 훼손된다는 문제를 제기한다. ViCo-SAM3는 텍스트 embedding을 전역 시각 문맥으로 동적으로 변조해 현재 이미지 내용에 맞게 적응시키는 vision-conditioned(ViCo) 모듈과, 시각·텍스트 표현의 cross-modal 상호작용과 의미 정렬을 강화하는 vision-conditioned cross-modal binding(ViCoBind) 모듈로 구성된다. OVCamo 벤치마크에서 state-of-the-art 성능과 강한 일반화를 보고하며, 정량 수치는 초록에 제시되지 않는다.

**코드**: 불명

**태그**: segmentation, open-vocab-detection, foundation-model, peft

---

### [Restore What Matters: Lessons from Joint Restoration and Recognition](https://arxiv.org/abs/2609.13791)

**한 줄 요약**: 시각적 화질이 아니라 인식 손실이 복원의 위치·강도·필요 여부를 결정하도록 복원과 인식을 end-to-end로 결합하고, 품질 게이트로 깨끗한 프레임의 약 70%를 건너뛰는 Joint Restoration-for-Recognition(JR²) 패러다임.

**핵심 기여**: 인식 파이프라인은 대개 복원 후 인식 순서를 따르지만, 보기 좋은 이미지 생성이 인식 향상으로 이어지는 경우는 드물다는 경험에서 출발한다. JR²는 세 축으로 구성된다. 광학적으로 정확한 난류 시뮬레이션(blur·noise로 확장 가능)으로 복원을 실제 영상 형성 과정에 근거시키고, 선택적 주의와 신경가소성에서 착안해 identity에 중요한 영역·프레임에 모델 용량을 집중시키면서 이미 깨끗한 입력은 우회하며, 인식 손실을 복원과 정렬을 거쳐 end-to-end로 결합해 저수준 편집이 고수준 identity 안정성을 최대화하도록 한다. IARPA-BRIAR에서 TAR@0.01% FAR +0.6, FNIR@1% FPIR -2.5의 일관된 향상을 보이고, 품질 게이트가 깨끗한 프레임의 약 70%를 건너뛰어 비용을 줄인다. Ablation에서 물리 prior가 사실성을 높이고, joint 학습이 파국적 망각을 막으며, 많은 경우 선택적 복원만으로 충분하다고 확인한다. 코드·사전학습 모델·레시피를 제공한다고 밝히지만 초록과 arXiv 페이지에 URL은 기재되지 않았다.

**코드**: 불명

**태그**: re-identification, sim2real, image-restoration, efficient-inference

---

### [What Input Resolution Is Required for Bird Species Identification, and What Is Its Latency Cost on an Edge Device?](https://arxiv.org/abs/2609.14247)

**한 줄 요약**: 조류 종 식별에서 입력 해상도 14단계 × 6개 아키텍처 × 2개 학습·평가 체계 × 30 seed의 요인 설계로 2,520개 체크포인트를 학습하고 Jetson Orin Nano에서 지연시간을 측정해, 정확도 목표·전처리 경로·배포 엔진 정밀도에 따라 해상도 선택이 달라짐을 보인 연구.

**핵심 기여**: 풍력발전소의 조류 충돌 완화는 수십 픽셀에 불과한 원거리 조류를 식별해야 하므로 분류기의 입력 해상도 N이 고정 사양이 아닌 설계 변수라는 점에서 출발한다. 네 가지 결과를 보고한다. 첫째, 선택되는 N은 목표에 따라 달라져 검증 정확도 0.90은 ResNet50 N=112에서 추정 1.85 ms(테스트 0.8980)로, 0.95는 DINOv2-L N=144에서 12.70 ms로 달성되며, N=112에서 모델 교체(+5.93점)가 해상도 증가(+2.33점)보다 정확도를 더 높인다. 둘째, N 축소의 이득은 전처리 경로에 따라 달라져 N=224에서 80으로 줄일 때 개체별 파일 디코딩에서는 13.5%, 검출기가 4K 프레임을 한 번만 디코딩하는 경로에서는 46.2%가 절감되고 Pareto 집합이 20개에서 23개로 늘어난다. 셋째, 정확도는 배포 엔진에서 측정해야 하며 half precision이 ViT-S/16에서만 N≥96에서 4~7점을 잃고 CNN은 0.1점 이내이며, 176개 목표 중 26개에서 선택이 바뀐다. 잘못된 FP16 엔진이 올바른 엔진보다 빠르게 돌 수 있어 지연시간만으로는 탐지되지 않는다. 넷째, ViT-L급 모델도 이 장치에 탑재되지만 activation이 FP16 범위를 초과하므로 transformer block 경계에서 그래프를 분할해 FP32를 해당 구간에만 한정하면 DINOv2-L 체인이 단일 엔진 빌드보다 1.85배 빨라진다. seed 수에 따라 체계 간 차이의 부호가 안정화되는 양상도 정량화한다.

**코드**: 공개([Zenodo](https://doi.org/10.5281/zenodo.22697995) · 데이터·코드)

**태그**: fine-grained, efficient-inference, quantization, foundation-model

---

### [Pre-PEFT Probing: Weight Statistics and Perturbation Robustness for Layer Selection in VLM Vision Encoders](https://arxiv.org/abs/2609.15229)

**한 줄 요약**: VLM vision encoder의 각 transformer layer에 대해 Q/K/V projection 가중치 통계(norm·condition number)와 통제된 파라미터 섭동에 대한 강건성을 fine-tuning 전에 측정해, PEFT를 적용할 layer를 고르는 probing 방법.

**핵심 기여**: LoRA 등 adapter를 모든 layer에 일괄 적용하거나 heuristic 규칙으로 layer를 고르는 관행에서, 더 적은 학습 파라미터로 더 안정적이고 높은 이득을 얻는 layer 선택을 목표로 한다. vision encoder에 초점을 맞춰 각 layer의 '적응 가능성'을 Q/K/V projection 가중치의 통계적 성질과 통제된 파라미터 섭동 하의 강건성 두 관점으로 특성화하고, 이 지표들을 단일 layer에 PEFT를 적용했을 때의 downstream 성능 이득과 체계적으로 비교한다. 7개 벤치마크와 5개 PEFT 변형에 걸친 실험에서 weight norm이 크고 condition number가 높은 layer(또는 행렬)가 섭동에 더 강건하고 fine-tuning 이득도 더 클 가능성이 높다는 일관된 상관을 관찰하며, fine-tuning 전 분포 통계 분석과 섭동 테스트가 학습 파라미터를 줄이면서 성능을 유지·개선하는 layer 선택 신호가 된다고 보고한다. IJCNN 2026 채택 6쪽 논문이다.

**코드**: 불명

**태그**: peft, foundation-model, vlm

---

### [Discovering and Preserving Category Correlation Knowledge via Adaptive Reciprocal Knowledge Distillation](https://arxiv.org/abs/2609.13199)

**한 줄 요약**: teacher의 class correlation matrix를 student의 관계 표현에 맞춰 reciprocal하게 적응시켜 teacher 출력 분포를 단순화하고, 과신 teacher가 붕괴시킨 inter-class dark knowledge를 student 용량에 맞게 복원하는 knowledge distillation 방법 AR-KD.

**핵심 기여**: teacher와 student의 큰 크기 격차가 지식 전이를 방해하고, 기존의 정적 일방향 teacher→student 증류가 student 학습의 동적 성격을 무시하며 hard sample에 대한 표적 지도를 제공하지 못한다는 문제를 제기한다. Adaptive Reciprocal Knowledge Distillation(AR-KD)은 teacher의 class correlation matrix를 student의 relational representation에 매칭하는 reciprocal adaptation을 수행해 teacher의 prediction 구조를 student 용량에 맞게 재구성하며, 이 관계 정렬이 과신 teacher로 인한 inter-class dark knowledge 붕괴를 완화해 더 풍부하고 호환되는 지도 신호를 만든다고 설명한다. CIFAR-100과 ImageNet-1k에서 state-of-the-art 증류 베이스라인을 앞서며, 동질·이질 teacher-student 구성에서 student 정확도가 최대 7.13% 향상되고 vanilla KD 대비 평균 1.42~4.15% 높으며 다른 방법과 결합하면 추가로 개선된다고 보고한다.

**코드**: 공개([ARKD](https://anonymous.4open.science/r/ARKD/) · 익명 저장소)

**태그**: distillation, efficient-inference

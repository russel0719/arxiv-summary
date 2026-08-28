# arXiv cs.CV Daily Digest — 2026-08-28 (arXiv 공개일)

- **전체 신규 논문 수**: 114편 (new 93 + cross-list 21)
- **선별 수**: 11편

## 오늘의 트렌드

비디오 생성·world model 계열이 목록의 가장 큰 축을 이룬다. 긴 영상의 장기 기억을 어떻게
구조화할지(외형 신규성 기반 KV 캐시 유지, 링 구조 학습, query별 메모리 라우팅)를 다루는
autoregressive 비디오 확산 연구가 여러 편 나왔고, 이를 확률 분포 수준에서 평가하려는
벤치마크와 재방문 일관성 벤치마크가 함께 제출됐다. 표현학습 쪽에서는 collapse 방지를
아키텍처 비대칭 대신 정규화 항으로 해결하는 JEPA 계열 비디오 사전학습과 RGB-D 기반
visuospatial 표현학습이 눈에 띈다. VLM 영역은 두 갈래로 갈라져 있는데, 하나는 visual token
pruning·adaptive pixel compression 같은 추론 비용 절감이고 다른 하나는 attention head 수준의
내부 메커니즘 분석과 reasoning distillation이다. 검출·분할에서는 SAM과 diffusion을 학습 없이
조합하거나 open-world 검출을 추론 시점 보정으로 개선하는 training-free 접근이 반복해서
등장한다. 응용 분야로는 의료 영상(초음파·OCT·MRI·병리)과 원격탐사 식생 매핑이 다수를
차지하고, 문서·OCR 쪽은 고문서 벤치마크와 데이터셋 공개가 중심이다.

---

### [LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics](https://arxiv.org/abs/2608.27395)

**한 줄 요약**: EMA target encoder·stop-gradient 같은 비대칭 구조 없이 단일 인코더로 학습되는 비디오 self-supervised 사전학습 프레임워크.

**핵심 기여**: 기존 비디오 SSL은 표현 붕괴를 막기 위해 EMA target encoder, stop-gradient, 용량 제한 predictor 같은 아키텍처 비대칭에 의존하거나 픽셀 공간 복원에 의존해 사전학습 비용이 컸다. LeVJEPA는 LeJEPA의 붕괴 방지 목적함수를 비디오에 처음 적용해, 클립의 global/local view 간 invariance loss와 붕괴를 이론적으로 배제하는 SIGReg만으로 인코더+projector 구조를 학습하며 하이퍼파라미터를 하나로 줄인다. 동일 epoch·동일 데이터 조건에서 ViT-S/B/L 전반에 걸쳐 V-JEPA 2와 같거나 더 나은 성능을 5.6~20.8배 적은 사전학습 연산으로 달성하고, 동일 FLOPs 기준으로는 ImageNet-1K에서 최강 비디오 베이스라인을 7.6점 앞선다. 분기 간 비대칭이 없어 block-causal attention으로 학습해도 정확도 손실이 측정되지 않으며, 같은 비디오의 프레임으로 학습한 compute-matched DINOv2와 비교하면 appearance 중심 평가에서 근접하고 motion 중심 정확도는 약 2배다.

**태그**: ssl-backbone, video, image-embedding, foundation-model, efficient-inference

---

### [SSMB: Self-Supervised Local Feature Detection under Motion Blur](https://arxiv.org/abs/2608.27181)

**한 줄 요약**: 디블러링 없이 모션 블러 영상에서 반복 검출 가능한 키포인트를 self-supervised로 학습하는 검출기.

**핵심 기여**: 모션 블러는 국소 구조를 왜곡해 키포인트 위치의 repeatability를 떨어뜨리는데, 기존 방법은 연산 비용이 큰 deblur-then-detect 파이프라인을 쓰거나 선명한 이미지에서 뽑은 handcrafted 키포인트 위치를 회귀해 블러 환경에서 실제로 반복 가능한 지점이 아니라 handcrafted 검출기의 가정을 학습한다. SSMB는 외부 pseudo-label 없이, 전역 feature mixing 이후 국소 판별력을 복원하는 Local Discriminability Enhancement(LDE) 모듈과 2단계 학습(합성 도형 기하 사전학습 → 실제 sharp-blur 쌍에서 cross-domain consistency·기하 정합·공간 커버리지를 결합한 self-supervised 목적함수)으로 블러 불변 검출을 학습한다. 키포인트 검출, 이미지 매칭, 상대 pose 추정, visual localization 전 과제에서 지도·자기지도 베이스라인을 일관되게 앞서며 sparse 키포인트 검출기 중 최고 성능을 보고한다. 코드·모델·데이터셋은 논문 게재 시 공개 예정이다.

**태그**: feature-matching, ssl-backbone, correspondence, pose

---

### [PailitaoGR: Latent Think-with-Images for Generative Image Retrieval](https://arxiv.org/abs/2608.26658)

**한 줄 요약**: 실제 이미지 검색 로그로 학습해, 질의 이미지에서 검색 대상과 보조 근거를 스스로 분리해 semantic ID를 생성하는 검색 모델.

**핵심 기여**: 상품 semantic identifier(SID)를 직접 생성하는 generative retrieval을 이미지 검색으로 확장할 때, 실제 질의 이미지는 검색 대상과 유용한 보조 근거, 무관한 시각 정보가 섞여 있어 모델이 대상에 집중하면서 보조 근거를 선택적으로 쓰는 능력이 필요하다. PailitaoGR은 target Enhancer와 on-policy distillation·attention guidance loss로 검색 대상 영역의 visual token을 강화하는 target-focused perception, 그리고 auxiliary enhancer와 in-capacity incremental contrastive distillation으로 보조 근거 토큰을 활용하는 메커니즘을 결합해, crop 없이 확대하고 OCR 없이 읽는 동작을 모델 내부로 내재화한다. 실제 온라인 이미지 검색 로그에서 구성한 학습·검증 셋에서 기존 베이스라인 대비 평균 13.8% 향상을 보고한다.

**태그**: image-retrieval, image-embedding, vlm, distillation

---

### [Omni-Interactive Universal Embedder](https://arxiv.org/abs/2608.27044)

**한 줄 요약**: 텍스트·비디오·오디오를 하나의 임베딩 공간에 넣고, 시각 관심영역이나 오디오 구간 같은 상호작용 입력으로 질의를 조건화하는 범용 임베더.

**핵심 기여**: LLM 기반 임베더는 instruction-following 능력 덕에 two-tower 구조를 대체하고 있지만 대상 모달리티와 사용자 조건화 입력이 사실상 텍스트·이미지에 머물러 있다. OmniUE는 전용 learnable token의 중간층 표현을 이용해 텍스트·비디오·오디오를 통합 임베딩 공간에 매핑하고, visual/audio segmenter가 사용자의 영역·구간 지정을 처리해 omni-LLM과 결합하는 context aggregation으로 any-to-any 임베딩을 만든다. 텍스트·비디오·오디오와 상호작용 프롬프트를 함께 주는 compositional audio retrieval 평가용 OmniCHOIR 벤치마크를 새로 제안했고, MMEB-v2-video에서 평균 10.5%, MAEB에서 1.1%, 시각 상호작용 벤치마크 SCaR에서 83.7%, OmniCHOIR에서 24.1% 향상을 보고한다.

**태그**: image-embedding, image-retrieval, metric-learning, vlm

---

### [Text-to-seed generation: Training-free open-vocabulary seeded semantic segmentation via re-purposing diffusion as text-guided seed generator](https://arxiv.org/abs/2608.26624)

**한 줄 요약**: Stable Diffusion의 text-to-region 대응으로 seed point를 만들고 이를 SAM의 point prompt로 넘기는 학습 불필요 open-vocabulary 분할 프레임워크.

**핵심 기여**: SAM 단독으로는 open-vocabulary semantic segmentation 성능이 제한적이라 다른 모델이 낸 거친 마스크를 SAM으로 정제하는 방식이 흔한데, 초기 마스크가 부정확하면 이 전략은 신뢰할 수 없다. 이 논문은 SAM을 부정확한 마스크의 정제기가 아니라 정확한 객체 점(seed)으로 유도되는 영역 확장 모듈로 쓰자고 보고, 고전적 seeded segmentation을 따라 과제를 text-guided seed localization + seed 기반 영역 확장으로 재정의한다. T2S는 Stable Diffusion의 attention에서 대상 카테고리의 seed point를 뽑아 SAM의 point prompt로 사용하며, 별도 학습이나 추가 어노테이션 없이 표준 OVSS 벤치마크에서 강한 성능을 보고한다.

**태그**: segmentation, open-vocab-detection, foundation-model, correspondence

---

### [CODE: Cross-Modal Calibration and Dynamic Suppression for Open World Object Detection](https://arxiv.org/abs/2608.27214)

**한 줄 요약**: 멀티모달 파운데이션 모델 기반 open world 검출의 텍스트 단방향 매칭 문제를 추론 시점 보정만으로 완화하는 프레임워크.

**핵심 기여**: 파운데이션 모델 위에 세운 OWOD는 text-to-vision 단방향 매칭에서 오는 의미 모호성을 겪고, 경직된 outlier 페널티는 기지 클래스 결정 경계 근처의 미지 객체를 과도하게 억제한다. CODE는 전역 visual prototype을 주입해 텍스트 기반 기지 클래스 예측을 보정하는 Cross-Modal Joint Confidence Calibration, 국소 시각 응답에서 분류 망설임을 측정해 잠재적 미지 객체를 강화하는 Uncertainty-Guided Universal Objectness Enhancement, 경직된 억제를 margin 기반 조정으로 대체하는 Dynamic Outlier Suppression을 추론 시점에서 결합한다. OWL-ViT L/14 백본 기준 Real-World Detection 벤치마크 Task 1에서 U-mAP 21.7, K-mAP 40.8로 각각 이전 최고 대비 2.6점, 2.3점 향상을 보고한다.

**태그**: open-vocab-detection, object-detection, foundation-model

---

### [GeoMAD: Geometry-Aware Multi-View Anomaly Detection via Deformable Fusion and Distributional Alignment](https://arxiv.org/abs/2608.26724)

**한 줄 요약**: 카메라 캘리브레이션이나 voxel 구성 없이 2D feature map 위에서 뷰 간 대응을 학습하는 multi-class 산업 이상 탐지 프레임워크.

**핵심 기여**: 여러 시점의 관측을 융합하는 이상 탐지는 voxel 기반이면 명시적 기하 정합을 얻지만 3D 구성 비용과 클래스별 가정이 필요하고, 경량 patch 기반이면 효율적이지만 이산적 후보 매칭에 머물러 연속적 뷰 간 대응이 없다. GeoMAD는 2D feature map에서 뷰쌍별·내용 적응적 sampling offset을 학습하고 이를 multi-scale window pyramid와 image-global reference sampling으로 배치하는 Cross-view Deformable Fusion Module(CDFM)과, 각 뷰의 bottleneck 분포를 인스턴스별 view-centric 목표에 맞추는 self-supervised 정규화 손실 Distributional View Alignment(DVA)를 결합한다. Real-IAD와 MANTA-Tiny에서 통합 multi-view·multi-class 설정의 검출·위치추정 성능을 보고하며, 캘리브레이션·voxel·클래스별 3D 감독 없이 동작한다.

**태그**: anomaly-detection, industrial-inspection, defect-detection, correspondence

---

### [Data-efficient crack quantification in lithium-ion cathodes using foundation model transfer](https://arxiv.org/abs/2608.27162)

**한 줄 요약**: 동결된 self-supervised ViT 인코더에 경량 디코더와 반복적 model-assisted 어노테이션을 붙여 대면적 전자현미경 이미지의 균열을 정량화한 사례.

**핵심 기여**: 리튬이온 양극재 열화의 핵심인 입자 균열은 정량 현미경 분석이 필요한데, 파괴 단면 한 장이 수백 메가픽셀이고 픽셀 단위 전문가 라벨링에 이미지당 몇 시간이 들어 어노테이션이 병목이다. 이 연구는 동결된 self-supervised vision transformer 인코더 위에 학습 가능한 경량 디코더를 얹고 model-assisted 어노테이션을 반복해, 희소한 라벨 예산을 집단 규모 열화 측정으로 전환한다. 초기·사이클 열화·달력 열화 상태를 대표하는 120메가픽셀 NMC 양극 단면 3장에 적용해 입계 균열의 초기/후기 단계와 입내 균열을 구분하고 입자별 균열 폭·굴곡도·면적 비율 분포를 산출했으며, 후기 입계 균열 피복률이 사이클 시료에서 4.6%로 초기·달력 열화 시료의 0.5%와 대비된다.

**태그**: industrial-inspection, defect-detection, ssl-backbone, foundation-model, segmentation

---

### [Cross-Architecture Knowledge Distillation from a Vision Foundation Model to a Lightweight Visual State Space Model for Tea Leaf Disease Classification](https://arxiv.org/abs/2608.26771)

**한 줄 요약**: DINOv2 ViT 교사에서 4.45M 파라미터 양방향 visual state space model 학생으로 넘어가는 이종 아키텍처 증류의 학습 안정화 기법과 절제 실험.

**핵심 기여**: DINOv2 같은 self-supervised 파운데이션 모델은 강한 특징을 주지만 현장 배포에는 너무 크고, 소규모 농업 데이터셋에서 처음부터 학습한 경량 모델은 underfit하는데, ViT와 SSM은 토큰 혼합 방식이 근본적으로 달라 이종 증류가 거의 탐구되지 않았다. 이 논문은 from-scratch SSM 학생의 학습을 막는 두 문제(단일 대형 patch-embedding convolution, residual 경로를 끊는 fusion layer)를 지목하고 점진적 convolutional stem과 gated bidirectional selective-scan 블록으로 교정해 4.45M 파라미터 학생을 안정적으로 학습시킨다. 세 시드 기준 temperature-scaled logit 증류가 정확도를 92.32±2.14%에서 95.41±1.17%(최고 96.20%, macro-F1 94.45%)로 평균 +3.09%p 끌어올렸고, 학생은 22M 교사 대비 5.0배 적은 파라미터로 정확도의 98.3%를 유지한다. 중간 feature-alignment 손실은 오히려 정확도를 떨어뜨려 단순 logit 수준 증류가 가장 강한 구성이었으며, 단일 데이터셋 범위와 비공식 간소화 SSM 구현이라는 한계를 함께 밝히고 있다.

**태그**: distillation, ssl-backbone, fine-grained, efficient-inference

---

### [PACE: A Unified Condense-and-Extract Paradigm for Fast VLM Inference](https://arxiv.org/abs/2608.27206)

**한 줄 요약**: 비전 인코더 이전의 픽셀 적응 압축과 인코더 이후의 이중 attention 기반 토큰 선별을 결합한 학습 불필요 VLM 가속 프레임워크.

**핵심 기여**: 기존 visual token pruning은 대부분 비전 인코더 이후에만 작동해 인코딩 단계의 지연을 그대로 두고, 엄격한 토큰 예산에서는 전역 맥락과 세부 정보를 동시에 보존하지 못해 성능이 떨어진다. PACE는 인코딩 전에 시각 정보 밀도를 평가해 중복 입력을 적응적으로 다운샘플링하는 Adaptive Pixel Compressor(Condense 단계)와, 인코더 내부 시각 신호와 LLM의 의미 신호를 융합해 과제 핵심 토큰을 남기는 Dynamic Dual-Attention Extractor(Extract 단계)로 비전 인코더와 LLM을 함께 가속한다. Qwen2.5-VL-7B에 적용하면 visual token의 10%만 사용하면서 원 성능의 93.8%를 유지하고 time to first token 기준 3.1배 속도 향상을 얻는다. 코드가 공개돼 있다.

**태그**: efficient-inference, vlm, foundation-model

---

### [G2D: Generative-to-Discriminative Collaborative Inference for Zero-Shot Image Classification](https://arxiv.org/abs/2608.26744)

**한 줄 요약**: CLIP이 뽑은 top-K 후보를 생성형 VLM이 이미지에 근거해 검증하도록 분리한 학습 불필요 zero-shot 분류 프레임워크.

**핵심 기여**: CLIP의 top-1 예측이 틀려도 정답이 top-K 후보 안에 남는 경우가 많아 문제는 recall이 아니라 disambiguation인 반면, 생성형 모델 단독은 큰 라벨 공간과 제약 없는 출력 때문에 어려움을 겪는다. G2D는 광범위한 후보 검색과 이미지 기반 세밀 검증을 분리해, CLIP 확률과 후보 이름을 시각적으로 유사한 클래스 구분을 위한 구조적 사전으로 제공하고 fixed confidence routing, entropy 적응형 후보 크기, trie 제약 디코딩으로 불확실한 샘플에만 생성 추론을 집중시키며 입력마다 유효한 출력 하나를 보장한다. 8개 벤치마크 평균 정확도가 CLIP 59.35%, 단독 VLM 63.11% 대비 68.85%이고, 7개 생성기 설정에서 후보 검증이 평균 정확도를 1.08~27.42%p 높였으며 DCLIP·WaffleCLIP·CuPL로도 전이된다.

**태그**: fine-grained, vlm, image-retrieval, foundation-model

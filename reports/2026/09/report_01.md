# arXiv cs.CV Daily Digest — 2026-08-31 (arXiv 공개일)

- **전체 신규 논문 수**: 93편 (new 75 + cross-list 18)
- **선별 수**: 11편

## 오늘의 트렌드

목록의 가장 큰 덩어리는 동결된 foundation feature를 재사용·압축·재배치하는 연구다. DINOv2/DINOv3·V-JEPA·CLIP/SigLIP 같은 사전학습 표현을 그대로 쓰면서 pruning(Cut-ViT), 경량 헤드 부착(WALDO), sparse autoencoder를 통한 성분 분리(EXPOSE, block-sparse featurizer), attention 구조 재설계(Semantic Head Specialization)로 비용을 줄이거나 표현의 성질을 진단하는 흐름이 반복된다. 두 번째 축은 long-horizon video·streaming 처리로, KV 캐시와 메모리 관리(DensityKV, LayerRecall, StreamEMS), 토큰 예산 축소(VTC, Token-Budget Distillation), 학습 없는 시간 분할(STITCH, Temporal Tree of Thought)이 몰려 있다. 3D 쪽은 3D Gaussian Splatting의 메모리·압축·in-the-wild 강건성(ABCD, WilLaGS, 비균일 양자화)과 대규모 feed-forward 재구성(GeoFF3D, ABot-Recon)이 주도한다. 응용 영역에서는 산업 결함·이상 탐지, 위조·인페인팅 판별, 다중 스크립트 OCR(UniLipi, PSMC, Synth-JDoc), VLA·GUI 에이전트(VLAct, DeicticVLA, Iron, GMA), 의료 영상이 각각 소규모 군집을 이루며, 벤치마크·감사(audit) 성격의 논문 비중이 눈에 띈다.

---

### [Cut-ViT: Task-Specific Model Pruning via Gram Anchoring Subspace Consistency](https://arxiv.org/abs/2608.28205)

**한 줄 요약**: DINOv3의 Gram 부분공간을 앵커로 정렬해 downstream 태스크별로 특화된 서브네트워크를 1분 만에 뽑아내는 pruning 파이프라인.

**핵심 기여**: 기존 visual foundation model pruning은 단일 데이터셋에서 토큰 대 토큰 정합에 의존해 강건성이 떨어지고 태스크 특화가 부족하다고 지적한다. Cut-ViT은 공간·의미 관점의 gram anchoring 행렬을 만들어 부분공간 분해로 기저를 추출하고, basis-agnostic 및 residual 제약으로 native DINOv3와 pruned 모델의 gram 부분공간을 공간·채널 축에서 정렬해 서브네트워크가 원 표현을 상속하도록 한다. 여기에 특징 manifold의 정보 밀도를 공간·채널 방향으로 정량화하는 spectral entropy adaptation을 붙여 pruning 목적함수를 downstream 태스크에 맞춘다. A100 1장에서 약 1분, 기존 방법 대비 시간 20.9%·GPU 메모리 45.5%만 사용해 다양한 sparsity의 서브네트워크를 얻으며 9개 데이터셋 6개 태스크에서 SOTA를 보고한다.

**태그**: ssl-backbone, foundation-model, model-pruning, efficient-inference

---

### [WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes](https://arxiv.org/abs/2608.28216)

**한 줄 요약**: 동결된 V-JEPA 2.1 특징 위에 3.4M 파라미터 헤드만 얹어 참조 이미지 한 장과 짧은 설명으로 특정 인스턴스를 찾고 부재까지 판정하는 검출기.

**핵심 기여**: 어수선한 장면에서 참조 이미지 한 장으로 특정 객체 인스턴스를 찾고 없을 때는 없다고 보고하는 작업은 통상 대형 VLM이 담당하는데, 이 논문은 world-model 사전학습이 이미 학습한 표현만으로 훨씬 저렴하게 같은 능력을 얻을 수 있는지 묻는다. 백본에 gradient를 주지 않고 동결된 특징을 읽는 exemplar·언어 조건 헤드를 두고, 인스턴스 주석에서 학습 에피소드를 합성하되 참조 인스턴스만 제외하고 동일 카테고리 distractor는 남기는 방식으로 부재 사례를 구성한다. 순진한 구현에서는 crop 크기만으로 라벨이 예측돼 exemplar를 보지 않고도 부재 AUROC 0.9998에 도달하는 지름길이 생기며, 이를 차단하는 negative control을 함께 보고한다. 35개 held-out 장면에서 catalogue AP@50 0.461로 동일 채점자 하의 prompted Grounding DINO(0.306)를 앞서고, 동일 576 토큰 그리드에서 V-JEPA를 DINOv3로 바꾸면 동일 카테고리 부재 AUROC가 0.880→0.726, 인스턴스 AP@50이 0.201→0.141로 떨어진다. 다만 인스턴스 수준 Success@1은 0.190으로 카테고리 우연 수준(0.190)에 머물러, world-model 특징이 위치 정확도와 부재 판정에는 전이되지만 인스턴스 정체성에는 전이되지 않는다고 밝힌다.

**태그**: object-detection, open-vocab-detection, foundation-model, one-shot-detection

---

### [Cross-Spectral Dense Correspondence for Multimodal Spectral Medical Imaging](https://arxiv.org/abs/2608.28341)

**한 줄 요약**: 겹치지 않는 파장대 이미지쌍의 dense correspondence를 위해 센서 비의존 cross-spectral 변조 프로토콜과 합성 벤치마크를 제안.

**핵심 기여**: 서로 다른 분광 감도로 관측된 대응점은 파장 의존 대비 변화·명암 반전·외형 이동을 겪는데, dense ground truth를 얻기 어렵고 RGB 기반 학습 데이터로는 감독 신호가 부족하다는 문제를 다룬다. 기존 correspondence 벤치마크 위에 intensity input projection을 쓰는 센서 비의존 cross-spectral 변조 프로토콜을 도입하고, 물리적으로 타당한 radiometric 차이를 시뮬레이션한 합성 cross-spectral 벤치마크를 함께 제안한다. 이 통합 프로토콜로 최신 dense correspondence 백본 여러 개를 학습했을 때 심한 spectral mismatch 조건에서 성능이 크게 오르고 표준 RGB 벤치마크 성능은 유지된다. Ablation 결과 view별 채널 선택과 비선형 radiometric 변환이 상호 보완적으로 작용해, 기존 모델의 주된 한계는 구조적 매칭 능력이 아니라 학습 분포와 대상 이미지쌍의 분광 특성 불일치라고 결론한다.

**태그**: correspondence, feature-matching, cross-spectral, dataset-benchmark

---

### [Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs](https://arxiv.org/abs/2608.28383)

**한 줄 요약**: ViT attention head가 객체·배경 전문가로 분화되는 현상(SHS)을 지표화하고, 이를 설계 원리로 삼아 full attention 성능을 1/6.5 연산으로 재현하는 hybrid attention을 제시.

**핵심 기여**: hybrid attention이 LLM에서는 표준이 됐지만 멀티모달 LLM의 ViT에는 만족스러운 설계가 없고 어떤 attention 패턴이 왜 잘 되는지 합의가 없다는 지점에서 출발한다. ViT head를 분석해 객체 전문가와 배경 전문가로 분화되며 이 분화가 full attention에서 가장 두드러진다는 Semantic Head Specialization을 관찰하고, 이를 정량화하는 SHS-Index를 제안해 full-attention ViT와 chunk-window ViT를 구분하고 downstream 벤치마크 성능과 강하게 연동됨을 보인다. 이어 window interaction, token serialization, local softmax allocation 세 구조 요인이 SHS를 좌우함을 확인하고 이를 설계 원리로 삼은 Ariadne Attention을 만들어, 22개 이미지·비디오 태스크에서 attention 연산량 6.5분의 1로 full attention과 동등한 성능을 보고한다.

**태그**: foundation-model, efficient-inference, vlm, attention-analysis

---

### [Relational Knowledge Distillation Brings DNN Representations Close Enough to Humans to Be Aligned Without Supervision](https://arxiv.org/abs/2608.27877)

**한 줄 요약**: Relational Knowledge Distillation으로 미세조정한 사전학습 DNN이 내부 거리 구조만으로 사람 표현과 개별 객체 수준까지 대응됨을 Gromov-Wasserstein 최적수송으로 검증.

**핵심 기여**: 기존 연구는 사람 표현의 관계 구조를 DNN에 이전해 표현 유사도가 개선된다고 보고했지만, 개별 객체 수준의 세밀한 정렬과 학습 데이터와 독립적인 사람 임베딩에 대한 일반화라는 두 가지 엄격한 조건에서 검증되지 않았다고 지적한다. 내부 거리 구조만으로 사람-DNN 대응을 추정하는 비지도 비교법 Gromov-Wasserstein optimal transport를 사용하고, 학습 데이터와 개념이 겹치지 않는 별도 테스트셋에서 일반화를 평가한다. Relational Knowledge Distillation으로 사전학습 DNN을 미세조정하면 이 테스트셋에서 개별 객체 수준의 정렬이 성립하며, 개선의 원인은 거친 카테고리 간 거리 순서로 드러나는 더 사람에 가까운 전역 구조이고 국소 최근접 이웃 중첩률은 거의 변하지 않는다.

**태그**: distillation, image-embedding, representation-analysis, fine-grained

---

### [Image Augmentation as Test Generation for Deep Learning-Based Image Retrieval Systems](https://arxiv.org/abs/2608.27502)

**한 줄 요약**: 50개 증강·생성 기법을 10개 범주로 분류하고, 임베딩 기반 이미지 검색 시스템의 테스트 생성기로서 임베딩 유사도·불확실성·의미 현실성·검색 실패율 네 축에서 대규모로 평가.

**핵심 기여**: 딥러닝 기반 이미지 검색 시스템의 신뢰성 확보를 소프트웨어 공학 문제로 놓고, 증강·생성 기법 문헌 리뷰로 50개 기법을 10개 범주 분류체계로 정리한 뒤 이들을 테스트 생성기로 실증 평가한다. 증강 이미지를 Amazon Titan과 OpenCLIP으로 임베딩하고 임베딩 공간 유사도, 네 가지 추정기로 측정한 임베딩 불확실성, LLaVA가 채점한 의미 현실성, 검색 실패율로 분석하며 CIFAR-10·ImageNet-1K·산업 파트너 데이터셋에서 실험한다. 평가한 모든 데이터셋과 임베딩 모델에서, 기법별 단일 강도 설정 하에 weather simulation과 SaSPA가 가장 높은 임베딩 불확실성과 실패율을 만들면서 성능 안정성·시각적 현실성·증강 효과의 균형이 좋았고, GAN 기반 증강은 현실성이 가장 낮아 합성 artifact와 지각적 불일치를 드러냈다. 논문은 결과가 설정 의존적이며 더 약하거나 강한 perturbation에서는 달라질 수 있다고 명시한다.

**태그**: image-retrieval, image-embedding, dataset-benchmark, robustness

---

### [ShiftSplit-AD: Separating Domain Shift from Defects in Foundation-Feature Visual Anomaly Detection](https://arxiv.org/abs/2608.27610)

**한 줄 요약**: DINOv2 최근접 정상 residual을 low-rank와 row-sparse로 분해해 도메인 변화 성분을 억제하고 sparse 성분만으로 이상을 점수화.

**핵심 기여**: 동결된 foundation feature 기반 이상 탐지기는 테스트 패치와 정상 feature 메모리 사이 거리를 점수로 쓰는데, 촬영 조건 변화만으로도 이 거리가 커져 도메인 변화와 결함이 뒤섞인다는 문제를 다룬다. ShiftSplit-AD는 패치 residual 행렬을 low-rank와 row-sparse 성분으로 분해해 sparse 성분을 점수화하고, low-rank/sparse 융합을 선택적으로 적용한다. Bottle 개발 후 고정한 설정으로 AeBAD-S에서 sparse-only 점수화가 image AUROC를 0.6780→0.7294, AUPRC를 0.8052→0.8465로 올리고 개선의 paired bootstrap 95% 구간은 각각 [0.0238, 0.0808], [0.0170, 0.0650]이다. 다만 같은 방식이 held-out MVTec 4개 카테고리의 평균 clean AUROC를 0.9890→0.9133으로 떨어뜨리고 Bottle localization을 악화시켜, 진짜 결함도 상관된 저차원 구조를 가질 수 있으므로 residual 활동을 폭넓게 걸러내면 결함 정보까지 제거된다는 트레이드오프를 논문 스스로 한계로 제시한다.

**태그**: anomaly-detection, industrial-inspection, ssl-backbone, foundation-model

---

### [CF-YOLO: Context-Aware Feature Refinement for Camouflaged Industrial Micro-Defect Detection](https://arxiv.org/abs/2608.28070)

**한 줄 요약**: 복잡한 배경에 위장된 미세 표면 결함을 잡기 위한 실시간 검출기와 구리관 결함 데이터셋 CTDD 공개.

**핵심 기여**: 구리관 같은 산업 부품의 표면 미세 결함은 크기가 매우 작고 복잡한 배경에 시각적으로 위장돼 특징 표현이 약해지고 오검·미검이 많다는 점을 문제로 잡는다. 큰 커널로 거시 텍스처 맥락을 보고 작은 커널로 경계를 선명하게 하는 Context-Perception Aggregation Module(CPAM)로 배경 위장을 깨고, 선형 복잡도 additive token mixer를 쓰는 Feature Additive Refinement Module(FARM)으로 미세 이상의 표현을 전역적으로 검증·정제해 노이즈로 인한 오류를 억제한다. 구리관 검사 장면에서 수동 주석한 1,847장·4,898개 bounding-box 결함 인스턴스로 구성된 Copper Tube Defect Dataset(CTDD)을 함께 공개한다. CTDD에서 YOLOv11 등 대표 baseline 대비 mAP@50 2.2%, Precision 3.9% 높은 성능을 실시간 추론 속도로 달성하며, 코드와 모델이 공개돼 있다.

**태그**: defect-detection, industrial-inspection, object-detection, dataset-benchmark

---

### [FUSED: Forensic-Semantic Mixture-of-Experts for AI Inpainting Detection and Localization](https://arxiv.org/abs/2608.28302)

**한 줄 요약**: 저수준 forensic 신호와 고수준 semantic 특징을 sparsely-gated MoE로 결합해 AI 인페인팅을 탐지하고 픽셀 단위로 위치까지 찾는 통합 프레임워크.

**핵심 기여**: diffusion 기반 인페인팅은 이미지의 국소 영역만 바꾸지만 대부분의 AI 이미지 탐지기는 전역 artifact에 의존하고 위치를 특정하지 못하며, 이 artifact가 생성기마다 달라 분포 이동에서 전이가 잘 안 된다는 문제를 다룬다. FUSED는 저수준 forensic 단서와 고수준 semantic 특징을 sparsely-gated Mixture-of-Experts로 결합해 토큰마다 가장 관련 있는 신호를 적응적으로 선택하고, 입력마다 이미지 수준 조작 점수와 인페인팅 영역의 픽셀 단위 마스크를 동시에 예측한다. OpenSDID cross-generator 벤치마크에서 평균 탐지·localization이 가장 좋고 미지 생성기에서 향상 폭이 가장 크며, 동일 모델이 held-out AutoSplice와 CocoGlide로 직접 전이되어 localization 성능을 두 배 이상 높인다. 각 held-out 벤치마크를 전역 생성기 artifact가 있는 조건과 없는 조건으로 나눠 평가한 결과, 제안 방법을 포함한 모든 방법이 그 artifact를 조작 증거로 일부 읽고 있음을 함께 보고한다. 코드와 사전학습 모델이 공개돼 있다.

**태그**: forgery-detection, segmentation, mixture-of-experts, foundation-model

---

### [From Perspective to Fisheye Depth Estimation and Open-Vocabulary Segmentation](https://arxiv.org/abs/2608.27860)

**한 줄 요약**: fisheye 이미지의 latent embedding을 perspective 쪽으로 옮기는 학습 파라미터 Distortion Extenders(DEX)로 vision foundation model을 광각 카메라에 일반화.

**핵심 기여**: vision foundation model은 대규모 perspective 이미지로 학습된 덕에 잘 일반화하지만, fisheye처럼 시야가 넓은 이미지에서는 픽셀의 방사 왜곡에서 오는 covariate shift 때문에 잘못된 출력을 낸다. DEX는 fisheye 왜곡 계수와 fisheye·perspective 사이의 latent 공간 분포 이동을 모델링하는 학습 파라미터 집합으로, self-supervised alignment loss를 최소화해 fisheye 이미지의 latent embedding이 perspective 이미지의 것을 닮도록 변환한다. 구조·태스크에 비의존적이어서 monocular depth estimation과 open-vocabulary segmentation, convolution·Transformer 기반 구조 모두에서 실내외 fisheye 데이터셋의 baseline을 일관되게 상회한다. 부산물로 DEX의 activation을 왜곡 계수로 디코딩해 카메라 캘리브레이션에 쓸 수 있고, 코드가 공개돼 있다.

**태그**: foundation-model, peft, segmentation, depth

---

### [A Deeper Analysis of Block-Sparse Featurizers](https://arxiv.org/abs/2608.27515)

**한 줄 요약**: 방향 하나가 아니라 저차원 부분공간(블록)을 원자 단위로 쓰는 block-sparse featurizer의 실패 양상을 분석하고 Tournament Top-K 등 구조 개선을 제안.

**핵심 기여**: block-sparse featurizer(BSF)는 sparse autoencoder와 유사하지만 원자 단위가 단일 방향이 아니라 방향들의 작은 블록이어서, 저차원 manifold 위에 놓이는 특징 — vision에서 특히 흔한 — 을 다루도록 설계됐다. 이 논문은 BSF의 강점과 약점을 살펴, feature splitting과 composition 같은 고전적 SAE 실패 양상이 여전히 어느 정도 남아 있음을 확인한다. 이를 완화하는 여러 구조 변경을 제안하며, 그중 Tournament Top-K 선택 규칙은 feature splitting을 크게 줄이고, 블록 패러다임을 crosscoder로도 확장한다.

**태그**: image-embedding, representation-analysis, sparse-autoencoder, foundation-model

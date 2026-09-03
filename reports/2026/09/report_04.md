# arXiv cs.CV Daily Digest — 2026-09-03 (arXiv 공개일)

- **전체 신규 논문 수**: 136편 (new 118 + cross-list 18)
- **선별 수**: 12편

## 오늘의 트렌드

목록에서 가장 두꺼운 군집은 여전히 의료 영상으로, MRI 복원·재구성(SliceBridge, Diffusion-Encoding Gaussian Field, Data-Efficient Multi-Contrast MRI), 병리 whole slide image의 foundation model 활용(Morphology signal in WSI, Synergistic Information Disentanglement), 반지도 분할(SAUF-Net, Asymmetric Paired-Annotation Learning)이 20편 안팎을 차지한다. 두 번째 축은 배포 제약을 정면으로 다루는 논문들이다. 마이크로컨트롤러에서의 forward-only test-time adaptation(FORGE), post-training quantization을 염두에 둔 학습(SCULPT), 임베디드 메모리 절감 추론(GaLe), 우주 로보틱스용 하드웨어 가속 instance segmentation이 모두 같은 날 올라왔고, discrete visual tokenization의 VQ·PQ·SQ를 rate-distortion 관점으로 통일한 이론 논문이 여기에 붙는다. test-time adaptation 자체도 별도 군집을 이뤄 vision-language object detector(DESA-TTA), missing modality(Test-Time Logit Prompting), world action model(World-Coherent Decoding)로 갈라진다. VLM·MLLM 쪽은 평가와 실패 진단이 주류로, hallucination 완화 방법의 재평가(Does Playing it Safe Count as Faithfulness), cross-modal attention drift 기반 object hallucination 탐지, 공정성·문화 이해·미적 판단 편향 벤치마크(FairLens, MemeCULT-1K, Beauty is in the AI of the beholder)가 함께 나왔다. 미디어 포렌식은 이진 판별을 넘어 위·변조 영역 localization과 편집 도구 attribution, 생성기 provenance 추적으로 세분화되는 흐름이 뚜렷하다. 검색·임베딩 계열에서는 비디오 임베딩 예산 배분(AllocEmbed), text-video retrieval(TAME, MARS), 문서 검색용 단일 타워 인코더(NeoMME), CBIR rank aggregation이 나란히 등장했고, 원격탐사·레이더·UAV 응용과 Gaussian splatting 기반 3D/4D 재구성이 각각 별도 블록을 형성한다.

---

### [CoViT: Instance-Correspondence Contrastive Learning for Vision Transformer](https://arxiv.org/abs/2609.01787)

**한 줄 요약**: ViT의 attention map으로 instance mask를 만들어 patch 단위 hardest triplet을 구성하는 self-supervised 학습으로 instance 구별력을 주입한다.

**핵심 기여**: ViT는 semantic 이해에는 강하지만 같은 범주의 서로 다른 개체(예: 두 마리 개)에 사실상 동일한 임베딩을 주어 instance 수준 태스크에서 한계를 보인다. CoViT는 multi-head attention을 adaptive thresholding과 morphological operation으로 정제해 instance mask를 뽑아 foreground anchor를 정하고, anchor마다 mask 내부에서 가장 덜 유사한 patch를 hardest positive로, 다른 instance에서 가장 유사한 patch를 hardest negative로 골라 contrastive loss를 건다. 추가 decoder나 라벨 없이 순수 ViT만으로 여러 instance-level perception 태스크에서 2 AP 이상의 일관된 향상을 보고하며, 코드와 모델을 공개할 예정이라고 밝혔다.

**태그**: ssl-backbone, correspondence, image-embedding, metric-learning, foundation-model

---

### [NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference](https://arxiv.org/abs/2609.01657)

**한 줄 요약**: 이미지 patch와 다국어 텍스트를 하나의 양방향 Transformer 인코더로 처리하는 260M/800M 규모 멀티모달 인코더로, 검색용 dense·late-interaction 헤드를 붙여 미세조정한다.

**핵심 기여**: ColPali 계열 문서 검색기는 생성용으로 설계된 VLM을 인코더로 전용하면서 비생성 태스크에 불필요한 파라미터·연산 비용을 그대로 떠안는다. NeoMME는 별도 vision encoder와 causal LM을 결합하는 대신 단일 양방향 인코더를 masked discrete-diffusion 텍스트 목적함수로 처음부터 사전학습하고, 16,384 토큰 컨텍스트로 4K UHD 이미지 두 장까지 인코딩한다. ViDoRe v3에서 260M 모델이 nDCG@10 0.523으로 800M 미만 모델을 모두 앞서고 800M 모델은 0.556에 도달하며, 2048×2048 입력·L40S 기준 ColModernVBERT 대비 약 2배 처리량을 낸다. hierarchical token pooling과 asymmetric quantization으로 late-interaction 임베딩을 255배 압축하면서 기준 nDCG@10의 95% 이상을 유지하고, 사전학습 백본과 검색용 체크포인트를 Apache 2.0으로 공개했다.

**태그**: foundation-model, image-embedding, image-retrieval, quantization, vlm

---

### [GeoStore: Finding Small Storefronts in Large Scenes -- A Fine-Grained POI Localization Benchmark with Global-to-Local Asymmetric Matching](https://arxiv.org/abs/2609.02012)

**한 줄 요약**: 클로즈업 쿼리와 광각 레퍼런스라는 비대칭 매칭 설정을 정의한 벤치마크와, global descriptor에 비대칭 local 경로를 결합한 매칭 방법 GLAM.

**핵심 기여**: POI localization은 대상이 화면을 가득 채운 클로즈업 사진을 대상이 작고 중심에서 벗어난 광각 street-view와 대조해야 하므로, 같은 스케일의 전체 이미지끼리 맞추는 대칭 가정의 visual place recognition과 성격이 다르다. 저자들은 이 비대칭·fine-grained·open-set 설정을 다루는 첫 벤치마크 GeoStore를 만들고, 단일 global vector가 작은 대상을 희석시켜 기존 global descriptor 방법이 구조적으로 불리함을 보인다. 제안한 GLAM은 retrieval anchoring용 global descriptor와, 레퍼런스를 pooled region token 집합으로 유지해 쿼리 probe와 learnable soft late interaction으로 대조하는 비대칭 local 경로를 결합하고, 추론 시 같은 token으로 mutual-nearest-neighbor 재순위화를 수행한다. Recall@1/5/10과 mAP에서 global·2단계 baseline을 앞서면서 재순위화 특징 크기는 약 1/5, 쌍당 매칭 비용은 기존 local 재순위화 대비 약 2자릿수 낮으며, 벤치마크와 코드를 공개할 예정이다.

**태그**: feature-matching, image-retrieval, fine-grained, correspondence, dataset-benchmark

---

### [Aggregating Neighbor Embedding Projection and Rank-Based Manifold Learning for Image Retrieval](https://arxiv.org/abs/2609.01963)

**한 줄 요약**: UMAP 투영으로 얻은 순위 리스트와 rank 기반 재순위화 결과를 Borda Count로 합쳐 CBIR 정확도를 올리는 프레임워크.

**핵심 기여**: 고차원 특징 공간에서 pairwise 거리는 맥락 관계를 담지 못하고, manifold learning(표현 개선)과 rank 기반 재순위화(순위 리스트의 맥락 정보 활용)는 서로 보완적이지만 결합 방법이 정립돼 있지 않다. 이 논문은 UMAP으로 대안적인 저차원 표현을 만들어 얻은 순위 리스트와 rank 기반 재순위화 순위 리스트를 Borda Count rank aggregation으로 통합한다. ResNet152·Swin Transformer·DINOv2 특징을 사용해 여러 공개 데이터셋에서 실험했고, 특히 기준 표현의 precision이 낮은 경우에 검색 성능이 개선되며 상위 순위 품질이 향상돼 MAP과 Precision에서 경쟁력 있는 수치를 보인다고 보고한다.

**태그**: image-retrieval, image-embedding, metric-learning

---

### [Learning to Attract and Repel: Dual Quality Margin Learning for Face Recognition (DQM-Face)](https://arxiv.org/abs/2609.02644)

**한 줄 요약**: feature magnitude 기반 품질 추정에 semantic 품질 학습을 더해 attraction·repulsion margin을 동시에 조절하는 face recognition 손실.

**핵심 기여**: 기존 margin 기반 face recognition은 샘플 품질을 feature magnitude로만 모델링해 identity와 무관한 노이즈에 취약하고, 이것이 표현의 판별력을 떨어뜨린다. DQM-Face는 magnitude 기반 품질 추정에 squeeze-and-excitation semantic attention으로 구현한 semantic 품질 학습을 결합해 quality-aware margin을 만들고, intra-class 응집을 강화하는 attraction과 함께 inter-class 분리를 명시적으로 넓히는 repulsion margin을 도입한다. 여러 벤치마크에서 기존 SOTA를 상회하며, margin 최적화를 위해 학습된 품질 신호가 face image quality assessment에도 그대로 유효함을 보인다. 코드가 공개돼 있다.

**태그**: metric-learning, image-embedding, re-identification, fine-grained

---

### [DPA: Decoupling Product-Agnostic Anomaly Representations for Zero-shot Anomaly Generation](https://arxiv.org/abs/2609.02075)

**한 줄 요약**: 다른 제품의 실제 결함을 옮겨 심는 방식으로 정상 이미지만 있는 신규 제품의 이상 샘플을 생성하는 diffusion 프레임워크.

**핵심 기여**: 새로 투입된 제품은 정상 이미지만 확보되는 경우가 많아 이상 탐지 학습에 쓸 결함 샘플이 부족하고, 기존 zero-shot 이상 생성은 텍스처 이미지나 텍스트 설명을 결함 소스로 삼아 비현실적인 결과를 낸다. DPA는 유사한 결함이 제품군을 넘어 반복된다는 관찰에서 출발해 기존 제품의 실제 결함을 전이하는 설정을 제안하고, 불일치 데이터 쌍으로 학습해 제품에 무관한 결함 임베딩을 분리해 낸다. 여기에 결함 유형 필터링, 생성 위치·기하 타당성을 제어하는 adaptive mask 파이프라인, 픽셀 단위 라벨을 만드는 학습 불필요 labeling 모듈을 더했다. MVTec-AD·VisA와 전용 anomaly-transfer 벤치마크에서 더 현실적인 결함을 생성하고 zero-shot·few-shot 이상 탐지 성능을 향상시켰으며, 코드와 모델을 공개할 예정이다.

**태그**: anomaly-detection, industrial-inspection, defect-detection, generative

---

### [MAOL: Morphology-Aware Ordinal Learning for Fine-Grained Industrial Defect Severity Grading](https://arxiv.org/abs/2609.02266)

**한 줄 요약**: 결함 심각도 등급을 instance 단위 ordinal learning으로 정식화하고 형태 특징과 클래스별 적응 임계값을 결합한 프레임워크.

**핵심 기여**: 산업 검사에서 결함 심각도 등급은 라벨이 순서형이고 형태 단서 의존도가 높으며, 2단계 파이프라인에서 학습 시의 깨끗한 annotation과 추론 시의 노이즈 섞인 예측 instance 사이에 불일치가 생긴다. MAOL은 이를 instance 수준 ordinal learning으로 정식화하고, 명시적 morphological feature로 표현 학습을 보강하며, 결함별 등급 경계를 모델링하는 class-conditional adaptive ordinal threshold와 localization perturbation을 이용한 prediction-aware training을 도입한다. clean-ROI와 predicted-instance 두 설정 모두에서 규칙 기반·nominal 분류·기존 ordinal baseline을 상회하고 특히 predicted-instance 설정에서 격차가 크며, IDA 2026 Challenge의 정밀 제조 심각도 등급 부문에서 3위를 기록했다.

**태그**: industrial-inspection, defect-detection, fine-grained, anomaly-detection

---

### [FuDU: A Fuzzy Dual-dimensional Uncertainty Framework for Streaming Active Learning in Industrial Defect Detection](https://arxiv.org/abs/2609.02212)

**한 줄 요약**: 이미지 수준과 박스 수준 불확실성을 fuzzy inference로 융합해 스트리밍 산업 영상에서 라벨링할 샘플을 고르는 active learning 방법.

**핵심 기여**: 실시간 산업 결함 검사에서는 연속 유입되는 영상 스트림에서 불확실한 샘플을 골라내야 검사 시스템의 신뢰도를 유지할 수 있다. FuDU는 백본에 정상/결함 feature prototype으로 이미지 수준 불확실성을 재는 PGUQ 모듈을, 검출 헤드에 박스 수준 불확실성을 재는 dual-entropy 평가기 DeUE를 각각 붙이고, 불확실성을 계통 오차로 모델링해 두 차원을 fuzzy inference로 융합하는 적응형 샘플링 전략을 제안한다. 핵연료봉 결함 검출을 포함한 실험에서 효율성과 유연성을 보였고, 코드가 공개돼 있다.

**태그**: industrial-inspection, defect-detection, object-detection, anomaly-detection

---

### [From Detection to Localization: A Unified Forensics Framework for Fully Synthetic and Tampered Images](https://arxiv.org/abs/2609.02640)

**한 줄 요약**: 진짜·완전 생성·부분 변조의 3분류와 변조 영역 분할을 하나의 프레임워크로 묶은 이미지 포렌식 방법.

**핵심 기여**: 조작 이미지 탐지는 보통 real vs. generated 이진 분류로 다뤄지는데, 이 틀에서는 조작의 형태를 구분하거나 위치를 짚어낼 수 없다. 이 연구는 기존 detector를 확장해 real / fully generated / tampered의 다중 클래스 판별로 바꾸고, segmentation branch를 추가해 변조 영역을 픽셀 단위로 국소화한다. 선정한 최신 벤치마크 대비 분류 정확도와 localization IoU 모두에서 개선을 보고하며, 코드가 GitHub에 공개돼 있다.

**태그**: forgery-detection, segmentation, image-embedding

---

### [Multi-Tool Image Editing Attribution in Facial Forgery](https://arxiv.org/abs/2609.02751)

**한 줄 요약**: 여러 편집 도구가 겹쳐 적용된 얼굴 이미지에서 사용된 도구들을 모두 식별하는 과제 정의와 50만 장 규모 데이터셋, 공간·주파수 기반 판별 방법.

**핵심 기여**: 기존 editing attribution 연구는 단일 도구 가정을 두어, 서로 다른 도구의 흔적이 합성·중첩되는 실제 다중 편집 상황을 다루지 못한다. 저자들은 다중 도구 편집 attribution(MIEA) 과제를 제시하고, face swapping(Deepfake)과 각종 얼굴 보정을 포함한 6종 편집 도구로 만든 50만 장 이상의 얼굴 이미지 데이터셋 MultiEdit을 구축했다. 데이터 분석에서 얻은 관찰을 바탕으로 설계한 DPEC는 공간·주파수 영역 모두에서 국소적 편집 흔적을 포착하고 오차 기반 curriculum learning으로 학습하며, 최대 5단계까지 편집된 얼굴 이미지에서 기존 9개 방법을 앞선다.

**태그**: forgery-detection, dataset-benchmark, fine-grained

---

### [SCULPT: Training Edge Vision Models for Post-Training Quantization Readiness](https://arxiv.org/abs/2609.01743)

**한 줄 요약**: FP32 미세조정 단계에서 활성값 분포의 왜도·첨도를 억제하고 clipping 경계를 학습해, 별도 QAT 없이 저비트 PTQ에 적합한 모델을 만드는 방법.

**핵심 기여**: 일반적인 FP32 학습은 heavy-tailed 활성값 분포를 만들고, 그 outlier가 활성값 양자화를 불안정하게 한다. 전체 범위를 보존하면 희귀한 극단값에 양자화 bin을 낭비하고, 강하게 clipping하면 정보를 잃는다. SCULPT는 양자화에 불리한 skewness·kurtosis를 억제하는 topology-aware 활성값 정규화 항과 percentile 기반 clipping 경계 학습을 평범한 FP32 미세조정에 결합한다. QAT와 달리 학습 중 양자화를 시뮬레이션하지 않고, 사후 outlier 보정 PTQ와 달리 런타임 활성값 변환을 요구하지 않으며, 학습된 clipping 경계를 표준 PTQ 워크플로에 그대로 넘겨 INT8과 W4A8 같은 저비트 배포에 쓸 수 있다.

**태그**: quantization, efficient-inference, foundation-model

---

### [GaLe: memory-efficient Global Approximate and Local Exact features](https://arxiv.org/abs/2609.02689)

**한 줄 요약**: feature map을 정확한 local 표현과 근사된 global 표현으로 나눠, 재학습 없이 사전학습 네트워크를 제약된 임베디드 기기에 올리는 추론 기법.

**핵심 기여**: 임베디드 기기 추론은 patch 기반 방식의 높은 연산 오버헤드와 근사 기반 방식의 정확도 손실 사이에서 선택을 강요받는다. GaLe는 feature map을 세부를 보존하는 local exact 표현과 장거리 의존성을 유지하는 global approximate 표현으로 분할해, 일반 tiling과 달리 CNN-transformer 하이브리드 모델의 global 연산과 attention을 지원한다. ImageNet에서 exact inference와 동등한 성능을 유지하면서 Cortex-M33에서 patch 기반 추론 대비 최대 65% 속도 향상과 90% RAM 절감을 달성했고, 분류·검출·생성 태스크에 걸쳐 적용 가능함을 보인다.

**태그**: efficient-inference, image-embedding, object-detection


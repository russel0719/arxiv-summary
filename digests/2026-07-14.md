# arXiv cs.CV Daily Digest — 2026-07-14 (KST)

- **전체 신규 논문 수**: 77편 (new 70 + cross-list 7)
- **선별 수**: 12편

## 오늘의 트렌드

오늘 배치는 **foundation model을 재활용·진단하는 흐름**이 특히 두드러진다. video diffusion backbone을 범용 perception 모델로 쓰거나(GenCeption), VGGT가 co-visibility를 암묵적으로 인코딩함을 프로빙하고, 갓 공개된 SAM 3의 zero/one-shot 한계를 정량화하는 등 "기존 대형 모델에서 무엇을 끌어낼 수 있는가"를 묻는 논문이 다수다. 두 번째 축은 **표현 학습·재식별·검색**으로, DINOv2/DINOv3·SigLIP·CLIP을 기반으로 fine-grained 인식(SubViT), 장기 ReID(REMIND, Animal ReID), 시각적 혼동성 기반 hard negative mining(SAN)이 나란히 등장했다. 세 번째 축은 **실서비스 배포·경량화**로, VLM을 heterogeneous 구조로 자동 변환하는 MOSAIC, 엣지 VLM 에너지 병목을 재정의한 프로파일링 연구가 실무적으로 눈에 띈다. 산업 응용에서는 JEPA 기반 태양광 패널 열화상 결함 분류가, open-vocabulary 계열에서는 프롬프트 정제만으로 소수 클래스 검출을 끌어올리는 C-GAP이 선별 기준에 부합했다. 3D 재구성(Glob3R, DGSfM, StereoSplat+)과 diffusion 생성 계열도 활발했으나 프로필 우선순위가 낮아 대부분 제외했다.

---

### [Subtoken Vision Transformer for Fine-grained Recognition](https://arxiv.org/abs/2607.09086)

**한 줄 요약**: 판별적 패치만 여러 subtoken으로 세분화해 fine-grained 인식 성능을 높이는 selective tokenization ViT.

**핵심 기여**: 표준 ViT가 각 패치를 단일 토큰으로 압축해 미세한 차이를 놓치는 문제를, 판별적 패치를 다중 subtoken으로 표현하고 나머지는 원래 토큰 시퀀스를 유지해 필요한 곳에 용량을 집중시키는 방식으로 해결한다. 2단계 학습(랜덤 attention head 기반 subdivision fine-tuning → informative attention map을 경량 single-map router로 distill)으로 추론 시 별도 backbone forward 없이 token-importance를 예측한다. Generalized Category Discovery에서 DINOv2의 novel-category 정확도를 CUB/Aircraft/Cars 평균 81.3%→84.7%로, 단 +0.5ms·+3.4% FLOPs만으로 향상시켰다.

**실무 관련성**: fine-grained 유사도·식별이 핵심인 제품/부품 인식에 직결되며, DINOv2 임베딩을 거의 그대로 쓰면서 국소 판별력만 강화하는 접근이라 기존 벡터 검색 파이프라인에 얹기 좋다.

**키워드**: fine-grained recognition, Vision Transformer, DINOv2, GCD, token selection

---

### [Video Generation Models are General-Purpose Vision Learners](https://arxiv.org/abs/2607.09024)

**한 줄 요약**: 대규모 text-to-video 생성 backbone을 feed-forward perception 모델로 재활용해 텍스트 지시로 다양한 비전 태스크를 수행하는 범용 비전 학습 패러다임(GenCeption).

**핵심 기여**: video diffusion backbone이 제공하는 spatiotemporal prior·vision-language alignment·확장성을 근거로, depth·surface normal·camera pose·referring segmentation·3D keypoint 등에서 전문 모델(DepthAnything3, SAM3, VGGT 등)과 대등하거나 우위를 보인다. V-JEPA/Video MAE 등 대안 pretraining 패러다임을 능가하고, 7~500배 적은 학습 데이터로 유사 성능을 내는 데이터 효율성을 보였다. 합성 인간 영상만으로 학습해도 실제 영상·OOD 객체(동물·로봇)로 일반화하는 emergent 특성도 확인했다.

**실무 관련성**: 하나의 backbone으로 depth/segmentation/pose를 텍스트로 스위칭하는 구조는 다목적 비전 서비스의 표현 학습 기반으로 매력적이며, self-supervised/foundation 표현이라는 관심사와 정확히 부합한다.

**키워드**: video diffusion, foundation model, general-purpose vision, self-supervised, zero-shot

---

### [SigLIP-HD by Fine-to-Coarse Supervision](https://arxiv.org/abs/2607.09488)

**한 줄 요약**: 고해상도 입력 없이 fine-to-coarse supervision만으로 표준 해상도에서 세밀한 시각 토큰을 얻는 SigLIP 2 개선.

**핵심 기여**: MLLM에서 해상도를 올려 계산·설계 비용을 키우는 대신, 중간 해상도 이미지의 coarse feature가 고해상도 버전의 fine-grained feature를 모방하도록 강제하는 매우 단순한 supervision을 SigLIP 2에 적용한다. 동일한 추론 예산에서 더 나은 시각 토큰을 생성하며, 특히 OCR 계열 벤치마크에서 baseline 대비 일관된 향상을 보였다.

**실무 관련성**: OCR/document AI와 이미지 임베딩 품질이 동시에 중요한 상황에서, 추론 비용 증가 없이 표현력을 끌어올리는 실용적 기법이라 배포 관점에서 이점이 크다.

**키워드**: SigLIP, representation learning, OCR, knowledge distillation, MLLM

---

### [REMIND: RE-Identification with Memory for INDoor Navigation](https://arxiv.org/abs/2607.09267)

**한 줄 요약**: pose/depth 없이 monocular RGB만으로 긴 시간 간격·시점/조명 변화에도 일반 객체를 재식별하는 DINOv3 기반 online tracker.

**핵심 기여**: frozen DINOv3 feature에 dual-bank multi-prototype appearance memory, part/background descriptor, 공간 co-occurrence 기반 neighbour-context reasoning, ambiguity-aware Hungarian assignment를 결합해 장기 multi-object re-ID를 수행한다. 자체 실내 데이터셋(통제된 재방문·동일 클래스 밀집 환경)에서 IDF1 90.35%로, VOS baseline 대비 약 20점, tracking-by-detection baseline 대비 36점 이상 우위를 보였다.

**실무 관련성**: self-supervised 임베딩(DINOv3) + 프로토타입 메모리로 재식별을 구성하는 설계는 제품/객체 재식별과 retrieval 파이프라인 구축에 그대로 참고할 수 있다.

**키워드**: re-identification, DINOv3, appearance memory, metric learning, tracking

---

### [REBASE: Reference-Background Subspace Elimination for Training-Free In-Context Segmentation](https://arxiv.org/abs/2607.09082)

**한 줄 요약**: 참조 이미지의 배경 subspace를 제거해 문맥 오정합을 억제하는 training-free in-context segmentation.

**핵심 기여**: 단일 annotated 참조 이미지로 새 카테고리를 추론 시점에 도입하는 in-context segmentation에서, 참조-쿼리가 공유하는 배경이 비-타깃 영역의 유사도를 부풀리는 문제를 지적한다. 참조 이미지의 low-rank 배경 feature subspace를 찾아 참조/쿼리 feature를 그 직교 보공간으로 closed-form 투영해 깨끗한 semantic matching을 얻고, similarity-weighted farthest-point sampling으로 positive prompt를 생성한다. 학습·파라미터 갱신 없이 PACO-Part/FSS-1000/ISIC2018 등에서 training-free SOTA를 달성했다.

**실무 관련성**: SAM 계열과 vision foundation model을 조합한 one-shot 세그멘테이션은, 라벨이 희소한 신규 제품/결함 영역을 재학습 없이 분할하는 데 유용하다.

**키워드**: in-context segmentation, training-free, SAM, one-shot, feature subspace

---

### [C-GAP: Class-Aware and Online Prompting Improves Vision-Language Models on Imbalanced Classes](https://arxiv.org/abs/2607.09008)

**한 줄 요약**: 언어 프롬프트를 반복 정제해 frozen open-vocabulary detector의 소수 클래스 검출을 개선하는 annotation-free 프레임워크.

**핵심 기여**: 재학습이나 추가 annotation 없이 프롬프트 품질만으로 class imbalance를 완화한다. scene description과 class-quantity를 결합한 composite caption baseline을 세우고, LLM이 이미지별 caption을 개별 정제하되 minority-class AP@0.5를 동적 임계값과 비교해 accept/tentative/regenerate로 triage한다. COCO에서 소수 클래스 AP@0.5를 composite baseline 대비 상대 ~81%(17.69→32.09) 향상시켰고, detector 가중치는 전혀 갱신하지 않는다.

**실무 관련성**: GroundingDINO 계열 open-vocab detector를 그대로 두고 프롬프트만으로 희귀 클래스 성능을 끌어올리는 접근이라, 라벨이 부족한 산업 검출 문제에 저비용으로 적용할 수 있다.

**키워드**: open-vocabulary detection, prompt engineering, class imbalance, LLM, annotation-free

---

### [Promptable Concept Segmentation from Above: Evaluating SAM 3's Zero-Shot and One-Shot Capabilities in Remote Sensing](https://arxiv.org/abs/2607.09583)

**한 줄 요약**: 갓 공개된 SAM 3의 zero-shot/one-shot 능력을 원격탐사 분류·검출·분할에서 종합 평가하고 cross-modal 간섭을 진단.

**핵심 기여**: SAM 3의 decoupled binary presence head를 zero-shot 분류기로 재활용하는 구조적 변형을 제안하고, 텍스트/비주얼 프롬프트를 5가지 조합으로 분리해 멀티모달 디코더의 정합 메커니즘을 분석한다. 비주얼 프롬프트는 복잡한 지형 geometry에 디코더를 잘 정렬시키는 반면, 텍스트 프롬프트는 ground-level semantic bias를 주입해 좌표 회귀를 저해하는 심각한 cross-modal 간섭을 밝혔다. 자원 소모가 큰 학습 없이 평가하는 training-free proxy 프로토콜도 제시한다.

**실무 관련성**: SAM 3(신규 foundation model)의 open-vocab/one-shot 실전 한계와 프롬프트 모달리티별 특성을 파악할 수 있어, SAM 계열 도입 시 프롬프트 설계 판단에 참고가 된다.

**키워드**: SAM 3, open-vocabulary segmentation, zero-shot, prompt modality, foundation model

---

### [Joint-Embedding Predictive Architecture for Solar PV Panel Fault Classification](https://arxiv.org/abs/2607.09205)

**한 줄 요약**: JEPA 자기지도 표현과 EfficientNetV2 지도 특징을 융합한 태양광 패널 열화상(IR) 결함 분류 모델(JEFFNet).

**핵심 기여**: thermal IR PV 결함 분류의 class imbalance·제한된 텍스처·미세 열 차이 문제에, JEPA-pretrained ViT의 semantic 표현과 EfficientNetV2-S의 convolutional feature를 결합한 multibranch 구조를 제안한다. PVF-10에서 10-class F1 93.21(2-class 97.53), ISM에서 2-class F1 94.69를 달성했고, GEPFNet 대비 파라미터를 47.2% 절감(108.6M)했다.

**실무 관련성**: 산업 품질검사·결함/이상 탐지에 직결되며, self-supervised(JEPA)와 지도 특징을 융합해 라벨 불균형을 다루는 설계가 제조 검사 태스크로 이식 가능하다.

**키워드**: fault classification, anomaly detection, JEPA, self-supervised, thermal imaging

---

### [MOSAIC: Adaptive Inter-layer Composition for Efficient Heterogeneous Vision-Language Models](https://arxiv.org/abs/2607.09029)

**한 줄 요약**: homogeneous VLM을 하드웨어-aware 탐색으로 최적 heterogeneous 아키텍처로 자동 변환하는 경량화 프레임워크.

**핵심 기여**: linear/sparse/low-rank operator를 통합 search space로 두고, 다목적 Mixed Integer Programming으로 latency 제약 하 최적 layer 구성을 탐색한다. 구조 전이로 인한 성능 저하는 global off-policy distillation과 dual-teacher(235B oracle + 원본 4B teacher) on-policy distillation의 2단계 파라미터 복구로 완화한다. MOSAIC-4B는 Qwen3-VL-4B 대비 원본 학습비의 2% 미만으로 baseline 성능을 유지하면서 prefill 1.76×·decode 2.54× 가속을 달성했다.

**실무 관련성**: VLM 실서비스 배포에서 정확도를 지키며 latency를 줄이는 경량화/증류 파이프라인으로, 하드웨어 제약 배포 전략을 짤 때 참고 가치가 크다.

**키워드**: model efficiency, distillation, VLM, architecture search, deployment

---

### [Parameter-Efficient Vision-Language Adaptation with Continuous Metadata Conditioning for Animal Re-Identification](https://arxiv.org/abs/2607.09443)

**한 줄 요약**: 연속형 메타데이터를 프롬프트에 직접 조건화하는 파라미터 효율적 CLIP 적응 기반 동물 재식별.

**핵심 기여**: 장기 동물 ReID의 형태 변화·계절적 외형 변화에 대응해, low-rank visual adaptation·prompt supervision·cross-modal alignment 위에 numerical 메타데이터를 이산화하지 않고 연속 구조 그대로 프롬프트에 주입하는 metadata-conditioning을 핵심 기여로 제안한다. 학습 시 embedding space를 부드럽게 modulate하되 추론은 순수 시각 파이프라인을 유지하며, 7년 종단 어류 데이터셋과 다수 wildlife 벤치마크의 closed/open/time-aware 프로토콜에서 성능이 향상됐다.

**실무 관련성**: CLIP의 PEFT 적응 + metric learning으로 재식별을 구성하고 부가 메타데이터를 추론 없이 학습에만 활용하는 방식은, 제조/개체 재식별 표현 학습에 응용할 수 있다.

**키워드**: re-identification, CLIP, parameter-efficient fine-tuning, metric learning, metadata conditioning

---

### [Semantic Hardness Is Not Visual Hardness: Sign-Aware Hard Negative Mining for Sign Language Retrieval](https://arxiv.org/abs/2607.09263)

**한 줄 요약**: 언어적 유사도가 아니라 임베딩 공간의 시각적 혼동성으로 hard negative를 구성하는 검색 기법(SAN).

**핵심 기여**: fine-grained 검색 실패를 negative distribution mismatch로 정식화하며, 의미적으로 다르지만 시각적으로 혼동되는 샘플이 hard negative로 거의 다뤄지지 않고 텍스트 기반 마이닝으로는 이런 시각적 모호성을 못 잡는다는 점을 짚는다. sign embedding 공간의 visual confusability를 기준으로 hard negative를 구성해, PHOENIX-2014T에서 coarse 정확도는 유지하면서 fine-grained 검색을 크게 개선했다.

**실무 관련성**: "시각적 혼동성 기반 hard negative"라는 아이디어는 fine-grained 유사도/metric learning과 FAISS 벡터 검색의 negative sampling 설계에 직접 이식 가능하다.

**키워드**: hard negative mining, retrieval, metric learning, contrastive learning, fine-grained

---

### [Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference](https://arxiv.org/abs/2607.09520)

**한 줄 요약**: 엣지 VLM 추론의 진짜 에너지 병목은 시각 토큰이 아니라 출력 토큰 수라는 것을 체계적 프로파일링으로 규명.

**핵심 기여**: 5개 모델·4해상도·2 하드웨어(RTX 3070, Jetson Orin NX)에 걸친 최초의 on-device VLM 에너지 프로파일링을 수행했다. (1) 평균 추론 전력은 입력에 무관한 모델 고유 상수(변동 <5%), (2) 출력 토큰당 wall-clock 비용이 입력 토큰의 11~39배(prefill/decode 비대칭), (3) 이미지 복잡도(객체 수)에 따른 에너지 차이도 실은 출력 길이 차이에서 기인한다. 따라서 visual token pruning은 최대 10%만 절감 가능한 반면, 출력 길이 제어로는 최대 97% 에너지를 절감할 수 있다.

**실무 관련성**: 엣지 VLM 배포 최적화의 우선순위를 "시각 토큰 줄이기"에서 "출력 길이 제어"로 재조정해야 한다는, 곧바로 실행 가능한 통찰을 제공한다.

**키워드**: edge inference, VLM, energy efficiency, deployment, token pruning

# arXiv cs.CV Daily Digest — 2026-09-16 (arXiv 공개일)

- **전체 신규 논문 수**: 123편 (new 94 + cross-list 29)
- **선별 수**: 11편

## 오늘의 트렌드

멀티모달 LLM의 환각 진단·근거 지역화와 도메인별 추론 벤치마크가 가장 두꺼운 군집이고, Gaussian Splatting·occupancy·SLAM 등 기하 복원, 의료 영상 분할·진단, 로봇·자율주행용 행동 모델이 뒤따른다. 방법론으로는 동결된 사전학습 표현 위에 어댑터·프롬프트·폐형식 후처리만 얹어 backbone을 건드리지 않는 적응, 주파수·잔차 단서를 의미 표현과 결합하는 이중 스트림 설계, 양자화·토큰 선택·증류로 추론 비용을 줄이는 배포 최적화가 반복된다.

---

### [Multi-modal Knowledge Preserving Adapter for Embedding Backward Compatibility](https://arxiv.org/abs/2609.16875)

**한 줄 요약**: backbone을 전혀 갱신하지 않고 어댑터만으로 구형 데이터베이스 임베딩과의 backward compatibility를 확보해, 임베딩 모델 교체 시의 전체 재색인을 없애는 MKP-Adapter.

**핵심 기여**: 임베딩 모델을 업그레이드하면 새 query 임베딩이 기존 데이터베이스 임베딩과 호환되지 않아 비싼 재색인이 필요하고, 기존 Backward Compatible Training(BCT)은 학습 비용·성능 회귀 위험·독점 가중치 접근 제약 때문에 backbone 갱신을 전제한다는 점을 문제로 삼는다. MKP-Adapter는 MLLM 대상 최초의 adapter-only BCT로, 어댑터만 쓸 때의 핵심 난점을 "backward compatibility를 강제하면서 새 임베딩의 지식을 보존하는 것"으로 규정하고, BCT 전 과정에서 두 임베딩 공간의 기하 구조를 유지하는 multi-level preservation loss와 어려운 샘플에 가중치를 주는 focal re-weighting을 결합한다. 이미지·텍스트·visual document·비디오 검색 벤치마크와 여러 모델 종류에서 backward compatibility를 보고하며, 사전 추출된 임베딩만으로 학습되고 원 backbone forward 대비 추가 지연이 미미하다고 밝힌다.

**코드**: 불명

**태그**: image-embedding, image-retrieval, peft, continual-learning, foundation-model

---

### [Hub-Spectral Activation of Latent Multimodal Knowledge](https://arxiv.org/abs/2609.17094)

**한 줄 요약**: 동결된 멀티모달 표현에서 hub 연결의 2차 통계만으로 모달리티 간 잠재 대응 성분을 폐형식으로 복원해, 학습 없이 cross-modal 검색 성능을 끌어올리는 HSA.

**핵심 기여**: hub 기반 binding은 쌍별 지도 비용을 줄이지만, 각 모달리티가 hub와 따로 연결되어 있을 뿐 직접 공동 학습이 없으면 모달리티 간 정렬이 보장되지 않는다는 문제에서 출발한다. HSA는 이 잠재 지식을 source-induced cross-modal dependence로 정식화하고, 두 hub edge의 2차 통계로 결정되는 hub-readable 성분을 규정해 그 차원이 hub 공분산 rank로 제한됨을 보인다. 방법은 hub-edge 통계를 합성·표준화하고 짝지어진 spectral direction을 추출한 뒤, 신뢰도 가중 매칭 근거와 source-gated 후보 해소를 결합해 양방향 검색과 prototype 분류에 쓰며, 목표 쌍 지도·경사 최적화·backbone 갱신을 요구하지 않는다. ImageBind와 LanguageBind 위 19개 검색 관계에서 평균 양방향 Recall@10을 18.27%에서 31.15%로, 11개 prototype 분류 관계에서 macro Top-1을 29.01%에서 52.43%로 올린다.

**코드**: 공개([HSA](https://github.com/Luo1Yan/HSA))

**태그**: image-retrieval, image-embedding, training-free, foundation-model

---

### [FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation](https://arxiv.org/abs/2609.16591)

**한 줄 요약**: 대조 정렬과 양방향 cross-modal 생성 목적을 한 번의 사전학습에서 함께 최적화해, 검색용 판별 표현과 생성 조건으로 동시에 쓰이는 가변 길이 1D 멀티모달 임베딩을 학습하는 FLAT.

**핵심 기여**: 대조·자기지도 시각 인코더를 먼저 학습하고 생성 모델을 따로 붙이는 2단계 구성은 동결된 임베딩이 생성 성능의 병목이 된다는 점을 지적하고, 표현학습과 생성을 공동으로 다시 본다. FLAT은 공유 멀티모달 인코더를 text-to-image·image-to-text 디코더와 함께 최적화하고, 시각·텍스트 입력을 하나의 연속 1D 시퀀스 공간으로 매핑한 뒤 prefix-K 토큰에 nested dropout을 적용해 출력 길이를 가변화한다. 단일 사전학습 단계만으로 다양한 prefix K에서 검색과 생성을 수행해 T2I GenEval 71.1을 얻고, 과제별 미세조정 후 GenEval 83.1, MS-COCO 캡셔닝 BLEU-4 40.5·CIDEr 138.6, MS-COCO Recall@5 86.8(I2T)/75.8(T2I), Flickr30K 98.3/93.6을 보고한다. 표현이 선형 보간, 잠재 공간 연산, zero-shot composed retrieval을 지원함을 정성적으로 보인다.

**코드**: 불명

**태그**: image-embedding, image-retrieval, metric-learning, generative

---

### [RegRet: Enhancing Region-Level Retrieval in Large Multimodal Models](https://arxiv.org/abs/2609.16847)

**한 줄 요약**: 전역 검색 성능을 유지하면서 사용자가 지정한 이미지 영역 단위의 표현을 강화해, 영역 대 영역·영역 대 텍스트 검색을 수행하는 LMM 기반 프레임워크와 REGMB 벤치마크.

**핵심 기여**: 최근 LMM 기반 멀티모달 검색은 전역 수준 과제에 집중되어 있어 영역 단위 표현을 제대로 포착하지 못하고, 이는 상품 검색·RAG처럼 이미지 일부를 질의로 쓰는 응용에서 제약이 된다는 점을 문제로 삼는다. RegRet은 세밀한 영역 특징과 전역 배경 맥락을 함께 담는 Region-Aware Encoder를 두고, 국소 상세 캡셔닝과 영역 단위 대조학습을 포함한 다단계 학습 파이프라인으로 표현의 변별력을 높인다. 영역 단위 대조 학습 데이터와 평가 과제 다양성이 부족한 상황을 보완하기 위해 4개 멀티모달 검색 과제, 22.5만 대조 쌍으로 구성된 REGMB 벤치마크를 함께 공개한다. zero-shot 설정에서 강한 baseline을 앞서고, 대조학습을 추가하면 REGMB와 공개 벤치마크에서 평균 20% 이상 향상되면서 전역 검색 성능은 동등하거나 개선된다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, fine-grained, metric-learning, vlm

---

### [DenseFace: Bias Mitigation in Face Recognition via Density-Aware Probabilistic Matching](https://arxiv.org/abs/2609.16149)

**한 줄 요약**: 인물별 얼굴 임베딩을 von Mises-Fisher 분포로 모델링하고 분포 밀도 차이를 반영한 확률적 매칭 절차로 바꿔, 재학습 없이 사전학습 얼굴 인식 모델의 인종 편향을 줄이는 DenseFace.

**핵심 기여**: 기존 편향 완화 기법들이 학습 절차에 제약을 걸어 인식 정확도를 떨어뜨린다는 점을 문제로 삼고, 사전학습된 모델을 그대로 두고 매칭 단계만 바꾸는 접근을 제안한다. 각 인물의 얼굴 임베딩을 von Mises-Fisher 분포로 모델링한 뒤 인구통계 속성과 분포 밀도 사이의 의존성을 관찰하고, 이 밀도 차이를 반영한 확률적 매칭 절차를 설계한다. 네트워크 구조·학습 데이터셋·손실 함수가 서로 다른 강한 얼굴 인식 모델들에서 일관되게 인종 편향이 줄었고, 인식 정확도는 보존되며 기반 모델의 재학습이 필요 없다고 보고한다. 기존에 쓰이던 편향 측정 지표들도 함께 검토해 개선을 제안한다.

**코드**: 불명

**태그**: re-identification, image-embedding, metric-learning, calibration

---

### [InfoTaxa: Information-Calibrated Label-Free Clustering for Fine-Grained Visual Taxonomy](https://arxiv.org/abs/2609.17218)

**한 줄 요약**: 동결 시각 임베딩의 라벨 없는 군집화가 종(species) 수준에서 정체되는 원인이 방법 한계인지 정보 한계인지를, 정보량 대비 회수율과 DNA 감사 신호로 분리해 진단하는 분석 프레임워크.

**핵심 기여**: 동결 사전학습 임베딩의 라벨 없는 군집화는 생물다양성 모니터링으로 가는 확장성 있는 경로지만, 이미지 단독 fine-grained 분류에서 상위 분류 구조는 회복하면서 종 수준에서 일관되게 정체되는 실패 양상을 보인다는 관찰에서 출발한다. BIOSCAN-5M에서 BioCLIP 2 특징에 UMAP과 HDBSCAN을 적용해 과(family) 수준 AMI 0.79, 속(genus) 0.67을 얻어 기존 이미지 baseline을 크게 넘고 oracle-K·그래프 기반·학습형 군집 헤드와 동등한 수준을 보인다. InfoTaxa는 비지도 분할이 회수한 probe 추정 이미지 정보의 비율(clustering efficiency)과, 추론 입력이 아닌 감사 신호로만 쓰는 짝지어진 DNA를 결합해 진단하며, 밀도 기반 파이프라인이 목(order)·과 수준에서 이미지 가용 정보의 약 0.90·0.81을 회수함을 보인다. 이미지 임베딩에 DNA를 더하면 종 수준 예측 오차가 약 2비트 줄어, 종 수준 군집화가 군집화 한계와 표현 한계에 동시에 묶여 있다고 결론짓는다.

**코드**: 불명

**태그**: fine-grained, image-embedding, calibration, image-retrieval

---

### [Unifying Semantic Priors and High-Frequency Traces: Enhancing V-JEPA with Mixture-of-Experts for Robust Synthetic Image Forensics](https://arxiv.org/abs/2609.16778)

**한 줄 요약**: V-JEPA 2 backbone에 Residual Mixture-of-Experts와 노이즈 스트림을 붙여 의미 사전지식과 고주파 흔적을 함께 쓰는 딥페이크·합성 이미지 판별 이중 스트림 구조.

**핵심 기여**: 현대 딥페이크 판별기는 ViT로 저수준 불일치를 포착하지만, foundation model의 전역적 이해만으로는 특히 압축되거나 소셜 미디어를 거친 이미지에서 진짜와 가짜를 구분하기 어렵다는 점을 문제로 삼는다. 이 논문은 JEPA 계열 모델을 딥페이크 판별에 처음 적용해, world model이 학습한 일반화된 시각 표현이 판별기의 강한 사전지식이 될 수 있다는 가설을 세우고 실증한다. MoE-JEPA는 V-JEPA 2 backbone에 Residual MoE와 노이즈 스트림 분기를 더해 포렌식 지식을 동적으로 내재화하고, Gated Attention 기반 Multiple Instance Learning 모듈로 공간적 의미 이해를 확보한다. AI 생성·변조·진짜 이미지 30만 장으로 구성된 SID-Set 벤치마크에서 정확도 95.54%로 훨씬 큰 모델들을 앞선다.

**코드**: 불명

**태그**: forgery-detection, ssl-backbone, foundation-model, anomaly-detection

---

### [PSMP-CLIP: Patch-Prompt SAM and Multi-Semantic Prompting for CLIP-Based Zero-Shot Anomaly Detection](https://arxiv.org/abs/2609.16785)

**한 줄 요약**: 중간 patch feature에서 직접 prompt를 뽑아 SAM2로 정밀 마스크를 만들고, 의미 앵커로 제약한 다중 학습 prompt를 결합한 CLIP 기반 zero-shot 이상 탐지.

**핵심 기여**: 대상 도메인 샘플 없이 이상 영역을 지역화하는 zero-shot anomaly detection에서, 기존 CLIP 기반 방법은 이상 맵이 거칠고 의미 prompt가 제한적이라는 문제를 지적한다. PSMP-CLIP은 patch-prompt SAM2 분할(PPSS)과 multi-semantic guided prompt regularization(MSGPR)을 통합하는데, PPSS는 중간 patch feature에서 직접 prompt를 샘플링해 임계값 드리프트를 피하면서 SAM2가 정밀한 마스크를 내도록 유도하고, MSGPR은 의미 앵커로 제약된 복수의 학습 가능한 prompt로 일반화를 보존한다. 14개 데이터셋 실험에서 경쟁력 있는 성능을 보이며, MVTec AD·BTAD·DTD-Synthetic·CVC-ClinicDB·TN3K·Endo·Kvasir에서 픽셀 수준 AUROC 최고치를 기록한다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, segmentation, training-free

---

### [CLARE: Scalable Class-Incremental Continual Learning via a Sparsity-Based Framework](https://arxiv.org/abs/2609.17026)

**한 줄 요약**: 과제마다 희소한 임계 파라미터 마스크를 먼저 찾고 그 마스크 안에서만 미세조정해, 공유 어댑터 공간에 여러 과제를 누적하면서 과제 간 간섭을 줄이는 class-incremental continual learning 프레임워크.

**핵심 기여**: 사전학습 모델 활용이 continual learning을 크게 진전시켰지만, 많은 과제를 순차 학습할 때 과제 간 간섭과 가소성 손실로 성능이 떨어지는 확장성 병목이 남아 있다는 점을 문제로 삼는다. 희소 미세조정이 전체 미세조정에 필적한다는 관찰에 근거해, CLARE는 sparsity-inducing 목적으로 과제별 임계 파라미터 마스크를 식별하는 단계와 그 마스크로 선택된 파라미터만 최적화하는 mask-constrained 미세조정 단계로 동작한다. 이 2단계 희소 어댑터 기제는 모든 과제를 하나의 공유 어댑터 공간에 누적하면서 파괴적 간섭을 줄인다. 긴 과제열 벤치마크 Omnibenchmark-1k에서 100개 과제 학습 후 최종 정확도가 EASE 대비 4.64%·13.34% 향상된다고 보고한다.

**코드**: 불명

**태그**: continual-learning, peft, foundation-model

---

### [Symmetry-Aware Likelihood-Orbit Aggregation for Selective Left-Right Claim Verification](https://arxiv.org/abs/2609.17004)

**한 줄 요약**: 반사·역관계·개체 교환으로 생성한 여덟 개 정규화 우도를 학습 파라미터 없는 폐형식 대비로 묶고, Clopper-Pearson 상한 신뢰구간으로 고른 임계값을 넘을 때만 주장을 단정하는 선택적 검증 방식.

**핵심 기여**: 동결 VLM은 좌우 관계 같은 세밀한 공간 주장에서 신뢰도가 낮고, 원시 우도만으로는 검증 오류를 안정적으로 순위화하지 못한다는 문제에서 출발한다. Relation-Orbit은 수평 반사 개입을 고정한 뒤, 반사·역관계·개체 교환으로 결정되는 질의 지지 역할과 반사실 역할에 여덟 개 정규화 우도를 배정하고, 학습된 융합 파라미터 없이 폐형식 대비를 계산한다. 주장은 이 부호 있는 대비가 held-out 데이터에서 pointwise Clopper-Pearson 상한 신뢰구간으로 선택한 임계값을 넘을 때만 단정된다. 네 개 동결 VLM과 VSR·GQA에서 선택적 위험 10% 목표 하에 여덟 개 데이터셋-backbone 조합 전부에서 all-eight Orbit-Max baseline보다 높은 평균 테스트 coverage를 얻으며, 축소 orbit 대조군과 양측 분할 진단으로 구조적 이점을 추가 분석한다.

**코드**: 불명

**태그**: calibration, vlm, training-free

---

### [Channel-Wise and Token-Aware Post-Training Quantization for Visual State Space Duality](https://arxiv.org/abs/2609.16656)

**한 줄 요약**: VSSD 백본의 저비트 병목을 활성값 양자화로 특정하고, 입력 채널별 clipping 경계를 token-balanced 재구성 손실로 학습하는 post-training quantization 기법.

**핵심 기여**: Mamba 계열 state space model이 vision으로 확장됐지만 VSSD의 저비트 post-training quantization 거동은 충분히 이해되지 않았다는 점에서 출발한다. VSSD-Tiny에서 가중치·활성값을 분리 분석해 저비트 병목이 활성값 양자화임을 확인하고, 선택된 선형 계층 입력이 강한 채널별 크기 편차와 토큰 국소적 극단값을 보인다는 관찰을 얻는다. 제안하는 CTOAC는 해당 선형 출력에 대한 token-balanced 재구성 손실을 최소화해 입력 채널별 clipping 경계를 학습하며, 선택된 선형 계층과 그 입력 활성값만 양자화하고 나머지 backbone 연산은 원 정밀도를 유지한다. VSSD-Tiny·Small·Base에서 ImageNet-1K 정확도를 유지하고 공격적인 정밀도 설정에서 baseline보다 강건하며, COCO·ADE20K의 검출·분할 성능도 보존하고 RTX 4090 배포 설정에서 FP32 대비 최대 1.42배 속도 향상을 보고한다.

**코드**: 불명

**태그**: quantization, efficient-inference, foundation-model, object-detection

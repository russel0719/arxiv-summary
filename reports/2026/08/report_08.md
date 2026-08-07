# arXiv cs.CV Daily Digest — 2026-08-08 (KST)

- **전체 신규 논문 수**: 132편 (new 108 + cross-list 24)
- **선별 수**: 9편

## 오늘의 트렌드

오늘 목록은 비디오 생성·world model(다수의 audio-visual 생성기, JEPA/autoregressive video, 로봇 world-action model)과 MLLM 기반 long-video 이해·frame selection, 그리고 3D Gaussian splatting·의료영상(분할·리포트 생성)이 수적으로 압도적이었다. 관심사 관점에서 건질 만한 흐름은 **frozen foundation-model 특징(DINOv3·CLIP·SigLIP2)을 재학습 없이 다운스트림(분할·검색·이상탐지)에 재사용하고, 필요한 부분만 얇은 어댑터·LoRA·프롬프트로 적응하는 "adapt, don't retrain"** 기조다. 구체적으로 few-shot 산업 이상탐지, training-free open-vocab 분할, LVLM 기반 멀티모달 검색, SSL 인코더의 지름길(shortcut)·생성이미지 탐지 특성 분석이 눈에 띄었고, 배포 측면에서는 profiling 기반 pruning·mixed-precision quantization 자동화와 PEFT/VPT 계열이 이어졌다. SAM3가 처음 등장(적대적 강건성 관점)한 점도 참고할 만하다.

---

### [ConceptADapt: Concept-guided Adaptive Feature Reconstruction with Dynamic Attention for Few-Shot Industrial Anomaly Detection](https://arxiv.org/abs/2608.05743)

- **한 줄 요약**: 소수의 정상 샘플만으로 foundation-model 특징을 재보정해 결함을 검출·국소화하는 few-shot 산업 이상탐지 모델.
- **핵심 기여**: 제한된 support 특징에서 고정된 정상 concept 집합을 사전학습하고 query 특징과의 관계를 마이닝해 test-time에 통계를 재보정한다. low-data에서 심한 feature shortcut을 완화하기 위해 sparse autoencoder와 결합한 dynamic attention으로 강건한 정상 concept를 학습하고, attention 모듈에 LoRA만 얹어 최소 파라미터로 빠르게 적응한다. MVTec-AD·VisA·MPDD 세 벤치마크에서 검출·국소화 모두 SOTA를 갱신했다.
- **태그**: anomaly-detection, industrial-inspection, defect-detection, foundation-model, peft

---

### [Invisible Shortcuts: Why Vision Encoders Know Your Camera](https://arxiv.org/abs/2608.05424)

- **한 줄 요약**: 대규모 사전학습이 픽셀 단위 메타데이터 흔적과 의미의 상관을 학습시켜 비전 인코더가 카메라·처리 흔적에 민감해짐을 보이고 완화책을 제시한 연구.
- **핵심 기여**: ImageNet 라벨이든 LAION 캡션이든 대규모 의미 supervision이 metadata-semantics 상관을 유도하며, 상관이 강할수록 메타데이터 흔적 민감도와 분포 이동 하 성능 저하가 함께 커짐을 통제 실험으로 입증한다. 사전학습 중/후 완화 전략으로 미관측 메타데이터에 대한 민감도까지 낮추면서 downstream 성능을 유지했다. 흥미롭게도 이 민감도가 일부 인코더의 생성이미지 탐지 능력을 부분적으로 설명하고, 완화 시 OOD 일반화가 오히려 향상된다.
- **태그**: ssl-backbone, forgery-detection, image-embedding, foundation-model

---

### [Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval](https://arxiv.org/abs/2608.06060)

- **한 줄 요약**: 초기 검색 결과를 되짚어 오분류 단서를 분석하고 재랭킹·재검색하는 LVLM 기반 통합 멀티모달 검색(UniME-R1) 프레임워크.
- **핵심 기여**: query만 설명하던 기존 CoT와 달리, retrieval feedback에 조건화한 Retrieval-Centric CoT를 생성해 embedder가 혼동한 판별 단서를 짚어낸다. target이 top-k 안에 있으면 후보를 직접 재랭킹하고, 없으면 RC-CoT로 검색 방향을 보정한 뒤 dual-mode embedder로 전체 코퍼스를 재검색한다. hard negative를 마이닝해 실제 검색 실패를 시뮬레이션하고 supervised + retrieval-oriented RL로 adviser를 정렬해 MMEB-V2 등에서 일관된 향상을 보였다.
- **태그**: image-retrieval, metric-learning, image-embedding, vlm

---

### [Context Matters: Support Set Selection and Failure Detection for In-Context Medical Image Segmentation](https://arxiv.org/abs/2608.05333)

- **한 줄 요약**: DINOv3 임베딩 유사도로 support set을 고르고 분할 실패를 사용 전에 예측해 in-context 분할의 신뢰성을 높인 연구.
- **핵심 기여**: in-context 분할에서 무작위 샘플링 대신 query와의 시각 유사도 기반 exemplar 검색이 특히 support가 작을 때 일관되게 우수함을 보인다. 또한 query와 support 이미지만으로 IoU 임계 미달(분할 실패) 여부를 예측하는 transformer 분류기를 학습해 사용 전에 실패를 예상한다. DINOv3 임베딩 + MultiverSeg로 4개 벤치마크·3개 모달리티에서 검증했다.
- **태그**: image-retrieval, ssl-backbone, metric-learning, segmentation

---

### [SCI-CLIP: Segment-Centric Inference with Reference Memory for Training-Free Open-Vocabulary Segmentation](https://arxiv.org/abs/2608.05627)

- **한 줄 요약**: frozen CLIP 특징을 segment 단위 추론으로 조직화해 학습 없이 open-vocab 분할을 수행하고 exemplar 검색으로 보정하는 프레임워크.
- **핵심 기여**: patch 단위로만 나오는 frozen VLM 특징을 region-consistent interaction graph로 묶고 그래프 전파로 dense 특징을 재구성하며, 국소 증거가 부족한 곳만 cross-window support로 보강한다. 같은 segment 추상화로 offline reference memory를 구성·질의해 exemplar 검색을 예측 단위와 정렬함으로써, 학습 없이 8개 벤치마크에서 dense 예측의 구조 품질·문맥 추론·exemplar 보정을 개선한다.
- **태그**: segmentation, foundation-model, image-retrieval, open-vocab-detection

---

### [A Paragraph is Worth a Thousand Captions: Rethinking Text Supervision for Vision-Language Retrieval](https://arxiv.org/abs/2608.05260)

- **한 줄 요약**: 짧은 캡션 대신 문단 수준 텍스트로 대조학습하면 긴 설명 기반 이미지 검색 성능이 크게 오름을 체계적으로 분석한 연구.
- **핵심 기여**: Qwen2-VL/Llama-3.2로 CC3M 500K에 다양한 캡션·hard negative·품질 점수 문단을 합성하고, vision encoder는 얼린 채 BLIP text encoder만 파인튜닝해 text granularity의 효과를 분리했다. 문단 supervision은 아키텍처 변경 없이 Long-CLIP-L과 동급~DOCCI에서 14점 이상 우위를 보였고, 캡션-only 학습은 60토큰 이후 성능이 저하되며, text-only 파인튜닝에서는 hard negative가 오히려 해로웠다.
- **태그**: image-retrieval, metric-learning, image-embedding, vlm

---

### [Adapting Vision Foundation Models with Cascaded Semantics](https://arxiv.org/abs/2608.05393)

- **한 줄 요약**: 손수 만든 기초 이미지 prior와 self-attention 의미를 주입해 ViT를 0.74% 파라미터만으로 적응시키는 visual prompt tuning 기법.
- **핵심 기여**: 랜덤 초기화되던 visual prompt에 color/texture/shape 등 고전 연산자 기반 기초 이미지 prior(입력 공간)와 self-attention map의 instance-aware 의미(특징 공간)를 주입하고, 두 prior를 ViT 적응 전 과정에 cascaded로 통합한다. 34개 challenging 분류 데이터셋에서 ViT 파라미터의 0.74%만 튜닝하고도 우수한 downstream 적응을 달성했다.
- **태그**: peft, foundation-model, ssl-backbone

---

### [APQF: Agentic Profiling-Guided Structured Pruning and Mixed-Precision Quantization with Adaptive Fine-Tuning](https://arxiv.org/abs/2608.05499)

- **한 줄 요약**: 레이어별 민감도를 프로파일링해 구조적 pruning·mixed-precision 양자화·정확도 복원을 하나로 자동화하는 LLM-guided 압축 파이프라인.
- **핵심 기여**: profiling agent가 비용 분포와 압축 민감도를 측정하고, LLM planner가 레이어별 pruning 비율·bit-width·복원 전략을 제안한 뒤 실행 전에 검증한다. CNN과 ViT 모두에 대해 training-aware pruning + quantization을 통합했으며, ImageNet에서 bit-operation을 13-18배 줄이면서 정확도를 유지하고 균일 압축 대비 우위를 보였다. 여러 오픈웨이트 LLM planner로도 재현된다.
- **태그**: quantization, efficient-inference, foundation-model

---

### [Universal Concept Disruption for SAM3 Image Segmentation](https://arxiv.org/abs/2608.05983)

- **한 줄 요약**: SAM3의 open-vocabulary concept 분할을 무력화하는 첫 범용 cross-concept 적대적 섭동(UCD)을 제안한 연구.
- **핵심 기여**: (image, noun-phrase) 쌍에서 단일 bounded 섭동을 학습해 SAM3를 concept-grounding 시스템 전체로 공격한다. text-conditioned 입력 경로 교란, prompt-공유 시각특징 발산 극대화, presence-gated concept 점수 억제, 잔존 마스크의 공간 유효성 붕괴를 동시에 수행하며, 5개 데이터셋에서 mask AP를 59.4→18.7로 크게 낮추고 SAM3.1·비디오 추론으로도 재최적화 없이 전이된다.
- **태그**: segmentation, foundation-model, adversarial-robustness, open-vocab-detection

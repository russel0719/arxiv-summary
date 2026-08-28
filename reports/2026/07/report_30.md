# arXiv cs.CV Daily Digest — 2026-07-29 (arXiv 공개일)

- **전체 신규 논문 수**: 104편 (new 88 + cross-list 16)
- **선별 수**: 11편

## 오늘의 트렌드

오늘은 새로운 SSL 백본 제안은 없었지만, 표현·검증 시스템을 **실전 조건에서 신뢰할 수 있게 만드는** 논문이 유난히 많았다. retrieval/re-ID의 노이즈 이웃 강건성(ANFI), 합성 데이터 기반 임계값 캘리브레이션의 한계 실증, 입력 품질에 따른 판정 임계값 조정, 열화 입력을 다운스트림 task 성능 기준으로 복원하는 TDIR 등 "판정 점수를 언제 믿을 수 있는가"를 다루는 작업이 눈에 띈다. 배포 측면에서는 경량 DETR의 완전 정수 추론, VLM vision token pruning 등 edge 최적화가 이어졌고, 딥페이크·AIGC 탐지는 reconstruction residual 증거 기반 탐지와 공격(morphing, black-box evasion) 양쪽에서 활발했다. 그 외 UAV-위성 cross-view geo-localization과 long-form video keyframe 선택이 각각 4편 이상 나올 만큼 붐비는 주제였다.

---

### [ANFI: Rethinking Neighbor Feature Interaction in Person Re-ID](https://arxiv.org/abs/2607.25407)

- **한 줄 요약**: re-ID에서 이웃 샘플과의 affinity만 쓰는 기존 feature interaction이 noisy neighbor에 취약함을 지적하고, discrepancy 관계까지 함께 모델링하는 적응형 이웃 상호작용(ANFI)을 제안.
- **핵심 기여**: affinity 관계만으로 이웃 특징을 융합하면 false positive 이웃이 섞일 때 표현이 오염된다는 문제를 분석하고, pairwise가 아닌 neighborhood 유사도에서 유도한 discrepancy 관계와 샘플별 적응 가중치로 이웃의 부정적 영향을 명시적으로 상쇄한다. Noisy Relation Supervision으로 노이즈 관계에 대한 강건성을 점진적으로 주입하며, 표준·cross-modal·cross-domain re-ID와 re-ranking 비교에서 일관된 우위를 보였다.
- **태그**: re-identification, image-retrieval, metric-learning

---

### [HOME: Robust Hough-space Matching Method for Structured and Textureless Videos](https://arxiv.org/abs/2607.25389)

- **한 줄 요약**: 이미지를 Hough 공간으로 변환해 선형 구조를 1D 극점 매칭으로 바꾸는 초경량·training-free 피쳐 매칭 프레임워크.
- **핵심 기여**: ORB류 포인트 피쳐가 실패하는 강한 선형 구조·textureless 장면에서, 전역 라인 구조를 Hough 공간의 안정적 local extrema로 사상해 복잡한 라인 매칭을 효율적인 1D 포인트 매칭으로 재정식화했다. 1D radial descriptor로 회전·평행이동 불변성을 수학적으로 보장하며, 기존 라인 기반 방법 대비 훨씬 빠른 속도로 homography 추정에서 강건한 정합을 보였다.
- **태그**: feature-matching, correspondence, efficient-inference

---

### [Few-Shot Open-Vocabulary Remote Sensing Segmentation via Textual Inversion](https://arxiv.org/abs/2607.25563)

- **한 줄 요약**: open-vocab segmentation이 특수 도메인에서 실패하는 원인이 모델이 아니라 "약한 텍스트 쿼리"임을 보이고, frozen 모델 위에서 few-shot textual inversion으로 클래스 임베딩을 복구.
- **핵심 기여**: 클래스명이 vision-language 임베딩 공간의 부정확한 주소 역할을 해서 생기는 성능 저하를 분리해내고, 자연어 rephrasing으로는 복구 안 되는 부분을 몇 장의 예시만으로 textual inversion하여 해결했다. 모델 파인튜닝 없이 추론은 텍스트 쿼리만으로 유지되며, 영향받은 카테고리의 mIoU를 3.9→39.4로 끌어올리고 8개 데이터셋에서 visual prompt 주입 방식의 few-shot 방법을 능가했다.
- **태그**: open-vocab-detection, segmentation, peft, fine-grained

---

### [On the Use of Synthetic Data for Threshold Calibration in Face Recognition](https://arxiv.org/abs/2607.25990)

- **한 줄 요약**: 얼굴 인증 시스템의 판정 임계값을 합성 데이터로 캘리브레이션하면 score 분포 꼬리(tail) 불일치 때문에 저FMR 구간에서 신뢰할 수 없음을 실증.
- **핵심 기여**: 국경 통제(EES)급 저FMR 운영점에서 genuine/impostor score 분포의 합성↔실데이터 정렬을 분석하고, 통제된 조건에서는 합성 캘리브레이션이 근사하지만 unconstrained 조건에서는 tail 불일치로 성능 저하와 morphing 공격 취약성이 커짐을 보였다. 캘리브레이션 결과가 합성 데이터셋 간에도 크게 달라져, 고보안 배포에는 대표성 있는 실데이터 검증이 필수라고 결론짓는다.
- **태그**: threshold-calibration, synthetic-data, re-identification, forgery-detection

---

### [Noise-Free One-Step LoRA for Task-Driven Image Restoration with Diffusion Priors](https://arxiv.org/abs/2607.25390)

- **한 줄 요약**: 사전학습 diffusion prior를 노이즈 없는 deterministic 1-step forward + LoRA로 적응시켜, 열화 이미지 복원이 다운스트림 인식 성능까지 개선되게 만든 task-driven restoration.
- **핵심 기여**: diffusion 기반 복원의 확률적 샘플링이 task 일관성을 해친다는 점을 짚고, deterministic one-step 추론에서 LoRA 적응은 일관된 이득을 주지만 ControlNet식 conditioning은 그렇지 않음을 보였다. multi-step 대비 빠르면서 분류·세그·검출에서 기존 TDIR을 능가하고, 실제 열화 이미지와 OCR에서도 일반화를 검증했다.
- **태그**: image-restoration, peft, foundation-model, ocr-document

---

### [Fine-Grained Food Image Understanding via Target-Aware Data Alignment](https://arxiv.org/abs/2607.25794)

- **한 줄 요약**: 웹 수집 이미지-텍스트 쌍의 도메인 갭·캡션 노이즈를 target-aware 데이터 선별 + VLM 캡션 정제로 해결해 fine-grained retrieval을 크게 개선한 데이터 중심 접근.
- **핵심 기여**: 타깃 분포에 시각적으로 맞는 학습 부분집합을 선별하고 VLM으로 캡션을 타깃 스타일로 재작성해 CLIP류 retrieval expert들을 학습시켰으며, expert 간 의견이 갈릴 때만 VLM을 호출하는 계층적 decision-level 융합을 제안했다. 캡션 정제만으로 평균 ~19% retrieval 성능 향상을 얻었고, 순수 VLM retrieval 대비 2배 이상의 점수를 훨씬 낮은 비용으로 달성했다.
- **태그**: fine-grained, image-retrieval, vlm

---

### [FunnelAL: Retrieve-then-Rank Active Learning for Single-Class Discovery](https://arxiv.org/abs/2607.25276)

- **한 줄 요약**: 추천시스템의 다단계 funnel 구조(임베딩 retrieval → 학습형 ranker → 탐색 전환)를 능동학습에 이식해, 대규모 코퍼스에서 단일 클래스 샘플을 최소 라벨링으로 발굴.
- **핵심 기여**: 긍정 예시 1장에서 시작해 임베딩 retrieval로 후보를 좁히고, batch precision이 높은 동안은 RankNet ranker를 exploit하다가 수확이 줄면 committee 기반 탐색(QBC)으로 자동 전환하는 cascade를 설계했다. 3개 벤치마크에서 최종 F1·annotation 효율·라운드 수 모두 최고였고, 현실적인 라벨링 오류율에서도 불확실성 기반 고전 기법보다 2~3배 느리게 열화된다.
- **태그**: active-learning, image-retrieval, image-embedding

---

### [Enabling Fully Integer-Only Inference for Lightweight Detection Transformers](https://arxiv.org/abs/2607.24981)

- **한 줄 요약**: 경량 DETR의 forward pass 전체(Softmax·GELU·LayerNorm 포함)를 정수 연산만으로 실행하는 최초의 fully integer-only 검출 트랜스포머 I-LW-DETR.
- **핵심 기여**: multi-scale projector 브랜치별 독립 activation scale을 주는 scale-preserving split convolution, 부호 의존 GELU 근사(SD-ShiftGELU), 안정적 정규화를 유지하는 constrained Shiftmax로 NPU·MCU에서 걸림돌이던 비선형 연산을 정수화했다. 모델 크기 ~3.6배, 연산량 한 자릿수 이상 절감에 정확도 저하는 완만한 수준으로 억제했다.
- **태그**: quantization, efficient-inference, object-detection

---

### [LaP-Forensics: Latent-Pixel Consistency Guided Multimodal Reasoning for Deepfake Detection](https://arxiv.org/abs/2607.25962)

- **한 줄 요약**: frozen Stable Diffusion의 inversion-reconstruction residual을 forensic 증거로 삼아, RGB 의미 정보와 융합해 딥페이크 탐지·artifact 위치·텍스트 설명까지 내는 프레임워크.
- **핵심 기여**: 생성 이미지가 고정된 reconstruction 기준과 얼마나 어긋나는지를 residual map으로 측정해, 표면적 artifact가 사라진 최신 생성물에도 남는 신호를 활용한다. Where-What-Why 구조의 설명 생성에 GRPO 보상(마스크 겹침 + 증거 참조)을 결합했고, UniversalFakeDetect cross-generator 탐지와 SynthScars artifact localization에서 경쟁력을 보였다.
- **태그**: forgery-detection, anomaly-detection, vlm

---

### [Image Quality Dependent Degradation for AI Systems](https://arxiv.org/abs/2607.25736)

- **한 줄 요약**: normalizing flow로 입력 이미지가 학습 데이터 분포에서 얼마나 벗어났는지(품질)를 추정하고, 그에 따라 검출 confidence threshold를 낮추는 fail-degraded 설계.
- **핵심 기여**: 노이즈·저조도 등 저품질 입력에서 미검출(치명적)과 오검출(회복 가능)의 비대칭 비용을 명시하고, 품질 추정치에 연동해 임계값을 조정함으로써 fallback 없이도 가장 치명적인 오류를 회피하는 시스템 설계 전략을 제시했다. SOTA 객체 탐지에 적용한 실험으로 실효성을 확인했다.
- **태그**: image-quality, threshold-calibration, object-detection

---

### [Face De-Identification: A Domain-Centric Survey from Capture to Processing](https://arxiv.org/abs/2607.25926)

- **한 줄 요약**: 얼굴 비식별화 연구를 물리(촬영 전)–센서(획득 중)–디지털(후처리) 도메인 전체 파이프라인 관점에서 통합 정리한 첫 서베이.
- **핵심 기여**: 픽셀 후처리 중심이던 기존 정리를 넘어 센서 내장 프라이버시 메커니즘과 물리적 은닉까지 포괄하는 도메인별 분류 체계를 세우고, 기존 평가 프로토콜을 정리하며 표준화된 벤치마크의 부재를 핵심 공백으로 지목했다. 문헌·데이터셋·코드를 모은 프로젝트 페이지를 유지한다.
- **태그**: de-identification, video, dataset-benchmark

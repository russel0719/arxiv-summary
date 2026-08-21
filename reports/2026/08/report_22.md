# arXiv cs.CV Daily Digest — 2026-08-22 (KST)

- **전체 신규 논문 수**: 86편 (new 66 + cross-list 20)
- **선별 수**: 8편

## 오늘의 트렌드

오늘은 비디오/3D/4D 생성모델과 로봇 VLA(vision-language-action) 논문이 물량의 큰 축을 차지했고, medical imaging 응용도 여느 때처럼 많았다. 그 속에서 관심 영역과 직결되는 sparse feature matching 논문이 2편(RIPE++, UPAL) 나온 것이 가장 눈에 띈다 — 하나는 positive pair만으로 detector·descriptor·matcher 전체를 약지도 학습하는 RL 접근, 다른 하나는 point+line 특징을 단일 경량 네트워크로 통합 추출하는 효율화 접근으로, 매칭 파이프라인의 '지도 신호 완화'와 '프론트엔드 경량화'라는 두 실무 병목을 각각 겨냥한다. 그 외에는 zero-shot VLM의 conformal 캘리브레이션이 클래스 조건부 안전을 보장하지 못한다는 감사(audit) 연구, training-free 추론 시 grounding bbox 정밀화, VLM 토큰 프루닝·projector-only 학습 같은 foundation model 효율화 기법이 실무 적용 관점에서 유용했다.

---

### [RIPE++: Reinforced Keypoint Learning from Positive Pairs Only](https://arxiv.org/abs/2608.19693)

- **한 줄 요약**: 카메라 포즈·depth·negative pair 없이 "같은 장면을 찍은 이미지 쌍"이라는 신호만으로 keypoint detector/descriptor와 매처(LightGlue)까지 강화학습으로 학습하는 약지도 sparse matching 파이프라인.
- **핵심 기여**: 기존 RL 기반 keypoint 학습(RIPE)이 의존하던 coarse binary reward와 negative pair 구성을 제거하고, 단일 positive pair 내부의 기하 일관성에서 reward와 penalty를 모두 유도하는 보상 설계를 제안했다. 같은 RL objective를 매칭 단계(LightGlue)로 확장해 MegaDepth1500 AUC@5를 56.58→59.65로 끌어올렸고, 부분 겹침만 있는 이미지 쌍으로 전체 sparse matching 파이프라인을 약지도 학습할 수 있음을 보였다. 포즈가 없는 저텍스처 medical 비디오에서도 학습이 가능함을 시연했으며 코드·데이터를 공개했다.
- **태그**: feature-matching, correspondence, ssl-backbone, metric-learning

---

### [Unified and Efficient Point-Line Local Features](https://arxiv.org/abs/2608.19894)

- **한 줄 요약**: keypoint·line segment·descriptor를 단일 경량 네트워크(UPAL)로 동시에 추출해 ALIKED+DeepLSD 대비 4배 속도·1/10 메모리로 SOTA급 매칭 성능을 내는 통합 로컬 특징 추출기.
- **핵심 기여**: 기존 point-line 파이프라인이 점·선을 별도 네트워크로 검출하고 CPU 휴리스틱에 의존하던 비효율을, 공유 백본 + 브랜치 구조와 LSD를 가속·개선한 후처리로 해결했다. 점·선 매칭과 pose estimation 양쪽에서 SOTA에 필적하거나 상회하면서 계산량을 크게 줄였고(4× speedup, 10× 메모리 절감), 코드를 공개했다 (Pollefeys 그룹).
- **태그**: feature-matching, correspondence, efficient-inference

---

### [Does Marginal Coverage Guarantee Class-Conditional Safety for Zero-Shot VLMs Under Shift?](https://arxiv.org/abs/2608.19376)

- **한 줄 요약**: CLIP/OpenCLIP/SigLIP의 zero-shot 예측에 conformal prediction을 abstention 레이어로 쓸 때, 분포 이동 하에서 marginal coverage는 유지돼도 클래스 조건부(worst-class) coverage는 0 근처까지 붕괴함을 보인 감사 연구.
- **핵심 기여**: ImageNet-Sketch에서 marginal coverage 0.86을 유지하면서도 worst-class coverage가 ≈0으로 떨어지는 실패 모드를 체계적으로 규명하고, 이 실패가 소스 도메인 진단 지표로는 예측되지 않음을 보였다. 소스 측 Mondrian·clustered conformal·Conf-OT 등 보정 기법이 tail을 복구하지 못하고, 타깃 측 클래스별 캘리브레이션만이 유효하지만 전 클래스 라벨이 필요함을 정리했다. 결론적으로 marginal conformal coverage를 "평균 신뢰도 통계"로만 취급해야 하며 클래스 tail의 안전 보장으로 쓰면 안 된다고 경고한다.
- **태그**: foundation-model, image-embedding, anomaly-detection, dataset-benchmark

---

### [Where Grounding Accuracy Lives on the IoU Curve: Label-Free Inference-Time Boundary Refinement](https://arxiv.org/abs/2608.19553)

- **한 줄 요약**: frozen grounding 모델의 예측 bbox를 라벨 없이 추론 시점에 정밀화하는 기법(LFPR) — 작게 예측된 영역을 고해상 재관찰·재grounding하고 기하 가드로 검증해 특히 엄격한 IoU(Acc@0.9)에서 큰 이득을 얻는다.
- **핵심 기여**: 참조 표현 grounding에서 "대상 식별은 맞지만 박스가 부정확한" 실패를 분리해, 예측 크기 기반 라우팅→컨텍스트 크롭 내 재grounding→고정 기하 가드→좌표 midpoint 융합의 training-free 연산자를 제안했다. Ref-L4에서 mAcc 72.9→76.0%, Acc@0.9 55.8→61.1%를 달성하고, 공개된 grounding 특화 모델에도 그대로 적용해 Acc@0.9를 최대 +6.7pt 개선했다(약 2배 지연 비용). 가드를 제거한 대조군이 전 지표에서 나빠짐을 보여 각 구성요소의 기여를 검증했다.
- **태그**: open-vocab-detection, object-detection, vlm, fine-grained

---

### [Far from the Crowd: Scalable Self-Supervised Learning via Geographic Isolation](https://arxiv.org/abs/2608.19766)

- **한 줄 요약**: 이미지 디코딩·모델 피드백 없이 메타데이터(지리적 고립도)만으로 샘플 난이도를 매겨 SSL 사전학습 커리큘럼을 구성, 20~40% 학습 예산으로 baseline 성능에 도달하는 방법.
- **핵심 기여**: MoCoV2(contrastive)와 MAE(reconstructive) 양쪽에 적용 가능한 O(D log D) 라벨-프리 커리큘럼을 제안해, visual complexity 기반 커리큘럼과 동등한 성능을 140배 낮은 사전 계산 비용으로 달성했다. BigEarthNet에서 최대 +5 mAP 등 downstream 개선과 함께, 커리큘럼 학습된 인코더가 더 고차원·균일한 임베딩 공간을 형성함을 CKA·effective-rank 분석으로 보였다. 원격탐사 도메인 실험이지만 "저비용 메타데이터 프록시로 SSL 데이터 순서를 제어한다"는 아이디어 자체는 일반적이다.
- **태그**: ssl-backbone, image-embedding, foundation-model

---

### [Clustering and Token Denoising for Faster and More Robust VLMs](https://arxiv.org/abs/2608.19285)

- **한 줄 요약**: attention 가중 클러스터링으로 대표 비주얼 토큰을 뽑고 residual shrinkage로 노이즈를 제거하는 training-free VLM 토큰 프루닝(ClustRS) — 토큰 97% 삭감에도 노이즈 환경에서 기존 기법 대비 최대 20% 우위.
- **핵심 기여**: score 기반과 diversity 기반 프루닝의 한계를 클러스터 단위 대표 토큰 선택 + 1-pass denoising 조합으로 극복했다. 재학습이 전혀 필요 없어 아키텍처 변경에 즉시 적용 가능하고, LLaVA-OneVision에서 1/3 미만 토큰으로 baseline 성능을 유지했다. 특히 다양한 이미지 노이즈 유형·강도에 대한 강건성을 명시적으로 평가한 점이 엣지 배포 관점에서 실용적이다.
- **태그**: vlm, efficient-inference, foundation-model

---

### [Projector Is All You Train](https://arxiv.org/abs/2608.19726)

- **한 줄 요약**: 멀티모달 LLM을 새 모달리티에 적응시킬 때 백본 파인튜닝 없이 projector만 학습해도 joint 학습과 대등한 성능을 내고, 기존 능력의 drift도 원천 차단됨을 보인 연구.
- **핵심 기여**: 3D MLLM 실험에서 projector-only 학습이 (1) joint 학습 대비 동등한 멀티모달 성능, (2) 언어 모델 기존 능력의 drift 회피, (3) 약 2배의 학습 샘플 처리량을 달성함을 보였다. "frozen 백본 + 얇은 연결부 학습"이라는 최소 개입 전략이 모달리티 적응에 충분하다는 실증으로, 여러 백본에서 재현했다.
- **태그**: peft, foundation-model, vlm, efficient-inference

---

### [ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation](https://arxiv.org/abs/2608.20122)

- **한 줄 요약**: 사람은 읽지만 모델은 놓치는 adversarial 시각 텍스트를 영역 단위로 검출·인식하는 grounded OCR 벤치마크(AdvSpot)와 2단계 학습 프레임워크(ArmorOCR).
- **핵심 기여**: 13개 세부 유형의 adversarial 텍스트를 region-level로 주석한 첫 grounded adversarial OCR 벤치마크를 구축하고, 변환된 관찰(privileged observation)로부터의 on-policy self-distillation + task 조건 reward GRPO로 LMM의 adversarial 텍스트 지각을 강화했다. 일반 OCR 성능을 유지하면서 adversarial 벤치마크 전반에서 일관된 개선을 보였다.
- **태그**: ocr-document, forgery-detection, vlm, dataset-benchmark

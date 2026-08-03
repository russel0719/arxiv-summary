# arXiv cs.CV Daily Digest — 2026-07-21 (KST)

- **전체 신규 논문 수**: 88편 (new 76 + cross-list 12)
- **선별 수**: 9편

## 오늘의 트렌드

오늘은 비디오 생성·장시간 비디오 이해(video LLM), event camera, medical imaging, remote sensing 계열이 물량의 큰 축을 차지했고, 새로운 SSL 백본 논문은 나오지 않았다. 대신 **frozen foundation model을 어떻게 잘 써먹을 것인가**를 파고드는 실전형 연구가 여럿 보인다: frozen 백본의 readout(aggregation)만 교체해 AIGV 탐지 성능을 되살리는 V-PVP, frozen VFM 위에 얹는 경량 멀티태스크 디코더 DPNeXt, VPR 파운데이션 모델의 token reduction 실증 벤치마크가 대표적이다. 증류(distillation) 계열도 두 편(스테레오 기하 prior를 monocular depth로 이식하는 EpiDistill, GT 박스를 privileged 신호로 쓰는 IoUPD)이 나와, foundation model의 배포·정련 기법이 꾸준히 축적되는 흐름이다. 산업·보안 응용에서는 cross-modality feature matching 기반 zero-shot 6D 포즈 추정(PIXIE)과 ID 문서 위조 탐지 대회 리포트가 눈에 띈다.

---

### [PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects](https://arxiv.org/abs/2607.16015)

- **한 줄 요약**: untextured 3D 모델과 RGB 이미지 한 장만으로, 사전학습된 cross-modality feature matcher를 이용해 학습 없이 6D 포즈를 추정하는 산업 환경용 zero-shot 프레임워크.
- **핵심 기여**: 참조 시점들에서 렌더링한 합성 depth/normal map과 쿼리 RGB 이미지를 사전학습된 cross-modality feature matcher로 매칭하고, 매칭된 keypoint를 back-projection해 2D–3D 대응을 만든 뒤 PnP로 포즈를 푼다. 기하 정보에만 의존하므로 조명·텍스처 변화에 본질적으로 강건하며, correspondence filtering으로 조립 결함 등 모델–실물 간 기하 편차까지 처리한다. texture-less 물체 공개 벤치마크에서 객체별 학습 없이 SOTA를 보고했고, 조립 결함·텍스처 변화·occlusion을 포함한 신규 데이터셋도 공개했다.
- **태그**: feature-matching, pose, industrial-inspection, foundation-model

---

### [Are All Tokens Necessary for Visual Place Recognition? An Empirical Study of Token Reduction for Efficient Inference](https://arxiv.org/abs/2607.15563)

- **한 줄 요약**: ViT/파운데이션 모델 기반 visual place recognition에서 token pruning·merging·hybrid 기법을 처음으로 체계적으로 벤치마크한 실증 연구.
- **핵심 기여**: 여러 SOTA VPR 모델과 도심·교외·자연 환경 데이터셋에 걸쳐 대표적 token reduction 기법들을 정확도, 연산량, 추론 속도, edge device 배포 효율 관점에서 종합 평가했다. 정확도 저하 1% 미만으로 연산량을 최대 29% 줄이고 throughput을 최대 44% 올릴 수 있음을 보이는 등 정확도–효율 트레이드오프에 대한 실용적 가이드를 제시한다. 코드·모델 공개 예정.
- **태그**: image-retrieval, efficient-inference, foundation-model, dataset-benchmark

---

### [Rethinking the Readout: Unlocking Video Backbones for AI-Generated Video Detection](https://arxiv.org/abs/2607.15321)

- **한 줄 요약**: frozen 비디오 백본의 global readout이 패치 수준 시간 역학을 뭉개버리는 것이 AI 생성 비디오 탐지 실패의 원인임을 밝히고, aggregation 층만 교체하는 0.5M 파라미터 readout(V-PVP)으로 이를 복원.
- **핵심 기여**: 비디오 사전학습 백본이 이미지 백본 probe보다 AIGV 탐지에서 오히려 밀리는 원인을 프레임을 단일 global descriptor로 압축하는 과도한 spatiotemporal aggregation으로 진단했다. 패치 velocity field 위에 두 개의 병렬 스트림을 두는 경량 readout V-PVP를 제안해, 백본을 완전히 frozen한 채 AIGVDBench에서 AUC 95.28을 달성했고, 다양한 백본·fine-tuning/linear probing 설정에서 일관된 plug-and-play 개선을 보였다.
- **태그**: forgery-detection, video, foundation-model, efficient-inference

---

### [The Third Competition on Document Forgery Detection on ID-Cards and Passports](https://arxiv.org/abs/2607.15734)

- **한 줄 요약**: ID카드·여권 위조 탐지(PAD) 국제 대회 3회차 결과 분석 — 63개 팀, 100개 이상 제출 모델을 합성 데이터 기반 트랙과 이종 도메인 공격 트랙에서 평가.
- **핵심 기여**: 합성 데이터로 학습하는 통제 조건 트랙과 도메인이 다른 이종 공격 시나리오 트랙 양쪽에서 우승팀(Incode)의 결과를 분석하고, 높은 정확도만이 아니라 다양한 공격 유형·촬영 조건에 걸친 일관성이 실전 PAD의 핵심임을 보였다. ID 문서 PAD 분야의 표준 벤치마크로 자리잡은 대회로, 현재 SOTA 수준과 남은 격차를 파악할 수 있는 자료다.
- **태그**: forgery-detection, dataset-benchmark, industrial-inspection

---

### [Reasoning-Guided Part-Level Visual Grounding via Reinforcement Learning](https://arxiv.org/abs/2607.15374)

- **한 줄 요약**: 객체→부위 순의 coarse-to-fine 추론과 self-check reflection을 도입한 part-level visual grounding 프레임워크로, 4B 모델이 7B grounding LLM과 SAM3를 능가.
- **핵심 기여**: MLLM이 부위(part) 단위 질의에 약한 원인을 객체–부위 계층 구조의 부재로 진단하고, 부모 객체를 먼저 찾은 뒤 그 안에서 부위를 찾는 OP-HRG 전략을 제안했다. 예측 crop을 다시 인코딩해 결과를 검증하는 reflection 단계와, 단계별 보상을 주는 part-aware GRPO 학습 프레임워크를 결합했다. PascalPart·PartImageNet·InstructPart에서 7B 모델·SAM3를 앞섰고 reasoning segmentation으로도 전이된다.
- **태그**: open-vocab-detection, vlm, fine-grained, segmentation

---

### [IoUPD: IoU-Aware Privileged Distillation for Visual Grounding with Multimodal Large Language Models](https://arxiv.org/abs/2607.15732)

- **한 줄 요약**: GT 박스를 좌표 라벨로만 쓰지 않고, 박스를 표시한 이미지를 보는 teacher로부터의 privileged distillation 신호로 활용해 MLLM visual grounding의 토큰 우도–IoU 불일치를 해소.
- **핵심 기여**: 좌표를 텍스트로 생성하는 MLLM grounding은 토큰 우도로 학습되지만 평가는 IoU로 되는 불일치가 있음을 지적하고, 학습 시에만 GT 박스가 오버레이된 이미지를 받는 frozen teacher를 두어 기하학적 중요도와 teacher 신뢰도로 토큰별 가중치를 주는 증류 손실을 설계했다. 추론 시에는 teacher·힌트·추가 모듈이 전혀 필요 없으며, 표준 referring expression grounding 벤치마크에서 일관된 개선을 보였다.
- **태그**: vlm, distillation, open-vocab-detection

---

### [Geometric Distillation from Rectified Stereo: Leveraging Epipolar Cues for Monocular Depth](https://arxiv.org/abs/2607.15600)

- **한 줄 요약**: multi-view 모델의 scale-aware 기하 prior를 epipolar 증류로 monocular depth foundation model에 이식해, 추론은 단일 이미지만으로 zero-shot metric depth를 개선.
- **핵심 기여**: 단안 추론의 scale ambiguity를 해결하기 위해 Rectified Stereo Token 기반 Epipolar Distillation(EpiDistill)을 제안, 단일 뷰 모델이 multi-view 입력 없이도 epipolar attention 패턴과 기하 일관성을 유지하도록 학습시킨다. scale 정렬이 중요한 ETH3D·DIODE 등에서 zero-shot metric depth를 크게 개선했고, UniDepthV2·DepthPro 등 SOTA ViT 모델에 model-agnostic하게 적용된다.
- **태그**: depth, distillation, foundation-model

---

### [Von Mises-Fisher Mixture Model with Dynamic Shrinkage for Realistic Test-Time Transduction](https://arxiv.org/abs/2607.15851)

- **한 줄 요약**: VLM zero-shot 분류의 test-time transduction이 클래스 불균형에서 붕괴하는 원인을 anchoring 부재로 규명하고, zero-shot prior로 shrinkage 강도를 동적 조절하는 training-free 기법 MOON을 제안.
- **핵심 기여**: transduction을 penalized likelihood estimation 관점에서 재해석해, KL anchor 항이 prior와 경험적 추정치 사이의 적응적 shrinkage를 만든다는 점을 보였다. 단위 초구면 위 피쳐를 von Mises-Fisher 혼합으로 모델링하고 인스턴스·클래스 수준에서 shrinkage를 동적으로 조절해 outlier 클래스로 인한 negative transfer를 억제한다. 모델 무관·학습 불필요·태스크별 하이퍼파라미터 튜닝 불필요.
- **태그**: vlm, foundation-model, test-time-adaptation, image-embedding

---

### [DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction](https://arxiv.org/abs/2607.16012)

- **한 줄 요약**: frozen vision foundation model 위에 얹는 DPT 대체용 경량 멀티태스크 디코더로, 학습 파라미터를 78.6% 줄이면서 segmentation+depth 멀티태스크 SOTA를 달성.
- **핵심 기여**: depthwise separable inverted bottleneck 두 개로 구성된 fusion 중심 디코더 DPNeXt와, 추가 모듈 없이 대칭적 boundary 감독만으로 태스크 간 negative transfer를 줄이는 Multi-Task Boundary Guidance를 제안했다. Cityscapes·NYUv2에서 기존 멀티태스크 SOTA를 앞섰고, 표준 DPT 대비 학습 파라미터 78.6% 절감과 노트북급 하드웨어 최고 추론 속도를 보였다. 코드·체크포인트 공개 예정.
- **태그**: foundation-model, segmentation, depth, efficient-inference

---

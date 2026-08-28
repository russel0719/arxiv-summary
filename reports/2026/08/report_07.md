# arXiv cs.CV Daily Digest — 2026-08-06 (arXiv 공개일)

- **전체 신규 논문 수**: 131편 (new 111 + cross-list 20)
- **선별 수**: 9편

## 오늘의 트렌드

오늘 cs.CV 신규의 절반 이상은 VLM/MLLM 주변에 몰렸다. 특히 visual-token 압축·pruning(RUTA, DIVE, Not All Redundant Tokens, HiSC, CARVE, SlotNarrative)과 VLA/world-model 로보틱스(CofactVLA, Faster-WAM, MobileWAM), 그리고 의료영상·3D Gaussian Splatting·생성모델 distillation(Poly-OPD, STEP-OPD)이 큰 덩어리를 이뤘다. 내 관심사에 닿는 흐름은 두 갈래로 뚜렷했다. 첫째, **frozen foundation-model 특징 위에 얇은 헤드/프로토타입을 얹어 판별·검색을 푸는 계열**(AIGI 탐지에서 PE vs DINOv3, composed retrieval, foundation-model 기반 pose correspondence)이 여러 편 등장해 SSL 백본·임베딩·retrieval 관심과 정확히 겹쳤다. 둘째, **정상 데이터만으로 이탈을 잡는 anomaly/재구성 계열**(image-space pose-agnostic AD, VQ 기반 motion codebook)과 검출기 경량화(정적 구조적 pruning), few-shot 도메인 적응(diffusion 증강)이 산업 검사·배포 최적화 관심과 맞물렸다. 아래 9편을 선별했다.

---

### [Unleashing the Potential of Vision-Language Models for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2608.04935)

- **한 줄 요약**: 언어 정렬 표현을 가진 Perception Encoder의 frozen feature를 semantic prototype으로 보정해, AI 생성 이미지 탐지에서 DINOv3 기반 baseline을 능가한다.
- **핵심 기여**: frozen 표현에 대한 단순 linear probe가 이미 특화 탐지기를 크게 앞서면서 DINOv3가 지배적 baseline으로 자리잡았으나, 저자들은 VLM인 Perception Encoder(PE)의 언어 정렬 표현이 provenance 의미를 더 잘 보존해 잠재력이 크다고 본다. 다만 semantic-agnostic linear probing으로는 이 구조를 못 살려 PE-Linear가 in-the-wild에서 DINOv3-Linear보다 4.1% 낮다. 이를 해결하려 forensic semantic 정보로 카테고리 프로토타입을 만들고 지도 데이터로 보정하는 Semantic Prototype Calibration(SPC)을 제안, PE-SPC가 cross-generator·post-processing·in-the-wild에서 새 SOTA를 달성한다.
- **태그**: forgery-detection, ssl-backbone, image-embedding, metric-learning, foundation-model

---

### [CoCo-IR: Contextual Composed Image Retrieval](https://arxiv.org/abs/2608.05149)

- **한 줄 요약**: 다중 턴 상호작용 이력을 해석해 턴마다 진화하는 Transformable Image Embedding을 생성하는 문맥형 composed image retrieval 모델.
- **핵심 기여**: 기존 instruction 기반 검색이 단일 턴에 한정돼 실제 반복적 시각 검색을 못 담는다는 한계를 지적하고, 상호작용 이력 전체를 해석하는 LMM 기반 문맥 추론기로 CoCo-IR 태스크와 모델을 정의한다. 사람 주석 없이 LMM으로 고품질 문맥 검색 데이터를 생성하고 모델 검증으로 hard negative를 채굴하는 자동·확장형 데이터 엔진을 함께 제안한다. 단일 턴 CIRCO 39.4 mAP@5, 4턴 대화에서 44.1 R@1로 다중 턴 문맥을 못 다루는 기존(28.2)을 크게 앞선다.
- **태그**: image-retrieval, image-embedding, metric-learning, vlm

---

### [LoRetta: A Foundation Model and Extensive Dataset for Global-Scale Remote Sensing Dense Image Matching](https://arxiv.org/abs/2608.04106)

- **한 줄 요약**: dense matching을 '정합영역 국소화 후 아핀 정합 → dense 잔차 정제'로 재정식화한 글로벌 스케일 dense image matching foundation model.
- **핵심 기여**: 촬영시각·계절·시점·해상도가 크게 다른 이미지쌍에서 큰 기하 오프셋·부분 겹침·본질적 매칭 불가 영역 탓에 직접 dense 대응 예측이 불안정한 문제를, matchability-aware 아핀 국소화와 guided dense registration을 결합해 해결한다. LEVIR-GM(103K 정합/827K 증강 쌍, 6대륙, 5년, 0.5–1024m)과 sparse/semi-dense/dense 통합 평가 프로토콜을 제공한다. RoMa v2 대비 AUC +1.6, PCK@1px +6.5·@2px +8.2, 지연 47.8% 감소하며, astronaut/UAV-to-satellite 지오로컬라이제이션으로 재사용 가능한 기하 정렬기로서의 전이성을 입증한다.
- **태그**: feature-matching, correspondence, foundation-model, dataset-benchmark

---

### [Promptable Animal Pose Tracking Across Species](https://arxiv.org/abs/2608.04995)

- **한 줄 요약**: 대규모 사전학습 vision foundation model 특징으로 소량 라벨만 쓰고 사용자 지정 키포인트를 영상에서 추적하는 종 간 promptable pose tracking.
- **핵심 기여**: 동물 pose가 종 간 형태·행동 차이와 라벨 부족으로 어렵다는 점에서, 지도형(keypoint prompt encoder로 레퍼런스 프레임의 구조 prior를 feature matching에 명시적으로 주입)과 비지도형(다양한 foundation-model 특징으로 training-free correspondence matching) 두 모델을 제안한다. 지도형은 추적 정확도, 비지도형은 종 간 강건성에서 우위를 보이며, APTv2·TigDog에서 정확도-일반화 균형을 달성한다.
- **태그**: correspondence, feature-matching, ssl-backbone, pose

---

### [PADFormer: Pose-agnostic Anomaly Detection from Sparse View Images](https://arxiv.org/abs/2608.04210)

- **한 줄 요약**: 3D 재구성 없이 ViT로 쿼리 이미지의 무결(정상) 버전을 재구성해 임의 시점의 결함을 잡는 image-space pose-agnostic anomaly detection.
- **핵심 기여**: 기존 PAD가 비싼 3D 재구성과 다량 multi-view에 의존하는 문제를, 정상 데이터만으로 cross-view masked reconstruction을 학습하는 image-space 접근으로 대체한다. dynamic patch selection과 spatial alignment로 sparse reference·큰 pose 변동에서도 학습 가능하며, 추론 시 서로 다른 마스킹 패턴으로 무결 재구성 앙상블을 만들어 쿼리와 비교해 결함을 검출한다. PAD 벤치마크 SOTA를 달성하면서 few-shot anomaly detection에서도 경쟁력을 유지, 3D 재구성 없이 효율·일반화를 확보한다.
- **태그**: anomaly-detection, industrial-inspection, ssl-backbone, defect-detection

---

### [Foreseeing the Invisible: Amodal Reconstruction of Leaf Fossil Images](https://arxiv.org/abs/2608.04423)

- **한 줄 요약**: DINOv3 ViT-L/16을 전체 미세조정하고 잎맥 보조 헤드를 붙여, 가시 마스크 입력 없이 가려진 대상의 완전한 형상을 복원하는 amodal dense 예측 모델.
- **핵심 기여**: 대부분의 amodal 연구가 가시 마스크를 입력으로 요구하는 것과 달리, 단일 RGB에서 가시/amodal 완전영역·주맥·세맥 4개 마스크를 동시 예측해 런타임에 별도 instance segmenter가 불필요하다. DINOv3를 freeze하지 않고 작은 lr로 완전 미세조정하고 venation 보조 헤드를 더하는 두 가지 단순한 변경으로 구조적 형상 prior를 학습한다. 합성 데이터만으로 학습해 검증 95.0% Dice/90.5% IoU, 실제 표본과 KINS/COCOA 벤치마크로 전이하며, 4-bit 양자화로 브라우저 오프라인 실행 시에도 IoU 0.910을 유지한다.
- **태그**: ssl-backbone, segmentation, quantization, distillation

---

### [StaticSegFormer: An Efficient High-Performance Semantic Segmentation Based on Static Structured Pruning](https://arxiv.org/abs/2608.04811)

- **한 줄 요약**: 동적 pruning이 GPU에서 오히려 느리다는 관찰에서, attention 층에 정적 구조적 pruning을 적용해 FLOPs와 프레임률을 함께 개선한 SegFormer 경량화.
- **핵심 기여**: ADE20K·Cityscapes에서 최근 동적 구조적 pruning이 mIoU·FLOPs는 단순 정적 방식과 비슷한데도 GPU 프레임률은 놀랍도록 낮다는 점을 밝힌다. 이를 해결하려 attention 층 전용 정적 구조적 pruning을 제안, Cityscapes에서 mIoU 저하 없이 프레임률을 최대 34% 상대 향상시킨다. 특히 작은 인코더·큰 이미지 조합에서 효과가 가장 크다.
- **태그**: segmentation, efficient-inference, foundation-model

---

### [Free-Lunch Augmentation by Revisiting Diffusion-Based Data Generation for Cross-Domain Few-Shot Object Detection](https://arxiv.org/abs/2608.04394)

- **한 줄 요약**: 도메인 갭을 시각 갭·의미 갭으로 나눠 약화 노이즈와 배경 인페인팅으로 diffusion 합성을 보정, cross-domain few-shot 검출을 개선한다.
- **핵심 기여**: CDFSOD에서 diffusion 데이터 증강을 재검토하되, 큰 도메인 갭 탓에 기존 diffusion은 원본 이미지보다도 성능이 낮아지는 문제를 진단한다. 시각 갭은 diffusion이 전문 도메인에서 노이즈와 유용 정보를 구분 못 하는 데서 오므로 약화된 노이즈로 완화하고, 의미 갭은 전경보다 배경 의미가 도메인 간 훨씬 작다는 점을 이용해 배경 인페인팅으로 메운다. 갭에 따라 노이즈·인페인팅 영역을 동적 선택하는 SITN으로 6개 CDFSOD·4개 cross-domain few-shot segmentation에서 새 SOTA를 달성한다.
- **태그**: object-detection, open-vocab-detection, generative, industrial-inspection

---

### [VQ-VAD: Vector-quantized Motion Representation Learning for Human-centric Video Anomaly Detection](https://arxiv.org/abs/2608.05069)

- **한 줄 요약**: 사람 keypoint 시퀀스에 VQ-GAN을 적용해 정상 동작의 이산 motion codebook을 학습하고, 매핑 불가한 재구성 오류로 이상을 탐지하는 pose 기반 video anomaly detection.
- **핵심 기여**: 조명·시점·외형 변화가 큰 감시영상에서 pose 기반 VAD가 시각 노이즈·프라이버시에 유리하나, 기존 방식이 연속 잠재공간으로 행동을 모델링해 compact한 정상 패턴 학습이 어렵다는 한계를 지적한다. 이미지 생성용 VQ-GAN을 keypoint 시퀀스에 맞춰 정상 행동의 motion codebook을 구성하고, 관측 동작이 codebook에 매핑되지 못할 때의 높은 재구성 오류로 이상을 판정한다. in-domain(HR-SHT 81.83%)·cross-domain·cross-dataset 세 설정에서 강건한 전이를 보인다.
- **태그**: anomaly-detection, pose, video, re-identification

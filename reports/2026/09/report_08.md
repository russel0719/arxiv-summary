# arXiv cs.CV Daily Digest — 2026-09-07 (arXiv 공개일)

- **전체 신규 논문 수**: 110편 (new 81 + cross-list 29)
- **선별 수**: 10편

## 오늘의 트렌드

목록에서 가장 큰 군집은 의료 영상으로, 4D flow MRI 대동맥 분할, 조직학 섬유 다발 분할, 수술 영상 foundation model의 depth 기반 사전학습(DART), 혈관조영 다중 클래스 분할, 안저 OCTA 표현형, 위장 내시경 분류, 병리 foundation model의 MSI-H 예측, 흉부 X-ray 중증도 triage와 국가 간 이식성 분석, 초음파 기반 간질환 예측 두 편, 구강 악성 병변 탐지, 폐암 종단 데이터셋까지 모달리티와 장기를 가리지 않고 넓게 퍼져 있다. 두 번째 축은 생성모델로, 시각 생성용 reflection-aware preference optimization, 비디오 생성의 alignment·distillation 결합, Diffusion Transformer 특징을 이용한 생성 제어(ReaDiT)와 참조 기반 생성의 국소 속성 안내(RefDiT), DiT의 중요도 인식 low-rank 증류, 렌즈 미학 스타일링, 짝 데이터 없는 3D 편집, 에이전트형 이미지 생성·편집 레시피, 텍스트 안내 편집용 white-box 워터마크(AngelFingerprint), 무한 길이 audio-video 생성이 함께 올라왔다. 3D·기하 쪽은 반복 구조 모호성을 scaffold로 푸는 SfM(HiSfM), 다시점 매칭과 단안 prior를 결합한 bundle adjustment(BLASt3R), 약지도 3D occupancy, 크로스 플랫폼 3D 탐지, 다시점 surround depth, 완성된 voxel map의 사후 의미 보정, Gaussian Splatting용 compact appearance model이 이어진다. Embodied·VLA 계열은 timestamp 수준 실패 탐지(FailureSpot), 장기 과제 벤치마크(RoboSPA), neuro-symbolic 절차 추론, visuomotor policy의 조건부 grounding 진단, 단일 이미지에서 물리를 결합한 world model(TourPhysics), grounded video에서 구성적 세계를 생성하는 WorldSculpt로 분화돼 있다. VLM은 sparse autoencoder로 실패를 해석하는 FailSAE, 시각 우세로 인한 개인화 안전 실패, multimodal chain-of-thought 압축, 시각→언어 인과 정보 흐름 분석, 논리 텐서 네트워크와 결합한 검증·수정 루프 등 진단과 신뢰성 연구가 주류이고, 해석 가능성 연구의 초점을 방법에서 모델로 옮기자는 position paper도 나왔다. 시각 인코딩 효율 축에서는 foveated 가변 해상도 인코딩(FAVE), 강화학습 기반 토큰 선택(LookThere), 이벤트 카메라의 다중 시간 스케일 표현, 수동 냉각 엣지 장치의 DVFS 보정, 농업용 ViT 압축 파이프라인이 각각 다른 지점을 다룬다. 산업 이상 탐지는 memory bank 구축·추론 효율(LUMIN)과 training-free 논리·구조 이상 융합 두 편이 나왔고, 검색·인식 쪽은 생성 증강 기반 visual place recognition, DINOv2에 3D shape prior를 보완한 산업 부품 인식, long-tailed 인식의 분산 감소 관점(VICAL), 계층적 metric learning 기반 few-shot 행동 인식, CLIP의 부분 관련 비디오 검색 적응이 소규모 군집을 이룬다. 이 밖에 overfitted 코덱 기반 이미지·비디오 표현 압축(MIRC, NVRC), 음성·전신 동작 동시 생성, 골격 무관 애니메이션, 소리 기반 3D 자세 추정, 카메라 트랩 counting-by-tracking, 위성 탑재 메탄 탐지 등이 각각 한두 편씩 등장한다.

---

### [Object Concepts Emerge from Motion](https://arxiv.org/abs/2609.04348)

**한 줄 요약**: 비디오의 motion boundary로 만든 pseudo-instance mask를 감독 신호로 삼아, 단일 이미지 인코더가 개별 인스턴스의 정체성과 응집성을 보존하는 object-centric 표현을 배우게 하는 대규모 사전학습 프레임워크.

**핵심 기여**: 기존 시각 사전학습은 의미 범주는 잘 잡지만 개별 인스턴스의 정체성과 경계는 잘 보존하지 못한다는 문제를 제기한다. 사람 주석이나 카메라 캘리브레이션 없이, off-the-shelf optical flow와 클러스터링으로 pseudo-instance mask를 만들고 이를 pixel-level pairwise metric learning으로 단일 이미지 인코더에 가르친다. 7,163시간의 주행·웹 비디오에서 1억 9,500만 프레임을 pseudo-label하고, 모델 제안과 motion 증거를 결합하는 Motion-Verified Self-Training으로 4억 2,100만 프레임까지 감독을 확장해 Swin-H까지 학습한 뒤 Swin-T/S/B/L 계열로 증류한다. KITTI 단안 depth에서 Swin-L이 Abs Rel 0.042로 DINOv3 ViT-L(0.044)을 앞서고, nuScenes 3D 탐지에서 Swin-H가 56.92 NDS로 ImageNet-22K 지도 사전학습을 넘으며, occupancy와 NAVSIMv2 planning에서는 DINOv2를 앞서되 DINOv3·DA-ViT-L에 소폭 뒤진다. 저자들은 optical flow 품질 의존(빠른 움직임·심한 occlusion·blur·약한 텍스처에서 감독 저하)과 flow가 안정적인 프레임을 선호하는 선택 편향을 한계로 밝힌다.

**태그**: ssl-backbone, image-embedding, metric-learning, foundation-model

---

### [AdaptVPR: Route-Aware Hard Positive Generation for Robust Visual Place Recognition](https://arxiv.org/abs/2609.04369)

**한 줄 요약**: VLM이 장면 속성과 편집 가능성을 판단하고 규칙 기반 스케줄러가 생성 경로를 정해, 같은 장소의 검증된 hard positive를 합성해 VPR 학습 데이터의 외관 다양성을 늘린다.

**핵심 기여**: visual place recognition은 조명·날씨·계절·동적 occlusion으로 인한 도메인 변화에 취약하며, 그 원인 중 하나로 학습 데이터에 같은 장소의 외관 다양성이 부족하다는 점을 지적한다. AdaptVPR는 VLM으로 장면 속성을 파싱하고 편집 가능성 점수와 위험 제약에 따라 Global Appearance Route(날씨·조명·시간대 전역 변화), Local Occlusion Route(동적 occluder 삽입), Dual Route(둘의 결합) 중 생성 경로를 정하며, 생성된 후보는 geometric consistency와 외관 다양성에 기반한 VPR 지향 검증을 거쳐 구조 드리프트를 줄인다. 전역 후보는 검증 실패 시 기각하고, 국소·이중 후보는 검증 피드백으로 제한된 prompt 수정과 재생성을 수행한다. 이렇게 구축한 AdaptCities는 16만 장의 검증된 합성 hard positive를 담고 있으며, 여러 VPR baseline과 vision foundation backbone에서 표준 벤치마크 성능이 일관되게 오르고 어려운 도메인 변화에서는 R@1이 최대 9.2% 향상된다. 코드와 데이터가 공개돼 있다.

**태그**: image-retrieval, image-embedding, dataset-benchmark, generative

---

### [Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381)

**한 줄 요약**: CAD 없이 짧은 객체 스캔에서 3DGS로 복원한 클래스별 shape prototype을 동결 DINOv2 특징과 융합해, 기하적으로 유사한 저텍스처 산업 부품 인식을 보완하는 연구.

**핵심 기여**: 라벨 학습셋 없이 온보딩된 특정 객체를 인식해야 하는 제조·서비스 로봇 상황에서 렌더링 가능한 prior인 CAD가 없을 때, 2D 촬영은 shape prior를 주지 못하고 동결 foundation 특징은 기하적으로 비슷한 저텍스처 부품에서 실패한다는 문제를 다룬다. 각 객체를 3D Gaussian Splatting으로 복원해 45차원 클래스별 shape prototype으로 요약하고, 추론 시에는 RGB crop의 동결 DINOv2-giant 특징을 경량 head로 기하 descriptor 공간에 사상해 프로토타입과 cosine similarity를 구한 뒤 이미지 점수와 가중합한다. RGB-D depth, 3DGS, CAD에서 얻은 기하가 HOPE에서 동률, T-LESS에서 1.6점 이내로 비슷한 인식 성능을 내어 스캔이 CAD의 인식 가치를 대체하며, 형태가 뚜렷한 HOPE에서는 기하만으로 0.920(이미지만 0.832), 형태가 혼동되는 T-LESS에서는 융합 시 0.560→0.591로 이득이 작지만 일관된다. prior는 이미지 실패를 회복시키는 경우가 성공을 깨는 경우보다 훨씬 많고 부분 occlusion에서 이득이 커지는 반면, 3DGS 렌더링은 이미지 분기에 도움이 되지 않는다. 연구 범위는 인식에 한정되며 BOP pose 벤치마크는 다루지 않고, 코드는 요청 시 제공으로 명시됐다.

**태그**: fine-grained, industrial-inspection, foundation-model, 3d

---

### [Training-Free Logical and Structural Anomaly Detection via Calibrated Fusion](https://arxiv.org/abs/2609.05091)

**한 줄 요약**: 정상 이미지 통계로 이질적인 이상 단서들을 보정해 하나의 training-free 프레임워크에서 융합하고, 추가 학습이나 부품 주석 없이 counting 능력을 도입해 논리·구조 이상을 함께 잡는다.

**핵심 기여**: 산업 이상 탐지는 국소 텍스처 손상인 structural anomaly와 객체 수·구성·배치 규칙을 어기는 logical anomaly를 모두 다뤄야 하지만, training-free 방법은 동결 표현을 잘 활용하되 객체 수 개념이 없고 count를 추론하는 방법은 카테고리별 부품 모델링에 의존한다는 간극을 지적한다. 핵심은 normal-set calibration으로, 정상 이미지에서 얻은 통계로 서로 다른 이상 단서를 정렬해 통일된 training-free 프레임워크 안에서 직접 융합할 수 있게 하고, 이를 바탕으로 상보적인 동결 단서들을 결합한다. MVTec-LOCO에서 logical 89.0, structural 95.9의 image-level AUROC로 평균 92.5를 기록해 비교한 training-free 탐지기 중 가장 높고, 네트워크 학습이나 부품 주석이 필요한 방법과도 경쟁하며, structural 변형은 MVTec-AD에서 PatchCore와 같은 99.1 image-AUROC를 낸다.

**태그**: anomaly-detection, industrial-inspection, defect-detection, foundation-model

---

### [LUMIN: Lightweight Universal Manufacturing Inspection Network for Anomaly Detection](https://arxiv.org/abs/2609.04775)

**한 줄 요약**: backbone forward pass 없이 픽셀 메타데이터로 memory bank를 샘플링하는 PSP 파이프라인과 병렬 유사도 계산·계층적 픽셀 샘플링으로 산업 이상 탐지의 구축·추론 비용을 낮춘다.

**핵심 기여**: 산업 이상 탐지의 병목으로 memory bank 구축 지연과 추론 효율을 꼽는다. Farthest Point Sampling·K-Means 같은 전통 샘플링은 다수의 backbone forward pass와 반복 거리 계산에 의존해 구축에 수 분에서 수 시간이 걸리고, 다중 스케일 특징 추출 같은 무거운 구성 요소는 생산 라인의 밀리초 수준 실시간 요건을 맞추기 어렵다. 첫 기여인 PSP(Plugin Sampler Pipeline)는 18차원 픽셀 메타데이터와 다섯 가지 시각 플러그인에 기반한 4단계 적응형 샘플링으로 backbone forward pass 없이 샘플링을 끝내며, 거친 필터링은 1초 미만의 수치 정렬이고 메타데이터 추출은 1회성 오프라인 비용이며 점진 배포와 증분 갱신을 지원한다. 두 번째는 병렬 memory bank 유사도 계산(추론 메모리·지연 95% 이상 감소)과 대규모 평가용 계층적 픽셀 샘플링(계산 시간 20배 감소)이다. 검증 수단으로 분할 헤드를 극단적으로 압축한 LUMIN을 제시하며, 다섯 벤치마크에서 PSP가 FPS보다 341배 빠른 거의 무작위 수준의 구축 비용으로 state-of-the-art 샘플링 정확도에 도달하고, 추론 최적화는 정확도 손실 없이 평가 시간을 20배 줄인다고 보고한다.

**태그**: anomaly-detection, industrial-inspection, efficient-inference, defect-detection

---

### [CLON: Cue-Calibrated Linguistic Object Onboarding for Zero-Shot 6D Pose Front-Ends](https://arxiv.org/abs/2609.04784)

**한 줄 요약**: 온보딩 객체의 렌더링 템플릿에서 언어적 semantic memory와 객체 집합별 cue 가중치를 구성해, SAM 3를 고재현율 proposal로 이끌고 보정된 점수로 distractor를 거르는 학습 불필요 front-end.

**핵심 기여**: zero-shot 6D pose 파이프라인은 강한 pose solver에 의존하지만 성능은 부분 가시 true positive를 보존하면서 의미적으로 유사한 distractor를 기각해야 하는 front-end에 제약된다는 점을 짚는다. CLON은 새 객체에 대한 task-specific 학습 없이, 온보딩 객체 집합의 렌더링 템플릿으로부터 top-down proposal 생성을 위한 linguistic semantic memory와 보정된 proposal 점수화를 위한 object-set cue weight를 만든다. semantic memory는 SAM 3를 온보딩 객체에 대한 고재현율 proposal로 안내하고, cue weight는 장면 추론 전 객체 집합에서 한 번 계산해 온라인 점수화 중 고정한다. BOP-Classic-Core 7개 데이터셋에서 CNOS·SAM-6D front-end 대비 detection AP 8.1pp, segmentation AP 6.2pp, 하류 6D pose AR 최대 4.1pp 향상을 보고한다.

**태그**: open-vocab-detection, segmentation, pose, foundation-model

---

### [FAVE: Foveated Adaptive Visual Encoding for Efficient Fine-Grained Visual Understanding](https://arxiv.org/abs/2609.04392)

**한 줄 요약**: 외부에서 선택된 영역을 원본 기하를 유지한 채 고해상도로 인코딩하는 경량 가변 해상도 ViT로, 작은 객체·텍스트·속성의 세밀한 이해를 적은 FLOPs로 보완한다.

**핵심 기여**: 세밀한 시각 이해는 국소 세부에 의존하지만 시각 인코더는 비용이 큰 전체 이미지 고해상도 처리와 그런 증거를 약화시키는 compact 전역 인코딩 사이에서 절충해야 한다. 인간의 능동 시각에서 착안해 '어디를 볼지'와 '무엇을 인코딩할지'를 분리하고 후자에 집중해, 외부 선택 영역을 높은 acuity로 인코딩하는 FAVE를 제안한다. oracle crop을 쓴 통제 실험에서 최대 변 96픽셀의 ImageNet 소형 객체에 대해 같은 crop 창의 고정 해상도 ViT보다 Top-1이 9.4점 높고 FLOPs는 12.7배 낮으며, 전역 해상도나 backbone 용량을 키워도 같은 동작점에 도달하지 못한다. FastVLM에 국소 분기로 결합해 전역 경로와 언어 모델을 동결한 채 최대 16개의 국소 토큰만 추가하면 TextVQA가 1.60점 오르고 SmolVLM2-2.2B 대비 통제된 TTFT가 3.3배 빨라지며, GQA 속성 질문에서 FastVLM-1.5B를 1.31점 개선해 FastVLM-7B와의 격차를 줄인다.

**태그**: fine-grained, efficient-inference, vlm, foundation-model

---

### [LookThere! Sparse Vision by Reinforced Selection](https://arxiv.org/abs/2609.04698)

**한 줄 요약**: 얕은 입력 선택기와 깊은 표현 추출기를 강화학습으로 함께 학습해, 보조 휴리스틱 없이 과제에 필요한 토큰만 골라 극단적 sparsity에서도 정확도를 유지하는 적응형 계산 프레임워크.

**핵심 기여**: vision transformer는 모든 이미지 토큰을 동등하게 처리하지만 대부분의 과제에는 일부만 필요하며, 기존 토큰 선택 방법은 극단적 sparsity에서 무너지고 토큰 다양성·attention 점수처럼 일반화가 보장되지 않는 휴리스틱에 의존한다고 지적한다. LookThere는 end-to-end 강화학습으로 선택기가 어디를 볼지, 추출기가 무엇을 볼지 배우게 하여 보조 신호 없이 과제별로 처리할 가치가 있는 입력만 선택한다. 고해상도 sparse 인식(교통 표지, 당구)에서 입력의 0.2%만으로 정확도를 유지하고, ImageNet 분류(전역 인식), ADE20K 분할(국소 인식), 증류를 통한 zero-shot 분류, counting(회귀)까지 과제와 모델을 가로질러 일반화하며 모든 설정에서 기존 state-of-the-art 선택 방법을 앞서 성능-계산 trade-off의 새 pareto frontier를 제시한다.

**태그**: efficient-inference, foundation-model, object-detection, segmentation

---

### [Adaptive Gated Deepfake Detection for Low-Resolution and Resource-Constrained Environments](https://arxiv.org/abs/2609.05320)

**한 줄 요약**: 이미지 품질 단서로 샘플을 dual multi-exit 경로에 라우팅해 고품질 입력은 일찍 종료시키는 적응형 gated deepfake 탐지 프레임워크.

**핵심 기여**: deepfake 탐지 모델이 고품질 입력, 고정된 추론 경로, 비용이 큰 아키텍처에 의존해 저해상도·자원 제약 환경에서 쓰기 어렵다는 문제를 다룬다. AdaGate-DF는 이미지 품질 단서를 기준으로 샘플을 두 개의 multi-exit 시스템에 라우팅해 고품질 이미지가 조기 종료로 계산을 절약하게 한다. Celeb-DF와 FaceForensics++에서 MaD-CoRN, DefakeHop++, ShuffleNetV2와 해상도 의존성·학습 및 추론 효율을 비교했으며, Celeb-DF에서 AUC 0.9370으로 MaD-CoRN과 DefakeHop++를 앞서면서 낮은 추론 지연을 유지하고, 해상도를 높이면 384×384에서 AUC 0.9708에 도달한다. FaceForensics++에서는 클래스 불균형 아래에서도 비교 모델과 경쟁력 있는 결과를 보인다.

**태그**: forgery-detection, efficient-inference

---

### [VICAL: Vicinal Consistency Alignment for Long-Tailed Visual Recognition](https://arxiv.org/abs/2609.04948)

**한 줄 요약**: 다중 expert long-tailed 인식의 이득은 expert 다양성보다 예측 분산 감소에서 온다는 관찰 아래, 자기 일관성 학습과 저해상도 뷰 기반 ensemble distillation으로 tail 클래스 과적합을 줄인다.

**핵심 기여**: 다중 expert 모델이 long-tailed 학습의 주류가 된 근거인 expert 다양성 가정을 재검토해, logit 조정이나 명시적 정규화로 유도한 다양성이 ensemble 정확도를 보장하지 않으며 실제 이득은 분산 감소에서 온다고 주장한다. VICAL은 두 요소로 구성되는데, Self-Consistency Learning은 불안정한 고주파 정보 의존을 억제해 국소 loss landscape를 평탄화하고 tail 클래스 과적합을 완화하며, Deep Ensemble Distillation은 저해상도 뷰로 expert 간 저주파 의미 합의를 유도해 기존 지식과의 최적화 충돌을 피한다. CIFAR-LT, ImageNet-LT, iNaturalist 2018에서 state-of-the-art 방법들을 일관되게 앞선다고 보고하며, 코드가 공개돼 있다.

**태그**: fine-grained, distillation, long-tailed-recognition

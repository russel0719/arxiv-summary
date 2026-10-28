# arXiv cs.CV Daily Digest — 2026-10-28 (arXiv 공개일)

- **전체 신규 논문 수**: 156편 (new 127 + cross-list 29)
- **선별 수**: 8편

## 오늘의 트렌드

MLLM의 비디오 추론·강화학습(RLVR)·GUI grounding이 가장 두꺼운 군집이고, Gaussian Splatting과 VGGT류 feed-forward 3D 재구성, world model·VLA 기반 로봇 제어가 뒤를 잇는다. MRI·병리 등 의료 영상 연구도 한 덩어리를 이룬다. 방법론으로는 사전학습 video diffusion을 인식·생성 과제에 재활용하는 흐름과 visual token pruning·저비트 양자화 같은 추론 효율화가 두드러진다.

---

### [EmbeddingGemma 2: Unified and Efficient Multimodal Representations](https://arxiv.org/abs/2610.37364)

**한 줄 요약**: 텍스트·이미지·오디오·비디오와 그 조합을 하나의 공간에 임베딩하는 744M 규모의 공개 multimodal embedding 모델.

**핵심 기여**: 단일 모달·교차 모달·혼합 모달 검색 품질을 함께 갖추면서 자원 제약 환경에서도 돌릴 수 있는 작은 임베딩 모델이 필요하다는 문제의식이다. 271M backbone에 Gemma 4 계열에서 초기화한 167M ViT(patch 16) vision encoder와 305M audio encoder를 붙이고, simplified per-layer embedding과 텍스트 distillation(~300B token) → 멀티모달 distillation(~2T) → contrastive·spread-out·Matryoshka loss fine-tuning(~600B) → checkpoint merging → QAT로 이어지는 약 2.9T token curriculum으로 학습한다(임베딩 768차원, 512/256/128로 절단 가능, 이미지당 vision token 70~1120 조절, 필요한 모달리티 encoder만 선택 로딩). MMEB-v2 평균 59.01(Image 57.28·VisDoc 67.84), MIEB(lite) 60.17(1B 미만 최고 모델 대비 Task +7.9), MTEB Multilingual v2 61.36을 기록하고, int4 QAT 가중치는 MTEB Multilingual 60.96으로 bf16 대비 0.4 point 안쪽이며 Pixel 11 Pro에서 텍스트+비전 구성의 최대 메모리는 447MB다. 한계로 MTEB English v2가 EmbeddingGemma 1보다 낮고(68.46 vs 69.67), 비디오는 vision token 560에서 280보다 오히려 떨어지며, 일부 baseline은 공개 leaderboard 값이고 양자화·float 평가의 harness가 일부 벤치마크에서 다르다고 밝힌다.

**코드**: 공개([google/embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2) · Hugging Face 메타데이터는 Apache-2.0, 라이선스 링크는 Gemma 4 license 문서로 연결), 가중치 공개·학습 코드 저장소는 명시 없음

**태그**: image-embedding, image-retrieval, foundation-model, quantization, efficient-inference

---

### [Forget the Data, Keep the Capability: Switchable Unlearning for Retrieval](https://arxiv.org/abs/2610.36858)

**한 줄 요약**: re-ID 검색 backbone을 core 파라미터와 zero-init parasitic 분기로 나눠, 분기를 끄는 것만으로 특정 인물의 학습 데이터 삭제 요청을 처리하는 switchable unlearning 프레임워크(MoME).

**핵심 기여**: 개인정보 규정상 re-ID 모델은 특정 인물을 잊으면서 다른 사람의 검색 능력은 유지해야 하는데, 요청마다 재학습하는 것은 비싸다는 문제의식이다. 사전학습 backbone(주 실험 TransReID ViT-B/16)에 LayerNorm/BatchNorm affine 보정항과 LoRA형 low-rank 쌍으로 된 parasitic 분기를 0으로 초기화해 붙이고, retain set으로 core만·전체 데이터로 parasitic만 갱신하는 gradient isolation으로 core가 forget set gradient를 한 번도 받지 않게 한 뒤, 이 독립성을 감사하는 rank 기반 Forgetting-Rank 통계를 제안한다. 학습 신원 절반을 지우는 설정(5개 split 평균)에서 Core의 mAP/Rank-1은 Market-1501 75.3/89.0(재학습 71.4/86.7), VeRi-776 42.5/70.0(37.3/65.0), RegDB V→T 57.0/59.0(45.4/47.0)이고, membership attack AUC는 0.49~0.52로 재학습(0.48~0.52)과 같은 수준이며, Full 모드는 원본 수준(Market 88.8/95.2)을 유지한다. 한계로 보장은 forward purity 등 가정 아래의 조건부이며 differential privacy가 아니고, 이미 core에 들어간 신원은 스위치만으로 지울 수 없으며, isolation 비용으로 Core mAP가 Market에서 약 10.7 point 낮아지고, ResNet-50·CLIP backbone에서는 privacy 판정 구간이 넓어 결론을 내지 못한다고 밝힌다.

**코드**: 공개 예정 (논문에 [Jingong-Chen/MoME](https://github.com/Jingong-Chen/MoME) 코드·가중치 공개 명시, 확인 시점 저장소가 비어 있음)

**태그**: re-identification, image-retrieval, machine-unlearning, peft

---

### [ARISE: Authentic Reference-Informed Stability Enhancement for Continual Multimodal Forgery Detection](https://arxiv.org/abs/2610.36509)

**한 줄 요약**: 새 위조 공격이 계속 등장하는 상황을 attack-incremental continual 학습으로 정의하고, 진짜 샘플의 분포만 GMM으로 기억해 망각을 줄이는 image-text 위조 탐지 방법과 벤치마크(Fable-Bench).

**핵심 기여**: 멀티모달 위조 탐지는 학습 때 본 공격이 배포 후에도 비슷하다고 가정하지만, 생성기·편집 도구·MLLM이 새로운 위조 방식을 계속 만든다는 문제의식이다. real/fake 이진 출력은 고정한 채 공격을 단계적으로 추가하는 Fable-Bench(joint-modality 5단계·text-side 4단계·image-side 4단계, 821,387 image-text 쌍, 30개 이상 조작 모델)를 만들고, ARISE는 replay한 authentic 표현에 real-only GMM을 맞춰 과거 기준으로 삼으며, GRASP가 GMM responsibility로 샘플별 비등방 metric을 만들어 역사적으로 안정된 방향만 강하게 묶고, VAR이 authentic 밀도 저하·위조-진짜 경계 혼동·mode 점유 변화로 단계별 취약도를 추정해 replay 비중을 나눈다(추론은 원래 backbone과 이진 head만 사용). Florence-2 backbone에서 세 프로토콜의 최종 평균 정확도가 85.37/81.22/90.47%로 가장 강한 baseline LPR(83.87/79.35/89.02%)보다 1.45~1.87 point 높고, CLIP·ViLT backbone에도 적용되며, VAR ablation에서 average forgetting이 ER 11.48%에서 8.67%로 줄었다. 별도 한계 서술은 없다.

**코드**: 불명 (논문에 코드 공개 언급 없음)

**태그**: forgery-detection, continual-learning, vlm, dataset-benchmark

---

### [SAGE: Saliency-Annealed Gated Encoder for Universal Vision Recognition](https://arxiv.org/abs/2610.36719)

**한 줄 요약**: DINO식 CLS-token saliency로 feature gating과 고주파 보강을 하는 ViT-Adapter 확장 backbone으로, 하나의 backbone에 과제별 decoder를 붙여 detection·segmentation·keypoint·분류를 다루는 방법.

**핵심 기여**: self-supervised ViT를 dense prediction에 쓸 때 수동적인 feature extractor로만 다뤄 saliency·전역 문맥·고주파 detail 같은 prior를 덜 쓴다는 문제의식이다. CLS-token saliency로 gating과 high-frequency enhancement를 유도하고 multi-layer 동적 aggregation·local-detail branch를 더한 구조, 학습 초반 수렴을 돕고 후반 feature drift를 줄이는 annealing 학습, focal loss에서 Varifocal Loss로 한 run 안에서 넘어가는 2단계 quality-aware 학습을 결합한다(Huawei Ascend 910B1 NPU 64장, O365 사전학습). SAGE-L(304M)은 COCO val 62.8 box AP·55.3 mask AP(ViT-Adapter-L 58.8/51.1), ADE20K 60.3 mIoU(frozen DINOv3 ViT-L 54.9, Mask2Former+ViT-Adapter-L 59.4), COCO keypoint 78.5 AP, DIOR-R 78.8 AP50이고, SAGE-B(86M)는 COCO 61.1/54.4다. 한계로 비교 대상 간 사전학습 데이터·학습 설정·파라미터 수가 달라 통제된 우위를 보인 것은 아니며, backbone 파라미터 수가 detector 전체 크기를 반영하지 않는다고 밝힌다.

**코드**: 공개 예정 (논문에 내부 검토 후 코드·사전학습 모델 공개 명시, URL 없음)

**태그**: ssl-backbone, object-detection, segmentation, foundation-model

---

### [Repurposing Video Diffusion Transformers for Cross-View Temporal Object Correspondence](https://arxiv.org/abs/2610.37633)

**한 줄 요약**: ego·exo 두 영상을 나란히 붙여 사전학습 video DiT에 넣고, 한쪽 첫 프레임의 query mask로 다른 시점과 전 시간에 걸친 같은 물체의 mask를 함께 예측하는 cross-view temporal object correspondence 프레임워크(XTrack).

**핵심 기여**: 기존 cross-view 물체 대응은 프레임별 매칭이나 순차 tracking에 의존해 외형 변화·가림에서 오류가 누적된다는 문제의식으로, 시점과 시간 모두에서 물체 identity를 유지하는 과제를 새로 정의한다. Wan 계열 video DiT의 의미·시공간 prior를 RGB→mask latent transport로 재활용해 ego·exo 영상을 diptych로 한 token 공간에 놓고, 의미가 비슷한 다른 물체에 attend하는 문제를 focal cross-view attention alignment·hard negative conditioning·local context crop으로 줄이며, 희소한 Ego-Exo4D 주석을 dense supervision으로 바꾸는 pseudo-label curation 파이프라인을 더한다. Ego-Exo4D validation 부분집합에서 VA(visibility accuracy)는 Ego2Exo 0.900·Exo2Ego 0.814로 최고 baseline(0.628·0.736)보다 높고 Exo2Ego mR@IoU는 0.911로 가장 높지만, J&F는 0.472·0.509로 SAM2 기반 V2-SAM(0.545·0.540)보다 낮다. 한계로 압축된 video DiT latent가 작은 물체의 경계를 흐려 mask 품질이 SAM2 계열 파이프라인에 못 미친다고 밝힌다.

**코드**: 공개 예정 ([cvlab-kaist/XTrack](https://github.com/cvlab-kaist/XTrack) 저장소가 있으나 확인 시점 README만 있음, 라이선스 표기 없음)

**태그**: correspondence, video, segmentation, object-tracking

---

### [Tail Cues, Principal Corrections: Plug-and-Play Rectification for Open-Set Test-Time Adaptation](https://arxiv.org/abs/2610.36870)

**한 줄 요약**: source 분류기 linear head의 SVD 기저로 특징을 principal·tail 좌표로 나누고, tail 좌표로 추정한 principal drift를 빼는 것만으로 open-set test-time adaptation을 하는 backward-free 보정 모듈(TALOR, NeurIPS 2026).

**핵심 기여**: covariate shift와 미지 클래스가 섞인 비정상 스트림에서 기존 TTA는 파라미터 갱신이나 가변 메모리에 의존해 비용이 크고 미지 샘플에 오염되기 쉽다는 문제의식이다. 고정된 head 가중치의 right-singular vector 중 에너지 상위(τ=0.8)를 principal, 나머지를 tail 부분공간으로 두고, tail energy에 맞춘 2성분 GMM으로 ID/OOD를 soft routing한 뒤 regime별 principal 평균과 tail→principal weighted ridge 회귀(dual 형태, EMA 갱신)로 drift를 추정해 principal 좌표에서만 빼고 원래 norm으로 복원해 head에 넣으며, backbone과 head는 갱신하지 않는다. ImageNet-1K 사전학습 ViT-B/16으로 ImageNet-C 15종(severity 5)과 6개 csOOD 데이터셋(Places-C·Textures-C·iNaturalist-C·SUN-C·SSB-Hard-C·NINCO-C)을 섞은 스트림에서 단독 plug-in으로 평균 H-score 66.1%(UniEnt 63.9%)를 얻고 COME에 얹으면 68.4%(+4.7)이며, UniEnt보다 2.5배 빠르고 GPU 메모리는 12%만 쓰며, LAION-C·ImageNet-R·ImageNet-Sketch와 closed-set·continual 프로토콜에서도 비교한 모든 baseline의 성능을 높인다. 확인한 본문 범위에 별도 한계 서술은 없다.

**코드**: 공개 예정 (논문에 [ekyle0522/TALOR](https://github.com/ekyle0522/TALOR) 명시, 확인 시점 README만 있고 구현 준비 중 표기)

**태그**: test-time-adaptation, open-set, ood-detection, training-free

---

### [MixSIS: Mixed-supervised instance segmentation](https://arxiv.org/abs/2610.37138)

**한 줄 요약**: 한 데이터셋(한 이미지 안까지) 안에 image·point·box·mask 주석이 섞여 있어도 SAM으로 모두 pseudo mask로 바꿔 instance segmentation을 학습하는 mixed-supervised 과제와 baseline(AnnsMixer).

**핵심 기여**: 약지도 instance segmentation은 한 종류의 주석만 가정하지만, 쉬운 물체는 point로·어려운 물체는 box나 mask로 주석 수준을 달리하는 편이 주석 비용 면에서 효율적이라는 문제의식이다. AnnsMixer는 box·point를 SAM prompt로 쓰고 image-level label은 CAM 상위 2개 peak를 point prompt로 바꾼 뒤, prompt당 SAM 출력 3개를 stability score·predicted IoU로 거르고 NMS로 중복을 지운 pseudo mask로 일반 Mask R-CNN을 학습한다. COCO val의 세 혼합 설정(Mix 1~3)에서 mAP 0.323/0.295/0.266으로 MAL·SAPNet·BoxLevelSet보다 높고(Mix 1의 Mask R-CNN 0.239, MAL 0.317), 단일 주석 WSIS에서는 box 34.5(MAL 35.7)·image-level 22.0(WeakSAM 21.0)이며, 사례 연구에서 box·point 혼합 주석으로 추정 주석 시간을 82~93% 줄이는 동안 mAP는 평균 약 5% 낮아지고, VOC에 box 주석을 합치면 mAP가 0.288에서 0.385(+34%)로 오른다. 한계로 point·image-level pseudo mask의 품질이 낮고(원본과 일치하는 비율 66.8%·48.5%), 주석 시간은 선행 연구 기반 추정치이며, Mask R-CNN만 개념 증명으로 썼고 데이터셋 병합에 domain adaptation을 하지 않았다고 밝힌다.

**코드**: 공개([chwilms/MixSIS](https://github.com/chwilms/MixSIS) · GPL-3.0), 학습된 Mask R-CNN 가중치와 pseudo-annotation도 공개

**태그**: segmentation, weakly-supervised, label-efficiency, foundation-model

---

### [AxisQ: Depth-Adaptive Channel--Frequency Quantization for Camouflaged Object Detection](https://arxiv.org/abs/2610.36844)

**한 줄 요약**: camouflaged object detection 모델의 post-training quantization에서 얕은 층은 channel 영역, 깊은 층은 local-frequency 영역으로 bit를 배분하는 depth-adaptive 정밀도 할당 방법.

**핵심 기여**: COD는 약한 texture·경계 단서에 의존하는데 공격적인 PTQ가 이 단서를 지우고, 기존 PTQ는 계층형 backbone 전체에 하나의 정밀도 배분 영역만 쓴다는 문제의식이다. 층별 평균 activation bit 예산을 고정한 채 얕은 특징은 channel 단위, 깊은 특징은 local-frequency 단위로 COD-aware 민감도에 따라 bit를 나누고, 경계 가중 gradient·오차 통계를 넣은 boundary-aware Hessian 근사로 block reconstruction을 한다(보정 이미지 128장, reconstruction 1,024장·block당 20,000 iteration). W2A2에서 CAMO weighted F-measure가 CFRN .727(LS-ViT .645)·CamoFormer-P .500(.375)로 상대 12.7%·33.3% 높고 CFRN은 20개 데이터셋-지표 비교 전부에서 앞서지만, W4A4에서는 최고 baseline과의 차이가 .003~.005로 좁아진다. 별도 한계 절은 없으며, 시험한 COD 모델이 2종이고 높은 정밀도로 갈수록 이득이 줄며(W2A4 CHAMELEON에서 MAE 소폭 악화) COD-TDQ의 W2A2 수치는 저자 공개 결과가 아닌 자체 확장이라고 적고 있다.

**코드**: 공개 예정 ([chi558/AxisQ](https://github.com/chi558/AxisQ) 저장소에 README·논문 PDF만 있고 "Code will be released" 표기, 라이선스 없음)

**태그**: quantization, efficient-inference, segmentation, camouflaged-object-detection

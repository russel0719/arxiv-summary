# arXiv cs.CV Daily Digest — 2026-09-14 (arXiv 공개일)

- **전체 신규 논문 수**: 90편 (new 74 + cross-list 16)
- **선별 수**: 8편

## 오늘의 트렌드

의료 영상(분할·진단·모달리티 변환)이 가장 두꺼운 군집이고, Gaussian Splatting·point cloud 정합·scan 재국소화 등 3D 계열과 VLM·에이전트 벤치마크가 뒤를 잇는다. RGB-thermal·편광·NIR 등 다중 센서 융합과 UAV·농업 응용도 여러 편이다. 방법론으로는 동결 foundation model 위에 경량 adapter·head를 얹는 구성, Mamba/SSM 백본, 물리·절차 기반 합성 데이터, 기존 평가 프로토콜의 인과적 재검증이 반복된다.

---

### [Multimodal Floorplan Encoding: Learning Dense Modality-Invariant Representations](https://arxiv.org/abs/2609.12723)

**한 줄 요약**: 동결 DINOv3 위에 DPT head를 얹고 셀 단위 InfoNCE로 학습해, 벡터 CAD·래스터 렌더링·센서 밀도맵 등 형태가 다른 2D 실내 도면을 하나의 dense latent grid로 매핑하는 modality 불변 encoder.

**핵심 기여**: 도면은 벡터 CAD 도면, 래스터 렌더링, 센서 유래 밀도맵 등 이질적 형태로 존재해 정렬·검색 같은 기하 중심 과제에서 modality 간 전이가 어렵다는 문제에서 출발한다. Multimodal Floorplan Encoder(MMFE)는 frozen DINOv3 backbone에 학습 가능한 Dense Prediction Transformer head를 결합하고, modality 간 공간적으로 대응하는 셀을 positive로, 나머지 모든 셀을 negative로 삼는 per-cell InfoNCE로 학습한다. 통제된 similarity transform을 적용하고 feature-grid warping으로 기하 일관성을 강제해 기하 왜곡에 대한 강인성을 높인다. CubiCasa5K·Swiss Dwellings·Zillow Indoor·Aria SE 네 소스의 도면 14,939장(modality 쌍 44,817개)으로 학습하고 held-out Structured3D에서 평가한 결과, cross-modal dense matching PCK@3.0이 easy/medium/hard 94.53/91.05/89.82%, RANSAC 정렬 Acc@10이 medium 84.38%·hard 75.91%이며, 학습된 aggregation(SALAD)과 결합한 Top-1 retrieval은 55.06%(NetVLAD 결합 시 24.29%)를 기록한다. ECCV 2026 TwinWorld Workshop 발표 논문이다.

**코드**: 불명

**태그**: correspondence, image-retrieval, ssl-backbone, image-embedding, foundation-model

---

### [SCORE: SubDistribution-aware Collaborative Knowledge Reinforcing for Cloth-Hybrid Lifelong Person Re-Identification](https://arxiv.org/abs/2609.12577)

**한 줄 요약**: 의상 일관 데이터와 의상 변경 데이터가 교대로 들어오는 lifelong person re-ID에서, identity별 분포 subprototype으로 identity 내부 다양성을 명시적으로 모델링해 두 지식의 충돌과 파국적 망각을 줄인다.

**핵심 기여**: Lifelong Person Re-Identification(LReID)은 비정상 데이터 스트림에서 통합 person retrieval 모델을 학습하는 과제인데, 기존 방법은 각 인물의 의상이 일정한 시나리오에 집중해 왔다. 의상 일관·의상 변경 데이터가 번갈아 등장하는 Cloth-Hybrid LReID에서는 clothing-relevant 지식과 clothing-irrelevant 지식이 충돌해 파국적 망각이 크게 악화된다고 지적한다. SCORE는 Adaptive SubDistribution Modeling으로 identity마다 분포 subprototype 집합을 할당해 intra-identity diversity를 포착하고 두 종류 지식의 호환성을 높이며, Distributional Knowledge Reinforcement로 옛 subprototype의 지식을 collaborative aligning을 통해 새 subprototype에 유지한다. 광범위한 실험에서 state-of-the-art 성능을 달성했다고 보고하며, 정량 수치는 초록에 제시되지 않는다.

**코드**: 공개([ECCV2026-SCORE](https://github.com/zhoujiahuan1991/ECCV2026-SCORE))

**태그**: re-identification, continual-learning, metric-learning, image-retrieval

---

### [RelateAnything: Real-Time Open-Vocabulary Relation Prediction From Any Inputs](https://arxiv.org/abs/2609.12552)

**한 줄 요약**: 이미지와 임의 출처의 region을 입력받아, 추론 시 문자열로 주어지는 predicate 어휘에 대해 관계 점수를 반환하는 53M 파라미터 open-vocabulary 관계 예측 모델로 20 ms/frame으로 동작한다.

**핵심 기여**: open-vocabulary detection과 promptable segmentation은 taxonomy를 모델 밖의 입력으로 옮겼지만, scene-graph 모델은 여전히 한 주석 체계의 50~56개 predicate로 학습·평가되고 relation head가 object label에 조건화되어 특정 detector에 묶여 있다는 문제를 제기한다. 원인으로 free-text이면서 검증된 관계 코퍼스의 부재, 미학습 어휘를 받을 수 없는 label 조건부 구조, 학습 코퍼스와의 일치를 보상해 큰 어휘가 퇴보로 보이는 표준 metric 세 가지를 든다. RelateAnything는 object label을 입력으로 받지 않아 region 출처를 바꿔도 재학습이 필요 없고, 어휘는 학습된 classifier가 아닌 text embedding bank로 처리한다. 19,103개 predicate 학습에는 positive-unlabeled 지도와 반의어를 분리하는 text encoder가 필요한데, contrastive encoder는 반의어를 cosine 0.95로 임베딩한다고 밝힌다. 지도를 위해 numbered box marker 기준으로 생성하고 기하적으로 검증한 474k 이미지·4.3M 관계·10,102개 free-text predicate의 RA-4M을 구축하고, 표준 recall이 포착하지 못하는 6개 축을 측정하는 OV-SGG-Bench를 제안한다. cross-dataset 벤치마크 3개와 zero-shot 1개에서 비슷한 규모의 최강 open-vocabulary 방법 대비 mean recall 2.3~3.5배를 기록하고 이 격차는 실제 detector를 붙여도 유지되며, 3B VLM scene-graph 모델을 2% 미만의 파라미터로 두 metric 모두에서 앞선다. in-domain 측정은 전이 이득을 약 5배 과대평가한다고 보고한다.

**코드**: 공개([RelateAnything](https://github.com/Maelic/RelateAnything) · 가중치 [Hugging Face](https://huggingface.co/collections/maelic/relateanything) · RA-4M [Hugging Face](https://huggingface.co/datasets/maelic/RA-4M))

**태그**: open-vocab-detection, scene-graph, dataset-benchmark, efficient-inference

---

### [Feature Recovery for Object Understanding After Irreversible Fire Damage](https://arxiv.org/abs/2609.12078)

**한 줄 요약**: 화재로 물리적으로 변형된 물체의 검출·검색·재질 복원을 다루는 벤치마크 TRACE와, host encoder를 동결한 채 열화된 feature를 원형 정렬 표현으로 되돌리는 plug-and-play Feature Recovery Module.

**핵심 기여**: 화재 후 물체는 기하·재질 상태·외관이 비가역적으로 바뀌며, 표준 image corruption과 달리 물체의 물리 구조 자체가 변한다는 점에서 출발한다. TRACE는 실사에 기반한 합성 장면 21.4K개와 189개 카테고리·499개 물체 identity의 pristine→degraded 진행 쌍으로 구성되며, degraded-object detection, pristine-state recovery·retrieval, original material recovery, pristine description generation, functional reasoning 다섯 과제를 정의한다. 기존 모델은 심각도가 오를수록 급락해 RF-DETR mAP는 상대 71% 감소하고 InternVL3.5 retrieval R@1은 93.85에서 28.11로 떨어진다. Feature Recovery Module(FRM)은 paired feature supervision만으로 학습되어 host를 동결한 채 열화된 encoder feature를 pristine 정렬 표현으로 매핑하며, scene-level detection, CLIP/SigLIP2 feature recovery, 네 개의 object-level VLM 과제를 모두 개선하고 열화가 심할수록 이득이 커진다. VLM host와 심각도 전반에서 상대 이득은 retrieval 12.5%, material recovery 20.1%, description generation 13.2%, functional reasoning 12.4% 평균이다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, foundation-model, object-detection, dataset-benchmark

---

### [An End-to-End Automated Pipeline for Controllable Crack Data Synthesis](https://arxiv.org/abs/2609.12431)

**한 줄 요약**: 절차적으로 샘플링한 Bézier 골격을 GAN으로 균열 mask로 바꾸고, 외관 guidance와 기하 guidance를 분리한 dual-ControlNet diffusion으로 경계가 정합된 균열 이미지를 합성하는 균열 검사용 데이터 생성 파이프라인.

**핵심 기여**: 자동 균열 검사는 딥러닝에 점점 의존하지만 결함 데이터가 희소하고 제어가 어려워 신뢰성이 제한되며, 기존 생성 증강은 균열 합성을 일반 이미지 생성 과제로 다뤄 형태·경계 충실도·장면 맥락 제어가 부족하다고 지적한다. 제안 파이프라인은 균열 기하와 검사 맥락을 재사용 가능한 계산 제약으로 형식화한다. 첫 단계에서 절차적으로 샘플링한 Bézier 곡선 골격을 GAN으로 사실적인 균열 mask로 변환해 수동 mask 설계 없이 다양한 형태를 대량 생성하고, 두 번째 단계에서 dual-ControlNet diffusion으로 appearance guidance와 geometric guidance를 분리하며 edge 기반 branch가 엄격한 경계 일관성을 강제한다. background-free 합성과 context-aware inpainting을 모두 지원한다. CRACK500과 CrackTree200에서 기존 증강 베이스라인 대비 일관된 향상을 보고하며, 정량 수치는 초록에 제시되지 않는다. Advanced Engineering Informatics 심사 중인 논문이다.

**코드**: 불명

**태그**: defect-detection, industrial-inspection, sim2real, generative, segmentation

---

### [DERA: Detached Edge-Residual Adaptation for Prohibited item Detection](https://arxiv.org/abs/2609.12411)

**한 줄 요약**: X-ray 보안검색 영상의 금지 물품 검출을 위해 foundation detector를 보존한 채 pixel-difference edge pyramid와 분리된 경계 prior를 residual head로 초기 시각 단계에 주입하는 적응 프레임워크로, 최종 적응 단계의 학습 파라미터는 14.7K다.

**핵심 기여**: X-ray 영상의 금지 물품 검출은 물체 중첩·약한 텍스처·재질 혼잡으로 의미적 외관과 물체 경계가 모두 흐려져 어렵다는 문제에서 출발한다. DERA는 계층적 시각 feature와 병렬 pixel-difference edge pyramid를 결합하고, 학습 시 instance mask의 윤곽에서 객체별 boundary prior를 학습한다. 이 detached prior가 edge-sensitive feature를 게이팅하고, 게이팅된 feature는 residual head를 통해 초기 시각 단계에 주입된다. 단계적 설계로 적응 초기에는 foundation detector를 그대로 보존하고, 경계 지도를 의미 feature 학습에서 분리하며, 최종 적응 단계의 학습 파라미터를 14.7K로 제한한다. PIDray·CLCXray·STCray에서 베이스라인 대비 각각 3.1·1.6·2.4 AP 향상을 보고한다.

**코드**: 불명

**태그**: object-detection, peft, industrial-inspection, foundation-model

---

### [Generative Retrieval for Unsupervised Text-Based Person Search](https://arxiv.org/abs/2609.12965)

**한 줄 요약**: 라벨 없는 이미지만으로 텍스트 기반 사람 검색을 학습하기 위해 3단계 설명 생성으로 세밀하고 다양한 pseudo text를 만들고, GMM 기반 신뢰도 가중으로 잡음 쌍의 영향을 줄이는 생성-후-검색 프레임워크와 대규모 데이터셋 LargeFine-Person.

**핵심 기여**: Text-Based Person Search(TBPS)는 자연어 설명으로 대규모 갤러리에서 대상 인물 이미지를 검색하는 과제로, 대부분 수작업 image-text 쌍의 지도학습에 의존한다는 문제에서 출발해 라벨 없는 이미지만 있는 비지도 TBPS를 다룬다. GTR+의 생성 단계는 base tier에서 자동 QA로 기본 시각 속성 설명을 만들고, intermediate tier에서 inter-sample contrastive 메커니즘으로 세밀한 디테일을 강화하고, advanced tier에서 stylized expansion으로 텍스트 다양성을 늘리는 3단계 순차 과정이다. 검색 단계에서는 image-text 쌍을 Gaussian Mixture Model로 clean/noisy로 모델링하고, 실시간 image-text 유사도와 이전 단계의 정적 텍스트 생성 확률로 보정해 학습 중 적응적 샘플 가중치를 부여한다. 고품질·세밀·다양한 텍스트 주석을 갖춘 대규모 TBPS 데이터셋 LargeFine-Person을 함께 제공해 비지도 설정의 사전학습 벤치마크로 삼는다. 여러 TBPS 벤치마크에서 GTR+와 LargeFine-Person의 효과와 일반화를 검증했다고 보고하며, 정량 수치는 초록에 제시되지 않는다.

**코드**: 공개([GTR](https://github.com/Flame-Chasers/GTR))

**태그**: image-retrieval, re-identification, vlm, dataset-benchmark, metric-learning

---

### [Same Encoder, Different Winner: A Paired-View Framework for Cell Painting Encoder Evaluation](https://arxiv.org/abs/2609.12761)

**한 줄 요약**: 중심 세포를 고정하고 주변 픽셀만 제거·증강한 네 가지 짝 view로 Cell Painting 이미지 encoder(DINOv3 ViT-B/16·OpenPhenom·SubCell)를 평가해, 네 가지 표준 프로토콜이 같은 encoder들의 순위를 체계적으로 다르게 매김을 보인다.

**핵심 기여**: Cell Painting용 vision encoder는 보통 replicate mean average precision 단일 평가로 순위가 매겨진다는 점을 문제로 삼는다. CP-BG-Bench는 중심 세포를 고정한 채 raw crop(C), segmented(S), density-augmented 변형(CD, SD) 네 view를 만들어 주변 픽셀 제거·증강을 통제된 개입으로 쓴다. JUMP-CP·RxRx1·RxRx3-core 세 데이터셋, 세 encoder, 네 프로토콜(replicate mAP, scIB batch integration, CellProfiler feature 예측, cross-batch perturbation recall)로 평가한 결과, 프로토콜 간 순위 불일치가 cell 대 background, morphology 대 context, within-study 대 across-batch 세 축으로 분해된다. 가장 큰 효과로, RxRx3-core에서 SubCell의 segmented 입력은 crop replicate mAP의 94%를 유지하지만 crop R@10은 32%만 유지해 분할 후 보존되는 within-study 신호가 대부분 전이되지 않으며, density augmentation은 within-study C→S 격차의 84%를 회복하지만 cross-batch 격차는 8%만 회복한다. segmented view가 세 데이터셋 중 둘에서 CellProfiler feature를 crop과 같거나 더 잘 예측해 replicate-mAP 순위가 뒤집히고, C→S 격차는 데이터셋 간에는 한 자릿수 order로 차이 나지만 encoder 간에는 비슷해 background 기인 이득이 encoder가 아닌 실험 설계에 의해 정해진다고 분석한다. paired-view 데이터셋, 재구성 파이프라인, 학습된 checkpoint 36개, aggregated embedding, 전체 평가 suite를 공개할 예정이라고 밝힌다.

**코드**: 공개 예정

**태그**: image-embedding, dataset-benchmark, ssl-backbone, fine-grained

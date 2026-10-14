# arXiv cs.CV Daily Digest — 2026-10-14 (arXiv 공개일)

- **전체 신규 논문 수**: 479편 (new 381 + cross-list 98)
- **선별 수**: 12편

## 오늘의 트렌드

자기회귀 비디오 확산과 world/world-action 모델이 가장 두꺼운 군집으로, KV 캐시 압축·캐싱·few-step 증류로 롤아웃 비용을 깎는 기법과 로봇 정책으로의 연결이 함께 나온다. VLM 쪽은 공간·시간 추론 벤치마크와 토큰 프루닝·환각 완화가 이어지고, feed-forward 3D 재구성과 Gaussian Splatting 압축이 한 덩어리를 이룬다. 인식 쪽에서는 얼굴 위조·AIGI 검출의 일반화, 그리고 자기지도 백본의 효율적 사전학습과 구조적 압축이 한 축을 이룬다.

---

### [Growing to See: Efficient Pretraining of Self-Supervised Vision Transformers](https://arxiv.org/abs/2610.16817)

**한 줄 요약**: 얕은 모델에서 시작해 학습 중 층을 삽입하는 progressive depth growth를 MAE와 DINOv3 자기지도 사전학습에 적용해, 학습 FLOPs를 줄이면서 다운스트림 성능을 높인 연구.

**핵심 기여**: LLM에서 다시 주목받는 점진적 깊이 성장이 자기지도 비전 트랜스포머의 표현 품질과 내부 계산 패턴에 어떤 영향을 주는지 밝혀진 바가 없다는 문제의식이다. MAE와 DINOv3 두 계열에 깊이 성장을 적용하되 MAE는 인코더만 키우고 디코더는 고정하며, 자기증류 DINOv3는 성장 시점마다 teacher 백본을 확장된 student 가중치로 리셋한 뒤 EMA 갱신을 재개하고, 다운스트림 성능·중간층 표현·어텐션 패턴을 분석한다. 전역·밀집 과제 전반에서 학습 FLOPs를 13.9~24.8% 줄이면서 성능이 오르고, ImageNet linear-probe 정확도는 최대 3.36%p 상승한다. 중간층의 다운스트림 성능도 함께 오르며, MAE에서는 전역·국소 어텐션이 번갈아 나타나는 패턴이, DINOv3에서는 local→global 어텐션 진행이 더 이른 층에서 나타난다.

**코드**: 불명

**태그**: ssl-backbone, foundation-model, image-embedding

---

### [Self-Supervised Learning of Semantically Consistent Visual Features via a Simple 3D Prior](https://arxiv.org/abs/2610.16988)

**한 줄 요약**: DINOv2류 특징이 대칭·반복 부위에서 좌우를 구분하지 못하는 한계를, 데이터셋 수준 대조학습과 분포 매칭으로 범주의 거친 3D 형상을 학습해 보완하는 자기지도 semantic correspondence 특징 학습.

**핵심 기여**: DINOv2나 Stable Diffusion 특징은 이미지 간 semantic correspondence에 널리 쓰이지만 대칭이나 반복 부위를 가진 범주에서 좌우를 구분하지 못하며, 기존 개선책은 키포인트 쌍·카메라 포즈 같은 지도 데이터에 기대거나 객체를 3D 구로 가정하는 제한적 토폴로지에 묶여 있었다는 문제의식이다. 인스턴스 단위의 비싼 analysis-by-synthesis 대신 전역 데이터셋 수준의 contrastive learning과 distribution matching으로 범주의 거친 형상과 외형을 학습하고, 추가 기하 손실을 결합해 실제 이미지에서 추출한 특징의 전역·국소 통계를 재현하도록 한다. 토폴로지가 복잡한 여러 객체 범주에서 정량 결과를 제시하며, 원본 DINOv2가 구분하지 못하던 좌우 부위가 학습된 특징에서는 뚜렷이 분리된다.

**코드**: 불명

**태그**: ssl-backbone, correspondence, image-embedding, 3d

---

### [Towards Complementary Keypoint Detection via Mixture of Detectors](https://arxiv.org/abs/2610.16762)

**한 줄 요약**: 이종 keypoint detector들을 하나의 인코더로 증류한 뒤, 패치마다 예산에 맞는 detector를 고르는 라우터를 다운스트림 매칭 품질 보상으로 학습한 Mixture of Detectors(MoD).

**핵심 기여**: 기존 detector들은 장면 구조와 키포인트 예산에 따라 상보적 강점을 보이는데, 단일 detector에 의존하면 키포인트 분포가 비최적이 된다는 문제의식이다. 1단계에서 이종 detector들을 VGG 인코더와 다중 경량 헤드로 증류해 한 번의 forward로 여러 검출 맵을 얻고, 2단계에서 인코더·헤드를 고정한 채 텍스처 특징과 키포인트 예산을 입력받는 경량 라우터가 8×8 패치마다 가장 적합한 detector를 할당한다. 라우터는 휴리스틱 지도 대신 키포인트 수량과 정밀도를 함께 반영하는 다운스트림 매칭 품질 보상으로 학습된다. MegaDepth·ScanNet·HPatches에서 넓은 키포인트 예산 범위에 걸쳐 강한 baseline을 일관되게 상회한다.

**코드**: 불명

**태그**: feature-matching, correspondence, distillation

---

### [TartanMatch: Towards Universal Dense Correspondence Across Modalities](https://arxiv.org/abs/2610.14513)

**한 줄 요약**: RGB·event·thermal·depth·projected LiDAR 5개 모달리티의 25개 순서쌍 전부를 하나의 공유 네트워크로 처리하는 dense correspondence 모델.

**핵심 기여**: 대부분의 dense correspondence 방법이 RGB-RGB나 소수 모달 쌍에 한정되고, 쌍마다 모델을 따로 두면 센서 수에 따라 확장이 어렵고 쌍 간 긍정 전이도 포기한다는 문제의식이다. RGB로 사전학습된 UFM 백본(DINOv2 인코더·정보공유 transformer·DPT 헤드)을 구조 변경 없이 공유하고 모달리티별 경량 입력 projection만 붙여, 실제·합성 혼합 데이터로 인코더를 동결한 1단계와 end-to-end 2단계로 학습한다. zero-shot 실세계 벤치마크에서 가장 강한 baseline 대비 EPE를 cross-modal 매칭에서 61.9%, same-modal 매칭에서 49.6% 줄인다. 모든 쌍을 함께 학습하는 것이 쌍별 학습보다 평균 매칭 정확도가 높고, 특히 어려운 cross-modal 쌍에서 차이가 크다.

**코드**: 불명 (프로젝트 페이지 [tartanmatch.github.io](https://tartanmatch.github.io/))

**태그**: correspondence, feature-matching, foundation-model

---

### [What Really Works for Universal Multimodal Embeddings? A Controlled Study of Contrastive Training Strategies](https://arxiv.org/abs/2610.15035)

**한 줄 요약**: MMEB 통제 실험으로 negative 선택·배치 구성·gradient 조절 등 대조학습 전략의 실제 효과를 재검증하고, MLLM-as-a-Judge로 top-1 검색 오류를 분해해 실패 양상을 진단한 연구.

**핵심 기여**: 다양한 대조학습 전략이 제안됐지만 통제된 재현 조건에서의 실효성이 불분명하다는 문제의식에서, MMEB 위의 통일된 벤치마크 프레임워크로 대표 전략들을 평가한다. 대부분의 전략이 표준 정렬 baseline 대비 미미한 이득에 그치고 일부는 전체 성능을 떨어뜨리며, top-1 검색 결과를 라벨된 positive·false negative(라벨 없는 유효 매치)·hard/easy negative 오류로 분해하는 MLLM-as-a-Judge 진단으로 원인을 추적한다. 고유사도 negative의 gradient를 키우면 일반화가 일관되게 나빠지고(gradient distortion), 양·음 유사도 분포의 분리폭 확대가 검색 성능 향상으로 이어지지 않으며(distribution illusion), hard-negative mining·false-negative 완화·hard-batch 구성은 단독으로는 이득이 작지만 결합하면 Qwen2-VL-2B 기준 MMEB 평균 6.0% 향상에 이른다.

**코드**: 공개([UME-Recipes](https://github.com/alibaba-multimodal-industrial-ai/UME-Recipes))

**태그**: metric-learning, image-embedding, image-retrieval, vlm

---

### [Web Scale on a Budget: Tail-Aware Retrieval Evaluation](https://arxiv.org/abs/2610.17986)

**한 줄 요약**: 인스턴스 검색 벤치마크의 distractor 1억 장을 모두 인덱싱하지 않고, 소량 무작위 샘플에서 추정한 쿼리별 retrieval hardness로 대규모 mAP를 복원하는 평가 방법.

**핵심 기여**: ILIAS처럼 distractor를 1억 장까지 늘린 벤치마크는 모델·ablation마다 수백 GPU시간과 약 200GB의 descriptor를 요구한다는 문제의식이다. 양성보다 상위에 오르는 distractor 수가 갤러리 크기에 대해 이항분포를 따른다는 점에서 갤러리 규모와 무관한 쿼리별 retrieval hardness를 정의하고, 추천시스템·생체인식의 sampled-rank 기법을 시각 검색에 맞게 쿼리 단위로 추정 가능하게 만든다. ILIAS·INSTRE의 1억 규모와 GLDv2의 759k distractor 풀에서 검증해, 5% 샘플(인덱싱 20배 감소)로 tail-aware(EVT) 추정치가 5개 백본·3개 벤치마크·2개 distractor 풀 전반에서 대규모 mAP와 약 0.01 이내(평균 절대 오차 0.005)로 수렴한다. 추천시스템식 count baseline은 +0.037~+0.068 과대예측하고, 같은 부분집합에서 지표를 그대로 보고하면 +0.08~+0.13 어긋난다.

**코드**: 공개 예정 (코드와 쿼리별 hardness 공개를 명시, 저장소 링크는 본문에 없음)

**태그**: image-retrieval, dataset-benchmark, image-embedding

---

### [DIME: Scaling Facial Representation Learning via Differential Masked Autoencoding](https://arxiv.org/abs/2610.17015)

**한 줄 요약**: 동일 인물 이미지 쌍의 재구성 차이 방향을 실제 차이와 정렬시키는 differential masked autoencoding으로, 2천만 장 얼굴 이미지에서 dense 표현을 학습한 자기지도 사전학습.

**핵심 기여**: 기존 pretext task는 각 이미지의 외형을 모델링하기 때문에 identity·pose·조명이 신호를 지배하고 identity 내 미세한 얼굴 변화는 학습에 거의 기여하지 못해, 세밀 얼굴 분석에서 스케일링 수익이 체감한다는 문제의식이다. DIME는 identity가 같은 두 마스킹 이미지를 각각 재구성하고 Explicit Differential Direction Supervision(EDDS)으로 재구성 차이의 방향을 실제 차이와 정렬하며, 크기를 무시하므로 미세 변화도 큰 pose·조명 변화만큼 반영되고 source isolation으로 각 재구성은 자기 이미지에만 의존한다. identity 라벨은 쌍 구성에만 쓰고 dense annotation이 필요 없으며, 추론 시 인코더는 단일 이미지만 받는다. 6M→20M 사전학습 확장 시 BP4D AU 검출 F1이 5.9점 오르는 반면 MAE는 0.5점에 그치고, AU 검출·강도 추정·cross-domain anti-spoofing·landmark·head pose·face parsing·face generation에서 얼굴 특화 방법들을 상회한다.

**코드**: 공개([프로젝트 페이지](https://cv-ac.github.io/DIME_page))

**태그**: ssl-backbone, fine-grained, image-embedding, face-analysis

---

### [3D-VITAL: Visibility-aware Identity Training from Artificial Liftings of 3D Reconstruction model for Cross-View Object Re-Identification](https://arxiv.org/abs/2610.16692)

**한 줄 요약**: 단일 뷰 3D mesh 재구성으로 만든 novel view를 per-pixel visibility map으로 걸러 지상↔항공 cross-view ReID 학습에 쓰는 방법.

**핵심 기여**: 한 시점으로 학습해 다른 시점에서 추론하는 Single-View Aerial-Ground ReID에서 시점 격차를 메우려 생성모델로 novel view를 합성하는데, 단일 뷰 3D mesh 재구성 파이프라인은 기하가 틀린 mesh와 원본에서 보이지 않던 영역의 환각 텍스처라는 두 종류의 불량 데이터를 만든다는 문제의식이다. 렌더링의 결정적 부산물로 얻는 per-pixel visibility map을 활용해, Cross-View Consistency Filtering(CVCF)이 가시 패치의 원본–novel view 일관성으로 기하 오류 mesh를 버리고, Visibility-Aware Attention Supervision(VAAS)이 학습 중 모델의 어텐션을 렌더링의 신뢰 영역으로 유도한다. SV AG-ReID 벤치마크 3종에서 새 SOTA를 보고한다.

**코드**: 공개 예정([3D-VITAL](https://github.com/TurtleSmoke/3D-VITAL))

**태그**: re-identification, image-retrieval, sim2real, 3d

---

### [TAG: Calibrating SAM3 for Universal Image Segmentation without Dense Supervision](https://arxiv.org/abs/2610.14651)

**한 줄 요약**: SAM3의 병목이 마스크 품질이 아니라 concept 인식임을 보이고, 이미지 수준 라벨만으로 텍스트 앵커를 타깃 도메인에 재접지해 presence confidence를 보정하는 Text Anchor re-Grounding(TAG).

**핵심 기여**: SAM3가 concept prompt로 범용 분할을 약속하지만 다운스트림에서 성능이 불안정하며, 인식한 객체는 정확히 분할하되 어떤 concept이 존재하는지 판정하지 못하는 것이 원인임을 경험적으로 보인다. Anchor Residual Pathway의 이미지 조건부 low-rank adapter로 텍스트 앵커를 타깃 분포에 재접지하고 이후 텍스트 조건 상호작용을 조절하며, 이미지 수준 카테고리 라벨만으로 binary cross-entropy와 Soft Boundary Ranking을 함께 최적화해 presence confidence를 보정하고 혼동되는 negative와 구분한다. Confidence-Weighted Distillation으로 MLLM의 의미 맥락과 SAM3의 공간 prior를 결합해 수작업 주석 없이 보정한다. 학습 파라미터 3.1M으로 다양한 시나리오에서 성능을 내고, 일부 지표에서는 mask-supervised 방법을 능가한다.

**코드**: 공개 예정([TAG_SAM3](https://github.com/MiSsU-HH/TAG_SAM3))

**태그**: segmentation, open-vocab-detection, foundation-model, calibration, peft

---

### [Robust Logical Anomaly Detection under Capture Shifts via Synthetic Anomalies](https://arxiv.org/abs/2610.18295)

**한 줄 요약**: 밝기 감소·zoom-out 같은 촬영 조건 변화에 정상 참조 기반 논리 이상 검출기가 크게 무너짐을 보이고, LM과 이미지 편집기로 만든 합성 이상으로 분류기를 학습해 정상 데이터와 비교하지 않고 판정하는 프레임워크.

**핵심 기여**: 누락·추가·잘못 조합된 부품 같은 논리 이상 검출기는 MVTec LOCO에서 거의 완벽한 image-level AUROC를 내지만 촬영 조건 변화에 대한 강건성은 검증되지 않았다는 문제의식이다. 테스트 이미지를 무작위로 원본 유지·밝기 감소·zoom-out 중 하나로 처리하는 이질 perturbation 프로토콜에서 정상 참조 방법들은 9.7~34.1 AUROC 포인트를 잃고, CSAD와 SALAD는 97.7%·96.4%에서 68.1%·62.3%로 떨어진다. 제안 방법은 제품의 짧은 설명에서 언어모델이 이상 유형과 편집 지시를 도출하고 이미지 편집기가 정상 이미지에 적용하며, DINOv3 가중치의 ConvNeXt-L 분류기가 편집 이미지를 자동 발견한 정상 sub-mode와 구분하도록 학습된다. 전체 레시피로 clean 94.9% AUROC(SALAD·CSAD보다 1.5~2.8 낮음), perturbation 하에서 94.1%를 내고, 밝기·zoom-out 증강 없이 학습해도 92.5%(clean 93.2%)를 유지한다. 언어모델과 이미지 편집기가 closed model이라 생성 단계를 정확히 재현할 수 없다는 한계를 밝힌다.

**코드**: 공개 예정 (논문 채택 시 코드·합성 이미지 공개 명시, 합성 이미지는 CC BY-NC-SA 4.0)

**태그**: anomaly-detection, industrial-inspection, defect-detection, sim2real

---

### [COMPASS: Contextual Moment Prior Alignment for Generalizable AIGI Detection](https://arxiv.org/abs/2610.18034)

**한 줄 요약**: 소량의 unlabeled proxy set으로 추정한 활성 공분산을 사전학습 가중치 분해에 반영해, 타깃 의미를 보존한 채 residual adapter만 위조 특징을 학습하게 하는 AIGI·deepfake 검출 adaptation.

**핵심 기여**: VFM을 제한된 학습 분포에 맞추면 전이 가능한 표현이 손상되는 asymmetry 현상이 있고, 최근 subspace adaptation은 고크기 주성분을 동결하고 residual만 학습하지만 magnitude 기반 분해는 데이터와 무관해 타깃 의미와 어긋날 수 있다는 문제의식이다. COMPASS는 약 80장 수준의 unlabeled Semantic Proxy Set으로 타깃 활성 통계를 추정하고 공분산 유도 SVD로 가중치를 principal과 residual로 나눠, principal은 동결해 안정적 의미 참조로 두고 residual adapter가 위조 변이를 학습한다. proxy 보정은 gradient 최적화가 필요 없고, adapter와 principal 가중치는 추론 시 단일 가중치로 재파라미터화된다. cross-dataset·cross-method·joint·open-world cross-generator 평가에서 Deepfake와 AIGI 벤치마크 모두 SOTA를 보고한다.

**코드**: 공개 예정

**태그**: forgery-detection, foundation-model, peft

---

### [Carve VFM: Carving Specialists out of Generalists, Automatic Task-Specific Compression of Vision Foundation Models](https://arxiv.org/abs/2610.16813)

**한 줄 요약**: DINOv3·MetaCLIP-2 같은 VFM에서 과제별 층 용량 배분을 탐색하고 closed-form 저랭크 보정으로 제거된 기능을 복구해, 재학습 없이 수 분 만에 조밀한 전문 서브네트워크를 잘라내는 구조적 pruning.

**핵심 기여**: VFM의 추론 비용이 배포를 제약하는데, 파인튜닝은 크기를 줄이지 못하고 증류는 비싼 teacher 학습이 필요하며 구조적 pruning은 공격적 압축에서 선택과 복구를 별개로 다뤄 실패한다는 문제의식이다. 층 간 용량은 과제 민감도를 따라야 하고 층 내 제거는 중요도만이 아니라 남은 것에서 복구 가능한지에 달린다는 관찰에서, 주어진 VFM·calibration set·파라미터 예산으로 층별 과제 특화 용량 배분을 탐색하고, 복구 인식 fitness로 탐색을 안내하며, 반복 closed-form 저랭크 보정을 생존 가중치에 병합한다. 단일 GPU에서 수 분 안에 백본 재학습 없이 조밀한 인코더를 얻는다. 12개 벤치마크·DINOv3와 MetaCLIP-2 4개 모델에서 8개 backbone-budget 구성 중 7개에서 평가된 dense structured pruning 방법 중 최고 평균 정확도를 내고, 추가 파인튜닝 시 가장 강한 edge 모델을 넘어서며(88.1% vs 85.8%), 비압축 모델 대비 GPU 처리량이 1.3~2.0배다.

**코드**: 불명

**태그**: foundation-model, efficient-inference, pruning, ssl-backbone

# arXiv cs.CV Daily Digest — 2026-10-02 (arXiv 공개일)

- **전체 신규 논문 수**: 215편 (new 174 + cross-list 41)
- **선별 수**: 11편

## 오늘의 트렌드

비디오 생성·월드 모델과 VLA/로봇 정책이 가장 두꺼운 군집을 이루고, 3D Gaussian Splatting 계열 재구성, VLM 평가·추론 벤치마크, MLLM 시각 토큰 압축·가지치기가 그 뒤를 잇는다. 방법론으로는 동결 비전 파운데이션 모델을 보조 교사로 쓰는 표현 정렬(REPA 계열)이 픽셀 공간 생성 모델로 번지고, 학습 없이 추론 시점에만 개입하는 training-free·post-hoc 보정과 on-policy 자기증류가 여러 과제에서 반복된다.

---

### [Emergent Object Binding Has a Finite Spatial Horizon](https://arxiv.org/abs/2610.00006)

**한 줄 요약**: 사전학습 ViT 패치 임베딩에서 읽히는 '같은 객체' 신호가 패치 간 거리에 따라 지수적으로 감쇠하는 유한한 공간 범위를 가진다는 것을 보인 분석.

**핵심 기여**: 동결 패치 임베딩에서 두 패치가 같은 객체에 속하는지(IsSameObject)가 높은 정확도로 디코딩된다는 기존 관찰에 대해, 단일 정확도 수치가 신호의 구조를 가린다고 지적한다. 같은 객체의 두 패치가 결합으로 디코딩될 확률은 패치 간 거리에 따라 단조 감소하다 0이 아닌 바닥값에 수렴하며, 유한한 길이 척도를 갖는 지수 함수로 잘 기술된다. 이 감쇠는 객체 크기, 세 종류의 프로브, ADE20K·COCO, DINO·CLIP 백본에 걸쳐 일관되어 디코더가 아닌 표현의 속성으로 해석되며, 큰 객체에서 결합이 약해지고 같은 클래스의 서로 다른 객체를 다른 클래스보다 덜 분리하며 부분을 전체와 묶는 행동을 설명하고, 객체 크기를 통제하면 가림에는 영향받지 않는다. DINOv2와 DINOv3에서 horizon과 바닥값이 서로 다른 깊이에 조직된다는 관찰은 프로빙한 층 수가 적고 두 모델 간 교란이 있어 예비 결과로 보고한다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, correspondence, segmentation

---

### [SmoothOperator: Enhancing Representations for Fine-grained Open-set Recognition via Modulated Label Smoothing](https://arxiv.org/abs/2610.00851)

**한 줄 요약**: 샘플별 임베딩 '두드러짐(prominence)'에 따라 label smoothing 계수를 조절해 구면 표현학습 기반 fine-grained open-set recognition을 개선하는 플러그인.

**핵심 기여**: open-set recognition에서 구면 표현학습이 강한 성과를 내고 label smoothing이 핵심 요인으로 꼽히지만, 모든 샘플에 같은 계수를 쓴다는 점을 문제로 삼는다. 저자들은 OSR용 구면 표현학습 목적함수들이 라벨이 alignment 항에만 들어가는 공통 alignment–uniformity 구조를 가짐을 보이고, label smoothing을 샘플마다 같은 값으로 고정된 alignment 다이얼로 해석한다. SmoothOP는 각 샘플의 자기 클래스가 가장 강한 경쟁 클래스 대비 얼마나 뚜렷한지를 재는 prominence로 계수를 정해, 두드러진 샘플에 강한 smoothing을 주어 당김을 완화한다. SpHOR·SpHOR-Lite·ConOSR·SupCon 네 방법에 적은 학습 오버헤드로 통합되며, Semantic Shift Benchmark(CUB·FGVC-Aircraft·Stanford Cars)에서 데이터셋·semantic shift 정도·OSR 후처리기 전반에 걸쳐 AUROC·OSCR·closed-set 정확도가 최대 4.7% 향상됐다. 기본 목적함수의 smoothing을 재분배하는 방식이어서 smoothing을 거의 쓰지 않는 목적함수에서는 효과가 제한된다고 밝힌다.

**코드**: 불명

**태그**: fine-grained, metric-learning, image-embedding, open-set-recognition

---

### [Revisiting Cross-Reconstruction for Generalizable Deepfake Detection](https://arxiv.org/abs/2610.01544)

**한 줄 요약**: 생성기별 아티팩트 다양성을 정렬로 지우지 않고 보존하는 cross-reconstruction과 마스크 주파수 재구성으로 미지의 조작 기법에 일반화하는 이미지 위조 탐지 프레임워크.

**핵심 기여**: 기존 cross-reconstruction 기반 방법은 의미–아티팩트 분리를 위해 생성기 간 이질적 아티팩트를 정렬하고 재구성에서 아티팩트 표현을 제외해, 조작 아티팩트 고유의 다양성과 시각 단서를 놓칠 수 있다고 지적한다. 이 논문은 생성 과정마다 다른 아티팩트 변이를 제거할 도메인 변이가 아니라 상보적인 포렌식 단서로 보고, 명시적 정렬 대신 의미적으로 정렬된 cross-generator 재구성으로 다양한 아티팩트 특성을 보존한다. 아티팩트 표현을 재구성 과정에 포함시키고, 조작 관련 잔차를 강조하면서 의미 간섭을 줄이는 masked frequency-aware reconstruction을 도입했다. FF++(c23)로 학습해 Celeb-DF v1/v2·DFDC·DFDCP·DFD 교차 데이터셋 프레임 수준 AUC 평균 90.6%를 보고했고, VQGAN·StyleGAN·SiT·DiT 교차 생성기 설정에서도 개선을 보였다.

**코드**: 불명

**태그**: forgery-detection, frequency-domain, domain-generalization

---

### [GIFTBench: Diagnosing Generalization in Image Forgery Localization and Informing Model Design](https://arxiv.org/abs/2610.01778)

**한 줄 요약**: 조작 소스·의미 대상·편집 연산·구성 복잡도 네 축으로 11.5만 장을 구성해 이미지 위조 지역화의 일반화를 진단하고, 그 진단으로 설계한 탐지·지역화 모델 ForenScope를 함께 제시한 벤치마크.

**핵심 기여**: 기존 image forgery localization 벤치마크는 조작 조건이 제한적이거나 교차 데이터셋 평가에서 여러 요인이 뒤섞여, 집계 성능만으로는 일반화를 파악하기 어렵다는 문제의식에서 출발한다. GIFTBench는 픽셀 단위 주석을 갖춘 115,013장의 조작 이미지를 네 축으로 구성해 축별 전이 분석과 12개 외부 데이터셋 평가를 지원하며, 진단 결과 비대칭적인 교차 소스 전이, recall 위주의 실패, 의미·연산·구성 변화에 따른 이질적 성능 저하를 확인했다. 기존 IFL 데이터셋보다 넓은 학습 분포를 제공해, 대표 지역화 모델들을 GIFTBench로 학습하면 외부 데이터셋 전이 성능이 일관되게 올랐다. 진단을 반영한 ForenScope는 분류 적응 표현과 다중 깊이·다중 스케일 공간 특징, 학습된 층 융합, 선택적 coarse-scale 조건화를 결합해 이미지 수준 탐지를 유지하면서 교차 데이터셋 지역화를 개선했다. 데이터셋 쇼케이스 페이지가 공개돼 있다.

**코드**: 불명

**태그**: forgery-detection, dataset-benchmark, segmentation, domain-generalization

---

### [Robust Online Aero-Engine Blade Defect Detection via Dual-Alignment Test-Time Adaptation](https://arxiv.org/abs/2610.00067)

**한 줄 요약**: 특징 통계 정렬과 pseudo-box 정렬을 결합한 test-time adaptation으로 항공엔진 블레이드 결함 검출기를 온라인 도메인 변화에 적응시키는 프레임워크 ABDD.

**핵심 기여**: 항공엔진 블레이드 검사는 생산 라인·촬영 조건·블레이드 포즈·표면 배경에 따라 결함 외형이 달라지고, 결함이 희소해 pseudo-label 기반 적응이 잡음과 누락에 취약하다는 문제를 다룬다. ABDD는 전역 시각 스타일을 특징 통계 정렬로, 국소 결함 형태를 pseudo-box 정렬로 함께 적응시키는 Dual-Alignment Strategy를 쓰고, 분류 신뢰도·분류 엔트로피·위치 엔트로피로 pseudo-box를 거르는 Uncertainty-aware Box Filtering으로 오류 누적을 줄이며, 경량 Sparse Dilated Mona 모듈로 소스 도메인 망각을 제한하는 parameter-efficient delta tuning을 수행한다. RT-DETR + Swin-T 통일 구조에서 CD-AeBD·HD-AeBD의 여러 도메인 변화 시나리오로 7개 TTA 기법과 비교해, CD-AeBD Subset II 평균 mAP@50이 68.4%에서 79.9%로 올랐고 HD-AeBD에서 mAP@50:95 +6.4%를 보고했으며 산업 검사 플랫폼에서도 검증했다. 적응 시 순전파 2회·역전파 1회가 필요해 고실시간 환경에 제약이 있고, 큰 도메인 격차에서 누락된 결함(false negative)은 복구하지 못한다고 밝힌다.

**코드**: 불명

**태그**: defect-detection, industrial-inspection, object-detection, test-time-adaptation, peft

---

### [Dataset Identity, Not Novelty: The Source of an Inflated OOD Detection Gain](https://arxiv.org/abs/2610.01096)

**한 줄 요약**: OOD 데이터로 맞춘 post-hoc OOD 검출기가 보고하는 성능 이득의 대부분이 novelty가 아니라 '데이터셋 정체성' 학습에서 온다는 것을 데이터셋 전체 hold-out으로 측정한 분석.

**핵심 기여**: post-hoc OOD 검출기는 벤치마크가 제공하는 OOD 데이터로 상수·특징 방향·조합기를 맞추고 같은 OOD 데이터셋의 held-out 샘플로 검증하는데, 이 검증은 개별 이미지 암기는 막지만 어느 데이터셋인지를 알아보는 방향이 학습된 경우를 걸러내지 못한다고 지적한다. 저자들은 샘플이 아니라 OOD 데이터셋 전체를 hold-out해 그 차이를 '인플레이션'으로 정의하고, ImageNet·CIFAR-100 백본의 여러 조합기에서 측정해 보고된 이득의 대부분이 데이터셋 정체성에서 온다는 것을 보였다. 적합 크기를 바꿔도 살아남는 이득이 변하지 않아 통상의 과적합과 다르며, 입력이 클래스 정체성을 노출하는지에 따라 인플레이션 비중이 갈린다는 것을 두 통제 실험으로 확인했다. 폐형식(closed form)으로 적합 행(fitting rows)에서 인플레이션을 계산할 수 있어 hold-out 프로토콜 없이도 어떤 적합이 부풀려질지 판별할 수 있으며, 지정 검증 데이터셋에서 고르는 단일 상수만 hold-out 아래에서도 이득이 유지된다고 보고한다.

**코드**: 불명

**태그**: calibration, open-set-recognition, evaluation-protocol, dataset-benchmark

---

### [Localisation-Aware Uncertainty for Pretrained Object Detection](https://arxiv.org/abs/2610.01409)

**한 줄 요약**: 동결 검출기 위에 사후(post-hoc) evidential 메타모델을 얹어 bounding box 단위로 위치추정 불확실성을 추정하는 경량 기법 GRACE.

**핵심 기여**: 분포 변화나 적대적 공격 아래에서 검출기의 불확실성 추정이 필요하지만, 기존 방법은 재학습·구조 수정·반복 추론을 요구해 적용이 어렵거나 비용이 크다는 문제에서 출발한다. GRACE는 검출기를 그대로 둔 채 위치추정 관련 특징을 자동으로 식별하고, saliency 유도 변형으로 점점 어려워지는 커리큘럼을 구성하며, 위치 오차·변형 수준·예측 불안정성을 결합한 검출 단위 타깃으로 evidential 메타모델을 학습해 각 예측 박스의 불확실성을 산출한다. 검출기의 원래 위치 출력은 보존되며, 적대적 공격과 강도 전반에서 TP-FP AUROC가 가장 강한 비교 대상 대비 일부 경우 22% 개선되고 in-distribution 검출 성능은 유지됐다.

**코드**: 불명

**태그**: calibration, object-detection, uncertainty-estimation, robustness

---

### [Towards Automatic Video Annotation with ASH: Zero-Shot Open-Vocabulary Multi-Object Tracking and Segmentation](https://arxiv.org/abs/2610.01022)

**한 줄 요약**: SAM3에 N개 텍스트 프롬프트를 가상 배치로 한 번에 처리하는 Generalized Presence Token과 임의 길이 영상을 겹치는 청크로 잇는 ASH를 붙여, 학습 없이 open-vocabulary 다중 객체 추적·분할 주석을 만드는 파이프라인.

**핵심 기여**: 메모리 어텐션 기반 video instance segmentation은 zero-shot 추적이 강하지만 메모리 요구량 때문에 짧은 클립에 묶이고, 단일 프롬프트 추론 설계 때문에 다중 카테고리 open-vocabulary 추적 비용이 과도하다는 문제를 다룬다. Generalized Presence Token은 학습된 구성 요소를 바꾸지 않고 SAM3 추론 파이프라인을 재구성해 N개 텍스트 프롬프트를 동시에 처리하며 이미지 인코딩 비용을 O(N)에서 O(1)로 낮추고, ASH는 겹치는 시간 청크와 IoU 기반 청크 간 ID 매칭으로 데이터셋별 학습 없이 임의 길이 시퀀스로 확장한다. SAM3-ASH는 완전 zero-shot으로 MOTS20에서 HOTA 68.1, YouTube-VIS 2019/2021/2022 AP 49.8/48.5/47.1, LV-VIS AP 47.3을 기록했고 피크 GPU 메모리는 25 GB 미만이다. 가림 아래 유사 객체를 SAM2 메모리 뱅크가 구분하지 못하는 점, 겹침 구간 내내 사라진 객체가 재등장 시 새 ID를 받는 점, 어휘가 커지면 처리량이 크게 떨어지는 점(1,196 클래스 LV-VIS에서 0.017 FPS)을 한계로 밝힌다.

**코드**: 불명

**태그**: segmentation, open-vocab-detection, video, training-free, foundation-model

---

### [Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation](https://arxiv.org/abs/2610.02148)

**한 줄 요약**: 텍스트 임베딩 백본의 텍스트 쪽 가중치를 전혀 바꾸지 않고, 백본 자신의 캡션 임베딩을 교사로 삼아 이미지·비디오·문서·음성·오디오를 같은 cosine 공간에 묶은 0.9B 임베딩 모델.

**핵심 기여**: 텍스트 임베딩 모델을 새 모달리티로 확장하면 텍스트 검색 품질이 떨어지기 쉽고, 기존 omni-modal 임베더는 수십억 파라미터로 이를 보상한다는 문제의식에서 출발한다. 각 미디어 샘플에 조밀한 cascaded caption을 짝지어 동결 백본이 그 캡션을 임베딩한 값을 교사 타깃으로 쓰므로 별도 교사 모델이 필요 없고 교사·학생이 바이트 단위로 동일한 기하를 공유하며, 모달리티 인코더 위의 경량 프로젝터와 단계적 LoRA 어댑터만 학습한다. 학습은 Matryoshka SigLIP contrastive loss와 인코더가 좋아질수록 negative가 날카로워지는 온라인 hard-negative 마이너를 결합한다. 0.9B 모델은 MTEB-v2 BEIR-8 49.57 nDCG@10의 텍스트 검색 성능을 그대로 유지하면서 5개 모달리티를 추가했고 비교한 공개 omni 임베더보다 2.7~9.5배 작으며, 네이티브 vision-language 백본으로 바꾼 2.3B 변형은 전체 모달리티 평균에서 gemini-embedding-2를 근소하게 앞섰다. 모델·코드·데이터·평가 하네스가 프로젝트 페이지에 공개돼 있고, 캡션 코퍼스는 CC BY-SA 4.0으로 배포된다.

**코드**: 공개([Omni-Embed-Mini](https://github.com/k-m-irfan/Omni-Embed-Mini))

**태그**: image-retrieval, image-embedding, metric-learning, distillation, vlm

---

### [Two Routes to the Middle: Placement Search and Brain Readouts Converge on Where Continual Learners Should Specialize](https://arxiv.org/abs/2610.01590)

**한 줄 요약**: 사전학습 ViT에 task별 어댑터를 네 블록에만 둘 때 중간 깊이가 최적임을 배치 탐색으로 보이고, fMRI 인코딩 모델 readout으로 탐색 없이 같은 위치를 고르는 continual learning 기법 LS-B.

**핵심 기여**: 모든 블록에 task별 어댑터를 두는 continual learner는 저장량이 task 수에 비례해 늘고, 몇 블록에만 두면 어디에 둘지가 문제가 된다. 연속 4블록 배치를 모두 학습하면 최종 정확도가 중간 깊이에서 정점을 찍는 역U 형태로 최대 3.5%p 차이가 나는 반면, 가중치 스펙트럼이나 활성 통계 같은 값싼 기준은 가장 깊은 블록을 고른다. LS-B는 인간 시각 영역 12개의 동결 fMRI 인코딩 모델로 초기 task들을 관찰해, 안정 구조 대비 readout 변동이 큰 블록에 task별 용량을 한 번에 배정하며, 라벨·역전파 없이 런타임 0.6% 미만을 추가한다. ViT-B/16 세 백본에서 안정적인 백본별 배정을 냈고, AugReg·iBOT에서는 탐색이 찾은 중간 깊이 영역과 겹쳤으며, 동일 저장·관찰 예산에서 최상층·최하층 4블록 구성을 앞섰다. Split ImageNet-R에서는 full-BiLoRA 어댑터 저장량의 60%로 최종 정확도 1.5%p 이내를 유지했다.

**코드**: 불명

**태그**: continual-learning, peft, foundation-model

---

### [Domain generalization and synthetic data in object detection: the enabler, the probe, and the gap](https://arxiv.org/abs/2610.00030)

**한 줄 요약**: 객체 검출 관점에서 domain generalization 연구를 정리하고, 합성 데이터를 DG의 enabler·probe·synthetic-to-real gap 세 관점으로 검토한 리뷰.

**핵심 기여**: 검출기는 날씨·운용 환경·객체 외형 변화 같은 분포 변화에서 성능이 떨어지지만, 위치추정과 다중 스케일 표현이라는 추가 난제가 있음에도 검출에 특화된 DG 연구는 드물다는 점을 짚는다. 합성 데이터를 (1) 다양화·정렬 전략으로 분포 변화 강건성을 높이는 enabler, (2) 통제 실험으로 실패 모드를 찾는 probe, (3) 합성 이미지로 학습한 모델이 실제 데이터에 배포될 때 생기는 synthetic-to-real gap 자체라는 세 관점에서 검토한다. 이를 통해 현재 검출용 DG 접근의 한계를 정리하고, 분포 변화 아래 위치추정과 분류를 모두 명시적으로 다루는 representation-aware 방법이 필요하다고 주장한다.

**코드**: 불명

**태그**: sim2real, object-detection, domain-generalization, survey

---

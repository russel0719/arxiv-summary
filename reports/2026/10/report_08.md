# arXiv cs.CV Daily Digest — 2026-10-07 (arXiv 공개일)

- **전체 신규 논문 수**: 164편 (new 130 + cross-list 34)
- **선별 수**: 11편

## 오늘의 트렌드

월드 모델과 비디오 생성·편집, 3D Gaussian Splatting 재구성이 가장 두꺼운 군집을 이루고 의료영상 분할·진단, MLLM 토큰 축소·효율화가 그 뒤를 잇는다. 평가에서는 공간 중첩 누출이나 프레임 위상·보기 순서 같은 프로토콜 요인이 점수를 좌우한다는 감사 연구가 반복된다. 방법론으로는 동결 foundation model 위에 어댑터·프롬프트를 얇게 얹는 적응, 물리 기반 합성으로 사람 주석 없이 도메인을 옮기는 자기지도 적응, 추론 시점에만 보정하는 training-free·test-time 기법이 흐름을 이룬다.

---

### [Unlocking Fine-Grained Perception in CLIP via Structurally-Aware Latent Masked Modeling](https://arxiv.org/abs/2610.07689)

**한 줄 요약**: 이미지-텍스트 쌍 없이 공간 상관·활성 강도를 정렬하고 잠재 마스크 모델링을 더해 CLIP의 세밀 지각을 끌어올리는 비지도 임베딩 정렬 프레임워크 SALM.

**핵심 기여**: CLIP 같은 VLM은 전역 의미 정렬에는 강하지만 세밀한 지각 능력이 부족해 dense prediction 과제를 막고 MLLM의 시각 성능에 병목이 된다는 문제의식에서 출발한다. vision-centric 모델의 기하 사전지식을 주입하는 기존 전략은 국소 공간 구조와 전역 의미를 함께 깊이 정렬하지 못하고 원래의 image-text 공간을 왜곡할 수 있다고 지적하며, SALM은 명시적·암묵적 두 경로를 묶는다. 먼저 dual-matrix alignment로 샘플 내부의 공간 상관과 활성 강도를 명시적으로 교정해 국소 기하 사전지식을 넣고, 그 위에서 latent mask modeling으로 타깃 모델의 결손 의미 세부를 복원하게 해 세밀 구조를 전역 의미 공간에 암묵적으로 모은다. CLIP의 얕은 층 특징이 이미 강한 공간 관측 능력을 가진다는 관찰을 근거로 외부 모델 없이 자기 증류만 쓰는 SALM-Self로 확장했고, dense prediction 성능과 zero-shot 정확도가 함께 올랐으며 MLLM의 세밀 이해도 개선됐다.

**코드**: 불명 (초록에는 프로젝트 페이지 [salm_project_page](https://qzfm.github.io/salm_project_page/)만 명시)

**태그**: ssl-backbone, image-embedding, fine-grained, distillation, foundation-model

---

### [REViT-v2: Hierarchical Windowed Roto-reflection Equivariant ViT for Equivariant Feature Extraction](https://arxiv.org/abs/2610.07585)

**한 줄 요약**: 윈도우 그룹 합성곱 셀프어텐션과 계층적 특징 구조로 ImageNet 규모까지 확장한 회전·반사 등변 ViT.

**핵심 기여**: 회전·반사(roto-reflection) 군에 등변인 vision transformer를 윈도우 단위 group-convolutional self-attention과 계층적 특징 아키텍처 위에 구성한다. 기존 군 등변 모델이 소규모에 머물던 것과 달리 수백만 파라미터 규모의 등변 ViT로, 그리고 ImageNet처럼 실사용 크기 이미지를 담은 대규모 데이터셋으로 확장 가능함을 보인다. 초록에는 정량 비교 수치가 제시되지 않았고, 코드와 사전학습 가중치 공개만 명시돼 있다.

**코드**: 공개([revit](https://github.com/kc-ml2/revit) · 사전학습 가중치 포함)

**태그**: vision-backbone, equivariance, image-embedding, foundation-model

---

### [Anchor Divergence for Semantic Geometry in Contrastive Learning](https://arxiv.org/abs/2610.06919)

**한 줄 요약**: 고정된 대조학습 표현 위에서 anchor 분포를 지정하는 것만으로 맥락별 Bregman 기하를 정의해 코사인 유사도를 대체하는 Anchor Divergence.

**핵심 기여**: 유사도는 보통 코사인으로 재지만 이는 고정된 단일 기하를 강제하는 반면, 의미적 유사성은 맥락 의존적이라는 문제의식에서 출발한다 — 두 이미지는 같은 물체를 담아서, 시각적 스타일을 공유해서, 또는 같은 임상 소견과 관련돼서 유사할 수 있다. 논문은 대조학습 표현이 하나의 기하가 아니라 특정 의미 구조에 특화될 수 있는 기하의 족(family)을 자연스럽게 품고 있음을 보이고, 대조학습·지수족·정보기하를 엮어 "anchor"에 대한 확률분포와 표현공간 위의 Bregman 기하 사이에 대응을 세운다. 이 대응 아래에서는 anchor 분포를 모델링하는 것이 곧 기하 자체를 모델링하는 일이 되며, 검색 실험에서 맥락별 의미 유사도를 고정 표현 위에 효율적으로 지정할 수 있음을 보였다.

**코드**: 불명

**태그**: metric-learning, image-embedding, image-retrieval, contrastive-learning

---

### [WildMatch: Weakly Supervised Image Matcher Adaptation for Wildlife Re-Identification](https://arxiv.org/abs/2610.07384)

**한 줄 요약**: 대응 주석 없이 신원 레이블만으로 사전학습 keypoint matcher를 대조 미세조정해 야생동물 개체 재식별에 맞춘 전이 가능한 대응 사전지식을 얻는 WildMatch.

**핵심 기여**: 카메라 트랩 기반 개체 재식별은 질의 이미지로 기준 집합에서 같은 개체를 찾는 instance retrieval 문제이며 털·피부 무늬 같은 변별적 국소 패턴을 봐야 한다. 기존 접근은 전역 임베딩을 분류 문제로 학습해 개체당 많은 레이블을 요구하면서 국소 증거를 거의 버리거나, 도메인 무관 기성 매처를 그대로 쓰는데, 야생동물 데이터셋은 작고 대응 수준 주석이 없어 매처 적응이 어렵다. 논문은 사전학습 매처로 정보량이 큰 이미지 쌍을 채굴하고 신원 일치 여부에서 약한 양성·음성 지도를 끌어내, 같은 개체 쌍의 대응은 강화하고 다른 개체 쌍의 대응은 억제하도록 매칭 네트워크를 대조 미세조정한다. 공개 야생동물 재식별 데이터셋 전반에서 기성 매처와 local–global fusion 기반 최신 기법보다 정확도가 높았고, 개체를 held-out 하는 open-world 프로토콜에서는 학습 신원을 외우는 대신 전이 가능한 대응 사전지식을 학습함을 보였다.

**코드**: 불명

**태그**: feature-matching, correspondence, re-identification, image-retrieval, fine-grained

---

### [Identity-Conditioned Score Fusion for Open-Set Person Re-Identification](https://arxiv.org/abs/2610.07366)

**한 줄 요약**: 갤러리 신원마다 얼굴·걸음걸이·체형 점수의 융합 가중치를 학습 없이 맞추는 open-set 재식별용 신원 조건부 점수 융합.

**핵심 기여**: 사람 재식별은 얼굴·걸음걸이·체형 같은 상보적 단서를 결합하는데, 적응적 융합은 대개 질의 품질만 겨냥하는 반면 모델의 강점은 신원에 따라서도 달라진다는 문제의식에서 출발한다. 제안 방법은 신원 내부 일관성과 교차 신원 impostor를 대비해 신원별 프로파일을 추출하고, 이를 질의 조건부 적응과 파라미터 없는 규칙으로 결합해 별도 학습 없이 가중치를 정한다. 점수 캘리브레이션을 보존하면서 참·거짓 매치 사이 간격을 넓히며, 옷을 갈아입는 재식별 벤치마크 3개에서 통계 기반·순위 기반·학습 기반 베이스라인을 일관되게 앞서고 false non-identification rate를 최대 8.8%p 절대 감소시켰다.

**코드**: 불명

**태그**: re-identification, calibration, metric-learning, training-free

---

### [Localize Any Object in X-Ray Security Scans without Human Annotation](https://arxiv.org/abs/2610.07326)

**한 줄 요약**: 흡수도 영역 물리 기반 합성과 가림 통제 커리큘럼으로 SAM2를 X-ray 보안검색 영상에 사람 주석 없이 적응시키는 자기지도 프레임워크 LAO-X.

**핵심 기여**: X-ray 보안 스캔은 일상 RGB 이미지와 달리 고유한 색 패턴, 모호한 경계, 부피 중첩에서 오는 합성 구조를 가져 웹 스케일 RGB로 학습한 dense perception foundation model의 zero-shot 전이를 막고, 주석 데이터는 전문가 레이블링이 필요해 희소하다는 문제의식에서 출발한다. LAO-X는 saliency 유도 X-ray 객체 채굴 모듈로 다양한 인스턴스를 분리한 뒤 흡수도(absorbance) 영역에서 물리 기반으로 이미지–주석 쌍을 합성하고, 객체 수와 겹침 정도를 점진적으로 올리는 가림 통제 커리큘럼으로 SAM2 로컬라이저를 미세조정한다. X-ray 벤치마크 6개 실험에서 범주 무관(category-agnostic) 로컬라이제이션이 SAM2 및 X-ray 전용 베이스라인 대비 심하게 혼잡한 장면에서 mAP 2~23% 향상됐으며, 사람이 단 레이블은 전혀 쓰지 않았다.

**코드**: 불명

**태그**: segmentation, object-detection, sim2real, industrial-inspection, foundation-model

---

### [Anchor and Adapt: Asymmetric Prompt Adaptation for Few-Shot Industrial Anomaly Detection](https://arxiv.org/abs/2610.07016)

**한 줄 요약**: 보조 데이터에서 배운 정상·이상 anchor를 고정한 채 소수 타깃 정상 샘플로 정상 분기만 비대칭 적응시키는 2단계 프롬프트 학습.

**핵심 기여**: few-shot 산업 이상탐지에서는 소수의 정상 타깃 이미지만 주어져 결함에 대한 직접 지도가 없고, 그래서 이상 프롬프트를 이 샘플만으로 학습하기 어렵다. 일부 비전-언어 기법은 수동으로 작성한 설명으로 이상 의미를 공급하지만 제품별 작업량이 들고 효과가 프롬프트 선택에 좌우된다. Anchor and Adapt는 이상 의미 획득과 타깃 정상 외형 적응을 분리해, 1단계에서 주석된 보조 데이터로 전이 가능한 정상·이상 anchor를 학습하고 2단계에서는 anchor를 고정한 채 소수 타깃 정상 샘플로 추가 정상 분기만 적응시킨다. 상속된 정상 분기와 적응된 정상 분기가 타깃 정상성을 함께 기술하고 text-anchor 정규화가 일반 정상 prior와의 일관성 및 이상 anchor와의 분리를 유도하며, 합성 이상 생성 없이 MVTec-AD와 VisA 사이 교차 데이터셋 1·2·4-shot 설정에서 경쟁력 있는 탐지·국소화 성능을 보였다.

**코드**: 불명

**태그**: anomaly-detection, industrial-inspection, defect-detection, peft, vlm

---

### [Forensic Reserve: Eliciting Latent Knowledge for Image Forgery Detection](https://arxiv.org/abs/2610.08639)

**한 줄 요약**: 사전학습 비전 모델 내부의 희소한 원천 민감 성분을 'forensic reserve'로 식별하고 그 부분공간에만 어댑터를 꽂아 잠재된 위조 탐지 능력을 끌어내는 RGE.

**핵심 기여**: 기존 위조 탐지는 과제별 지도로 비전 foundation model 표현을 적응시킬 뿐 모델 내부에 이미 있는 포렌식 지식을 충분히 활용하지 않는다는 문제의식에서 출발한다. Reserve-Guided Elicitation(RGE)은 먼저 Forensic Lens로 층과 토큰 그룹에 걸친 활성을 독립 성분으로 분해하고 실제 이미지와 생성 이미지 사이 반응 차이로 전역 선별해 reserve 위치와 방향을 찾은 뒤, 선택된 방향을 은닉 상태 공간으로 되돌려 고정 reserve 부분공간을 만들고 해당 위치에만 Forensic Reserve Adapter를 삽입한다. 백본 파라미터·사전 적합된 참조 분류기·부분공간 기저를 모두 고정한 채 어댑터 계수 맵만 학습해 입력 의존 잔차 업데이트를 해당 부분공간 안으로 제한한다. 레이블 이미지 500장과 백본 대비 0.2% 미만의 학습 파라미터만으로 탐지 벤치마크 3개에서 타깃 벤치마크 적응 없이 경쟁력 있는 성능을 냈고, 자기지도·비전-언어 사전학습을 아우르는 인코더 8종에서 동결 탐지기 대비 일관되게 개선됐다.

**코드**: 불명

**태그**: forgery-detection, peft, foundation-model, ssl-backbone

---

### [Can We Model the Artifacts Explicitly? Disentangle Artifacts via Pairwise Edit Relations for Image Manipulation Localization](https://arxiv.org/abs/2610.07916)

**한 줄 요약**: 조작 흔적을 잠재변수로 두고 편집 쌍 관계에서 특징 분리로 artifact를 명시 모델링하는 2단계 조작 영역 국소화 패러다임 PAL.

**핵심 기여**: Image Manipulation Localization(IML)은 보통 이미지 $x$에서 최적 마스크 $y$를 추정하는 완전지도 과제로 세워지는데, 논문은 artifact $z$를 잠재변수로 보아 $P(y|x)=\int P(y|z)P(z|x)dz$로 재해석하고 현 IML 모델의 부족함을 artifact를 암묵적으로만 모델링하는 전략 탓으로 지목한다. $z$에 직접 레이블이 없으므로 특징 분리(disentanglement)를 명시 모델링의 해법으로 택하고, 편집 관계를 통해 $P(z|x)$와 $P(y|z)$를 각각 추정하는 Pairwise Artifacts Learning(PAL)과 Standard Localization(SL) 2단계 학습 패러다임을 제안한다. 편집 관계 기반 학습을 뒷받침하기 위해 원천을 기준으로 편집 그룹을 묶어 쌍을 구성할 수 있게 한 EditGroup-45K를 함께 구축했으며, PAL이 다양한 IML 아키텍처에서 일관된 개선을 주고 실제로 특징 분리를 통해 artifact를 명시적으로 포착함을 실증 분석으로 확인했다.

**코드**: 공개([PAL](https://github.com/venus-guangjian/PAL) · 데이터셋 포함)

**태그**: forgery-detection, segmentation, dataset-benchmark

---

### [Learning to Curate What You Generate for Generalizable Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2610.07008)

**한 줄 요약**: base 세션조차 클래스가 적은 상황을 겨냥해 동결 diffusion이 만든 합성 후보를 전이 가능한 선별 정책으로 큐레이션해 쓰는 few-shot class-incremental learning.

**핵심 기여**: FSCIL은 보통 충분히 큰 base 세션을 전제하지만 base와 증분 데이터가 모두 희소하면 초기 표현이 약해지고 의미 drift와 불안정한 경계가 생기며, 논문은 base 세션 자체에 클래스가 몇 개뿐인 이 설정을 Generalizable FSCIL(G-FSCIL)로 정식화한다. 합성 데이터가 지도 부족을 덜어줄 수 있으나 생성 샘플을 그냥 섞으면 의미 잡음이 들어오고 신·구 경계 충돌이 커지므로, 동결 latent diffusion으로 클래스별 합성 후보 풀을 만들되 첫 관측 시 class inversion을 수행하고 그 조건 임베딩을 재사용해 필요할 때 생성한다. 의미 일관성과 시각 다양성을 함께 보는 큐레이션 전략을 base 세션에서 전이 가능한 선별 정책으로 증류해 이후에는 추가 최적화 없이 재사용하고, 합성 기반 프로토타입 초기화와 양방향 경계 캘리브레이션으로 신·구 충돌을 완화한다. 실험에서 기존 FSCIL 베이스라인을 일관되게 앞서며 망각이 줄고 신·구 클래스 균형이 개선됐다.

**코드**: 공개([G-FSCIL](https://github.com/NiHaoWoJiaoYYC/G-FSCIL))

**태그**: continual-learning, generative, calibration

---

### [Catastrophic Forgetting in Sequential Thermal Anti-UAV Detection: The Role of Scale-Conditioned Gradient Imbalance](https://arxiv.org/abs/2610.08315)

**한 줄 요약**: 열적외선 UAV 검출기를 세 벤치마크에 순차 학습시켜 망각을 계량하고 원인을 가중치 drift가 아닌 크기 조건부 gradient 불균형으로 지목한 continual learning 연구.

**핵심 기여**: 운용 데이터셋이 계속 바뀌는 counter-UAV 시스템에서 순차 미세조정이 파국적 망각을 일으키지만 이 영역에서는 아직 충분히 특성화되지 않았다는 문제의식에서, 움직임 채널을 끈 단일 열적외선 스트림으로 돌린 YOLOMG를 Anti-UAV-RGBT → Anti-UAV410 → CST Anti-UAV 순으로 학습하며 안정성-가소성 트레이드오프를 측정한다. 단순 미세조정은 1단계 상한 대비 Forgetting Measure -0.605(약 90% 능력 손실, 그중 -0.572가 3단계에서 발생)를 기록한 반면 동결 교사로부터의 지식증류는 세 seed에서 -0.033±0.004(95% 유지)에 머물렀고, 계층별 분석에서는 gradient 업데이트 가중치의 단계 간 코사인 유사도가 0.987로 높은데도 큰 표적 검출이 첫 epoch 안에 0에 가깝게 무너져 크기 조건부 gradient 불균형이 후보 기제로 제시된다. UAV 크기 4계층에 균형 잡은 300개 exemplar 버퍼(Scale-Stratified Herding)는 망각을 -0.605에서 -0.311로 줄였고 큰 표적 검출을 0이 아닌 상태로 유지했으나, ablation은 이득이 herding보다 크기 계층화에서 온다고 돌린다(무작위 계층 replay -0.221). 논문은 2단계에 KD 미적용 대조군이 없어 KD의 인과 효과가 아니라 유지율만 확인한 결과이고 replay 결과는 단일 seed라 예비적이라고 밝힌다.

**코드**: 불명

**태그**: continual-learning, object-detection, distillation

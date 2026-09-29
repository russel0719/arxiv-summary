# arXiv cs.CV Daily Digest — 2026-09-29 (arXiv 공개일)

- **전체 신규 논문 수**: 564편 (new 460 + cross-list 104)
- **선별 수**: 12편

## 오늘의 트렌드

가장 두꺼운 군집은 world model과 vision-language-action으로, 주행·조작 환경의 미래 예측과 정책 학습이 이어진다. 다음은 vision-language model 효율화로 visual token pruning·압축, 4비트 양자화, on-policy self-distillation이 반복된다. diffusion·flow matching의 few-step 가속과 비디오 생성, 의료영상 분석도 큰 축이다. 표현학습 쪽은 JEPA 계열의 마스킹 설계와 차원 붕괴 분석이, 포렌식 쪽은 AI 생성 이미지 판별과 워터마크 제거·추적이 각각 묶인다.

---

### [$\lambda$-JEPA Spectral Anti-Collapse Regularization for Self-Supervised Learning](https://arxiv.org/abs/2609.35288)

**한 줄 요약**: 목적함수가 projector 뒤에 걸리는 탓에 백본 표현이 차원 붕괴를 피하지 못한다는 지적에서 출발해, 층 간 가중치 스케일 균형($\lambda$-balance)을 유도하는 스펙트럼 정규화를 백본에 직접 거는 JEPA 변형.

**핵심 기여**: joint-embedding self-supervised learning은 붕괴 방지 장치를 projection head 뒤에 적용하지만 downstream은 projector 앞의 백본 표현을 쓰며, 이 불일치 때문에 백본이 낮은 유효 랭크를 유지한 채 전이 성능이 제한될 수 있다고 지적한다. 층 간 가중치 행렬의 상대적 스케일을 나타내는 $\lambda$-balance 분석을 근거로 스펙트럼 anti-collapse 정규화항 SACReg를 제안하고, 2층 선형 네트워크에서 $\lambda$-balance가 붕괴를 막는다는 점과 이 정규화가 $\lambda$-balance를 유도한다는 점을 보인 뒤 비선형·실제 구조(ImageNet100)에서도 표현 랭크가 올라감을 확인한다. 이를 JEPA에 적용한 $\lambda$-JEPA는 ImageNet-1k 분류와 8개 downstream 데이터셋 평균 linear probe에서 LeJEPA·VISReg를 앞서고, 비디오에서는 Something-Something-v2·Kinetics-400에서 LeVJEPA·V-JEPA 2를 앞선다.

**코드**: 공개([lambda-jepa](https://github.com/berkerdemirel/lambda-jepa))

**태그**: ssl-backbone, image-embedding, foundation-model, video

---

### [JEPA Learns What the Mask Leaves Unrecoverable](https://arxiv.org/abs/2609.32481)

**한 줄 요약**: JEPA에서 block mask는 되고 흩뿌린 mask는 안 되는 경험칙을, 마스크를 선형 측정으로 보고 "마스크가 복원 불가능하게 남기는 coarse-scale 내용량"으로 설명한 뒤 151회 사전학습으로 검증한 분석.

**핵심 기여**: 마스크를 선형 측정으로 보면 compactly supported wavelet 기저에서 은닉 영역 안에 서포트가 들어가는 원자는 측정의 영공간에 떨어져 데이터에 흔적을 남기지 않으며, JEPA 손실은 문맥이 타깃을 맞추기만 요구하므로 저수준 prior로 복원 가능한 타깃은 지름길을 허용하고 moving-average 타깃 인코더가 이를 자기일관적으로 만든다고 주장한다. 학습 전에 "복원 불가능한 내용량"을 점수화해 예측을 세우고 151회 사전학습으로 검증한 결과, ImageNet-100에서 면적과 연결성을 block과 맞춘 strip mask는 복원 가능해 linear top-1 40.3%(random 40.8%)에 그친 반면 block은 64.3%였고, 같은 기하 계열 안에서도 복원 불가능 내용을 적게 남기는 배치가 많이 남기는 배치보다 6.5점 낮았다. 타깃 인코더를 고정하면 random과 block의 격차가 19점에서 1.5점으로 닫혀, 마스크 기하가 인코더가 스스로 만들어 내는 타깃을 통해 작동함을 보인다. UCF101에서는 마스킹 비율에 따라 내용 조건과 도달 범위 조건 중 무엇이 병목인지가 바뀐다고 보고한다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, video

---

### [W2Rep: Learning Visual Representations by Watching the World Change](https://arxiv.org/abs/2609.35464)

**한 줄 요약**: 비디오의 변화를 감독 신호로 쓰되 단일 이미지에서 뽑는 특징 자체를 갱신하도록 설계해, 이미지 단위와 비디오 단위 모두에서 쓸 수 있는 인코더를 학습하는 masked feature prediction 프레임워크.

**핵심 기여**: 이미지 self-supervision은 한 순간의 공간 구조를 배우고 비디오 방법은 여러 프레임을 함께 인코딩한 표현 안에서 시간 관계를 배우는데, 장면의 변화를 보는 것이 비디오 표현 능력을 잃지 않으면서 단일 이미지에서 얻는 특징을 개선할 수 있는지 묻는다. W2Rep은 독립적으로 인코딩된 source 이미지가 같은 시점 또는 다른 시점의 예측에 참여하는 masked feature prediction 구조로, 예측기는 보이는 비디오 문맥·질의 위치·source와 target 사이의 부호 있는 시간 간격을 조건으로 받는다. 이미지 경로는 시간이 지나도 유효한 특징을 배우고 비디오 경로는 source 이미지에 없는 증거를 모으게 되며, 모델 규모와 downstream 과제 전반에서 frozen·fine-tuned 인식 성능이 개선되고 joint video encoding이 프레임별 집계보다 추가 이득을 준다. 통제 실험에서 이 이득이 source 이미지 특징을 직접 갱신하는 것과 비디오 문맥·시간 변위를 함께 쓰는 것에 의존함을 보인다.

**코드**: 공개([W2Rep](https://wenooi.github.io/W2Rep))

**태그**: ssl-backbone, image-embedding, video, foundation-model

---

### [Copy the Same, Distill the Difference: Initializing Linear Vision Transformers](https://arxiv.org/abs/2609.35745)

**한 줄 요약**: Softmax ViT의 사전학습 가중치를 linear ViT로 옮길 때 attention 가중치 복사는 무용하고 MLP 복사 + attention 증류가 효과적임을 보인 전이 초기화 연구.

**핵심 기여**: linear attention을 쓰는 ViT는 선형 복잡도로 토큰 라우팅을 하지만 처음부터 사전학습해야 하고 Softmax 버전보다 낮은 성능에 머무는데, 주류 foundation ViT가 Softmax attention 기반이라는 점에서 그 가중치를 재사용할 수 있는지 묻는다. Attention Transfer 계열이 시사하는 것과 달리 Softmax→linear 전이에서는 attention 가중치가 연산자 특이적이라 복사해도 거의 도움이 되지 않고 때로 random 초기화보다 나빴으며, 대신 손실 설계를 갖춘 증류로 attention의 토큰 라우팅 거동을 복원하면 격차가 줄어든다고 보고한다. 반면 학습된 표현을 담는 MLP 가중치는 연산자 무관해 단순 복사만으로 사전학습 가중치 이득의 대부분을 옮길 수 있고, 복사한 MLP와 증류한 attention을 함께 쓰면 linear ViT가 Softmax 대응물을 따라잡거나 넘어선다. 이 결과는 여러 linear ViT 변형·모델 크기·데이터셋에서 일관되게 관찰됐다.

**코드**: 불명

**태그**: ssl-backbone, distillation, efficient-inference, foundation-model

---

### [The Devil is in the Spectrum Bias: Spectrum-Balanced Feature Matching for Robust Representation Distillation](https://arxiv.org/abs/2609.34106)

**한 줄 요약**: L2 기반 feature matching 증류가 교사 표현의 지배적 스펙트럼 방향만 재현하고 저분산 방향을 방치한다는 진단 위에, 덜 최적화된 방향을 적응적으로 강조하는 목적함수 SpecMatch.

**핵심 기여**: 라벨 없이 교사 표현을 작은 학생 모델로 옮기는 feature matching 증류에서, 관행적인 L2 거리 목적함수가 교사 표현의 지배적 스펙트럼 방향 재구성에 본질적으로 편향돼 과제 관련 정보가 자주 담기는 저분산 방향을 덜 최적화한다고 보인다. SpecMatch는 지배적 방향의 상대적 중요도를 보존하면서 덜 최적화된 스펙트럼 방향을 적응적으로 강조하는 단순한 목적함수로, 구현이 간단하고 계산 부담이 거의 없다. 이미지 분류·anomaly detection·의료영상 분석·도메인 일반화를 포함한 downstream 적응에서 교사-학생 및 학습 설정 조합 42개 중 40개에서 기존 feature matching을 앞섰고, 모든 설정에서 원래 학생 모델보다 나았다. 단백질 이해 과제 6종에서도 개선을 보고해 비전 밖으로도 일반화됨을 주장한다.

**코드**: 불명

**태그**: distillation, foundation-model, image-embedding, anomaly-detection

---

### [VisionHOPE: Visual Backbones as Self-Modifying Learning Systems](https://arxiv.org/abs/2609.33325)

**한 줄 요약**: 무엇을 기억할지와 어떻게 학습할지가 한 이미지 안에서 함께 진화하는 self-modifying 구조로 시각 백본을 재구성하고, 발산을 막는 step-size 제어와 비확장성 증명을 붙인 범용 백본.

**핵심 기여**: CNN에서 ViT, SSM, Test-Time Training 층으로 오면서 시각 연산은 입력마다 점점 더 적응적이 됐지만 적응 규칙 자체는 여전히 학습된 백본이 규정한다는 문제의식에서, Nested Learning의 self-referential 구성을 가져와 내용 저장·key/value 생성·학습률과 보존율 관리를 맡는 다섯 개의 결합된 메모리가 스캔을 따라 함께 진화하는 VisionHOPE를 제안한다. 제약 없는 self-referential 갱신을 시각 백본에 그대로 적용하면 불안정해지므로, self-referential 주입에 soft cap을 걸고 보존 메모리 전이에 spectral clamp를 거는 stability-matched step-size 제어를 유도하고 각 스캔에서 메모리 동역학이 비확장적임을 증명한다. 2차원 특징 맵에 대해서는 네 방향 스캔에서 청크를 이미지의 행·열에 맞추는 방식으로 Nested Learning의 청크 정식화를 적응시킨다. ImageNet-1K·COCO·ADE20K에서 경쟁력 있는 결과를 보고한다.

**코드**: 공개([VisionHOPE](https://github.com/PSRben/VisionHOPE))

**태그**: ssl-backbone, foundation-model, object-detection, segmentation

---

### [When Does Geometric View Synthesis Help Wine Label Retrieval? A Public One-Shot Benchmark Across Self-Supervised and Vision-Language Backbones](https://arxiv.org/abs/2609.33359)

**한 줄 요약**: 클래스당 등록 사진 한 장뿐인 1,000클래스 와인 라벨 검색 벤치마크에서, 기하학적 view synthesis 증강의 효과가 백본 종류에 따라 크게 갈린다는 것을 실측한 연구.

**핵심 기여**: 라벨 사진 한 장을 기하학적 view synthesis로 학습셋으로 늘리는 방식이 사전학습 인코더와 함께 쓸 때도 값어치가 있는지를, WineSensed 기반 공개 벤치마크(1,000클래스, 클래스당 등록 사진 1장, 실제 질의 4,295장)에서 검증한다. DINO ViT-S/16 레시피에서는 기하 뷰가 top-1을 34.1%에서 62.6~63.7%로 올려 2D 증강 이득의 약 3배였지만, frozen SigLIP 2-B는 증강 없이 이미 94.7%에 도달했고 그 frozen 특징 위의 linear head는 SAM으로 국소화한 두 파이프라인에서 1.2~1.3%p만 얻었다. LoRA와 검증셋으로 고른 full fine-tuning은 신뢰구간 안에서 뚜렷한 이득이 없었고 고정 예산 full fine-tuning은 9~24점을 잃었으며, SAM 국소화는 소스의 99%에서 여섯 뷰를 모두 공급한 반면 에지 기반 전처리는 43%에 그쳤다. 잔여 오류 50건 감사에서 21건이 질의-등록 외형 불일치였으나 저자들은 비가역 오류율을 확정하지는 않았다고 밝힌다.

**코드**: 불명

**태그**: image-retrieval, fine-grained, ssl-backbone, peft, dataset-benchmark

---

### [Concepts Complement Dense Semantics: Learning Compact Sparse Spaces for Text-Image Retrieval](https://arxiv.org/abs/2609.32671)

**한 줄 요약**: dense 임베딩이 놓치는 세밀한 시각-텍스트 정보를 보완하기 위해, 언어모델 토큰 공간 대신 코퍼스에서 캐낸 개념 공간 위에 sparse 분기를 얹은 cross-modal 검색 프레임워크 GRASP.

**핵심 기여**: vision-language 사전학습 모델이 이미지와 텍스트를 공유 dense 임베딩 공간에 넣어 cross-modal 검색을 끌어올렸지만, dense 표현은 전반적 의미 유사도는 잘 담아도 정밀한 매칭에 필요한 세밀한 정보를 흐린다는 문제를 제기한다. 최근 방법들은 lexical 증거로 dense 매칭을 보완하는 학습형 sparse 분기를 도입하지만 중복이 많은 언어모델 토큰 공간에 의존하고 sparse 차원에 명시적 근거가 없다는 점을 지적하고, GRASP는 코퍼스에서 시각-텍스트 개념을 캐낸 뒤 각 이미지·텍스트에 관련된 개념을 예측하는 경량 sparse head를 학습해 해석 가능한 개념 수준 증거를 만든다. 실험에서 최신 dense-sparse 기준선들보다 검색 정확도가 높으면서 sparse 공간은 더 작고 근거가 붙은 형태를 유지한다고 보고한다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, metric-learning, vlm

---

### [Re:Cognize -- Open-Set Comic Character Re-Identification](https://arxiv.org/abs/2609.34032)

**한 줄 요약**: 등장인물 목록을 미리 받지 않고 페이지를 읽어 나가며 갤러리를 스스로 키우는 open-set 순차 re-ID 평가 프로토콜과, 아무것도 학습하지 않는 수용 판정 규칙 ReCast.

**핵심 기여**: 만화 인물 재식별을 폐쇄형 검색이 아니라 페이지가 읽기 순서대로 흘러오고 이름 붙기 전의 새 얼굴이 등장하며 갤러리를 스스로 모아 가는 open-set 순차 과제로 규정하고, 하나의 질의 스트림 위에 네 개 프로토콜을 둔 Re:Cognize 벤치마크를 만든다. 실측에서 인식 자체는 거의 해결돼 인물당 참조 이미지 한 장이 미리 구축한 갤러리만큼 잘 순위를 매기는 반면, 무엇을 믿을지 판단하는 쪽이 병목이어서 모델이 자기 매칭 결과를 갤러리에 추가하면 오히려 나빠지고 같은 성장을 정답 라벨로 하면 top-1이 20점 이상 오른다고 보고한다. 병목은 시각이 아니라 수용 판정이며, "추가가 이득인 조건은 그 추가가 넘겨받는 질의들에서 기존 갤러리보다 더 자주 맞을 때"라는 비교 하나로 결정된다고 주장하고, 새 코퍼스의 절반에서 잰 이 규칙이 나머지 절반을 옳게 판정함을 보인다. ReCast는 인물당 이동평균 하나로 된 갤러리를 페이지 자체가 보증하는 crop에서만 키워 완전 라벨 대비 1/3~2/3을 회복하며, 저자들은 주장 범위를 이미 만난 인물의 정체성 유지로 한정하고 새 인물의 출현은 진단 지표로만 측정한다고 밝힌다.

**코드**: 불명

**태그**: re-identification, image-retrieval, calibration, fine-grained, dataset-benchmark

---

### [Mixed-Prior Decision Risk for Open-Set Recognition](https://arxiv.org/abs/2609.35043)

**한 줄 요약**: open-set 인식의 불확실도 점수를 KL 요약이 아니라 실제로 내린 결정에 딸린 오류 사건(오수용·오식별·오기각)의 위험으로 직접 계산하는 MPRisk.

**핵심 기여**: open-set recognition에서는 오수용·오기각·오식별 세 오류가 공존하므로 선택적 인식용 불확실도 점수는 시스템이 내린 결정의 위험 순으로 질의를 정렬해야 하는데, HolUE 같은 베이지안 갤러리 인지 모델이 쓰는 KL 발산 요약은 결정 위험에 대해 일반적으로 단조가 아니며 검증셋에서 튜닝한 KL 성분의 선형 융합이 여러 벤치마크에서 음의 filtering quality를 낸다고 보인다. MPRisk는 같은 베이지안 사후분포를 유지하되 선택된 결정에 대응하는 오류 사건의 위험(오수용·오식별·오기각)과 기각에 대한 non-specificity 페널티를 직접 점수화하며, 미지 신원을 연속 성분으로 모델링해 이를 가능하게 하고 검증셋에서 튜닝한 음이 아닌 가중치 넷만으로 순위를 매겨 비선형 지도 캘리브레이터를 없앤다. 이미지·오디오·텍스트 9개 벤치마크에서 이미지와 오디오는 모든 동작점에서, 텍스트는 대부분의 동작점에서 최고 또는 동률의 Prediction Rejection Ratio를 얻었고, 5개 벤치마크에서 HolUE 대비 부트스트랩으로 확인된 개선(최대 +0.19 PRR)을 비슷하거나 더 낮은 실행시간에 달성했다.

**코드**: 불명

**태그**: calibration, re-identification, image-retrieval, open-set-recognition

---

### [Focus and Supplement: Dual-Enhanced Vision Transformer for Multi-Class Anomaly Classification](https://arxiv.org/abs/2609.33353)

**한 줄 요약**: 산업 이상 분류에서 잡음 섞인 불완전한 이상 표현과 미지의 이상 클래스 수 문제를 겨냥해, 이상 맵 기반 soft-focus 어텐션과 보조 [A-CLS] 토큰, 상관 기반 클래스 수 추정을 결합한 MACO.

**핵심 기여**: 산업 비전의 multi-class anomaly classification은 이상 표현이 잡음 섞이고 불완전한 데다 이상 클래스 수를 모른다는 점에서 어렵다고 보고, MACO는 이상 맵으로 비정상 영역에 집중하고 배경 잡음을 억제하는 soft-focus 어텐션과, [CLS] 토큰을 보완해 여러 이상 하위 영역에 함께 주목하는 보조 분류 토큰([A-CLS])으로 더 전체적이고 변별력 있는 특징을 만든다. 클래스 수 추정에는 라벨된 클래스 간 평균 상관을 계산해 그 분리도 단서를 미라벨 집합으로 옮기는 Correlation-based Number Estimation을 제안한다. MVTec AD와 MTD에서 클래스 수를 아는 조건일 때 ARI를 각각 6.5%, 16.3% 개선했고, 클래스 수를 모르는 더 어려운 조건에서는 MTD에서 NMI 11.2% 향상, MVTec AD에서 기존 클래스 수 추정 전략 대비 UPS 24.1% 우위를 보고한다.

**코드**: 공개 예정([MACO](https://github.com/HUST-SLOW/MACO))

**태그**: anomaly-detection, industrial-inspection, defect-detection, fine-grained

---

### [DBCF: Dual-Branch Complementary Fusion of Foundation Models for Generalized Deepfake Detection](https://arxiv.org/abs/2609.34720)

**한 줄 요약**: CLIP의 전역 의미 단서와 DINOv3의 국소 구조 단서가 서로 보완적이라는 관찰 위에, 두 동결 foundation model을 계층적 다중 입도 구조로 융합한 얼굴 위조 판별기.

**핵심 기여**: 소규모 위조 판별 모델은 위조 단서를 담는 능력이 제한돼 도메인과 미지 조작 방식을 넘어 일반화하기 어렵고, 단일 foundation model에 기대는 것만으로도 충분하지 않다는 점에서 출발한다 — CLIP은 견고한 전역 의미 단서를 주지만 세밀한 국소 얼굴 특징을 담지 못하고, DINO는 국소 구조를 잘 잡지만 전역 의미 맥락이 약하다. DBCF는 CLIP 기반 Global Context Branch와 DINOv3 기반 Fine-grained Cue Branch를 두는 계층적 다중 입도 구조에, 동결된 두 백본에서 상보적 특징을 적응적으로 뽑아 합치는 parameter-efficient 특징 융합 모듈을 설계한다. 여러 벤치마크에서 특히 cross-dataset·cross-manipulation 설정의 이득을 보고한다.

**코드**: 불명

**태그**: forgery-detection, foundation-model, ssl-backbone, peft

---

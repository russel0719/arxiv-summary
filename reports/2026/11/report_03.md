# arXiv cs.CV Daily Digest — 2026-11-02 (arXiv 공개일)

- **전체 신규 논문 수**: 102편 (new 76 + cross-list 26)
- **선별 수**: 7편

## 오늘의 트렌드

병리·MRI·CT 분할과 진단을 다루는 의료 영상이 가장 두꺼운 군집이고, 4D 장면 생성·3D 재구성·Gaussian 기반 위치 추정이 뒤를 잇는다. MLLM의 공간·영상 추론 벤치마크와 embodied agent·로봇 제어도 한 덩어리를 이룬다. 방법론으로는 생성·복원·깊이 추정 전반에 퍼진 flow matching과, 모델 풀의 상관된 실패·데이터 재사용·회귀 시험처럼 평가 절차 자체를 감사(audit)하는 흐름이 두드러진다.

---

### [A Patch is More Than a Token](https://arxiv.org/abs/2610.41814)

**한 줄 요약**: frozen DINOv3의 patch 하나를 여러 관측 조건에서 얻은 특징 묶음(Representation State Family)으로 넓히고 이를 저차원 Manifold로 정리해, 표현 재학습 없이 correspondence 등 patch 수준 과제의 성능을 높이는 표현 프레임워크(PMTT).

**핵심 기여**: ViT가 각 patch를 한 관측 조건에서 만든 canonical token 하나로만 표현해, backbone이 가진 patch 정보가 표준 인터페이스로 다 드러나지 않는다는 문제의식이다. crop 범위·scale·종횡비·주변 문맥·8방향 상대 위치를 바꾼 Dense Orbital Views로 anchor마다 같은 patch의 상태 32개(Visible 16·Hidden 16)를 얻고, Visible 상태에서 center 평행 성분을 뺀 rank-8 SVD 인자로 center 주변의 단위 구(unit-ball) 형태 Manifold를 만들어 canonical Center·실제 상태 집합 Observed와 비교한다(frozen DINOv3 S/B/L/H+, 표현 후처리 학습 없음). 두 개의 4,096-anchor cohort에서 Manifold는 Hidden 변동의 70.8~79.6%를 설명해 Observed(55.0~72.3%)보다 높고, SPair-71k·DAVIS-2017·MegaDepth-1500·ScanNet-1500·NYUv2·ADE20K 6개 과제 × 4개 scale 중 23개 조건에서 Center를 앞서며, MegaDepth P@10은 S 기준 Center 20.83 → Observed 27.64 → Manifold 28.65이고 Center 대비 Manifold 이득은 S/B/L/H+에서 7.82/5.61/3.39/2.38 point로 scale이 커질수록 줄어든다. 한계로 DINOv3 한 계열에서만 확인했고, SPair(H+)·NYUv2에서는 Observed가 더 낫고 ScanNet(L·H+)에서는 Manifold가 이기지 못하는 등 이득이 과제에 따라 다르며, rank-8 선형 인자가 비선형 구조를 놓칠 수 있다고 밝힌다.

**코드**: 공개([zixiongwang-ai/PMTT](https://github.com/zixiongwang-ai/PMTT))

**태그**: ssl-backbone, correspondence, feature-matching, training-free

---

### [Hard Sample-Conditioned Decorrelated Attention for Robust Face Recognition](https://arxiv.org/abs/2610.41789)

**한 줄 요약**: negative class center와의 cosine 유사도가 높은 hard sample일수록 attention head 간 상관을 더 강하게 억제해, 구조 변경·추가 추론 비용 없이 ViT 얼굴 인식 성능을 높이는 정규화(ViT-HarDis).

**핵심 기여**: ViT의 multi-head attention은 명시적 정규화가 없으면 head들이 중복 패턴을 배우는데, 기존 상관 기반 penalty는 모든 샘플에 같은 세기로 걸려 정체성이 가장 헷갈리는 hard sample에 집중하지 못한다는 문제의식이다. KP-RPE ViT(112×112 입력, patch 8)와 AdaFace loss 위에, 샘플별 head×head attention cosine 유사도 행렬의 비대각 제곱 평균(DeCAtt 방식)을 penalty로 두고, 이를 최대 negative-center 유사도로 정한 hardness 가중치(오분류 샘플은 0, batch 평균으로 정규화, gradient 차단)로 곱해 마지막 25% block에만 건다. ViT-S(MS1MV3 1만 identity 부분집합)에서 IJB-C TAR@1e-5가 baseline 78.25·균일 disentanglement 78.51 대비 80.52, TinyFace Rank-1이 66.12 → 67.11이고, ViT-B를 WebFace4M으로 학습하면 IJB-B/IJB-C TAR@1e-4·TinyFace Rank-1이 95.84/97.24/75.97(재학습 KP-RPE 95.66/97.17/75.51), MS1MV3로 학습하면 96.14/97.34/73.52다. 전 층에 거는 설정이 가장 나빴고, 학습이 약 30% 느려지며(ViT-B·WebFace4M epoch당 39 → 51분) MS1MV3 IJB-C에서는 ViT-8R에 뒤지는 등 이득이 벤치마크마다 고르지 않다고 밝힌다.

**코드**: 공개([TaharChettaoui/Hard-Sample-Conditioned-Attention-for-FR](https://github.com/TaharChettaoui/Hard-Sample-Conditioned-Attention-for-FR))

**태그**: metric-learning, re-identification, image-embedding, face-recognition

---

### [FieldGuideRAG: Image-Grounded GraphRAG for Fine-Grained Recognition with Vision-Language Models](https://arxiv.org/abs/2610.40971)

**한 줄 요약**: 종(species) 노드마다 실제 사진 한 장을 저장한 knowledge graph에서, frozen VLM이 질의 이미지와 후보 노드 사진을 직접 대조(verification)해 닮은 종을 가려내는 training-free GraphRAG(FieldGuideRAG).

**핵심 기여**: 기존 multimodal GraphRAG는 엔티티를 텍스트로 묘사하는데, 텍스트로는 닮은 종을 가르는 시각적 세부가 거의 전달되지 않는다는 문제의식이다. SigLIP so400m 유사도 상위 8종·최상위 종의 형제 종·그래프 shortlist로 후보 풀을 만들고, frozen Qwen2.5-VL-7B/Qwen3-VL-8B에 질의·노드 사진·종 이름을 함께 주어 «같은 종인가» yes/no 첫 토큰 확률을 verification 점수로 쓰며, iNaturalist에서는 5° 격자 출현 빈도로 만든 지리 분포(range) edge 항을 log-linear로 더한다. 정확도는 SigLIP retriever 대비 CUB-200 53.2 → 69.0%(Qwen2.5)·Lepidoptera 16.3 → 32.6%(Qwen3) 등 최대 약 16 point 오르고, range edge가 iNaturalist에서 7~19 point(조류 39.4 → 58.5%)를 더하며, 노드 사진은 모든 그래프에서 종 이름만 쓸 때보다 낫지만 텍스트 설명의 이득은 작다. 최대 verification 점수로 그래프에 없는 종의 질의를 검출하는 AUROC는 CUB-200 0.819(retriever 0.663)·iNaturalist 0.60~0.69이고, fact edge로 답한 생태 질문 28,820개의 정답률은 최대 89.5%이며, range edge는 위치 정보가 없는 CUB-200에는 쓸 수 없고 역광 실루엣 같은 비전형 사진에서는 닮은 종을 고르는 실패 사례를 보고한다.

**코드**: 공개 예정(그래프·프롬프트·코드)

**태그**: fine-grained, vlm, training-free, image-retrieval

---

### [Beyond CLIP: Calibrated (Few-Shot) Defect Detection With System One Decision Models](https://arxiv.org/abs/2610.41199)

**한 줄 요약**: 클래스당 참조 이미지 2장만으로 structured decision model(Jev·Clef-Flash)을 제조 결함 판별에 쓰고, agent가 클래스 설명 문구를 다듬은 뒤 Platt scaling으로 결함 확률을 보정하는 few-shot 검사 프레임워크.

**핵심 기여**: CLIP 같은 ViT가 결함 판별 학습 데이터를 클래스당 50~100장으로 줄였지만, 수율이 높거나 소량 생산인 공정에서는 결함 이미지 50장도 모으기 어렵다는 문제의식이다. 이미지·질문·선택지별 텍스트 설명을 받아 선택지 확률을 내는 «System One» structured decision model Jev(원격 API)·Clef-Flash(로컬 GPU)에 추론 시 클래스당 k개 참조 이미지를 주는 k-shot 틀(재학습 없음), 개발셋으로 텍스트 설명을 반복 수정하는 agentic 개선, 별도 calibration 셋에 맞춘 Platt scaling(민감도 분석은 isotonic regression)을 묶고, 금속 팬 표면·3D 프린팅 과/미압출·직물 표면 교란·자동차 배관 스테이플 누락·모사 미세조직 이상의 5개 사례에서 정상/결함 이진 판별을 시험한다. k=2에서 test 정확도는 Jev 0.75~1.00·Clef-Flash 0.71~0.99로 같은 참조를 쓴 CLIP(0.67~0.84)보다 높고, 설명 문구 개선은 8개 모델-사례 조합 중 6개에서 정확도를 유의하게 올리며, Platt 보정은 15개 구성 중 13개에서 Brier score를 낮춘다(isotonic은 k=2의 10개 구성 중 8개에서 ECE가 더 낮지만 log loss가 크게 나빠지기도 한다). 한계로 비교적 안정된 촬영 조건의 이미지만 썼고, 이진 분류만 다뤄 다중 클래스·결함 위치 추정은 시험하지 않았으며, 모델이 사실상 black box이고 conformal prediction은 향후 과제라고 밝힌다.

**코드**: 공개(재현 코드와 모델 평가용 R 패키지 `decisions` — 코드 저장소 URL은 본문에 없음, [보조 사이트](https://fmegahed.github.io/decision-models-for-industrial-image-qc/) · no-code 웹 앱 [Hugging Face Space](https://huggingface.co/spaces/fmegahed/decisions))

**태그**: defect-detection, industrial-inspection, calibration, training-free, few-shot

---

### [ReuScope: Auditing Data Reuse and Evaluation Sensitivity in Capsule Vision 2024](https://arxiv.org/abs/2610.41835)

**한 줄 요약**: 파일 해시·perceptual hash·픽셀·embedding 유사도로 train/validation 간 데이터 재사용을 재고, 평가 집단과 학습 데이터를 각각 바꾸는 두 비교로 성능 민감도를 가르는 감사(audit) 프로토콜(ReuScope)과 캡슐 내시경 챌린지 Capsule Vision 2024 사례 연구.

**핵심 기여**: 공개 벤치마크에서 같은 원천 데이터가 분할 경계를 넘을 때, 관찰된 재사용과 그것이 점수에 주는 영향을 구분해 말할 절차가 없다는 문제의식이다. SHA-256 byte 일치, pHash/dHash(Hamming ≤6), 96×96 grayscale NCC(≥0.99)·SSIM, DINOv2-L/14 CLS cosine 유사도로 데이터 관계를 재고, 예측을 고정한 채 평가 집단을 바꾸는 비교와 평가를 고정한 채 학습 목록을 바꾸는 paired-seed 비교를 결합한다(모델은 DINOv2-L/14 + 마지막 4 block rank-8 LoRA, seed 10개). public train·validation 경계를 넘는 byte 동일 파일 그룹이 216개(파일명만 대조하면 45개 그룹을 놓친다)이고 Kvasir-Capsule 녹화 41개가 두 분할에 모두 나오며, Kvasir-Capsule 출처 학습 행을 빼면 public validation balanced accuracy가 82.5 → 61.2%로 떨어지지만 다른 출처 validation 행에서는 오히려 1.38 point 오른다. 이 하락은 누출로 부풀려진 양이 아니라 출처 제거에 대한 민감도이고, 유사도 선별 기준은 보정된 중복 검출기가 아니며, 벤치마크 하나·주 학습 파이프라인 하나에서만 확인했다는 점을 한계로 밝힌다.

**코드**: 공개([eunseobchoi/ReuScope](https://github.com/eunseobchoi/ReuScope) · 코드 MIT, 파생 데이터 CC BY 4.0)

**태그**: data-leakage, evaluation-protocol, dataset-benchmark

---

### [One Verdict Is Not Enough: Regression Testing Learned World Models and Their Test Harnesses](https://arxiv.org/abs/2610.41130)

**한 줄 요약**: 학습된 world model을 네 가지 고정 설정에서 같은 시험으로 돌려 시험마다 결과 등급(4종)을 매기고, 판(revision) 간 시험별 등급 전이로 회귀를 잡으며 test harness 자체도 판 관리하는 회귀 시험(regression testing) 프로토콜(TetraState).

**핵심 기여**: 모델 판·전처리·test harness가 배포마다 바뀌는데, 시험 하나가 설정에 따라 통과·실패가 갈리고 harness 결함이 크래시 없이 틀린 점수를 낼 수 있어 정확도나 negative flip 집계만으로는 이를 잡지 못한다는 문제의식이다. 물리적으로 가능/불가능한 영상 쌍 시험을 12·24·36·42 프레임 네 설정으로 돌려 맞힌 판정 수 4/3/1/0을 각각 CP·CDP·CDF·CF로 두고, 2:2는 판정 불가, 실행 실패는 따로 집계해 verdict rate와 함께 보고하며, 두 판을 같은 시험·설정에서 비교해 통과 설정 수가 줄면 회귀로 본다. IntPhys 2 Main 506개 시험에서 V-JEPA 2 harness의 padding 수정은 정확도를 48.3 → 48.5%로만 바꾸지만 시험 라벨 11개를 바꾸고, context 점수 계산 수정은 정확도를 2.6 point 올리면서 라벨 214개를 바꿔(회귀 114·개선 100) verdict rate를 5.5 point 낮추며, 회귀 중 43개는 최빈 판정이 그대로라 modal-verdict flip 검사로는 놓친다(Cosmos 3 Nano는 최빈 정확도 70.6%, CP 175·CDP 111·CDF 76·CF 43). 한계로 두 판 비교 모두 사후 사례 연구이고 회귀 관점도 관찰 뒤에 정했으며, 시스템 2개·합성 벤치마크 1개에서만 확인했고, 등급 전이는 변화의 원인을 알려 주지 않는다고 밝힌다.

**코드**: 공개([익명 재현 패키지](https://anonymous.4open.science/r/tetrastate-artifact-5C1E/) — 코드·실행 기록·CPU 재계산 스크립트)

**태그**: regression-testing, evaluation-protocol, video

---

### [AquaProbe: Efficient Adaptation of Frozen Vision Models for Underwater Images](https://arxiv.org/abs/2610.40900)

**한 줄 요약**: 깨끗한 이미지와 물리 기반으로 렌더링한 수중 이미지 쌍으로 frozen encoder의 층별 domain gap 발생 위치를 재고, 그 분포에 비례해 고정된 LoRA rank 예산을 층마다 나누는 수중 적응 기법(AquaProbe).

**핵심 기여**: 지상 이미지로 사전학습한 모델은 탁도·backscatter·파장별 감쇠 때문에 수중에서 신뢰도가 떨어지는데, 기존 적응법은 adapter를 깊이에 균등하게 펴거나 고정된 두 도메인 간 발산으로 층을 골라 수질·촬영 거리에 따라 gap 위치가 바뀌는 점을 놓친다는 문제의식이다. NYU Depth V2 RGB-D 1,449쌍을 직접 투과 + backscatter 2항 수중 형성 모델로 Jerlov 10개 수형 × 거리 배율 4개(40조건)로 렌더링하고, 층별 1−linear CKA 누적 gap의 증가분(새로 생긴 발산)을 재어 — 맑고 짧은 거리에서는 block 6 부근, 탁하고 긴 거리에서는 block 2 부근이 정점 — 그 증가분에 비례해 LoRA rank(총 96, 약 0.59M 파라미터·backbone의 0.68%)를 배분하고, 조건 군집 3개별 배분을 고르는 작은 router(block 2 특징 MLP)도 둔다. DINOv2 ViT-B/14로 SUIM 분할 mIoU는 uniform LoRA 68.2·AdaLoRA 68.9 대비 70.1(router 사용 시 70.6, full fine-tuning 71.8)이고, 보지 않은 촬영 거리 배율에 걸친 mIoU 적분 AUDRC는 uniform 59.8 → 63.4이며, SAM encoder와 TrashCan 데이터에서도 uniform 대비 1.5 mIoU 이득이 있다. 한계로 실내 RGB-D 장면과 단일 계수 형성 모델이라 실제 수질을 보정한 것이 아니라 근사이고, 의미 분할 과제와 backbone 2개·데이터셋 2개에서만 평가했으며, router 이득은 seed 분산이 없는 탐색적 결과라고 밝힌다.

**코드**: 공개 예정

**태그**: peft, sim2real, segmentation, foundation-model

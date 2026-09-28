# arXiv cs.CV Daily Digest — 2026-09-25 (arXiv 공개일)

- **전체 신규 논문 수**: 143편 (new 111 + cross-list 32)
- **선별 수**: 12편

## 오늘의 트렌드

3D Gaussian Splatting 복원·렌더링, world model과 vision-language-action으로 로봇 행동을 잇는 연구, 의료영상 진단·분할, 멀티모달 LLM의 환각·정렬 평가가 두꺼운 군집을 이룬다. 방법론으로는 동결된 foundation model의 특징을 재조합하거나 추론 시점 보정만으로 성능을 끌어올리는 training-free 설계, 여러 specialist를 하나의 백본으로 증류해 통합하는 설계, 잠재 공간에서 단계적으로 표현을 정련하는 구조가 반복된다.

---

### [ImCorr: Sub-pixel Semantic Correspondence via Implicit Feature Decoding](https://arxiv.org/abs/2609.29193)

**한 줄 요약**: patch grid에 묶인 특징 읽기가 semantic correspondence의 정밀도 한계를 만든다고 보고, 임의의 연속 좌표에서 질의 가능한 특징 필드로 바꿔 sub-pixel 대응을 얻는 방법.

**핵심 기여**: 최신 semantic correspondence 기법이 표준 임계에서는 잘 작동하지만 fine-grained 임계에서 성능이 급격히 정체한다는 문제에서 출발해, 그 원인이 백본 특징의 표현력이 아니라 격자에 묶인 readout이라고 주장한다. SPair-71k의 499,188개 keypoint 전수를 448×448·patch-14 설정에서 측정해 PCK@0.01 기준 ground-truth keypoint의 84.9%가 자기 위치를 대표하는 격자 특징을 아예 갖지 못한다는 양자화 상한을 정량화한다. ImCorr는 FiLM 조건화 디코더로 sub-pixel 위치 정보를 특징 필드에 심어, source 측은 정확한 keypoint 좌표에서 직접 질의하고 target 측은 백본 격자보다 조밀한 격자로 디코딩해 양자화 오차를 줄인다. SPair-71k와 AP-10K(동종·이종·과 단위)에서 PCK@0.01~0.05 구간이 개선됐고, SPair-71k PCK@0.01에서 기존 최고 대비 6.2%p 상승을 보고한다.

**코드**: 공개([ImCorr](https://github.com/YusungChoi/ImCorr))

**태그**: correspondence, feature-matching, fine-grained, foundation-model

---

### [IronViT: Toward Efficient Generalist Visual Representation Learning](https://arxiv.org/abs/2609.29252)

**한 줄 요약**: 여러 specialist teacher를 효율 아키텍처로 곧장 증류하면 표현이 망가진다는 관찰에서, 먼저 softmax attention 브리지로 능력을 통합한 뒤 hybrid softmax-linear encoder로 점진 전이하는 generalist 비전 인코더.

**핵심 기여**: generalist 비전 인코더는 의미·공간·언어 정렬·행동 관련 단서를 하나의 표현에 담아야 하지만 현재 강력한 백본이 쓰는 softmax attention이 고해상도에서 비용을 감당하기 어렵다는 문제를 다룬다. 여러 specialist를 효율적 구조에 직접 증류하면 student가 이질적 능력의 조정과 다른 token-mixing 구조로의 적응을 동시에 떠안아 표현 품질이 떨어진다는 것을 확인하고, "연산을 제약하기 전에 능력을 먼저 통합한다"는 원칙으로 IronViT를 설계한다. 상보적 specialist를 softmax attention capability bridge로 증류한 뒤 통합된 표현을 hybrid softmax-linear attention encoder로 점진 이전하며, 증류 코퍼스를 정보 밀도와 도메인 커버리지 기준으로 큐레이션하는 데이터 파이프라인을 함께 둔다. 인식·검색·dense prediction·멀티모달 이해·로봇 학습 전반에서 기존 specialist·generalist 인코더와 경쟁 가능하며, softmax bridge는 멀티모달 이해와 로봇 학습에서 평가 백본 중 최고 종합 성능을, hybrid encoder는 입력 해상도가 커질수록 커지는 효율 이점을 유지했다고 보고한다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, foundation-model, distillation, efficient-inference

---

### [Learning a Flow to Self-Supervised Representations](https://arxiv.org/abs/2609.29350)

**한 줄 요약**: 적대적 encoder-critic 최적화 없이 구면 조건부 속도 회귀로 기하 기준을 향한 흐름을 학습하는 비적대적 self-supervised 표현학습 framework.

**핵심 기여**: 명시적 기하 기준(reference)으로 self-supervised 표현을 구조화하는 기존 적대적 distribution matching 방식이 비싼 encoder-critic 최적화를 요구한다는 문제에서 출발한다. FBDM(Flow-Based Distribution Matching)은 구면 조건부 속도 회귀로 기준을 향한 기하를 학습하는 비적대적 framework로, ETF에서 착안한 기준을 써서 구성요소 수 K'가 보조 flow 차원 d*를 넘어서도 구조적 기하 분리를 유지한다. 한 이미지의 두 augmented view를 같은 타깃에 배정하되 기준 중심 하나가 받을 수 있는 이미지 수를 제한하고, 두 view의 표현을 당기는 명시적 alignment loss를 더한다. CIFAR부터 ImageNet까지의 벤치마크에서 DM에 거의 준하는 성능을 내면서 학습 비용을 맞춘 비교에서 1.48~1.83배 속도 향상을 GPU 메모리 증가 거의 없이 달성했고, 명시된 조건 아래 downstream 오분류율을 FBDM 사전학습 손실로 상계하는 이론적 설명을 함께 제시한다.

**코드**: 불명

**태그**: ssl-backbone, image-embedding, metric-learning

---

### [Can Frozen Hyperspherical Features Guide the Selection of Pseudo Masks?](https://arxiv.org/abs/2609.30080)

**한 줄 요약**: SAM 계열이 내놓는 여러 후보 마스크를 추가 모델이나 품질 헤드 없이, 동결된 DINOv2 특징의 초구를 마스크가 어떻게 가르는지만으로 채점·선별하는 방법.

**핵심 기여**: foundation segmenter가 레이블 없는 이미지에 대해 여러 그럴듯한 마스크를 내놓고 그중 틀린 것으로 학습한 student가 오류를 그대로 물려받는데, 후보를 고르려면 또 다른 대형 모델을 질의하거나 주석된 마스크로 품질 헤드를 학습해야 한다는 문제를 다룬다. SphereTrust는 정규화된 DINOv2 patch 특징이 초구 위에 놓이고 후보 마스크가 그 구를 둘로 가른다는 점에 착안해, 양쪽의 각도 대비, 전경 외관 모드의 커버리지, 이미지 프레임과의 접촉이라는 세 가지 속성으로 — 마스크가 실패하는 세 가지 흔한 방식에 각각 대응해 — 후보를 채점하고 동결 특징만으로 이미지당 0.55초에 순위를 매긴다. camouflaged·salient·dichotomous 분할과 저조도 위장을 포괄하는 8개 SAM·SAM3 후보 풀에서 6개 풀에 대해 최강 외부 baseline을 mean selected Dice 기준 1.7~9.3%p 앞섰고, 프롬프트 기반 위장 풀 2개에서는 후보 유래 DSS 적응 대비 0.1%p 이내이면서 치명적 오류율은 더 낮았다. 같은 초구를 학습에도 써서 상위 후보를 점수 사전확률과 함께 후보 집합으로 투입하고 prototype 재정렬과 cross-fitted 2라운드로 레이블을 완성하면, 3개 MLLM anchor 풀에서 고정 레이블 학습 대비 weighted F가 각각 4.5·2.3·5.5점 올랐다.

**코드**: 불명

**태그**: ssl-backbone, segmentation, image-embedding, training-free, foundation-model

---

### [Industrial Anomaly Detection via Defect-Grounded Reasoning in Visual Latent Space](https://arxiv.org/abs/2609.29457)

**한 줄 요약**: 국소 영역을 반복 재방문하거나 외부 도구를 붙이는 대신, 시각 잠재 공간에서 결함 관련 표현을 점진적으로 정련하는 산업 이상탐지용 latent reasoning framework.

**핵심 기여**: 산업 이상탐지가 탐지·국소화를 넘어 결함을 설명하고 추론하는 멀티모달 검사로 옮겨가는 가운데, MLLM 기반 기법들이 fine-grained 검사에서 두 가지 한계를 갖는다고 지적한다 — 시각 정련이 국소 영역의 반복 재방문이나 추가 도구를 요구하고, 그렇게 얻은 국소 결함 근거가 이후 추론 과정에서 안정적으로 보존되지 않는다는 점이다. Anomaly-LR은 입력에 대한 전역 이해를 먼저 형성한 뒤 시각 잠재 공간에서 이상 관련 표현을 점진적으로 정련하는 defect-grounded latent reasoning framework이다. 산업 이미지 4,523장에서 뽑은 22,228개 image-question 인스턴스에 전역 텍스트 추론 trace와 영역 단위 시각 주석을 붙인 latent reasoning용 IAD 지시 데이터셋 IAD-LR-22K를 함께 구축했고, 외부 레퍼런스나 도구 없이 여러 IAD 벤치마크에서 동급 규모 기법 중 최고 성능을 보고한다.

**코드**: 공개 예정([Anomaly-LR](https://github.com/Yen666/Anomaly-LR))

**태그**: anomaly-detection, industrial-inspection, defect-detection, vlm

---

### [EIB-Net: Entropy-Guided Information Bottleneck for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2609.29064)

**한 줄 요약**: 생성모델이 전역 의미를 우선하느라 국소 텍스처 충실도를 희생한다는 관찰에서, 엔트로피가 가장 낮은 patch를 골라 variational information bottleneck으로 압축 표현을 학습하는 AI 생성 이미지 판별기.

**핵심 기여**: 조작 기반 위조는 국소 아티팩트를 남기지만 diffusion 등 생성 기반 이미지는 그런 흔적이 없어 생성모델 전반에 일반화되는 탐지가 어렵다는 문제를 다룬다. 생성모델이 전역 의미를 우선시하면서 국소 텍스처 충실도를 희생하므로 저텍스처 영역이 합성 여부의 핵심 지표가 된다고 보고, Image Entropy(IE) 지표로 가장 정보량이 큰(엔트로피가 가장 낮은) patch를 자동 선택한 뒤 Variational Information Bottleneck으로 압축·일반화 가능한 특징을 학습하는 EIB-Net을 제안한다. DIFF·DiffusionForensics·GenImage 벤치마크에서 학습 데이터의 2%만 쓰고도 85.7% 정확도로 전체 이미지 baseline을 15%p 이상 앞섰고, GenImage에서 생성기 교차 일반화 평균 83.5%를 유지했다. 엔트로피 기반 patch 선택(EGPL) 자체는 CNN과 Transformer 등 다양한 백본에서 일관된 향상을 준다고 보고한다.

**코드**: 불명

**태그**: forgery-detection, image-embedding, print-forensics

---

### [Domain Recentering and Confidence-Weighted Prior Calibration for Vision-Language Models](https://arxiv.org/abs/2609.29358)

**한 줄 요약**: 레이블 없는 타깃 이미지 집합만으로 CLIP 임베딩의 도메인 편향을 posterior 가중 평균으로 빼고 잔여 클래스 선호를 log-prior 보정으로 제거하는 training-free 적응 기법.

**핵심 기여**: CLIP 같은 vision-language 모델이 zero-shot 분류에 강하지만 분포 이동 아래에서 시각 임베딩이 고정된 텍스트 임베딩으로부터 표류한다는 문제를 다룬다. Training-free 보정은 prompt learning의 샘플별 최적화를 피할 수 있지만, 기존 feature calibration은 각 이미지에 하드 클러스터 하나의 편향을 통째로 적용한다는 한계가 있다. DRC는 레이블 없는 타깃 이미지 집합에서 Gaussian mixture를 한 번 적합해 각 임베딩에서 posterior 가중 평균 성분 평균을 빼고(domain recentering), 신뢰도 가중 예측으로 사전확률을 추정해 log-prior 보정으로 잔여 클래스 선호를 제거한다. 비교 기법 중 cross-domain 데이터셋 평균 정확도가 가장 높았고, ViT-B/16과 ResNet-50에서 zero-shot CLIP 대비 각각 4.13점·5.07점 상승했으며 ImageNet 분포 이동에서도 이득이 유지됐다.

**코드**: 불명

**태그**: calibration, training-free, foundation-model, image-embedding

---

### [ReCalMatch: Reliability-Calibrated Semantic Guidance for Semi-Supervised Fine-Grained Recognition](https://arxiv.org/abs/2609.29678)

**한 줄 요약**: 시각적으로는 확신하지만 의미적으로 어긋난 pseudo-label을 시각-의미 일치도로 잡아내 가중치를 낮추는 준지도 fine-grained 인식 framework.

**핵심 기여**: 준지도 fine-grained 인식은 시각적으로 유사한 범주가 높은 확신의 오답을 자주 만들고 consistency regularization이 그 오류를 학습 내내 강화하기 때문에 과확신 pseudo-label 오류에 특히 취약하다는 문제에서 출발한다. 기존 SSL 기법은 최대 확률·적응 임계·엔트로피처럼 시각 분류기 자신에게서만 신뢰도를 추정해, 예측된 클래스가 시각 표현과 의미적으로 양립하는지에는 눈이 멀어 있다고 지적한다. ReCalMatch는 클래스명과 도메인별 의미 측면으로 클래스 조건부 semantic prototype을 만들고, 각 레이블 없는 임베딩과 그 pseudo-label prototype 사이의 visual-semantic agreement 점수를 재서 예측 확신·엔트로피와 합쳐 하나의 신뢰도 가중치로 결합한다 — 시각적으로 확신하지만 의미적으로 불일치하는 pseudo-label은 여기서 가중치가 낮아진다. semantic consistency 항과 semantic margin 정규화가 적은 레이블 아래 prototype 분리도를 더 날카롭게 하며, CUB-200-2011·Stanford Dogs·NABirds·iNaturalist18에서 강한 SSL baseline을 일관되게 개선하고 pseudo-label 잡음이 가장 심한 저레이블 구간에서 이득이 가장 컸다.

**코드**: 불명

**태그**: fine-grained, calibration, metric-learning, image-embedding

---

### [AgriCountDINO: Parameter-Efficient Exemplar-Guided Counting and Localization in Agriculture](https://arxiv.org/abs/2609.29460)

**한 줄 요약**: 동결된 DINOv3 다중스케일 특징을 exemplar 박스의 외관·크기로 조건화해 점 단위 위치까지 내놓는, 학습 파라미터 8.4M의 exemplar 기반 계수·국소화 framework.

**핵심 기여**: 식물과 기관의 계수·국소화는 표현형 분석과 수확량 추정에 필요하지만 대상의 외관·스케일·밀도가 종과 촬영 조건에 따라 크게 달라진다는 문제를 다룬다. exemplar 박스는 범주별 재학습 없이 대상을 지정할 수 있고 점 예측은 계수에 기여한 개별 인스턴스를 식별해 준다는 점에 기대어, AgriCountDINO는 동결된 DINOv3 다중스케일 특징을 exemplar의 외관과 크기로 조건화한 뒤 점진적으로 대상 점으로 디코딩한다. 초기 매칭이 놓친 대상까지 감독을 확장하는 missed-object recovery와 exemplar 스케일에 맞춰 중복 예측을 거르는 exemplar-adaptive point NMS를 둔다. 학습 파라미터 8.4M(TasselNetV4의 약 1/10)으로 TPC-268 벤치마크 three-shot MAE 11.92를 기록해 계수 오차를 9.7% 줄이면서 개별 위치까지 제공하고, TPC-268로만 학습한 상태에서 FSC-147의 미학습 일반 객체 범주에 대해 zero-shot MAE 14.25로 비교 대상 최고 zero-shot 기법을 타깃 도메인 학습·미세조정 없이 6.0% 앞섰다.

**코드**: 불명

**태그**: peft, object-detection, foundation-model, fine-grained

---

### [MEVL-STP: Multi-Encoder and Vision Language Model for Arbitrarily Shaped Scene Text Spotting](https://arxiv.org/abs/2609.28857)

**한 줄 요약**: 동결된 여섯 개 비전 인코더의 상보적 특징을 융합해 임의 형태 텍스트의 polygon 마스크를 뽑고, 그 crop만 LoRA 미세조정한 VLM에 넘겨 읽는 2단계 scene text spotting 파이프라인.

**핵심 기여**: 곡선 간판이나 조밀한 다방향 문자처럼 임의 형태의 텍스트에서 검출과 인식이 강하게 결합된 구조는 국소화 오류를 인식 실패로 그대로 전파한다는 문제를 다룬다. 검출 단계에서 CLIP·DINOv2·SigLIP·EVA-CLIP·SAM·ConvNeXt 여섯 개 동결 인코더가 의미·공간·텍스처 스펙트럼을 아우르는 상보적 특징을 뽑고, 학습 가능한 계층적 FPN과 channel attention으로 융합한 뒤 deep-supervision Progressive Scale Expansion 네트워크로 디코딩해 인스턴스 단위 텍스트 마스크를 만든다. 인코더를 동결해 각자 학습한 특징 공간이 융합 중에도 직교성을 유지하게 함으로써 단일 백본 검출기에서 경계 정밀도를 떨어뜨리는 특징 동질화를 막는다는 것이 설계 근거다. 인식 단계는 polygon으로 마스킹한 crop을 LoRA로 미세조정한 Qwen3-VL-8B-Instruct에 넘긴다. 합성 사전학습 데이터 없이 CTW1500에서 검출 F-measure 91.99%, end-to-end H-mean 85.86%를 기록했고 Total-Text와 ICDAR 2015에서도 마찬가지로 합성 학습 데이터 없이 성능을 보고한다.

**코드**: 공개([MEVL-STP](https://github.com/doubleblind-afk/MEVL-STP))

**태그**: text-detection, foundation-model, peft, segmentation, vlm

---

### [Hyperbolic Multimodal Continual Learning: A Closest-Admissible Solution](https://arxiv.org/abs/2609.29329)

**한 줄 요약**: 하이퍼볼릭 멀티모달 모델의 지속학습에서 Lorentz 기하를 보존하는 것이 모든 모달리티를 하나의 공유 등거리변환으로 제한하는 것과 같음을 보이고, 그 허용 집합에 가장 가까운 파라미터 보정을 구하는 방법.

**핵심 기여**: 기존 지속학습 기법이 파라미터·재현 예제·유클리드 특징 부분공간을 보호하지만, 하이퍼볼릭 멀티모달 모델에 적용하면 모달리티 내 유사도·교차모달 대응·의미 계층을 함께 인코딩하는 Lorentz 기하를 명시적으로 보존하지 못해 과제 점수는 유지되면서도 기존에 학습한 관계가 왜곡될 수 있다는 문제를 다룬다. HMCL은 이전 멀티모달 기하의 보존이 모든 모달리티를 하나의 공유 하이퍼볼릭 등거리변환으로 제한하는 것과 같음을 보이고, 그로부터 유도되는 허용 가능한 1차 파라미터 변화 집합 안에서 후보 모달 갱신에 가장 잘 맞는 공유 회전을 남기는 joint closest-admissible(CA) 보정을 정식화한다 — 회전을 0으로 고정한 minimal-rotation(MR)이 그 특수 경우다. 분류·검색 16개 과제 스트림과 세 가지 하이퍼볼릭 백본에서 순차 미세조정과 네 가지 지속학습 baseline 대비 최종 성능과 backward transfer가 개선됐고 HMCL-CA가 모든 백본에서 최고 종합 점수를 냈으며, 표현 분석에서 반경·각도·교차모달·쌍거리 표류가 81.2~95.5% 줄었다.

**코드**: 불명

**태그**: continual-learning, image-retrieval, metric-learning, image-embedding

---

### [Not All Confusion Is Equal: A Source-Aware Uncertainty Diagnosis for Fine-Grained Aircraft Detection](https://arxiv.org/abs/2609.29959)

**한 줄 요약**: 혼동행렬이 보여주지 못하는 "왜 혼동하는가, 줄일 수 있는가"를 aleatoric/epistemic × 클래스 내/클래스 간의 2×2 분류로 분해해 각 사분면을 독립된 양으로 측정하는 진단 도구.

**핵심 기여**: fine-grained 검출기를 흔히 혼동행렬로 평가하지만 혼동행렬은 어디서 혼동하는지만 보여줄 뿐 왜 그런지, 그 혼동을 줄일 수 있는지는 말해 주지 않는다는 문제에서 출발한다. A²E²는 혼동의 원인을 {aleatoric, epistemic} × {클래스 내, 클래스 간}의 2×2 분류로 분해하고, 각 사분면을 입력 기하·출력 공간 불일치·bias 파라미터 posterior 중 한 곳에서 계산되는 고유한 양으로 측정해 두 epistemic 원인이 경험적 상관이 아니라 구성상 분리되도록 한다. fine-grained 항공기 검출에서 네 사분면은 각각 affinity(기하적 유사, 크기만으로는 환원 불가), heterogeneity(기하적으로 이질적인 하위 변종으로, 데이터 추가보다 재레이블링을 가리킴), contested(학습이 부족하지만 학습 가능한 경계로 개선 가능), collapsed(데이터가 굶주린 클래스로 환원 가능)라는 이름과 처방 판정을 갖는다. 환원 가능한 원인으로 혼동을 귀속시킨 뒤 표적 개입을 적용해 진단된 원인만 선택적으로 줄고 환원 불가능한 원인은 그대로임을 실험으로 검증한다. 논문은 이 데이터셋에서 일부 원인만 부분적으로 식별 가능하다는 점을 포함해 framework의 한계를 함께 밝힌다.

**코드**: 불명

**태그**: fine-grained, calibration, object-detection, dataset-benchmark

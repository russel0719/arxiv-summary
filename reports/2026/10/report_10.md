# arXiv cs.CV Daily Digest — 2026-10-09 (arXiv 공개일)

- **전체 신규 논문 수**: 207편 (new 169 + cross-list 38)
- **선별 수**: 12편

## 오늘의 트렌드

world model과 video generation 계열이 가장 두껍고, 스트리밍 생성·4D 일관성·few-step distillation 가속이 한 덩어리로 묶인다. 다음은 VLA·embodied agent 군집으로 자기개선 루프와 KV·메모리 재사용이 반복된다. 세 번째는 MLLM 평가 벤치마크 군집이며 공간추론·스트리밍 지각·환각 억제가 축을 이룬다. 그 밖에 3D Gaussian Splatting 재구성이 꾸준하고, DINOv2·CLIP 표현을 동결한 채 재활용해 검색·대응·위조 판별로 가져가는 흐름이 얇게 깔린다.

---

### [Region-Aware CLS Token Augmentation for Fine-Grained Image Retrieval](https://arxiv.org/abs/2610.10991)

**한 줄 요약**: DINOv2-reg의 [CLS]·register 토큰 각각에 대응하는 공간 패치 영역을 자동으로 찾아 ROI 토큰으로 묶고 ColBERT식 multi-vector 검색에 쓰는 방법.

**핵심 기여**: 이미지 전체 의미를 [CLS] 토큰 하나에 압축하면 fine-grained 검색에서 성능이 깎인다는 문제의식에서 출발한다. register 토큰이 객체·부분 단위 표현을 emergent하게 학습한다는 점을 이용해, 각 cue 토큰([CLS]와 네 개 register)마다 가장 가까운 "buddy" 패치 토큰을 찾고 그 주변 N×N 영역을 뽑아 국소 ROI 토큰 집합을 만든다. 외부 bounding box나 saliency 모듈 없이 의미 토큰과 공간 표현을 매칭하는 것만으로 관심 영역이 잡히며, 이 토큰들을 ColBERT에서 착안한 per-token 정렬 기반 multi-vector 검색에 넣어 전체 패치 임베딩을 보관하는 저장 비용을 피한다. 실험에서 register 토큰이 [CLS]를 보완하는 세부 정보를 담고 있고, 자동 pooling된 ROI 토큰이 fine-grained 변별을 더 높이며, 소수 토큰만 쓰는 multi-vector 검색이 DINOv2-reg single-vector 기준선을 넘으면서 대규모 검색에 쓸 만한 비용을 유지한다고 보고한다.

**코드**: 공개([Augmenting_CLS_with_ROI_tokens](https://github.com/IdhcbIan/Augmenting_CLS_with_ROI_tokens))

**태그**: image-retrieval, fine-grained, ssl-backbone, image-embedding

---

### [Beyond Resolution: Object-to-Image Ratio Mismatch in Instance Retrieval](https://arxiv.org/abs/2610.11489)

**한 줄 요약**: instance 검색이 쿼리와 갤러리의 객체 크기 차이에서 무너지는 주원인이 해상도 손실이 아니라 객체가 이미지에서 차지하는 비율(O2I) 불일치임을 통제 실험으로 분리한 분석과 대응책.

**핵심 기여**: 같은 객체가 쿼리와 갤러리에서 다른 크기로 찍히면 검색이 실패하는데, 그 원인이 해상도인지 구도인지 분리되지 않았다는 문제의식이다. Objaverse 객체 3,021개를 다섯 가지 카메라 거리에서 렌더한 통제 벤치마크에서, 사전학습 백본 12개 중 9개에 대해 거리 간 성능 저하의 80% 이상이 해상도가 아닌 O2I 불일치에 귀속되며, multi-scale 구조는 해상도 단독 효과를 한 자릿수로 줄이지만 O2I 취약성은 그대로임을 보인다. 실패는 비대칭적이어서 타이트한 쿼리로 넓은 갤러리를 찾는 쪽이 그 반대보다 안정적이다. 이 분석에 따라 쿼리 측 scale augmentation과 OWLv2 crop reranker를 적용해 미리 계산된 갤러리 인덱스를 건드리지 않고 ILIAS 100M에서 reranking 전 29.2 mAP@1000, 후 42.0을 기록했고, LoRA fine-tune은 단일 forward pass로 같은 쿼리 측 이득을 재현해 O2I 강건성이 학습 가능한 성질임을 보인다.

**코드**: 불명

**태그**: image-retrieval, image-embedding, metric-learning, peft

---

### [Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching](https://arxiv.org/abs/2610.12421)

**한 줄 요약**: 부드러운 움직임·강체 기하 같은 시공간 사전가정 없이 생성·의미 foundation 표현과 이종 지도를 결합해 정체성 보존 대응을 찾는 dense matching 프레임워크 FreeMatching.

**핵심 기여**: 기존 dense correspondence는 smooth motion·rigid geometry 같은 단순화된 시공간 prior에 묶여 있는데, 이미지 편집과 reference-guided generation(IEG)에서는 시각적 정체성은 유지되면서 물리적 연속성이 깨지는 변환이 흔해 이 가정이 무너진다는 문제의식이다. FreeMatching은 생성 표현과 의미 foundation 표현을 결합하고 고전 데이터셋·추적 영상·합성 장면이라는 이종 지도를 함께 쓰며, dense correspondence 주석 없이 teacher 주도 반복 refinement로 IEG 상황의 대응을 개선한다. 단일 모델이 어려운 IEG 이미지쌍에서 대응 품질을 크게 올리면서 고전 벤치마크에서도 경쟁력 있는 성능을 유지하고, 정체성 보존을 재는 정량 지표로 쓸 때 사람 판단과 상관되는 점수를 낸다고 보고한다.

**코드**: 공개([FreeMatching](https://github.com/luping-liu/FreeMatching))

**태그**: correspondence, feature-matching, foundation-model

---

### [Rethinking Contrastive Loss in CLIP Post-training: A Complementary Framework with Frozen Text Encoder](https://arxiv.org/abs/2610.11374)

**한 줄 요약**: CLIP post-training에서 보고된 파국적 망각이 작은 배치가 아니라 contrastive temperature 크기 탓임을 짚고, 텍스트 인코더를 동결한 1-epoch 레시피 ComCLIP을 제안한 연구.

**핵심 기여**: 최근 연구는 작은 배치에서 음성 샘플이 부족해 contrastive loss가 post-training에 부적합하다며 distillation으로 갈아타자고 주장하는데, 이 논문은 InfoNCE의 gradient가 temperature에 어떻게 의존하는지로 설명하며 원인이 음성 부족이 아니라 부적절한 temperature $\tau$ 크기임을 보인다. $\tau$를 충분히 작게 두면 contrastive post-training이 사전학습 CLIP을 오히려 개선한다. 이 발견 위에 ComCLIP은 텍스트 인코더를 동결해 정제된 비전 인코더가 구조·추론 비용 변화 없이 그대로 교체 가능하도록 하고, 적절히 조정된 contrastive loss와 원본 CLIP에 대한 MSE anchoring, DINOv2로부터의 relational distillation을 함께 쓴다. 여러 seed에서 zero-shot 분류는 self-distillation 기준선 CLIP-Refine과 동등하면서 linear probing으로 잰 전이성이 크게 올랐고(ViT-B/16에서 48.99 대 42.28), ViT-L/14에서는 MMVP도 24.20 대 19.01로 앞선다. image-text 검색에서는 CLIP-Refine이 여전히 강하다는 한계를 밝히며, LLaVA-1.5-7B에 projector·LLM 재정렬 없이 끼워 넣어도 8개 VLM 벤치마크에서 순변화가 없어 하위 호환이 깨지지 않음을 보인다.

**코드**: 공개([ComCLIP](https://github.com/showstarpro/ComCLIP))

**태그**: ssl-backbone, image-embedding, distillation, foundation-model

---

### [One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed Experts](https://arxiv.org/abs/2610.12448)

**한 줄 요약**: Transformer 블록 하나를 재귀적으로 돌리되 각 깊이의 FFN을 공유 expert bank의 볼록 결합으로 표현해 full-depth 인코더 정확도를 맞추는 reViT.

**핵심 기여**: 단일 블록을 반복 적용하면 깊이별 변환이 사라진다는 문제를 두고, reViT는 각 재귀 깊이의 FFN을 작은 공유 expert bank의 볼록 결합으로 구성하고 연속적인 정규화 깊이 좌표가 그 혼합을 프로그래밍하게 해 FFN 파라미터 공간을 지나는 재샘플링 가능한 궤적을 정의한다. ImageNet-1k 지도학습과 DINOv2 teacher distillation 두 체제에서 평가했고, 동일한 one-FFN 예산에서 weight-space merging이 token-dispatch·output-mixture 대안보다 강한 MoE 계열임을 통제 비교로 확인한다. 처음부터 학습한 reViT-B/16은 저장 파라미터를 약 70% 줄이면서 DeiT III 정확도에 도달하고, teacher의 출력 피쳐만으로 증류한 8-expert 모델은 DINOv2 teacher의 linear-probe 정확도를 거의 그대로 유지하면서 분류·segmentation·depth로 전이된다. elastic-depth 학습으로 체크포인트 하나가 여러 깊이에서 동작하며, 고정 깊이 배포 시에는 재귀 블록을 일반 dense 그래프로 펼쳐 온라인 라우팅과 merging을 없앨 수 있으나 배포 저장 용량은 늘어난다.

**코드**: 불명

**태그**: ssl-backbone, distillation, efficient-inference, foundation-model

---

### [CARE: Constrained Attention Refinement for Fine-Grained Visual Classification via Teacher-Student Distillation](https://arxiv.org/abs/2610.11153)

**한 줄 요약**: 학습 때만 쓰는 query teacher가 DINOv2 중간층을 읽어 class-specific attention student에 지식을 넘기는 해석 가능한 fine-grained 인식 프레임워크.

**핵심 기여**: class-specific attention 경로는 해석 가능한 인식의 자연스러운 기반이지만 제한된 예측 구조 탓에 변별력이 떨어지고 강한 사전학습 백본의 중간 표현을 충분히 쓰지 못한다는 문제의식이다. CARE는 최종 예측과 설명을 class-specific attention student 안에 유지하면서, 학습 전용 auxiliary query teacher가 학습 가능한 query로 선택된 DINOv2 중간층을 읽어 multi-level 표현을 융합하고 logit-standardized class-discriminative 지식을 student에 전달한다. student의 attention head에는 다양성·희소성 항을 걸어 중복을 줄이고 특징이 좁게 국소화되도록 한다. CUB·Oxford-IIIT Pet·Stanford Dogs·Stanford Cars에서 백본을 동결한 해석 가능 설정으로 CUB Top-1 78.5%를 기록했고, insertion/deletion 기반 faithfulness 분석에서 상위 attention 영역이 클래스 관련 근거를 담고 있음을 보인다.

**코드**: 불명

**태그**: fine-grained, distillation, ssl-backbone

---

### [S$^3$Geo: Structure-Semantic Synergistic Learning for Cross-View Geo-Localization](https://arxiv.org/abs/2610.11608)

**한 줄 요약**: dense 토큰에서 영역 단위 피쳐를 뽑고 optimal transport 기반 query-level contrastive로 soft 대응을 세우며 CLIP teacher의 의미 사전지식을 증류하는 cross-view 매칭 프레임워크.

**핵심 기여**: 드론·위성처럼 시점이 크게 다른 이미지를 매칭하는 기존 방법은 시각 표현에만 기대어 fine-grained 구조 대응과 의미 사전지식을 함께 모델링하지 못하고, 겉은 비슷하지만 의미가 다른 영역을 혼동한다는 문제의식이다. Decoupled Query Pooling(DQP)으로 dense 토큰에서 영역 인식 피쳐를 소수만 뽑아 국소 구조 패턴을 명시적으로 모델링하고, optimal transport 형태의 query-level contrastive 학습으로 cross-view 공간 어긋남 아래에서 soft 대응을 세운다. 여기에 동결된 CLIP teacher로부터 Semantic Knowledge Distillation(SKD)을 걸어 의미 사전지식과 관계 구조를 옮겨 hard negative 변별을 높인다. University-1652와 SUES-200에서 추론 복잡도를 늘리지 않고 기존 최고 성능을 일관되게 넘는다고 보고한다.

**코드**: 불명

**태그**: feature-matching, image-retrieval, metric-learning, distillation

---

### [EvoKnow: Continual Knowledge Evolution for AI-Generated Image Detection](https://arxiv.org/abs/2610.11381)

**한 줄 요약**: 과거 생성 이미지를 재생(replay)하지 않고 분리된 residual expert를 증설하며 closed-form 라우터로 전문성을 불러오는 AI 생성 이미지 탐지의 지속학습 프레임워크.

**핵심 기여**: AI 생성 이미지 탐지기는 고정된 생성기 도메인에서 학습돼 새 생성 모델이 나올 때마다 유지가 어렵고, 과거 생성 이미지 재생은 비용이 크며 현재 도메인 데이터만으로 공유 파라미터를 갱신하면 이전 포렌식 지식을 덮어쓴다는 문제의식이다. EvoKnow는 base 도메인에서 학습한 공유 포렌식 기반은 보존한 채, 생성기별 보완 증거를 담당하는 고립된 residual expert를 점진적으로 추가하고, 현재 단계 생성 이미지와 누적 충분통계로부터 closed form으로 갱신되는 Analytical Incremental Router(AIR)로 전문성을 검색한다. 생성기 하나당 생성 이미지 열 장만으로 GenImage의 non-base 생성기에서 평균 96.70%, 대상 벤치마크 적응 없이 Chameleon에서 94.48% 정확도를 달성하고, 엄격한 replay-free 지속학습 프로토콜에서 단계별 평균 정확도 96.32%, 평균 망각 4.32%를 기록한다.

**코드**: 불명

**태그**: forgery-detection, continual-learning, anomaly-detection

---

### [Relative Patch Response Learning for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2610.11876)

**한 줄 요약**: 정렬된 real-generated 쌍의 두 혼합 뷰 사이에서 같은 패치의 점수 변화량을 비교해 학습하는 AI 생성 이미지 탐지 목적함수.

**핵심 기여**: 정렬 쌍을 쓰는 최근 방법은 실제 이미지의 일부 패치를 생성 대응물로 바꿔 혼합 뷰를 만드는데, self-attention 때문에 real 패치와 generated 패치가 상호작용해 각 패치 피쳐가 더는 자기 출처만 반영하지 않으므로 패치별 출처 라벨이 부정확한 학습 목표가 된다는 관찰에서 출발한다. PRL은 패치마다 라벨을 붙이는 대신 정렬 쌍의 두 혼합 뷰에서 같은 패치의 점수 변화(patch response)를 비교하며, (i) 출처가 바뀐 패치의 반응을 출처가 그대로인 패치의 반응과 견주는 relative response 목적함수로 맥락 이동만 따로 떼어 정밀한 지도를 주고, (ii) reference coherence 항으로 출처 불변 패치 집단이 한 덩어리로 움직이게 해 기준을 안정화하며, (iii) area ranking 항으로 생성 영역이 넓은 뷰가 더 높은 평균 패치 점수를 갖도록 한다. 표준 벤치마크 8개와 in-the-wild 3개에서 평균 balanced accuracy를 기존 최고 대비 각각 4.3%, 5.9% 끌어올렸다.

**코드**: 불명

**태그**: forgery-detection, anomaly-detection, image-embedding

---

### [Stop My Dancing! Understanding, Detecting and Attributing Motion-Aware Deepfake Videos](https://arxiv.org/abs/2610.11496)

**한 줄 요약**: pose-guided diffusion이 만드는 전신 동작 딥페이크(MAD)의 벤치마크를 구축하고, 공간 의미와 steganalysis 주파수 피쳐를 교차 정렬해 탐지·출처 귀속하는 MoDA.

**핵심 기여**: pose-guided diffusion이 움직이는 전신을 합성하면서 생긴 Motion Aware Deepfake(MAD)를 다루기 위해, 실제 1,363편과 생성기 여섯 종의 합성 30,122편을 섞은 150만 프레임 규모의 첫 MAD 전용 벤치마크를 현실적 왜곡과 open-world 평가 분할과 함께 만든다. 분석 결과 MAD는 전역적으로는 일관돼 보여도 제한된 입력 프레임으로 움직임을 예측·시뮬레이션해야 하므로 동작 경계에 고주파 아티팩트와 모델별 스펙트럼 지문을 남긴다. MoDA는 공간 의미와 steganalysis 기반 주파수 피쳐를 cross-domain alignment와 multi-scale aggregation으로 결합해 in-distribution 94.8%, cross-dataset 89.1% 탐지 정확도(기존 대비 10~25% 향상)와 91.5% 모델 귀속 정확도를 얻는다. 미지의 상용 MAD 플랫폼 두 곳에서 만든 200클립에 81.94%, 인터넷에서 수집한 미지의 MAD 1,200클립(총 5.5만 프레임)에 78.13% 정확도를 보이고, white-box·gray-box·black-box 적응형 공격에서도 기준선이 급락하는 동안 상대적으로 안정적인 성능을 유지한다.

**코드**: 불명

**태그**: forgery-detection, video, dataset-benchmark, print-forensics

---

### [Is In-Domain Training Enough for Fine-Grained Industrial Anomaly Understanding?](https://arxiv.org/abs/2610.12310)

**한 줄 요약**: 산업 이상 이해에서 in-domain 학습만으로는 fine-grained 지각 격차가 닫히지 않음을 보이고, 이종 MLLM 에이전트와 전용 결함 전문가를 분업시킨 SiGMA를 제안한 연구.

**핵심 기여**: 단일 MLLM은 탐지·위치추정·기술·추론을 동시에 잘하기 어렵다는 문제의식에서, in-domain 학습이 이 격차를 메우지 못함을 MMAD 벤치마크에서 보인다. 학습된 특화 모델도 결함 위치추정 정확도가 최대 75.5%로 사람 전문가 92.3%에 못 미치고, 이상 탐지는 오히려 학습 전 기반 모델보다 부정확하며, 서로 보완적인 MLLM들을 단순 결합해도 fine-grained 지각 약점은 공통이라 제거되지 않는다. SiGMA는 공간적으로 접지된 multi-agent 구조로, multimodal searcher가 산업 지식과 정상 레퍼런스를 공급하고 전용 결함 전문가가 쿼리-레퍼런스 비교를 캘리브레이션된 이상 증거로 바꾸며, 라벨 없이 동작하는 신뢰도 컨트롤러가 과제별 역량과 쿼리별 증거 품질로 각 출처에 가중치를 준다. MMAD 평균 정확도 85.2%로 가장 강한 학습 특화 모델과 Gemini-2.5-Pro를 4.0% 앞서고 사람 전문가와 1.5% 차이이며, 9B 이하 에이전트 셋만으로도 84.4%에 도달하고 새 MLLM은 재학습 없이 합류한다.

**코드**: 불명

**태그**: industrial-inspection, anomaly-detection, defect-detection, vlm

---

### [Do Not Train Away Uncertainty: Early Uncertainty Anchored Calibration](https://arxiv.org/abs/2610.12048)

**한 줄 요약**: 학습 초기 모델이 더 잘 캘리브레이션돼 있다는 관찰에 기대어, 초기 모델을 불확실성 앵커로 삼아 과신을 억제하는 정규화 기법 EUA-Cal.

**핵심 기여**: 학습·미세조정이 진행될수록 정확도 이득은 미미한데 캘리브레이션 오차는 크게 늘어나는 현상이 여러 모델에서 일관되게 나타나며, 초기 모델이 예측과 피쳐 양쪽에서 불확실성 인식을 유지하다가 학습이 이어지면서 이를 점차 잃는다는 분석을 제시한다. EUA-Cal은 초기 예측 불확실성을 보존하는 early prediction regularization과 초기 피쳐 공간에 반영된 불확실성을 활용하는 prototype structure regularization을 함께 걸어 과신을 완화한다. 이미지 분류와 객관식 질의응답에서 서로 다른 모델 여덟 종에 적용해 기존 최고 캘리브레이션 기법들을 앞선다고 보고한다.

**코드**: 불명

**태그**: calibration, training-free, foundation-model

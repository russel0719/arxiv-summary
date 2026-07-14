# arXiv cs.CV Daily Digest — 2026-07-15 (KST)

- **전체 신규 논문 수**: 223편 (new 188 + cross-list 35)
- **선별 수**: 12편

## 오늘의 트렌드

오늘 cs.CV 신규는 3D Gaussian Splatting·diffusion 생성/편집·의료영상이 여전히 큰 비중을 차지하는 가운데, 파운데이션 모델(CLIP·GroundingDINO·SAM3·DINOv3)을 특정 태스크에 파인튜닝 없이 적응시키는 "training-free"·in-context 접근이 두드러졌다. 관심 분야 관점에서는 (1) open-vocabulary 검출/분할의 신뢰도 편향·grounding 일관성 등 실사용 신뢰성 이슈, (2) MVTec-3D·포인트클라우드 기반 산업 이상탐지의 멀티모달·데이터 효율화, (3) 문서 AI 전용 비전 백본과 위변조/합성 이미지 포렌식, (4) 소형 VLM 증류·다차원 프루닝 등 엣지/실서비스 배포 경량화가 고르게 관찰되었다.

---

### [MonkeyOCRv2: A Visual-Text Foundation Model for Document AI](https://arxiv.org/abs/2607.11562)

**한 줄 요약**: 문서 이미지 전용으로 사전학습한 비전-텍스트 파운데이션 인코더로, 동결 상태에서도 CLIP/DINO/SAM 기반 인코더를 능가하는 문서 AI 백본.

**핵심 기여**: 1.13억 장·17개 언어 규모의 최대 문서 이미지 코퍼스 MonkeyDoc v2를 구축하고, image-to-text 생성과 픽셀 단위 문서 복원을 동시에 학습해 텍스트 정렬과 문자 획·레이아웃 디테일을 함께 보존한다. 텍스트 인식·수식 인식·검출·위변조 검출·중첩 텍스트 분할 등 5개 과제에서 인코더 교체만으로 일관된 향상을 보인다. 동결 인코더 + 경량 LLM으로 만든 0.7B 파싱 모델이 11배 큰 기존 3B SOTA(dots.ocr)를 MDPBench에서 2.8%p 앞선다.

**실무 관련성**: OCR/document AI 파이프라인의 비전 백본으로 바로 교체 가능하며, 문서 위변조 검출까지 커버해 문서 품질검사 응용에 유용하다.

**키워드**: Document AI, OCR, visual-text pretraining, foundation model, document tampering

---

### [Bridging the Catalog-to-Real Gap: Scalable Product Recognition via Multi-Stage Contrastive Learning](https://arxiv.org/abs/2607.09888)

**한 줄 요약**: 매장 실촬영 이미지를 대규모 상품 카탈로그에 매칭하는 문제를 임베딩 기반 크로스도메인 검색으로 재정의한 다단계 대조학습 프레임워크.

**핵심 기여**: 닫힌집합 분류가 아니라 쿼리 crop→카탈로그 참조 이미지 검색 문제로 정식화했다. 스튜디오 packshot과 노이즈 많은 매장 이미지 간 도메인 격차를 좁히기 위해 item-level·image-level 유사도를 모두 활용해 타겟형 hard negative mining을 수행하는 catalog-to-real 다단계 대조학습(Cat2Real)을 제안한다. 실제 학습 이미지가 전혀 없는 신규 상품/카테고리에도 seamless하게 확장되는 zero-shot 일반화를 입증한다.

**실무 관련성**: fine-grained 상품 검색 + FAISS 벡터 검색과 결합하는 임베딩 학습 파이프라인에 직접 대응되는 사례로, hard negative mining 전략이 특히 참고할 만하다.

**키워드**: product recognition, cross-domain retrieval, contrastive learning, hard negative mining, zero-shot

---

### [GFR-SAM: Training-Free Referring Camouflaged Object Segmentation via Cross-Image Prompting](https://arxiv.org/abs/2607.11732)

**한 줄 요약**: SAM3의 cross-image in-context 프롬프팅과 DINOv3 프로토타입 정렬을 결합해 학습 없이 위장(camouflaged) 객체를 참조 기반으로 분할하는 3단계 프레임워크.

**핵심 기여**: 취약한 point-matching 대신 "Generate-Filter-Refine" 파이프라인을 제안한다. (1) In-Context Exemplar-guided Segmentation으로 SAM3에 cross-image 추론을 부여해 후보 마스크를 생성하고, (2) DINOv3 기반 Region-Global 대조 필터링으로 배경 방해요소를 억제하며, (3) bbox+텍스트 프롬프트를 결합한 기하-의미 정제로 경계와 recall을 개선한다. R2C7K에서 training-free 기법 대비 F-measure +8.7%로 지도학습 SOTA와 경쟁한다.

**실무 관련성**: SAM/DINO 파운데이션 모델을 파인튜닝 없이 특수 분할 과제에 적용하는 방법론으로, 라벨 없는 산업 분할·검사 시나리오에 응용 가능하다.

**키워드**: SAM3, DINOv3, training-free segmentation, referring segmentation, in-context prompting

---

### [SynCLIP: Synonym-Coherent Language-Image Pretraining for Robust Open-Vocabulary Dense Perception](https://arxiv.org/abs/2607.11008)

**한 줄 요약**: 동의어로 표현이 바뀌면 grounding이 흔들리는 문제(synonym-induced inconsistency)를 해결한 open-vocabulary dense perception용 CLIP 사전학습.

**핵심 기여**: 의미가 같은 표현이 서로 다른 공간 attention을 유발하는 한계를 지적하고, 원 표현과 동의어 표현의 attention map 차이를 최소화하는 SSA 모듈과 관련 영역을 선택적으로 강화하는 SAR 모듈을 제안한다. 카테고리마다 다중 동의어·정의를 붙인 SEViC 코퍼스를 구축해 동의어 일관 사전학습을 지원한다. CLIP 기반 OVDP에서 언어 변형에 대한 견고성과 SOTA 성능을 달성한다.

**실무 관련성**: open-vocabulary 검출/분할을 실서비스에 쓸 때 프롬프트 표현 변화에 대한 안정성을 높여주는 접근으로, 텍스트 쿼리 다양성이 큰 환경에 유용하다.

**키워드**: open-vocabulary, CLIP, dense perception, grounding consistency, synonym robustness

---

### [Confidence Scores in Open-Vocabulary Detection Are a Biased Mixture of Scale and Semantics](https://arxiv.org/abs/2607.10993)

**한 줄 요약**: GroundingDINO·OWL-ViT·YOLO-World의 confidence 점수가 물체 크기와 쿼리 일반성에 편향된 혼합 신호임을 통제 실험으로 규명.

**핵심 기여**: s=cos(v,t) 점수가 (1) 큰 물체 점수를 부풀리는 scale bias와 (2) 일반적 쿼리 점수를 낮추는 semantic bias의 편향된 혼합임을 COCO·LVIS에서 정량적으로 입증하고 α·β 계수를 제시한다. 이 편향은 CLIP의 image-level 사전학습에서 구조적으로 필연적이며 임계값 조정만으로는 제거할 수 없다. 파라미터 없는 temperature scaling으로 소형 물체 Recall@10을 19.6% 개선하되 pooled-ranking precision은 소폭 손해를 봐, 편향이 부분적으로만 되돌릴 수 있음을 규명한다.

**실무 관련성**: open-vocab 검출기의 threshold/스코어를 실무에서 다룰 때 크기·쿼리 편향을 반드시 보정해야 함을 알려주는 실용적 진단으로, 검출 신뢰도 캘리브레이션에 직접 참고된다.

**키워드**: open-vocabulary detection, GroundingDINO, confidence calibration, scale bias, CLIP

---

### [TC-MAF: Train-Calibrated Bounded Multi-Evidence Fusion for Multimodal Industrial Anomaly Detection](https://arxiv.org/abs/2607.11170)

**한 줄 요약**: RGB+3D 멀티모달 산업 이상탐지에서 카테고리별로 신뢰도가 다른 보조 근거를 훈련 통계만으로 조절해 융합하는 base-anchored 다중근거 융합.

**핵심 기여**: 멀티모달 검출기 + 보완적 Dinomaly 근거 + 소규모 cross-modal 일관성 단서를 고정된 픽셀 단위 융합 공식 하나로 결합한다. 정상 훈련 통계만 쓰는 경량 training-dispersion confidence(TDC)로 보조 근거의 참여도를 스케일한다. MVTec-3D에서 image-level AUROC 0.979, pixel-level AUPRO 0.990으로 비교 멀티모달 기법 중 최고이며, few-shot·3D 결손·cross-dataset(Eyecandies)에서도 견고하다.

**실무 관련성**: 제조 품질검사(MVTec-3D류)의 멀티모달 이상탐지 실전 배치에 바로 부합하며, 라벨 없이 정상 통계만으로 캘리브레이션하는 점이 매력적이다.

**키워드**: industrial anomaly detection, multimodal fusion, MVTec-3D, Dinomaly, calibration

---

### [Physics-inspired Pseudo Anomaly Generation and Prototype Feature Guidance for 3D Anomaly Detection](https://arxiv.org/abs/2607.10544)

**한 줄 요약**: 실제 이상 샘플이 희소한 3D 포인트클라우드 이상탐지를 위해 물리 기반 pseudo-anomaly 생성과 프로토타입 특징 가이드를 도입한 프레임워크(PA3AD).

**핵심 기여**: 정상 데이터에서 물리적으로 그럴듯한 가짜 이상 포인트클라우드를 생성하는 multi-physics 모듈과, momentum 업데이트 프로토타입 + difference-aware fusion으로 정상 표현과 가짜 이상 간 분포 차이를 포착하는 설계를 제안한다. Anomaly-ShapeNet·Real3D-AD에서 SOTA를 일관되게 상회한다.

**실무 관련성**: 이상 샘플 수집 비용이 큰 제조 검사에서 정상 데이터만으로 3D 이상탐지 성능을 끌어올리는 접근으로, 데이터 부족 환경에 실용적이다.

**키워드**: 3D anomaly detection, point cloud, pseudo-anomaly, prototype learning, industrial inspection

---

### [ScratNet: A Swin-Based Multi-Scale Dilated Network with Precision Refinement for Semiconductor Scratch Segmentation](https://arxiv.org/abs/2607.10214)

**한 줄 요약**: 불규칙·저대비·다중 스케일의 반도체 표면 스크래치 결함을 Swin 백본 + 정밀 경계 정제로 분할하는 end-to-end 프레임워크.

**핵심 기여**: 수정된 Swin Transformer 백본에 전용 디코더를 결합해, 지역·전역 문맥을 함께 잡는 Multi-Scale Dilated Aggregation, 공간 디테일 복원을 위한 Stem Integration Module, 이방성 컨볼루션으로 경계를 날카롭게 하는 Precision Refinement 분기를 도입한다. 얇고 불규칙한 결함에서 기존 기법 대비 일관되게 우수한 정확도를 보인다.

**실무 관련성**: 반도체/제조 품질검사의 미세 결함 세그멘테이션에 직접 대응하는 산업 응용으로, 경계 민감 결함 검출 아키텍처 설계에 참고된다.

**키워드**: semiconductor inspection, scratch segmentation, Swin Transformer, defect detection, manufacturing

---

### [Answer-Conditioned Chain-of-Thought Distillation for Few-Shot Industrial Vision with Small VLMs](https://arxiv.org/abs/2607.10666)

**한 줄 요약**: 정답을 조건으로 준 frontier VLM의 시각적 추론을 3B 소형 VLM에 LoRA로 증류해, 극소량 라벨로 산업 검사 과제에 빠르게 적응.

**핵심 기여**: frontier VLM에 이미지+정답을 주고 근거 있는 시각 설명을 생성시킨 뒤, 이 추론 증강 예시로 3B 모델을 LoRA 파인튜닝한다. 정답 조건화로 모든 훈련 추론을 올바른 결론으로 유도하여, frontier 모델 정확도가 24.1%까지 낮아지는 어려운 과제를 보완한다. 과제당 18~30장만으로 4개 산업 분류 과제에서 direct fine-tuning을 16/16 조합 모두 상회(+1.7~4.4%p)하며, 용접 방사선 사진에서는 24장 학습으로 GPT-4.1을 10.0%p 앞선다.

**실무 관련성**: 결함 유형이 자주 바뀌고 라벨이 적은 제조 검사에 소형 VLM을 배포하는 시나리오에 딱 맞으며, 증류 + 경량 배포 관심사와 정확히 부합한다.

**키워드**: industrial inspection, VLM distillation, chain-of-thought, LoRA, few-shot

---

### [Towards Efficient Convolutional Neural Network for Embedded Hardware via Multi-Dimensional Pruning](https://arxiv.org/abs/2607.11473)

**한 줄 요약**: CNN의 depth·width·resolution 세 차원을 협력적으로 프루닝해 임베디드 하드웨어 실행 효율을 높이는 다차원 프루닝 프레임워크(TECO).

**핵심 기여**: 각 차원 내 지역 중요도와 차원 간 전역 중요도를 함께 평가하는 2단계 중요도 평가 프레임워크를 제안하고, 이를 바탕으로 정확도-효율 최적 절충을 향해 점진적으로 세 차원을 프루닝하는 휴리스틱 알고리즘을 제시한다. 여러 벤치마크에서 기존 SOTA 프루닝을 상회한다.

**실무 관련성**: 실서비스/엣지 배포를 위한 모델 경량화 기법으로, 단일 축이 아닌 다차원 동시 압축이 필요한 배포 최적화에 참고된다.

**키워드**: model pruning, CNN compression, embedded deployment, efficiency, multi-dimensional

---

### [Effective Synthetic Image Detection via Noise Residual Clustering](https://arxiv.org/abs/2607.10695)

**한 줄 요약**: Noiseprint++ 잔차 지문 + 동결 ViT 특징을 비지도 K-Means로 군집화해 학습 없이 합성(생성 AI) 이미지를 탐지.

**핵심 기여**: 대규모 라벨 학습에 의존하는 기존 탐지기의 미지 생성모델 일반화 저하를 완화하기 위해 training-free 방식을 제안한다. Noiseprint++로 노이즈 잔차 지문을 뽑고 동결 ViT로 멀티스케일 특징을 추출·적응 가중 융합한 뒤, 소수의 실제 이미지 샘플만으로 K-Means 군집 중심을 초기화해 실제/합성을 구분한다. 4개 벤치마크 평균 82.2% 정확도로 일반화 측면에서 SOTA를 상회하며 특히 diffusion 계열에 우수하다.

**실무 관련성**: 위조/합성 이미지 판별을 라벨·재학습 없이 수행하는 접근으로, 미지 생성모델에 대한 일반화가 중요한 포렌식/콘텐츠 진위 판별에 유용하다.

**키워드**: synthetic image detection, forgery detection, training-free, noise residual, ViT

---

### [Label-Free Target-Domain Adaptation for Unconstrained Event-Image Feature Matching via Dual-Stage Distillation](https://arxiv.org/abs/2607.10082)

**한 줄 요약**: 매칭 라벨도 정렬된 하드웨어도 없는 실환경에서 이벤트-이미지 픽셀 대응을 학습하는 2단계 증류 패러다임.

**핵심 기여**: (1) 대규모 데이터로 분포 기반·대조 손실을 결합한 label-agnostic 증류 사전학습으로 일반화 표현을 학습하고, (2) epipolar prior 기반 기하 신뢰도와 일관성 검증으로 견고한 매칭만 골라 타겟 도메인에서 지도 없이 self-evolve하는 epipolar-guided self-distillation을 도입한다. 서로 다른 내부 파라미터·해상도의 물리적으로 분리된 카메라 기반 신규 벤치마크(TUM-VIE)를 제시하고 MVSEC·TUM-VIE 포즈 추정에서 SOTA를 달성한다.

**실무 관련성**: 라벨 없는 크로스모달 feature matching + 증류 조합으로, 정렬 가정 없이 표현을 전이·자기증류하는 방법론이 feature-matching 연구에 직접 참고된다.

**키워드**: feature matching, event camera, self-distillation, cross-modal, label-free

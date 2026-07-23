# arXiv cs.CV Daily Digest — 2026-07-24 (KST)

- **전체 신규 논문 수**: 88편 (new 71 + cross-list 17)
- **선별 수**: 9편

## 오늘의 트렌드

오늘은 네 흐름이 두드러진다. 첫째, **UAV·위성·항공을 무대로 한 크로스뷰 검색·측위**가 큰 묶음을 이뤘다 — DINOv2 리트리버를 검색과 국소 매칭에 함께 재사용하는 RIM, 오프-나디르 시점 지오로컬라이제이션 ONLoc, 항공 소형 타깃 참조분할(SkyAnchor) 등. 둘째, **학습 없는 plug-and-play 가속**이 거의 모든 서브분야에 퍼졌다 — SAM2(Lean-SAM2), AR 비디오 확산(HeadCast), diffusion policy 캐시(EVO), MLLM 토큰-연산 공동 스케줄링(SmartVL), 원스텝 비디오 편집(OSVE). 셋째, **비디오·월드 생성과 3D Gaussian Splatting**(SGF, StreamHOI, Vera, WearWow, ATSplat, GaussianSeed)이 여전히 대량으로 등장했다. 넷째, **벤치마크·데이터셋 공개**가 유독 많았다(DRGBT-1K, DIM-Fashion, NavVerse, KineBench, MV-Bench, PhenSPINE 등). 내 관심사 기준으로는 검색·매칭 임베딩(RIM·OffNadirLoc·FashionAM), SSL 목적함수가 표현 수렴을 이끈다는 인과 분석, SAM2 경량화, 대조학습 재가중(IAS), OOD/이상 탐지 벤치마크 누수 진단, 그리고 위조 영상 조기 판별에서 수확이 있었다.

---

### [RIM: A Retrieval-In-Matching Framework for Cross-Domain Global Visual Localization of UAVs](https://arxiv.org/abs/2607.20116)

**한 줄 요약**: 하나의 DINOv2-B forward만으로 전역 검색(retrieval)과 국소 매칭(local matching)을 동시에 처리하는 UAV 크로스도메인 시각 측위 파이프라인.

**핵심 기여**: UAV↔위성 이미지 간 촬영시점·플랫폼 차이(cross-domain shift)를 다루기 위해 Google 3D Tiles에서 UAV 시점 참조뷰를 위치·고도·방향별로 샘플링하고, pose-near positive와 지리적으로 먼 hard negative로 SALAD를 크로스도메인 파인튜닝한다. 핵심인 RIM은 적응된 DINOv2-B 리트리버를 프로즌한 뒤 그 token field를 재사용하는 local-descriptor decoder를 증류(distill)해, 두 번째 파운데이션 백본 없이 하나의 쿼리 forward로 SALAD 검색과 국소 기술자를 함께 얻는다. zero-shot으로 EPFL/Park에서 Recall@1을 SALAD 대비 크게(25/50m에서 8.55/13.77pp 등) 끌어올리고, 검색+매칭+기하검증 전체가 67.9ms로 RoMa보다 40배 이상 빠르다.

**실무 관련성**: 단일 SSL 백본(DINOv2)을 검색용 global descriptor와 매칭용 local descriptor로 함께 재사용하는 설계는, FAISS 벡터 검색과 피쳐 매칭을 하나의 임베딩 파이프라인으로 통합하려는 내 관심사와 정확히 맞닿는다.

**태그**: feature-matching, image-retrieval, foundation-model, distillation, correspondence

---

### [OffNadirLoc: Benchmark and Framework for Challenging UAV-to-Satellite Geo-Localization under Large Off-Nadir Views](https://arxiv.org/abs/2607.19951)

**한 줄 요약**: 큰 오프-나디르 시점의 UAV-위성 크로스뷰 지오로컬라이제이션 벤치마크와, 구조 인지 가중·뷰 일관 학습으로 시점 불변 표현을 학습하는 ONLoc.

**핵심 기여**: 기존 벤치마크가 near-nadir에 치우쳐 심한 시점 왜곡·가림·외형 격차를 다루지 못하는 한계를 지적하고, 대규모 오프-나디르 벤치마크 OffNadirLoc을 제안한다. ONLoc은 (i) 신뢰할 만한 국소 피쳐를 강조하고 반복적·모호한 영역을 억제하는 structure-aware contextual weighting과 (ii) 하나의 위성 이미지와 여러 시점의 UAV 이미지를 하나의 의미 그룹으로 묶어 set-level로 지도하는 view-coherent learning을 도입한다. 이 집합 단위 지도는 pairwise contrastive보다 멀티뷰 일관성을 잘 포착해 시점 불변·판별적 표현을 얻고, 미학습 데이터셋에도 강한 zero-shot 일반화를 보인다.

**실무 관련성**: 시점이 크게 달라도 같은 장소를 검증·검색하는 표현학습으로, re-identification·이미지쌍 검증·검색용 임베딩 설계에 참고할 set-level metric learning 기법이다.

**태그**: image-retrieval, metric-learning, correspondence, re-identification

---

### [Diverse-Intent Multi-Turn Fashion Image Retrieval](https://arxiv.org/abs/2607.20291)

**한 줄 요약**: 다양한 의도 전환·롤백을 담은 멀티턴 패션 검색 벤치마크와, 텍스트화 없이 멀티모달 대화 쿼리를 갤러리 임베딩 공간에 직접 정렬하는 FashionAM.

**핵심 기여**: 기존 멀티턴 검색이 매 턴 동일한 속성 편집(attribute-editing)만 가정하는 한계를 지적하며, 7개 태스크·13개 패션 데이터셋에서 구성한 26K 세션 벤치마크 DIM-Fashion을 제안한다. 또 멀티모달 쿼리를 텍스트로 변환(textification)해 세밀한 시각 단서를 잃는 관행 대신, MLLM-VLP 프레임워크 FashionAM으로 멀티모달 대화 쿼리를 패션 지향 갤러리 임베딩 공간에 직접 정렬해 중간 텍스트화를 제거한다.

**실무 관련성**: 텍스트 경유 없이 이미지+텍스트 쿼리를 하나의 검색 임베딩 공간으로 맞추는 접근은, 대화형·조건부 이미지 검색을 벡터 검색과 결합하려는 내 관심사에 직접 적용 가능하다.

**태그**: image-retrieval, image-embedding, metric-learning, fine-grained, vlm

---

### [Self-supervision drives representational convergence in medical foundation models more than clinical supervision](https://arxiv.org/abs/2607.20274)

**한 줄 요약**: 의료 파운데이션 인코더들의 표현 수렴은 규모나 임상 지도가 아니라 self-supervised 목적함수가 이끈다는, 통제된 해부 실험.

**핵심 기여**: 18개 이미지·7개 텍스트 인코더(7M~27B), 5개 modality, 흉부 X선 65만 장(6개 데이터셋)을 로컬에서 돌리고, 데이터·구조·규모를 고정한 채 목적함수만 바꾼 인코더로 인과를 분리했다(합성 모델로도 재현). 수렴은 랜덤 바닥보다는 높되 완만하며, self-supervised 목적함수가 가장 크게 정렬(흉부 40.4%)시키고 label-supervised(21.1%)·image-text(3.3%)는 훨씬 낮았다. 수렴은 모델 크기·능력에 따라 커지지 않았고 within-modality에 국한됐지만, 선형 분류기는 인코더 간·5개 미학습 병원으로 전이돼 within-encoder 성능의 약 85%를 유지했다.

**실무 관련성**: "왜 SSL 백본 임베딩이 태스크·도메인을 넘어 재사용되는가"를 인과적으로 짚어, 상호운용성은 규모가 아니라 사전학습 목적함수로 설계해야 한다는 실무 지침을 준다.

**태그**: ssl-backbone, image-embedding, foundation-model

---

### [Lean-SAM2: Target-Anchored Memory and Encoder Acceleration for SAM2](https://arxiv.org/abs/2607.19811)

**한 줄 요약**: 타깃 앵커 기반 메모리 프루닝과 위험 인지 인코더 라우팅으로 SAM2의 메모리·인코더 연산 중복을 제거한 경량 promptable 세그멘테이션 프레임워크.

**핵심 기여**: SAM2의 무거운 memory cross-attention과 매 프레임 전체 피쳐 추출을 줄이되, 기존 휴리스틱 프루닝이 가림·distractor에서 급락하는 문제를 세 기법으로 해결한다 — (1) 프롬프트 유래 전경 앵커와의 의미 일관성으로 타깃 토큰을 보호하는 TAMP, (2) 가시성 게이트 융합에 고신뢰 항목 보험뱅크를 더한 TCIM, (3) 앵커 유사도로 타깃 관련 윈도우에만 무거운 인코더를 켜고 급변 시 전체 갱신으로 폴백하는 위험 인지 라우팅 TARR. LVOSv2에서 SAM2.1-Large/Base+를 각각 1.412×/1.417× 가속하면서 J&F를 5.0%/3.6% 높였다.

**실무 관련성**: SAM 계열을 실서비스에 얹을 때의 핵심 병목(메모리·인코더 비용)을 정확도 손실 없이 줄이는 배포 최적화로, 세그멘테이션 파운데이션 모델 경량화에 바로 참고된다.

**태그**: segmentation, efficient-inference, foundation-model, video

---

### [Not All Patches are Equal: Sampling Matters for Visible-Infrared Pre-Training](https://arxiv.org/abs/2607.20238)

**한 줄 요약**: 패치마다 비교 신뢰도가 다르다는 관점에서 대조 사전학습의 강조도를 재가중하는 plug-and-play 중요도 인지 샘플링(IAS).

**핵심 기여**: VIS-IR 대조 사전학습에서 균일 패치 대조는 촬영 물리 차이로 비교 불가한 영역까지 동일 강도로 정렬해 표현·전이를 해친다고 지적한다. IAS는 (i) 적외선 구조 단서로 패치 가중치를 유도해 대조 목적함수를 재가중하고, (ii) 경량 sampler로 soft importance mask를 학습(수제 prior로 warm-start 가능)하며, (iii) 고신뢰 영역에서 어려운 패치로 넓혀가는 patch curriculum을 쓴다. UNIV류 패치/상관 정렬과 ImageBind류 이미지 대조 양쪽에 붙어 IR 분할·검출, VIS 분할, 크로스모달 검색에서 일관된 향상을 준다.

**실무 관련성**: 대조·표현학습에서 "어떤 쌍을 얼마나 강하게 정렬할지"를 신뢰도로 조절하는 범용 재가중 아이디어로, 크로스모달 검색·매칭 임베딩 학습에 이식 가능하다.

**태그**: ssl-backbone, metric-learning, image-retrieval, correspondence

---

### [Decodable but Not Detectable: A Leakage Fingerprint for Near-OOD Benchmarks](https://arxiv.org/abs/2607.19393)

**한 줄 요약**: near-OOD 벤치마크의 라벨 누수를 잡아내는 "leak fingerprint" 진단과, 오염 제거·재학습으로 AUROC를 0.326→0.911로 되돌린 프로토콜 교정.

**핵심 기여**: 문서 벤치마크에서 OOD 검출기를 감사하다 chance(0.5) 이하 AUROC 0.326이 나온 원인이, 지정된 "OOD" 클래스가 실은 모델이 학습한 in-distribution 클래스였던 벤치마크 누수임을 밝혔다. 이를 "supervised decodability는 거의 완벽(AUROC≈1)한데 unsupervised detection은 0.65 이하로 붕괴"라는 leak fingerprint로 정식화하고, ResNet-50·ViT-B/16, CIFAR-10/100의 52개 통제 설정(누수 20·정상 32)에서 임베딩 공간 기준 민감도 18/20·특이도 31/32로 검증했다. 24개 표준 near/far OOD 쌍 감사에서는 단 하나(난이도 높은 CIFAR-100 vs 10)에만 반응해 특이도를 확인했다.

**실무 관련성**: 이상·OOD 탐지 파이프라인을 평가할 때 벤치마크 오염을 자동 진단하는 도구로, anomaly/OOD detection 실험의 신뢰성 확보에 직접 쓸 수 있다.

**태그**: anomaly-detection, dataset-benchmark, image-embedding

---

### [Look Less, Think Faster: Joint Token-Compute Adaptation for Multimodal LLMs](https://arxiv.org/abs/2607.20357)

**한 줄 요약**: 시각 토큰 수와 LLM 연산량을 입력·예산에 맞춰 함께 조절하는 통합 적응 추론(SmartVL)으로 MLLM의 정확도-효율 Pareto를 개선.

**핵심 기여**: 기존 MLLM 가속이 시각 토큰 프루닝, LLM 레이어/헤드 스킵을 각각 독립적으로 다뤄 "연산 자원을 입력 내용에 따라 차원 간 동적으로 배분해야 한다"는 결합을 놓친다고 지적한다. SmartVL은 정보성 시각 토큰을 고르는 vision-side controller와 LLM 연산을 조절하는 compute controller를 공유 budget encoding과 미분가능 latency estimator로 연결해, 목표 예산을 만족하도록 두 컨트롤러를 end-to-end로 협조 학습시킨다. 여러 MLLM 벤치마크에서 기존 적응 기법을 앞서는 정확도-효율 프론티어를 보였다.

**실무 관련성**: VLM/파운데이션 모델을 예산 제약 하에 배포할 때 토큰 압축과 연산 스킵을 함께 스케줄링하는 실무 최적화로, 경량화·효율 추론 관심사에 부합한다.

**태그**: vlm, efficient-inference, foundation-model

---

### [Detect Early, Escalate Rarely: Anytime Detection of AI-Generated Video from the Compressed Bitstream](https://arxiv.org/abs/2607.19476)

**한 줄 요약**: 픽셀 디코딩 없이 코덱 비트스트림의 모션 필드를 파싱해 AI 생성 영상을 스트리밍으로, anytime-valid하게 조기 판별.

**핵심 기여**: AI 생성 영상 탐지를 오프라인 1회 스코어링이 아닌 streaming perception으로 재정식화하고, 코덱이 이미 비트스트림에 써놓은 모션 필드를 픽셀 forward 없이 파싱해 점수화한다. 누적량이 단조라 하나의 end-calibrated 임계값이 데이터 의존 결정 시점에서 anytime-valid하며(매 prefix 재보정은 그렇지 않음), escalation(무거운 모델로의 지연 판단)은 닫힌 형태로 비용이 매겨진다. GenVidBench에서 코덱 단계만으로 픽셀 CNN 대비 5자릿수 적은 연산(CPU)으로 full-length AUC 0.64를 얻고, 15% 클립을 defer하면 7배 적은 연산으로 정확도 0.75→0.78로 오른다(신 검출기 제안이 아니라 재정식화·보증·프론티어가 기여).

**실무 관련성**: 딥페이크·생성물 판별을 저비용·실시간 스트리밍으로 배포하는 관점을 제시해, 위조 탐지 서비스의 연산 예산·조기 판단 설계에 참고된다.

**태그**: forgery-detection, efficient-inference, video

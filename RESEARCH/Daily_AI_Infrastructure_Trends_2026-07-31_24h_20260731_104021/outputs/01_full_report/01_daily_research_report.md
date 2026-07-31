# Daily AI Infrastructure Trends - 2026-07-31 최근 24시간

## 연구 범위

- 핵심 창: 2026-07-30 01:23 UTC부터 2026-07-31 01:23 UTC
- 누락 복구: 최근 7일
- SNS 문맥: 최근 30일, X/Twitter 제외
- 검증 결과: verified 5, unresolved 3, refuted 0
- 합성 근거: `outputs/verified_claims.json`의 verified claim만 사용

## 한눈에 보는 변화

새 자료는 시드 글의 harness engineering 개념을 세 방향으로 확장한다. 첫째, skill portfolio와 agent 협업 자체가 harness-time scaling 대상이 된다. 둘째, agent의 권한·memory·공급망은 모델 바깥의 강제 가능한 정책 계층으로 이동한다. 셋째, AI infrastructure 최적화는 benchmark 숫자 하나가 아니라 workload와 topology, correctness를 함께 묶는 반복 검증 과정이 된다.

## 1. Self-evolving harness와 harness-time scaling

`clm_001` - 최근 자료에서 agent harness는 고정 glue code가 아니라 skill routing, evaluation, verification, memory, infrastructure optimization을 함께 다루는 동적 운영 계층으로 취급되고 있다.

시드 글은 context, tools, memory, evaluation, execution control을 모델 외부의 최적화 표면으로 설명한다. SKIMIX는 이를 skill retrieval·routing·evolution과 multi-agent refinement로 확장한다. Asari는 동일한 구조를 inference infrastructure에 적용해 discover-build-evaluate-verify-self-improve loop를 운영한다고 설명한다. 서로 다른 출처가 공통으로 보여주는 핵심은 “모델이 스스로 좋아진다”가 아니라 “모델 주위의 control loop가 측정과 검증을 거쳐 변한다”는 것이다. (`src_001`, `src_002`, `src_007`)

## 2. 개선보다 먼저 평가 프로토콜

`clm_002` - harness 개선 효과는 agent 수나 반복 횟수에 따라 단조롭게 증가한다고 볼 수 없으며, matched-budget baseline과 held-out·trace-level 평가가 없으면 개선을 과대평가할 수 있다.

SKIMIX는 open-ended reasoning에서는 협업 효과가 있지만 multiple-choice task에서는 제한적이거나 음의 효과가 있고, agent-count scaling도 비단조적이라고 보고한다. Asari는 noisy end-to-end evaluation에서 matched baseline, 통계 분석, anti-cheating check, output-distribution matching을 사용한다고 설명한다. 별도의 protocol-validity 연구와 공개 평가 코드는 aggregate score가 execution path와 budget 차이를 숨길 수 있음을 보완한다. 실무적으로는 harness PR마다 sealed task, 동일 inference budget, trace diff, rollback 기준을 함께 저장해야 한다. (`src_002`, `src_007`, `src_008`, `src_009`)

## 3. Model 외부의 production control plane

`clm_003` - production agent의 신뢰성은 model 내부 판단만으로 보장할 수 없고, 권한·sandbox·공급망·memory write·감사 가능성을 model 외부의 강제 가능한 control plane으로 분리해야 한다.

NVIDIA는 access control, sandbox, default-deny egress, secret isolation과 package provenance를 agent 바깥에서 강제해야 한다고 설명한다. CNCF의 NRI 방식은 같은 원칙을 container runtime 공급망 검증에 적용한다. ProofAgent는 capability와 production readiness를 분리하고 evaluation, context, compliance, governance를 별도 증거로 남긴다. MemTxn과 ChronoMem도 memory update와 rollback을 answer model 밖의 governance layer로 분리한다. 메모리 논문의 성능 수치는 아직 미확정이지만, 외부 강제 경계라는 설계 방향은 독립 출처에서 일치한다. (`src_004`, `src_005`, `src_006`, `src_010`, `src_011`, `src_016`)

## 4. Kubernetes runtime verification

`clm_004` - Kubernetes 공급망 검증을 API admission에만 두면 static pod와 direct kubelet path 같은 우회·가용성 공백이 남을 수 있어 container runtime 경로의 검증이 보완책이 된다.

CNCF 기술 글과 reference implementation은 containerd·CRI-O의 NRI hook에서 signature와 attestation policy를 검사한다. 이것은 admission을 대체하기보다 API server를 통과하지 않는 생성 경로까지 포함하는 defense in depth다. Agent workload는 동적으로 tool와 package를 실행하므로 runtime provenance 정책의 운영 가치가 일반 workload보다 크다. (`src_011`, `src_012`)

## 5. Cloud AI inference의 full-stack 검증

`clm_005` - AI inference 성능 최적화는 단일 kernel이나 GPU 사양이 아니라 workload, topology, runtime, scheduler, load balancer, correctness check를 포함한 full-stack 검증 문제다.

Asari는 kernel, scheduler, load balancer, configuration을 함께 최적화하며 speedup과 output distribution을 동시에 검사한다고 설명한다. NVIDIA Exemplar Cloud는 동일 GPU라도 BIOS, NUMA, NCCL, VM kernel, container 환경 차이가 결과를 바꾼다고 보고한다. OpenAI와 Google Cloud의 GPU cluster 운영 세션 역시 NVLink domain, RoCE, topology-aware scheduling, failure handling을 핵심으로 둔다. vendor 수치의 크기는 독립 재현 전까지 확정하지 않지만, measurement boundary가 전체 serving path여야 한다는 결론은 교차검증된다. (`src_007`, `src_013`, `src_014`)

## 시드 글과의 연결

시드 글의 핵심은 모델을 고정한 채 harness를 개선할 수 있다는 것이다. 이번 24시간 자료는 이 생각을 다음과 같이 운영 계약으로 바꾼다.

1. 변경 가능한 대상: skill routing, memory, evaluator, sandbox, runtime policy, infrastructure configuration.
2. 변경 허용 조건: 동일 budget, held-out task, trace audit, correctness check.
3. 배포 조건: 외부 권한 경계, provenance, rollback, observability가 있는 경우만 승격.

따라서 self-evolution은 자유로운 자기수정이 아니라 검증 가능한 control-plane change management로 보는 편이 정확하다.

## 미확정·반박된 주장

- **Unresolved:** MemTxn과 ChronoMem은 transaction·semantic rollback의 유망한 설계를 제시하지만 모두 신규 preprint이며 독립 production replication과 비용 데이터가 없다. (`src_004`, `src_005`)
- **Unresolved:** Agent Harness Distillation의 extraction·deception defense는 저자들이 work in progress라고 명시했고 독립 재현이 없다. (`src_003`)
- **Unresolved:** LinkedIn과 Digg의 공유량은 발견 우선순위 신호일 뿐 업계 채택이나 사실성 근거가 아니다. (`src_017`, `src_018`)
- **Refuted:** 없음.

## Edge AI 관찰

최근 24시간 창에서 독립 검증을 통과한 새로운 edge AI 핵심 변화는 확인되지 않았다. Cloudflare workerd release는 날짜와 원문을 확인해 기록했지만 release page만으로 Kubernetes·edge 운영 영향을 단정할 수 없어 핵심 결론에서 제외했다. (`src_015`)

## 다음 자동 조사 질문

1. SKIMIX의 비단조 scaling이 coding·tool-use benchmark에서도 재현되는가?
2. MemTxn·ChronoMem의 snapshot과 rollback 비용이 장기 세션에서 얼마나 누적되는가?
3. AHD의 harness extraction이 다른 AMAS와 closed model에서도 독립 재현되는가?
4. NRI supply-chain plugin의 production latency와 fail-open·fail-closed 운영 사례가 공개되는가?
5. Asari의 vendor-reported inference gain이 공개 코드와 독립 benchmark로 재현되는가?

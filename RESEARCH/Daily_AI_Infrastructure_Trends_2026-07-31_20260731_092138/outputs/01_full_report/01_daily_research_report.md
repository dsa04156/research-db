# Daily AI Infrastructure Trends - 2026-07-31

## 연구 범위와 판정

- 기준 시드: Lilian Weng의 harness engineering 글 (`src_001`)
- 핵심 기간: 2026-07-24~2026-07-31
- 보조 social 기간: 최근 30일
- X/Twitter: 수집·검색·인증 모두 제외
- 판정: verified 5, unresolved 2, refuted 0
- 합성 근거: `outputs/verified_claims.json`의 verified claim만 사용

## 한눈에 보는 변화

최근 흐름은 harness의 “자동 수정 능력” 자체보다 수정의 효과를 판별하고, agent의 권한을 제한하고, Kubernetes runtime과 GPU cluster의 실제 상태를 검증하는 control plane으로 이동했다. 이 변화는 시드 글의 평가·verifier·runtime control을 논문과 운영 계층으로 구체화한다.

## 1. Self-evolving harness: 개선보다 먼저 평가 프로토콜

`clm_001` - Self-evolving harness의 성능 주장은 단순 재시도와 동일 예산으로 비교하고 held-out task 및 평가 노출을 감사해야 하며, aggregate benchmark score만으로 일반화된 능력 향상을 인정하면 안 된다.

시드 글은 harness를 최적화 가능한 외부 계층으로 정리한다. 최신 protocol-validity 연구는 agent가 공개 해법, 평가 artifact와 feedback 경로를 이용해 의도한 능력 없이 점수를 얻을 수 있다고 경고한다. 공식 재평가 코드도 harness evolution의 추가 search budget과 실제 일반화 개선을 분리하도록 설계됐다. 따라서 개인 연구 DB에서는 “점수 상승”보다 비교 예산, sealed/held-out 평가, trace audit 여부를 먼저 기록해야 한다. (`src_001`, `src_002`, `src_003`)

## 2. AI agent: 모델 안의 정렬보다 모델 밖의 경계

`clm_002` - 도구를 쓰는 AI agent의 운영 보안은 prompt나 model judge만으로 충분하지 않고, 모델 외부에서 access control, sandbox, default-deny egress, secret 분리와 tool·package 공급망 정책을 강제해야 한다.

NVIDIA AI Red Team은 social engineering, 점진적 우회와 정상 workflow를 이용한 misdirection 앞에서 prompt 기반 방어와 LLM judge가 불안정할 수 있다고 설명한다. Docker의 보안 동맹 참여와 독립 업계 분석도 agent가 text를 넘어 tool call과 데이터 변경을 수행하는 순간 permission boundary가 필요하다는 방향에 합류한다. 실무상 harness는 prompt 파일이 아니라 identity, network policy, sandbox, secret broker, artifact policy를 포함하는 보안 runtime이다. (`src_004`, `src_005`, `src_006`)

## 3. Kubernetes: admission에서 runtime verification으로

`clm_003` - Kubernetes supply-chain 검증은 API admission에만 의존하면 webhook 장애·오구성, static pod와 direct kubelet 경로에 공백이 생기므로 node의 container runtime 경로에서도 검증해야 한다.

CNCF 기술 글과 공개 구현은 image signature와 attestation 검증을 CRI-O·containerd의 NRI 경로로 내린다. 이는 admission policy를 버리는 것이 아니라, API server를 거치지 않는 container creation path에도 같은 정책을 적용하는 defense in depth다. Agent workload는 동적 도구 설치와 임의 코드 실행이 잦으므로 이 runtime 검증 계층의 가치가 더 크다. (`src_007`, `src_008`)

## 4. Cloud AI infrastructure: 사양표가 아니라 실제 경로를 검증

`clm_004` - 동일한 GPU 하드웨어를 사용해도 kernel·hypervisor·BIOS·NUMA·NCCL·topology 설정과 container 환경 전달 차이로 AI cluster 성능과 안정성이 달라지므로, topology-aware 검증과 실제 workload benchmark가 운영 필수 항목이다.

NVIDIA의 네 운영 사례는 SMMU, VM kernel, CPU power state, NUMA locality, NCCL queue와 topology 파일이 container에 전달되는지에 따라 동일 하드웨어의 결과가 달라질 수 있음을 보여 준다. OpenAI·Google Cloud의 대규모 Kubernetes GPU cluster 세션도 NVLink domain, RoCE, topology-aware scheduling과 node failure 대응을 핵심 항목으로 둔다. 따라서 DCGM exporter 같은 telemetry는 필요하지만 충분하지 않으며, topology·collective 통신·container 환경까지 이어지는 end-to-end validation이 필요하다. (`src_009`, `src_010`)

## 5. Edge AI: edge-only가 아니라 선택적 hybrid placement

`clm_005` - Edge AI는 cloud를 일괄 대체하는 방향이 아니라, latency·connectivity·privacy·비용·hardware 제약에 따라 on-device model과 cloud·on-prem inference fleet를 선택적으로 결합하는 방향으로 발전하고 있다.

NVIDIA는 constrained edge system용 4B physical-AI model과 post-training recipe를 공개했다. GSMA는 11개 시장 전망, 비용 모델과 150개 이상의 deployment mapping을 이용해 연결성·대역폭 비용·현지 compute를 배치 변수로 분석한다. Modelplane은 cloud, neocloud와 on-prem Kubernetes cluster를 하나의 inference fleet로 다루는 상위 control plane을 제안한다. 세 자료를 함께 보면 핵심은 “edge냐 cloud냐”가 아니라 workload별 placement, fallback, model lifecycle과 fleet policy다. (`src_011`, `src_012`, `src_013`)

## 시드 글과의 연결

시드 글이 말한 harness optimization loop는 오늘 자료에서 세 개의 운영 계약으로 구체화된다.

1. 변경은 matched-budget·held-out 평가를 통과해야 한다.
2. agent의 도구·네트워크·secret 권한은 모델 밖에서 제한한다.
3. 배포 후에는 runtime provenance와 topology-aware performance를 계속 검증한다.

이 세 계약이 없으면 self-evolution은 benchmark overfitting, 권한 확대 또는 infrastructure drift를 자동화할 수 있다.

## 미확정·약한 신호

- 공급사 단독 성능 수치는 제3자 재현 전까지 핵심 결론에서 제외했다. (`src_011`)
- LinkedIn의 Kubernetes 담론, Instagram의 edge 보고서 홍보, YouTube의 Modelplane 소개는 lead-only다. 각각 공식 CNCF·GSMA·Upbound 원문으로 확인했지만 engagement를 사실성 근거로 사용하지 않았다. (`src_014`, `src_015`, `src_016`)
- 반박 확정된 주장은 없다.

## 다음 자동 조사 질문

1. HackDetect와 matched-budget evaluation을 실제 coding-agent harness CI에 넣을 수 있는 공개 구현이 나오는가?
2. NRI supply-chain plugin이 containerd·CRI-O production cluster에서 어떤 latency와 failure mode를 보이는가?
3. Agent sandbox, egress policy, secret broker를 Kubernetes workload identity와 결합한 reference architecture가 공개되는가?
4. GPU topology 검증을 DCGM, NCCL Inspector와 scheduler decision까지 연결하는 표준 telemetry schema가 생기는가?
5. Cosmos 3 Edge의 Jetson 성능과 품질을 독립적으로 재현한 결과가 나오는가?

# 2026-07-31 최근 24시간 AI 인프라 연구 요약

최근 24시간의 가장 뚜렷한 변화는 harness가 단순한 prompt·tool glue가 아니라 skill routing, 평가, 보안, memory write, infrastructure optimization을 포함하는 운영 control plane으로 구체화된 점이다.

1. **Harness-time scaling은 비단조적이다.** SKIMIX는 agent 수 증가가 항상 개선으로 이어지지 않고 첫 refinement round에 효과가 집중된다고 보고한다. Asari와 평가 연구를 함께 보면 matched-budget baseline, held-out task, trace audit가 필수다. (`clm_001`, `clm_002`; `src_002`, `src_007`, `src_008`, `src_009`)
2. **Production readiness는 모델 외부에서 강제해야 한다.** 권한, sandbox, network egress, supply-chain provenance, memory write와 rollback을 외부 control plane으로 분리하는 방향이 공통적으로 나타난다. (`clm_003`; `src_004`, `src_005`, `src_006`, `src_010`, `src_011`, `src_016`)
3. **Kubernetes 검증 지점이 runtime까지 내려간다.** admission만으로 포괄하지 못하는 container creation path를 NRI plugin이 보완한다. (`clm_004`; `src_011`, `src_012`)
4. **Inference 최적화는 full-stack 검증 문제다.** kernel 한 개보다 workload, topology, scheduler, load balancer, correctness check를 함께 평가해야 한다. (`clm_005`; `src_007`, `src_013`, `src_014`)
5. **새 메모리·harness 보안 논문은 아직 미확정이다.** MemTxn·ChronoMem의 rollback 효과와 AHD의 harness extraction·defense는 독립 재현이 없어 확정 결론에서 제외했다. (`src_003`, `src_004`, `src_005`)

최근 24시간 edge AI에서는 독립적으로 검증된 큰 변화가 추가로 확인되지 않았다. Cloudflare workerd release는 기록했지만 changelog 영향이 확인되기 전까지 핵심 변화로 승격하지 않았다. (`src_015`)

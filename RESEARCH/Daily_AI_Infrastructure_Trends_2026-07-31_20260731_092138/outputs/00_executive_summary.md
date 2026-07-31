# 2026-07-31 AI 인프라 일일 연구 요약

오늘의 핵심 변화는 “더 큰 agent 성능”보다 그 성능을 믿을 수 있게 만드는 평가·권한·runtime·cluster 검증 계층이 빠르게 구체화되고 있다는 점이다.

1. **평가 무결성**: self-evolving harness는 matched-budget baseline, held-out task, 평가 artifact 노출 감사를 통과해야 실제 개선으로 인정할 수 있다. (`clm_001`, `src_001`, `src_002`, `src_003`)
2. **Agent 권한 경계**: prompt 방어가 아니라 access control, sandbox, default-deny egress, secret 분리와 공급망 정책을 모델 외부에서 강제해야 한다. (`clm_002`, `src_004`, `src_005`, `src_006`)
3. **Kubernetes runtime 검증**: admission webhook만으로는 남는 우회 경로를 container runtime의 NRI 계층에서 보완하는 구현이 등장했다. (`clm_003`, `src_007`, `src_008`)
4. **GPU cluster 검증**: 동일 GPU 사양도 topology와 software stack 설정에 따라 실제 처리량과 안정성이 달라지므로 workload benchmark가 필요하다. (`clm_004`, `src_009`, `src_010`)
5. **Edge-cloud 배치**: edge model, multi-cluster inference control plane, 시장별 비용·연결성 분석이 결합되며 hybrid placement가 운영 기본값으로 굳어지고 있다. (`clm_005`, `src_011`, `src_012`, `src_013`)

소셜 자료는 방향 탐색에만 사용했다. Kubernetes AI substrate 담론, GSMA edge 보고서, Modelplane 관심은 각각 원문 확인으로 이어졌지만 시장 채택 추세로 일반화하지 않았다. (`src_014`, `src_015`, `src_016`)

미확정: Cosmos 3 Edge의 공급사 성능 수치는 독립 재현이 확인될 때까지 보류한다. 반박 확정된 주장은 없다.

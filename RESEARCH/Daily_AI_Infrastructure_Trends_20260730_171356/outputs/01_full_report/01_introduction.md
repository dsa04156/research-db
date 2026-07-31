# 1. 범위와 방법

이 리포트는 최근 7일 동안 공개된 self-evolving harness, AI agent 운영,
Kubernetes AI 인프라, cloud-native 플랫폼, edge AI 자료를 대상으로 한다.
논문 메타데이터·공식 RSS·GitHub 릴리스를 먼저 수집한 뒤 원문과 공개 날짜를
확인했다.

핵심 주장은 `artifacts/claim_ledger.jsonl`에 등록했으며 서로 다른 도메인
2개 이상이 지지하는지 확인했다. 프리프린트는 최신 1차 연구 원고이지만
미심사이므로 D등급으로 취급했고, 성능 수치보다 설계 방향과 운영 함의를
중심으로 종합했다.

이번 주 자료는 연구와 실무를 연결한다. 연구 쪽에서는 하네스 적응,
자기검증의 한계, 장기 실행 관찰과 메모리 보안이 함께 등장했다
([src_001](https://arxiv.org/abs/2607.26598);
[src_003](https://arxiv.org/abs/2607.24300);
[src_007](https://arxiv.org/abs/2607.26300);
[src_008](https://arxiv.org/abs/2607.27080)). 실무 쪽에서는 GitHub,
NVIDIA, Red Hat이 하네스 활용과 행동 테스트를 구체적인 엔지니어링 작업으로
설명했다
([src_004](https://github.blog/ai-and-ml/github-copilot/the-harness-is-all-you-need-mostly/);
[src_005](https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/);
[src_006](https://developers.redhat.com/articles/2026/07/30/behavioral-testing-for-ai-agents)).

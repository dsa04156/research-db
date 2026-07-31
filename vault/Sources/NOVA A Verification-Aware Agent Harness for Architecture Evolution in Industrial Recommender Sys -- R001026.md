---
type: research-source
item_id: 1026
title: "NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems"
source: "arxiv"
published: "2026-06-25T16:30:39Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.27243"
url: "https://arxiv.org/abs/2606.27243v3"
generated_by: codex-research-db
aliases:
  - "NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems"
topics:
  - "self-evolving-harness"
---

# NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems

[원문 열기](https://arxiv.org/abs/2606.27243v3)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`QEC2QW39`)
- 발행일: 2026-06-25T16:30:39Z
- 저자: Shaohua Liu, Liang Fang, Yilong Sun, Shudong Huang, Qingsong Luo, Shaoxin Liu, Xiaoyang Chen, Dongqiang Liu, Chuangang Ma, Zhenzhen Chai, Henghuan Wang, Shijie Quan, Changyuan Cui, Zhangbin Zhu, Peng Chen, Wei Xu, Lei Xiao, Haijie Gu, Jie Jiang
- 식별자: `arxiv:2606.27243`

## 요약·초록

Industrial advertising recommender systems are continually improved through architecture modifications, yet production iteration remains expert-intensive because coordinated changes to model topology, feature configuration, and interaction modules must satisfy strict interface, resource, and serving constraints. AutoML is limited to predefined search spaces, while generic coding agents verify runnability rather than recommender-specific semantic validity. Executable candidates may therefore violate architectural contracts, while the lack of structured reuse of semantic diagnostics and evaluation outcomes can lead to repeated invalid or ineffective modifications. We present NOVA, a verification-aware agent harness that organizes production architecture modification as multi-round search over concrete implementations within a fixed evaluation budget. At each round, NOVA generates multiple candidates under production constraints, rejects semantic violations, and ranks the valid survivors for local testing and offline evaluation. Across rounds, trajectory memory synthesizes semantic diagnostics, local-test outcomes, and offline metric changes into modification directions and forbidden patterns that guide subsequent search. Under the same maximum offline-evaluation budget for automated methods, NOVA achieves the highest effective pass rate, reaching 53.3% on ScaleUp and 51.7% on Literature-to-Production tasks. In a production A/B test covering 5% of traffic in an advertising system serving over one billion users, the selected Literature-to-Production candidate yields GMV gains of +1.25%, +1.70%, and +2.02% across three major pCVR objectives, with corresponding relative reductions in absolute pCVR bias of 58.8%, 66.7%, and 37.3%, respectively.

## 내 메모



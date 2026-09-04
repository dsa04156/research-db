---
type: research-source
item_id: 2566
title: "DNative-Twin: Decision Graphs and Digital Twins for Reconstructable Agentic Decisions"
source: "arxiv"
published: "2026-09-03T12:59:34Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.03787"
url: "https://arxiv.org/abs/2609.03787v1"
generated_by: codex-research-db
aliases:
  - "DNative-Twin: Decision Graphs and Digital Twins for Reconstructable Agentic Decisions"
topics:
  - "ai-agents"
---

# DNative-Twin: Decision Graphs and Digital Twins for Reconstructable Agentic Decisions

[원문 열기](https://arxiv.org/abs/2609.03787v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-03T12:59:34Z
- 저자: Junjie Pang, Zhenzhen Xie, Haoke Han, Ying He, Jing Wang, Gang Liu
- 식별자: `arxiv:2609.03787`

## 요약·초록

AI agents increasingly gather evidence, invoke tools, apply constraints, and produce decisions that people or software may commit to action. A final output alone cannot show which evidence, tool state, rule, authorization, or action path produced it. We present DNative-Twin, a graph-native digital twin that records a committed agentic decision as a typed trajectory and re-executes its decision mechanism under declared conditions. The graph links the state observed by the agent, the path it followed, and the authority behind the resulting action. The twin synchronizes this information, replays the mechanism in isolation, and compares it under controlled changes. We instantiate the framework in enterprise decision processes using three public process logs and controlled replay suites. The experiments identify a specific failure: graph structure localizes represented changes but cannot determine the consequence of an unobserved tool state. In a three-condition controlled experiment with 300 injected instances, unresolved-divergence recall increased from 0 to 0.667 when replay-contract state was added and to 1.0 when verification results were also available; the held-out set contained no critical-class instance. Across 500--5,000 BPI 2020 cases, median end-to-end time increased from 0.794 to 8.889 seconds on the reported platform. These results separate the roles of graph structure, replay context, and verification evidence in reviewing a decision mechanism.

## 내 메모



---
type: research-source
item_id: 2826
title: "RideWay: Benchmarking Efficient Task Completion for Tool-Using Language Agents"
source: "arxiv"
published: "2026-09-16T01:15:21Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.17985"
url: "https://arxiv.org/abs/2609.17985v1"
generated_by: codex-research-db
aliases:
  - "RideWay: Benchmarking Efficient Task Completion for Tool-Using Language Agents"
topics:
  - "ai-agents"
---

# RideWay: Benchmarking Efficient Task Completion for Tool-Using Language Agents

[원문 열기](https://arxiv.org/abs/2609.17985v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-16T01:15:21Z
- 저자: Qingnuan Han, Boli Fang, Mingzhi Hou, Claire Liu
- 식별자: `arxiv:2609.17985`

## 요약·초록

AI agents are usually evaluated by whether they complete a task. In interactive service settings, a successful agent can still frustrate users by asking repeated questions, performing redundant searches, or making avoidable revisions. We introduce RideWay, an efficiency-centered benchmark for ridehailing agents in a stateful tool-calling environment, together with Efficiency Utility, a success-gated metric that discounts successful trajectories for excess tool calls and user-facing turns relative to task-specific reference effort. Human paired preferences calibrate the relative penalties, reflecting an aggregate service-workflow trade-off: extra dialogue often creates visible friction, whereas extra tool use can sometimes verify constraints or preserve user intent. Across 58 tasks and 24 models, the fitted penalty for excess turns is about twice that for excess tool calls. On task-disjoint held-out preferences, Efficiency Utility achieves 78.7% accuracy overall: 90.6% when trajectories differ in turns, but chance-level accuracy when they differ solely in tool calls - the axis on which human annotators agree least. RideWay therefore makes interaction efficiency measurable alongside task success, while exposing the boundary of count-based tool-use evaluation.

## 내 메모

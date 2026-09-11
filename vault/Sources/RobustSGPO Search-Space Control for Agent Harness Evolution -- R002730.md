---
type: research-source
item_id: 2730
title: "RobustSGPO: Search-Space Control for Agent Harness Evolution"
source: "arxiv"
published: "2026-09-09T03:00:03Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.09646"
url: "https://arxiv.org/abs/2609.09646v1"
generated_by: codex-research-db
aliases:
  - "RobustSGPO: Search-Space Control for Agent Harness Evolution"
topics:
  - "self-evolving-harness"
---

# RobustSGPO: Search-Space Control for Agent Harness Evolution

[원문 열기](https://arxiv.org/abs/2609.09646v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JB29GBD5`)
- 발행일: 2026-09-09T03:00:03Z
- 저자: Zibo Zhao, Jijun Shi, Mo Zhou, Zhongyuan Wang, Shifu Bie, Yunfei Zhang, Xuanting Zhou, Xiangyu Wu, Bin Liu, Ruiming Tang, Wenwu Ou, Kun Gai
- 식별자: `arxiv:2609.09646`

## 요약·초록

Semantic-gradient-based prompt optimization (SGPO) improves agent harnesses using execution feedback, but its local update rule leaves the choice of edit scope and operation unresolved. We introduce RobustSGPO, which specifies the requested edit, constructs and checks the patch, and continues search from either the incumbent or retained snapshots. We evaluate permission scheduling, cumulative controls, and task-family transfer in the AgentX brainstorming workflow using 120 tasks, 95 runs, and 7,350 candidate attempts. Periodic $1\to2\to3$ scheduling exceeds fixed maximum permission by 0.28 test-score points. RobustSGPO increases completion on 30 held-out tasks from 60.0% to 80.0% and improves test quality from 3.77 to 4.14 under a 20-million-token budget. Category retention reduces source-task degradation after a shift, whereas random retention reaches a higher destination endpoint. Search-space control benefits quality through executable edits and alternative starting points, with measurable retention overhead.

## 내 메모



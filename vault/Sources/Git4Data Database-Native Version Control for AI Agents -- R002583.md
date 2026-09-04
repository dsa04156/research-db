---
type: research-source
item_id: 2583
title: "Git4Data: Database-Native Version Control for AI Agents"
source: "arxiv"
published: "2026-09-02T04:50:09Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.02106"
url: "https://arxiv.org/abs/2609.02106v1"
generated_by: codex-research-db
aliases:
  - "Git4Data: Database-Native Version Control for AI Agents"
topics:
  - "ai-agents"
---

# Git4Data: Database-Native Version Control for AI Agents

[원문 열기](https://arxiv.org/abs/2609.02106v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-02T04:50:09Z
- 저자: Hongshen Gou, Zuyu Zhang, Yuze Sun, Peng Xu, Feng Tian, Long Wang, Jianguo Wang
- 식별자: `arxiv:2609.02106`

## 요약·초록

Large Language Model (LLM) agents increasingly explore many candidate states of relational data in parallel, each of which should remain isolated, reproducible, and auditable, preferably through the same SQL interface used for ordinary data work. Existing tools support this requirement only partially: source-code version control does not scale to large datasets, whereas relational databases manage large data efficiently but rarely expose native branching, comparison, and merging. We present Git4Data, a database-native version-control layer for agentic workflows. Git4Data treats a database as a repository and a table as a versioned object, exposing Git-style operations (snapshot/tag, branch, diff, and merge with explicit conflict-resolution policies) through SQL extensions. Implemented in MatrixOne, a cloud-native relational database, Git4Data leverages immutable object storage and MVCC to make the cost of these operations proportional to the size of the change rather than the size of the data. On the BranchBench agentic branching workloads, Git4Data outperforms DoltDB by up to an order of magnitude. Overall, we believe this work sheds light on how relational databases can better support AI agents through efficient versioning.

## 내 메모



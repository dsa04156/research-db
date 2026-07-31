---
type: research-source
item_id: 1019
title: "Experience Graphs: The Data Foundation for Self-Improving Agents"
source: "arxiv"
published: "2026-06-29T06:02:20Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.29823"
url: "https://arxiv.org/abs/2606.29823v1"
generated_by: codex-research-db
aliases:
  - "Experience Graphs: The Data Foundation for Self-Improving Agents"
topics:
  - "self-evolving-harness"
---

# Experience Graphs: The Data Foundation for Self-Improving Agents

[원문 열기](https://arxiv.org/abs/2606.29823v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VS94UBSR`)
- 발행일: 2026-06-29T06:02:20Z
- 저자: Gang Liao, Yujia He, Abdullah Ozturk, Zhouyang Li, Ying Wang, Zhitong Guo, Hongsen Qin, Yaobin Qin, Tao Yang, Zewei Jiang, Dianshi Li, Jort Gemmeke, Jiangyuan Li, Liyuan Li, Nathan Yan, Masha Basmanova, Uladzimir Pashkevich, Matt Steiner, Pedro Pedreira, Rob Fergus, Anirudh Goyal, Carole-Jean Wu, Gaoxiang Liu, Andrew Witten, Daniel J. Abadi
- 식별자: `arxiv:2606.29823`

## 요약·초록

The database community has repeatedly advanced the state of the art by recognizing that new workloads demand new system architectures. We argue that long-horizon agentic tasks -- code generation, scientific discovery, hardware design -- are such a workload. These agents explore: they generate artifacts, execute tools, observe failures, branch, and repair over hundreds of steps. This search produces a structured object we call an experience graph: executable artifacts, tool outputs, rewards, sibling comparisons, and causal lineage. Yet existing agent frameworks treat this experience as disposable state -- JSON checkpoints and session logs that cannot be recovered after a crash, queried across users, or materialized into training data. We propose Trellis: a data foundation that treats the experience graph as first-class, governed, queryable database state. The core insight is that search over experience graphs is a database access pattern. Frontier selection is a query, cross-session reuse is vector-seeded graph retrieval, training-data extraction is a materialized view, and reconstructing what an agent knew at any past step is a time-travel query. When the database owns the experience graph, agents become stateless compute, and crash recovery, horizontal scaling, and a closed-loop training flywheel emerge as architectural byproducts. We ground the design in KernelEvolve, a production accelerator-kernel optimizer at Meta, where cross-session reuse reaches a target speedup roughly 10x faster at 52% lower token cost. More broadly, Trellis turns inference-time search from disposable computation into a durable institutional asset: logs made databases reliable; experience graphs may make agents cumulative.

## 내 메모



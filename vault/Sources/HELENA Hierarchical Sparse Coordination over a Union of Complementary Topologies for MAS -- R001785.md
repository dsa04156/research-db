---
type: research-source
item_id: 1785
title: "HELENA:Hierarchical Sparse Coordination over a Union of Complementary Topologies for MAS"
source: "arxiv"
published: "2026-08-05T09:49:30Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.04634"
url: "https://arxiv.org/abs/2608.04634v1"
generated_by: codex-research-db
aliases:
  - "HELENA:Hierarchical Sparse Coordination over a Union of Complementary Topologies for MAS"
topics:
  - "ai-agents"
---

# HELENA:Hierarchical Sparse Coordination over a Union of Complementary Topologies for MAS

[원문 열기](https://arxiv.org/abs/2608.04634v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-05T09:49:30Z
- 저자: Zhifang Mao, Linyao Zheng, Xuhang Shi, Xiuquan Hou
- 식별자: `arxiv:2608.04634`

## 요약·초록

LLM-based multi-agent systems (MAS) typically optimize a single topology, restricting reasoning to a narrow trajectory and limiting comprehensive analytical capacity. Naively merging multiple topologies into a composite graph introduces redundant noise propagation across irrelevant connections, degrading solution quality. To address this dilemma, we propose \textbf{Hierarchical Sparse Coordination over a Union of Complementary Topologies for MAS (HELENA)}, a multi-agent framework that balances diverse reasoning paths with sparse task-dependent execution. \helena{} constructs a union MAS graph from complementary candidate topologies selected via Monte Carlo Tree Search and Determinantal Point Process, broadening the reasoning trajectory for comprehensive analysis of complex problems. A Hierarchical Sparse Coordination module then activates only a sparse subgraph at each step while agents exchange compressed latent briefs to suppress redundant noise propagation. Finally, a Local Self-Refinement stage identifies decision units with discrepancy evidence and rewrites them only when contrastive evidence simultaneously confirms a reliable solution-side failure and a challenger-side improvement. Experiments across eight benchmarks show that \helena{} achieves state-of-the-art results on all benchmarks, with an average gain of \pctup{3.47} over the strongest baseline and up to \pctup{10.34} on MMLU-Pro, achieving larger improvements on harder benchmarks at a reasonable additional cost.

## 내 메모



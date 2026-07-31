---
type: research-source
item_id: 1245
title: "Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems"
source: "openalex"
published: "2026-06-11"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.12950"
url: "https://arxiv.org/abs/2606.12950"
generated_by: codex-research-db
aliases:
  - "Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems"
topics:
  - "ai-agents"
---

# Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2606.12950)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`5CN6N8R7`)
- 발행일: 2026-06-11
- 저자: Jinghao Wang, X J Zhou, Xiaoyang Sun, Yihui Zhang, Yilong Li, Tianyu Wo, Xu Wang, Chunming Hu, Renyu Yang
- 식별자: `arxiv:2606.12950`

## 요약·초록

Large Language Model based Multi-Agent Systems (LLM-MAS) have emerged as a powerful paradigm for tackling complex tasks by breaking them into collaborative workflows of specialized LLM-powered agents. However, deploying such multi-agent workloads at scale poses significant system challenges. Each user query spawns an iterative pipeline of LLM calls, greatly amplifying resource consumption compared to single-turn queries. In resource-constrained cloud settings, these workflows face non-deterministic and input-dependent costs at decode stage, heavy-tailed multi-model requirements with memory fragmentation and over-provisioning, and cross-cluster scheduling trade-offs. We present Maestro, a workload-aware scheduling system designed for LLM-MAS serving under strict GPU budgets. Maestro explicitly leverages agent semantics and roles: it predicts the output length and memory usage of each stage and uses this prediction to drive a hierarchical scheduler. At the node level, Maestro enables dynamic multi-model co-location via hierarchical weight caching and elastic memory provisioning. At the cluster level, it performs latency-aware routing to avoid cold-start delays and memory overloads. At the global level, it enforces workflow-aware prioritization to minimize head-of-line blocking for interactive tasks. Across prototype experiments and trace-driven simulations, Maestro reduces KV-reservation HBM by 67.2% and improves high-contention SLO attainment over EDF by 23.6 percentage points.

## 내 메모



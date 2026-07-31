---
type: research-source
item_id: 1368
title: "A Delta-Aware Orchestration Framework for Scalable Multi-Agent Edge Computing"
source: "arxiv"
published: "2026-04-22T02:54:35Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.20129"
url: "https://arxiv.org/abs/2604.20129v1"
generated_by: codex-research-db
aliases:
  - "A Delta-Aware Orchestration Framework for Scalable Multi-Agent Edge Computing"
topics:
  - "edge-computing"
  - "ai-agents"
---

# A Delta-Aware Orchestration Framework for Scalable Multi-Agent Edge Computing

[원문 열기](https://arxiv.org/abs/2604.20129v1)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MQFAVE8C`)
- 발행일: 2026-04-22T02:54:35Z
- 저자: Samaresh Kumar Singh, Joyjit Roy
- 식별자: `arxiv:2604.20129`

## 요약·초록

The Synergistic Collapse occurs when scaling beyond 100 agents causes superlinear performance degradation that individual optimizations cannot prevent. We observe this collapse with 150 cameras in Smart City deployment using MADDPG, where Deadline Satisfaction drops from 78% to 34%, producing approximately $180,000 in annual cost overruns. Prior work has addressed each contributing factor in isolation: exponential action-space growth, computational redundancy among spatially adjacent agents, and task-agnostic hardware scheduling. None has examined how these three factors interact and amplify each other. We present DAOEF (Delta-Aware Orchestration for Edge Federations), a framework that addresses all three simultaneously through: (1) Differential Neural Caching, which stores intermediate layer activations and computes only the input deltas, achieving 2.1x higher hit ratios (72% vs. 35%) than output-level caching while staying within 2% accuracy loss through empirically calibrated similarity thresholds; (2) Criticality-Based Action Space Pruning, which organizes agents into priority tiers and reduces coordination complexity from O(n2) to O(n log n) with less than 6% optimality loss; and (3) Learned Hardware Affinity Matching, which assigns tasks to their optimal accelerator (GPU, CPU, NPU, or FPGA) to prevent compounding mismatch penalties. Controlled factor-isolation experiments confirm that each mechanism is necessary but insufficient on its own: removing any single mechanism increases latency by more than 40%, validating that the gains are interdependent rather than additive. Across four datasets (100-250 agents) and a 20-device physical testbed, DAOEF achieves a 1.45x multiplicative gain over applying the three mechanisms independently. A 200-agent cloud deployment yields 62% latency reduction (280 ms vs. 735 ms), sub-linear latency growth up to 250 agents.

## 내 메모



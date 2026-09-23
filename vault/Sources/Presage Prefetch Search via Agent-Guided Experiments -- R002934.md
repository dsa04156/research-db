---
type: research-source
item_id: 2934
title: "Presage: Prefetch Search via Agent-Guided Experiments"
source: "arxiv"
published: "2026-09-18T22:56:39Z"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "arxiv:2609.22636"
url: "https://arxiv.org/abs/2609.22636v1"
generated_by: codex-research-db
aliases:
  - "Presage: Prefetch Search via Agent-Guided Experiments"
topics:
  - "self-evolving-harness"
---

# Presage: Prefetch Search via Agent-Guided Experiments

[원문 열기](https://arxiv.org/abs/2609.22636v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3PNKVFUT`)
- 발행일: 2026-09-18T22:56:39Z
- 저자: Matthew Giordano, Parthasarathy Ranganathan, Baris Kasikci, Akanksha Jain
- 식별자: `arxiv:2609.22636`

## 요약·초록

Data prefetching is an established technique to mitigate cache miss latency and keep the processor saturated with data. Software exists in a unique position to issue prefetches, having algorithmic knowledge of the workload at hand. However, inserting software prefetches is a time consuming, unpredictable task, with a high degree of sensitivity to microarchitecture or future code changes. While several compiler- and FDO-based approaches insert and tune software prefetches automatically, they use heuristics that do not generalize and do not consider issues that arise in large codebases. In this paper, we show that semantic understanding and reasoning about a program is a vital component in inserting effective software prefetches. We also identify that prefetching at the scale of large codebases poses new challenges, including prefetch codependence and interference. To remedy this, we build Presage, a system that leverages the semantic reasoning of Large Language Models to insert effective software prefetches. Presage processes a workload through a custom agent harness specifically designed to navigate the wide space of potential prefetches on large-scale workloads. First, a proposer agent with access to performance metrics identifies promising software prefetching candidates. Then, several long-horizon optimizer agents optimize prefetching candidates in a loop, working towards discovery of performance wins. Finally, a combiner agent handles composition of individually effective prefetches. Through this method, Presage is able to insert prefetches that improve performance by a geomean of 10% across 81 workloads by exploring tens of different prefetching alternatives per workload, including a 2.7% runtime reduction on SPEC CPU 2026 where prior SOTA fails. When compared against prior SOTA on its evaluation suite, Presage achieves a geomean runtime improvement of 17% compared to SOTA's 10%.

## 내 메모

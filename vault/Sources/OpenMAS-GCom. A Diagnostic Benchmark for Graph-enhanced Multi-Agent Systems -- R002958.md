---
type: research-source
item_id: 2958
title: "OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems"
source: "arxiv"
published: "2026-09-18T09:17:20Z"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "arxiv:2609.21527"
url: "https://arxiv.org/abs/2609.21527v1"
generated_by: codex-research-db
aliases:
  - "OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems"
topics:
  - "ai-agents"
---

# OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2609.21527v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-18T09:17:20Z
- 저자: Kairui Yang, Xunkai Li, Kaixiang Zhang, Minghao An, Zekai Chen, Yuxuan Ba, Rong-Hua Li
- 식별자: `arxiv:2609.21527`

## 요약·초록

Graph-enhanced multi-agent systems (G-MAS) coordinate large language model agents through communication graphs and role assignments, which determine how agents exchange information and divide responsibilities. However, final-score comparisons across systems combine differences in models, communication patterns, roles, and computation costs, making performance differences difficult to attribute to specific communication structures, role assignments, and information flows. To address this evaluation attribution problem, we introduce OpenMAS-GCom, a benchmark for diagnosing how these components affect G-MAS performance through controlled interventions. We represent systems through collaboration units, communication links, shared intermediate information, and execution rules. OpenMAS-GCom compares original systems with versions modified by changing one component while keeping tasks, models, prompts, and budget limits fixed. We rewire communication edges, remove specialist or critic agents, replace intermediate messages with incorrect content, and disable workers during execution. The benchmark evaluates 17 single-agent, ordinary multi-agent, and graph-enhanced configurations on 29 datasets across six domains. We add 400 G-MAS-Complex tasks requiring agents to combine information from multiple documents, resolve conflicting records, and return specified values with source identifiers. Experiments show larger mean losses after specialist removal than after critic removal, different performance degradation under incorrect messages and worker failures despite similar original scores, and different configurations achieving the highest accuracy and accuracy per token on G-MAS-Complex.

## 내 메모

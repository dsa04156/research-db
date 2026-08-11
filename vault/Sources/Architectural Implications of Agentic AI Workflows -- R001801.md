---
type: research-source
item_id: 1801
title: "Architectural Implications of Agentic AI Workflows"
source: "openalex"
published: "2026-08-05"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.04458"
url: "https://arxiv.org/abs/2608.04458"
generated_by: codex-research-db
aliases:
  - "Architectural Implications of Agentic AI Workflows"
topics:
  - "ai-agents"
---

# Architectural Implications of Agentic AI Workflows

[원문 열기](https://arxiv.org/abs/2608.04458)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`G9TMANW3`)
- 발행일: 2026-08-05
- 저자: Jirong Yang, Peizhe Liu, Chaojie Zhang, Jovan Stojkovic
- 식별자: `arxiv:2608.04458`

## 요약·초록

Agentic AI is emerging in datacenters, but its architectural implications remain unexplored. We organize agentic workflows in a taxonomy and present its first architectural characterization with a production study at Microsoft Azure and a controlled study of open-source frameworks. We show that agentic execution is fragmented and heterogeneous. Requests expand into a workflow of LLM inferences, tool invocations, and orchestration decisions that repeatedly cross the CPU-GPU boundary. Our taxonomy explains how this fragmentation turns into resource demand. As orchestration and tools run on the host, the CPU sits on the critical path. Execution structure sets the load over time, which stays low with sudden spikes. Model composition sets how evenly the workflow uses the GPUs. Diversity in tasks and tools widens this range even further. These characteristics expose architectural mismatches of conventional uniform servers. Fragmented execution strands CPU and GPU capacity despite bursty demand. Different software roles make homogeneous CPU provisioning inefficient. Finally, multiplexing many agents onto shared cores degrades microarchitectural locality. Guided by our findings, we derive implications for agentic servers and examine them through Agora, our prototype for commodity servers. Agora dynamically harvests idle CPU cores for co-located throughput work, while protecting agentic tail latency against tool spikes. It oversubscribes GPU memory by placing more agents on each GPU, prefetching the next agent's state to hide swap latency. To match the machine to the heterogeneous roles, Agora pools cores by role and applies affinity-aware scheduling to restore locality. It automatically tunes mechanisms to the workload. Agora improves utilization and server throughput while preserving agent tail latency. Our insights also identify key directions for future server architectures for agentic AI.

## 내 메모



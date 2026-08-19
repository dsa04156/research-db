---
type: research-source
item_id: 2099
title: "FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution"
source: "arxiv"
published: "2026-08-17T06:22:53Z"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "arxiv:2608.16157"
url: "https://arxiv.org/abs/2608.16157v1"
generated_by: codex-research-db
aliases:
  - "FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution"
topics:
  - "ai-agents"
---

# FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution

[원문 열기](https://arxiv.org/abs/2608.16157v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-17T06:22:53Z
- 저자: Shuo Yang, Xiaoze Fan, Melissa Pan, Haocheng Xi, Zhe Wang, Shanlin Sun, Kurt Keutzer, Song Han, Matei Zaharia, Chenfeng Xu, Ion Stoica
- 식별자: `arxiv:2608.16157`

## 요약·초록

Frontier open-weight models are increasingly available, but serving them still largely assumes datacenter infrastructure. We present FreeToken, an edge-native MoE serving system that treats a personal machine not as a small GPU, but as a unified, elastic inference platform. FreeToken co-designs the full serving stack, including model layout and loading, expert residency, CPU--GPU execution, agentic state reuse, and runtime memory management, around two realities of local AI: agent workloads continuously change their execution pattern, and edge hardware exposes heterogeneous resources whose balance differs from machine to machine. Rather than committing to a fixed offloading strategy, FreeToken continuously maps computation and model state onto the resources actually available. FreeToken supports more than 20 MoE models and real coding and tool-using agents across hardware ranging from an 8GB laptop GPU to a single workstation GPU. More importantly, it changes what these machines can practically serve, from a 35B model on a laptop to a 284B model on a gaming desktop and the 753B GLM-5.2 on a single workstation GPU. FreeToken turns open weights into deployable local software, making the machines users already own a practical platform for frontier-scale intelligence. We release the system at flashml.ai.

## 내 메모



---
type: research-source
item_id: 1209
title: "ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System"
source: "arxiv"
published: "2026-02-14T09:26:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2602.13692"
url: "https://arxiv.org/abs/2602.13692v3"
generated_by: codex-research-db
aliases:
  - "ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System"
topics:
  - "kubernetes"
---

# ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System

[원문 열기](https://arxiv.org/abs/2602.13692v3)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VAV5NPI7`)
- 발행일: 2026-02-14T09:26:41Z
- 저자: Hao Kang, Ziyang Li, Weili Xu, Xinyu Yang, Yinfang Chen, Junxiong Wang, Beidi Chen, Tushar Krishna, Chenfeng Xu, Simran Arora
- 식별자: `arxiv:2602.13692`

## 요약·초록

Large language models(LLMs) are now used to power complex multi-turn agentic workflows. Existing systems run agentic inference by loosely assembling isolated components: an LLM inference engine (e.g., vLLM) and a tool orchestrator (e.g., Kubernetes). Although agentic workflows involve multiple LLM and tool requests, these systems schedule and allocate resources separately on a per-request basis, without end-to-end knowledge of the workflow. This leads to sub-optimal management of KV cache and tool execution environments. To address the challenges, we propose ThunderAgent, a fast, simple, and program-aware agentic inference system. We first abstract agentic workflows as LLM Programs, enabling a unified view of heterogeneous resources, including KV caches, system states, and external tool assets such as disk memory and network ports. Built upon this abstraction, ThunderAgent introduces a program-aware scheduler and a tool resource manager designed to maximize KV cache hit rates, mitigate memory imbalances, and enable asynchronous environment preparation. Evaluations across coding, routing, and scientific discovery agents demonstrate that ThunderAgent achieves 1.5-3.6x throughput improvements in serving, 1.8-3.9x in RL rollout, and up to 4.2x disk memory savings compared to state-of-the-art inference systems. To facilitate reproducibility and support future development, we open-source the system implementations of the whole ThunderAgent at: https://github.com/Agentic-Kinetics/ThunderAgent.

## 내 메모



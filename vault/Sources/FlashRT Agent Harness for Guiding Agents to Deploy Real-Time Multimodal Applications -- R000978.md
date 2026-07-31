---
type: research-source
item_id: 978
title: "FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications"
source: "arxiv"
published: "2026-07-20T17:12:28Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.18171"
url: "https://arxiv.org/abs/2607.18171v1"
generated_by: codex-research-db
aliases:
  - "FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications"
topics:
  - "self-evolving-harness"
---

# FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications

[원문 열기](https://arxiv.org/abs/2607.18171v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`REEVCRPM`)
- 발행일: 2026-07-20T17:12:28Z
- 저자: Krish Agarwal, Zhuoming Chen, Yanyuan Qin, Zhenyu Gu, Atri Rudra, Beidi Chen
- 식별자: `arxiv:2607.18171`

## 요약·초록

Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a new application requires hand-crafting an efficient implementation. We present FlashRT, an agent harness that guides coding agents to lift simple developer-written reference implementations into optimized multi-GPU deployments that flexibly weigh target metrics like latency and throughput. Using a new chain-of-program paradigm, FlashRT directs a generic coding agent through a multi-pass transformation process where an agent transforms the reference into an intermediate representation (IR) to capture data dependencies and persistent-state scopes, validates this IR via a sequential interpreter, and performs static analyses to identify candidate transformations. Then, the agent iteratively implements, verifies, and benchmarks each candidate under a measurement-gated optimization loop to produce effective deployments that span different hardware budgets. Across various applications, including video world models and multimodal LLMs, FlashRT converts reference implementations into highly efficient deployments, delivering up to ~70x latency reduction and 2.8x throughput improvement on NVIDIA B200 GPUs. On AMD MI355X GPUs, FlashRT matches the peak latency reduction while increasing peak throughput improvement to 3.6x, demonstrating that agent-driven optimization can be more scalable on platforms with less mature expert optimization. In fact, for Qwen3-Omni text-to-audio inference, FlashRT reduces response latency by 65% compared to the expert vLLM-Omni implementation on AMD MI355X.

## 내 메모



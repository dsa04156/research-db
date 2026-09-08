---
type: research-source
item_id: 2615
title: "MaxKernel: Agentic Kernel Generation for TPUs"
source: "arxiv"
published: "2026-09-03T22:22:37Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.04523"
url: "https://arxiv.org/abs/2609.04523v1"
generated_by: codex-research-db
aliases:
  - "MaxKernel: Agentic Kernel Generation for TPUs"
topics:
  - "ai-agents"
---

# MaxKernel: Agentic Kernel Generation for TPUs

[원문 열기](https://arxiv.org/abs/2609.04523v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-03T22:22:37Z
- 저자: Shangkun Wang, Nina Cai, Charles Hoong, Julian Walker, Gerson Kroiz, George Vanica, Deepak Patil, Andi Gavrilescu, Hassan Sipra, Sethu Sankaran
- 식별자: `arxiv:2609.04523`

## 요약·초록

Designing and authoring high-performance custom kernels for accelerators is a complex task that requires deep hardware-level expertise. Large Language Models (LLM) can be leveraged together with real-time compiler feedback to build agentic systems for kernel generation. In this work, we present MaxKernel, a multi-agent system that implements three distinct paradigms for TPU kernel development: (1) a Human-in-the-Loop (HITL) agent for collaborative, step-by-step design; (2) an Autonomous (Auto) agent that executes a fully automated, metric/trace-driven optimization loop; and (3) a Graph-Based Autonomous Search that scales the Auto agent for global exploration of the design space. All three paradigms leverage a shared pool of specialized sub-agents to handle planning, implementation, self-debugging, testing, and hardware profiling. We evaluate MaxKernel on JaxBench, a comprehensive suite of 50 diverse kernel tasks for TPUs, alongside complex, real-world workloads from state-of-the-art open-source models. We demonstrate that MaxKernel consistently generates highly optimized implementations, matching expert hand-tuned baselines and delivering significant performance across the benchmark. Our agent is open-sourced and available https://github.com/AI-Hypercomputer/accelerator-agents/tree/main/MaxKernel.

## 내 메모



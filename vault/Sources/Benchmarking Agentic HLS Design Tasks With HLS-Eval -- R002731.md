---
type: research-source
item_id: 2731
title: "Benchmarking Agentic HLS Design Tasks With HLS-Eval"
source: "arxiv"
published: "2026-09-08T23:12:36Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.09526"
url: "https://arxiv.org/abs/2609.09526v1"
generated_by: codex-research-db
aliases:
  - "Benchmarking Agentic HLS Design Tasks With HLS-Eval"
topics:
  - "ai-agents"
---

# Benchmarking Agentic HLS Design Tasks With HLS-Eval

[원문 열기](https://arxiv.org/abs/2609.09526v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-08T23:12:36Z
- 저자: Stefan Abi-Karam, Callie Hao
- 식별자: `arxiv:2609.09526`

## 요약·초록

Large language models (LLMs) and AI agents are increasingly explored for hardware design, including high-level digital design. While most work targets code generation and editing for hardware description languages (HDLs), our prior work introduced HLS-Eval, an open-source benchmark for evaluating LLMs on high-level synthesis (HLS) design tasks. Those evaluations, however, focused on zero-shot generation and editing, leaving open how agents achieve HLS design tasks. We therefore extend HLS-Eval with an agentic evaluation flow built on the open-source mini-swe-agent framework. The flow lets HLS design agents use file-editing tools, invoke a C++ compiler for self-verification, and iteratively refine designs during inference, while logging agent traces for analysis of cost, token usage, and iteration count. We present initial results on the existing HLS-Eval benchmarks. In our initial evaluation, we find open-source LLMs paired with an agentic harness solve every simple HLS code generation task in our evaluation, underscoring the need to expand benchmark difficulty as model capabilities advance. Analyzing traces from passing and failing runs, we show how model size, token usage, and trajectory length relate to design pass rates. These results establish a foundation for agentic HLS design and motivate harder benchmarks and new agentic tooling as model capabilities progress.

## 내 메모



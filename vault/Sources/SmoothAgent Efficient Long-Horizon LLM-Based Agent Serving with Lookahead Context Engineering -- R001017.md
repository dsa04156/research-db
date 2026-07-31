---
type: research-source
item_id: 1017
title: "SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering"
source: "arxiv"
published: "2026-06-30T20:27:49Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.00151"
url: "https://arxiv.org/abs/2607.00151v1"
generated_by: codex-research-db
aliases:
  - "SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering"
topics:
  - "self-evolving-harness"
---

# SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering

[원문 열기](https://arxiv.org/abs/2607.00151v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MXWNETZD`)
- 발행일: 2026-06-30T20:27:49Z
- 저자: Zaifeng Pan, Qianxu Wang, Zhengding Hu, Chang Chen, Yue Guan, Yanbo Zhou, Steven Swanson, Yufei Ding
- 식별자: `arxiv:2607.00151`

## 요약·초록

LLM-based agents execute multi-turn workflows with continuously growing contexts, where LLM calls are interleaved with tool invocations and environment feedback. To maintain model quality, modern agent frameworks rely on context engineering strategies such as offloading, reduction, and isolation to control the context length. However, these strategies introduce significant context transformation overhead: each transformation invalidates existing KV caches and triggers re-prefill, leading to increased time-to-first-token (TTFT). In this paper, we identify that context transformations are segment-decomposable, where the transformation of a prefix is independent of future tokens. This property enables transformations to be executed ahead of time. Based on this insight, we propose a lookahead programming model that allows agent frameworks to express context transformations as asynchronous operations without modifying their execution logic. The runtime proactively executes these transformations and prepares transformed KV caches in advance, enabling direct context replacement without blocking. We further design a lookahead-aware scheduler in LLM serving systems to support these asynchronous requests alongside latency-critical workloads with controlled interference. We implement our approach to support representative context engineering strategies and integrate it into existing agent frameworks and LLM serving systems. Experiments show that our approach effectively eliminates transformation overhead and reduces TTFT by up to 11.9x.

## 내 메모



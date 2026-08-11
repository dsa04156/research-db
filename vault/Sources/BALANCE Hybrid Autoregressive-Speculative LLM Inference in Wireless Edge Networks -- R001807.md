---
type: research-source
item_id: 1807
title: "BALANCE: Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks"
source: "arxiv"
published: "2026-08-06T11:57:36Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.05926"
url: "https://arxiv.org/abs/2608.05926v1"
generated_by: codex-research-db
aliases:
  - "BALANCE: Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks"
topics:
  - "edge-computing"
---

# BALANCE: Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks

[원문 열기](https://arxiv.org/abs/2608.05926v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`I8SD44V2`)
- 발행일: 2026-08-06T11:57:36Z
- 저자: Guanqiao Qu, Shuo Chen, Qian Chen, Kin K. Leung, Xianhao Chen
- 식별자: `arxiv:2608.05926`

## 요약·초록

Edge inference is a promising paradigm to provide large language model (LLM) inference services in next-generation mobile networks. LLM inference mainly relies on two approaches: Autoregressive decoding (AD) generates output tokens sequentially, resulting in long latency; Speculative decoding (SD) accelerates inference by using a small language model (SLM) to generate multiple draft tokens for LLM verification, but incurs extra memory costs. Due to this latency-memory tradeoff, neither approach alone can efficiently serve users with heterogeneous demands under limited edge computing resources. To address this challenge, we propose a hybrid autoregressive-speculative inference (BALANCE) framework for edge LLM inference. In BALANCE, an edge server hosts both an SLM and an LLM, assigns each user to AD or SD, and performs the two modes simultaneously. To maximize the number of served users, we formulate a task throughput maximization problem to jointly determine user scheduling and computing resource allocation between AD and SD under user latency requirements and server memory constraints. Since the problem is NP-hard, we develop a polynomial-time algorithm that transforms the original problem into two sub-problems and obtains a sub-optimal solution with a constant approximation guarantee. Experiments demonstrate that BALANCE consistently outperforms conventional AD and SD and significantly improves task throughput.

## 내 메모



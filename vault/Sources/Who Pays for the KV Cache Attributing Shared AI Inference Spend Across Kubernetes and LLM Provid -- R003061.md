---
type: research-source
item_id: 3061
title: "Who Pays for the KV Cache? Attributing Shared AI Inference Spend Across Kubernetes and LLM Provider Bills"
source: "arxiv"
published: "2026-09-21T17:57:40Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.24991"
url: "https://arxiv.org/abs/2609.24991v1"
generated_by: codex-research-db
aliases:
  - "Who Pays for the KV Cache? Attributing Shared AI Inference Spend Across Kubernetes and LLM Provider Bills"
topics:
  - "kubernetes"
---

# Who Pays for the KV Cache? Attributing Shared AI Inference Spend Across Kubernetes and LLM Provider Bills

[원문 열기](https://arxiv.org/abs/2609.24991v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-21T17:57:40Z
- 저자: Timothy Urista
- 식별자: `arxiv:2609.24991`

## 요약·초록

Organizations pay for AI through disconnected ledgers: Kubernetes allocations for self-hosted inference, gateway logs, and per-token bills from API providers. We present unalloc, an open-source tool that joins OpenCost, LiteLLM, OpenAI and Anthropic cost data into one exact ledger and reports the share of spend with no owner, and use it to study where attribution breaks at the seams between these systems. Five case studies run inference for real or simulate it: a vLLM-style serving simulator with paged KV memory and prefix caching; a PyTorch transformer serving a multi-tenant trace with a real KV cache; tensor- and pipeline-parallel inference on torch.distributed; the unmodified CLI against mock provider APIs; and four downstream use cases. At the seams, in a constructed multi-pod deployment scenario -- one month of synthetic OpenCost allocations, not observed billing data -- owner labels set only on LeaderWorkerSet leader pods leave 66% of that deployment's GPU bill unowned, and the natural fallback key assigns 61% of it to a Helm chart name while the headline unallocated share falls to 4%; enabling every source double counts all gateway spend; and reading one page of a billing API reports a quarter of spend. Inside a shared inference server the metering rule decides who pays: on an NVIDIA H100 running vLLM, a token meter assigns a retrieval-heavy tenant 12-14 percentage points more of the bill than an equal time-share meter at every load tested, while GPU utilization reads 97-99% across configured loads of 2 to 16 requests per second (3.7 to 26.9 completed requests per second; the configured rate counts session-initial arrivals only) and power draw tracks load. Neither meter is a ground truth; we position these results against recent Shapley-based energy attribution. Code, raw data, captured evidence, figures and the paper regenerate from the repository.

## 내 메모

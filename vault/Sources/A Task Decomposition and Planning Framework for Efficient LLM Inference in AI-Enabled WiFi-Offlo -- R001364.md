---
type: research-source
item_id: 1364
title: "A Task Decomposition and Planning Framework for Efficient LLM Inference in AI-Enabled WiFi-Offload Networks"
source: "arxiv"
published: "2026-04-23T08:05:10Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.21399"
url: "https://arxiv.org/abs/2604.21399v1"
generated_by: codex-research-db
aliases:
  - "A Task Decomposition and Planning Framework for Efficient LLM Inference in AI-Enabled WiFi-Offload Networks"
topics:
  - "edge-computing"
---

# A Task Decomposition and Planning Framework for Efficient LLM Inference in AI-Enabled WiFi-Offload Networks

[원문 열기](https://arxiv.org/abs/2604.21399v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`WV5JC2R6`)
- 발행일: 2026-04-23T08:05:10Z
- 저자: Mingqi Han, Xinghua Sun
- 식별자: `arxiv:2604.21399`

## 요약·초록

AI WiFi offload is emerging as a promising approach for providing large language model (LLM) services to resource-constrained wireless devices. However, unlike conventional edge computing, LLM inference over WiFi must jointly address heterogeneous model capabilities, wireless contention, uncertain task complexity, and semantic correlation among reasoning tasks. In this paper, we investigate LLM inference offloading in a multi-user multi-edge WiFi network, where each task can be executed locally, directly offloaded to a nearby edge access point (AP), or decomposed into multiple subtasks for collaborative execution across local and edge nodes. To this end, we propose a user-edge collaborative framework with an LLM-based planner that not only performs task decomposition but also infers subtask difficulty and expected output token length, enabling more accurate estimation of execution quality and latency on heterogeneous nodes. Based on these estimates, we further design a decomposition-aware scheduling strategy that jointly optimizes subtask assignment, execution, and aggregation under communication, queuing, and computation constraints. Simulation results show that the proposed framework achieves a better latency-accuracy tradeoff than local-only and nearest-edge baselines, reducing the average latency by $20\%$ and improving the overall reward by $80\%$. Moreover, the distilled lightweight planner approaches the performance of the large teacher model while remaining more suitable for practical edge deployment.

## 내 메모



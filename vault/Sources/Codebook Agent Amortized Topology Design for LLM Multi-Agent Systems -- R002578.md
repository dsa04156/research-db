---
type: research-source
item_id: 2578
title: "Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems"
source: "arxiv"
published: "2026-09-02T08:10:22Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.02264"
url: "https://arxiv.org/abs/2609.02264v1"
generated_by: codex-research-db
aliases:
  - "Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems"
topics:
  - "ai-agents"
---

# Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2609.02264v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-02T08:10:22Z
- 저자: Jinxi Yu, Yubei Li, Eric Hanchen Jiang, Zhi Zhang, Dong Liu, Wenxiao Zhao, Levina Li, Kai-Wei Chang, Ying Nian Wu
- 식별자: `arxiv:2609.02264`

## 요약·초록

Adapting the communication topology of an LLM multi-agent system to each query improves both accuracy and efficiency, yet current designers treat this as conditional graph generation: a variational, autoregressive, or diffusion decoder searches the $N \times N$ adjacency space, and a graph-network proxy trained on utility and a structural cost such as edge count ranks the sampled candidates. We argue that this formulation is misaligned with the problem. Empirically, topologies that survive a reward filter collapse to about six distinct graphs even when the codebook capacity grows from 8 to 64; edge count is negatively correlated with measured token consumption (Pearson $r \approx -0.4$), so sparsifying the graph makes inference more expensive; and a message-passing scorer over agent-profile nodes is adjacency-invariant whenever agents share a profile---the default configuration of published benchmarks---so it cannot rank candidates at all in that regime. These three facts motivate Codebook Agent: a vector-quantized autoencoder compresses successful topologies into a query-independent 16-entry codebook; a reward-weighted MLP maps the query embedding to a distribution over codes; and an MLP proxy that reads the flattened adjacency, regressed on measured utility and per-task normalized token cost, reranks the top decoded candidates in a single batched forward pass. With no iterative search and no message passing at test time, Codebook Agent is the most accurate method on all six benchmarks we compare (84.6 average against 83.0 for the strongest prior designer), emits a topology in 2.4 ms, and uses 21.9--33.2% fewer LLM tokens.

## 내 메모



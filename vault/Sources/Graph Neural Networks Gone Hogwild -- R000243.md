---
type: research-source
item_id: 243
title: "Graph Neural Networks Gone Hogwild"
source: "arxiv"
published: "2024-06-29T17:11:09Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.00494"
url: "https://arxiv.org/abs/2407.00494v2"
generated_by: codex-research-db
aliases:
  - "Graph Neural Networks Gone Hogwild"
topics:
  - "ai-agents"
---

# Graph Neural Networks Gone Hogwild

[원문 열기](https://arxiv.org/abs/2407.00494v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`BV6P8B34`)
- 발행일: 2024-06-29T17:11:09Z
- 저자: Olga Solodova, Nick Richardson, Deniz Oktay, Ryan P. Adams
- 식별자: `arxiv:2407.00494`

## 요약·초록

Graph neural networks (GNNs) appear to be powerful tools to learn state representations for agents in distributed, decentralized multi-agent systems, but generate catastrophically incorrect predictions when nodes update asynchronously during inference. This failure under asynchrony effectively excludes these architectures from many potential applications where synchrony is difficult or impossible to enforce, e.g., robotic swarms or sensor networks. In this work we identify "implicitly-defined" GNNs as a class of architectures which is provably robust to asynchronous "hogwild" inference, adapting convergence guarantees from work in asynchronous and distributed optimization. We then propose a novel implicitly-defined GNN architecture, which we call an 'energy GNN'. We show that this architecture outperforms other GNNs from this class on a variety of synthetic tasks inspired by multi-agent systems.

## 내 메모



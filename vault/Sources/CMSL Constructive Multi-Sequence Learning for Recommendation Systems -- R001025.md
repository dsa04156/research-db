---
type: research-source
item_id: 1025
title: "CMSL: Constructive Multi-Sequence Learning for Recommendation Systems"
source: "arxiv"
published: "2026-06-26T18:32:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3805712.3808426"
url: "https://arxiv.org/abs/2606.28533v2"
generated_by: codex-research-db
aliases:
  - "CMSL: Constructive Multi-Sequence Learning for Recommendation Systems"
topics:
  - "self-evolving-harness"
---

# CMSL: Constructive Multi-Sequence Learning for Recommendation Systems

[원문 열기](https://arxiv.org/abs/2606.28533v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`4KIZNGP5`)
- 발행일: 2026-06-26T18:32:43Z
- 저자: Zikun Cui, Renzhi Wu, Junjie Yang, Li Sheng, Jijie Wei, Linfeng Liu, Tai Guo, Tao Jia, Xiaodong Wang, Hong Li, Li Yu, Sri Reddy, Hong Yan
- 식별자: `doi:10.1145/3805712.3808426`

## 요약·초록

Sequence learning has emerged as the promising paradigm in recommendation systems, surpassing traditional Deep Learning Recommendation Models (DLRM) by capturing the temporal nuances of user behavior. However, current state-of-the-art architectures operate under a limiting analogy: they treat user history as a monolithic chronological sequence like a sentence in a Large Language Model (LLM). We observe a fundamental divergence between natural language and recommendation data: unlike the linear, logical flow of text, user history is inherently multi-faceted. A user's journey is a fragmented reflection of diverse interests, resulting in much weaker coherence between items than is found in LLM training data. This lack of structural unity leads to context pollution. In single-sequence modeling, unrelated behaviors compete for the same attention budget. This "noisy" signal dilutes the model's focus, effectively capping its ability to discern high-intent patterns from background activity. To address this, we propose Constructive Multi-Sequence Learning (CMSL), a paradigm shift from passive sequence ingestion to active "context engineering" that constructs multiple coherent sequences in latent space. CMSL leverages a learnable Sequence Construction Module to disentangle user history into "pure" thematic strands, followed by a linear attention mechanism to efficiently model these strands at scale. CMSL has been deployed across ranking and retrieval tasks and across four major surfaces at Meta.

## 내 메모



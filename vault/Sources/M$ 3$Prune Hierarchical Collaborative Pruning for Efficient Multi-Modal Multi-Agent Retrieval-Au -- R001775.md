---
type: research-source
item_id: 1775
title: "M$^3$Prune: Hierarchical Collaborative Pruning for Efficient Multi-Modal Multi-Agent Retrieval-Augmented Generation"
source: "arxiv"
published: "2026-08-06T12:44:35Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.05967"
url: "https://arxiv.org/abs/2608.05967v1"
generated_by: codex-research-db
aliases:
  - "M$^3$Prune: Hierarchical Collaborative Pruning for Efficient Multi-Modal Multi-Agent Retrieval-Augmented Generation"
topics:
  - "ai-agents"
---

# M$^3$Prune: Hierarchical Collaborative Pruning for Efficient Multi-Modal Multi-Agent Retrieval-Augmented Generation

[원문 열기](https://arxiv.org/abs/2608.05967v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-06T12:44:35Z
- 저자: Taolin Zhang, Weizi shao, Zijie Zhou, Chen Chen, Daiyang Yu, Tingyuan Hu, Chengyu Wang, Xiaofeng He
- 식별자: `arxiv:2608.05967`

## 요약·초록

Recent advances in multi-modal retrieval-augmented generation (mRAG), which augments multi-modal large language models (MLLMs) with external knowledge, have shown that collective intelligence from multiple agents can outperform a single model through effective communication. Despite their strong performance, existing multi-agent systems incur substantial token overhead and computational cost, posing challenges for large-scale deployment. To address these issues, we propose a Multi-Modal Multi-agent hierarchical communication graph PRUNING framework, termed M3Prune. M3Prune eliminates redundant communication edges both across and within modalities, improving the trade-off between task performance and token overhead. Specifically, M3Prune first performs intra-modal graph sparsification in the textual and visual modalities to identify task-critical communication links. It then constructs an inter-modal communication graph and sparsifies cross-modal connections while encouraging consistent cross-modal reasoning through a modality alignment score. Finally, it progressively prunes redundant edges to obtain an efficient hierarchical topology. Extensive experiments on both general-domain and domain-specific mRAG benchmarks show that M3Prune consistently outperforms single-agent and strong multi-agent mRAG systems while signifi- cantly improving token efficiency.

## 내 메모



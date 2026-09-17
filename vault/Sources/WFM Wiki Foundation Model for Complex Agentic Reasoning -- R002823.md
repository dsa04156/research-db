---
type: research-source
item_id: 2823
title: "WFM: Wiki Foundation Model for Complex Agentic Reasoning"
source: "arxiv"
published: "2026-09-16T06:13:33Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.18182"
url: "https://arxiv.org/abs/2609.18182v1"
generated_by: codex-research-db
aliases:
  - "WFM: Wiki Foundation Model for Complex Agentic Reasoning"
topics:
  - "ai-agents"
---

# WFM: Wiki Foundation Model for Complex Agentic Reasoning

[원문 열기](https://arxiv.org/abs/2609.18182v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-16T06:13:33Z
- 저자: Junnan Dong, Linhao Luo, Senlei Zhang, Gong Chen, Taian Guo, Yifei Yu, Rong Tao, Tao Guo, Qian-Wen Zhang, Siyu An, Ruizhi Qiao, Xing Sun
- 식별자: `arxiv:2609.18182`

## 요약·초록

Real-world agents fundamentally require persistent non-parametric knowledge for dynamic reasoning, i.e., long-term memory and retrieval-augmented generation. While graphs have shown reliable advantages in providing structured evidence, the sparse graph representations naturally restrict machine readability and semantic density required for complex agentic workflows. Driven by this limitation, the entire industry is witnessing a paradigm shift from traditional sparse graphs to LLM Wiki, an agent-native knowledge representation that couples dense document contexts with markdown files containing multi-layered topological linkages. However, parameterizing such rich semantics is challenging to encode dense textual contexts using traditional sparse graph embeddings. Moreover, learning LLM Wiki with existing graph encoders could overwhelm distributed system overheads that hinder deployment in large-scale commercial scenarios. To this end, we propose a novel paradigm Wiki Foundation Model, i.e., WFM, tailored for scalable, agent-native representation and retrieval. Specifically, (i) we formalize a Wiki Graph schema that seamlessly bridges fine-grained structures with dense contexts, maintaining explicit topologies alongside continuous semantics; (ii) A query-conditioned attentive aggregation is tailored for rich wiki message passing and explicit attention variance regularization; (iii) We engineer an infrastructural NCCL boundary exchange protocol that hoists static partition indices and leverages fixed-shape GPU-to-GPU collectives, bypassing CPU serialization and memory copy overheads. Extensive evaluations across five long-term agent memory and multi-hop reasoning benchmarks demonstrate the remarkable performance of WFM, while achieving a 10.5 times training acceleration on distributed clusters.

## 내 메모

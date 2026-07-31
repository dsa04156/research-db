---
type: research-source
item_id: 610
title: "Assemble Your Crew: Automatic Multi-agent Communication Topology Design via Autoregressive Graph Generation"
source: "arxiv"
published: "2025-07-24T09:17:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.18224"
url: "https://arxiv.org/abs/2507.18224v4"
generated_by: codex-research-db
aliases:
  - "Assemble Your Crew: Automatic Multi-agent Communication Topology Design via Autoregressive Graph Generation"
topics:
  - "ai-agents"
---

# Assemble Your Crew: Automatic Multi-agent Communication Topology Design via Autoregressive Graph Generation

[원문 열기](https://arxiv.org/abs/2507.18224v4)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3U8AD5XE`)
- 발행일: 2025-07-24T09:17:41Z
- 저자: Shiyuan Li, Yixin Liu, Qingsong Wen, Chengqi Zhang, Shirui Pan
- 식별자: `arxiv:2507.18224`

## 요약·초록

Multi-agent systems (MAS) based on large language models (LLMs) have emerged as a powerful solution for dealing with complex problems across diverse domains. The effectiveness of MAS is critically dependent on its collaboration topology, which has become a focal point for automated design research. However, existing approaches are fundamentally constrained by their reliance on a template graph modification paradigm with a predefined set of agents and hard-coded interaction structures, significantly limiting their adaptability to task-specific requirements. To address these limitations, we reframe MAS design as a conditional autoregressive graph generation task, where both the system composition and structure are designed jointly. We propose ARG-Designer, a novel autoregressive model that operationalizes this paradigm by constructing the collaboration graph from scratch. Conditioned on a natural language task query, ARG-Designer sequentially and dynamically determines the required number of agents, selects their appropriate roles from an extensible pool, and establishes the optimal communication links between them. This generative approach creates a customized topology in a flexible and extensible manner, precisely tailored to the unique demands of different tasks. Extensive experiments across six diverse benchmarks demonstrate that ARG-Designer not only achieves state-of-the-art performance but also enjoys significantly greater token efficiency and enhanced extensibility. The source code of ARG-Designer is available at https://github.com/Shiy-Li/ARG-Designer.

## 내 메모



---
type: research-source
item_id: 628
title: "DHEvo: Data-Algorithm Based Heuristic Evolution for Generalizable MILP Solving"
source: "arxiv"
published: "2025-07-21T13:40:19Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.15615"
url: "https://arxiv.org/abs/2507.15615v1"
generated_by: codex-research-db
aliases:
  - "DHEvo: Data-Algorithm Based Heuristic Evolution for Generalizable MILP Solving"
topics:
  - "ai-agents"
---

# DHEvo: Data-Algorithm Based Heuristic Evolution for Generalizable MILP Solving

[원문 열기](https://arxiv.org/abs/2507.15615v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DNAF2RZR`)
- 발행일: 2025-07-21T13:40:19Z
- 저자: Zhihao Zhang, Siyuan Li, Chenxi Li, Feifan Liu, Mengjing Chen, Kai Li, Tao Zhong, Bo An, Peng Liu
- 식별자: `arxiv:2507.15615`

## 요약·초록

Primal heuristics play a critical role in improving the efficiency of mixed integer programming (MILP) solvers. As large language models (LLMs) have demonstrated superior code generation abilities, recent MILP works are devoted to leveraging the evolutionary computation approaches with LLMs to generate effective primal heuristics. Although the generated heuristics have achieved better solving performance than the hand-crafted ones with little adaptability, the advantage of current LLM-based methods is limited to few MILP instances in one problem class, as they fail to capture the instance characteristics in the problem class (the MILP instances generated from the same mathematical model are defined as a problem class). Since MILP instances often differ significantly in structure and feature distribution, the neglect of their characteristics in the evolution process results in poor generalization within the same problem class. To overcome this challenge, we propose a data-algorithm co-evolution framework (DHEvo) that iteratively selects representative instances and evolves corresponding heuristics. With the initial instance distribution, we develop an LLM-based multi-agent system to generate data-code pairs simultaneously. These data-code pairs are iteratively refined based on their fitness scores, leading to the identification of the most effective heuristic over the entire problem class. Extensive experiments across diverse MILP benchmarks demonstrate that our approach significantly outperforms both human-designed heuristics and existing LLM-based methods.

## 내 메모



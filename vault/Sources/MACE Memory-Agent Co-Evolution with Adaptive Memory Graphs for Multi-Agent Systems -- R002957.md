---
type: research-source
item_id: 2957
title: "MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems"
source: "arxiv"
published: "2026-09-18T09:25:06Z"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "arxiv:2609.21533"
url: "https://arxiv.org/abs/2609.21533v1"
generated_by: codex-research-db
aliases:
  - "MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems"
topics:
  - "ai-agents"
---

# MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2609.21533v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SDE3UT76`)
- 발행일: 2026-09-18T09:25:06Z
- 저자: Kairui Yang, Minghao An, Xunkai Li, Ziheng Yi, Zekai Chen, Guangyuan He, Rong-Hua Li
- 식별자: `arxiv:2609.21533`

## 요약·초록

LLM-based multi-agent systems generate collaboration traces that record how agents plan tasks, verify intermediate results, and repair failures. Reusing these procedures requires preserving an action's prerequisites and the outputs needed by subsequent agents. Our empirical studies show that grouping these dependencies into functional memory units improves their retention, while connecting units increases retrieval of the units and links jointly required by a task. The preferred combination of units also changes between instructions and checklists, even when each combination's content is fixed across formats. Updating choices from the outcomes of each combination and format pairing outperforms scoring combinations and formats separately. These findings motivate MACE, a memory-agent co-evolution framework that adapts memory organization and agent memory use through execution feedback. Its MemGoG structure represents functional units as subgraphs of related conditions, actions, and outputs, connecting them through support, conflict, and repair relations. MACE Loop selects task-relevant units and relations within a memory budget and provides each agent with instructions or checklists for its current operation. It records the selected units, presentation formats, agent outputs, and task outcomes to update unit scores and relations for retrieval and inform subsequent presentation choices. Across eight benchmarks, MACE outperforms ten baselines with an average score of 81.11%, compared with 78.97% for the strongest baseline, SAGE.

## 내 메모

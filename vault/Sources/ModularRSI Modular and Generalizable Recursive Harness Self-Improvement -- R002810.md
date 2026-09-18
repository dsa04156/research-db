---
type: research-source
item_id: 2810
title: "ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement"
source: "arxiv"
published: "2026-09-14T00:10:45Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.14857"
url: "https://arxiv.org/abs/2609.14857v1"
generated_by: codex-research-db
aliases:
  - "ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement"
topics:
  - "self-evolving-harness"
---

# ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement

[원문 열기](https://arxiv.org/abs/2609.14857v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MXDFGJFH`)
- 발행일: 2026-09-14T00:10:45Z
- 저자: Siwei Wu, Jincheng Ren, Yizhi Li, Haau-Sing Li, Chengran Yang, Yuxuan Zhang, Weicheng Gu, Jian Yang, Riza Batista-Navarro, Chuanyi Zhang, Xianglong Liu, Ming Zhou, Bryan Dai, Chenghua Lin
- 식별자: `arxiv:2609.14857`

## 요약·초록

Recent work extends recursive self-improvement (RSI) to agent harnesses for long-horizon coding and terminal tasks, enabling agents to improve execution mechanisms from experience. However, generalizable harness RSI remains challenging. First, evolving harnesses on evaluation benchmarks or their subsets makes it difficult to distinguish reusable improvements from benchmark-specific adaptation. Second, single-trajectory updates can conflate systematic harness deficiencies with instance-specific reasoning and solution details, producing modifications that transfer poorly to unseen tasks. Third, localizing recurring behavioral deficiencies within monolithic harnesses is difficult, while whole-harness optimization can entangle unrelated mechanisms and complicate attribution and validation. We propose ModularRSI, a benchmark-disjoint, contrastive, and modular framework for generalizable harness evolution. ModularRSI contrasts successful and failed trajectories for the same task and aggregates evidence across tasks to identify recurring behavioral deficiencies. It decomposes the evolvable harness into five functional modules: Agent Loop, Tool Use, Observation Management, Context Management, and Task Completion Detection. Each module evolves independently within a restricted modification scope, followed by an integration stage that combines the evolved modules into a unified harness and resolves potential conflicts. To support benchmark-disjoint evolution, we curate 2,000 executable evolution tasks from external sources that are disjoint from downstream evaluation benchmarks. Experiments on TB2.0 and SWE-Bench Verified show consistent improvements on unseen in-domain and cross-domain tasks, with the evolved harness also transferring across different foundation models.

## 내 메모

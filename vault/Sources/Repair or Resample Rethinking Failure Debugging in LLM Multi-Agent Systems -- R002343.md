---
type: research-source
item_id: 2343
title: "Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems"
source: "arxiv"
published: "2026-08-26T15:33:47Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.25920"
url: "https://arxiv.org/abs/2608.25920v1"
generated_by: codex-research-db
aliases:
  - "Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems"
topics:
  - "ai-agents"
---

# Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2608.25920v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FRJGQNCK`)
- 발행일: 2026-08-26T15:33:47Z
- 저자: Zhongwen Luan, Xiaoyu Zhang, Ming Hu, Yue Yang, Jiongchi Yu, Xiaohong Chen
- 식별자: `arxiv:2608.25920`

## 요약·초록

As large language model (LLM)-based multi-agent systems (MASs) are increasingly applied to long-horizon complex tasks, their reliability has emerged as the core bottleneck hindering their real-world deployment. Existing MAS debugging and repair methods typically rely on rerunning and resampling the entire execution trajectory. However, a fundamental question remains to be answered: do these methods causally repair MAS failures or merely stochastically repair by leveraging the randomness of LLM sampling? To evaluate the effectiveness of MAS repair methods, we introduce SymTrace, a controlled evaluation framework that records the MAS execution trajectory and establishes intervention anchors. During replay, it effectively reconstructs the execution before the anchor using recorded logs and only regenerates the downstream trajectory, thereby enabling the reliable reproduction of MAS failures. We further construct the dataset SymFail, comprising 536 human-annotated failure trajectories with graph-linked locations, categories, and trace evidence. Based on these foundations, we conduct a large-scale empirical study across three mainstream MAS frameworks. Our findings reveal that existing unguided rerun methods are highly unreliable, exhibiting low failure reproduction and repair rates (only 67.97% and 6.90%, respectively). Building upon these findings, we further explore the effectiveness of a symptom-driven intervention method, which successfully repairs 20.15% of the failed cases (a 191.89% improvement to state-of-the-art repair methods). This study aims to provide actionable insights for MAS debugging and repair research, paving the way for the robust deployment of multi-agent systems.

## 내 메모



---
type: research-source
item_id: 605
title: "MAC: Masked Agent Collaboration Boosts Large Language Model Medical Decision-Making"
source: "arxiv"
published: "2025-07-25T04:21:16Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.21159"
url: "https://arxiv.org/abs/2507.21159v3"
generated_by: codex-research-db
aliases:
  - "MAC: Masked Agent Collaboration Boosts Large Language Model Medical Decision-Making"
topics:
  - "ai-agents"
---

# MAC: Masked Agent Collaboration Boosts Large Language Model Medical Decision-Making

[원문 열기](https://arxiv.org/abs/2507.21159v3)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JNUT5MNK`)
- 발행일: 2025-07-25T04:21:16Z
- 저자: Zhihao Peng, Liuxin Bao, Yixuan Yuan
- 식별자: `arxiv:2507.21159`

## 요약·초록

Large language models (LLMs) have proven effective in artificial intelligence, where the multi-agent system (MAS) holds considerable promise for healthcare development by achieving the collaboration of LLMs. However, the absence of a systematic pipeline for agent construction and the rigidity of static collaboration patterns render current MAS-based models vulnerable to collaboration failures, resulting in substantial performance degradation in medical decision-making scenarios. To this end, we propose a novel Masked Agent Collaboration (MAC) framework that harnesses Pareto-optimal agent construction and cross-consistency maximization mechanisms to achieve adaptive progressive propagation of collaborative information, boosting the medical decision-making capacity. Specifically, we first conduct a Pareto-frontier factors analysis towards the LLMs pool to consider their key factors, including the model size, inference time, diversity score, and throughput ratio, where we calculate the similarity between pairwise outputs within an LLM to derive its diversity score. Beyond this analysis, we enable the identification of Pareto-optimal models that balance efficiency and capability, which are subsequently selected as collaborative agents to consider the fundamental trade-offs inherent in practical LLM deployment. Afterward, we measure the pairwise similarity between the outputs from collaborative agents to determine their cross-consistency values, subsequently masking out the agent with the lowest cross-consistency value to eliminate the output that is likely semantically inconsistent. Finally, we conduct collaboration of agents by achieving adaptive progressive propagation, where each agent aggregates the outputs of unmasked agents from the previous layer as its input to generate the corresponding output via prompt engineering.

## 내 메모



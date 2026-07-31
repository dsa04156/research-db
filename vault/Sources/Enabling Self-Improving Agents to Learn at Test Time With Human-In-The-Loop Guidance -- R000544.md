---
type: research-source
item_id: 544
title: "Enabling Self-Improving Agents to Learn at Test Time With Human-In-The-Loop Guidance"
source: "arxiv"
published: "2025-07-23T02:12:32Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.17131"
url: "https://arxiv.org/abs/2507.17131v2"
generated_by: codex-research-db
aliases:
  - "Enabling Self-Improving Agents to Learn at Test Time With Human-In-The-Loop Guidance"
topics:
  - "self-evolving-harness"
---

# Enabling Self-Improving Agents to Learn at Test Time With Human-In-The-Loop Guidance

[원문 열기](https://arxiv.org/abs/2507.17131v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ERW7JEVC`)
- 발행일: 2025-07-23T02:12:32Z
- 저자: Yufei He, Ruoyu Li, Alex Chen, Yue Liu, Yulin Chen, Yuan Sui, Cheng Chen, Yi Zhu, Luca Luo, Frank Yang, Bryan Hooi
- 식별자: `arxiv:2507.17131`

## 요약·초록

Large language model (LLM) agents often struggle in environments where rules and required domain knowledge frequently change, such as regulatory compliance and user risk screening. Current approaches, like offline fine-tuning and standard prompting, are insufficient because they cannot effectively adapt to new knowledge during actual operation. To address this limitation, we propose the Adaptive Reflective Interactive Agent (ARIA), an LLM agent framework designed specifically to continuously learn updated domain knowledge at test time. ARIA assesses its own uncertainty through structured self-dialogue, proactively identifying knowledge gaps and requesting targeted explanations or corrections from human experts. It then systematically updates an internal, timestamped knowledge repository with provided human guidance, detecting and resolving conflicting or outdated knowledge through comparisons and clarification queries. We evaluate ARIA on the realistic customer due diligence name screening task on TikTok Pay, alongside publicly available dynamic knowledge tasks. Results demonstrate significant improvements in adaptability and accuracy compared to baselines using standard offline fine-tuning and existing self-improving agents. ARIA is deployed within TikTok Pay serving over 150 million monthly active users, confirming its practicality and effectiveness for operational use in rapidly evolving environments.

## 내 메모



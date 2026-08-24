---
type: research-source
item_id: 2180
title: "Inadvertent Context Leakage in Language Models"
source: "arxiv"
published: "2026-08-20T10:05:29Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.19857"
url: "https://arxiv.org/abs/2608.19857v1"
generated_by: codex-research-db
aliases:
  - "Inadvertent Context Leakage in Language Models"
topics:
  - "ai-agents"
---

# Inadvertent Context Leakage in Language Models

[원문 열기](https://arxiv.org/abs/2608.19857v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-20T10:05:29Z
- 저자: Jaiden Fairoze, Neal Mangaokar, Kamalika Chaudhuri, Sanjam Garg, Saeed Mahloujifar
- 식별자: `arxiv:2608.19857`

## 요약·초록

For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel adaptive attack that assumes black-box access to the underlying model. In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82\% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. We observe that more capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, suggesting leakage is a byproduct of capability as opposed to a patchable bug. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent.

## 내 메모



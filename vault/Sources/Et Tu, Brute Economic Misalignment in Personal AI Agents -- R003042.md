---
type: research-source
item_id: 3042
title: "Et Tu, Brute? Economic Misalignment in Personal AI Agents"
source: "arxiv"
published: "2026-09-21T17:22:44Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.24927"
url: "https://arxiv.org/abs/2609.24927v1"
generated_by: codex-research-db
aliases:
  - "Et Tu, Brute? Economic Misalignment in Personal AI Agents"
topics:
  - "ai-agents"
---

# Et Tu, Brute? Economic Misalignment in Personal AI Agents

[원문 열기](https://arxiv.org/abs/2609.24927v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-21T17:22:44Z
- 저자: Aman Priyanshu, Supriti Vijay, Brian Jabarian, Niloofar Mireshghallah
- 식별자: `arxiv:2609.24927`

## 요약·초록

Personal AI agents make recommendations and take actions on people's behalf in high-stakes economic contexts, e.g., buying a flight, choosing health insurance, or selecting a graduate program. The agent is given access to the user's personal context, e.g., their email inbox and a structured profile of personal attributes, with the intention of making an optimal, personalized decision for the user. We show that by simply providing this personal context, the agent steers recommendations based on inferred wealth, without being explicitly instructed to do so. In a suite of 325K experiments on 13 agents across three types of economic decisions (flights, health insurance, and graduate programs), we find that 8 models systematically choose more expensive options for wealthier users when requests are identical. This steering continues even when it directly goes against the user's stated objective: when explicitly instructed to find the cheapest option, some agents still act on the wealth profile they have inferred. It also occurs when wealth is inferred from ambient data, such as emails unrelated to the task. And it persists under privacy controls that block specific attributes: blocking financial attributes largely removes the disparity, but blocking other attributes leaves it unchanged and can increase it by up to 40% for insurance, as agents rely on the remaining signals to infer wealth. Larger and more capable models are no better; Claude Opus 4.8 shows the largest effect. We term this misalignment "adversarial delegation", in which the very conditions that make a personal AI agent useful - access to personal information - enable it to act against the user's interests.

## 내 메모

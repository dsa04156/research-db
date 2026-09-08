---
type: research-source
item_id: 2609
title: "Testing Interchangeability in LLM Agent Teams"
source: "arxiv"
published: "2026-09-04T15:32:20Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.05279"
url: "https://arxiv.org/abs/2609.05279v1"
generated_by: codex-research-db
aliases:
  - "Testing Interchangeability in LLM Agent Teams"
topics:
  - "ai-agents"
---

# Testing Interchangeability in LLM Agent Teams

[원문 열기](https://arxiv.org/abs/2609.05279v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-04T15:32:20Z
- 저자: Jianxin Gao, Tianyi Yu, Linna Deng, Runze Li, Zining Wang
- 식별자: `arxiv:2609.05279`

## 요약·초록

Production multi-agent systems replace agents constantly, on the assumption that an agent filling a role is interchangeable with any other agent that can do the job. We test that assumption. Eight teams per setting are formed independently from one base model on the same tasks, each agent keeping a private notebook across ten formation episodes; we then trade role-matched agents between teams and measure what changes on held-out tasks. Against a placebo that reproduces the disruption of a roster change without changing who occupies the seat, a swap costs little in task score but raises the communication a team spends per unit of progress by 16 to 63 percent, and in Hanabi a swapped agent is more expensive than an inexperienced one, consistent with interference from conventions learned with its former partner. In Collab-Overcooked, when the agent that sets the agenda is replaced, most of the extra communication comes from the agent that stayed. Three ablations, over base models, decoding temperature and formation length, move the swap penalty alongside one other quantity: how far independently formed teams drift apart. Greedy decoding lowers both; doubling a team's history raises both. In these settings, agents are more fungible in task outcome than in coordination efficiency, with larger swap effects after longer formation histories.

## 내 메모



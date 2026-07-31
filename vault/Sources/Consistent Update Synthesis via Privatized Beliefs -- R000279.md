---
type: research-source
item_id: 279
title: "Consistent Update Synthesis via Privatized Beliefs"
source: "arxiv"
published: "2024-06-14T13:24:07Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.10010"
url: "https://arxiv.org/abs/2406.10010v1"
generated_by: codex-research-db
aliases:
  - "Consistent Update Synthesis via Privatized Beliefs"
topics:
  - "ai-agents"
---

# Consistent Update Synthesis via Privatized Beliefs

[원문 열기](https://arxiv.org/abs/2406.10010v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5S8FDD4M`)
- 발행일: 2024-06-14T13:24:07Z
- 저자: Thomas Schlögl, Roman Kuznets, Giorgio Cignarale
- 식별자: `arxiv:2406.10010`

## 요약·초록

Kripke models are an effective and widely used tool for representing epistemic attitudes of agents in multi-agent systems, including distributed systems. Dynamic Epistemic Logic (DEL) adds communication in the form of model transforming updates. Private communication is key in distributed systems as processes exchanging (potentially corrupted) information about their private local state should not be detectable by any other processes. This focus on privacy clashes with the standard DEL assumption for which updates are applied to the whole Kripke model, which is usually commonly known by all agents, potentially leading to information leakage. In addition, a commonly known model cannot minimize the corruption of agents' local states due to fault information dissemination. The contribution of this paper is twofold: (I) To represent leak-free agent-to-agent communication, we introduce a way to synthesize an action model which stratifies a pointed Kripke model into private agent-clusters, each representing the local knowledge of the processes: Given a goal formula $\varphi$ representing the effect of private communication, we provide a procedure to construct an action model that (a) makes the goal formula true, (b) maintain consistency of agents' beliefs, if possible, without causing "unrelated" beliefs (minimal change) thus minimizing the corruption of local states in case of inconsistent information. (II) We introduce a new operation between pointed Kripke models and pointed action models called pointed updates which, unlike the product update operation of DEL, maintain only the subset of the world-event pairs that are reachable from the point, without unnecessarily blowing up the model size.

## 내 메모



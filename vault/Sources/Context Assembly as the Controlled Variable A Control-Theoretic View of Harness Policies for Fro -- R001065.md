---
type: research-source
item_id: 1065
title: "Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents"
source: "arxiv"
published: "2026-07-28T08:07:06Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25408"
url: "https://arxiv.org/abs/2607.25408v1"
generated_by: codex-research-db
aliases:
  - "Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents"
topics:
  - "ai-agents"
---

# Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents

[원문 열기](https://arxiv.org/abs/2607.25408v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`B8CJXWIB`)
- 발행일: 2026-07-28T08:07:06Z
- 저자: Debjyoti Paul
- 식별자: `arxiv:2607.25408`

## 요약·초록

A growing body of 2026 work applies control theory to LLM agents: Lyapunov-certified stability for tool-mediated controllers (Prinos et al., "Stable Agentic Control", 2026), sample-complexity bounds for sparse policies over massive discrete tool universes (Majumdar, "Sparse Agentic Control", 2026), and regulatory-control decompositions of multi-agent systems into auditable feedback loops (Nogueira and Skogestad, 2026). We do not claim to introduce control theory to LLM agents -- that ship has sailed. Our narrower claim is about what the controlled variable is. Prior work controls tool selection, inter-agent message routing, or the agent's raw action stream. We instead treat context assembly itself -- which prompt template, which few-shot demonstrations, how much retrieved context, how many planning/verification passes -- as the controlled variable, learned online by a contextual bandit or REINFORCE policy sitting outside a frozen model. This paper develops the formal decomposition (inner frozen policy $π_θ$, outer context policy $π_φ$), gives a stability argument for the online controller in the sense used by Zhang et al. (2026) (non-decreasing expected reward under bounded policy change), and reports an uncertainty-calibration analysis of the controller's own confidence against realized task outcomes. The applied counterpart to this paper instantiates the same controller across three domains and two model providers and releases the dataset, trajectory logs, and a deployment recipe; here we focus on the formal framing and the stability/uncertainty evidence a control-theoretic claim requires.

## 내 메모



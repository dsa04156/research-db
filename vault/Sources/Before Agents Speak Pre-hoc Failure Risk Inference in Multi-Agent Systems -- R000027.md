---
type: research-source
item_id: 27
title: "Before Agents Speak: Pre-hoc Failure Risk Inference in Multi-Agent Systems"
source: "arxiv"
published: "2026-07-29T12:26:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26836"
url: "https://arxiv.org/abs/2607.26836v1"
generated_by: codex-research-db
aliases:
  - "Before Agents Speak: Pre-hoc Failure Risk Inference in Multi-Agent Systems"
topics:
  - "ai-agents"
---

# Before Agents Speak: Pre-hoc Failure Risk Inference in Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2607.26836v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`WEJEEQDC`)
- 발행일: 2026-07-29T12:26:41Z
- 저자: Shi Lin, Chenpei Wang, Peng Qian, Dezhang Kong, Minghao Li, Yufeng Li, Xun Wang
- 식별자: `arxiv:2607.26836`

## 요약·초록

LLM-based multi-agent systems (MAS) have exhibited remarkable capabilities in collaborative reasoning and decision-making, yet their interconnected communications introduce new systemic risk: localized hallucinations can propagate along agent communication chain, amplify through interactions, and ultimately trigger cascading failures. Existing countermeasures predominantly follow a post-hoc paradigm, identifying failures only after unsafe behaviors emerge, by which time harmful effects may have already spread throughout the agent network. To tackle this problem, we investigate a complementary pre-hoc approach and propose HalluProp, a Propagation-aware Hallucination inference framework that estimates individual agent failures and emergent system-level hallucination risks before inter-agent interaction. First, we model intrinsic hallucination risks by identifying fine-grained semantic misalignment between agent roles and task queries. We then characterize inter-agent risk propagation by modeling both semantic influence and communication topology. Finally, we integrate these two risks via a differentiable Noisy-OR inference mechanism to derive a systemic diagnosis. Extensive experiments show that HalluProp accurately localizes faulty agents, achieving an average AUROC of 84.6%, while enabling sub-second diagnosis with over $65\times$ speedup over post-hoc methods. By facilitating early intervention through upstream screening, HalluProp effectively complements post-hoc methods, highlighting the potential of pre-hoc risk inference for building more reliable multi-agent systems.

## 내 메모



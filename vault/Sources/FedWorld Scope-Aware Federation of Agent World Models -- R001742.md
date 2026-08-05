---
type: research-source
item_id: 1742
title: "FedWorld: Scope-Aware Federation of Agent World Models"
source: "arxiv"
published: "2026-08-03T00:37:52Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.01561"
url: "https://arxiv.org/abs/2608.01561v1"
generated_by: codex-research-db
aliases:
  - "FedWorld: Scope-Aware Federation of Agent World Models"
topics:
  - "ai-agents"
---

# FedWorld: Scope-Aware Federation of Agent World Models

[원문 열기](https://arxiv.org/abs/2608.01561v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`24KRHFWE`)
- 발행일: 2026-08-03T00:37:52Z
- 저자: Yuchao Hou
- 식별자: `arxiv:2608.01561`

## 요약·초록

Large language model (LLM) agents learn world dynamics from local interaction experience to support subsequent planning and action selection. However, the experience available to a single client is often incomplete, which motivates sharing knowledge across clients. Existing federated methods mainly aggregate model parameters, while agent memory-sharing methods commonly pool trajectories, memories, or rules without checking whether they remain valid for each client. This assumption is problematic because the same abstract action may produce different effects under different policies, environments, or exception conditions. Consequently, a rule supported by most clients may overwrite correct knowledge held by a minority client. To address this problem, we propose FEDWORLD, a scope-aware federated world-model protocol that exchanges structured abstract transition rules. Each client converts private transitions into normalized rules, and the server aligns related rules to identify each rule supporting and contradicting evidence across clients. The resulting evidence determines whether a rule is shared, cluster-specific, private, or unresolved. Each target client retains its local rules and accepts federated updates only for uncovered cases whose inferred scope is compatible; ambiguous rules are withheld. Experiments on $τ$-bench and ALFWorld show that FEDWORLD reduces negative transfer under conflicting dynamics while retaining useful cross-client transfer, leading to fewer state regressions, repeated actions, and excess steps, as well as higher task success.

## 내 메모



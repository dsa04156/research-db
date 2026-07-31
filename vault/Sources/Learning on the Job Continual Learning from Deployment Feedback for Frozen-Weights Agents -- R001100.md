---
type: research-source
item_id: 1100
title: "Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents"
source: "arxiv"
published: "2026-07-24T10:01:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.22157"
url: "https://arxiv.org/abs/2607.22157v1"
generated_by: codex-research-db
aliases:
  - "Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents"
topics:
  - "ai-agents"
---

# Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents

[원문 열기](https://arxiv.org/abs/2607.22157v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`IXTT6JEJ`)
- 발행일: 2026-07-24T10:01:00Z
- 저자: Valentin Tablan, Scott Taylor, Kristoffer Bernhem
- 식별자: `arxiv:2607.22157`

## 요약·초록

AI agents encounter learning opportunities in every episode they run, and discard nearly all of them: the underlying models are frozen at deployment, so an agent that resolves a difficult request today starts from zero when it recurs tomorrow. Yet ordinary operation already produces feedback, in the form of outcome verdicts and after-the-fact corrections. We show that this feedback is a sufficient signal for continual learning when the frozen model is paired with an external memory that distils each episode into retrievable natural-language rules. On the banking domain of $τ$-bench, against a static-RAG control retrieving over the complete policy corpus, learning from the one-bit outcome verdict lifts single-trial success to 1.6$\times$ the baseline, and learning from corrections to 2.6$\times$, converting 22 of the 84 tasks the baseline never solves. The result spans the deployment spectrum, measured on Mistral Large, an open-weights model that organisations with data sovereignty requirements can self-host, and replicated on a frontier model, Claude Sonnet 5. The accumulated memory also transfers: each model, reading the store built by the other, rises above its own no-memory baseline. The harness, protocol, and data are released.

## 내 메모



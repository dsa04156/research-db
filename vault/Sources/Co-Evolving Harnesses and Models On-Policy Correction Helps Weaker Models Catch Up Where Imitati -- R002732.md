---
type: research-source
item_id: 2732
title: "Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails"
source: "arxiv"
published: "2026-09-08T17:53:49Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.09134"
url: "https://arxiv.org/abs/2609.09134v1"
generated_by: codex-research-db
aliases:
  - "Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails"
topics:
  - "self-evolving-harness"
---

# Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails

[원문 열기](https://arxiv.org/abs/2609.09134v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-08T17:53:49Z
- 저자: Zhou Yu, Bin Bi, Shiva Kumar Pentyala, Shubham Mehrotra, Sougata Chaudhuri, Shilpa Bhagavath, Zeyuan Chen, Ran Xu, Phil Mui, James Zhu, Sitaram Asur
- 식별자: `arxiv:2609.09134`

## 요약·초록

Agent harnesses (the system prompt, tool set, execution hooks, and context-management scaffolding around a model) are a critical determinant of agentic task success. Automated harness evolution can enable smaller models to perform well on domain-specific tasks at a fraction of frontier-model cost. Since both the harness and model weights shape behavior, we ask how harness evolution and lightweight fine-tuning should be combined. Across seven enterprise agent tasks, we first evolve a harness with the weaker model, then find that a stronger expert often uses it more effectively, suggesting expert supervision could close the remaining gap. However, training the weaker model on the expert's complete trajectories under the evolved harness backfires: performance regresses on all seven tasks by 4 to 30 points across Qwen3-Coder and Gemma 4, even though the same procedure helps under the unevolved harness. Our analysis shows that imitation transfers knowledge and increases scaffold usage, but disrupts model-harness fit: the weaker model adopts the expert's planning strategy without the competence to execute it and no longer matches the harness evolved around its native planning style. We therefore develop an on-policy expert-correction pipeline, automated by a meta-level MLE agent, that localizes the failing turn in the weaker model's own rollout and asks the expert to rewrite only that turn. This preserves the model's planning style and combines the gains of harness evolution and model adaptation. Our results identify and resolve a source of contention between harness and weight updates, yielding a compatibility-preserving recipe for economical co-evolution on domain-specific enterprise tasks.

## 내 메모



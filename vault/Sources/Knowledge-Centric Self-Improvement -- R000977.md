---
type: research-source
item_id: 977
title: "Knowledge-Centric Self-Improvement"
source: "arxiv"
published: "2026-07-21T21:38:39Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19592"
url: "https://arxiv.org/abs/2607.19592v1"
generated_by: codex-research-db
aliases:
  - "Knowledge-Centric Self-Improvement"
topics:
  - "self-evolving-harness"
---

# Knowledge-Centric Self-Improvement

[원문 열기](https://arxiv.org/abs/2607.19592v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GNE2GEVC`)
- 발행일: 2026-07-21T21:38:39Z
- 저자: Xuefei Julie Wang, Lauren Hyoseo Yoon, Chengrui Qu, Amanda Zichang Wang, Atharva Sehgal, Eric Mazumdar, Yisong Yue
- 식별자: `arxiv:2607.19592`

## 요약·초록

Self-improving AI systems typically treat the agent as the object that improves, by optimizing prompts, workflows, harnesses, or even the agent's own code. This agent-centric view can make improvements expensive to maintain and difficult to transfer, because gains become tied to a particular agent design, task distribution, or adaptation run. We study a complementary paradigm: knowledge-centric self-improvement, in which agents remain generic and disposable while the persistent object is a curated knowledge base that agents can leverage for future tasks. We conduct controlled case studies to operationalize this idea via a simple protocol. Agents attempt one task, then contribute evidence-grounded insights to a shared knowledge base via task-level and cross-task forums, followed by knowledge distillation. Because self-improvement is contained in the knowledge rather than the agent, improvement can be more inspectable, transferable, and portable. Across abstract reasoning, coding, and terminal benchmarks, this protocol improves solve rates while reducing dollar cost relative to agent-centric baselines. The resulting distilled knowledge also transfers to held-out tasks and across LLM families, indicating that the improvement is not merely an LLM- or run-specific behavior. These results support a new view of self-improving agentic systems: progress can be driven primarily by the curated persistent knowledge. Code is available at https://github.com/recursive-knowledge/KSI.

## 내 메모



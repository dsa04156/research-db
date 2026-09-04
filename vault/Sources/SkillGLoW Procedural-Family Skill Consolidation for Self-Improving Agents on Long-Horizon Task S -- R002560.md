---
type: research-source
item_id: 2560
title: "SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams"
source: "arxiv"
published: "2026-09-02T07:31:18Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.02217"
url: "https://arxiv.org/abs/2609.02217v1"
generated_by: codex-research-db
aliases:
  - "SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams"
topics:
  - "self-evolving-harness"
---

# SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams

[원문 열기](https://arxiv.org/abs/2609.02217v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-02T07:31:18Z
- 저자: Ao Yan, Xin Zhang, Jiawei Du, Joey Tianyi Zhou
- 식별자: `arxiv:2609.02217`

## 요약·초록

LLM agents increasingly self-improve by writing and reusing textual skills, kept either as one global document or as a flat pool of per-task entries, though most of the evidence comes from domains with structurally similar tasks. On long-horizon workloads where each task demands a different solution, the two forms fail in opposite ways: the document collapses into generic discipline, while the pool inflates and its entries stay bound to the instance that wrote them. We argue the missing unit of reuse is the solving procedure shared by a cluster of related tasks, and build SkillGLoW (Global-Local Weave) around it: the local skills a task writes from its own execution are aggregated into procedural families and compressed into de-instantiated global priors, while the instance detail they hold is regenerated per task rather than stored; a commit gate admits a prior only when real execution shows it does not degrade the deployed library. Across four benchmarks (mathematical reasoning, terminal automation, software repair, and embodied control) and three models, the priors gain 17.2 points (hard) over the no-skill baseline on average, with positive gains in all 12 continual-improvement runs, and 18.0 with local regeneration, while the library holds one prior per procedural family, 3.6x more compact than the per-task pool. Under the same protocol GLoW leads a published single-document optimizer on 15 of 21 cells. Unmodified, the library lifts success on unseen ALFWorld tasks from 73.9% to 83.9%, evidence that what transfers is procedure rather than task memory.

## 내 메모



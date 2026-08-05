---
type: research-source
item_id: 1722
title: "SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation"
source: "arxiv"
published: "2026-08-03T14:18:00Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.02287"
url: "https://arxiv.org/abs/2608.02287v1"
generated_by: codex-research-db
aliases:
  - "SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation"
topics:
  - "self-evolving-harness"
---

# SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation

[원문 열기](https://arxiv.org/abs/2608.02287v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8RSE9AI7`)
- 발행일: 2026-08-03T14:18:00Z
- 저자: Zelin Tan, Yiqun Zhang, Hao Li, Zhiyao Cui, Hejia Geng, Shao Zhang, Hangfan Zhang, Yang Chen, Xiaosong Wang, Lilong Wang, Zhenfei Yin, Shuyue Hu, Chen Zhang, Lei Bai
- 식별자: `arxiv:2608.02287`

## 요약·초록

Agent skills have become an important mechanism for equipping language-model agents with reusable procedural knowledge. However, providing skills alone does not guarantee that current models can effectively identify, apply, and coordinate them. To improve skill-use capabilities, we introduce SKT, a verified data synthesis pipeline that constructs skill-grounded tasks and executable trajectories from large collections of agent skills. SKT selects suitable single-skill and multi-skill configurations, synthesizes tasks through rule-based and agent-based verification with feedback-guided repair, and retains only successful trajectories that substantially use every required skill. Using 2,000 public skills, SKT produces 4,000 task packages and 27,164 verified trajectories. Based on the same pipeline and a disjoint test pool, we further construct SkillEval, a held-out executable benchmark for evaluating skill use. Experiments across diverse models, benchmarks, and agent harnesses show that supervised fine-tuning on SKT-generated trajectories consistently improves skill-use performance. Verification ablations, cross-harness evaluation, and scaling experiments further demonstrate that these gains depend on high-quality supervision, extend beyond a single agent interface, and increase with broader skill coverage. Together, these results establish verified data synthesis as an effective and scalable approach for skill-use training.

## 내 메모



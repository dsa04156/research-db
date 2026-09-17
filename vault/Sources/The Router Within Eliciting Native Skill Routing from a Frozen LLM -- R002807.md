---
type: research-source
item_id: 2807
title: "The Router Within: Eliciting Native Skill Routing from a Frozen LLM"
source: "arxiv"
published: "2026-09-14T17:58:27Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.15982"
url: "https://arxiv.org/abs/2609.15982v1"
generated_by: codex-research-db
aliases:
  - "The Router Within: Eliciting Native Skill Routing from a Frozen LLM"
topics:
  - "self-evolving-harness"
---

# The Router Within: Eliciting Native Skill Routing from a Frozen LLM

[원문 열기](https://arxiv.org/abs/2609.15982v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-14T17:58:27Z
- 저자: Ruishuo Chen, Xun Wang, Yu Chen, Zhuoran Li, Longbo Huang
- 식별자: `arxiv:2609.15982`

## 요약·초록

Skills extend an LLM agent beyond its parametric knowledge, and the gain they promise rests on picking the right one. Deployed harnesses route by preloading every skill's metadata into the context, which disperses the agent's attention and caps the library size. Retrieval pipelines move the selection out of the context, but also out of the agent's capability. We show that the frozen agent LLM already carries the routing signal in its own forward passes, and that two linear maps suffice to read it out with no skill text in the context. Gavel (Glance And Verdict from a frozen LLM) reads it in two steps. A glance projects the task's and each skill's mid-layer states through the two maps, the only parameters trained, and scores the full library against compact per-skill banks that one forward pass builds at installation. A verdict then resumes the shortlisted skills' forward passes and reads the model's own likelihood and yes/no judgment, fused with the glance as a product of experts. Trained once, Gavel transfers zero-shot to three public benchmarks and SkillTraj, our new benchmark of 372 simulated agent trajectories. On Qwen3-32B it outperforms progressive disclosure and retrieve-and-rerank pipelines that add 1.2B to 16B external parameters, by up to 13.4 points on written tasks and up to 21.9 when the need for a skill arises mid-rollout. Routing accuracy improves as the backbone does, and in a bash-agent harness the same 32B triggers the correct skill on Skill-Use more often than far larger frontier models running in Codex.

## 내 메모

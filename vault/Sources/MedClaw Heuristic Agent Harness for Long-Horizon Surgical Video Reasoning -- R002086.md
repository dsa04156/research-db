---
type: research-source
item_id: 2086
title: "MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning"
source: "arxiv"
published: "2026-08-14T07:03:06Z"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "arxiv:2608.14015"
url: "https://arxiv.org/abs/2608.14015v1"
generated_by: codex-research-db
aliases:
  - "MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning"
topics:
  - "self-evolving-harness"
---

# MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning

[원문 열기](https://arxiv.org/abs/2608.14015v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8TJXJB64`)
- 발행일: 2026-08-14T07:03:06Z
- 저자: Yingying Fan, Penghui Du, Leyan Zhu, Runze He, Zimeng Wu, Yuxuan Zhang, Liang Chen, Jiahao Xie, Jiangtang Wang, Shuai Shao, Anchao Yang, Yutong Bai, Yan Wang
- 식별자: `arxiv:2608.14015`

## 요약·초록

Understanding tens-of-minutes surgical videos requires long-horizon temporal reasoning, answering what happens before, after, or across stages of a procedure by grounding the question in visual evidence spread across time. Existing approaches handle this poorly: a one-shot vision-language model (VLM) compresses the whole procedure to fit its context window and loses the detail a "before" or "after" question depends on, while video agents that train the model where to look are data-hungry and transfer poorly to out-of-domain surgery. We build an agent harness that separates reasoning from perception and improves by evolving context rather than optimizing weights. A text-only orchestrator plans which evidence to gather and issues an auditable sequence of tool calls, while frozen vision-language sub-agents execute each call over the pixels, viewing, cropping, inspecting frames, and retrieving external knowledge. We further propose a gradient-free, reward-gated Heuristic Skill Distillation loop that mines the agent's own low-scoring traces and keeps a candidate skill only when it raises a validation reward, yielding reusable retrieval skills, notably directed re-look. Growing an external skill library rather than tuning weights, the loop adapts from only about 100 labeled examples, far fewer than supervised or reinforcement fine-tuning requires. To evaluate this agent, we introduce MedClawBench, a de-leaked, doctor-grounded benchmark of 1,123 questions over self-built long neurosurgery recordings and a held-out public lecture-video test split. Across both datasets and all four evaluation dimensions, our agent consistently outperforms one-shot VLMs and general video-agent frameworks, with the largest gains on the long, out-of-domain neurosurgery videos. Project page: https://fyycs.github.io/medclaw/.

## 내 메모



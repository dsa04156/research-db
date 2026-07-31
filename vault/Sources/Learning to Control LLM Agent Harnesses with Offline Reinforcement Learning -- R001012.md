---
type: research-source
item_id: 1012
title: "Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning"
source: "arxiv"
published: "2026-07-05T22:11:18Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.05458"
url: "https://arxiv.org/abs/2607.05458v1"
generated_by: codex-research-db
aliases:
  - "Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning"
topics:
  - "self-evolving-harness"
---

# Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning

[원문 열기](https://arxiv.org/abs/2607.05458v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DXBBDA62`)
- 발행일: 2026-07-05T22:11:18Z
- 저자: Haiwen Yi, Xinyuan Song
- 식별자: `arxiv:2607.05458`

## 요약·초록

Large language model (LLM) agents are usually improved by changing prompts, models, or hand-written workflows, while the execution harness around the model is treated as fixed infrastructure. We argue that this harness is itself a learnable control layer. We formalize harness operation as a finite-horizon Harness MDP, where a lightweight controller selects structural execution actions while the LLM executor remains frozen. The controller is trained from offline rollouts using advantage-weighted regression with only terminal task-rubric rewards. We also separate final task quality from a post-hoc Harness Maturity Score, which measures whether the harness follows reliable execution patterns rather than only whether the final answer is correct. This separation gives a finite-buffer view of harness learning: final-quality gains require high-return support in the offline buffer, while process behavior can shift whenever it aligns with advantage-weighted actions. Across six controlled domains and two public-benchmark adapters, the learned controller consistently improves verification behavior and selectively improves final task quality, with the largest gains on adapted tau-bench retail, adapted AgentBench DB-Bench, and coding with a calibrated structural verifier. Ablations against behavior cloning and Forced CHECK show that the gains are not explained by imitation or by simply adding checks. These results identify harness control as a learnable layer for frozen LLM agents, while showing that offline support limits when better process control becomes better final answers.

## 내 메모



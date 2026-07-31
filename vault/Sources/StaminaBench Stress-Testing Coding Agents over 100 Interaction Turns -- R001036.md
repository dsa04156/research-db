---
type: research-source
item_id: 1036
title: "StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns"
source: "arxiv"
published: "2026-06-17T21:36:09Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.19613"
url: "https://arxiv.org/abs/2606.19613v1"
generated_by: codex-research-db
aliases:
  - "StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns"
topics:
  - "self-evolving-harness"
---

# StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns

[원문 열기](https://arxiv.org/abs/2606.19613v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FNHSQC6X`)
- 발행일: 2026-06-17T21:36:09Z
- 저자: Vlad Sobal, Shuo Yang, Yuting Zhang, Wei Xia, Stefano Soatto
- 식별자: `arxiv:2606.19613`

## 요약·초록

We introduce StaminaBench, a benchmark that measures the stamina of coding agents: how many consecutive interaction turns (change requests) they can handle before failing. Unlike the prevailing fraction-of-tasks-solved metric, this matches real vibe-coding where sessions run dozens or hundreds of turns. In StaminaBench, agents implement a REST API server and modify it across a tunable number of procedurally generated follow-up change requests - 100 in our experiments, resulting in codebases of up to 6,000 lines. Tests are generated fully programmatically without LLM involvement, ensuring reproducibility and reliability; change sequences are drawn from either a hardcoded or LLM-driven sampler, both constrained to a structured action space to ensure changes are valid. The agent and the server run in an isolated environment and communicate with the benchmark through HTTP, making testing fully black-box and language-agnostic. We evaluate six agent harnesses paired with seven open-source LLMs across 20 scenarios of 100 turns each and find that: (1) all the tested models fail within 5-6 turns, confirming that vibe-coding-style programming without thorough testing produces bugs; (2) passing test feedback back to the agent and allowing it to retry improves passed turn count by up to 12x; and (3) a good harness is required for strong performance: stronger models exhibit up to a 6x gap between their best and worst harness, while weaker models fail with any harness. We release the benchmark and the generated tasks to enable further research into multi-turn coding agent behavior. Benchmark code and data: github.com/amazon-science/StaminaBench.

## 내 메모



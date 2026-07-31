---
type: research-source
item_id: 998
title: "AgentAbstain: Do LLM Agents Know When Not to Act?"
source: "arxiv"
published: "2026-07-11T00:57:36Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.10059"
url: "https://arxiv.org/abs/2607.10059v1"
generated_by: codex-research-db
aliases:
  - "AgentAbstain: Do LLM Agents Know When Not to Act?"
topics:
  - "self-evolving-harness"
---

# AgentAbstain: Do LLM Agents Know When Not to Act?

[원문 열기](https://arxiv.org/abs/2607.10059v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TKW8NUVT`)
- 발행일: 2026-07-11T00:57:36Z
- 저자: Xun Liu, Yi Evie Zhang, Vira Kasprova, Parisa Rabbani, Pardis Sadat Zahraei, Tianyu Zhang, Ali Ebrahimpour-Boroojeny, Varun Chandrasekaran
- 식별자: `arxiv:2607.10059`

## 요약·초록

Agent systems based on large language models (LLMs) are increasingly deployed for autonomous tasks, yet existing evaluations mostly focus on task success rather than whether agents know when to abstain. This gap poses real risks: under ambiguity, conflicting constraints, or tool failures, agents may execute unintended and irreversible actions. To close this gap, we present the first systematic evaluation framework for agentic abstention: the calibrated ability of tool-using LLM agents to recognize when not to act. At its core, AgentAbstain is a paired-task benchmark built on an agent-native taxonomy of 8 abstention scenarios across pre-execution reasoning and runtime discovery. It contains 263 paired tasks across 42 executable sandbox environments, where each pair consists of a should-act task and a should-abstain variant produced through a controlled perturbation to the instruction, tool, or environment state. To scale this paired design and resist data contamination, we propose AbstainGen, a fully automated pipeline that synthesizes sandbox environments and generates paired tasks end-to-end, validated by deterministic replay and semantic LLM judges; fresh task instances can be regenerated on demand, and three independent annotators rate 94-98% of sampled tasks as well-designed. Across 17 frontier LLMs in 4 agent harnesses, the best agent (Gemini 3.1 Pro) achieves only 59.5% paired accuracy (correct on both the act and abstain sides of each paired task). More importantly, abstention capability is largely independent of general task-solving capability, indicating that scaling task-solving alone will not close this gap. We further identify failure modes such as post-hoc abstention, in which agents execute irreversible actions before recognizing abstention triggers. Our code and dataset are open-sourced at agentabstain.github.io.

## 내 메모



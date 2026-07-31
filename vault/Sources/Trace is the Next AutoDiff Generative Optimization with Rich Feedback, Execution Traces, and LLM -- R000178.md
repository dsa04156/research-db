---
type: research-source
item_id: 178
title: "Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs"
source: "arxiv"
published: "2024-06-23T21:05:31Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.16218"
url: "https://arxiv.org/abs/2406.16218v2"
generated_by: codex-research-db
aliases:
  - "Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs"
topics:
  - "self-evolving-harness"
---

# Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs

[원문 열기](https://arxiv.org/abs/2406.16218v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`7JWSBEW5`)
- 발행일: 2024-06-23T21:05:31Z
- 저자: Ching-An Cheng, Allen Nie, Adith Swaminathan
- 식별자: `arxiv:2406.16218`

## 요약·초록

We study a class of optimization problems motivated by automating the design and update of AI systems like coding assistants, robots, and copilots. AutoDiff frameworks, like PyTorch, enable efficient end-to-end optimization of differentiable systems. However, general computational workflows can be non-differentiable and involve rich feedback (e.g. console output or user's responses), heterogeneous parameters (e.g. prompts, codes), and intricate objectives (beyond maximizing a score). We investigate end-to-end generative optimization -- using generative models such as LLMs within the optimizer for automatic updating of general computational workflows. We discover that workflow execution traces are akin to back-propagated gradients in AutoDiff and can provide key information to interpret feedback for efficient optimization. Formally, we frame a new mathematical setup, Optimization with Trace Oracle (OPTO). In OPTO, an optimizer receives an execution trace along with feedback on the computed output and updates parameters iteratively. We provide a Python library, Trace, that efficiently converts a workflow optimization problem into an OPTO instance using PyTorch-like syntax. Using Trace, we develop a general LLM-based generative optimizer called OptoPrime. In empirical studies, we find that OptoPrime is capable of first-order numerical optimization, prompt optimization, hyper-parameter tuning, robot controller design, code debugging, etc., and is often competitive with specialized optimizers for each domain. We envision Trace as an open research platform for devising novel generative optimizers and developing the next generation of interactive learning agents. Website: https://microsoft.github.io/Trace/.

## 내 메모



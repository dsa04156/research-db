---
type: research-source
item_id: 1251
title: "When Agents Spend Watts: Measuring Performance-Energy Trade-offs in Agentic AI Systems with AgenticBench"
source: "openalex"
published: "2026-06-01"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:c03ceb177d859af2d982294afaea264147fe55ee02643d5cc2c880b39734bd9d"
url: "https://digitalcommons.calpoly.edu/theses/3324"
generated_by: codex-research-db
aliases:
  - "When Agents Spend Watts: Measuring Performance-Energy Trade-offs in Agentic AI Systems with AgenticBench"
topics:
  - "ai-agents"
  - "kubernetes"
---

# When Agents Spend Watts: Measuring Performance-Energy Trade-offs in Agentic AI Systems with AgenticBench

[원문 열기](https://digitalcommons.calpoly.edu/theses/3324)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`QZ45A356`)
- 발행일: 2026-06-01
- 저자: Logan J Barker
- 식별자: `url:c03ceb177d859af2d982294afaea264147fe55ee02643d5cc2c880b39734bd9d`

## 요약·초록

Agentic AI systems increasingly transform a single user request into a multi-step workflow of reasoning, tool use, retries, and framework coordination. Standard benchmark reporting emphasizes task accuracy, but this can hide the latency and energy-related cost of producing an answer. This thesis presents AgenticBench, a modular harness for evaluating agentic AI systems with task performance and execution-cost signals recorded together. AgenticBench integrates benchmark-owned scoring, framework adapters, deterministic task selection, energy profiling, SQLite persistence, and Pareto-style analysis. The main campaign evaluated an 84-cell matrix across four models, three agent frameworks, and six benchmarks on a Windows workstation with an NVIDIA RTX 2060; a secondary Nautilus Kubernetes extension validated GPU-local execution for local-model jobs and included an initial AutoGen Planner+Executor multi-agent pilot. The reported energy values are interpreted within explicit measurement boundaries: Windows GPU power was sampled through local nvidia-smi, Windows CPU and memory energy were estimated, and remote API rows capture client-observed runtime rather than server-side inference energy. Results show that no single model-framework pairing dominates all domains. AutoGen used more reported energy than LangChain in 20 of 24 matched single-agent cells, with a median ratio of 2.2x and a maximum of 15.8x. The Planner+Executor pilot shows why AgenticBench's multi-agent support matters: on small code-generation samples, a role-specialized multi-agent topology shifts the score-energy surface relative to single-agent baselines, but requires larger controlled trials before superiority claims are warranted. qwen3 reached high accuracy on hard reasoning tasks but produced long runtimes and timeout risk under extended reasoning, while llama3.2:3b with LangChain achieved a perfect HumanEval score at the lowest reported energy among non-baseline cells. These findings demonstrate that energy-aware benchmarking exposes design trade-offs that score-only evaluation misses and supports more transparent, sustainable selection of agentic AI architectures.

## 내 메모



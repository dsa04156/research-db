---
type: research-source
item_id: 1673
title: "AgentSLABench: Evaluating and Benchmarking Agentic Systems Under Resource Constraints"
source: "arxiv"
published: "2026-08-01T18:17:47Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.00805"
url: "https://arxiv.org/abs/2608.00805v1"
generated_by: codex-research-db
aliases:
  - "AgentSLABench: Evaluating and Benchmarking Agentic Systems Under Resource Constraints"
topics:
  - "ai-agents"
---

# AgentSLABench: Evaluating and Benchmarking Agentic Systems Under Resource Constraints

[원문 열기](https://arxiv.org/abs/2608.00805v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TU8J2EMM`)
- 발행일: 2026-08-01T18:17:47Z
- 저자: Meher Bhaskar Madiraju, Meher Sai Preetam Madiraju
- 식별자: `arxiv:2608.00805`

## 요약·초록

We present AgentSLABench, a resource-aware evaluation framework for autonomous AI agents that measures correctness alongside latency, cost, compute, memory, and network usage under declared resource budgets. Unlike standard benchmarks that report only accuracy, AgentSLABench produces a multi-dimensional profile per agent per task - the same way systems profilers (perf, pprof, cProfile) measure resource consumption of code, but extended with task correctness as a first-class dimension. AgentSLABench provides 16 task environments across 6 categories (5 core: multi-hop QA, retail substitution, code generation, web shopping, travel planning; 11 extended) with isolated Docker containers, declared CPU/memory/time/network budgets, sealed test sets with SHA256 hashes, and a standardized profiling protocol. We profile 5 general-purpose baseline agents (ReAct, PlanAndSolve, Reflexion, CoT, Random) plus 4 task-specialized agents, finding that specialized agents achieve 100% success on 3/5 core tasks (fact_qa, web_shopping, travel_planning) and 66.7-83.3% on retail and code_gen, while general baselines fail entirely on 4/5 domain tasks. Crucially, we report the Efficiency-Adjusted Success Rate (EASR) - success weighted by resource consumption relative to declared budgets - revealing that high accuracy at unbounded cost is not production-viable. We release the full infrastructure, sealed test sets, and profiling results to enable reproducible, resource-aware agent evaluation.

## 내 메모



---
type: research-source
item_id: 1086
title: "E-Bench: Benchmarking Multi-Step Tool-Use Agents in Real-World Product Scenarios"
source: "arxiv"
published: "2026-07-26T15:38:28Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.23722"
url: "https://arxiv.org/abs/2607.23722v1"
generated_by: codex-research-db
aliases:
  - "E-Bench: Benchmarking Multi-Step Tool-Use Agents in Real-World Product Scenarios"
topics:
  - "ai-agents"
---

# E-Bench: Benchmarking Multi-Step Tool-Use Agents in Real-World Product Scenarios

[원문 열기](https://arxiv.org/abs/2607.23722v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GXPCUXSM`)
- 발행일: 2026-07-26T15:38:28Z
- 저자: Weihuang Zheng, Tianyuan Zou, Eileen Ye, Alphet Liu, Youyong Kong, Ya-Qin Zhang, Duran Zheng, Maxm Pan
- 식별자: `arxiv:2607.23722`

## 요약·초록

Large Language Models (LLMs) are increasingly deployed as agents that interact with stateful environments over multiple steps: gathering hidden information, composing tool calls, and committing state changes. We refer to this capability as multi-step tool use. Existing benchmarks have advanced tool-use agent evaluation, but often focus on isolated API calls, short trajectories, or settings that are difficult to scale or control. We introduce E-Bench, a fully synthetic benchmark with 323 state-changing tasks across three product domains: Honor of Kings, QQ Music, and Tencent Meeting. E-Bench decouples environment synthesis from task synthesis: graph-guided database filling builds reusable, orphan-free product environments, while generator-solver asymmetry creates tasks with both an information gap and a tool gap, requiring agents to discover hidden data and compose multiple tool calls before changing state. Outcomes are graded deterministically by database-state diffs. Since both environments and tasks are synthetic, E-Bench is controllable at the environment level and scalable at the task level. Benchmarking 11 cutting-edge LLMs shows that multi-step tool use remains challenging: Pass^3 stays below 60% for the strongest models, and even with code execution in the E-Bench-Code extension, reliability (Pass^3) remains below 70%.

## 내 메모



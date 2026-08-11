---
type: research-source
item_id: 1864
title: "MoRSE: Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts"
source: "arxiv"
published: "2026-08-10T08:11:24Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.09251"
url: "https://arxiv.org/abs/2608.09251v1"
generated_by: codex-research-db
aliases:
  - "MoRSE: Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts"
topics:
  - "ai-agents"
---

# MoRSE: Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts

[원문 열기](https://arxiv.org/abs/2608.09251v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-10T08:11:24Z
- 저자: Peiwen Li, Shiyang Zhang, Yangtian Zhang, Sizhuang He, David van Dijk, Rex Ying
- 식별자: `arxiv:2608.09251`

## 요약·초록

Large language model-based multi-agent systems have recently shown strong potential for complex, long-horizon tasks. However, existing methods mainly rely on coarse prompt-level differentiation without parameter adaptation for diverse subtasks, resulting in insufficient inter-agent heterogeneity and limited specialized capability that bottleneck performance on tasks with complex requirements. To address this, we introduce a Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts (MoRSE) that distinguishes agents with (role, subtask)-conditional specialization at both the task structure and parameter levels. To make agents' responsibility explicit at the task structure level, we formulate a task-oriented multi-agent system that decomposes each task into a dependency-aware Directed Acyclic Graph of subtasks and assigns each agent a specific (role, subtask), introducing task-level specialization across collaborating agents. Additionally, to address the diverse role and subtask parameter adaptation demands, we propose a dynamic Mixture of (role, subtask) LoRA Experts module with a prototype-based semantic router for subtasks, augmenting agents with parameter-level specialization on a shared LLM substrate cost-effectively. Then, to co-optimize experts and router stably under sparse task rewards, we further propose a hierarchical group-relative policy optimization with two-layer credit assignment that isolates expert updates from the cross-route variance introduced by routing decisions, disentangling expert quality from routing quality. Experiments on code-generation benchmarks across three backbones demonstrate the effectiveness of our approach, with improvements in both whole-task and step-wise performance, and the gains from trained specialization generalize across held-out task categories and domains.

## 내 메모



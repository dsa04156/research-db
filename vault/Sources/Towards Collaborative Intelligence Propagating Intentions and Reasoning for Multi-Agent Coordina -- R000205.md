---
type: research-source
item_id: 205
title: "Towards Collaborative Intelligence: Propagating Intentions and Reasoning for Multi-Agent Coordination with Large Language Models"
source: "arxiv"
published: "2024-07-17T13:14:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.12532"
url: "https://arxiv.org/abs/2407.12532v1"
generated_by: codex-research-db
aliases:
  - "Towards Collaborative Intelligence: Propagating Intentions and Reasoning for Multi-Agent Coordination with Large Language Models"
topics:
  - "ai-agents"
---

# Towards Collaborative Intelligence: Propagating Intentions and Reasoning for Multi-Agent Coordination with Large Language Models

[원문 열기](https://arxiv.org/abs/2407.12532v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KUKNK8M6`)
- 발행일: 2024-07-17T13:14:00Z
- 저자: Xihe Qiu, Haoyu Wang, Xiaoyu Tan, Chao Qu, Yujie Xiong, Yuan Cheng, Yinghui Xu, Wei Chu, Yuan Qi
- 식별자: `arxiv:2407.12532`

## 요약·초록

Effective collaboration in multi-agent systems requires communicating goals and intentions between agents. Current agent frameworks often suffer from dependencies on single-agent execution and lack robust inter-module communication, frequently leading to suboptimal multi-agent reinforcement learning (MARL) policies and inadequate task coordination. To address these challenges, we present a framework for training large language models (LLMs) as collaborative agents to enable coordinated behaviors in cooperative MARL. Each agent maintains a private intention consisting of its current goal and associated sub-tasks. Agents broadcast their intentions periodically, allowing other agents to infer coordination tasks. A propagation network transforms broadcast intentions into teammate-specific communication messages, sharing relevant goals with designated teammates. The architecture of our framework is structured into planning, grounding, and execution modules. During execution, multiple agents interact in a downstream environment and communicate intentions to enable coordinated behaviors. The grounding module dynamically adapts comprehension strategies based on emerging coordination patterns, while feedback from execution agents influnces the planning module, enabling the dynamic re-planning of sub-tasks. Results in collaborative environment simulation demonstrate intention propagation reduces miscoordination errors by aligning sub-task dependencies between agents. Agents learn when to communicate intentions and which teammates require task details, resulting in emergent coordinated behaviors. This demonstrates the efficacy of intention sharing for cooperative multi-agent RL based on LLMs.

## 내 메모



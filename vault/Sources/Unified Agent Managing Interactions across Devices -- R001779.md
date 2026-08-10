---
type: research-source
item_id: 1779
title: "Unified Agent: Managing Interactions across Devices"
source: "arxiv"
published: "2026-08-06T08:14:33Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.05729"
url: "https://arxiv.org/abs/2608.05729v1"
generated_by: codex-research-db
aliases:
  - "Unified Agent: Managing Interactions across Devices"
topics:
  - "ai-agents"
---

# Unified Agent: Managing Interactions across Devices

[원문 열기](https://arxiv.org/abs/2608.05729v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-06T08:14:33Z
- 저자: Xinshuang Liu, Runfa Blark Li, Shaoxiu Wei, Xin Lin, Truong Nguyen
- 식별자: `arxiv:2608.05729`

## 요약·초록

As capabilities rapidly increase, AI agents can move from running inside one app to acting across a user's devices over time. Yet existing agent systems still fall short in this scenario. This is because observations are scattered across devices and moments, but mainstream systems are not designed around this fact: a single agent that treats devices as tools lacks effective state management for all devices across time, and multi-agent systems coordinate across agents but do not maintain the compact carried state a cross-device, cross-time request needs. We argue that the agent should maintain an effectively designed state that organizes engagement evidence, stated facts, and the standing request in a compact, action-ready form for deciding its action given the current observation. To compare state designs, we construct a benchmark of user-agent interaction across devices and time. We instantiate this principle in Unified Agent, a stateful agent that carries interaction evidence across devices and moments and uses it with the current observation to act. In the default setting, it significantly outperforms our adaptations of four published designs. Across changes in multimodal large language model (MLLM) family, capability, and reasoning effort, it remains ahead of all compared systems, demonstrating that the state-design advantage is robust across MLLM settings. Our code and data will be publicly available on GitHub.

## 내 메모



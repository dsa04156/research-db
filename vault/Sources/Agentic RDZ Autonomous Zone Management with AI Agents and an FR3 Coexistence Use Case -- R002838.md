---
type: research-source
item_id: 2838
title: "Agentic RDZ: Autonomous Zone Management with AI Agents and an FR3 Coexistence Use Case"
source: "arxiv"
published: "2026-09-15T12:40:25Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.17110"
url: "https://arxiv.org/abs/2609.17110v1"
generated_by: codex-research-db
aliases:
  - "Agentic RDZ: Autonomous Zone Management with AI Agents and an FR3 Coexistence Use Case"
topics:
  - "ai-agents"
---

# Agentic RDZ: Autonomous Zone Management with AI Agents and an FR3 Coexistence Use Case

[원문 열기](https://arxiv.org/abs/2609.17110v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-15T12:40:25Z
- 저자: Minh Dat Nguyen, Gabriele Gemmi, Tamerlan Aghayev, Paolo Testolina, Michele Polese, Tommaso Melodia
- 식별자: `arxiv:2609.17110`

## 요약·초록

Radio Dynamic Zones (RDZs) allow wireless experiments to operate outside conventional spectrum regulations while continuously guaranteeing protection for incumbent users. Existing RDZ prototypes automate this task procedurally, through handcrafted rules and predefined workflows, and become brittle when experiments encounter hardware impairments, user workflows and devices, or interference mechanisms not anticipated at design time. This paper introduces the agentic RDZ (A-RDZ), which, to the best of our knowledge, is the first RDZ realization in which agents use Large Language Models (LLMs) to perform spectrum management, experiment management, policy interpretation, and zone orchestration. Built on the GENESIS agentic framework, the architecture pairs autonomous reasoning with a deterministic policy gate and near-real-time (near-RT) reflexes, so that agents can improve outcomes but never weaken the zone's protection guarantee. We validate the A-RDZ on a hardware-in-the-loop Frequency Range 3 (FR3) (7.125-24.25 GHz) Open Radio Access Network (O-RAN) testbed in which a 5G New Radio (NR) experiment coexists with an emulated Fixed Satellite Service (FSS) earth-station incumbent. In an end-to-end use case, the monitoring agent detects an emission violation from live spectrum evidence, the orchestrator selects a mitigation that restores the interference budget while keeping the experiment running, and the action is applied and verified through the O-RAN control plane. We report the detection-to-mitigation latency decomposition and discuss the practical limits of agentic operation, including non-deterministic reasoning and decision-to-action translation.

## 내 메모

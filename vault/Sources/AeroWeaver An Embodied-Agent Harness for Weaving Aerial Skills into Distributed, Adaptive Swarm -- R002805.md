---
type: research-source
item_id: 2805
title: "AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution"
source: "arxiv"
published: "2026-09-16T11:49:38Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.18520"
url: "https://arxiv.org/abs/2609.18520v1"
generated_by: codex-research-db
aliases:
  - "AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution"
topics:
  - "self-evolving-harness"
---

# AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution

[원문 열기](https://arxiv.org/abs/2609.18520v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-16T11:49:38Z
- 저자: Jiabin Lou, Yirong Yang, Haopeng Wang, Xuxin Lv, Xinyu Liu, Diyuan Hou, Xuehong Liu, Rongye Shi, Wenjun Wu
- 식별자: `arxiv:2609.18520`

## 요약·초록

Collective intelligence is a collaborative autonomy paradigm in which multiple agents pursue shared objectives through local perception, information exchange, and coordinated action. UAV swarms embody this paradigm by coordinating multiple vehicles in tasks such as search, inspection, and tracking. Recent advances in large language model (LLM) agents have strengthened natural-language task understanding and high-level planning, providing a flexible semantic interface between mission descriptions and collective behavior. While these advances expand semantic reasoning, applying LLM agents to UAV swarms raises challenges in grounding model decisions in executable capabilities, reconciling global task reasoning with distributed execution, and using mission-specific experience for continual adaptation. To address these challenges, we introduce AeroWeaver, an embodied-agent harness that weaves individual UAV skills into coordinated mission-level behavior. AeroWeaver connects semantic decisions to governed skills, organizes role-conditioned local agents for distributed coordination, and uses role-indexed state-action-reward experience to refine skill selection online. Experiments and runtime validation show that AeroWeaver maintains valid skill execution under tested conditions and supports body-local multi-UAV operation without a central agent generating joint actions from global context, while reward-guided online updates provide a training-free path for adaptive learning swarm agents from accumulated execution experience. Code: https://github.com/Admire-ljb/AeroWeaver.

## 내 메모

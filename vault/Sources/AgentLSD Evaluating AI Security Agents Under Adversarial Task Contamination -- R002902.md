---
type: research-source
item_id: 2902
title: "AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination"
source: "arxiv"
published: "2026-09-16T17:58:55Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "doi:10.1145/3847352.3848111"
url: "https://arxiv.org/abs/2609.19140v1"
generated_by: codex-research-db
aliases:
  - "AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination"
topics:
  - "ai-agents"
---

# AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination

[원문 열기](https://arxiv.org/abs/2609.19140v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`4UNAIDX3`)
- 발행일: 2026-09-16T17:58:55Z
- 저자: Matteo Golinelli, Idilio Drago, Matteo Boffa, Francesco Bergadano, Bruno Crispo
- 식별자: `doi:10.1145/3847352.3848111`

## 요약·초록

AI agents for security inspect web pages, source code, logs, configuration files, and command outputs. These environments may contain deceptive artifacts that influence the agent's behavior. We call this adversarial task contamination. Whereas prompt injection relies on attacker-supplied instructions, task contamination also includes non-instructional evidence, such as fake results and decoy endpoints. We present AgentLSD, a controlled framework for studying adversarial task contamination. AgentLSD uses Capture the Flag (CTF) challenges as its experimental environment. We inject trap artifacts, such as fake flags, misleading hints, decoy endpoints, and hidden cues, while preserving the intended CTF solution. The framework supports paired clean and trap-augmented experiments with deterministic trap generation, runtime injection, telemetry, and delivery verification. We evaluate six models on 11 web CTF challenges. In the clean condition, agents capture 41% of the flags, and no model solves every challenge. We then measure the impact of task contamination. Even when the agent still recovers the flag, traps increase the number of turns (+20) and reasoning tokens (+2k). Solve-rate effects are more heterogeneous, as some model-challenge pairs are largely unaffected while others follow decoys or submit wrong flags. These results show that clean CTF performance understates vulnerability to deceptive task evidence. AgentLSD isolates this effect and provides a reproducible benchmark for studying it. We release the framework, configurations, trap specifications, and raw traces.

## 내 메모



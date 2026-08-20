---
type: research-source
item_id: 2097
title: "CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills"
source: "arxiv"
published: "2026-08-17T08:20:44Z"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "arxiv:2608.16246"
url: "https://arxiv.org/abs/2608.16246v1"
generated_by: codex-research-db
aliases:
  - "CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills"
topics:
  - "ai-agents"
---

# CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills

[원문 열기](https://arxiv.org/abs/2608.16246v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TPMQDICF`)
- 발행일: 2026-08-17T08:20:44Z
- 저자: Mingxiao Liu, Zhoumian Jiang, Jianan Ma, Jian Zhang, Jialuo Chen, Xinhao Deng, Zhen Wang
- 식별자: `arxiv:2608.16246`

## 요약·초록

Autonomous AI agents tackling Long Horizon Tasks depend on marketplace skills that are certified one at a time: a scanner returns a safety verdict for each skill and declares the ecosystem safe if every package passes. We show that this assumption fails under skill composition. A skill may pass the per-skill scanner individually yet participate in a risky composition when an agent connects its outputs, capabilities, or side effects with those of other scanner-passing skills. This makes skill composition risk a path level property rather than a node level property, explaining why existing skill scanners that inspect individual packages achieve limited interception. To study this threat, we present CompoSkill, a framework that constructs skill composition attacks through a dual attacker system. The white-box attacker knows the victim's installed skill pool and directly injects explicit skill-id sequences; the black-box attacker knows only a role profile, downloads the top marketplace skills for that scenario, builds a Skill Composition Graph, and searches for high risk chains whose implicit lures never name skill identifiers. We further construct CompoSkill-Bench, a benchmark of 1,140 records built from long-horizon professional workflows across five threats and six scenarios on OpenClaw and Nanobot. CompoSkill achieves risk Chain Formation Rates (CFR) up to 83.3% in the white box setting and 80.6% in the black box setting, while existing skill scanners block only a limited fraction of the risky compositions. Finally, we observe a bridge-bonus-then-hop-decay pattern: a bridge skill can increase attack success, but Attack Success Rate (ASR) decreases once additional hops make the risk chain longer than three skills. These results expose a systematic gap in single skill certification for autonomous AI agents.

## 내 메모



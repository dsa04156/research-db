---
type: research-source
item_id: 1856
title: "HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses"
source: "arxiv"
published: "2026-08-07T09:03:49Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.06984"
url: "https://arxiv.org/abs/2608.06984v1"
generated_by: codex-research-db
aliases:
  - "HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses"
topics:
  - "self-evolving-harness"
---

# HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses

[원문 열기](https://arxiv.org/abs/2608.06984v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-07T09:03:49Z
- 저자: Xiao Zhang, Yusheng Wang, Yuhao Fei, Dongyuan Li, Zian Liang, Liuyu Xiang, Hongxun Gu, Zhaofeng He
- 식별자: `arxiv:2608.06984`

## 요약·초록

Modern agent harnesses persist state across tasks and sessions through persistent carriers like memory, skills, tools, and shared artifacts. However, this capability creates delayed safety risks: attacker-influenced content can cross system boundaries and later affect the execution of a benign request. Existing benchmarks typically focus on a few carriers or harnesses, while end-to-end attack-success rates reveal little about how risks propagate. To this end, we present HarnessSafe, a benchmark comprising 328 executable cases across seven persistent-carrier families and evaluated on most mainstream agent harnesses. Each case is specified as a Persistent-Risk Lifecycle that traces attacker influence from its initial entry, through persistence across carriers and system boundaries, to a later benign trigger and an observable violation. We further introduce a multi-stage, trace-based evaluation that uses observable execution evidence to determine how far each attack chain progresses and where it is stopped. Experiments show that containment is carrier-specific and strongly depends on the harness-model configuration. Both the harness and model backend substantially shape containment outcomes, while attack success rates cannot reflect distinct lifecycle progression patterns.

## 내 메모



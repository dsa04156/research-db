---
type: research-source
item_id: 2010
title: "Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents"
source: "openalex"
published: "2026-08-12"
first_seen: "2026-08-18"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2608.11888"
url: "https://arxiv.org/abs/2608.11888"
generated_by: codex-research-db
aliases:
  - "Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents"
topics:
  - "ai-agents"
---

# Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents

[원문 열기](https://arxiv.org/abs/2608.11888)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-18|2026-08-18]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`9PGNUREJ`)
- 발행일: 2026-08-12
- 저자: Gen Dong, Yanjie Gao, Liqun Li, Tianyin Xu, Yu Hua, Fan Yang
- 식별자: `doi:10.48550/arxiv.2608.11888`

## 요약·초록

Agent skills are the de facto mechanism for extending LLM agents with reusable guidance. A skill can shape the agent's task execution, including planning, tool use, problem-solving, and validation. Prior work reported mixed results of agent skills: some skills improve task success rates, while others have no effect, increase token use and execution time, and even reduce success rates. This paper presents a comprehensive analysis of skill-induced agent failures by attributing task failures and cost regressions to specific loaded skills. We introduce a differential analysis framework that attributes a failure or regression to a skill by comparing a target skill-guided run against a no-skill or semantically matched skill reference run that solves the same task, or solves it more cheaply. We instantiate this framework on SkillsBench and SWE-Skills-Bench, yielding 307 skill-induced failures, including 125 functional failures and 182 efficiency regressions. We also build SkillTriage, a taxonomy-guided attribution tool that normalizes paired cases, extracts differential evidence, and produces triage reports. Our major findings include: (1) Skill induced functional failures are rarely caused by obviously irrelevant skills; instead, seemingly relevant skills often make the agent incorrectly implement or omit task-required implementation elements. (2) Skill-induced efficiency regressions are not explained by prompt length alone. (3) The largest sources within Excessive Procedure are excessive verification and heavy implementation pipelines, contributing 67 and 30 cases, respectively. This shows that skills often turn validation checklists and construction recipes into mandatory work. Based on our findings, we propose research topics and tooling improvements for safer and more cost-aware skill reuse.

## 내 메모



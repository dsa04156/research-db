---
type: research-source
item_id: 1157
title: "SpecBench: Evaluating Specification-Level Reasoning for Software Engineering LLM Agents"
source: "arxiv"
published: "2026-05-28T17:54:01Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.30314"
url: "https://arxiv.org/abs/2605.30314v1"
generated_by: codex-research-db
aliases:
  - "SpecBench: Evaluating Specification-Level Reasoning for Software Engineering LLM Agents"
topics:
  - "kubernetes"
---

# SpecBench: Evaluating Specification-Level Reasoning for Software Engineering LLM Agents

[원문 열기](https://arxiv.org/abs/2605.30314v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NF8DHT2H`)
- 발행일: 2026-05-28T17:54:01Z
- 저자: Grant Hamblin, Kevin Song, Zhanda Zhu, Anand Jayarajan, Sihang Liu, Nandita Vijaykumar, Gennady Pekhimenko
- 식별자: `arxiv:2605.30314`

## 요약·초록

Software engineering (SWE) agents are transitioning from code generation to full software development lifecycle automation. A critical phase in this lifecycle is specification design: transforming initial proposals into carefully considered requirements through expert review. Existing benchmarks such as SWE-Bench are implementation-focused by measuring the agent's ability to generate code given fixed, precise design requirements. This formulation assumes specifications are correct and complete. In real-world complex and critical software systems, initial specifications are often incomplete and flawed, requiring extensive expert reviews and revisions before being accepted for implementation. To fill this gap, we introduce SpecBench to evaluate specification-level reasoning: the ability to generate complete, unambiguous, consistent, and correct system specifications. SpecBench tasks are derived from the Request for Comments (RFC) process used by mature open-source projects. For each task, an agent is given an initial design proposal, the project codebase, and all past project RFC discussions. The agent is tasked with identifying specification deficiencies: omissions, ambiguities, inconsistencies, or incorrect assumptions in the initial proposal. We evaluate predictions against critiques raised by expert maintainers during historical RFC reviews. SpecBench contains tasks from 5 diverse repositories: Kubernetes, React, Rust, TVM, and vLLM. We evaluate state-of-the-art SWE agents on SpecBench, analyzing their capacity to reason about system design without execution feedback. The best performing agent, GPT-5.4, achieves 44.4% accuracy.

## 내 메모



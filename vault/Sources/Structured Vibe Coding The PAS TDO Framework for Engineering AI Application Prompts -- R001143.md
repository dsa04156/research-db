---
type: research-source
item_id: 1143
title: "Structured Vibe Coding: The PAS/TDO Framework for Engineering AI Application Prompts"
source: "openalex"
published: "2026-07-24"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.5281/zenodo.21524934"
url: "https://doi.org/10.5281/zenodo.21524934"
generated_by: codex-research-db
aliases:
  - "Structured Vibe Coding: The PAS/TDO Framework for Engineering AI Application Prompts"
topics:
  - "ai-agents"
---

# Structured Vibe Coding: The PAS/TDO Framework for Engineering AI Application Prompts

[원문 열기](https://doi.org/10.5281/zenodo.21524934)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`8TH8AXV5`)
- 발행일: 2026-07-24
- 저자: Muhammad Omar
- 식별자: `doi:10.5281/zenodo.21524934`

## 요약·초록

Abstract Generative AI (GenAI) applications are non-deterministic. That is the same input can produce different outputs from run to run, and increasingly it is the prompt, not a line of code, that stands between an unpredictable model, and a system people can rely on. Despite this, most AI-powered applications (i.e., applications with a generative-model component, however small — see P7 §7.7 for scope boundaries) are still built through informal, intuition-driven prompting, often called "vibe coding," with little connection to the requirements and design discipline that conventional software engineering (SE) treats as routine. This document brings that discipline back into the picture. It presents Structured Vibe Coding (SVC), a methodology that replaces ad hoc prompting with a structured, traceable process, along with PAS/TDO, a six-component prompt notation (Persona, Architecture, and Safety for the System Prompt; Task, Domain, and Output for the User Prompt) that refines the author's earlier three-part Instruction/Context/Constraints (ICC) framework. At the center of the framework is Source of Truth Mapping: every clause in a compiled prompt must trace back to a specific line in one of two lightweight, tiered documents — an SRS Lite (Software Requirements Specification) or an SDD Lite (Software Design Document)— rather than being written from memory or guesswork. Two mechanisms make this practical. A project's Data Flow Diagram converts directly into the Chain-of-Thought reasoning sequence given to the model, so a diagram engineers already draw becomes a derived prompt artifact rather than an invented one. And prompt development follows a two-phase lifecycle: an exploratory phase with high model temperature and loosely worded, inspirational constraints, followed by a production phase with low temperature and strict, guardrail-worded constraints, so that neither premature rigidity nor unreliable looseness takes hold. A companion Iteration Log turns production failures into a systematic, root-cause diagnostic exercise across all six prompt components, plus temperature and process-level failures —extending an earlier three-category diagnostic model. The framework is put to work in three complete, worked case studies spanning different architectural patterns and stakes: a multilingual halal ingredient classifier, a medicine label explainer for community health workers, and a retrieval-augmented job-market skills analyzer. The third case study is the most telling — it shows, rather than simply argues, that the framework needs real architectural extension, not just a drop-in adjustment, once domain knowledge comes from a live retrieval pipeline instead of static, expert-reviewed text. Beyond these three applications, the document points to a range of indirect uses for the framework's artifacts that don't require deploying any AI system at all — audit-ready compliance documentation, team onboarding material, and, in keeping with the framework's roots in software engineering, specifications that can simply be handed to a human developer. The limitations are stated as plainly as the contributions. The framework has only been validated for single-agent, largely single-interaction applications; long-running multi-turn or multi-session systems, multi-agent orchestration, large dynamic tool-use action spaces, and streaming output all remain untested. No empirical comparison against ad hoc prompting has been carried out yet. Instead, the document lays out a tiered evaluation methodology —spanning analytical, non-human empirical, and human-subject methods —covering internal effectiveness, token and cost efficiency, and external software quality against ISO/IEC 25010, as a concrete foundation for that future work. The framework is meant to engineer the AI-interaction layer of a system, not to replace the software development lifecycle around it. It is written for an international audience of students, practitioners, researchers, and engineering managers, organized so each can go directly to what matters most to them. Keywords: prompt engineering, requirements engineering, software design, generative AI applications, retrieval-augmented generation, AI safety, structured vibe coding, non-deterministic systems, software quality evaluation, software engineering education

## 내 메모



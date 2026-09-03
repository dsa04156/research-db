---
type: research-source
item_id: 2533
title: "Autonomous Trust: Self-Gating Evaluation as a Prerequisite for Agent-to-Agent Communication at Scale"
source: "openalex"
published: "2026-09-01"
first_seen: "2026-09-03"
review_status: "pending"
canonical_key: "doi:10.63412/rq21yh44"
url: "https://doi.org/10.63412/rq21yh44"
generated_by: codex-research-db
aliases:
  - "Autonomous Trust: Self-Gating Evaluation as a Prerequisite for Agent-to-Agent Communication at Scale"
topics:
  - "self-evolving-harness"
  - "ai-agents"
---

# Autonomous Trust: Self-Gating Evaluation as a Prerequisite for Agent-to-Agent Communication at Scale

[원문 열기](https://doi.org/10.63412/rq21yh44)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-03|2026-09-03]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`KE3C3QRJ`)
- 발행일: 2026-09-01
- 저자: Nehal Sangoi, Kris Feldmann, Deven Yadav, Sandeep Loi, Karan Gandhi
- 식별자: `doi:10.63412/rq21yh44`

## 요약·초록

As autonomous agents backed by large language models (LLMs) move from single-user assistants toward peer systems that transact directly with one another, the volume of agent-to-agent (A2A) communication is projected to reach a scale comparable to today’s host-to-host network traffic. At that scale, no human reviewer can vet each outbound action, yet LLM output quality is non-stationary: a single model can produce an excellent decision at one turn and an unsafe or incoherent one at the next, with no guarantee tied to prior behavior. This paper argues that trust in such systems cannot be modeled on human trust, which is accumulated through track record, nor can it be delegated to the LLM itself, since the model is fundamentally an input-output function with no internal mechanism for self-policing. We propose Autonomous Trust, a framework in which trustworthiness is engineered as a property of the agent as a whole (LLM plus an external evaluation layer) rather than of the model in isolation. The framework rests on four design principles: (1) pre-transmission self-gating, in which the sending agent, not only the receiver, is responsible for intercepting its own unsafe outputs before they leave the system; (2) a verifiability taxonomy that routes each action to an appropriate gating strategy, from deterministic checks to LLM-panel adjudication; (3) continuous self-reported quality telemetry, analogous to application health metrics, that exposes an agent’s own output degradation to external monitoring in real time; and (4) explicit treatment of the gameable verifier" failure mode, in which self-evolving agents can degrade their own automated checks (for example, by authoring tests engineered to always pass). We formulate the design space, analyze failure modes including judge-panel correlated blind spots, and outline an empirical evaluation plan. This work contributes a concrete engineering framework, not a purely theoretical trust model, toward the near-term infrastructural challenge of building safe, unsupervised, internet-scale agent ecosystems.

## 내 메모



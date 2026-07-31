---
type: research-source
item_id: 1155
title: "Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight"
source: "arxiv"
published: "2026-06-04T17:50:54Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.06460"
url: "https://arxiv.org/abs/2606.06460v3"
generated_by: codex-research-db
aliases:
  - "Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight"
topics:
  - "kubernetes"
---

# Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight

[원문 열기](https://arxiv.org/abs/2606.06460v3)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GPM2QPD7`)
- 발행일: 2026-06-04T17:50:54Z
- 저자: Thamilvendhan Munirathinam
- 식별자: `arxiv:2606.06460`

## 요약·초록

Autonomous LLM agents increasingly hold real credentials and operate infrastructure with no human in the loop, yet operators have no standard way to tell an agent a resource is off-limits, or to ask a running agent to stand down: access controls either admit it or hard-fail it. We propose a third mode -- the Recuse Signal, a lightweight in-band governance signal a server emits over a protocol's existing channels (an SSH banner, a PostgreSQL NOTICE, a Kubernetes admission warning) asking an automated agent to voluntarily withdraw. It is a cooperative control, the robots.txt analogue for live access -- explicitly not a security boundary. We define it as an open mini-standard (access-time directives deny/throttle/warn and a mid-task halt), build three live-validated adapters, and measure compliance across five LLM agents (GPT-4o, GPT-4o-mini, Claude Sonnet 4.5, Gemini 2.5 Flash, and an open-weights Llama-3.3-70B). At the access door, compliance is real but strongly model-dependent: deny recusal ranges from 100% (GPT-4o-mini, Claude) to 55-75% (Gemini, GPT-4o), while the open-weights agent barely engaged the signal. Agents honor the standard's directive granularity -- they do not over-withdraw on the permissive throttle/warn (0/176) -- but throttle produced no measurable self-limiting, and no agent ever surfaced a warn to the operator (0/100). Mid-flight, a halt stops nobody: across 40 trials 0/40 stopped, and an in-band halt was never acknowledged (0/20) versus 20/20 as a prompt message -- yet even a fully-noticed halt stopped no one. Cooperative in-band signaling is thus reliable-but-model-dependent at the access door and unreliable in flight; stopping a running agent needs enforcement, not a request. We release the standard, adapters, and harness for reproduction.

## 내 메모



---
type: research-source
item_id: 1102
title: "Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings"
source: "arxiv"
published: "2026-07-24T04:19:45Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.21962"
url: "https://arxiv.org/abs/2607.21962v1"
generated_by: codex-research-db
aliases:
  - "Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings"
topics:
  - "ai-agents"
---

# Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings

[원문 열기](https://arxiv.org/abs/2607.21962v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`T6IWC3KF`)
- 발행일: 2026-07-24T04:19:45Z
- 저자: Quentin Spencer
- 식별자: `arxiv:2607.21962`

## 요약·초록

Benchmarks for LLM-agent memory typically generate conversations first and extract answer keys afterwards -- with documented label-error and contamination problems -- and they overwhelmingly measure short interaction histories. We invert the pipeline: a seeded life-script sampler emits facts with validity intervals, volatility classes, and source channels before any text exists; an LLM renderer writes chat and email from per-event fact manifests; a fidelity verifier confirms every planted fact; and questions are instantiated mechanically from the script, so gold answers are script-valid by construction and separately validated for answerability. The synthetic, fictionalized corpus (~380 questions, 15 types) embeds features absent from the benchmarks we survey: per-fact validity intervals, sent/received trust distinctions, injection probes in a benign harness, and as-of-date question sets. Benchmarking five memory architectures against a no-memory control (fixed answerer, versioned LLM judge, three replicates, two horizons), we find backend rankings invert with history length: the budgeted curated-map memory that leads at three weeks loses recall of evicted content by nine weeks (96% to 72%) while a provenance-typed graph rises to 90%; the inversion is positive for all six users under complete cross-family re-judging (exact p=0.031). A full-rendered-history baseline ties or exceeds the best memory system at the short horizon but shows no judge-independent advantage at nine weeks, at about twice the read cost. Write-stage quality strongly correlates with downstream quality (weakly-written facts fail 24% vs 2%), and injection resistance tracked whether provenance boundaries survive representation. A layered architecture performs best among the memory systems in both regimes (96.8% short-horizon) and is released as Veracium, an open-source library, with the corpus generator and harness.

## 내 메모



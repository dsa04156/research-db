---
type: research-source
item_id: 2818
title: "NovaFabric: Tamper-Evident, Replayable Evidence for Autonomous AI Agent Runs"
source: "openalex"
published: "2026-09-11"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2609.12582"
url: "https://arxiv.org/abs/2609.12582"
generated_by: codex-research-db
aliases:
  - "NovaFabric: Tamper-Evident, Replayable Evidence for Autonomous AI Agent Runs"
topics:
  - "ai-agents"
---

# NovaFabric: Tamper-Evident, Replayable Evidence for Autonomous AI Agent Runs

[원문 열기](https://arxiv.org/abs/2609.12582)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`2NBE8UQ7`)
- 발행일: 2026-09-11
- 저자: Mohsen Seyedkazemi Ardebili
- 식별자: `doi:10.48550/arxiv.2609.12582`

## 요약·초록

When an autonomous AI agent does something consequential, what can be proven about what it did? Agent-observability platforms capture traces, but a trace is mutable: alterable undetected, with no recipe for re-executing it, silent on whether captured secrets were removed. Regulation (EU AI Act, ISO 42001, NIST AI RMF) presumes records an independent party can check. We present NovaFabric, producing audit-grade execution evidence: provider-neutral, tamper-evident, replayable, shareable. It records an agent run, without modifying agent logic, into a portable Run Capsule (fifteen-entity schema), sealed with a holistic DSSE signature, RFC 3161 timestamp, Merkle log and redaction attestation. Sealed runs are re-executable under a four-mode replay protocol and exportable as an Evidence Bundle for third-party verification with stock tooling (specified, not evaluated). The contribution is integration, not new cryptography: OpenTelemetry, DSSE/in-toto and W3C PROV. We evaluate eight research questions at measured scope. Mocked replay serves every model response from the capsule (no live model call, 10/10) but is offline w.r.t. models, not the network; only 2/10 tool-using workloads completed; the gap is missing tool-response substitution. Tampering is rejected across three tested classes. Declared-stream completeness is 0.652 (95% CI +/-0.064, ten scenarios). A repaired rule pack redacts 14/14 credential types, preserving 9/9 decoys; diff localises 140/140 mutations. Blast-radius queries: 45.5ms p99 over 10M edges (3.3x faster than a columnar baseline), 167.9ms over 100M (1 client, n=30). A 314-machine, ten-region run finds capsule REST ingest lossless but capped at 61.6 req/s (p99 26.8s) by per-worker serialisation. Six defects found in NovaFabric and its evaluation corpus: four fixed, one withdrawn, one open. Verification is conditional on a stated trusted computing base.

## 내 메모

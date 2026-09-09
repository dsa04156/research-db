---
type: research-source
item_id: 2653
title: "A Governance Methodology Layer for AI-Assisted Software Development: Defect Taxonomy, Controlled Ablation, and Process-Over-Capability Evidence"
source: "openalex"
published: "2026-09-07"
first_seen: "2026-09-08"
review_status: "pending"
canonical_key: "doi:10.5281/zenodo.22558450"
url: "https://arxiv.org/abs/2603.25723"
generated_by: codex-research-db
aliases:
  - "A Governance Methodology Layer for AI-Assisted Software Development: Defect Taxonomy, Controlled Ablation, and Process-Over-Capability Evidence"
topics:
  - "ai-agents"
---

# A Governance Methodology Layer for AI-Assisted Software Development: Defect Taxonomy, Controlled Ablation, and Process-Over-Capability Evidence

[원문 열기](https://arxiv.org/abs/2603.25723)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-08|2026-09-08]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`GZJAGH3U`)
- 발행일: 2026-09-07
- 저자: Sungjin Kwon
- 식별자: `doi:10.5281/zenodo.22558450`

## 요약·초록

Autonomous coding agents produce output that passes syntactic checks — compilation, type safety, CI — at high velocity. Yet syntactic correctness does not imply semantic correctness: design boundaries, security invariants, and maintainability contracts remain structurally invisible to automated pipelines. This paper makes four contributions. First, we present a defect-class taxonomy grounded in five AI agent permission and governance modules, separating defects structurally detectable by static analysis from those requiring semantic review. Second, we describe a runtime-decoupled governance gate — a file-based protocol that reads generator output and emits a structured verdict without API coupling, hence portable across generators. Third, we formalize methodology-as-code: expressing a verification protocol as a version-controlled, executable artifact whose two layers separate portable methodology from host automation. Fourth, we report a controlled ablation experiment (E-ablation, N=5 artifacts, 8-item independent ground truth) comparing harness-structured review against a token-matched unstructured prompt. The structured condition records 62% lenient ground-truth recall against 50% for the unstructured condition, with 25% strict recall against 0%. A severity-grade differential reported earlier does not survive blind re-grading by three model families and a human rater, and is withdrawn (§6.6). The recall figures come from a single-session design that a later replication did not re-test (§8). Both conditions miss document-quality defects identified by a human QA reviewer, indicating complementarity between structured AI review and human process inspection. Within this sample, the results are consistent with the thesis that review-process design, rather than reviewer-model capability, is the dominant factor in critical-defect coverage for AI-assisted software development. Companion to "The Forge Harness: A Structured Methodology for Sustainable AI-Assisted Software Development" (Zenodo 10.5281/zenodo.20397565). Changes in v1.2 (2026-09-07). This version adds §6.6, reporting two replications of the E-ablation that were run in June 2026 but omitted from v1.1: a cross-session re-run of both conditions in ten fully independent sessions, and a blind re-grading of the pooled findings, repeated across three model families and one human rater. Two previously reported results are withdrawn as a consequence — the reading of the S-count differential as unstructured over-grading, and the between-condition false-positive-rate comparison — together with one non-overlapping finding cited in §6.3 that source inspection overturned. Limitation L1 is replaced, and a new limitation L8 (grade-boundary subjectivity) is added. The replications recomputed finding counts and severity distributions only: ground-truth recall, on which this paper’s central comparative claim rests, was not re-measured, and §8 L1 and §9 state this explicitly. Changes in v1.2.1 (2026-09-07). The §6.6 withdrawal is propagated into the abstract and the §11 conclusion, which v1.2 left unrevised; one sentence in §3.3 that read “This confirms” about a check that was not run now reads “This is consistent with”; the draft-version and companion header lines were removed, and the reference to the v1.0 methodology now cites the concept DOI. No results changed.

## 내 메모



---
type: research-source
item_id: 2515
title: "Don't Let the Model Write the YAML: Deterministic, Minimal-Diff GitOps Remediation from LLM-Proposed Field Changes"
source: "arxiv"
published: "2026-08-31T18:37:12Z"
first_seen: "2026-09-02"
review_status: "pending"
canonical_key: "arxiv:2609.00227"
url: "https://arxiv.org/abs/2609.00227v1"
generated_by: codex-research-db
aliases:
  - "Don't Let the Model Write the YAML: Deterministic, Minimal-Diff GitOps Remediation from LLM-Proposed Field Changes"
topics:
  - "kubernetes"
---

# Don't Let the Model Write the YAML: Deterministic, Minimal-Diff GitOps Remediation from LLM-Proposed Field Changes

[원문 열기](https://arxiv.org/abs/2609.00227v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-02|2026-09-02]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5MI9U6TC`)
- 발행일: 2026-08-31T18:37:12Z
- 저자: Pruthvi Davineni
- 식별자: `arxiv:2609.00227`

## 요약·초록

LLM agents increasingly diagnose incidents and propose remediations. In a GitOps workflow, applying a fix means editing a version-controlled config file, and the obvious implementation, having the model author the edited file or a diff, is what practitioners reach for first. Evaluating that choice on real Kubernetes manifests, we find no text-generation strategy is safe for unattended automation. Unified diffs are unsafe: under strict patching almost none apply, but that is an artifact, since a tolerant tool (GNU patch) applies 96%, yet silently misapplies about 1 in 7 (14-20%) with no error signal. Full-file rewrite is capability-dependent: a small model corrupts the file, while a frontier model is usually correct but non-deterministic (it silently drops a field or edits a neighbor on some runs) and must regenerate the whole file, costing O(file size) per edit. We present an alternative that separates the semantic decision (which resource, field, and value) from the syntactic act of editing the file. The agent emits only a structured field-change intent; a deterministic pipeline indexes manifests by (kind, name), locates the target scalar's exact character span via the YAML parser's node position marks, and replaces only that span in the raw text. Because the file is never re-serialized, the diff is minimal by construction, formatting and comments are preserved, and the edit is correct and deterministic independent of the model, at O(1) generation cost. The contribution is the pairing of an LLM-proposed intent with a deterministic, fail-closed application contract for GitOps. We implement it in KubeAstra (Apache-2.0) and release the benchmark. Our claim is scoped to faithful application of a known change; whether the change is right is left to human PR review.

## 내 메모



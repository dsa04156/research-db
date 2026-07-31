---
type: research-source
item_id: 69
title: "Ground-Side Mission Plan Compilation with Policy-as-Code Guardrails for Cloud-Native Satellite Platforms"
source: "openalex"
published: "2026-07-16"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.14798"
url: "https://arxiv.org/abs/2607.14798"
generated_by: codex-research-db
aliases:
  - "Ground-Side Mission Plan Compilation with Policy-as-Code Guardrails for Cloud-Native Satellite Platforms"
topics:
  - "kubernetes"
---

# Ground-Side Mission Plan Compilation with Policy-as-Code Guardrails for Cloud-Native Satellite Platforms

[원문 열기](https://arxiv.org/abs/2607.14798)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`GUKAJMBS`)
- 발행일: 2026-07-16
- 저자: Hsiu-Chi Tsai, Chan‐Jin Chung
- 식별자: `arxiv:2607.14798`

## 요약·초록

Onboard cloud-native runtimes for satellites are emerging on multiple tracks (ORCHIDE, Axiom Space's AxDCU-1, Kepler's Jetson nodes), but each assumes that the workflow artifacts it executes arrive from the ground. ORCHIDE's architecture document D3.1 states explicitly that "only the Deferred Phase is part of the ORCHIDE scope," and no open-source ground-side toolchain has been released by the consortium. We present Satellite Mission Compiler, a four-stage pipeline that addresses this gap: it takes a human-authored mission plan, checks it against machine-checkable structural and policy rules, and compiles it into the container-workflow artifacts that cloud-native satellite runtimes consume. The pipeline parses the plan against a Pydantic schema derived from public ORCHIDE materials, evaluates it against an OPA/Rego policy package of ten deny rules with documented provenance, compiles it into a typed WorkflowIntent intermediate representation, and renders it as Argo Workflow DAGs and Kueue Job manifests with Dynamic Resource Allocation (DRA) support. We classify pre-uplink loss events into four severity tiers tied to specific schema and policy checks, and anchor the layered-validation design in the safety reading of defense-in-depth (NASA-STD-8739.8B) rather than the security reading (NIST SP 800-53). The implementation is validated by golden translation evaluations, argo lint, an in-process baseline that reproduces OPA's decisions, and live single-node cluster submission, including a DRA-backed GPU admission cascade on Kueue v0.17.3 (re-validated on v0.18.3) and, on v0.18.3, a unified GPU+CPU device-class quota with a scheduler-level accelerator fallback. Six Model Context Protocol (MCP) tools expose the pipeline to AI agents. The compiler is released under EUPL-1.2 (DOI 10.5281/zenodo.21228150).

## 내 메모



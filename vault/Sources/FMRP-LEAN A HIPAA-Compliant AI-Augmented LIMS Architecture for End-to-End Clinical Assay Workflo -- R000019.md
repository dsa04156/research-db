---
type: research-source
item_id: 19
title: "FMRP-LEAN: A HIPAA-Compliant AI-Augmented LIMS Architecture for End-to-End Clinical Assay Workflow Optimization"
source: "arxiv"
published: "2026-07-22T17:11:52Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.20382"
url: "https://arxiv.org/abs/2607.20382v1"
generated_by: codex-research-db
aliases:
  - "FMRP-LEAN: A HIPAA-Compliant AI-Augmented LIMS Architecture for End-to-End Clinical Assay Workflow Optimization"
topics:
  - "self-evolving-harness"
---

# FMRP-LEAN: A HIPAA-Compliant AI-Augmented LIMS Architecture for End-to-End Clinical Assay Workflow Optimization

[원문 열기](https://arxiv.org/abs/2607.20382v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`F6Q89HXJ`)
- 발행일: 2026-07-22T17:11:52Z
- 저자: Eva McCord, Ernest Pedapati, Zag ElSayed
- 식별자: `arxiv:2607.20382`

## 요약·초록

Clinical biomarker workflows in translational research settings often rely on spreadsheet-driven tracking, manual quality control (QC) reconciliation, and loosely integrated systems, resulting in limited state visibility, delayed reporting, and increased operational risk. These challenges are particularly pronounced in multi-day assays such as Luminex-based quantification of Fragile X Messenger Ribonucleoprotein (FMRP), where HIPAA-compliant data governance, deterministic workflow progression, and coordinated communication across laboratory and clinical teams are required. This paper presents FMRP-LEAN, a HIPAA-compliant, AI-augmented Laboratory Information Management System (LIMS) architecture that formalizes biospecimen lifecycle management through a finite-state workflow model with explicit transition guards and dwell-time observability. The system integrates a self-hosted Supabase/PostgreSQL stack deployed within hospital-controlled infrastructure, hybrid edge-internal isolation with encrypted tunneling and loopback-only services, and bi-directional REDCap synchronization. A unified MRN-UUIDv7 identifier framework with QR-based tracking ensures traceable clinical-research linkage under PHI residency constraints. FMRP-LEAN incorporates automated statistical QC pre-screening and a governance-constrained AI operations module that operates exclusively on aggregate projections, with deterministic fallback guarantees. Deployment demonstrates improved workflow observability, reduced QC latency, and enhanced cross-role transparency between laboratory technicians, research coordinators, and patient-facing teams. The architecture provides a reproducible model for secure, state-explicit, and AI-augmented clinical research workflows in regulated healthcare environments.

## 내 메모



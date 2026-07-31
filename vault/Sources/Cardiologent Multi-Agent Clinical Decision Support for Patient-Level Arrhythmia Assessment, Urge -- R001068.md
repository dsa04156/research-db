---
type: research-source
item_id: 1068
title: "Cardiologent: Multi-Agent Clinical Decision Support for Patient-Level Arrhythmia Assessment, Urgency, and Management"
source: "arxiv"
published: "2026-07-28T06:43:39Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25340"
url: "https://arxiv.org/abs/2607.25340v1"
generated_by: codex-research-db
aliases:
  - "Cardiologent: Multi-Agent Clinical Decision Support for Patient-Level Arrhythmia Assessment, Urgency, and Management"
topics:
  - "ai-agents"
---

# Cardiologent: Multi-Agent Clinical Decision Support for Patient-Level Arrhythmia Assessment, Urgency, and Management

[원문 열기](https://arxiv.org/abs/2607.25340v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RH6JIDIA`)
- 발행일: 2026-07-28T06:43:39Z
- 저자: Sukju Oh, Moo-Yong Rhee, Jae-Sik Jang, Sukkyu Sun
- 식별자: `arxiv:2607.25340`

## 요약·초록

The same episode of atrial fibrillation is a minor finding in a healthy adult and grounds for anticoagulation in an elderly patient with hypertension: identical signal, opposite decision. Naming the rhythm is only the start; what determines a patient's outcome is the judgement that follows -- what the arrhythmia is across the whole record, what it means for this patient, and what should be done about it. Recent work pairing large language models with the ECG stops short of this, reading one recording without assembling a patient-level finding; and agentic systems built around it either receive the arrhythmia a device has already detected or target a different diagnostic task, stopping before the decision this task requires. We formulate patient-level arrhythmia decision support as a task and present Cardiologent, a multi-agent system that spans it from detection to decision. An agent for each signal -- a single ECG lead and the photoplethysmogram a wearable acquires -- grounds its window reading in measured features rather than a bare label; the readings are assembled into the patient's rhythm profile and, with the patient's own data, reasoned against clinical guidelines retrieved for the case, with a critic checking each conclusion against the guideline it cites. We evaluate the clinical decision rather than the report, across integrated diagnosis, clinical significance, and urgency and management. Cardiologent scores highest on every axis, first on every patient-level task under both cardiologists and an at-scale LLM judge -- whose agreement with the cardiologists (ICC 0.74, 0.66) matches theirs with each other (0.67). Because each conclusion traces to a cited guideline and is validated against expert cardiologists, it yields decisions a clinician can audit rather than act on blindly -- a step toward use in continuous monitoring.

## 내 메모



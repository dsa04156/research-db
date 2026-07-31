---
type: research-source
item_id: 1098
title: "SMEFT-Pheno-Agent: a natural-language-driven AI agent for machine-learning-assisted Standard Model Effective Field Theory phenomenology"
source: "arxiv"
published: "2026-07-24T14:08:52Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.22331"
url: "https://arxiv.org/abs/2607.22331v1"
generated_by: codex-research-db
aliases:
  - "SMEFT-Pheno-Agent: a natural-language-driven AI agent for machine-learning-assisted Standard Model Effective Field Theory phenomenology"
topics:
  - "ai-agents"
---

# SMEFT-Pheno-Agent: a natural-language-driven AI agent for machine-learning-assisted Standard Model Effective Field Theory phenomenology

[원문 열기](https://arxiv.org/abs/2607.22331v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`CHABRR35`)
- 발행일: 2026-07-24T14:08:52Z
- 저자: Yu-Chen Guo, Jie Wang, Ji-Chong Yang
- 식별자: `arxiv:2607.22331`

## 요약·초록

We present SMEFT-Pheno-Agent, a Python workflow guided by a natural-language AI agent to perform machine-learning-assisted Standard Model Effective Field Theory (SMEFT) phenomenology at high-energy colliders. The software coordinates twelve automated execution phases spanning configuration intake, environment validation, event generation, machine-learning selection, statistical inference, and final audit. At each phase boundary, the agent interprets natural-language intent to generate runnable parameter files and adapter invocations required for subsequent execution. Once the detector-level events are written, the agent automatically proposes key kinematic observables alongside candidate machine-learning algorithms suited to the specific data structure and analysis objectives. All numerical calculations are delegated strictly to validated domain tools, with MadGraph5_aMC@NLO, Pythia, Delphes generating collider simulations, and MLAnalysis extracting features. The agent cannot modify physical parameters outside the locked configuration, and all LLM-produced artifacts, including parameter files, observable choices, algorithm selections, and prose drafts, are documented in machine-readable phase manifests prior to execution. These manifests establish complete reproducibility and audit traceability for SMEFT phenomenology studies.

## 내 메모



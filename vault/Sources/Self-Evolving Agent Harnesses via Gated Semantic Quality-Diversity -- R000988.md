---
type: research-source
item_id: 988
title: "Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity"
source: "arxiv"
published: "2026-07-15T10:26:26Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.13683"
url: "https://arxiv.org/abs/2607.13683v1"
generated_by: codex-research-db
aliases:
  - "Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity"
topics:
  - "self-evolving-harness"
---

# Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity

[원문 열기](https://arxiv.org/abs/2607.13683v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`V3XA69RU`)
- 발행일: 2026-07-15T10:26:26Z
- 저자: Xiaotian Luo, Fengxingyu Wang, Chuanrui Hu, Dizhan Xue, Yafeng Deng
- 식별자: `arxiv:2607.13683`

## 요약·초록

An LLM agent's real-task performance is shaped as much by the harness around its model as by the frozen model itself: its prompts, injected knowledge, runtime control, and configuration. In deployment the harness is often the only lever available, so improving it automatically is the natural way to raise performance without touching the weights. The hard part is not generating changes but knowing which one truly helped. Self-generated feedback is noisy, and an apparent gain can be a measurement artifact or an edit that merely overfits the tasks it was tuned on. We present a self-evolving agent-harness framework that separates proposing changes from crediting them: a language model diagnoses failures and proposes patches, while all sampling, measurement, and significance testing are owned by deterministic code, so every credited improvement is trustworthy by construction. Patches populate a gated, categorical quality-diversity archive (GSME) keyed on the (WHERE x WHY) pathology an edit addresses rather than the tasks it fixes, an anti-overfitting inductive bias; generalization is measured on a sealed test scored only after evolution. Across seven domains with a frozen open-weight model, the harness is train-selected and scored once on a sealed test; its credited gains there are +9 to +15.5pp and retain 86-147% of the training gain, evidence they generalize rather than overfit. The winning patch tracks the model's dominant pathology, not its size or family: changing the model can change the pathology and the patch, while the same pathology-to-patch match recurs across two model families. What transfers is the diagnose-and-credit loop, not any specific harness.

## 내 메모



---
type: research-source
item_id: 2359
title: "ReproAgent: Contract-Guided Paper-to-Code Reproduction"
source: "arxiv"
published: "2026-08-25T09:19:00Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.24291"
url: "https://arxiv.org/abs/2608.24291v1"
generated_by: codex-research-db
aliases:
  - "ReproAgent: Contract-Guided Paper-to-Code Reproduction"
topics:
  - "ai-agents"
---

# ReproAgent: Contract-Guided Paper-to-Code Reproduction

[원문 열기](https://arxiv.org/abs/2608.24291v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3T44R7M6`)
- 발행일: 2026-08-25T09:19:00Z
- 저자: Xue Hu, Zewei Pan, Zhongyuan Wang, Zhou Liu, Zeli Su, Wentao Zhang
- 식별자: `arxiv:2608.24291`

## 요약·초록

Paper-to-code reproduction asks scientific AI agents to turn research papers into executable repositories that preserve the paper's method, protocol and artifacts. This is difficult because the specification is split: explicit paper content such as algorithms, metrics and artifacts is often lost across long agent trajectories, while implicit details such as framework defaults and conventions inherited from related work are absent from the paper. We introduce ReproAgent, a four-stage Prepare--Plan--Generate--Repair pipeline built around a persistent implementation contract with two channels: an implementation-requirement channel that turns paper snippets into code obligations, and a reference-evidence channel that retrieves content and structure evidence from related repositories. Both are bound to work packages, projected into file-level contracts, and consumed across generation and repair. On PaperBench Code-Dev, ReproAgent reaches the highest mean score among same-backbone scaffolds under both Claude-Sonnet-4.5 and Gemini-3-Flash. End-to-end channel ablations and per-paper cases support the contribution of both channels. Code and experimental artifacts are publicly available.

## 내 메모



---
type: research-source
item_id: 2425
title: "SkillZip Pro: Execution-Aware Dynamic Compression of Progressively Loaded Skills for Self-Evolving Agents"
source: "arxiv"
published: "2026-08-31T13:41:16Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.30785"
url: "https://arxiv.org/abs/2608.30785v1"
generated_by: codex-research-db
aliases:
  - "SkillZip Pro: Execution-Aware Dynamic Compression of Progressively Loaded Skills for Self-Evolving Agents"
topics:
  - "self-evolving-harness"
---

# SkillZip Pro: Execution-Aware Dynamic Compression of Progressively Loaded Skills for Self-Evolving Agents

[원문 열기](https://arxiv.org/abs/2608.30785v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`57DV65UN`)
- 발행일: 2026-08-31T13:41:16Z
- 저자: Xiaofan Bai, Chao Liu, Hongqiang Lin, Di Wu, Mingli Song, Xuan Jin, Xipeng Cao, Yuhong Li
- 식별자: `arxiv:2608.30785`

## 요약·초록

Production agent skills are directory bundles, not isolated prompts. The root is loaded at activation; references, schemas, scripts, assets, and nested subskills are loaded only when an execution path needs them. Compressing only the root misses most deployment cost and may move branch-specific details into the always-loaded context. Flattening instead destroys progressive-loading boundaries. We introduce \method, an evaluation-free compressor for complete, progressively loaded skill bundles. It leaves the agent harness unchanged and emits an ordinary directory. The method combines two safeguards. First, it compresses \emph{across files}, removing content from a reference or subskill when the root or a declared environment contract already provides it. Second, it preserves routing, so every required file and directly callable entry remains reachable after rewriting. Users can configure \method along two independent axes. \emph{One-Shot} mode rebuilds the full bundle; \emph{Continual} mode reuses state and applies Zip-on-Write after each evolution patch. \emph{Persistent} compression rewrites the shipped bundle to reduce storage and runtime context. \emph{Transient} compression keeps that bundle byte-identical and builds a task-specific view, reducing only per-run context after build cost. Entry contracts mark private, public, and conditional resources; a multi-entry audit preserves standalone public subskills. On a production content-moderation skill evaluated by our industrial multi-round harness, \method removes \hl{38\%} of skill bundle tokens and \hl{10.4\%} of end-to-end per-run tokens with no quality loss, while an unprotected 71\% configuration loses up to 26 accuracy points to one-sided false positives. On a multi-entry bundle, \method effeciently reduces token cost while near-perfectly preserving every route and public entry.

## 내 메모



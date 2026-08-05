---
type: research-source
item_id: 1669
title: "Control Under Compression: Reliability Frontiers for Tool-Using Agents"
source: "arxiv"
published: "2026-08-02T07:43:44Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.01056"
url: "https://arxiv.org/abs/2608.01056v1"
generated_by: codex-research-db
aliases:
  - "Control Under Compression: Reliability Frontiers for Tool-Using Agents"
topics:
  - "ai-agents"
---

# Control Under Compression: Reliability Frontiers for Tool-Using Agents

[원문 열기](https://arxiv.org/abs/2608.01056v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DQX7PPGH`)
- 발행일: 2026-08-02T07:43:44Z
- 저자: Yinghan Hou, Zongyou Yang
- 식별자: `arxiv:2608.01056`

## 요약·초록

Tool-using language-model agents are governed not only by task prompts but also by persistent system-side instructions that specify tools, arguments, policies, execution protocols, and recovery. Compressing these agent control contexts (ACCs) can reduce input cost and context use, yet existing prompt-compression evaluations do not reveal whether the resulting control remains operationally reliable. We introduce CompressAgent, an environment-verified benchmark for ACC compression across nine independently constructed ACCs, three task families, three fixed Qwen API model identifiers, six retained-context budgets, and 15,525 runs. We uncover a nonlinear, method-dependent reliability frontier. At 75% retained context, generic rewriting and section-based compression achieve 92.7% and 92.4% success, close to the 93.8% full-context baseline. Between 50% and 35%, methods diverge sharply; at 35%, section-based, obligation-aware, and generic rewriting achieve 47.0%, 39.0%, and 19.9%. At retained-context budgets from 25% to 10%, executable protocols become fragile. Reliability also varies substantially across ACCs, making universal compressor rankings inappropriate and motivating per-context qualification. Failure analysis shows that compression primarily surfaces as tool-execution and action-parsing errors. These findings recast ACC compression from token reduction into a runtime-reliability problem that must be evaluated through executable outcomes.

## 내 메모



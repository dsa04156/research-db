---
type: research-source
item_id: 1670
title: "What Could the Agent See at 19:05? Generating Temporal Enterprise Scenarios from Real Research and Replaying Them to Evaluate Agents"
source: "arxiv"
published: "2026-08-02T06:56:56Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.01042"
url: "https://arxiv.org/abs/2608.01042v1"
generated_by: codex-research-db
aliases:
  - "What Could the Agent See at 19:05? Generating Temporal Enterprise Scenarios from Real Research and Replaying Them to Evaluate Agents"
topics:
  - "ai-agents"
---

# What Could the Agent See at 19:05? Generating Temporal Enterprise Scenarios from Real Research and Replaying Them to Evaluate Agents

[원문 열기](https://arxiv.org/abs/2608.01042v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GNQ4DRSN`)
- 발행일: 2026-08-02T06:56:56Z
- 저자: Tezan Sahu, Himani Arora
- 식별자: `arxiv:2608.01042`

## 요약·초록

Enterprise AI agents act across many apps whose data changes continuously, so an answer is correct only relative to what data existed and who could see it at the moment it was asked. Offline evaluation today grades against a single static snapshot, effectively the end of the episode. So, it can only evaluate one situation, the final one, even though every earlier moment of the episode is a different situation that invites its own realistic questions with its own correct answers. Recreating each of those moments as a separate snapshot would mean re-provisioning a whole tenant per instant, which is prohibitively costly; and even a single snapshot leaks future state hidden inside records and cannot represent the multi-app, time-ordered way real work happens. Our system closes two gaps at once: it generates a realistic, persona-driven, temporally-evolving enterprise world from real research, and replays that world at any chosen moment to evaluate any pluggable agent. A schema-inferred temporal description drives a deterministic-plus-LLM rebuild of each record's past state; because the queryable moments are finite, all rebuilds are precomputed into a compact difference cache, making evaluation a fast, reproducible lookup with no model in the path. We describe the design, an architecture spanning both flows, and early experience evaluating enterprise agents.

## 내 메모



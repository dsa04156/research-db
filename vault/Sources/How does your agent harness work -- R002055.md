---
type: research-source
item_id: 2055
title: "How does your agent harness work"
source: "social:reddit"
published: "2026-08-16"
first_seen: "2026-08-18"
review_status: "pending"
canonical_key: "url:b17602b837a3a6edc918107b99da90314e645e94793ead120ce5e3c99b97f869"
url: "https://www.reddit.com/r/AI_Agents/comments/1vpna1c/how_does_your_agent_harness_work/"
generated_by: codex-research-db
aliases:
  - "How does your agent harness work"
topics:
  - "self-evolving-harness"
---

# How does your agent harness work

> [!warning] SNS 탐색 신호
> 원문이나 1차 자료를 확인하기 전에는 근거로 인용하지 않습니다.

[원문 열기](https://www.reddit.com/r/AI_Agents/comments/1vpna1c/how_does_your_agent_harness_work/)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-18|2026-08-18]]
- 수집 채널: `social:reddit`
- 검토 상태: `pending`
- 발행일: 2026-08-16
- 식별자: `url:b17602b837a3a6edc918107b99da90314e645e94793ead120ce5e3c99b97f869`

## 요약·초록

Sandboxed execution is the piece a lot of harness writeups skip over. We run agent-generated code in real Firecracker microVMs instead of shared-kernel containers -- proper kernel isolation, and boot is well under a second so it doesn't slow the loop down. Snapshot/resume lets you suspend idle sandboxes instead of paying for 24/7 uptime, which matters once you have more than a handful running. Dis I went with a completely custom setup: github.com/devoidfury/hotdog Only real dependency is bun, the rest is implemented in the codebase. One "nonstandard" thing I've found to be real useful is implementing "handoff" as a built-in tool. The thing that moved the needle most for us wasn't in the harness itself, it was making the repo...

## 내 메모



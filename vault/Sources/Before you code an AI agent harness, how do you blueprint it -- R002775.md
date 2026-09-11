---
type: research-source
item_id: 2775
title: "Before you code an AI agent harness, how do you blueprint it?"
source: "social:reddit"
published: "2026-09-09"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "url:dbfb4aedf3aa34654ab4497bb76b2149bc088c609fce5d56040ad52af54fe5a1"
url: "https://www.reddit.com/r/LLMDevs/comments/1wbuwz9/before_you_code_an_ai_agent_harness_how_do_you/"
generated_by: codex-research-db
aliases:
  - "Before you code an AI agent harness, how do you blueprint it?"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# Before you code an AI agent harness, how do you blueprint it?

> [!warning] SNS 탐색 신호
> 원문이나 1차 자료를 확인하기 전에는 근거로 인용하지 않습니다.

[원문 열기](https://www.reddit.com/r/LLMDevs/comments/1wbuwz9/before_you_code_an_ai_agent_harness_how_do_you/)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `social:reddit`
- 검토 상태: `pending`
- 발행일: 2026-09-09
- 식별자: `url:dbfb4aedf3aa34654ab4497bb76b2149bc088c609fce5d56040ad52af54fe5a1`

## 요약·초록

You are not importing too much, but I would reorder one thing. You have adversarial testing after the harness. Write those cases at blueprint time instead, before you know how it works. Once you have seen the implementation you unconsciously write tests it passes. Same reason acceptance criteria go in the ticket rather than after the diff. The other change is format, not amount. Failure conditio i’d skip the pretty charter until you’ve written the ugly one — what kills the run, what’s the hard $ ceiling, and which tools can mutate anything outside a sandbox. diagram agents/tools/data flows if you want, but the boxes that matter are trust boundaries (where a prompt can talk a tool into spend blueprint...

## 내 메모



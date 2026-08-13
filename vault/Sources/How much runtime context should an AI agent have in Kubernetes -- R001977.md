---
type: research-source
item_id: 1977
title: "How much runtime context should an AI agent have in Kubernetes?"
source: "social:reddit"
published: "2026-08-12"
first_seen: "2026-08-13"
review_status: "pending"
canonical_key: "url:1a7595499122f629a29a62079cd053ace58f833ec1eeb348088c968666914dae"
url: "https://www.reddit.com/r/kubernetes/comments/1vm9wuf/how_much_runtime_context_should_an_ai_agent_have/"
generated_by: codex-research-db
aliases:
  - "How much runtime context should an AI agent have in Kubernetes?"
topics:
  - "kubernetes"
  - "ai-agents"
---

# How much runtime context should an AI agent have in Kubernetes?

> [!warning] SNS 탐색 신호
> 원문이나 1차 자료를 확인하기 전에는 근거로 인용하지 않습니다.

[원문 열기](https://www.reddit.com/r/kubernetes/comments/1vm9wuf/how_much_runtime_context_should_an_ai_agent_have/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-13|2026-08-13]]
- 수집 채널: `social:reddit`
- 검토 상태: `pending`
- 발행일: 2026-08-12
- 식별자: `url:1a7595499122f629a29a62079cd053ace58f833ec1eeb348088c968666914dae`

## 요약·초록

No experience with Ai agents specifically in Kubernetes, but the default should always be 'as little as needed'. You should treat your AI agents as an overly enthusiastic intern. You wouldn't give those write permissions on Prod either. Every AI agent should be subjected to the same RBAC and permission scrutiny as human employees, and preferably enforced by mechanisms outside the AI context itself We've deployed a Hermes agent within our k8s cluster. Out devops guy has actually written some pretty solid plugins for handling EntraID scope first, using Slack as the chat interface. Inside the cluster everything is read only - the agent doesn't get to do any changes. It can open PRs and Jira tick Pods, logs, services,...

## 내 메모



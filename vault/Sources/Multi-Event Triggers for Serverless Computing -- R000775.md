---
type: research-source
item_id: 775
title: "Multi-Event Triggers for Serverless Computing"
source: "arxiv"
published: "2025-05-27T13:46:01Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.21199"
url: "https://arxiv.org/abs/2505.21199v3"
generated_by: codex-research-db
aliases:
  - "Multi-Event Triggers for Serverless Computing"
topics:
  - "cloud-infrastructure"
---

# Multi-Event Triggers for Serverless Computing

[원문 열기](https://arxiv.org/abs/2505.21199v3)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`33X58ZUH`)
- 발행일: 2025-05-27T13:46:01Z
- 저자: Natalie Carl, Trever Schirmer, Niklas Kowallik, Joshua Adamek, Tobias Pfandzelter, Sergio Lucia, David Bermbach
- 식별자: `arxiv:2505.21199`

## 요약·초록

Function-as-a-Service (FaaS) is an event-driven serverless cloud computing model in which small, stateless functions are invoked in response to events, such as HTTP requests, new database entries, or messages. Current FaaS platform assume that each function invocation corresponds to a single event. However, from an application perspective, it is desirable to invoke functions in response to a collection of events of different types or only with every n\textsuperscript{th} event. To implement this today, a function would need additional state management, e.g., in a database, and custom logic to determine whether its trigger condition is fulfilled and the actual application code should run. In such an implementation, most function invocations would be rendered essentially useless, leading to unnecessarily high resource usage, latency, and cost for applications. In this paper, we introduce multi-event triggers, through which complex conditions for function invocations can be specified. Specifically, we introduce abstractions for invoking functions based on a set of $n$ events and joins of multiple events of different types. This enables application developers to define intricate conditions for function invocations, workflow steps, and complex event processing. Our evaluation with a proof-of-concept prototype shows that this reduces event--invocation latency by 62.5\% in an incident detection use-case and that our system can handle more than 300,000 requests per second on limited hardware, which is sufficient load for implementation in large FaaS platforms.

## 내 메모



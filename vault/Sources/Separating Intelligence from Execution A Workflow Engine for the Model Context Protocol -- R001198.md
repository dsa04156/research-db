---
type: research-source
item_id: 1198
title: "Separating Intelligence from Execution: A Workflow Engine for the Model Context Protocol"
source: "arxiv"
published: "2026-03-13T05:12:14Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.00827"
url: "https://arxiv.org/abs/2605.00827v1"
generated_by: codex-research-db
aliases:
  - "Separating Intelligence from Execution: A Workflow Engine for the Model Context Protocol"
topics:
  - "kubernetes"
---

# Separating Intelligence from Execution: A Workflow Engine for the Model Context Protocol

[원문 열기](https://arxiv.org/abs/2605.00827v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6FZ4ZPB2`)
- 발행일: 2026-03-13T05:12:14Z
- 저자: Abhinav Singh Parmar
- 식별자: `arxiv:2605.00827`

## 요약·초록

Large Language Model (LLM) agents increasingly interact with external systems through tool-calling protocols such as the Model Context Protocol (MCP). In prevailing architectures, the agent must reason about every tool invocation in every session, consuming tokens proportional to the number of actions performed--even when the task has been solved before. We present the MCP Workflow Engine, a novel MCP-native orchestration layer that decouples intelligence (deciding what to do) from execution (carrying it out). An agent reasons once to produce a declarative workflow blueprint--a JSON document specifying a directed sequence of MCP tool calls with parameterized templates, loops, parallel branches, and data piping. Subsequent executions are triggered by a single run_workflow tool call, consuming one invocation's worth of tokens regardless of the blueprint's internal complexity. We formalize the MCP Mediator architectural pattern--an MCP server that simultaneously acts as a client to downstream MCP servers--and implement it in TypeScript against the MCP SDK. We evaluate the engine on a production-scale Kubernetes CMDB synchronization task spanning 67 orchestrated steps across 2 MCP servers, 38 namespaces, 13 worker nodes, and 22 distinct resource types. The engine reduces per-execution token cost by over 99%, completes the full cluster graph--comprising 1,200+ nodes and 2,800+ relationships across 20 relationship types--in under 45 seconds, and achieves deterministic, idempotent execution with zero agent involvement at run time.

## 내 메모



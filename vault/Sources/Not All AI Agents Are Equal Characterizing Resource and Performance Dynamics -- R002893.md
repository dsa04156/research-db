---
type: research-source
item_id: 2893
title: "Not All AI Agents Are Equal: Characterizing Resource and Performance Dynamics"
source: "arxiv"
published: "2026-09-17T09:20:53Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.19947"
url: "https://arxiv.org/abs/2609.19947v1"
generated_by: codex-research-db
aliases:
  - "Not All AI Agents Are Equal: Characterizing Resource and Performance Dynamics"
topics:
  - "ai-agents"
---

# Not All AI Agents Are Equal: Characterizing Resource and Performance Dynamics

[원문 열기](https://arxiv.org/abs/2609.19947v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`EG82XS9V`)
- 발행일: 2026-09-17T09:20:53Z
- 저자: Wonmi Choi, Minuk Park, Zhixiong Niu, Yongqiang Xiong, Chuck Yoo, Gyeongsik Yang
- 식별자: `arxiv:2609.19947`

## 요약·초록

LLM-based AI agents process user requests through iterative reasoning and tool execution, often involving the invocation of remote LLM APIs with local tool containers. This execution model can make the optimization of agent serving difficult because latency, local resource demand, and container bottlenecks inter-mix across requests. However, the current agent ecosystem runs without much consideration of resource dynamics, which results in significant waste of the precious resources. This paper analyzes the resource inter-mix of AI agents for three representative tasks: retrieval-augmented question answering, web search, and software coding. To this end, we characterize the latency with respect to the resource dynamics of processing multiple requests and tasks concurrently. Our measurements show that agents have a wide range of behaviors depending on tasks, so that even the same tool can differ substantially in resource dynamics. We also find that running multiple requests concurrently exposes task-dependent bottlenecks in resource dynamics such as CPU, disk I/O, and memory. Furthermore, we uncover that faster LLM responses or more CPU cores do not always accelerate agents. Based on these observations, we demonstrate new optimization opportunities that exploit the resource dynamics of tasks: CPU-aware tool admission and task-aware CPU allocation. Our results show that the latency of CPU-sensitive agent tasks improves $\sim$5.4$\times$, and the average latency across multiple tasks is reduced $\sim$32% compared to native agents.

## 내 메모



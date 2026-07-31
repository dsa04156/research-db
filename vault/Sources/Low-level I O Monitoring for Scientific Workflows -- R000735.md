---
type: research-source
item_id: 735
title: "Low-level I/O Monitoring for Scientific Workflows"
source: "arxiv"
published: "2024-08-01T09:29:24Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2408.00411"
url: "https://arxiv.org/abs/2408.00411v1"
generated_by: codex-research-db
aliases:
  - "Low-level I/O Monitoring for Scientific Workflows"
topics:
  - "kubernetes"
---

# Low-level I/O Monitoring for Scientific Workflows

[원문 열기](https://arxiv.org/abs/2408.00411v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GQMCP4VR`)
- 발행일: 2024-08-01T09:29:24Z
- 저자: Joel Witzke, Ansgar Lößer, Vasilis Bountris, Florian Schintke, Björn Scheuermann
- 식별자: `arxiv:2408.00411`

## 요약·초록

While detailed resource usage monitoring is possible on the low-level using proper tools, associating such usage with higher-level abstractions in the application layer that actually cause the resource usage in the first place presents a number of challenges. Suppose a large-scale scientific data analysis workflow is run using a distributed execution environment such as a compute cluster or cloud environment and we want to analyze the I/O behaviour of it to find and alleviate potential bottlenecks. Different tasks of the workflow can be assigned to arbitrary compute nodes and may even share the same compute nodes. Thus, locally observed resource usage is not directly associated with the individual workflow tasks. By acquiring resource usage profiles of the involved nodes, we seek to correlate the trace data to the workflow and its individual tasks. To accomplish that, we select the proper set of metadata associated with low-level traces that let us associate them with higher-level task information obtained from log files of the workflow execution as well as the job management using a task orchestrator such as Kubernetes with its container management. Ensuring a proper information chain allows the classification of observed I/O on a logical task level and may reveal the most costly or inefficient tasks of a scientific workflow that are most promising for optimization.

## 내 메모



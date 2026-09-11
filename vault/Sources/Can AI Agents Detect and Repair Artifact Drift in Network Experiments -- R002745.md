---
type: research-source
item_id: 2745
title: "Can AI Agents Detect and Repair Artifact Drift in Network Experiments?"
source: "arxiv"
published: "2026-09-09T07:58:24Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.09849"
url: "https://arxiv.org/abs/2609.09849v1"
generated_by: codex-research-db
aliases:
  - "Can AI Agents Detect and Repair Artifact Drift in Network Experiments?"
topics:
  - "ai-agents"
---

# Can AI Agents Detect and Repair Artifact Drift in Network Experiments?

[원문 열기](https://arxiv.org/abs/2609.09849v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`A6ESPHWK`)
- 발행일: 2026-09-09T07:58:24Z
- 저자: Tianzhu Zhang, Weichen Tao, Changgang Zheng, Yusheng Zheng, Long Chen, Xiaoyi Fan, Meikang Qiu
- 식별자: `arxiv:2609.09849`

## 요약·초록

In recent years, AI agents have evolved into capable assistants that carry out multi-step tasks in digital environments. The network systems community is beginning to explore these capabilities in operational and experimental settings. However, an agent operating in network systems should not be judged solely by whether it completes the immediate task. The experiment record it modifies must also remain trustworthy. We call this property artifact integrity: the record's claims must remain supported by the available evidence, confined to the scope established by that evidence, and traceable through the artifacts that encode their support. To make this property measurable, we introduce NetArtifactBench, which tests whether AI agents can repair inconsistent records derived from public network-system artifacts while preserving claims that remain supported. The benchmark contains 52 instances with injected inconsistencies ranging from direct contradictions to unstated relations spread across several artifacts. We evaluate 23 agent configurations across three general-purpose AI agent runtimes using deterministic scoring. The average contract pass rate is 65.3 % across 5,980 outputs, but no agent runtime exceeds 30 % when repair requires recovering implicit relations and propagating changes across artifacts. These results reveal a sharp boundary between local correction and complete record-level repair. Therefore, we argue that artifact integrity should become a first-class design and evaluation requirement for AI agents operating on network systems.

## 내 메모



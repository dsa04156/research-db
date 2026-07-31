---
type: research-source
item_id: 1029
title: "ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses"
source: "arxiv"
published: "2026-06-23T21:33:13Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.25189"
url: "https://arxiv.org/abs/2606.25189v2"
generated_by: codex-research-db
aliases:
  - "ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses"
topics:
  - "self-evolving-harness"
---

# ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses

[원문 열기](https://arxiv.org/abs/2606.25189v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZR252I5X`)
- 발행일: 2026-06-23T21:33:13Z
- 저자: Yusheng Zheng, Tianyuan Wu, Quanzhi Fu, Tong Yu, Wenan Mao, Tao Ma, Dan Williams, Wei Wang, Andi Quinn
- 식별자: `arxiv:2606.25189`

## 요약·초록

AI agents increasingly run in production through harnesses, the software around the LLM, including an engine that enforces safety and effectiveness policies, e.g., 'run tests before committing.' Enforcing these policies requires bridging a semantic gap: policy intent is expressed in underspecified natural language, while enforcement must act on concrete system actions, e.g., which test to run. Many policies also define event ordering or data flow actions. Yet existing approaches fall short. Tool-call guardrails miss system actions that bypass the tool layer, while OS sandboxes control resource access instead of actions, returning opaque errors that confuse the agent. Our key insight is that policy context lives within the agent closest to the task, while enforcement must happen at the OS to cover all execution paths. We introduce ActPlane, a policy engine that lets agents declare policies and enforces them in the OS kernel with semantic feedback and isolation. ActPlane uses a simple information-flow control (IFC) DSL to support cross-event policies. We implement ActPlane with eBPF and evaluate it on policies from the empirical study, coding-task benchmarks, and safety benchmarks. ActPlane improves policy compliance, including on indirect execution paths that tool-call interception cannot observe, with 1.9%-8.4% overhead. ActPlane is at https://github.com/eunomia-bpf/ActPlane

## 내 메모



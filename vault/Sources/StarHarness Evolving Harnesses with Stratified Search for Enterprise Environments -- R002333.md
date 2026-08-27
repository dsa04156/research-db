---
type: research-source
item_id: 2333
title: "StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments"
source: "arxiv"
published: "2026-08-25T16:48:05Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.24804"
url: "https://arxiv.org/abs/2608.24804v1"
generated_by: codex-research-db
aliases:
  - "StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments"
topics:
  - "self-evolving-harness"
---

# StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments

[원문 열기](https://arxiv.org/abs/2608.24804v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-25T16:48:05Z
- 저자: Esakkivel Esakkiraja, Denis Akhiyarov, Vikas Yadav, Sai Rajeswar, Patrice Bechard, Sridhar Nemala, Sagar Davasam
- 식별자: `arxiv:2608.24804`

## 요약·초록

We present StarHarness, a framework for evolving environment-specific agent harnesses while keeping model weights fixed. The evolved harness can include prompt and task framing, tool interfaces, skills, MCP-backed providers, subagent structure, and agent-loop configuration. StarHarness constructs a compact evolution pool by stratifying tasks according to baseline failure behavior, separates proposer-visible search tasks from proposer-hidden selection tasks, and reserves held-out tasks for evaluating generalization. Across ITBench SRE, EnterpriseOps-Gym ITSM, and AutomationBench Finance, harness evolution improves full-benchmark performance by 20-35 percentage points over the default harness after 4-12 accepted changes per environment. These gains persist on tasks excluded from evolution and transfer without re-evolution across GPT and Qwen model families. Trace analysis links the improvements to interface repairs, environment conventions, and operational knowledge that compresses search, with fewer false-positive diagnoses and shorter trajectories in several settings. StarHarness therefore offers a practical way to reduce persistent model-environment mismatch in tool-rich enterprise tasks.

## 내 메모

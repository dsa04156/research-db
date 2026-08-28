---
type: research-source
item_id: 2264
title: "ARGUS: MCP-Grounded Root Cause Analysis for Kubernetes Incidents"
source: "arxiv"
published: "2026-08-24T10:48:21Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.23084"
url: "https://arxiv.org/abs/2608.23084v1"
generated_by: codex-research-db
aliases:
  - "ARGUS: MCP-Grounded Root Cause Analysis for Kubernetes Incidents"
topics:
  - "kubernetes"
---

# ARGUS: MCP-Grounded Root Cause Analysis for Kubernetes Incidents

[원문 열기](https://arxiv.org/abs/2608.23084v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`AGTSU37P`)
- 발행일: 2026-08-24T10:48:21Z
- 저자: Ergi Senja, Seyed Mohammad Reza Razavi Zadegan, Philipp Leitner
- 식별자: `arxiv:2608.23084`

## 요약·초록

Kubernetes incident triage requires correlating signals from metrics, logs, container state, and messaging systems across multiple monitoring tools, a fragmented workflow that slows diagnosis and contributes to alert fatigue. Large language models (LLMs) have shown promise for automated root cause analysis (RCA), but existing systems rely on custom, system-specific data access layers that cannot be reused across organisations. We present ARGUS, an MCP-grounded RCA assistant that connects a commercial LLM to live Kubernetes observability data through standardised MCP servers covering Kubernetes state, Prometheus metrics, Loki logs, and NATS messaging, and delivers structured diagnostic summaries inside the Slack incident channel where on-call engineers already work. We conduct a preliminary evaluation of ARGUS using three complementary methods: controlled fault injection across ten Kubernetes incident scenarios, rubric-based scoring of the resulting RCA summaries on three dimensions, and semi-structured interviews with six on-call engineers at an industrial partner. ARGUS named the correct root cause in all ten scenarios with an aggregate MCP success ratio of 0.91. Practitioners trusted the diagnostic output but consistently expressed scepticism toward the recommended fixes. Our central finding is a diagnostic/prescriptive asymmetry: ARGUS reliably identifies what went wrong, but is perceived as less reliable or trustworthy at specifying what to do next. This pattern can be observed across all three evaluation methods, and has important implications for future autonomous agentic incident handling systems.

## 내 메모



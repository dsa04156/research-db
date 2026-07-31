---
type: research-source
item_id: 5
title: "SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response"
source: "arxiv"
published: "2026-07-29T11:32:23Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26791"
url: "https://arxiv.org/abs/2607.26791v1"
generated_by: codex-research-db
aliases:
  - "SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response

[원문 열기](https://arxiv.org/abs/2607.26791v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UDTJEQJZ`)
- 발행일: 2026-07-29T11:32:23Z
- 저자: Lehan Wang, Boli Chen, Ruixue Ding, Pengjun Xie, Jinwei Huang, Zhendong Liu, Shuo Wang, Tao Lei, Xin Ouyang, Xiaomeng Li
- 식별자: `arxiv:2607.26791`

## 요약·초록

Large Language Model (LLM) agents are increasingly adopted in real-world security operations with access to host artifacts and command-line interfaces (CLIs), making it critical to thoroughly assess their security capabilities. However, existing cybersecurity benchmarks focus on pre-compromise settings where agents are placed in a clean and idealized environment before an attack occurs. This leaves the post-compromise setting underexplored. To address this gap, we introduce SecRespond, the first benchmark for evaluating LLM agents on the post-compromise incident-response workflow. Given a forensic disk snapshot of a compromised host together with the alerts, vulnerability scans, and baseline checks reported by a host security product, agents are required to produce forensic reports on intrusions, baseline risks, and vulnerability risks, together with a remediation plan. We instantiate this task across 10 cyber ranges, each constructed from a distinct compromised cloud host, spanning 4 entry-point types, 21 ATT&CK techniques, and 5 operating systems. We evaluate 23 frontier LLMs on the OpenCode agent harness. Experimental results show that although current agents can reliably uncover the problems exposed by alerts, they struggle to proactively investigate the disk for silent intrusions and to produce comprehensive, verified remediation plans, with no model achieving complete detection and remediation on any single range. This reveals a fundamental bottleneck in building agents for real-world incident response. The benchmark is publicly available at https://github.com/Alibaba-NLP/qqr/tree/main/data/secrespond.

## 내 메모



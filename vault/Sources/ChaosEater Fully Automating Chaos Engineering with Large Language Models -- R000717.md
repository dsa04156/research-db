---
type: research-source
item_id: 717
title: "ChaosEater: Fully Automating Chaos Engineering with Large Language Models"
source: "arxiv"
published: "2025-01-19T16:35:09Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2501.11107"
url: "https://arxiv.org/abs/2501.11107v2"
generated_by: codex-research-db
aliases:
  - "ChaosEater: Fully Automating Chaos Engineering with Large Language Models"
topics:
  - "kubernetes"
---

# ChaosEater: Fully Automating Chaos Engineering with Large Language Models

[원문 열기](https://arxiv.org/abs/2501.11107v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MH2KGSCK`)
- 발행일: 2025-01-19T16:35:09Z
- 저자: Daisuke Kikuta, Hiroki Ikeuchi, Kengo Tajiri
- 식별자: `arxiv:2501.11107`

## 요약·초록

Chaos Engineering (CE) is an engineering technique aimed at improving the resiliency of distributed systems. It involves artificially injecting specific failures into a distributed system and observing its behavior in response. Based on the observation, the system can be proactively improved to handle those failures. Recent CE tools implement the automated execution of predefined CE experiments. However, defining these experiments and improving the system based on the experimental results still remain manual. To reduce the costs of the manual operations, we propose ChaosEater, a system for automating the entire CE operations with Large Language Models (LLMs). It predefines the agentic workflow according to a systematic CE cycle and assigns subdivided operations within the workflow to LLMs. ChaosEater targets CE for Kubernetes systems, which are managed through code (i.e., Infrastructure as Code). Therefore, the LLMs in ChaosEater perform software engineering tasks to complete CE cycles, including requirement definition, code generation, debugging, and testing. We evaluate ChaosEater through case studies on both small and large Kubernetes systems. The results demonstrate that it stably completes reasonable single CE cycles with significantly low time and monetary costs. The CE cycles are also qualitatively validated by human engineers and LLMs.

## 내 메모



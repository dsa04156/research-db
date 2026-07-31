---
type: research-source
item_id: 721
title: "Dual-Use Commercial and Military Communications on a Single Platform using RAN Domain Specific Language"
source: "arxiv"
published: "2024-12-01T22:16:24Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2412.00983"
url: "https://arxiv.org/abs/2412.00983v1"
generated_by: codex-research-db
aliases:
  - "Dual-Use Commercial and Military Communications on a Single Platform using RAN Domain Specific Language"
topics:
  - "kubernetes"
---

# Dual-Use Commercial and Military Communications on a Single Platform using RAN Domain Specific Language

[원문 열기](https://arxiv.org/abs/2412.00983v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HKC98Z4F`)
- 발행일: 2024-12-01T22:16:24Z
- 저자: Alan Gatherer, Chaitali Sengupta, Sudipta Sen, Jeffery H. Reed
- 식별자: `arxiv:2412.00983`

## 요약·초록

Despite the success of the O-RAN Alliance in developing a set of interoperable interfaces, development of unique Radio Access Network (RAN) deployments remains challenging. This is especially true for military communications, where deployments are highly specialized with limited volume. The construction and maintenance of the RAN, which is a real time embedded system, is an ill-defined NP problem requiring teams of specialized system engineers, with specialized knowledge of the hardware platform. In this paper, we introduce a RAN Domain Specific Language (RDSL(TM)) to formally describe use cases, constraints, and multi-vendor hardware/software abstraction to allow automation of RAN construction. In this DSL, system requirements are declarative, and performance constraints are guaranteed by construction using an automated system solver. Using our RAN system solver platform, Gabriel(TM) we show how a system engineer can confidently modify RAN functionality without knowledge of the underlying hardware. We show benefits for specific system requirements when compared to the manually optimized, default configuration of the Intel FlexRAN(TM), and conclude that DSL/automation driven construction of the RAN can lead to significant power and latency benefits when the deployment constraints are tuned for a specific case. We give examples of how constraints and requirements can be formatted in a "Kubernetes style" YAML format which allows the use of other tools, such as Ansible, to integrate the generation of these requirements into higher level automation flows such as Service Management and Orchestration (SMO).

## 내 메모



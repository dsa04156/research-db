---
type: research-source
item_id: 377
title: "TME-Box: Scalable In-Process Isolation through Intel TME-MK Memory Encryption"
source: "arxiv"
published: "2024-07-15T14:09:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.14722/ndss.2025.240277"
url: "https://arxiv.org/abs/2407.10740v2"
generated_by: codex-research-db
aliases:
  - "TME-Box: Scalable In-Process Isolation through Intel TME-MK Memory Encryption"
topics:
  - "cloud-infrastructure"
---

# TME-Box: Scalable In-Process Isolation through Intel TME-MK Memory Encryption

[원문 열기](https://arxiv.org/abs/2407.10740v2)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`BWCFAN83`)
- 발행일: 2024-07-15T14:09:00Z
- 저자: Martin Unterguggenberger, Lukas Lamster, David Schrammel, Martin Schwarzl, Stefan Mangard
- 식별자: `doi:10.14722/ndss.2025.240277`

## 요약·초록

Efficient cloud computing relies on in-process isolation to optimize performance by running workloads within a single process. Without heavy-weight process isolation, memory safety errors pose a significant security threat by allowing an adversary to extract or corrupt the private data of other co-located tenants. Existing in-process isolation mechanisms are not suitable for modern cloud requirements, e.g., MPK's 16 protection domains are insufficient to isolate thousands of cloud workers per process. Consequently, cloud service providers have a strong need for lightweight in-process isolation on commodity x86 machines. This paper presents TME-Box, a novel isolation technique that enables fine-grained and scalable sandboxing on commodity x86 CPUs. By repurposing Intel TME-MK, which is intended for the encryption of virtual machines, TME-Box offers lightweight and efficient in-process isolation. TME-Box enforces that sandboxes use their designated encryption keys for memory interactions through compiler instrumentation. This cryptographic isolation enables fine-grained access control, from single cache lines to full pages, and supports flexible data relocation. In addition, the design of TME-Box allows the efficient isolation of up to 32K concurrent sandboxes. We present a performance-optimized TME-Box prototype, utilizing x86 segment-based addressing, that showcases geomean performance overheads of 5.2 % for data isolation and 9.7 % for code and data isolation, evaluated with the SPEC CPU2017 benchmark suite.

## 내 메모



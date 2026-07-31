---
type: research-source
item_id: 82
title: "Valinor: Architectural Support for Fast, Energy-Efficient and Programmable Physical Memory Allocation"
source: "openalex"
published: "2026-07-16"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.14789"
url: "https://arxiv.org/abs/2607.14789"
generated_by: codex-research-db
aliases:
  - "Valinor: Architectural Support for Fast, Energy-Efficient and Programmable Physical Memory Allocation"
topics:
  - "cloud-infrastructure"
---

# Valinor: Architectural Support for Fast, Energy-Efficient and Programmable Physical Memory Allocation

[원문 열기](https://arxiv.org/abs/2607.14789)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`F6DQ76G5`)
- 발행일: 2026-07-16
- 저자: Konstantinos Kanellopoulos, Spiros Galanopoulos, Konstantinos Sgouras, Vlad-Petru Nitu, Ilias Papalamprou, Andreas Kosmas Kakolyris, Rahul Bera, Dimosthenis Masouros, Dimitrios Soudris, Onur Mutlu
- 식별자: `arxiv:2607.14789`

## 요약·초록

Physical memory allocation establishes virtual-to-physical mappings on demand. In current systems, each minor page fault traps into the kernel and triggers pipeline flushes, stalls, and a long sequence of allocation steps that can cost tens of thousands of cycles. These overheads are increasingly significant for short-lived workloads such as serverless functions and microservices, where minor faults can account for up to 54% of runtime and up to 40% of system energy. Prior hardware allocation proposals avoid traps and context switches, but either sacrifice useful placement optimizations or rely on fixed-function logic that cannot adapt to new policies or changing hardware conditions. We present Valinor, a hardware-OS cooperative memory allocation substrate that combines software flexibility with hardware-class performance. Valinor introduces a programmable hardware allocation engine that executes compact OS-supplied allocation libraries at close to fixed-hardware speed. It supports diverse policies, including short-lived object allocators, integrity mechanisms, and hardware-telemetry-guided placement. We implement Valinor on a BOOM RISC-V soft core running Linux and in a full-system simulator. On real hardware, Valinor accelerates allocation by 17x, improves end-to-end performance by 16%, and reduces energy consumption by up to 8%. Full-system simulation further evaluates the programmable allocation engine and six allocation libraries, showing that Valinor provides hardware-class performance without sacrificing programmability.

## 내 메모



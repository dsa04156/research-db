---
type: research-source
item_id: 2621
title: "Extending concurrent separation logic to the hardware level to verify the xv6 OS kernel on RISC-V with AI agents"
source: "arxiv"
published: "2026-09-03T16:17:47Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.04043"
url: "https://arxiv.org/abs/2609.04043v1"
generated_by: codex-research-db
aliases:
  - "Extending concurrent separation logic to the hardware level to verify the xv6 OS kernel on RISC-V with AI agents"
topics:
  - "ai-agents"
---

# Extending concurrent separation logic to the hardware level to verify the xv6 OS kernel on RISC-V with AI agents

[원문 열기](https://arxiv.org/abs/2609.04043v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`F8RGIZVV`)
- 발행일: 2026-09-03T16:17:47Z
- 저자: M. Frans Kaashoek, Nickolai Zeldovich
- 식별자: `arxiv:2609.04043`

## 요약·초록

MachCSL is a framework for verifying systems software, such as an OS kernel, on top of low-level semantics of a RISC-V computer, based on the Sail RISC-V semantics. The key idea behind MachCSL is to adapt concurrent separation logic, based on Iris, to reasoning about low-level hardware execution at the sub-instruction level: page-table translation, TLB, privilege levels, configuration registers, instruction fetch/decode/execute, traps and interrupts, DMA, shared memory, power failures, etc. Reasoning at this level of detail ensures that the system software correctly manages all of the hardware details. Verifying software at this low level of abstraction is tedious, but LLM-based agents are capable of reasoning about such low-level details. As a case study, we verify the xv6 OS kernel (6,593 lines of C and assembly code), which provides a traditional Unix system call interface (processes, file system, file descriptors, and preemptive scheduling) and has substantial internal concurrency (multi-core support with fine-grained locking, shared memory, interrupts, DMA, etc.). In the verification process, we uncovered nine bugs in the xv6 implementation, as well as one bug in the Sail RISC-V semantics. The verification effort took us 77 days, including the time to develop the MachCSL framework.

## 내 메모



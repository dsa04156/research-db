---
type: research-source
item_id: 1046
title: "EvoDRC: A Self-Evolving Agentic Framework for Automated DRC Violation Repair"
source: "openalex"
published: "2026-07-22"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.20019"
url: "https://arxiv.org/abs/2607.20019"
generated_by: codex-research-db
aliases:
  - "EvoDRC: A Self-Evolving Agentic Framework for Automated DRC Violation Repair"
topics:
  - "self-evolving-harness"
---

# EvoDRC: A Self-Evolving Agentic Framework for Automated DRC Violation Repair

[원문 열기](https://arxiv.org/abs/2607.20019)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`IAE75BGR`)
- 발행일: 2026-07-22
- 저자: Bing-Yue Wu, Chia-Tung Ho, Haoyu Yang, Brucek Khailany, Vidya A. Chhabria
- 식별자: `arxiv:2607.20019`

## 요약·초록

Design rule check (DRC) closure remains a major bottleneck in advanced-node physical design. Although detailed routers are rule-aware, residual design rule violations (DRVs) often require manual engineering change order iterations. Automating this process is challenging because repairs must account for complex geometric interactions, preserve circuit connectivity, and avoid introducing new violations. We present EvoDRC, a skill-evolution framework for agentic block-level DRC repair. EvoDRC initializes layer-specific repair skills using knowledge distilled from an unrelated reference design and continuously evolves these skills using traceable repair experience collected from the target design. EvoDRC decomposes the layout into bounded repair regions and assigns an LLM repair agent to each region. Local DRC analysis, connectivity-checking, and impact-preview tools provide feedback on proposed modifications. Repair operations and their resulting DRV changes are stored in a knowledge database and used to evolve the repair skills. Experiments on seven block-level designs from the DAC26 DRC Benchmark show that EvoDRC achieves a 73.5\% overall reduction compared to the reported baseline.

## 내 메모



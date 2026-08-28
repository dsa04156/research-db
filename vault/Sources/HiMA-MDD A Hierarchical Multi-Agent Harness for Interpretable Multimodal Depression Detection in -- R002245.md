---
type: research-source
item_id: 2245
title: "HiMA-MDD: A Hierarchical Multi-Agent Harness for Interpretable Multimodal Depression Detection in Clinical Interviews"
source: "arxiv"
published: "2026-08-22T09:26:42Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.21868"
url: "https://arxiv.org/abs/2608.21868v1"
generated_by: codex-research-db
aliases:
  - "HiMA-MDD: A Hierarchical Multi-Agent Harness for Interpretable Multimodal Depression Detection in Clinical Interviews"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# HiMA-MDD: A Hierarchical Multi-Agent Harness for Interpretable Multimodal Depression Detection in Clinical Interviews

[원문 열기](https://arxiv.org/abs/2608.21868v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DAFCFVV7`)
- 발행일: 2026-08-22T09:26:42Z
- 저자: Ao Chen, Xiaojiang Peng
- 식별자: `arxiv:2608.21868`

## 요약·초록

Depression assessment from multimodal clinical interviews requires integrating dispersed evidence from multiple symptoms into a coherent PHQ-8 profile. This process is hierarchical: relevant evidence is often sparse and context-dependent within local question-answer exchanges, multiple exchanges jointly support symptom-level judgments, and the final assessment depends on the coherence of the complete symptom profile. Existing LLM systems either process interviews holistically or distribute work across generic agent roles; neither design necessarily provides an explicit orchestration mechanism that coordinates evidence access, item-score authority, bounded feedback, and state recording across these levels. To address this gap, we introduce HiMA-MDD, a hierarchical multi-agent harness that aligns this assessment hierarchy with three agent layers. After non-agentic preprocessing constructs context-preserving multimodal QA units, Layer 1 identifies candidate QA-to-item relations and supports bounded item-grounded evidence routing. Layer 2 assigns symptom groups to operational factor specialists, with one specialist responsible for each provisional item score. Layer 3 audits the complete provisional profile, requests at most one round of targeted revision, and reconstructs the verified PHQ-8 profile. This layered design naturally yields a Hierarchical Evidence Trace, preserves all intermediate evidence, judgments, and revisions for auditability. The final item scores then deterministically produce the total score and screening decision. Using Qwen2.5-72B-Instruct as the harness backbone, our experiments on E-DAIC demonstrate that HiMA-MDD outperforms the compared state-of-the-art methods.

## 내 메모



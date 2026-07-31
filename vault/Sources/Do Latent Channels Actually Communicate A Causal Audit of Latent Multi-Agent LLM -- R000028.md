---
type: research-source
item_id: 28
title: "Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM"
source: "arxiv"
published: "2026-07-29T11:14:27Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26773"
url: "https://arxiv.org/abs/2607.26773v1"
generated_by: codex-research-db
aliases:
  - "Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM"
topics:
  - "ai-agents"
---

# Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM

[원문 열기](https://arxiv.org/abs/2607.26773v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GFZTFNR6`)
- 발행일: 2026-07-29T11:14:27Z
- 저자: Huixiang Zhang, Mahzabeen Emu
- 식별자: `arxiv:2607.26773`

## 요약·초록

Latent communication in large language model (LLM)-based multi-agent systems (MAS) transmits continuous internal representations instead of text, but greater representational capacity does not establish that the receiver uses task-relevant information. End-task performance alone also cannot reveal whether an observed effect depends on message presence, content generated for the evaluated example, or information supplied by a separate agent. We introduce a causal audit that applies controlled message replacements at the boundary where the sender-produced representation enters the receiver. Four message settings support five measurements of encoded sender information, receiver sensitivity to message presence and identity, the task value of example-specific content, and the additional value supplied by a separate agent. We apply the audit to latent relay with Qwen3-4B and Qwen3-8B on GSM8K, ARC-C, and MATH-500. On GSM8K, the Qwen3-4B overall performance effect of -1.00 percentage point decomposes into a -6.17-point effect retained by an other-example message and a +5.17-point effect attributable to example-specific content; both component directions reverse at 8B. On MATH-500, the Qwen3-4B gain of 15.00 points comprises 8.33 points retained by an other-example message and 6.67 points attributable to example-specific content, while the 8B gain is dominated by the former component. Self-substitution comparisons further show that example-specific content and other-agent value are distinct. These results show that aggregate accuracy does not identify how a latent message affects the receiver and motivate controlled message comparisons as a standard evaluation for latent communication.

## 내 메모



---
type: research-source
item_id: 2614
title: "Repeat-After-Me: Black-Box Adaptive Visual Prompt Injection"
source: "arxiv"
published: "2026-09-03T22:44:45Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.04533"
url: "https://arxiv.org/abs/2609.04533v1"
generated_by: codex-research-db
aliases:
  - "Repeat-After-Me: Black-Box Adaptive Visual Prompt Injection"
topics:
  - "ai-agents"
---

# Repeat-After-Me: Black-Box Adaptive Visual Prompt Injection

[원문 열기](https://arxiv.org/abs/2609.04533v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-03T22:44:45Z
- 저자: Sizhe Chen, Yu-Lin Tsai, Ivan Evtimov, Kamalika Chaudhuri, Raluca Ada Popa, David Wagner, Arman Zharmagambetov
- 식별자: `arxiv:2609.04533`

## 요약·초록

Prompt injection is widely recognized as a major security threat to AI agents that interact with untrusted external data, such as websites, documents, and emails. Prior work has shown that, in the text domain, black-box prompt injection can achieve near-perfect attack success rates (ASRs). In the image domain, however, existing visual prompt injection methods are substantially less effective in attacking frontier commercial VLMs for materially harmful behavior. Achieving such outputs is hard because it requires a long and/or format-compliant target string, such as a precise, parseable native tool call with exact function names and arguments. We present Repeat-After-Me, a black-box adaptive visual prompt injection attack that can reveal personally identifiable information or make malicious tool calls. Across both open-weight and commercial frontier VLMs, including Qwen3.6-27B and GPT-5.5, our method achieves ASRs exceeding 80% and 47%, respectively, under a realistic setting in which the benign user prompt is semantically unrelated to the injected task and does not verbally authorize it. In our evaluation, injections optimized on one surrogate retain 43-46% of the original ASR on two commercial victims, and cross-sample transferability retains 64-66% of the original ASR on those two models. We test our attack in a real-world OpenClaw agent: in a default OpenClaw Discord deployment, an untrusted user can use a minimally injected image to overwrite TOOLS.md, enabling future sensitive behaviors like remote code execution and secret exfiltration. We show our new attack vector works in cases where adaptive textual prompt injection fails. We discuss potential defenses.

## 내 메모



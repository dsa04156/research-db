---
type: research-source
item_id: 993
title: "Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened"
source: "arxiv"
published: "2026-07-13T10:14:15Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.13083"
url: "https://arxiv.org/abs/2607.13083v1"
generated_by: codex-research-db
aliases:
  - "Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened"
topics:
  - "self-evolving-harness"
---

# Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened

[원문 열기](https://arxiv.org/abs/2607.13083v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ESTQECMX`)
- 발행일: 2026-07-13T10:14:15Z
- 저자: Su Wang, Pin Qian, Yifan Lin, Jingzhou Xu, Yihang Chen, Xiaochong Jiang, Lifei Liu, Haoran Yu
- 식별자: `arxiv:2607.13083`

## 요약·초록

Self-improving AI agents are designed to learn from their mistakes. We show they can also hallucinate mistakes that never happened. We study this failure mode in automated harness optimization, where an LLM-based proposer edits an agent's scaffold, including prompts, parsers, filters, validators and guardrails, to eliminate observed failures. But this process rarely asks first: was there a real failure to fix? We introduce the Counterfactual Fabrication Lab, a deterministic micro-lab where the correct action is known: do nothing. The lab plants a candidate guardrail for a failure class that provably never occurs, presents only legal episodes, and uses a byte-exact oracle to check every cited violation. The proposer behaves as expected on real violations and abstains on featureless legal input. Yet when the legal input contains a harmless pattern resembling a familiar game rule, it invents a failure: in 15/60 runs, versus 0/60 on featureless input, it enables the nonexistent-rule guardrail and cites a violation the oracle refutes. The effect is structured, not indiscriminate. In single-shot proposals it appears only when three conditions coincide: a rule-shaped pattern, an open-ended rule set and an instruction that presupposes failures. Removing any of these conditions eliminates the fabrication. Because the invented guardrail changes no true outcome and cannot improve an already-perfect suppression score, the phenomenon is neither reward hacking nor over-refusal. It is a phantom guardrail: a fix for a failure that never happened, invisible to suppression-only acceptance. Inside an add-only accept loop it re-enters even without the failure-presupposing instruction, the loop's keep-adding role supplying the demand the instruction supplied in single shot, and once in it stays. We present the Counterfactual Fabrication Lab for measuring fabricated failures in self-improving agent harnesses.

## 내 메모



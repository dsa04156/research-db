---
type: research-source
item_id: 2558
title: "Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds"
source: "arxiv"
published: "2026-09-02T08:47:34Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.02302"
url: "https://arxiv.org/abs/2609.02302v1"
generated_by: codex-research-db
aliases:
  - "Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds"
topics:
  - "self-evolving-harness"
---

# Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds

[원문 열기](https://arxiv.org/abs/2609.02302v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-02T08:47:34Z
- 저자: Axel Ahlqvist, Richard Guan, Juan-Pablo Rivera, Adeline Kassler, Dmitrii Troitskii, Alexandra Souly, Kai Fronsdal, Robert Kirk, John Hughes
- 식별자: `arxiv:2609.02302`

## 요약·초록

A core obstacle to alignment evaluation is evaluation awareness: capable models can tell when they are being tested rather than deployed, weakening the conclusions a safety evaluation can support. We present two techniques that make simulated alignment evaluations harder to distinguish from real deployments. Our first technique, critique refinement, spends additional inference-time compute on each simulator action: the simulator generates multiple candidate actions, refines them using feedback from an instance of the target model on how to make them more realistic, and continues the evaluation with the most deployment-like candidate. Our second technique, DISH (Deployment-Imitating SWE-Agent Harness), wraps the target in an agent harness, reducing the gap between simulated and real deployment environments in coding settings. We test the techniques on multiple target models and find that they compose: applying both yields larger realism gains than either alone. Our results show that automated approaches can improve the realism of alignment evaluations, and that these improvements use additional compute more effectively than making the audits longer.

## 내 메모



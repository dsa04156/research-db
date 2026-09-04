---
type: research-source
item_id: 2574
title: "You Can't Escape Your Own Activations : Evaluation Awareness and Multi-Agent Monitoring"
source: "arxiv"
published: "2026-09-02T18:07:14Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.03035"
url: "https://arxiv.org/abs/2609.03035v1"
generated_by: codex-research-db
aliases:
  - "You Can't Escape Your Own Activations : Evaluation Awareness and Multi-Agent Monitoring"
topics:
  - "ai-agents"
---

# You Can't Escape Your Own Activations : Evaluation Awareness and Multi-Agent Monitoring

[원문 열기](https://arxiv.org/abs/2609.03035v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-02T18:07:14Z
- 저자: Aritra Das, Jaee Ponde, Mihir More, Debayan Gupta
- 식별자: `arxiv:2609.03035`

## 요약·초록

LLM agents are increasingly deployed in multi-agent systems, where they can collude while keeping their actions benign. Output monitors designed to detect such collusions can be fooled by obfuscation and steganography, motivating the use of probes trained on internal activations. However, these probes are usually evaluated on agents that do not know they are being watched. We study how activation-based detection changes when agents are explicitly informed that their internal activations are being monitored, and when they additionally receive feedback from the monitor. We keep the models, probes, and thresholds fixed and change only what the agents are told: nothing (baseline), that an activation monitor is present (aware), or that a monitor is present together with the previous round's score (feedback). We test two games, a four-agent blackjack game and a two-agent Simmons prisoners game, using Qwen3-32B-AWQ and GPT-OSS-20B in homogeneous and mixed pairings. Telling agents about the monitor does not hide them. The best probes stay accurate in all three conditions, and the agents keep colluding.

## 내 메모



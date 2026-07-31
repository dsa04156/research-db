---
type: research-source
item_id: 1043
title: "Open-SWE-Traces: Advancing Dual-Mode Multilingual Distillation for Software Engineering Agents"
source: "arxiv"
published: "2026-06-14T22:10:06Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.16038"
url: "https://arxiv.org/abs/2606.16038v1"
generated_by: codex-research-db
aliases:
  - "Open-SWE-Traces: Advancing Dual-Mode Multilingual Distillation for Software Engineering Agents"
topics:
  - "self-evolving-harness"
---

# Open-SWE-Traces: Advancing Dual-Mode Multilingual Distillation for Software Engineering Agents

[원문 열기](https://arxiv.org/abs/2606.16038v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`BP3GJVKE`)
- 발행일: 2026-06-14T22:10:06Z
- 저자: Wasi Uddin Ahmad, Nikolai Ludwig, Somshubra Majumdar, Boris Ginsburg
- 식별자: `arxiv:2606.16038`

## 요약·초록

The path toward autonomous software engineering is currently bottlenecked by a severe deficit of diverse, large-scale trajectory data. We address this by introducing \ourdataset, an expansive dataset of 207,489 agentic trajectories spanning nine programming languages (Python, Go, TS, JS, Rust, Java, PHP, C, C++). Sourced from 20,000 real-world PRs via OpenHands and SWE-agent harnesses, the dataset utilizes a hybrid-reasoning synthesis: Minimax-M2.5 generates trajectories with explicit "thinking" processes, while Qwen3.5-122B provides high-quality "non-thinking" traces. Filtered for permissive licenses (MIT, Apache, BSD) from SWE-rebench-V2, this data facilitates the training of models capable of long-horizon reasoning. We validate the dataset by fine-tuning the Qwen3-30B-A3B series (Thinking, Instruct, and Coder). The best performing model achieves resolve rates of 61.7% on SWE-bench Verified, 57.1% on SWE-bench Multilingual, and 36.8% on SWE-bench Pro. These results establish Open-SWE-Traces as a premier resource for distilling human-level software engineering capabilities into efficient, open-source agentic LLMs.

## 내 메모



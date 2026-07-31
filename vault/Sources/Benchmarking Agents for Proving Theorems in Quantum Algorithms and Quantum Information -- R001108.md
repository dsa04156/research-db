---
type: research-source
item_id: 1108
title: "Benchmarking Agents for Proving Theorems in Quantum Algorithms and Quantum Information"
source: "arxiv"
published: "2026-07-23T17:19:21Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.21533"
url: "https://arxiv.org/abs/2607.21533v1"
generated_by: codex-research-db
aliases:
  - "Benchmarking Agents for Proving Theorems in Quantum Algorithms and Quantum Information"
topics:
  - "ai-agents"
---

# Benchmarking Agents for Proving Theorems in Quantum Algorithms and Quantum Information

[원문 열기](https://arxiv.org/abs/2607.21533v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KC695TFF`)
- 발행일: 2026-07-23T17:19:21Z
- 저자: Lei Zhang, Yusheng Zhao, Yimeng Cao, Ranyiliu Chen, Mingrui Jing, Jizhe Lai, Ziao Tang, Jingu Xie, Hongshun Yao, Xuanqiang Zhao, Guocheng Zhen, Chengkai Zhu, Xin Wang
- 식별자: `arxiv:2607.21533`

## 요약·초록

Formal verification is becoming increasingly practical for quantum computing, yet the ability of AI agents to construct machine-checkable proofs in this domain remains unmeasured. We introduce Lean-QuantumAlg-Bench and Lean-QIT-Bench, two Lean 4 benchmarks containing 36 and 40 theorem-completion tasks for quantum algorithms and quantum information theory, respectively. Every task compiles in a fixed environment and is evaluated by deterministic proof checking and targeted semantic review, with difficulty weights assigned before model execution. We evaluate four models-GPT-5.5, Kimi K3, DeepSeek V4-Pro, and MiniMax M3-within a common theorem-proving framework under two settings: a task-only baseline and library-augmented deduction (LAD), which additionally provides access to a verified domain library. The highest difficulty-weighted scores are 60.4 out of 100 on the quantum-algorithm benchmark and 59.6 out of 100 on the quantum-information benchmark. LAD improves both score and completion rate in all eight model-benchmark comparisons, with gains of up to 15.9 points, providing evidence that verified libraries can strengthen domain-specific proof agents. The results reveal recurring weaknesses of agentic proving in areas such as quantum simulation, quantum learning, quantum information measures, and entanglement theory. Monetary and wall-clock costs per score point also vary substantially across models, highlighting important capability-efficiency trade-offs. We expect these benchmarks to establish a reproducible baseline for developing more capable and reliable proof agents, and to pave the way toward self-evolving AI scientists for advancing quantum information science.

## 내 메모



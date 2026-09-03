---
type: research-source
item_id: 2530
title: "Cooperative control of multi-microgrids under uncertainty: a multi-agent actor-critic approach with LSTM and deep dense architecture"
source: "openalex"
published: "2026-09-02"
first_seen: "2026-09-03"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-65292-z"
url: "https://doi.org/10.1038/s41598-026-65292-z"
generated_by: codex-research-db
aliases:
  - "Cooperative control of multi-microgrids under uncertainty: a multi-agent actor-critic approach with LSTM and deep dense architecture"
topics:
  - "ai-agents"
---

# Cooperative control of multi-microgrids under uncertainty: a multi-agent actor-critic approach with LSTM and deep dense architecture

[원문 열기](https://doi.org/10.1038/s41598-026-65292-z)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-03|2026-09-03]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`SR4UH7FP`)
- 발행일: 2026-09-02
- 저자: Zhengdong Wan, Jinsong Zhang, Taofei Ku
- 식별자: `doi:10.1038/s41598-026-65292-z`

## 요약·초록

The high penetration of renewable energy poses significant source-load uncertainty challenges to the economic and stable operation of microgrids. To address the key challenges of multi-microgrid cooperative optimization, including temporal source-load uncertainty, heterogeneous inter-microgrid coordination, and real-time decentralized decision-making, this paper proposes a cooperative control strategy named Long Short-Term Memory-based Multi-Agent Actor-Critic (L-MAAC). Under the Centralized Training with Decentralized Execution (CTDE) framework, the proposed method learns cooperative policies using global system information during training, while enabling each microgrid to make decisions based only on local observations during execution. Specifically, the Actor network incorporates an LSTM module to extract temporal features from historical source-load data, thereby improving the ability to proactively respond to renewable generation and load fluctuations, while the Critic network integrates an individual attention mechanism with a Deep Dense architecture in Reinforcement Learning (D2RL), which enhances the representation of heterogeneous interactions among microgrids and alleviates information loss in deep value-function approximation. Ablation studies, reward sensitivity, and hyperparameter sensitivity analyses confirm the synergistic contributions of these components. Simulation results based on a modified IEEE 13-bus multi-microgrid system show that, compared with advanced algorithms such as MAAC, L-MAAC reduces the total system operating cost by 4.81% on the test set. Furthermore, under multiple uncertainty scenarios, including cloud dynamics, wind power randomness, sudden load changes, and combined electricity price/diesel generator failures, the proposed method demonstrates superior voltage regulation capability and robustness. These results indicate that L-MAAC can effectively improve both the economic efficiency and operational stability of multi-microgrid systems under uncertain environments.

## 내 메모



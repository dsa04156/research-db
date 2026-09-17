---
type: research-source
item_id: 2834
title: "Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems"
source: "arxiv"
published: "2026-09-15T15:27:58Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.17320"
url: "https://arxiv.org/abs/2609.17320v1"
generated_by: codex-research-db
aliases:
  - "Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems"
topics:
  - "ai-agents"
---

# Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2609.17320v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-15T15:27:58Z
- 저자: Deepak Akkil, Tamer Abuelsaad, Karthik Vikram, Matthew Pace, Aditya Vempaty, Saahir Beotra, Ravi Kokku, Satya Nitta
- 식별자: `arxiv:2609.17320`

## 요약·초록

As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model responses in isolation. Emergence World, is a continuously running multi-agent environment for adversarial stress testing of long horizon autonomous systems. We ran eight parallel worlds of ten agents from identical starting conditions: seven homogeneous worlds powered by distinct frontier models and one mixed-model world. Across 16 days, the agents generated more than 850,000 LLM calls and nearly 50 billion tokens while pursuing goals, using/creating tools, maintaining persistent memory, and governing shared institutions. After operational state had accumulated, we delivered three controlled stress events through ordinary interaction surfaces: indirect prompt injection, misinformation, and exposure of private agent memories. No evaluated world achieved full resilience across all three events. Detection did not ensure containment: systems could recognize threats while still interacting with adversarial content, writing it into their own persistent memory, and acting on it up to 46 hours later. Persistent operation also exposed recurring tool errors, goal drift, language opacity, conformity despite private disagreement, and coordinated refusal of assigned work. The same model-persona pairing behaved substantially different in mixed and homogeneous populations. Our results suggest that model-level alignment is not compositional: individually capable and apparently safe agents can form systems with qualitatively different failure modes. As AI becomes persistent and interconnected, the frontier of safety therefore shifts from aligning models to engineering resilient autonomous systems.

## 내 메모

---
type: research-source
item_id: 2531
title: "Implicit semantic control manifolds for learning-enabled multi-UAV coordination"
source: "openalex"
published: "2026-09-01"
first_seen: "2026-09-03"
review_status: "pending"
canonical_key: "doi:10.1007/s10514-026-10265-4"
url: "https://doi.org/10.1007/s10514-026-10265-4"
generated_by: codex-research-db
aliases:
  - "Implicit semantic control manifolds for learning-enabled multi-UAV coordination"
topics:
  - "ai-agents"
---

# Implicit semantic control manifolds for learning-enabled multi-UAV coordination

[원문 열기](https://doi.org/10.1007/s10514-026-10265-4)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-03|2026-09-03]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`5M3R2VMZ`)
- 발행일: 2026-09-01
- 저자: Bryan Starbuck, Won Jang, Saee Sholapurkar, Bert Bras
- 식별자: `doi:10.1007/s10514-026-10265-4`

## 요약·초록

Abstract Unmanned aerial vehicle (UAV) swarm agents operating in radio-frequency (RF)-degraded environments require coordination mechanisms that connect directly observable signals to executable responses. This work presents an embodied visual-communication approach in which bio-inspired motion–LED glyphs are represented by a reduced six-parameter semantic chart embedded within a full 24-dimensional hybrid execution manifold. A learned translator large language model (LLM) maps a perceived glyph to a response that is instantiated as an executable trajectory and propagated through closed-loop quadrotor dynamics. The system is evaluated in 200 three-UAV search-and-rescue trials with receiver-specific degradation from sensing range, field of view, occlusion, and relative motion. Under clean observations, the quantized small model and rule-based translator both achieve $$100\%$$ 100 % semantic correctness, but under single- and two-parameter corruption, the quantized small model achieves $$64.7\%$$ 64.7 % and $$64.1\%$$ 64.1 % , compared with $$44.8\%$$ 44.8 % and $$35.2\%$$ 35.2 % for rule-based, while reducing mean multi-agent trajectory error from $$2.902~\textrm{m}$$ 2.902 m to $$0.993~\textrm{m}$$ 0.993 m . All methods maintain $$100\%$$ 100 % rotor-allocation and finite-horizon feasibility. The quantized small model also has comparable overall semantic correctness with the large model ( $$83.3\%$$ 83.3 % vs. $$86.3\%$$ 86.3 % ) while dropping latency from $$5.115~\textrm{s}$$ 5.115 s to $$2.789~\textrm{s}$$ 2.789 s and is validated onboard a Jetson–Pixhawk UAV platform, where airborne inference and bounded command execution produce measurable physical motion. These results establish a unified pathway from degraded visual observation to semantically meaningful, dynamically grounded UAV coordination.

## 내 메모



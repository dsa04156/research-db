---
type: research-source
item_id: 2539
title: "EcoFair: Energy-efficient inference routing for edge AI under data degradation"
source: "openalex"
published: "2026-09-01"
first_seen: "2026-09-03"
review_status: "pending"
canonical_key: "doi:10.1016/j.adhoc.2026.104403"
url: "https://doi.org/10.1016/j.adhoc.2026.104403"
generated_by: codex-research-db
aliases:
  - "EcoFair: Energy-efficient inference routing for edge AI under data degradation"
topics:
  - "edge-computing"
---

# EcoFair: Energy-efficient inference routing for edge AI under data degradation

[원문 열기](https://doi.org/10.1016/j.adhoc.2026.104403)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-09-03|2026-09-03]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`MXI3X635`)
- 발행일: 2026-09-01
- 저자: Mostafa Anoosha, Dhavalkumar Thakker, Kuniko Paxton, Koorosh Aslansefat, Bhupesh Kumar Mishra, Baseer Ahmad, Rameez Raja Kureshi
- 식별자: `doi:10.1016/j.adhoc.2026.104403`

## 요약·초록

Medical edge-AI systems must operate under a difficult tension: delivering reliable diagnostic inference while running on devices with limited battery capacity, memory, and compute. In dermatology, this problem is amplified by real-world image degradation caused by smartphone capture, poor lighting, blur, compression, and heterogeneous edge sensors. To handle these degraded inputs, deploying a heavyweight model can improve reliability, but it rapidly increases the energy burden on resource-constrained devices. Conversely, always using a lightweight model saves energy but may be less reliable on ambiguous or degraded inputs. This paper introduces EcoFair, a vertically partitioned inference framework for dermatology classification in which image and tabular inputs remain local to edge clients while only learned modality-specific representations are transmitted for server-side fusion. EcoFair first processes each sample using a lightweight image encoder and then decides whether additional heavyweight computation is necessary. Escalation is triggered when the lightweight prediction exhibits high uncertainty, a narrow separation between safe and high-risk classes, or elevated metadata-derived risk from patient age and lesion location. Across HAM10000, BCN20000, and PAD-UFES-20, EcoFair is evaluated using multiple lightweight–heavy backbone pairings to quantify the trade-off between energy consumption, diagnostic performance, and worst-group malignant-case recall. Results show that EcoFair can reduce per-sample image-inference energy by up to 68% relative to always using the heavyweight encoder, while selectively allocating additional computation under difficult data regimes to support inference reliability. Group-level analysis further shows configuration-dependent effects, with improvements in selected model–dataset settings and mixed behaviour in others.

## 내 메모



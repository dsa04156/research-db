---
type: research-source
item_id: 1365
title: "Robust Cross-Domain WiFi Fall Detection via Physics-Driven Attention-Enhanced Transformers"
source: "arxiv"
published: "2026-04-23T03:28:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.00869"
url: "https://arxiv.org/abs/2605.00869v1"
generated_by: codex-research-db
aliases:
  - "Robust Cross-Domain WiFi Fall Detection via Physics-Driven Attention-Enhanced Transformers"
topics:
  - "edge-computing"
---

# Robust Cross-Domain WiFi Fall Detection via Physics-Driven Attention-Enhanced Transformers

[원문 열기](https://arxiv.org/abs/2605.00869v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DZ5I4BZ4`)
- 발행일: 2026-04-23T03:28:12Z
- 저자: Yingzhe Wang, Cunhua Pan, Ruijing Liu, Shaokai Li, Hong Ren, Kezhi Wang, Jiangzhou Wang
- 식별자: `arxiv:2605.00869`

## 요약·초록

Device-free fall detection utilizing WiFi Channel State Information (CSI) has emerged as a promising, privacy-preserving solution for elderly health monitoring in the Internet of Things (IoT) era. However, existing deep learning approaches suffer from severe performance degradation when deployed in unseen environments due to static background overfitting and Non-Line-of-Sight (NLoS) signal attenuation. To address these critical bottlenecks, we propose a robust, domain-generalizable framework featuring a novel Attention-Enhanced CNN-Transformer hybrid architecture. First, we design a physics-driven \textbf{Dynamic Variance Gate (DVG)} to dynamically calculate local temporal variance, acting as a soft-attention mask that eliminates static environmental DC components while amplifying dynamic human motion. Second, we introduce a Physics-Aware Data Augmentation strategy to force the network to learn invariant morphological signatures rather than environment-specific noise. Furthermore, a Convolutional Block Attention Module (CBAM) is integrated to refine spatiotemporal features prior to Transformer-based sequence modeling. Extensive cross-domain evaluations across four distinct indoor environments demonstrate that our method achieves 97.6\% accuracy in NLoS scenarios and 98.8\% in completely unseen environments without target-domain fine-tuning. Finally, we deploy the proposed framework on an edge computing system equipped with commercial WiFi NICs. Real-world live inference field tests confirm the system's robustness against unseen environmental layouts and its capability for continuous, low-latency whole-home safety monitoring.

## 내 메모



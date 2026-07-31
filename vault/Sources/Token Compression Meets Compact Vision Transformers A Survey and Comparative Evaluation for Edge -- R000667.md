---
type: research-source
item_id: 667
title: "Token Compression Meets Compact Vision Transformers: A Survey and Comparative Evaluation for Edge AI"
source: "arxiv"
published: "2025-07-13T16:26:05Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.09702"
url: "https://arxiv.org/abs/2507.09702v1"
generated_by: codex-research-db
aliases:
  - "Token Compression Meets Compact Vision Transformers: A Survey and Comparative Evaluation for Edge AI"
topics:
  - "edge-computing"
  - "ai-agents"
---

# Token Compression Meets Compact Vision Transformers: A Survey and Comparative Evaluation for Edge AI

[원문 열기](https://arxiv.org/abs/2507.09702v1)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`W4C46G59`)
- 발행일: 2025-07-13T16:26:05Z
- 저자: Phat Nguyen, Ngai-Man Cheung
- 식별자: `arxiv:2507.09702`

## 요약·초록

Token compression techniques have recently emerged as powerful tools for accelerating Vision Transformer (ViT) inference in computer vision. Due to the quadratic computational complexity with respect to the token sequence length, these methods aim to remove less informative tokens before the attention layers to improve inference throughput. While numerous studies have explored various accuracy-efficiency trade-offs on large-scale ViTs, two critical gaps remain. First, there is a lack of unified survey that systematically categorizes and compares token compression approaches based on their core strategies (e.g., pruning, merging, or hybrid) and deployment settings (e.g., fine-tuning vs. plug-in). Second, most benchmarks are limited to standard ViT models (e.g., ViT-B, ViT-L), leaving open the question of whether such methods remain effective when applied to structurally compressed transformers, which are increasingly deployed on resource-constrained edge devices. To address these gaps, we present the first systematic taxonomy and comparative study of token compression methods, and we evaluate representative techniques on both standard and compact ViT architectures. Our experiments reveal that while token compression methods are effective for general-purpose ViTs, they often underperform when directly applied to compact designs. These findings not only provide practical insights but also pave the way for future research on adapting token optimization techniques to compact transformer-based networks for edge AI and AI agent applications.

## 내 메모



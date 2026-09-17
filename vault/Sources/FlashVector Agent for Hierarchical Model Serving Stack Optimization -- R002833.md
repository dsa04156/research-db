---
type: research-source
item_id: 2833
title: "FlashVector: Agent for Hierarchical Model Serving Stack Optimization"
source: "arxiv"
published: "2026-09-15T16:27:45Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.17391"
url: "https://arxiv.org/abs/2609.17391v1"
generated_by: codex-research-db
aliases:
  - "FlashVector: Agent for Hierarchical Model Serving Stack Optimization"
topics:
  - "ai-agents"
---

# FlashVector: Agent for Hierarchical Model Serving Stack Optimization

[원문 열기](https://arxiv.org/abs/2609.17391v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-15T16:27:45Z
- 저자: Qi Wu, Lohan Lemire, Kai Meng, Zhongmou Cai, Raphael Bargues, Petr Zhitnikov, Zeyuan Cao, Yao Wang, Shujun Bian, Wei Chen, Sean Sheng
- 식별자: `arxiv:2609.17391`

## 요약·초록

Model serving is one of the largest cost drivers in production recommender systems. Maximizing its throughput requires navigating a deeply layered hierarchy: GPU kernels, the ML framework computation graph, the model server, and on-demand feature processing -- each demanding specialized domain expertise. Such cross-layer expertise is inherently difficult to acquire, and does not scale with a workload that continuously grows and evolves, leaving significant cost efficiency gains unrealized. While recent AI agents have demonstrated human expert level efficiency in standalone GPU kernel optimization, automated tuning and optimization for the rest of the serving stack remain largely unexplored. We present FlashVector, an agentic system that optimizes performance across all layers of the model serving stack. The key contribution is an extensible framework to generalize the single kernel optimization agent paradigm to heterogeneous technical stacks, and to deliver performance improvements holistically. After deployment in Unity's Vector advertising platform, FlashVector achieved up to 2x throughput increase and up to 1.98x latency speedup on model server, and up to 1.6x throughput increase on feature store. These optimizations were discovered not only at the GPU kernel and computation graph levels, but also across the other components of the model serving stack, such as the model server (NVIDIA Triton's C++ codebase) and the on-demand feature transformation service (Python codebase), demonstrating the extensibility of the framework to more complex system architectures.

## 내 메모

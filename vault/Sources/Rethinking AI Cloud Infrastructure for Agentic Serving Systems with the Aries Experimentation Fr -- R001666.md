---
type: research-source
item_id: 1666
title: "Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework"
source: "arxiv"
published: "2026-07-31T06:44:06Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2607.29069"
url: "https://arxiv.org/abs/2607.29069v1"
generated_by: codex-research-db
aliases:
  - "Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework"
topics:
  - "cloud-infrastructure"
  - "self-evolving-harness"
---

# Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework

[원문 열기](https://arxiv.org/abs/2607.29069v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6Q5JGA8D`)
- 발행일: 2026-07-31T06:44:06Z
- 저자: Leonid Kondrashov, Hongrui Liu, JooYoung Park, Boxi Zhou, Zonghao Liu, Chengzhi Lu, Riccardo Mancini, Esha Choukse, Haris Javaid, German Sviridov, Tao Peng, Chen Zhao, Anastasia Avdeeva, Aleksei Gusev, Marios Kogias, Luo Mai, Dmitrii Ustiugov
- 식별자: `arxiv:2607.29069`

## 요약·초록

Autonomous agents challenge conventional LLM serving by coupling repeated inference with persistent context and sandboxed tool execution. We present Aries, a full-stack experimentation framework that separates task semantics from execution configurations, reconstructs cross-component agent trajectories with correlated system telemetry, and exposes stateful tool execution through a consistent interface across heterogeneous sandbox substrates. We use Aries to conduct reproducible experiments on open agent harnesses and benchmarks. We complement these experiments with production traces from a commercial platform, grounding low-level systems research in observed production behavior. Our results show that (1) token-centric metrics miss non-inference bottlenecks, (2) retaining additional context yields diminishing accuracy benefits while reducing serving capacity, and (3) tool sandboxes alternate between long idle periods and short resource bursts, while current snapshot-based state management makes aggressive suspension costly. A complementary security analysis further highlights the need to reduce the sandbox attack surface. We then discuss the vision for agent-native serving systems designed around trajectory-level metrics, adaptive context management, elastic sandbox resource management, and sandboxes with minimized attack surface.

## 내 메모



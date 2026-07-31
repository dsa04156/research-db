---
type: research-source
item_id: 1441
title: "Announcing the AI Gateway Working Group"
source: "rss:Kubernetes Blog"
published: "2026-03-09T18:00:00+00:00"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:c2b58f4a4a6ae180e5c1c6d49f4cbe9c1909f544933d19652e7273624d3fa079"
url: "https://kubernetes.io/blog/2026/03/09/announcing-ai-gateway-wg/"
generated_by: codex-research-db
aliases:
  - "Announcing the AI Gateway Working Group"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Announcing the AI Gateway Working Group

[원문 열기](https://kubernetes.io/blog/2026/03/09/announcing-ai-gateway-wg/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- Zotero: created (`SFXUMW54`)
- 발행일: 2026-03-09T18:00:00+00:00
- 식별자: `url:c2b58f4a4a6ae180e5c1c6d49f4cbe9c1909f544933d19652e7273624d3fa079`

## 요약·초록

The community around Kubernetes includes a number of Special Interest Groups (SIGs) and Working Groups (WGs) facilitating discussions on important topics between interested contributors. Today, we're excited to announce the formation of the AI Gateway Working Group , a new initiative focused on developing standards and best practices for networking infrastructure that supports AI workloads in Kubernetes environments. What is an AI Gateway? In a Kubernetes context, an AI Gateway refers to network gateway infrastructure (including proxy servers, load-balancers, etc.) that generally implements the Gateway API specification with enhanced capabilities for AI workloads. Rather than defining a distinct product category, AI Gateways describe infrastructure designed to enforce policy on AI traffic, including: Token-based rate limiting for AI APIs. Fine-grained access controls for inference APIs. Payload inspection enabling intelligent routing, caching, and guardrails. Support for AI-specific protocols and routing patterns. Working group charter and mission The AI Gateway Working Group operates under a clear charter with the mission to develop proposals for Kubernetes Special Interest Groups (SIGs) and their sub-projects. Its primary goals include: Standards Development : Create declarative APIs, standards, and guidance for AI workload networking in Kubernetes. Community Collaboration : Foster discussions and build consensus around best practices for AI infrastructure. Extensible Architecture : Ensure composability, pluggability, and ordered processing for AI-specific gateway extensions. Standards-Based Approach : Build on established networking foundations, layering AI-specific capabilities on top of proven standards. Active proposals WG AI Gateway currently has several active proposals that address key challenges in AI workload networking: Payload Processing The payload processing proposal addresses the critical need for AI workloads to inspect and transform full HTTP request and response payloads. This enables: AI Inference Security Guard against malicious prompts and prompt injection attacks. Content filtering for AI responses. Signature-based detection and anomaly detection for AI traffic. AI Inference Optimization Semantic routing based on request content. Intelligent caching to reduce inference costs and improve response times. RAG (Retrieval-Augmented Generation) system integration for context enhancement. The proposal defines standards for declarative payload processor configuration, ordered processing pipelines, and configurable failure modes - all essential for production AI workload deployments. Egress gateways Modern AI applications increasingly depend on external inference services, whether for specialized models, failover scenarios, or cost optimization. The egress gateways proposal aims to define standards for securely routing traffic outside the cluster. Key features include: External AI Service Integration Secure access to cloud-based AI services (OpenAI, Vertex AI, Bedrock, etc.). Managed authentication and token injection for third-party AI APIs. Regional compliance and failover capabilities. Advanced Traffic Management Backend resource definitions for external FQDNs and services. TLS policy management and certificate authority control. Cross-cluster routing for centralized AI infrastructure. User Stories We're Addressing Platform operators providing managed access to external AI services. Developers requiring inference failover across multiple cloud providers. Compliance engineers enforcing regional restrictions on AI traffic. Organizations centralizing AI workloads on dedicated clusters. Upcoming events KubeCon + CloudNativeCon Europe 2026, Amsterdam AI Gateway working group members will be presenting at KubeCon + CloudNativeCon Europe in Amsterdam, discussing the problems at the intersection of AI and networking, including the working group's active proposals, as well as the intersection of AI gateways with Model Context Protocol (MCP) and agent networking patterns. This session will showcase how AI Gateway working group proposals enable the infrastructure needed for next-generation AI deployments and communication patterns. The session will also include the initial designs, early prototypes, and emerging directions shaping the WG’s roadmap. For more details see our session here: AI'm at the Gate! Introducing the AI Gateway Working Group in Kubernetes Get involved The AI Gateway Working Group represents the Kubernetes community's commitment to standardizing AI workload networking. As AI becomes increasingly integral to modern applications, we need robust, standardized infrastructure that can support the unique requirements of inference workloads while maintaining the security, observability, and reliability standards that Kubernetes users expect. Our proposals are currently in active development, with implementations beginning across various gateway projects. We're working closely with SIG Network on Gateway API enhancements and collaborating with the broader cloud-native community to ensure our standards meet real-world production needs. Whether you're a gateway implementer, platform operator, AI application developer, or simply interested in the intersection of Kubernetes and AI, we'd love your input. The working group follows an open contribution model - you can review our proposals, join our weekly meetings, or start discussions on our GitHub repository. To learn more: Visit the working group's umbrella GitHub repository . Read the working group's charter . Join the weekly meeting on Thursdays at 2PM EST. Connect with the working group on Slack (#wg-ai-gateway) (visit https://slack.k8s.io/ for an invitation). Join the AI Gateway mailing list . The future of AI infrastructure in Kubernetes is being built today, join up and learn how you can contribute and help shape the future of AI-aware gateway capabilities in Kubernetes.

## 내 메모



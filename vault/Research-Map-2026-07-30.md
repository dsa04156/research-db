---
date: 2026-07-30
type: research-map
coverage_start: 2023-07-30
coverage_end: 2026-07-30
items: 1565
active_items: 1501
social_signals: 38
---

# AI agent·Kubernetes·Cloud·Edge 연구 지도

## 수집 범위

- 논문·공식 블로그·공식 릴리스: 최근 3년
- SNS·커뮤니티 신호: 최근 30일
- 관심 축: self-evolving harness, AI agents, Kubernetes, cloud infrastructure, edge computing
- SNS 글은 `lead_only`로 분리하며, 원문을 확인하기 전에는 사실 근거나 Zotero 항목으로 사용하지 않는다.

## 먼저 읽을 자료

### 1. Self-evolving harness

1. [Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/)
   - 연구 전체의 기준점. 모델 자체보다 워크플로·평가·권한·메모리·상태 관리가 성능을 좌우한다는 관점이다.
2. [Agentic Harness Engineering](https://arxiv.org/abs/2604.25850)
   - 구성요소, 경험, 의사결정을 관찰 가능한 형태로 만들고 실제 결과를 기준으로 하네스를 수정하는 폐루프를 다룬다.
3. [Self-Harness](https://arxiv.org/abs/2606.09498)
   - 더 강한 외부 에이전트 없이 하네스가 자신의 운영 구조를 개선하는 문제를 직접 다룬다.
4. [Continual Harness](https://arxiv.org/abs/2605.09998)
   - 프롬프트·서브에이전트·스킬·메모리를 지속적으로 수정하는 온라인 적응 구조다.
5. [Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity](https://arxiv.org/abs/2607.13683)
   - 단일 최고점만 쫓지 않고 다양한 후보를 유지하면서 품질 게이트를 통과시키는 탐색 전략이다.
6. [Phantom Guardrails](https://arxiv.org/abs/2607.13083)
   - 존재하지 않았던 실패를 에이전트가 잘못 진단해 불필요한 가드레일을 추가하는 위험을 보여준다.
7. [Self-Authored Verification Is Unreliable](https://arxiv.org/abs/2607.24300)
   - 수정 주체와 검증 주체가 같으면 점수는 좋아져도 실제 성능은 나빠질 수 있다는 핵심 경고다.
8. [MemoHarness](https://arxiv.org/abs/2607.14159)
   - 경험을 메모리로 축적해 하네스가 반복 실행에서 학습하는 구조를 다룬다.

### 2. AI agents on Kubernetes

1. [Running Agents on Kubernetes with Agent Sandbox](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/)
   - 도구 실행형 에이전트를 Kubernetes에서 격리하고 운영하는 공식 출발점이다.
2. [Kubernetes v1.36: Haru](https://kubernetes.io/blog/2026/04/22/kubernetes-v1-36-release/)
   - 최신 리소스·스케줄링·운영 변화가 AI 워크로드에 주는 영향을 확인할 기준 문서다.
3. [SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters](https://arxiv.org/abs/2605.00528)
   - 독립 요청이 아니라 여러 호출로 이어지는 에이전트 워크플로 전체를 GPU 스케줄링 단위로 본다.
4. [MAS-H2](https://arxiv.org/abs/2603.07607)
   - cloud-native 환경에서 다중 에이전트를 이용한 계층적 autoscaling을 다룬다.
5. [K8S Power Irrigation](https://arxiv.org/abs/2605.25218)
   - Kubernetes 마이크로서비스의 성능과 전력 효율을 함께 최적화하는 강화학습 접근이다.

### 3. Cloud·serverless infrastructure

1. [CASA: SLO and Carbon-Aware Autoscaling](https://arxiv.org/abs/2409.00550)
   - 서버리스 autoscaling에서 SLO와 탄소 비용을 함께 고려한다.
2. [Optimizing simultaneous autoscaling for serverless cloud computing](https://arxiv.org/abs/2310.19013)
   - 여러 서버리스 구성요소의 동시 확장을 최적화하는 기반 연구다.
3. [Securing Production Debugging in Kubernetes](https://kubernetes.io/blog/2026/03/18/securing-production-debugging-in-kubernetes/)
   - 자동화 에이전트에 디버깅 권한을 줄 때 필요한 운영·보안 통제와 연결된다.
4. [Admission Policies That Can't Be Deleted](https://kubernetes.io/blog/2026/05/04/kubernetes-v1-36-manifest-based-admission-control/)
   - 에이전트의 클러스터 변경을 정책 계층에서 제한하는 데 중요한 공식 변화다.

### 4. Edge computing·distributed inference

1. [Internet of Agentic Things](https://arxiv.org/abs/2607.12662)
   - 네트워크로 연결된 에이전트가 IoT 환경을 폐루프로 관찰·판단·제어하는 구조를 제안한다.
2. [Efficient Routing of Inference Requests across LLM Instances in Cloud-Edge Computing](https://arxiv.org/abs/2507.15553)
   - cloud와 edge의 여러 LLM 인스턴스 사이에서 지연·비용을 고려해 요청을 라우팅한다.
3. [Active Inference-Based Adaptive Routing for Heterogeneous Edge AI Services](https://arxiv.org/abs/2604.17373)
   - 이질적인 edge AI 서비스 사이의 적응형 라우팅 문제를 다룬다.
4. [Comparative Analysis of Lightweight Kubernetes Distributions for Edge Computing](https://arxiv.org/abs/2504.03656)
   - 제한된 edge 자원에서 경량 Kubernetes 배포판의 성능과 자원 효율을 비교한다.
5. [Trusting the Cloud-Native Edge](https://arxiv.org/abs/2405.10131)
   - 원격 attestation을 통해 edge Kubernetes worker를 신뢰하는 보안 구조다.
6. [Ray 2.56.0](https://github.com/ray-project/ray/releases/tag/ray-2.56.0)
   - 분산 추론·에이전트 실행 기반의 실제 구현 변화를 추적할 공식 릴리스다.

## 현재 보이는 연구 축

1. **성능보다 검증 구조가 먼저다.** 자기개선 루프의 핵심 위험은 평가기까지 같은 에이전트가 통제하면서 잘못된 개선을 승인하는 것이다.
2. **하네스의 편집 단위가 넓어지고 있다.** 프롬프트뿐 아니라 메모리, 스킬, 도구, 워크플로, 권한, 라우팅을 함께 최적화한다.
3. **에이전트 인프라는 요청 단위에서 워크플로 단위로 이동한다.** GPU 스케줄링과 autoscaling도 여러 단계의 에이전트 실행을 하나의 작업으로 이해해야 한다.
4. **Kubernetes는 실행 기반이면서 보안 경계다.** sandbox, admission policy, identity, observability가 에이전트 운영의 핵심 계층이 된다.
5. **cloud-edge 배치는 비용·지연·프라이버시의 동적 최적화 문제다.** 항상 cloud 또는 항상 edge가 아니라 상태에 따라 실행 위치를 바꾸는 방향이 강하다.

## 다음 검토 순서

1. 위 하네스 핵심 자료 8개를 읽고 `검증기 독립성`, `rollback`, `평가 데이터 누출`을 비교한다.
2. Kubernetes 자료에서 agent sandbox, GPU scheduling, admission control을 하나의 운영 아키텍처로 연결한다.
3. edge 자료는 routing objective가 지연·비용·에너지·프라이버시 중 무엇을 최적화하는지 표로 비교한다.
4. SNS 신호는 논점 발견에만 사용하고, 주장마다 논문·공식 문서 원문을 다시 연결한다.

# 4. Kubernetes와 cloud-native AI 계층

## 검증된 핵심 주장

**clm_004 — Kubernetes 기반 AI 인프라는 컨테이너 배치에서 더 나아가
분리형 가속기 자원, 안전 게이트, 통합 ML 수명주기와 관찰 가능성을 다루는
방향으로 확장되고 있다.**

CoHDI는 Kubernetes DRA를 이용해 GPU 같은 장치를 노드에 동적으로 연결·분리하고,
prefill과 decode처럼 단계별 자원 요구가 다른 추론을 대상으로 제시한다
([src_010](https://www.cncf.io/blog/2026/07/28/welcome-cohdi-to-the-cncf-evolving-kubernetes-into-composable-disaggregated-infrastructures/)).
다만 CNCF Sandbox 단계이므로 운영 표준으로 간주해서는 안 된다.

Kubeflow는 데이터 처리, 파이프라인, 분산 학습, 튜닝을 하나의 SDK 흐름으로
묶고, CRD 기반 Notebook과 Trainer 확장을 진행하고 있다
([src_011](https://www.cncf.io/blog/2026/07/28/kubeflow-unveils-new-cloud-native-innovations-to-supercharge-ai/)).
여기에도 alpha·proposal 단계 기능이 섞여 있어 성숙도를 별도로 기록해야 한다.

운영 안정성 측면에서는 autoscaler의 추천 앞에 anomaly·policy·conflict
검사를 배치하고 dry-run과 rollback을 두는 제안이 나왔다
([src_009](https://arxiv.org/abs/2607.26503)). 일반 controller 운영에서도
cache scope, index, APIReader 같은 읽기 경로 선택이 메모리와 API 부하에 직접
연결된다
([src_015](https://kubernetes.io/blog/2026/07/29/controller-runtime-cache/)).

개인 연구 관점에서 Kubernetes 자료에는 기능명뿐 아니라 다음 상태를 붙이는
것이 유용하다.

- maturity: proposal / alpha / beta / stable / CNCF sandbox
- resource model: Pod / workload / DRA device / disaggregated phase
- safety gate: dry-run / policy / anomaly / rollback / human approval
- observability: trace / metric / event / OpenTelemetry
- portability: upstream / vendor-specific / managed-service-only

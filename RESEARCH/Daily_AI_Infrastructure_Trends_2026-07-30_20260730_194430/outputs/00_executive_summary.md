# 2026-07-30 AI 인프라·에이전트 연구 요약

## 오늘의 결론

1. **자기진화형 하네스는 유망하지만 아직 “자동 진화가 항상 낫다”는 단계는
   아니다.** 최적화 대상은 프롬프트에서 컨텍스트, 워크플로, 하네스 코드로
   넓어지고 있으나 동일 계산 예산과 held-out 평가에서는 일반적 우월성이
   확립되지 않았다
   ([src_001](https://lilianweng.github.io/posts/2026-07-04-harness/);
   [src_002](https://arxiv.org/abs/2607.12227);
   [src_003](https://arxiv.org/abs/2607.15524);
   [src_004](https://arxiv.org/abs/2607.13683)).
2. **개선 루프보다 승인 경계가 먼저다.** 하네스가 바꿀 수 있는 표면을
   제한하고, 제안자와 평가기를 분리하며, sealed test와 회귀 테스트를 통과한
   변경만 승격하는 구조가 개인 연구 자동화에도 맞다
   ([src_001](https://lilianweng.github.io/posts/2026-07-04-harness/);
   [src_002](https://arxiv.org/abs/2607.12227);
   [src_004](https://arxiv.org/abs/2607.13683)).
3. **Kubernetes의 AI 계층은 장치·워크로드·토폴로지·추론 상태를 함께 보는
   방향으로 이동 중이다.** DRA와 PodGroup, 분산 추론 라우팅, 토폴로지 라벨을
   따로 보지 말고 하나의 운영 스택으로 추적할 필요가 있다
   ([src_005](https://arxiv.org/abs/2607.22242);
   [src_006](https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/);
   [src_007](https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/);
   [src_008](https://github.com/llm-d/llm-d);
   [src_009](https://github.com/llm-d/llm-d/releases);
   [src_010](https://docs.nvidia.com/topograph/engines/kubernetes)).
4. **에이전트 런타임은 일반적인 stateless Pod와 다른 수명주기가 필요하다.**
   상태, 신원, 격리, suspend/resume와 warm pool을 지원하는 더 높은 수준의
   추상화가 등장하고 있다
   ([src_011](https://www.cncf.io/blog/2026/07/14/is-a-pod-the-right-deployment-unit-for-an-ai-agent/);
   [src_012](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/)).
5. **엣지는 클라우드 대체가 아니라 선택적 배치 문제다.** 품질, 지연, 비용,
   프라이버시와 장치 자원을 동시에 보고 요청별로 cloud/edge를 선택하는
   연구가 핵심이다
   ([src_013](https://doi.org/10.1109/JIOT.2026.3663918);
   [src_014](https://arxiv.org/abs/2507.15553)).

## 약한 신호

TikTok에서는 동일 계산 예산의 단순 재시도와 하네스 진화를 비교해야 한다는
논점이, LinkedIn에서는 하네스·평가·메모리와 Kubernetes DRA가, Reddit에서는
통제 가능한 자기개선 메모리가 반복적으로 등장했다. 다만 추천 알고리즘 편향,
작은 표본, 날짜 불확실성 때문에 방향 탐색용으로만 본다
([src_015](https://www.tiktok.com/@rajistics/video/7664394161205923102);
[src_016](https://www.linkedin.com/posts/shen-sean-chen_you-can-learn-ai-agent-harness-loop-engineering-activity-7478447459745210368-R6DR);
[src_017](https://www.linkedin.com/posts/kubefm_kubernetes-currently-manages-cpu-memory-activity-7485056484427522049-lm1O);
[src_018](https://www.reddit.com/r/ContextEngineering/comments/1va8gr5/dejadb_governed_selfimproving_memory_for_ai_agents/)).

Threads도 이번 실행에서 조회했지만 최종 품질 기준을 통과한 결과는 없었다.

## 미확정

- 자기진화형 하네스의 두 자릿수 성능 향상 또는 최대 60% 비용 절감 수치는
  동일 조건의 독립 재현이 없어 일반화하지 않는다.
- SNS 언급량만으로 시장 채택 또는 기술 성숙도를 판단하지 않는다.

## 개인 연구 DB에 적용

매일 읽을 것은 원문 전체가 아니라 `오늘의 브리핑` 하나다. 원문과 상세
메타데이터는 Obsidian의 Source 노트와 Zotero에 보관하고, 브리핑에는 검증된
결론, 약한 신호, 다음 추적 질문만 남긴다. 다음 자동화 질문은
“새 하네스 논문이 matched-compute·held-out 평가를 제공했는가?”와
“Kubernetes AI 프로젝트가 실제 릴리스·GA 단계로 이동했는가?” 두 가지다.

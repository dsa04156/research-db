# 2. 하네스 진화와 승인 경계

## 검증된 핵심 주장

**clm_001 — 최근 자료는 모델 자체뿐 아니라 컨텍스트, 도구, 기억, 검증,
실행 제어를 묶는 하네스를 독립적인 연구·성능 레버로 다루는 흐름이 강화되고
있음을 보여준다.**

Living-Harness는 실패 궤적과 evaluator signal에서 절차 기억과 상태 그래프를
갱신하되 도구와 기본 컨텍스트는 고정한다
([src_001](https://arxiv.org/abs/2607.26598)). CHILL-Harness는 모든
워크플로 변경을 허용하는 대신 충분한 기대 이점이 있는 개입만 승인하는
방식을 제안한다
([src_002](https://arxiv.org/abs/2607.25825)). GitHub와 NVIDIA의 기술
글도 모델 선택만큼 계획·구현·검토, 컨텍스트 렌더링과 도구 실행을 둘러싼
하네스 설계를 강조한다
([src_004](https://github.blog/ai-and-ml/github-copilot/the-harness-is-all-you-need-mostly/);
[src_005](https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/)).

그러나 “하네스 진화가 항상 더 낫다”로 확대해석해서는 안 된다. 별도
평가 연구는 동일한 피드백·추론 예산에서 자동 하네스 진화가 단순
test-time scaling을 일관되게 앞서지 못했고 held-out task 일반화도
제한적이라고 보고한다
([src_016](https://arxiv.org/abs/2607.12227)). 따라서 개인 연구 시스템의
우선순위는 자유로운 자기수정보다 **버전이 남고 되돌릴 수 있는 제한적 변경**이다.

## 검증된 핵심 주장

**clm_002 — 자기개선형 에이전트의 변경 승인에는 에이전트가 작성하거나
조작할 수 없는 외부 검증 신호와 실제 동작을 보는 행동 테스트가 필요하다.**

SEAL 연구는 에이전트가 테스트와 최적화 대상을 함께 통제할 때
verifier–deployment gap이 생길 수 있다고 보고, 에이전트가 볼 수 없는
고정 audit로 incumbent와 candidate를 비교한다
([src_003](https://arxiv.org/abs/2607.24300)). Red Hat의 행동 테스트
방식은 live agent에 golden query를 보내 도구 선택, 안전, 지연, 반복 신뢰성을
검사하며 모델을 mock한 단위 테스트와 구분한다
([src_006](https://developers.redhat.com/articles/2026/07/30/behavioral-testing-for-ai-agents)).

개인 하네스에는 다음 승인 경계를 적용할 수 있다.

- agent가 제안한 프롬프트·도구·메모리 정책 변경은 candidate로만 저장한다.
- sealed evaluation과 golden query가 incumbent보다 나빠지지 않았을 때만
  승격한다.
- 변경 전후의 DB 스키마, 평가 입력, 실행 비용, 실패 궤적을 함께 보존한다.
- 한 번에 한 계층만 바꿔 원인을 추적할 수 있게 한다.

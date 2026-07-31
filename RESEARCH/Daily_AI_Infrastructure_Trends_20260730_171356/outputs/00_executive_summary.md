# 최신 AI 인프라·에이전트 연구 요약

조사 기간은 2026년 7월 24일부터 30일까지다. 17개 출처를 등록하고 핵심 주장
5개를 교차검증했다. 이번 주의 중심 변화는 “더 큰 모델” 하나가 아니라
**하네스의 지속적 개선, 외부 검증, 실행 궤적 관찰, 자원 오케스트레이션**을
한 시스템으로 다루기 시작했다는 점이다.

## 먼저 볼 것

1. **자기개선의 승인 경계** — 에이전트가 자신의 변경과 테스트를 모두 통제하게
   두지 말고, 고정된 외부 승인 신호와 실제 행동 회귀 테스트를 둔다
   ([src_003](https://arxiv.org/abs/2607.24300);
   [src_006](https://developers.redhat.com/articles/2026/07/30/behavioral-testing-for-ai-agents)).
2. **하네스 상태를 제한적으로 진화** — 도구와 기본 컨텍스트까지 무제한으로
   재작성하기보다, 실패에서 얻은 절차 기억과 상태 전이를 제한된 범위에서
   갱신하는 설계가 등장했다
   ([src_001](https://arxiv.org/abs/2607.26598);
   [src_002](https://arxiv.org/abs/2607.25825)).
3. **장기 실행을 관찰 가능한 시스템으로 취급** — 최종 답변 외에 궤적,
   도구 선택, 지속 메모리, 삭제·복구 결과를 저장하고 평가해야 한다
   ([src_007](https://arxiv.org/abs/2607.26300);
   [src_008](https://arxiv.org/abs/2607.27080)).
4. **Kubernetes AI 계층의 확장** — DRA 기반 분리형 장치, 안전 게이트,
   Kubeflow의 통합 수명주기처럼 스케줄링 위의 운영 계층이 넓어지고 있다
   ([src_010](https://www.cncf.io/blog/2026/07/28/welcome-cohdi-to-the-cncf-evolving-kubernetes-into-composable-disaggregated-infrastructures/);
   [src_011](https://www.cncf.io/blog/2026/07/28/kubeflow-unveils-new-cloud-native-innovations-to-supercharge-ai/)).
5. **엣지는 클라우드 대체가 아니라 선택적 배치** — 재현성, 지연, 데이터 통제,
   자원 예측에 따라 클라우드·사설·엣지를 나누는 하이브리드 관점이 타당하다
   ([src_012](https://arxiv.org/abs/2607.23227);
   [src_014](https://www.techradar.com/pro/the-case-for-moving-creative-production-ai-to-the-edge)).

## Confidence

- 검증 게이트: 핵심 주장 5개 verified
- 출처 구성: 공식 프로젝트 3개(B), 프리프린트·기술 블로그·전문가 기고
  14개(D)
- 해석: 방향성 판단에는 유용하지만 개별 프리프린트의 성능 수치는 재현이나
  피어리뷰 전까지 일반화하지 않는다.

## Refuted

이번 claim ledger에서 반박으로 폐기된 핵심 주장은 없다.

## Unresolved

이번 claim ledger에서 미확정으로 분류된 핵심 주장은 없다. 다만 자동 하네스
진화가 단순 test-time scaling보다 항상 우월하다는 주장은 근거가 부족하여
애초에 핵심 주장에 포함하지 않았다
([src_016](https://arxiv.org/abs/2607.12227)).

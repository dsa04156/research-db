# Executive summary

이번 재실행에서 확인된 가장 큰 변화는 self-improving harness의 범위가 prompt·skill 수정에서 multi-agent topology와 실행 중 정보교환으로 넓어지고 있다는 점이다. MANTA와 AgentRadio는 각각 협업 구조의 제한적 갱신과 비동기 passive awareness를 제안한다. 다만 성능 수치는 아직 독립 재현이 없는 preprint 결과이므로 구조적 아이디어만 채택한다. [src_002] [src_003] [src_004] [src_005] [src_013]

운영 관점에서는 model 자체보다 외부 control plane이 더 중요한 공통분모로 남았다. 권한·sandbox·package provenance·memory recovery를 모델 밖에서 강제해야 하며, Kubernetes에서는 admission만으로 잡기 어려운 실행 경로를 runtime 검증으로 보완해야 한다. [src_001] [src_007] [src_008] [src_009] [src_010] [src_020] [src_021]

Inference infrastructure도 동일한 방향이다. Triton Control과 Modelplane은 model lifecycle, routing, performance test, fleet placement를 control plane으로 끌어올리고, Asari·NVIDIA·OpenAI 운영 자료는 성능이 workload·topology·runtime·scheduler·correctness의 결합 문제임을 보여준다. [src_011] [src_012] [src_013] [src_014] [src_015]

Edge는 cloud를 없애는 전략이 아니라 latency·bandwidth·privacy·connectivity 제약에 맞춰 workload를 나누는 배치 문제로 보는 것이 타당하다. [src_016] [src_017] [src_018]

Confidence: verified synthesis는 중간 이상. 새 preprint의 benchmark 수치, PAIChecker 오류율의 일반화, 초기 control-plane 프로젝트의 채택 규모, SNS 신호는 미확정이다. [src_006] [src_019] [src_022] [src_023]

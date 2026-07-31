# 4. 개인 연구용 권장 구조

## 권장 데이터 흐름

```text
공식 API · RSS · GitHub · Zotero
                ↓
       SQLite 후보 자료함
  원문 메타데이터·중복·sightings
                ↓
        Codex 관련도 판정
        ┌───────┴────────┐
      보류/제외         채택
                         ↓
          한국어 구조화 요약 DB
                         ↓
          Obsidian 자료별 소스 노트
                         ↓
          일일·주간·주제별 종합 노트
```

## 데이터 소유권

- DOI, 저자, 학술지, PDF, 인용키: Zotero가 소유
- 웹 글·릴리스까지 포함한 후보 자료와 수집 이력: SQLite가 소유
- AI 한국어 요약과 요약 버전: SQLite가 소유
- 사람이 고친 해석, 연구 아이디어, 논문 초안 연결: Obsidian이 소유
- 일일 자동 브리핑: SQLite에서 생성하되 Obsidian에 Markdown으로 출력

Codex가 다시 실행될 때 사람의 문장을 덮어쓰지 않도록 `AI 생성 영역`과 `내 메모 영역`을 분리해야 한다. ZotFlow도 자동 생성 소스 노트와 개인 해석을 분리하거나 잠금 영역을 두는 방향을 사용한다. (src_005; [ZotFlow](https://github.com/duanxianpi/zotflow))

## 다음으로 추가할 테이블

```sql
item_summaries(
  id,
  item_id,
  language,
  title_ko,
  summary_ko,
  key_points_json,
  methods_ko,
  results_ko,
  limitations_ko,
  why_relevant_ko,
  evidence_json,
  model,
  prompt_version,
  source_hash,
  created_at
)
```

같은 자료를 새 모델이나 새 프롬프트로 다시 정리하더라도 기존 요약을 덮어쓰지 않고 새 버전으로 남겨야 한다.

PDF 전체 검색은 처음부터 넣지 않아도 된다. **문헌에 대한 신뢰도 높은 질의응답은 단순 요약 DB보다 전문 검색 인덱스와 근거 구간·인용 추적을 추가한 별도 계층을 요구한다.** (clm_006; src_008, src_009) 실제로 “내 논문 200편 전체에 질문하기”가 필요해질 때 PaperQA2 또는 별도 전문검색을 붙이면 된다.

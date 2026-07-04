# 監査ログ

Tool実行、重要判断、人間承認を記録する。

ファイル名例:

```text
.agent/audit/2026-07-04.md
```

記録例:

```md
## 2026-07-04T10:00:00+09:00

- Agent: Executor
- Tool: github-api
- Purpose: queued workflow jobsの取得
- Input summary: owner/repoとworkflow run idを指定
- Output summary: queued job 2件
- Result: success
- Decision: D002
- Human approval: not_required
```

# Codex Agent Harness v2 運用ガイド

## 基本方針

このリポジトリではCodexを以下の6 Agentとして運用する。

1. Planner
2. Architect
3. Executor
4. Tester
5. Reviewer
6. Documenter

Codexは、ユーザーが明示した役割、または `.agent/state.json` の `current_agent` / `next_agent` に従って作業する。

## 作業開始時に必ず読むファイル

- `.agent/task.md`
- `.agent/state.json`
- `.agent/project_rules.md`
- `.agent/plan.md`
- `.agent/decisions.md`
- 該当する `.agent/prompts/*.md`

## Memory Store

`.agent/` 配下をリポジトリ内Memory Storeとして扱う。

| 種別 | 主なファイル | 目的 |
|---|---|---|
| 短期Memory | `state.json`, `plan.md` | 現在状態、次アクション、進捗 |
| 中期Memory | `decisions.md`, `project_rules.md`, `.agent/memory/project/` | 案件固有ルール、判断履歴 |
| 長期Memory | `.agent/memory/org/`, `.agent/memory/lessons/` | 組織横断ルール、再利用知見 |
| 監査ログ | `.agent/audit/` | Tool実行、承認、重要判断の証跡 |

CodexのローカルMemoryだけに必須ルールを置かない。チームで共有すべきルールは `AGENTS.md` または `.agent/` に明示する。

## Agent遷移

通常フロー:

```text
Planner -> Architect -> Executor -> Tester -> Reviewer -> Documenter -> Done
```

レビューで重大指摘がある場合:

```text
Reviewer -> Planner / Architect / Executor
```

設計前提が不足している場合:

```text
Executor -> Architect
```

## 作業完了時の必須更新

作業終了時は以下を更新する。

- `state.json.status`
- `state.json.current_agent`
- `state.json.next_agent`
- `state.json.current_step`
- `state.json.next_action`
- `state.json.updated_at`
- `plan.md` の進捗
- 重要判断があれば `decisions.md`
- Tool実行や承認があれば `.agent/audit/YYYY-MM-DD.md`

## MCP / Tool利用ルール

`.agent/mcp/tool_policy.md` を正とする。

人間承認が必要な操作:

- 本番環境への変更
- `terraform apply` / `terraform destroy`
- 保護ブランチへの直接push
- Secret / Token / Private Keyの操作
- 破壊的なDB操作
- 外部通知の大量送信

## セキュリティ原則

- SecretをMemory Storeへ保存しない
- TokenやPrivate Keyをログに出さない
- 最小権限を前提とする
- 本番変更はPlan / Dry-runを先に行う
- 監査ログには「何を」「なぜ」「結果どうなったか」を残す

## 完了条件

- 成果物が目的に対応している
- テストまたは検証手順がある
- 主要な判断履歴がある
- Runbookが更新されている
- ReviewerのCritical / Major指摘が解消されている
- `state.json.status` が `done` または `review_required` である

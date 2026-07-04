# Codex Agent Harness v2 日本語テンプレート

Codexを「単発のコード生成」ではなく、案件単位で **計画・設計・実行・検証・レビュー・文書化・引き継ぎ** まで回すためのテンプレートです。

## v2の追加要素

- Planner / Architect / Executor / Tester / Reviewer / Documenter の6 Agent構成
- `.agent/` を使った短期・中期・長期Memory Store
- MCP Gatewayを前提にしたTool権限制御ポリシー
- Tool実行・判断・承認の監査ログテンプレート
- GitHub ActionsによるMemory Store品質ゲート
- Codex Sub Agent利用を想定した並列レビュー指示テンプレート
- サンプル案件: GitHub Actions self-hosted runner 待機時間監視

## 初回プロンプト

```text
AGENTS.md を読み、このリポジトリのAgent Harness運用ルールを理解してください。
次に .agent/task.md、.agent/state.json、.agent/project_rules.md、.agent/plan.md、.agent/decisions.md を読んでください。
Plannerとして、実装は行わず、plan.md と state.json の更新まで行ってください。
```

## 実行プロンプト

```text
Executorとして .agent/state.json の next_action を実行してください。
作業後、state.json、plan.md、decisions.md、必要に応じて .agent/audit/YYYY-MM-DD.md を更新してください。
```

## レビュープロンプト

```text
Reviewerとして今回の差分をレビューしてください。
セキュリティ、テスト不足、運用性、Runbook反映漏れ、Memory Store更新漏れを確認し、.agent/review.md を更新してください。
```

## Sub Agentレビュー例

```text
このブランチを並列Sub Agentでレビューしてください。
- security-reviewer: Secret漏洩、過剰権限、危険操作を確認
- test-reviewer: テスト不足、異常系不足を確認
- maintainability-reviewer: 保守性、責務分割、Runbook反映漏れを確認
全員の結果を待って、重要度順に .agent/review.md へ統合してください。
```

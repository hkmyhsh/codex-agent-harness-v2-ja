# Runbook: Runner待機時間監視

## アラート内容

20分以上queued状態のWorkflow jobが検知された。

## 初動確認

1. 通知されたRepository / Workflow / Job URLを開く
2. 必要なrunner labelを確認する
3. 対象runner groupにオンラインrunnerが存在するか確認する
4. ARC / autoscaler / Kubernetes nodeの状態を確認する
5. GitHub API Rate Limitや認証エラーがないか確認する

## 主な原因

- runner不足
- runner label不一致
- ARC scale-out遅延
- Kubernetes node不足
- Network / Proxy障害
- GitHub App権限不足

## 復旧対応

- runner poolのスケール確認
- label定義の修正
- ARC controller log確認
- node autoscaler確認
- 一時的なrunner追加

## 再発防止

- ラベル設計の標準化
- runner容量見積もりの見直し
- 待機時間メトリクスの継続監視
- 通知閾値の見直し

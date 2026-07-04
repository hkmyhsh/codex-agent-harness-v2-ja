# 基本設計: GitHub Actions Runner待機時間監視

## 目的

GitHub Actionsのself-hosted runnerで20分以上待機しているWorkflow jobを検知し、運用者へ通知する。

## 構成案

```text
EventBridge Scheduler
  -> Lambda
    -> GitHub API
    -> queued job抽出
    -> 通知済み状態確認
    -> Slack通知
    -> CloudWatch Logs / Metrics
```

## 認証

GitHub App認証を優先する。PATは原則避ける。

## 検知条件

- job statusが `queued`
- 現在時刻 - queued開始時刻 >= 20分
- 直近で同一jobを通知済みでない

## 通知内容

- Repository
- Workflow名
- Run ID / Job ID
- 待機時間
- Runner label
- 参照URL
- 想定原因の確認観点

## 非機能要件

- 重複通知を抑制する
- GitHub API Rate Limitを考慮する
- Lambda失敗時はCloudWatch Alarmで検知する
- SecretはSecrets ManagerまたはParameter Storeで管理する

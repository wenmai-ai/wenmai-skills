# FastMoss `video_data_trends` API 参考

### video_data_trends

查看单支视频的播放/互动趋势

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/video-data-trends` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.end_date` | string | 否 | 结束日期。 |
| `filter.start_date` | string | 否 | 开始日期。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。 |
| `filter.video_id` | string | 是 | 视频 ID。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.daily_trend` | array | 视频每日播放、点赞、评论和分享趋势 |
| `data.daily_trend[].comment_count` | integer | 评论数。 |
| `data.daily_trend[].date` | string | 日期。 |
| `data.daily_trend[].inc_comment_count` | integer | 数量。 |
| `data.daily_trend[].inc_like_count` | integer | 数量。 |
| `data.daily_trend[].inc_play_count` | integer | 数量。 |
| `data.daily_trend[].inc_share_count` | integer | 数量。 |
| `data.daily_trend[].like_count` | integer | 点赞数。 |
| `data.daily_trend[].play_count` | integer | 播放数。 |
| `data.daily_trend[].share_count` | integer | 分享数。 |
| `data.daily_trend[].video_id` | string | 视频 ID。 |
| `data.end_date` | string | 结束日期。 |
| `data.period_stats` | object | 周期统计。 |
| `data.period_stats.comment_count` | integer | 评论数。 |
| `data.period_stats.ipm` | integer | IPM。 |
| `data.period_stats.like_count` | integer | 点赞数。 |
| `data.period_stats.play_count` | integer | 播放数。 |
| `data.period_stats.share_count` | integer | 分享数。 |
| `data.period_stats.snapshot_at` | integer | 数据快照时间。 |
| `data.period_stats.video_created_at` | integer | 时间。 |
| `data.start_date` | string | 开始日期。 |
| `data.video_id` | string | 视频 ID。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "video_id" : "7676578620709588237"
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/video-data-trends" `
  -Method POST `
  -Headers @{
    "secret-key" = $API_KEY
    "Content-Type" = "application/json"
  } `
  -Body $body `
  -TimeoutSec 120

$response.Content
```

#### cURL 请求示例

```bash
curl -sS -X POST \
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/video-data-trends" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "video_id" : "7676578620709588237"
  }
}'
```

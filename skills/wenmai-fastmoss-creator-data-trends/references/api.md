# FastMoss `creator_data_trends` API 参考

### creator_data_trends

查看达人的粉丝/互动/带货趋势

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/creator-data-trends` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.end_date` | string | 否 | 结束日期。 |
| `filter.field_type` | string | 是 | 趋势指标类型。可选值：follower_change（粉丝变化数）、play_count（播放量）、like_count（点赞数）、comment_count（评论数）、collect_count（收藏数）、share_count（分享数）、units_sold（销量）、gmv（GMV）、video_units_sold（视频销量）、video_gmv（视频 GMV）、live_units_sold（直播销量）、live_gmv（直播 GMV）、showcase_units_sold（橱窗销量）、showcase_gmv（橱窗 GMV）。 |
| `filter.start_date` | string | 否 | 开始日期。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、14（近 14 天）、28（近 28 天）、90（近 90 天）。默认值：28。 |
| `filter.uid` | string | 是 | 达人 UID。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.channel` | string | 渠道。 |
| `data.currency` | null | 币种。 |
| `data.end_date` | string | 结束日期。 |
| `data.granularity` | string | 时间粒度。 |
| `data.metric` | string | 指标编码。 |
| `data.metric_label` | string | 指标名称。 |
| `data.series` | array | 趋势序列。 |
| `data.series[].date` | string | 日期。 |
| `data.series[].value` | integer | 数值。 |
| `data.start_date` | string | 开始日期。 |
| `data.summary` | object | 汇总信息。 |
| `data.summary.average_per_day` | number | 日均值。 |
| `data.summary.lowest_date` | string | 时间。 |
| `data.summary.lowest_value` | integer | 最低值。 |
| `data.summary.peak_date` | string | 时间。 |
| `data.summary.peak_value` | integer | 峰值。 |
| `data.summary.total` | integer | 符合条件的记录总数。 |
| `data.time_range_days` | integer | 统计时间范围天数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "uid" : "6861118469497553925",
    "field_type" : "follower_change",
    "time_range_days" : 28
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/creator-data-trends" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/creator-data-trends" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "uid" : "6861118469497553925",
    "field_type" : "follower_change",
    "time_range_days" : 28
  }
}'
```

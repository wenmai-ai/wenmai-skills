# FastMoss `creator_video_analysis` API 参考

### creator_video_analysis

分析达人的内容方向与带货视频

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/creator-video-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.end_date` | string | 否 | 结束日期。 |
| `filter.orderby` | array | 否 | 排序规则。 |
| `filter.orderby[].field` | string | 否 | 排序或统计字段。可选值：create_time（创建时间）、play_count（播放量）、digg_count（点赞数）、share_count（分享数）、comment_count（评论数）、sold_count（销量）、sale_amount（销售金额）。 |
| `filter.orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `filter.page` | integer | 否 | 页码。默认值：1。最小值：1。最大值：500。 |
| `filter.pagesize` | integer | 否 | 每页条数。最大值：10。 |
| `filter.start_date` | string | 否 | 开始日期。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、14（近 14 天）、28（近 28 天）、90（近 90 天）。 |
| `filter.type` | string | 否 | 类型。 |
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
| `data.video_list` | object | 达人带货视频列表 |
| `data.video_list.list` | array | 结果列表。 |
| `data.video_list.list[].caption_text` | string | 视频文案。 |
| `data.video_list.list[].comment_count` | integer | 评论数。 |
| `data.video_list.list[].cover_url` | string | 封面 URL。 |
| `data.video_list.list[].creator_handle` | string | 达人唯一用户名。 |
| `data.video_list.list[].duration_seconds` | integer | 时长（秒）。 |
| `data.video_list.list[].interaction_rate_percent` | number | 互动率百分比。 |
| `data.video_list.list[].is_ad` | boolean | 是否为广告流量。 |
| `data.video_list.list[].like_count` | integer | 点赞数。 |
| `data.video_list.list[].linked_product_count` | integer | 数量。 |
| `data.video_list.list[].linked_products` | array | 关联商品列表。 |
| `data.video_list.list[].linked_products[].cover_url` | string | 封面 URL。 |
| `data.video_list.list[].linked_products[].price` | string | 价格。 |
| `data.video_list.list[].linked_products[].product_id` | string | 商品 ID。 |
| `data.video_list.list[].linked_products[].product_units_sold` | integer | 销量。 |
| `data.video_list.list[].linked_products[].title` | string | 标题。 |
| `data.video_list.list[].play_count` | integer | 播放数。 |
| `data.video_list.list[].published_at` | integer | 时间。 |
| `data.video_list.list[].region` | string | 国家或地区代码。 |
| `data.video_list.list[].share_count` | integer | 分享数。 |
| `data.video_list.list[].snapshot_at` | string | 数据快照时间。 |
| `data.video_list.list[].video_gmv` | number | 视频 GMV。 |
| `data.video_list.list[].video_id` | string | 视频 ID。 |
| `data.video_list.list[].video_units_sold` | integer | 视频销量。 |
| `data.video_list.page` | integer | 当前页码。 |
| `data.video_list.total` | integer | 符合条件的记录总数。 |
| `data.video_tag_summary` | object | 达人视频标签与内容方向汇总 |
| `data.video_tag_summary.tag_distribution` | array | 标签分布。 |
| `data.video_tag_summary.tag_distribution[].percentage` | number | 占比。 |
| `data.video_tag_summary.tag_distribution[].tag` | string | 标签。 |
| `data.video_tag_summary.tag_distribution[].video_count` | integer | 视频数。 |
| `data.video_tag_summary.top_tag` | object | 主要标签。 |
| `data.video_tag_summary.top_tag.percentage` | number | 占比。 |
| `data.video_tag_summary.top_tag.tag` | string | 标签。 |
| `data.video_tag_summary.top_tag.video_count` | integer | 视频数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "uid" : "6861118469497553925",
    "page" : 1,
    "time_range_days" : 28
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/creator-video-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/creator-video-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "uid" : "6861118469497553925",
    "page" : 1,
    "time_range_days" : 28
  }
}'
```

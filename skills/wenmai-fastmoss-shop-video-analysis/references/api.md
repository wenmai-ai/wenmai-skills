# FastMoss `shop_video_analysis` API 参考

### shop_video_analysis

分析店铺的带货视频表现

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-video-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 过滤参数。 |
| `filter.is_ad` | boolean | 否 | 是否为广告视频。 |
| `filter.publish_end_date` | string | 否 | 发布结束日期。 |
| `filter.publish_start_date` | string | 否 | 发布开始日期。 |
| `filter.publish_time_range_days` | integer | 否 | 发布时间范围（天）。可选值：7（发布不超过 7 天）、28（发布不超过 28 天）、90（发布不超过 90 天）。 |
| `filter.seller_id` | string | 是 | 店铺卖家 ID。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、28（近 28 天）、90（近 90 天）。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：video_create_time（视频发布时间）、units_sold（销量）、gmv（GMV）、digg_count（点赞数）、play_count（播放量）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码。默认值：1。最小值：1。最大值：500。 |
| `pagesize` | integer | 否 | 每页条数。默认值：10。最大值：10。 |
| `filter.creator_uid` | string | 否 | 店铺关联达人uid。 |
| `filter.creator_unique_id` | string | 否 | 店铺关联达人唯一ID @xxxxxxx。 |
| `filter.shop_name` | string | 否 | 店铺名称。 |
| `filter.region` | string | 否 | 店铺所在国家/地区。seller_name 和 region 必须同时传。 |
| `filter.create_time_range` | object | 否 | 视频发布时间范围:{"min":1700000000,"max":1700000000}。 |
| `filter.create_time_range.min` | number | 否 | 最小值。 |
| `filter.create_time_range.max` | number | 否 | 最大值。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.summary` | object | 汇总信息。 |
| `data.summary.region` | string | 国家或地区代码。 |
| `data.summary.total_play_count` | integer | 数量。 |
| `data.summary.total_video_gmv` | integer | GMV。 |
| `data.summary.video_count` | integer | 视频数。 |
| `data.videos` | object | 店铺带货视频列表 |
| `data.videos.items` | array | 明细列表。 |
| `data.videos.total` | integer | 符合条件的记录总数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28,
    "publish_time_range_days" : 7
  },
  "orderby" : [ {
    "field" : "play_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/shop-video-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-video-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28,
    "publish_time_range_days" : 7
  },
  "orderby" : [ {
    "field" : "play_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

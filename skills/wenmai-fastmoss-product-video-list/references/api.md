# FastMoss `product_video_list` API 参考

### product_video_list

查看哪些视频在带货这个商品

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-video-list` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.create_time_range` | object | 否 | 创建时间范围。 |
| `filter.create_time_range.max` | number | 否 | 最大值。 |
| `filter.create_time_range.min` | number | 否 | 最小值。 |
| `filter.is_ad` | boolean | 否 | 是否为广告视频。 |
| `filter.product_id` | string | 是 | 商品 ID。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。 |
| `orderby` | array | 否 | 排序规则。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：gmv（GMV）、units_sold（销量）、digg_count（点赞数）、play_count（播放量）、share_count（分享数）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码。默认值：1。最小值：1。最大值：500。 |
| `pagesize` | integer | 否 | 每页条数。默认值：10。最大值：10。 |
| `product_id` | string | 是 | 商品 ID。 |
| `days` | integer | 否 | 最近N天(视频发布时间)。 |
| `create_time_range` | integer | 否 | 视频发布时间范围，例如：{min: 1767196800, max: 1777278619}。 |
| `is_ad` | integer | 否 | 是否为广告，0否，1是。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.page` | integer | 当前页码。 |
| `data.pagesize` | integer | 每页条数。 |
| `data.product_id` | string | 商品 ID。 |
| `data.total` | integer | 符合条件的记录总数。 |
| `data.videos` | array | 商品关联带货视频 |
| `data.videos[].creator` | object | 达人资料。 |
| `data.videos[].creator.creator_handle` | string | 达人唯一用户名。 |
| `data.videos[].creator.creator_uid` | string | 达人 UID。 |
| `data.videos[].engagement_metrics` | object | 互动指标。 |
| `data.videos[].engagement_metrics.comment_count` | integer | 评论数。 |
| `data.videos[].engagement_metrics.like_count` | integer | 点赞数。 |
| `data.videos[].engagement_metrics.play_count` | integer | 播放数。 |
| `data.videos[].engagement_metrics.share_count` | integer | 分享数。 |
| `data.videos[].product_contribution` | object | 商品贡献。 |
| `data.videos[].product_contribution.shop_id` | string | 店铺 ID。 |
| `data.videos[].product_contribution.video_gmv` | number | 视频 GMV。 |
| `data.videos[].product_contribution.video_units_sold` | integer | 视频销量。 |
| `data.videos[].traffic_flags` | object | 流量标记。 |
| `data.videos[].traffic_flags.is_ad` | boolean | 是否为广告流量。 |
| `data.videos[].video_id` | string | 视频 ID。 |
| `data.videos[].video_meta` | object | 视频元信息。 |
| `data.videos[].video_meta.caption_text` | string | 视频文案。 |
| `data.videos[].video_meta.cover_url` | string | 封面 URL。 |
| `data.videos[].video_meta.duration_seconds` | integer | 时长（秒）。 |
| `data.videos[].video_meta.fastmoss_url` | string | fastmoss URL。 |
| `data.videos[].video_meta.published_at` | integer | 时间。 |
| `data.videos[].video_meta.region` | string | 国家或地区代码。 |
| `data.videos[].video_meta.tiktok_url` | string | tiktok URL。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "product_id" : "1733683494177178921",
    "create_time_range" : {
      "max" : 1777278619,
      "min" : 1767196800
    }
  },
  "orderby" : {
    "field" : "play_count",
    "order" : "desc"
  },
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-video-list" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-video-list" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "product_id" : "1733683494177178921",
    "create_time_range" : {
      "max" : 1777278619,
      "min" : 1767196800
    }
  },
  "orderby" : {
    "field" : "play_count",
    "order" : "desc"
  },
  "pagesize" : 10
}'
```

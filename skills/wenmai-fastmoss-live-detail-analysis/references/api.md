# FastMoss `live_detail_analysis` API 参考

### live_detail_analysis

分析单场直播的整体表现

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/live-detail-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.room_id` | string | 是 | 直播间 ID。 |
| `lang` | string | 否 | 返回语言。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.category_breakdown` | object | 直播成交类目分布 |
| `data.category_breakdown.by_gmv` | array | GMV。 |
| `data.category_breakdown.by_gmv[].category_id` | integer | 类目 ID。 |
| `data.category_breakdown.by_gmv[].category_names` | array | 类目名称列表。 |
| `data.category_breakdown.by_gmv[].share` | integer | 占比。 |
| `data.category_breakdown.by_product_count` | array | 数量。 |
| `data.category_breakdown.by_product_count[].category_id` | integer | 类目 ID。 |
| `data.category_breakdown.by_product_count[].category_names` | array | 类目名称列表。 |
| `data.category_breakdown.by_product_count[].share` | integer | 占比。 |
| `data.creator` | object | 达人资料 |
| `data.creator.creator_categories` | array | 达人类目列表。 |
| `data.creator.creator_region` | string | 达人所在地区。 |
| `data.creator.follower_count` | integer | 粉丝数 |
| `data.creator.handle` | string | 账号 unique_id。 |
| `data.creator.historical_avg_units_sold` | integer | 销量。 |
| `data.creator.historical_avg_viewer_count` | integer | 数量。 |
| `data.creator.historical_live_count` | integer | 数量。 |
| `data.creator.nickname` | string | 达人昵称 |
| `data.creator.uid` | string | 达人 UID |
| `data.creator.video_count` | integer | 视频数。 |
| `data.live` | object | 直播场次资料 |
| `data.live.cover_url` | string | 封面 URL。 |
| `data.live.currency` | string | 币种。 |
| `data.live.duration_seconds` | integer | 时长（秒）。 |
| `data.live.end_time` | integer | 直播结束时间 |
| `data.live.gmv_per_thousand_viewers` | number | GMV。 |
| `data.live.hashtags` | array | 话题标签。 |
| `data.live.is_live` | integer | 是否标记。 |
| `data.live.is_shop_live` | integer | 是否标记。 |
| `data.live.like_count` | integer | 点赞数。 |
| `data.live.live_source` | string | 直播来源。 |
| `data.live.room_id` | string | 直播间 ID |
| `data.live.seller_id` | string | 店铺卖家 ID。 |
| `data.live.shop_avatar_url` | string | 店铺头像 URL。 |
| `data.live.shop_name` | string | 店铺名称。 |
| `data.live.start_time` | integer | 直播开始时间 |
| `data.live.title` | string | 直播标题 |
| `data.live.top_category_id` | integer | ID。 |
| `data.live.top_category_names` | array | 头部类目名称。 |
| `data.live.top_category_share` | integer | 头部类目占比。 |
| `data.live.traffic_source_share` | object | 流量来源占比。 |
| `data.live.traffic_source_share.from_following` | integer | 来自关注的流量。 |
| `data.live.traffic_source_share.from_video_detail` | integer | 来自视频详情的流量。 |
| `data.live.traffic_source_share.other` | integer | 其他。 |
| `data.live.updated_at` | integer | 数据更新时间。 |
| `data.performance` | object | 表现数据。 |
| `data.performance.avg_selling_price` | number | 平均售价。 |
| `data.performance.avg_viewer_count` | integer | 数量。 |
| `data.performance.gmv` | number | 成交总额 GMV。 |
| `data.performance.gmv_per_hour` | number | GMV。 |
| `data.performance.gmv_per_thousand_viewers` | number | GMV。 |
| `data.performance.gmv_per_viewer` | number | GMV。 |
| `data.performance.new_follower_count` | integer | 数量。 |
| `data.performance.peak_viewer_count` | integer | 数量。 |
| `data.performance.product_count` | integer | 商品数。 |
| `data.performance.products_with_sales_count` | integer | 产生销量的商品数。 |
| `data.performance.region` | string | 国家或地区代码。 |
| `data.performance.session_duration_seconds` | integer | 场次时长（秒）。 |
| `data.performance.total_viewer_count` | integer | 数量。 |
| `data.performance.units_sold` | integer | 销量。 |
| `data.performance.units_sold_per_hour` | integer | 销量。 |
| `data.performance.units_sold_per_viewer_rate` | number | 销量。 |
| `data.performance.viewer_to_follower_rate` | number | 观看转粉率。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "room_id" : "7539139975317703438"
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/live-detail-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/live-detail-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "room_id" : "7539139975317703438"
  }
}'
```

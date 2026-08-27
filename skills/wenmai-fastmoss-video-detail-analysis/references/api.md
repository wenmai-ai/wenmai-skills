# FastMoss `video_detail_analysis` API 参考

### video_detail_analysis

查看单支视频的表现与带货商品

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/video-detail-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.video_id` | string | 是 | 视频 ID。 |
| `lang` | string | 否 | 返回语言。 |
| `orderby` | array | 否 | 排序规则。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：units_sold（销量）、gmv（GMV）、launch_time（上架时间）、commission_rate（佣金率）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码。默认值：1。最小值：1。最大值：500。 |
| `pagesize` | integer | 否 | 每页条数。默认值：10。最大值：10。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.creator` | object | 达人资料 |
| `data.creator.avg_video_like_count` | integer | 数量。 |
| `data.creator.avg_video_play_count` | integer | 数量。 |
| `data.creator.category` | object | 类目。 |
| `data.creator.category.category_id` | integer | 类目 ID。 |
| `data.creator.category.category_name` | string | 类目名称。 |
| `data.creator.creator_handle` | string | 达人唯一用户名。 |
| `data.creator.creator_uid` | string | 达人 UID。 |
| `data.creator.follower_count` | integer | 粉丝数 |
| `data.creator.nickname` | string | 达人昵称 |
| `data.creator.region` | string | 达人所属国家或地区代码 |
| `data.creator.total_like_count` | integer | 获赞总数。 |
| `data.creator.video_count` | integer | 视频数。 |
| `data.linked_products` | object | 视频关联商品 |
| `data.linked_products.items` | array | 明细列表。 |
| `data.linked_products.items[].commerce_metrics` | object | 电商指标。 |
| `data.linked_products.items[].commerce_metrics.video_attributed_gmv` | number | 视频归因 GMV。 |
| `data.linked_products.items[].commerce_metrics.video_attributed_units_sold` | integer | 视频归因销量。 |
| `data.linked_products.items[].product` | object | 商品资料。 |
| `data.linked_products.items[].product.category_name` | string | 类目名称。 |
| `data.linked_products.items[].product.commission_rate_percent` | integer | 佣金率百分比。 |
| `data.linked_products.items[].product.cover_url` | string | 封面 URL。 |
| `data.linked_products.items[].product.current_price` | number | 当前价格。 |
| `data.linked_products.items[].product.is_off_shelf` | boolean | 是否已下架。 |
| `data.linked_products.items[].product.launch_date` | string | 上架日期。 |
| `data.linked_products.items[].product.launch_time` | integer | 上架时间戳。 |
| `data.linked_products.items[].product.price_display` | string | 价格展示文案。 |
| `data.linked_products.items[].product.product_id` | string | 商品 ID。 |
| `data.linked_products.items[].product.product_rating` | number | 商品评分。 |
| `data.linked_products.items[].product.region` | string | 国家或地区代码。 |
| `data.linked_products.items[].product.seller_id` | string | 店铺卖家 ID。 |
| `data.linked_products.items[].product.title` | string | 标题。 |
| `data.linked_products.summary` | object | 汇总信息。 |
| `data.linked_products.summary.region` | string | 国家或地区代码。 |
| `data.linked_products.summary.video_attributed_gmv` | number | 视频归因 GMV。 |
| `data.linked_products.summary.video_attributed_units_sold` | integer | 视频归因销量。 |
| `data.linked_products.total` | integer | 符合条件的记录总数。 |
| `data.video` | object | 视频资料 |
| `data.video.caption_text` | string | 视频文案。 |
| `data.video.cover_url` | string | 封面 URL。 |
| `data.video.creator_uid` | string | 达人 UID。 |
| `data.video.duration_seconds` | integer | 时长（秒）。 |
| `data.video.engagement_metrics` | object | 互动指标。 |
| `data.video.engagement_metrics.comment_count` | integer | 评论数。 |
| `data.video.engagement_metrics.favorite_count` | integer | 收藏数。 |
| `data.video.engagement_metrics.interaction_rate_percent` | number | 互动率百分比。 |
| `data.video.engagement_metrics.like_comment_ipm` | integer | 点赞评论 IPM。 |
| `data.video.engagement_metrics.like_count` | integer | 点赞数。 |
| `data.video.engagement_metrics.play_count` | integer | 播放数。 |
| `data.video.engagement_metrics.share_count` | integer | 分享数。 |
| `data.video.linked_product_count` | integer | 数量。 |
| `data.video.published_at_ts` | integer | 发布时间戳。 |
| `data.video.region` | string | 国家或地区代码。 |
| `data.video.traffic_flags` | object | 流量标记。 |
| `data.video.traffic_flags.is_ad` | boolean | 是否为广告流量。 |
| `data.video.updated_at_display` | string | 更新时间展示文案。 |
| `data.video.updated_at_ts` | integer | 更新时间戳。 |
| `data.video.video_id` | string | 视频 ID |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "video_id" : "7676578620709588237"
  },
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/video-detail-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/video-detail-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "video_id" : "7676578620709588237"
  },
  "pagesize" : 10
}'
```

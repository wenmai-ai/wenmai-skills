# FastMoss `video_search` API 参考

### video_search

用关键词搜索视频

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/video-search` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤参数。 |
| `filter.create_time_range` | object | 是 | 发布时间范围。 |
| `filter.create_time_range.max` | number | 否 | 最大值。 |
| `filter.create_time_range.min` | number | 否 | 最小值。 |
| `filter.creator_category_id` | integer | 否 | 达人分类 ID。 |
| `filter.creator_uid` | integer | 否 | 达人 UID。 |
| `filter.creator_unique_id` | string | 否 | 达人唯一用户名。 |
| `filter.digg_count_range` | object | 否 | 点赞量区间，例如：{'min': 100000, 'max': 500000}。 |
| `filter.digg_count_range.max` | number | 否 | 最大值。 |
| `filter.digg_count_range.min` | number | 否 | 最小值。 |
| `filter.follower_count_range` | object | 否 | 粉丝量区间，例如：{'min': 100000, 'max': 500000}。 |
| `filter.follower_count_range.max` | number | 否 | 最大值。 |
| `filter.follower_count_range.min` | number | 否 | 最小值。 |
| `filter.interact_rate_range` | object | 否 | 互动率区间，例如：{'min': 10, 'max': 20} （10%-20%）。 |
| `filter.interact_rate_range.max` | number | 否 | 最大值。 |
| `filter.interact_rate_range.min` | number | 否 | 最小值。 |
| `filter.is_ecommerce` | boolean | 否 | 是否为带货视频 1.是。 |
| `filter.play_count_range` | object | 否 | 播放量区间，例如：{'min': 100000, 'max': 500000}。 |
| `filter.play_count_range.max` | number | 否 | 最大值。 |
| `filter.play_count_range.min` | number | 否 | 最小值。 |
| `filter.product_category_id` | integer | 否 | 商品分类 ID。 |
| `filter.region` | string | 否 | 国家/地区。region 范围: ['US','GB','MX','ES','DE','IT','FR','ID','VN','MY','TH','PH','BR','JP','SG']。 |
| `keywords` | string | 否 | 搜索关键词。 |
| `lang` | string | 否 | 语言设置，英语(默认值)：EN_US 中文：ZH_CN。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：follower_count（粉丝数）、create_time（创建时间）、play_count（播放量）、digg_count（点赞数）、units_sold（销量）、interact_rate（互动率）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码，默认值：1。page * pagesize <= 5000。 |
| `pagesize` | integer | 否 | 每页条数，默认值：10。page * pagesize <= 5000。pagesize 范围[1,100]。 |

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
| `data.videos` | object | 视频列表。 |
| `data.videos.has_more` | boolean | 是否还有下一页。 |
| `data.videos.items` | array | 明细列表。 |
| `data.videos.items[].caption_text` | string | 视频文案。 |
| `data.videos.items[].commerce_flags` | object | 电商标记。 |
| `data.videos.items[].commerce_flags.has_linked_product` | boolean | 是否关联商品。 |
| `data.videos.items[].commerce_metrics` | object | 电商指标。 |
| `data.videos.items[].commerce_metrics.video_attributed_gmv` | integer | 视频归因 GMV。 |
| `data.videos.items[].commerce_metrics.video_attributed_units_sold` | integer | 视频归因销量。 |
| `data.videos.items[].cover_url` | string | 封面 URL。 |
| `data.videos.items[].creator` | object | 达人资料。 |
| `data.videos.items[].creator.avatar_url` | string | 头像 URL。 |
| `data.videos.items[].creator.category` | object | 类目。 |
| `data.videos.items[].creator.category.category_id` | integer | 类目 ID。 |
| `data.videos.items[].creator.category.category_name` | string | 类目名称。 |
| `data.videos.items[].creator.creator_handle` | string | 达人唯一用户名。 |
| `data.videos.items[].creator.creator_uid` | string | 达人 UID。 |
| `data.videos.items[].creator.follower_count` | integer | 粉丝数。 |
| `data.videos.items[].creator.nickname` | string | 昵称。 |
| `data.videos.items[].creator.region` | string | 国家或地区代码。 |
| `data.videos.items[].duration_seconds` | integer | 时长（秒）。 |
| `data.videos.items[].engagement_metrics` | object | 互动指标。 |
| `data.videos.items[].engagement_metrics.comment_count` | integer | 评论数。 |
| `data.videos.items[].engagement_metrics.favorite_count` | integer | 收藏数。 |
| `data.videos.items[].engagement_metrics.interaction_rate_percent` | number | 互动率百分比。 |
| `data.videos.items[].engagement_metrics.like_count` | integer | 点赞数。 |
| `data.videos.items[].engagement_metrics.play_count` | integer | 播放数。 |
| `data.videos.items[].engagement_metrics.share_count` | integer | 分享数。 |
| `data.videos.items[].linked_products` | array | 关联商品列表。 |
| `data.videos.items[].published_at_display` | string | 发布时间展示文案。 |
| `data.videos.items[].published_at_ts` | integer | 发布时间戳。 |
| `data.videos.items[].traffic_flags` | object | 流量标记。 |
| `data.videos.items[].traffic_flags.is_ad` | boolean | 是否为广告流量。 |
| `data.videos.items[].video_id` | string | 视频 ID。 |
| `data.videos.items[].video_url` | string | 视频链接。 |
| `data.videos.next_search_after` | null | 下一页游标。 |
| `data.videos.total` | integer | 符合条件的记录总数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "is_ecommerce" : 1,
    "create_time_range" : {
      "max" : 1787443199,
      "min" : 1787356800
    },
    "creator_category_id" : 4,
    "product_category_id" : 12,
    "follower_count_range" : {
      "max" : 100000,
      "min" : 1000
    }
  },
  "orderby" : [ {
    "field" : "follower_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/video-search" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/video-search" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "is_ecommerce" : 1,
    "create_time_range" : {
      "max" : 1787443199,
      "min" : 1787356800
    },
    "creator_category_id" : 4,
    "product_category_id" : 12,
    "follower_count_range" : {
      "max" : 100000,
      "min" : 1000
    }
  },
  "orderby" : [ {
    "field" : "follower_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

## JIIMORE

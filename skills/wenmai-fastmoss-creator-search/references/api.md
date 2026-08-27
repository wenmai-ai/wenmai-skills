# FastMoss `creator_search` API 参考

### creator_search

用昵称/关键词搜索达人

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/creator-search` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤条件。 |
| `filter.creator_category_id` | integer | 否 | 达人类目 ID。 |
| `filter.creator_type` | integer | 否 | 账号类型: 1 (Personal), 2 (Shop)。 |
| `filter.follower_age_type` | integer | 否 | 粉丝主力年龄段。 |
| `filter.follower_gender_type` | integer | 否 | 粉丝性别类型。 |
| `filter.follower_range` | object | 否 | 粉丝数范围。 |
| `filter.follower_range.max` | number | 否 | 最大值。 |
| `filter.follower_range.min` | number | 否 | 最小值。 |
| `filter.is_ecommerce_creator` | boolean | 否 | 是否是带货达人。 |
| `filter.is_mcn_creator` | boolean | 否 | 是否为 MCN 达人。 |
| `filter.product_category_l1_id` | integer | 否 | 商品一级类目 ID。 |
| `filter.product_category_l2_id` | integer | 否 | 商品二级类目 ID。 |
| `filter.product_category_l3_id` | integer | 否 | 商品三级类目 ID。 |
| `filter.region` | string | 否 | 国家/地区。region 范围: ['US','GB','MX','ES','DE','IT','FR','ID','VN','MY','TH','PH','BR','JP','SG']。 |
| `filter.uid` | string | 否 | 达人 UID。 |
| `filter.unique_id` | string | 否 | 达人唯一ID @xxxxxxx。 |
| `filter.verify_type` | integer | 否 | 认证类型: 1 (Normal), 2 (Blue V)。 |
| `keywords` | string | 否 | 查询关键词。 |
| `orderby` | array | 否 | 排序条件。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：follower_count（粉丝数）、day28_follower_count（近 28 天新增粉丝数）、video_count（视频数）、video_avg_play_count（视频平均播放量）、video_avg_digg_count（视频平均点赞数）、day28_units_sold（近 28 天销量）、day28_gmv（近 28 天 GMV）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码, default: 1。page * pagesize <= 5000。 |
| `pagesize` | integer | 否 | 每页数量, default: 10。page * pagesize <= 5000。pagesize 范围[1, 100]。 |
| `filter.category_id` | integer | 否 | 达人分类。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.list` | array | 达人搜索结果 |
| `data.list[].audience_summary` | object | 粉丝画像摘要 |
| `data.list[].audience_summary.age_distribution` | array | 年龄分布。 |
| `data.list[].audience_summary.age_distribution[].age_range` | string | 年龄区间。 |
| `data.list[].audience_summary.age_distribution[].percentage` | number | 占比。 |
| `data.list[].audience_summary.gender_distribution` | array | 性别分布。 |
| `data.list[].audience_summary.gender_distribution[].gender` | string | 性别。 |
| `data.list[].audience_summary.gender_distribution[].percentage` | number | 占比。 |
| `data.list[].commerce_summary` | object | 近期开播、视频与带货摘要 |
| `data.list[].commerce_summary.currency` | string | 币种。 |
| `data.list[].commerce_summary.day28_follower_count` | integer | 近 28 天粉丝变化。 |
| `data.list[].commerce_summary.day28_gmv` | integer | 近 28 天 GMV。 |
| `data.list[].commerce_summary.day28_live_count` | integer | 近 28 天直播场次。 |
| `data.list[].commerce_summary.day28_live_gmv` | integer | 近 28 天直播 GMV。 |
| `data.list[].commerce_summary.day28_units_sold` | integer | 近 28 天销量。 |
| `data.list[].commerce_summary.day28_video_count` | integer | 近 28 天视频数。 |
| `data.list[].commerce_summary.engagement_rate_percent` | number | 互动率百分比。 |
| `data.list[].commerce_summary.has_email` | boolean | 是否公开邮箱。 |
| `data.list[].commerce_summary.live_gmv` | integer | 直播 GMV。 |
| `data.list[].commerce_summary.live_units_sold` | integer | 直播销量。 |
| `data.list[].commerce_summary.total_gmv` | number | 累计 GMV。 |
| `data.list[].commerce_summary.total_units_sold` | integer | 累计销量。 |
| `data.list[].commerce_summary.trend_categories` | array | 趋势类目。 |
| `data.list[].commerce_summary.trend_categories[].id` | integer | ID。 |
| `data.list[].commerce_summary.trend_categories[].name` | string | 名称。 |
| `data.list[].commerce_summary.video_avg_digg_count` | integer | 视频平均点赞数。 |
| `data.list[].commerce_summary.video_avg_play_count` | integer | 视频平均播放量。 |
| `data.list[].commerce_summary.video_gmv` | number | 视频 GMV。 |
| `data.list[].commerce_summary.video_units_sold` | integer | 视频销量。 |
| `data.list[].creator` | object | 达人资料 |
| `data.list[].creator.account_type_code` | integer | 账号类型编码。 |
| `data.list[].creator.avatar` | string | 达人头像 URL |
| `data.list[].creator.category` | object | 类目。 |
| `data.list[].creator.category.id` | integer | ID。 |
| `data.list[].creator.category.name` | string | 名称。 |
| `data.list[].creator.creator_type_code` | integer | 编码。 |
| `data.list[].creator.follower_count` | integer | 粉丝数 |
| `data.list[].creator.live_count_total` | integer | 直播总场次。 |
| `data.list[].creator.nickname` | string | 达人昵称 |
| `data.list[].creator.region` | string | 达人所属国家或地区代码 |
| `data.list[].creator.seller_id` | string | 店铺卖家 ID。 |
| `data.list[].creator.uid` | string | 达人 UID |
| `data.list[].creator.unique_id` | string | 达人唯一用户名 |
| `data.list[].creator.verify_type_code` | integer | 编码。 |
| `data.list[].creator.video_count_total` | integer | 视频总数。 |
| `data.total` | integer | 符合条件的记录总数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "category_id" : 1,
    "follower_range" : {
      "max" : 10000,
      "min" : 1000
    }
  },
  "orderby" : [ {
    "field" : "follower_count",
    "order" : "desc"
  } ],
  "keywords" : "daisycabral_",
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/creator-search" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/creator-search" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "category_id" : 1,
    "follower_range" : {
      "max" : 10000,
      "min" : 1000
    }
  },
  "orderby" : [ {
    "field" : "follower_count",
    "order" : "desc"
  } ],
  "keywords" : "daisycabral_",
  "pagesize" : 10
}'
```

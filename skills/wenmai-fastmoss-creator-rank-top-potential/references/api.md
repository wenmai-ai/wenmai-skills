# FastMoss `creator_rank_top_potential` API 参考

### creator_rank_top_potential

查看有带货潜力的达人排行榜

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/creator-rank-top-potential` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤参数。 |
| `filter.category_path` | array | 否 | 类目路径。 |
| `filter.creator_category_id` | integer | 否 | 达人类目 ID。 |
| `filter.date_type` | string | 是 | 统计周期类型。可选值：day（按日）、week（按周）、month（按月）。 |
| `filter.date_value` | string | 是 | 统计周期值。 |
| `filter.ecommerce_type` | integer | 否 | 1:视频带货 2:直播带货。 |
| `filter.follower_age_type` | object | 否 | 粉丝年龄分布 1:18-24,2:25-34,3:35+。 |
| `filter.follower_count_range` | object | 否 | 粉丝数范围。 |
| `filter.follower_count_range.max` | number | 否 | 最大值。 |
| `filter.follower_count_range.min` | number | 否 | 最小值。 |
| `filter.follower_gender_type` | integer | 否 | 粉丝性别分布 0:女，1:男。 |
| `filter.region` | string | 否 | 国家/地区。region 范围: ['US','GB','MX','ES','DE','IT','FR','ID','VN','MY','TH','PH','BR','JP','SG']。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：potential_index（潜力指数）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码，默认值：1。page * pagesize <= 1000。 |
| `pagesize` | integer | 否 | 每页条数，默认值：10。page * pagesize <= 1000。pagesize 范围 [1, 100]。 |
| `filter.product_category_l1_id` | integer | 否 | 商品一级分类。 |
| `filter.product_category_l2_id` | integer | 否 | 商品二级分类。 |
| `filter.product_category_l3_id` | integer | 否 | 商品三级分类。 |
| `filter.date_info` | object | 是 | 日期信息。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.date_type` | string | 榜单周期类型 |
| `data.date_value` | string | 榜单周期值；周榜格式为 YYYY-Www |
| `data.list` | array | 结果列表。 |
| `data.list[].audience_summary` | object | 受众摘要。 |
| `data.list[].audience_summary.age_distribution` | array | 年龄分布。 |
| `data.list[].audience_summary.age_distribution[].age_range` | string | 年龄区间。 |
| `data.list[].audience_summary.age_distribution[].percentage` | number | 占比。 |
| `data.list[].audience_summary.gender_distribution` | array | 性别分布。 |
| `data.list[].audience_summary.gender_distribution[].gender` | string | 性别。 |
| `data.list[].audience_summary.gender_distribution[].percentage` | number | 占比。 |
| `data.list[].creator` | object | 达人资料。 |
| `data.list[].creator.avatar` | string | 头像 URL。 |
| `data.list[].creator.creator_category` | object | 达人类目。 |
| `data.list[].creator.creator_category.id` | integer | ID。 |
| `data.list[].creator.creator_category.name` | string | 名称。 |
| `data.list[].creator.follower_count` | integer | 粉丝数。 |
| `data.list[].creator.nickname` | string | 昵称。 |
| `data.list[].creator.region` | string | 国家或地区代码。 |
| `data.list[].creator.uid` | string | 达人 UID。 |
| `data.list[].creator.unique_id` | string | 达人唯一用户名。 |
| `data.list[].creator.video_count_total` | integer | 视频总数。 |
| `data.list[].potential_metrics` | object | 潜力指标。 |
| `data.list[].potential_metrics.avg_play_count` | integer | 数量。 |
| `data.list[].potential_metrics.currency` | string | 币种。 |
| `data.list[].potential_metrics.ecommerce_type_code` | integer | 编码。 |
| `data.list[].potential_metrics.ecommerce_type_label` | string | 电商类型展示文案。 |
| `data.list[].potential_metrics.gmv` | integer | 成交总额 GMV。 |
| `data.list[].potential_metrics.live_units_sold` | integer | 直播销量。 |
| `data.list[].potential_metrics.period_video_count` | integer | 数量。 |
| `data.list[].potential_metrics.potential_score` | integer | 潜力分。 |
| `data.list[].potential_metrics.sales_category_l3` | array | 销售三级类目。 |
| `data.list[].potential_metrics.sales_category_l3[].category_id` | integer | 类目 ID。 |
| `data.list[].potential_metrics.sales_category_l3[].category_name` | string | 类目名称。 |
| `data.list[].potential_metrics.units_sold` | integer | 销量。 |
| `data.list[].potential_metrics.video_units_sold` | integer | 视频销量。 |
| `data.normalized_period_key` | string | 归一化周期键。 |
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
    "date_info" : {
      "type" : "month",
      "value" : "2026-03"
    },
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "creator_category_id" : 4,
    "follower_count_range" : {
      "max" : 1000000,
      "min" : 500000
    },
    "product_category_l1_id" : 14
  },
  "orderby" : [ {
    "field" : "potential_index",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/creator-rank-top-potential" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/creator-rank-top-potential" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "date_info" : {
      "type" : "month",
      "value" : "2026-03"
    },
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "creator_category_id" : 4,
    "follower_count_range" : {
      "max" : 1000000,
      "min" : 500000
    },
    "product_category_l1_id" : 14
  },
  "orderby" : [ {
    "field" : "potential_index",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

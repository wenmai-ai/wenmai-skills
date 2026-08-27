# FastMoss `shop_rank_top_selling` API 参考

### shop_rank_top_selling

查看热销店铺排行榜

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-rank-top-selling` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤参数。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.date_type` | string | 是 | 统计周期类型。可选值：day（按日）、week（按周）、month（按月）。 |
| `filter.date_value` | string | 是 | 统计周期值。 |
| `filter.is_cross_border` | boolean | 否 | 是否跨境 1是，0否。 |
| `filter.region` | string | 否 | 国家/地区。region 范围: ['US','GB','MX','ES','DE','IT','FR','ID','VN','MY','TH','PH','BR','JP','SG']。 |
| `filter.shop_type` | integer | 否 | 店铺类型 1品牌店，2零售店。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：units_sold（销量）、usd_gmv（美元 GMV）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码，默认值：1。page * pagesize <= 500。 |
| `pagesize` | integer | 否 | 每页条数，默认值：10。page * pagesize <= 500。pagesize 范围 [1, 100]。 |
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
| `data.list` | array | 结果列表。 |
| `data.list[].ranking_metrics` | object | 榜单指标。 |
| `data.list[].ranking_metrics.gmv_growth_rate_percent` | number | 百分比。 |
| `data.list[].ranking_metrics.linked_creator_count` | integer | 关联达人数。 |
| `data.list[].ranking_metrics.period_gmv` | number | GMV。 |
| `data.list[].ranking_metrics.period_units_sold` | integer | 销量。 |
| `data.list[].ranking_metrics.products_with_sales_count` | integer | 产生销量的商品数。 |
| `data.list[].ranking_metrics.units_sold_growth_rate_percent` | number | 百分比。 |
| `data.list[].ranking_scope` | object | 榜单范围。 |
| `data.list[].ranking_scope.ranked_category_id` | integer | ID。 |
| `data.list[].ranking_scope.ranked_category_name` | string | 名称。 |
| `data.list[].shop` | object | 店铺资料。 |
| `data.list[].shop.active_product_count_total` | integer | 在售商品总数。 |
| `data.list[].shop.avatar_url` | string | 头像 URL。 |
| `data.list[].shop.brand_name` | string | 品牌名称。 |
| `data.list[].shop.company_name` | string | 名称。 |
| `data.list[].shop.currency_code` | string | 币种代码。 |
| `data.list[].shop.is_cross_border` | boolean | 是否为跨境店铺或商品。 |
| `data.list[].shop.is_fully_managed` | boolean | 是否为全托管模式。 |
| `data.list[].shop.main_category` | object | 主营类目。 |
| `data.list[].shop.main_category.category_id` | integer | 类目 ID。 |
| `data.list[].shop.main_category.category_name` | string | 类目名称。 |
| `data.list[].shop.region` | string | 国家或地区代码。 |
| `data.list[].shop.seller_id` | string | 店铺卖家 ID。 |
| `data.list[].shop.shop_name` | string | 店铺名称。 |
| `data.list[].shop.shop_rating` | number | 店铺评分。 |
| `data.list[].shop.shop_status_code` | integer | 编码。 |
| `data.list[].shop.shop_status_label` | string | 店铺状态展示文案。 |
| `data.list[].shop.shop_type_code` | string | 店铺类型编码。 |
| `data.ranking_context` | object | 榜单上下文。 |
| `data.ranking_context.date_type` | string | 日期粒度。 |
| `data.ranking_context.date_value` | string | 日期值。 |
| `data.ranking_context.normalized_period_key` | string | 归一化周期键。 |
| `data.ranking_context.total` | integer | 符合条件的记录总数。 |

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
      "type" : "day",
      "value" : "2026-04-01"
    },
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "category_id" : 14
  },
  "orderby" : [ {
    "field" : "units_sold",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/shop-rank-top-selling" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-rank-top-selling" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "date_info" : {
      "type" : "day",
      "value" : "2026-04-01"
    },
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "category_id" : 14
  },
  "orderby" : [ {
    "field" : "units_sold",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

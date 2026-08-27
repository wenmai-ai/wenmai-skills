# FastMoss `market_category_ranking` API 参考

### market_category_ranking

查看类目排名

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/market-category-ranking` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 筛选条件。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.date_type` | string | 否 | 统计周期类型。 |
| `filter.date_value` | string | 否 | 统计周期值。 |
| `filter.region` | string | 否 | 国家或地区代码。 |
| `lang` | string | 否 | 返回语言。 |
| `orderby` | array | 否 | 排序规则。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：category_units_sold（类目销量）、category_units_sold_yoy_percent（类目销量同比增长率）、category_gmv_yoy_percent（类目 GMV 同比增长率）、top_50_products_units_sold_share_percent（销量前 50 商品占比百分比）、top_10_shops_units_sold_share_percent（销量前 10 店铺占比百分比）。 |
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
| `data.ranked_categories` | array | 类目榜单 |
| `data.ranked_categories[].category_gmv_yoy_percent` | number | 百分比。 |
| `data.ranked_categories[].category_id` | integer | 类目 ID。 |
| `data.ranked_categories[].category_level` | integer | 类目层级。 |
| `data.ranked_categories[].category_name` | string | 类目名称。 |
| `data.ranked_categories[].category_units_sold` | integer | 销量。 |
| `data.ranked_categories[].category_units_sold_yoy_percent` | number | 百分比。 |
| `data.ranked_categories[].channel_gmv_share` | object | GMV。 |
| `data.ranked_categories[].channel_gmv_share.live_gmv_share_change_percent` | number | 百分比。 |
| `data.ranked_categories[].channel_gmv_share.live_gmv_share_percent` | number | 百分比。 |
| `data.ranked_categories[].channel_gmv_share.other_gmv_share_change_percent` | number | 百分比。 |
| `data.ranked_categories[].channel_gmv_share.other_gmv_share_percent` | number | 百分比。 |
| `data.ranked_categories[].channel_gmv_share.video_gmv_share_change_percent` | number | 百分比。 |
| `data.ranked_categories[].channel_gmv_share.video_gmv_share_percent` | number | 百分比。 |
| `data.ranked_categories[].rank` | integer | 排名。 |
| `data.ranked_categories[].region` | string | 国家或地区代码。 |
| `data.ranked_categories[].top_10_shops_units_sold_share_percent` | number | 百分比。 |
| `data.ranked_categories[].top_50_products_units_sold_share_percent` | number | 百分比。 |
| `data.ranking_scope` | object | 榜单范围与统计周期 |
| `data.ranking_scope.parent_category_id` | integer | ID。 |
| `data.ranking_scope.parent_category_name` | string | 名称。 |
| `data.ranking_scope.ranked_category_level` | integer | 上榜类目层级。 |
| `data.ranking_scope.region` | string | 国家或地区代码。 |
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
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "category_id" : 14
  },
  "orderby" : [ {
    "field" : "category_units_sold",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/market-category-ranking" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/market-category-ranking" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "category_id" : 14
  },
  "orderby" : [ {
    "field" : "category_units_sold",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

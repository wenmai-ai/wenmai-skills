# FastMoss `agency_shop_analysis` API 参考

### agency_shop_analysis

查看机构合作的店铺表现

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/agency-shop-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.agency_id` | string | 是 | MCN 机构 ID。 |
| `filter.product_category_id` | integer | 否 | 商品类目 ID。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、28（近 28 天）、90（近 90 天）。默认值：28。 |
| `orderby` | array | 否 | 排序规则。 |
| `orderby[].field` | string | 是 | 排序或统计字段。可选值：collaborating_product_count（合作商品数）、agency_collaboration_units_sold（机构合作销量）、agency_collaboration_gmv（机构合作 GMV）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码。默认值：1。最小值：1。最大值：500。 |
| `pagesize` | integer | 否 | 每页条数。默认值：10。最小值：1。最大值：10。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.agency` | object | 机构资料。 |
| `data.agency.agency_id` | string | 机构唯一标识。 |
| `data.analysis_period` | object | 分析周期。 |
| `data.analysis_period.time_range_days` | integer | 统计时间范围，单位为天。 |
| `data.applied_filters` | object | 实际生效的筛选条件。 |
| `data.applied_filters.product_category_id` | null | null |
| `data.collaborating_shops` | array | 合作店铺列表。 |
| `data.collaborating_shops[].agency_collaboration_performance` | object | 机构合作表现。 |
| `data.collaborating_shops[].agency_collaboration_performance.collaborating_product_count` | integer | 合作商品数量。 |
| `data.collaborating_shops[].agency_collaboration_performance.collaboration_gmv` | number | 机构合作成交总额。 |
| `data.collaborating_shops[].agency_collaboration_performance.collaboration_units_sold` | integer | 机构合作销售件数。 |
| `data.collaborating_shops[].agency_collaboration_performance.time_range_days` | integer | 本条数据对应的统计天数。 |
| `data.collaborating_shops[].shop` | object | 店铺资料。 |
| `data.collaborating_shops[].shop.avatar_url` | string | 店铺头像地址。 |
| `data.collaborating_shops[].shop.cumulative_gmv` | number | 店铺累计成交总额。 |
| `data.collaborating_shops[].shop.cumulative_units_sold` | integer | 店铺累计销售件数。 |
| `data.collaborating_shops[].shop.currency_code` | string | 成交金额使用的货币代码。 |
| `data.collaborating_shops[].shop.primary_product_category_id` | integer | 店铺主营商品类目编号。 |
| `data.collaborating_shops[].shop.primary_product_category_name` | string | 店铺主营商品类目名称。 |
| `data.collaborating_shops[].shop.region` | string | 店铺所属国家或地区代码。 |
| `data.collaborating_shops[].shop.shop_id` | string | 店铺唯一标识。 |
| `data.collaborating_shops[].shop.shop_name` | string | 店铺名称。 |
| `data.collaborating_shops[].top_selling_products` | array | 热销商品列表。 |
| `data.collaborating_shops[].top_selling_products[].agency_collaboration_units_sold` | integer | 该商品在机构合作范围内的销售件数。 |
| `data.collaborating_shops[].top_selling_products[].cover_url` | string | 商品封面地址。 |
| `data.collaborating_shops[].top_selling_products[].performance_rank` | integer | 商品在该店铺合作商品中的表现排名。 |
| `data.collaborating_shops[].top_selling_products[].product_id` | string | 商品唯一标识。 |
| `data.collaboration_summary` | object | 合作汇总。 |
| `data.collaboration_summary.shops_with_sales_count` | integer | 统计周期内产生销售的合作店铺数量。 |
| `data.collaboration_summary.total_collaborating_shop_count` | integer | 符合筛选条件的合作店铺总数量。 |
| `data.pagination` | object | 分页信息。 |
| `data.pagination.page` | integer | 当前页码。 |
| `data.pagination.page_size` | integer | 当前页返回的店铺数量。 |
| `data.pagination.total_matching_shop_count` | integer | 符合筛选条件的合作店铺总数量。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "agency_id" : "647f81f2fccde42ac22be7fe7bee2c26",
    "time_range_days" : 28
  },
  "orderby" : [ {
    "field" : "collaborating_product_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/agency-shop-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/agency-shop-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "agency_id" : "647f81f2fccde42ac22be7fe7bee2c26",
    "time_range_days" : 28
  },
  "orderby" : [ {
    "field" : "collaborating_product_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

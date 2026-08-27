# FastMoss `product_rank_top_selling` API 参考

### product_rank_top_selling

查看热销爆品排行榜

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-rank-top-selling` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤参数。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.date_type` | string | 是 | 统计周期类型。可选值：day（按日）、week（按周）、month（按月）。 |
| `filter.date_value` | string | 是 | 统计周期值。 |
| `filter.region` | string | 否 | 国家/地区，例如：['US', 'GB', 'MX', 'ES', 'ID', 'VN', 'MY', 'TH', 'PH']。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：period_units_sold（统计周期销量）、period_gmv（统计周期 GMV）、total_units_sold（累计销量）、total_gmv（累计 GMV）、units_sold_growth_rate_percent（销量增长率百分比）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码，默认值：1。page * pagesize <= 500。 |
| `pagesize` | integer | 否 | 每页条数，默认值：10。page * pagesize <= 500。pagesize 范围 [1, 100]。 |
| `filter.date_info` | object | 是 | 日期信息，例如：{'type': 'day', 'value': '2026-02-01'}。 |

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
| `data.list[].category` | object | 类目。 |
| `data.list[].category.l1` | object | 一级类目。 |
| `data.list[].category.l1.id` | integer | ID。 |
| `data.list[].category.l1.name` | string | 名称。 |
| `data.list[].category.l2` | object | 二级类目。 |
| `data.list[].category.l2.id` | integer | ID。 |
| `data.list[].category.l2.name` | string | 名称。 |
| `data.list[].category.l3` | object | 三级类目。 |
| `data.list[].category.l3.id` | integer | ID。 |
| `data.list[].category.l3.name` | string | 名称。 |
| `data.list[].ceiling_price` | number | 最高价。 |
| `data.list[].commission_rate_percent` | integer | 佣金率百分比。 |
| `data.list[].cover_url` | string | 封面 URL。 |
| `data.list[].currency_code` | string | 币种代码。 |
| `data.list[].floor_price` | number | 最低价。 |
| `data.list[].is_off_shelf` | boolean | 是否已下架。 |
| `data.list[].launch_date` | string | 上架日期。 |
| `data.list[].launch_time` | integer | 上架时间戳。 |
| `data.list[].period_gmv` | number | GMV。 |
| `data.list[].period_units_sold` | integer | 销量。 |
| `data.list[].price_display` | string | 价格展示文案。 |
| `data.list[].product_id` | string | 商品 ID。 |
| `data.list[].region` | string | 国家或地区代码。 |
| `data.list[].shop` | object | 店铺资料。 |
| `data.list[].shop.avatar_url` | string | 头像 URL。 |
| `data.list[].shop.is_fully_managed` | boolean | 是否为全托管模式。 |
| `data.list[].shop.shop_id` | string | 店铺 ID。 |
| `data.list[].shop.shop_name` | string | 店铺名称。 |
| `data.list[].shop.total_units_sold` | integer | 累计销量。 |
| `data.list[].title` | string | 标题。 |
| `data.list[].total_gmv` | number | 累计 GMV。 |
| `data.list[].total_units_sold` | integer | 累计销量。 |
| `data.list[].units_sold_growth_rate_percent` | number | 百分比。 |
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
      "type" : "day",
      "value" : "2026-02-01"
    },
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "category_id" : 2
  },
  "orderby" : [ {
    "field" : "gmv",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-rank-top-selling" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-rank-top-selling" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "date_info" : {
      "type" : "day",
      "value" : "2026-02-01"
    },
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "category_id" : 2
  },
  "orderby" : [ {
    "field" : "gmv",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

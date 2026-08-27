# FastMoss `live_products_list` API 参考

### live_products_list

查看直播场次卖了哪些商品

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/live-products-list` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.room_id` | string | 是 | 直播间 ID。 |
| `filter.seller_id` | string | 否 | 店铺卖家 ID。 |
| `lang` | string | 否 | 返回语言。 |
| `orderby` | array | 否 | 排序规则。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：units_sold（销量）、gmv（GMV）。 |
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
| `data.products` | array | 直播间商品列表 |
| `data.products[].category_name_l1` | string | 一级类目名称。 |
| `data.products[].commission_rate_percent` | integer | 佣金率百分比 |
| `data.products[].cover_url` | string | 封面 URL。 |
| `data.products[].currency` | string | 币种。 |
| `data.products[].currency_symbol` | string | 币种符号。 |
| `data.products[].is_off_shelf` | boolean | 是否已下架。 |
| `data.products[].live_gmv` | number | 本场直播 GMV |
| `data.products[].live_units_sold` | integer | 本场直播销量 |
| `data.products[].price` | integer | 价格。 |
| `data.products[].product_id` | string | 商品 ID。 |
| `data.products[].product_source` | string | 商品来源。 |
| `data.products[].region` | string | 国家或地区代码。 |
| `data.products[].sales_timeline` | array | 商品在本场直播中的销售时间线 |
| `data.products[].shop_avatar_url` | string | 店铺头像 URL。 |
| `data.products[].shop_cumulative_units_sold` | integer | 销量。 |
| `data.products[].shop_id` | string | 店铺 ID。 |
| `data.products[].shop_name` | string | 店铺名称。 |
| `data.products[].title` | string | 标题。 |
| `data.total` | integer | 符合条件的记录总数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "room_id" : "7539139975317703438"
  },
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/live-products-list" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/live-products-list" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "room_id" : "7539139975317703438"
  },
  "pagesize" : 10
}'
```

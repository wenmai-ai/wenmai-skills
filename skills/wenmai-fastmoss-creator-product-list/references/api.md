# FastMoss `creator_product_list` API 参考

### creator_product_list

查询达人橱窗里在卖的商品，含销量、GMV、佣金

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/creator-product-list` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 过滤参数。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.time_range_days` | string | 否 | 统计时间范围（天）。 |
| `filter.uid` | string | 是 | 达人 UID。 |
| `orderby` | array | 否 | 排序规则。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：units_sold（销量）、gmv（GMV）、commission_rate_percent（佣金率百分比）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码。默认值：1。最小值：1。最大值：500。 |
| `pagesize` | integer | 否 | 每页条数。默认值：10。最大值：10。 |
| `filter.days` | string | 否 | 时间范围，例如：[0, 7, 14, 28, 90]。 |

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
| `data.list[].category_id_l1` | integer | 一级类目 ID。 |
| `data.list[].category_id_l2` | integer | 二级类目 ID。 |
| `data.list[].category_id_l3` | integer | 三级类目 ID。 |
| `data.list[].category_name_l1` | string | 一级类目名称。 |
| `data.list[].ceiling_price` | number | 最高价。 |
| `data.list[].commission_rate_percent` | integer | 佣金率百分比。 |
| `data.list[].cover` | string | 封面 URL。 |
| `data.list[].creator_uid` | string | 达人 UID。 |
| `data.list[].floor_price` | number | 最低价。 |
| `data.list[].gmv` | integer | 成交总额 GMV。 |
| `data.list[].product_id` | string | 商品 ID。 |
| `data.list[].product_rating` | number | 商品评分。 |
| `data.list[].region` | string | 国家或地区代码。 |
| `data.list[].shop_avatar` | string | 店铺头像 URL。 |
| `data.list[].shop_id` | string | 店铺 ID。 |
| `data.list[].shop_name` | string | 店铺名称。 |
| `data.list[].shop_total_gmv` | number | 店铺累计 GMV。 |
| `data.list[].shop_total_units_sold` | integer | 店铺累计销量。 |
| `data.list[].title` | string | 标题。 |
| `data.list[].units_sold` | integer | 销量。 |
| `data.page` | integer | 当前页码。 |
| `data.time_range_days` | integer | 商品指标统计天数 |
| `data.total` | integer | 符合条件的记录总数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "uid" : "6861118469497553925",
    "days" : 7
  },
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/creator-product-list" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/creator-product-list" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "uid" : "6861118469497553925",
    "days" : 7
  },
  "pagesize" : 10
}'
```

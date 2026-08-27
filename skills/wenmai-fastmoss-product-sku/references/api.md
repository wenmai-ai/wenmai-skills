# FastMoss `product_sku` API 参考

### product_sku

查看商品各 SKU 的销量/库存占比

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-sku` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.product_id` | string | 是 | 商品 ID。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、28（近 28 天）。默认值：7。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.currency_code` | string | 币种代码。 |
| `data.product_id` | string | 商品 ID。 |
| `data.sku_dimensions` | array | SKU 规格维度。 |
| `data.sku_dimensions[].dimension_id` | string | ID。 |
| `data.sku_dimensions[].dimension_name` | string | 名称。 |
| `data.sku_dimensions[].distribution_summary` | object | 分发摘要。 |
| `data.sku_dimensions[].distribution_summary.breakdown` | array | 拆分明细。 |
| `data.sku_dimensions[].distribution_summary.breakdown[].dimension_value` | string | 维度值。 |
| `data.sku_dimensions[].distribution_summary.breakdown[].gmv` | integer | 成交总额 GMV。 |
| `data.sku_dimensions[].distribution_summary.breakdown[].gmv_share_percent` | integer | 百分比。 |
| `data.sku_dimensions[].distribution_summary.breakdown[].stock_share_percent` | integer | 百分比。 |
| `data.sku_dimensions[].distribution_summary.breakdown[].stock_units` | integer | 库存件数。 |
| `data.sku_dimensions[].distribution_summary.breakdown[].units_sold` | integer | 销量。 |
| `data.sku_dimensions[].distribution_summary.breakdown[].units_sold_share_percent` | integer | 百分比。 |
| `data.sku_dimensions[].distribution_summary.total_gmv` | integer | 累计 GMV。 |
| `data.sku_dimensions[].distribution_summary.total_stock_units` | integer | 库存总件数。 |
| `data.sku_dimensions[].distribution_summary.total_units_sold` | integer | 累计销量。 |
| `data.sku_dimensions[].values` | array | 数值列表。 |
| `data.sku_dimensions[].values[].dimension_value` | string | 维度值。 |
| `data.sku_dimensions[].values[].dimension_value_id` | string | ID。 |
| `data.sku_variants` | array | SKU 变体列表。 |
| `data.sku_variants[].currency_code` | string | 币种代码。 |
| `data.sku_variants[].current_price` | integer | 当前价格。 |
| `data.sku_variants[].original_price` | integer | 原价。 |
| `data.sku_variants[].properties` | array | 属性。 |
| `data.sku_variants[].properties[].dimension_id` | string | ID。 |
| `data.sku_variants[].properties[].dimension_name` | string | 名称。 |
| `data.sku_variants[].properties[].dimension_value` | string | 维度值。 |
| `data.sku_variants[].properties[].dimension_value_id` | string | ID。 |
| `data.sku_variants[].sku_id` | string | ID。 |
| `data.sku_variants[].stock_units` | integer | 库存件数。 |
| `data.snapshot_date` | string | 数据快照日期。 |
| `data.time_range_days` | integer | 统计时间范围天数。 |
| `data.top_sku_by_units_sold` | object | 按销量排名靠前的 SKU。 |
| `data.top_sku_by_units_sold.current_price` | integer | 当前价格。 |
| `data.top_sku_by_units_sold.dimension_name` | string | 名称。 |
| `data.top_sku_by_units_sold.dimension_value` | string | 维度值。 |
| `data.top_sku_by_units_sold.gmv` | integer | 成交总额 GMV。 |
| `data.top_sku_by_units_sold.stock_units` | integer | 库存件数。 |
| `data.top_sku_by_units_sold.units_sold` | integer | 销量。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "product_id" : "1733683494177178921",
    "time_range_days" : 28
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-sku" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-sku" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "product_id" : "1733683494177178921",
    "time_range_days" : 28
  }
}'
```

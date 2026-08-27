# FastMoss `product_sales_trend` API 参考

### product_sales_trend

查看商品的销量/GMV 趋势走势

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-sales-trend` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 筛选条件。 |
| `filter.product_id` | string | 是 | 商品 ID。 |
| `filter.time_range_days` | integer | 是 | 统计时间范围（天）。 |
| `filter.days` | integer | 是 | 近 N 天 ：1 <= days <= 28。 |

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
| `data.daily_trend` | array | 商品每日销售趋势 |
| `data.daily_trend[].daily_gmv` | integer | GMV。 |
| `data.daily_trend[].daily_units_sold` | integer | 销量。 |
| `data.daily_trend[].date` | string | 统计日期 |
| `data.period_summary` | object | 商品周期销售汇总 |
| `data.period_summary.linked_creator_count` | integer | 关联达人数。 |
| `data.period_summary.linked_live_count` | integer | 关联直播数。 |
| `data.period_summary.linked_video_count` | integer | 关联视频数。 |
| `data.period_summary.period_gmv` | number | 周期 GMV |
| `data.period_summary.period_units_sold` | integer | 周期销量 |
| `data.region` | string | 国家或地区代码。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "days" : 7,
    "product_id" : "1733683494177178921",
    "time_range_days" : 28
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-sales-trend" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-sales-trend" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "days" : 7,
    "product_id" : "1733683494177178921",
    "time_range_days" : 28
  }
}'
```

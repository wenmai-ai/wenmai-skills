# FastMoss `product_investment` API 参考

### product_investment

查看商品的广告投放与 ROAS 表现

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-investment` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 过滤参数。 |
| `filter.product_id` | string | 是 | 商品 ID。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。 |
| `orderby` | array | 否 | 排序参数。 |
| `page` | integer | 否 | 页码，默认值：1。page * pagesize <= 500。 |
| `pagesize` | integer | 否 | 每页条数，默认值：10。page * pagesize <= 500。pagesize 范围 [1, 100]。 |
| `filter.region` | string | 否 | 国家/地区。 |
| `filter.date_info` | object | 是 | 日期信息，例如：{'type': 'day', 'value': '2026-02-01'}。 |
| `filter.category_id` | integer | 否 | 商品分类。 |
| `filter.is_cross_border` | integer | 否 | 是否是跨境商品。 |
| `filter.is_fully_managed` | integer | 否 | 是否是全托管商品。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.ad_performance_summary` | object | 商品广告投放汇总；GMV 为广告归因 GMV |
| `data.ad_performance_summary.ad_gmv` | number | GMV。 |
| `data.ad_performance_summary.ad_gmv_share_percent` | number | 百分比。 |
| `data.ad_performance_summary.ad_play_count` | integer | 数量。 |
| `data.ad_performance_summary.ad_units_sold` | integer | 销量。 |
| `data.ad_performance_summary.ad_video_count` | integer | 数量。 |
| `data.ad_performance_summary.avg_daily_ad_gmv` | number | GMV。 |
| `data.ad_performance_summary.avg_daily_ad_play_count` | number | 数量。 |
| `data.ad_performance_summary.avg_daily_ad_units_sold` | number | 销量。 |
| `data.ad_performance_summary.avg_daily_estimated_ad_spend` | number | 日均预估广告花费。 |
| `data.ad_performance_summary.estimated_ad_spend` | number | 预估广告花费。 |
| `data.ad_performance_summary.product_total_gmv` | number | GMV。 |
| `data.ad_performance_summary.roas` | number | 广告回报率 ROAS。 |
| `data.currency_code` | string | 币种代码。 |
| `data.daily_ad_performance_trend` | array | 商品每日广告投放趋势 |
| `data.daily_ad_performance_trend[].ad_gmv` | integer | GMV。 |
| `data.daily_ad_performance_trend[].ad_play_count` | integer | 数量。 |
| `data.daily_ad_performance_trend[].ad_units_sold` | integer | 销量。 |
| `data.daily_ad_performance_trend[].ad_video_count` | integer | 数量。 |
| `data.daily_ad_performance_trend[].date` | string | 日期。 |
| `data.daily_ad_performance_trend[].estimated_ad_spend` | number | 预估广告花费。 |
| `data.daily_ad_performance_trend[].roas` | number | 广告回报率 ROAS。 |

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
    "product_id" : "1733683494177178921",
    "category_id" : 2
  },
  "orderby" : [ {
    "field" : "affiliate_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-investment" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-investment" \
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
    "product_id" : "1733683494177178921",
    "category_id" : 2
  },
  "orderby" : [ {
    "field" : "affiliate_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

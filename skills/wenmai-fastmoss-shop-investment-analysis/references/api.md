# FastMoss `shop_investment_analysis` API 参考

### shop_investment_analysis

查看店铺的广告投放表现

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-investment-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 过滤参数。 |
| `filter.end_date` | string | 否 | 结束日期。 |
| `filter.seller_id` | string | 是 | 店铺卖家 ID。 |
| `filter.start_date` | string | 否 | 开始日期。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、14（近 14 天）、28（近 28 天）、60（近 60 天）、90（近 90 天）、180（近 180 天）。 |
| `orderby` | array | 否 | 排序参数。 |
| `page` | integer | 否 | 页码，默认值：1。page * pagesize <= 500。 |
| `pagesize` | integer | 否 | 每页条数，默认值：10。page * pagesize <= 500。pagesize 范围 [1, 100]。 |
| `filter.region` | string | 否 | 国家/地区。region 范围: ['US','GB','MX','ES','DE','IT','FR','ID','VN','MY','TH','PH','BR','JP','SG']。 |
| `filter.category_id` | integer | 否 | 商品分类。 |
| `filter.shop_type` | integer | 否 | 店铺类型 1品牌店，2零售店。 |
| `filter.is_cross_border` | integer | 否 | 是否跨境 1是，0否。 |
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
| `data.ad_performance_summary` | object | 店铺广告消耗、ROAS 与广告归因 GMV 汇总 |
| `data.ad_performance_summary.ad_attributed_gmv` | integer | GMV。 |
| `data.ad_performance_summary.end_date` | string | 结束日期。 |
| `data.ad_performance_summary.estimated_ad_spend` | integer | 预估广告花费。 |
| `data.ad_performance_summary.promoted_creator_count` | integer | 数量。 |
| `data.ad_performance_summary.promoted_product_count` | integer | 数量。 |
| `data.ad_performance_summary.promoted_video_count` | integer | 数量。 |
| `data.ad_performance_summary.roas` | integer | 广告回报率 ROAS。 |
| `data.ad_performance_summary.start_date` | string | 开始日期。 |
| `data.ad_performance_summary.time_granularity` | string | 时间粒度。 |
| `data.daily_ad_performance_trend` | array | 店铺每日广告投放趋势 |
| `data.daily_ad_performance_trend[].ad_attributed_gmv` | integer | GMV。 |
| `data.daily_ad_performance_trend[].date` | string | 日期。 |
| `data.daily_ad_performance_trend[].estimated_ad_spend` | integer | 预估广告花费。 |
| `data.daily_ad_performance_trend[].promoted_creator_count` | integer | 数量。 |
| `data.daily_ad_performance_trend[].promoted_product_count` | integer | 数量。 |
| `data.daily_ad_performance_trend[].promoted_video_count` | integer | 数量。 |
| `data.daily_ad_performance_trend[].roas` | integer | 广告回报率 ROAS。 |
| `data.shop` | object | 店铺资料 |
| `data.shop.currency_code` | string | 币种代码。 |
| `data.shop.seller_id` | string | 店铺卖家 ID |

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
    "seller_id" : "7496313543931234624",
    "category_id" : 14,
    "time_range_days" : 28
  },
  "orderby" : [ {
    "field" : "affiliate_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/shop-investment-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-investment-analysis" \
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
    "seller_id" : "7496313543931234624",
    "category_id" : 14,
    "time_range_days" : 28
  },
  "orderby" : [ {
    "field" : "affiliate_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

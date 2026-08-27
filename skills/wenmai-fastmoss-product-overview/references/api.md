# FastMoss `product_overview` API 参考

### product_overview

查看商品成交来源与整体数据总览

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-overview` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.end_date` | string | 否 | 结束日期。 |
| `filter.product_id` | string | 是 | 商品 ID。 |
| `filter.start_date` | string | 否 | 开始日期。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.ads_distribution` | object | 广告与自然流量分布 |
| `data.ads_distribution.breakdown` | array | 拆分明细。 |
| `data.ads_distribution.breakdown[].gmv` | number | 成交总额 GMV。 |
| `data.ads_distribution.breakdown[].gmv_share_percent` | integer | 百分比。 |
| `data.ads_distribution.breakdown[].traffic_source` | string | 流量来源。 |
| `data.ads_distribution.breakdown[].units_sold` | integer | 销量。 |
| `data.ads_distribution.breakdown[].units_sold_share_percent` | integer | 百分比。 |
| `data.ads_distribution.total_gmv` | number | 累计 GMV。 |
| `data.ads_distribution.total_units_sold` | integer | 累计销量。 |
| `data.channel_distribution` | object | 成交渠道分布 |
| `data.channel_distribution.breakdown` | array | 拆分明细。 |
| `data.channel_distribution.breakdown[].gmv` | number | 成交总额 GMV。 |
| `data.channel_distribution.breakdown[].gmv_share_percent` | integer | 百分比。 |
| `data.channel_distribution.breakdown[].sales_channel` | string | 销售渠道。 |
| `data.channel_distribution.breakdown[].units_sold` | integer | 销量。 |
| `data.channel_distribution.breakdown[].units_sold_share_percent` | integer | 百分比。 |
| `data.channel_distribution.total_gmv` | number | 累计 GMV。 |
| `data.channel_distribution.total_units_sold` | integer | 累计销量。 |
| `data.content_distribution` | object | 内容类型成交分布 |
| `data.content_distribution.breakdown` | array | 拆分明细。 |
| `data.content_distribution.breakdown[].content_type` | string | 内容类型。 |
| `data.content_distribution.breakdown[].gmv` | number | 成交总额 GMV。 |
| `data.content_distribution.breakdown[].gmv_share_percent` | integer | 百分比。 |
| `data.content_distribution.breakdown[].units_sold` | integer | 销量。 |
| `data.content_distribution.breakdown[].units_sold_share_percent` | integer | 百分比。 |
| `data.content_distribution.total_gmv` | number | 累计 GMV。 |
| `data.content_distribution.total_units_sold` | integer | 累计销量。 |
| `data.currency_code` | string | 币种代码。 |
| `data.daily_trend` | array | 商品每日销售趋势 |
| `data.daily_trend[].average_order_value` | integer | 客单价。 |
| `data.daily_trend[].cumulative_gmv` | number | GMV。 |
| `data.daily_trend[].cumulative_linked_creator_count` | integer | 数量。 |
| `data.daily_trend[].cumulative_linked_live_count` | integer | 数量。 |
| `data.daily_trend[].cumulative_linked_video_count` | integer | 数量。 |
| `data.daily_trend[].cumulative_units_sold` | integer | 销量。 |
| `data.daily_trend[].daily_gmv` | integer | GMV。 |
| `data.daily_trend[].daily_new_linked_creator_count` | integer | 数量。 |
| `data.daily_trend[].daily_new_linked_live_count` | integer | 数量。 |
| `data.daily_trend[].daily_new_linked_video_count` | integer | 数量。 |
| `data.daily_trend[].daily_units_sold` | integer | 销量。 |
| `data.daily_trend[].date` | string | 统计日期 |
| `data.period_summary` | object | 商品周期销售汇总 |
| `data.period_summary.avg_daily_gmv` | integer | GMV。 |
| `data.period_summary.avg_daily_units_sold` | integer | 销量。 |
| `data.period_summary.current_price` | number | 当前价格。 |
| `data.period_summary.linked_creator_count` | integer | 关联达人数。 |
| `data.period_summary.linked_live_count` | integer | 关联直播数。 |
| `data.period_summary.linked_video_count` | integer | 关联视频数。 |
| `data.period_summary.live_gmv` | number | 直播 GMV。 |
| `data.period_summary.live_units_sold` | integer | 直播销量。 |
| `data.period_summary.period_total_gmv` | number | GMV。 |
| `data.period_summary.period_total_units_sold` | integer | 销量。 |
| `data.period_summary.video_gmv` | number | 视频 GMV。 |
| `data.period_summary.video_units_sold` | integer | 视频销量。 |
| `data.product_id` | string | 商品 ID。 |
| `data.region` | string | 国家或地区代码。 |
| `data.title` | string | 标题。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "product_id" : "1733683494177178921"
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-overview" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-overview" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "product_id" : "1733683494177178921"
  }
}'
```

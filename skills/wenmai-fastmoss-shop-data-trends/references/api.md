# FastMoss `shop_data_trends` API 参考

### shop_data_trends

查看店铺销量/GMV 走势

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-data-trends` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.end_date` | string | 否 | 结束日期。 |
| `filter.seller_id` | string | 是 | 店铺卖家 ID。 |
| `filter.start_date` | string | 否 | 开始日期。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、28（近 28 天）、90（近 90 天）。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.daily_trend` | array | 店铺每日 GMV、销量、达人、直播、视频和在售商品趋势 |
| `data.daily_trend[].cumulative_gmv` | number | GMV。 |
| `data.daily_trend[].cumulative_linked_creator_count` | integer | 数量。 |
| `data.daily_trend[].cumulative_linked_live_count` | integer | 数量。 |
| `data.daily_trend[].cumulative_linked_video_count` | integer | 数量。 |
| `data.daily_trend[].cumulative_units_sold` | integer | 销量。 |
| `data.daily_trend[].daily_active_product_count` | integer | 数量。 |
| `data.daily_trend[].daily_gmv` | number | GMV。 |
| `data.daily_trend[].daily_new_linked_creator_count` | integer | 数量。 |
| `data.daily_trend[].daily_new_linked_live_count` | integer | 数量。 |
| `data.daily_trend[].daily_new_linked_video_count` | integer | 数量。 |
| `data.daily_trend[].daily_units_sold` | integer | 销量。 |
| `data.daily_trend[].date` | string | 统计日期 |
| `data.query_summary` | object | 查询条件摘要。 |
| `data.query_summary.end_date` | string | 结束日期。 |
| `data.query_summary.period_active_product_count` | integer | 数量。 |
| `data.query_summary.period_gmv` | number | GMV。 |
| `data.query_summary.period_new_linked_creator_count` | integer | 数量。 |
| `data.query_summary.period_new_linked_live_count` | integer | 数量。 |
| `data.query_summary.period_new_linked_video_count` | integer | 数量。 |
| `data.query_summary.period_units_sold` | integer | 销量。 |
| `data.query_summary.start_date` | string | 开始日期。 |
| `data.query_summary.time_granularity` | string | 时间粒度。 |
| `data.shop` | object | 店铺资料 |
| `data.shop.currency_code` | string | 币种代码。 |
| `data.shop.region` | string | 店铺所属国家或地区代码 |
| `data.shop.seller_id` | string | 店铺卖家 ID |
| `data.shop.shop_name` | string | 店铺名称 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/shop-data-trends" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-data-trends" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28
  }
}'
```

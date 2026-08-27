# FastMoss `market_category_analysis` API 参考

### market_category_analysis

分析类目规模、成长性与竞争度

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/market-category-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `analysis_type` | string | 是 | 分析类型。可选值：basic_metrics（基础规模与竞争指标）、sales_trends（销售趋势）、price_distribution（价格带分布）。 |
| `filter` | object | 是 | 筛选条件。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.date_type` | string | 否 | 统计周期类型。 |
| `filter.date_value` | string | 否 | 统计周期值。 |
| `filter.region` | string | 否 | 国家或地区代码。 |
| `lang` | string | 否 | 返回语言。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.analysis_type` | string | 实际返回的分析类型 |
| `data.category` | object | 目标类目资料 |
| `data.category.category_id` | integer | 类目 ID。 |
| `data.category.category_level` | integer | 类目层级。 |
| `data.category.category_name` | string | 类目名称。 |
| `data.category.region` | string | 国家或地区代码。 |
| `data.category.stat_date` | string | 时间。 |
| `data.concentration_metrics` | object | 类目集中度与竞争指标 |
| `data.concentration_metrics.top_products_gmv_share` | integer | GMV。 |
| `data.concentration_metrics.top_shops_gmv_share` | integer | GMV。 |
| `data.growth_metrics` | object | 类目增长指标 |
| `data.growth_metrics.active_product_count_change` | integer | 在售商品数变化。 |
| `data.growth_metrics.category_gmv_mom_percent` | integer | 百分比。 |
| `data.growth_metrics.category_gmv_yoy_percent` | number | 百分比。 |
| `data.growth_metrics.category_units_sold_mom_percent` | number | 百分比。 |
| `data.growth_metrics.category_units_sold_yoy_percent` | number | 百分比。 |
| `data.growth_metrics.product_count_change` | integer | 商品数变化。 |
| `data.growth_metrics.selling_creator_count_change` | integer | 带货达人数变化。 |
| `data.growth_metrics.selling_live_count_change` | integer | 带货直播数变化。 |
| `data.growth_metrics.selling_video_count_change` | integer | 带货视频数变化。 |
| `data.scale_metrics` | object | 类目规模指标 |
| `data.scale_metrics.active_product_count` | integer | 在售商品数。 |
| `data.scale_metrics.category_gmv` | number | GMV。 |
| `data.scale_metrics.category_units_sold` | integer | 销量。 |
| `data.scale_metrics.product_count` | integer | 商品数。 |
| `data.scale_metrics.selling_creator_count` | integer | 数量。 |
| `data.scale_metrics.selling_live_count` | integer | 数量。 |
| `data.scale_metrics.selling_video_count` | integer | 数量。 |
| `data.top_products_summary` | object | 头部商品摘要。 |
| `data.top_products_summary.average_affiliate_count` | integer | 数量。 |
| `data.top_products_summary.average_live_count` | integer | 数量。 |
| `data.top_products_summary.average_video_count` | integer | 数量。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "region" : "US",
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "category_id" : 14
  },
  "analysis_type" : "basic_metrics"
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/market-category-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/market-category-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "region" : "US",
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "category_id" : 14
  },
  "analysis_type" : "basic_metrics"
}'
```

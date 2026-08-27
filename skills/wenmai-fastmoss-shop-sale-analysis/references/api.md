# FastMoss `shop_sale_analysis` API 参考

### shop_sale_analysis

分析店铺的成交结构（短视频/直播/商品卡）

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-sale-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.seller_id` | string | 是 | 店铺卖家 ID。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、28（近 28 天）、90（近 90 天）。默认值：28。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.content_type_distribution` | object | 内容类型分布。 |
| `data.content_type_distribution.by_gmv` | array | GMV。 |
| `data.content_type_distribution.by_gmv[].content_type_label` | string | 内容类型展示文案。 |
| `data.content_type_distribution.by_gmv[].gmv` | integer | 成交总额 GMV。 |
| `data.content_type_distribution.by_gmv[].gmv_share_percent` | integer | 百分比。 |
| `data.content_type_distribution.by_units_sold` | array | 销量。 |
| `data.content_type_distribution.by_units_sold[].content_type_label` | string | 内容类型展示文案。 |
| `data.content_type_distribution.by_units_sold[].units_sold` | integer | 销量。 |
| `data.content_type_distribution.by_units_sold[].units_sold_share_percent` | integer | 百分比。 |
| `data.sales_channel_distribution` | object | 销售渠道分布。 |
| `data.sales_channel_distribution.by_gmv` | array | GMV。 |
| `data.sales_channel_distribution.by_gmv[].gmv` | number | 成交总额 GMV。 |
| `data.sales_channel_distribution.by_gmv[].gmv_share_percent` | integer | 百分比。 |
| `data.sales_channel_distribution.by_gmv[].sales_channel_label` | string | 销售渠道展示文案。 |
| `data.sales_channel_distribution.by_units_sold` | array | 销量。 |
| `data.sales_channel_distribution.by_units_sold[].sales_channel_label` | string | 销售渠道展示文案。 |
| `data.sales_channel_distribution.by_units_sold[].units_sold` | integer | 销量。 |
| `data.sales_channel_distribution.by_units_sold[].units_sold_share_percent` | integer | 百分比。 |
| `data.shop` | object | 店铺资料 |
| `data.shop.region` | string | 店铺所属国家或地区代码 |
| `data.shop.seller_id` | string | 店铺卖家 ID |
| `data.shop.time_range_days` | integer | 统计时间范围天数。 |

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
  -Uri "$BASE_URL/fastmoss/shop-sale-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-sale-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28
  }
}'
```

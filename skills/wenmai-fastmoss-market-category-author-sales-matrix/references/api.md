# FastMoss `market_category_author_sales_matrix` API 参考

### market_category_author_sales_matrix

分析不同粉丝量级达人在该类目的贡献

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/market-category-author-sales-matrix` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 筛选条件。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.date_value` | string | 否 | 统计周期值。 |
| `filter.region` | string | 否 | 国家或地区代码。 |
| `filter.sold_type` | integer | 否 | 销量口径。 |
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
| `data.list` | array | 结果列表。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "region" : "US",
    "date_value" : "2026-08-25",
    "category_id" : 14
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/market-category-author-sales-matrix" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/market-category-author-sales-matrix" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "region" : "US",
    "date_value" : "2026-08-25",
    "category_id" : 14
  }
}'
```

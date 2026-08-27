# FastMoss `product_review_list` API 参考

### product_review_list

查看商品的顾客评论

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-review-list` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤参数。 |
| `filter.product_id` | string | 是 | 商品 ID。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：rating（评分）、create_time（创建时间）、review_id（评论 ID）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码。默认值：1。最小值：1。最大值：500。 |
| `pagesize` | integer | 否 | 每页条数。默认值：10。最大值：10。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.reviews` | array | 商品评论列表 |
| `data.reviews[].like_count` | integer | 点赞数。 |
| `data.reviews[].rating` | integer | 评分 |
| `data.reviews[].review_date` | string | 时间。 |
| `data.reviews[].review_id` | string | 评论 ID |
| `data.reviews[].review_text` | string | 评论文本。 |
| `data.reviews[].review_timestamp_ms` | integer | 评论时间戳（毫秒）。 |
| `data.reviews[].sku_id` | string | ID。 |
| `data.reviews[].sku_variant_text` | string | SKU 规格文案。 |
| `data.total_review_count` | integer | 评论总数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "product_id" : "1733683494177178921"
  },
  "orderby" : {
    "field" : "rating",
    "order" : "desc"
  },
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-review-list" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-review-list" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "product_id" : "1733683494177178921"
  },
  "orderby" : {
    "field" : "rating",
    "order" : "desc"
  },
  "pagesize" : 10
}'
```

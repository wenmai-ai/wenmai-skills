# FastMoss `product_category_info` API 参考

### product_category_info

查询商品分类树状结构

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-category-info` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `lang` | string | 否 | 语言设置，英语(默认值)：EN_US 中文：ZH_CN。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.[]` | array | 列表。 |
| `data.[].c_code` | string | 类目编码。 |
| `data.[].c_name` | string | 类目名称。 |
| `data.[].sub` | array | 子类目列表。 |
| `data.[].sub[].c_code` | string | 类目编码。 |
| `data.[].sub[].c_name` | string | 类目名称。 |
| `data.[].sub[].sub` | array | 子类目列表。 |
| `data.[].sub[].sub[].c_code` | string | 类目编码。 |
| `data.[].sub[].sub[].c_name` | string | 类目名称。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "lang" : "EN_US"
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-category-info" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-category-info" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "lang" : "EN_US"
}'
```

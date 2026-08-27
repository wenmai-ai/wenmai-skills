# FastMoss `creator_fans_distribution` API 参考

### creator_fans_distribution

分析达人的粉丝轮廓（年龄/性别/地区）

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/creator-fans-distribution` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.uid` | string | 是 | 达人 UID。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.age_distribution` | array | 粉丝年龄分布 |
| `data.audience_geo_level` | string | 受众地理层级。 |
| `data.gender_distribution` | array | 粉丝性别分布 |
| `data.location_distribution` | array | 粉丝地区分布 |
| `data.top_age_group` | object | 主要年龄段。 |
| `data.top_age_group.age_range` | string | 年龄区间。 |
| `data.top_age_group.percentage` | integer | 占比。 |
| `data.top_gender` | object | 主要性别。 |
| `data.top_gender.gender` | string | 性别。 |
| `data.top_gender.percentage` | integer | 占比。 |
| `data.top_location` | object | 主要地域。 |
| `data.top_location.location_name` | string | 名称。 |
| `data.top_location.percentage` | integer | 占比。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "uid" : "6861118469497553925"
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/creator-fans-distribution" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/creator-fans-distribution" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "uid" : "6861118469497553925"
  }
}'
```

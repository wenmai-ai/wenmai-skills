# FastMoss `creator_cargo_summary` API 参考

### creator_cargo_summary

查看达人视频 vs 直播带货的占比

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/creator-cargo-summary` |
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
| `data.avg_gmv_per_live` | number | 场均直播 GMV。 |
| `data.avg_gmv_per_video` | number | 视频平均 GMV。 |
| `data.avg_units_sold_per_live` | integer | 场均直播销量。 |
| `data.avg_units_sold_per_video` | integer | 视频平均销量。 |
| `data.category_product_share_list` | array | 类目商品占比列表。 |
| `data.category_product_share_list[].category_id` | string | 类目 ID。 |
| `data.category_product_share_list[].category_name` | string | 类目名称。 |
| `data.category_product_share_list[].share_percent` | integer | 百分比。 |
| `data.category_product_share_list[].share_text` | string | 占比展示文案。 |
| `data.category_units_sold_share_list` | array | 类目销量占比列表。 |
| `data.category_units_sold_share_list[].category_id` | string | 类目 ID。 |
| `data.category_units_sold_share_list[].category_name` | string | 类目名称。 |
| `data.category_units_sold_share_list[].share_percent` | number | 百分比。 |
| `data.category_units_sold_share_list[].share_text` | string | 占比展示文案。 |
| `data.currency` | string | 币种。 |
| `data.gmv_distribution` | object | GMV 分布。 |
| `data.gmv_distribution.live_share_percent` | number | 百分比。 |
| `data.gmv_distribution.video_share_percent` | number | 百分比。 |
| `data.live_gmv` | number | 直播 GMV。 |
| `data.live_units_sold` | integer | 直播销量。 |
| `data.product_count` | integer | 商品数。 |
| `data.product_count_with_live` | integer | 有直播带货的商品数。 |
| `data.product_count_with_video` | integer | 有视频带货的商品数。 |
| `data.region` | string | 国家或地区代码。 |
| `data.shop_count` | integer | 店铺数。 |
| `data.shop_count_with_live` | integer | 有直播带货的店铺数。 |
| `data.shop_count_with_video` | integer | 有视频带货的店铺数。 |
| `data.total_gmv` | number | 累计 GMV。 |
| `data.total_units_sold` | integer | 累计销量。 |
| `data.units_sold_distribution` | object | 销量分布。 |
| `data.units_sold_distribution.live_share_percent` | number | 百分比。 |
| `data.units_sold_distribution.video_share_percent` | number | 百分比。 |
| `data.video_gmv` | number | 视频 GMV。 |
| `data.video_units_sold` | integer | 视频销量。 |

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
  -Uri "$BASE_URL/fastmoss/creator-cargo-summary" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/creator-cargo-summary" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "uid" : "6861118469497553925"
  }
}'
```

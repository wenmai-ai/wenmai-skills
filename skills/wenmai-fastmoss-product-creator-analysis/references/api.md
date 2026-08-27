# FastMoss `product_creator_analysis` API 参考

### product_creator_analysis

查看是哪些达人在卖这个商品

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-creator-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 过滤参数。 |
| `filter.product_id` | string | 是 | 商品 ID。 |
| `orderby` | array | 否 | 排序规则。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：product_gmv（商品 GMV）、product_units_sold（商品销量）、creator_total_like_count（达人累计获赞数）、follower_count（粉丝数）。 |
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
| `data.creator_summary` | object | 带货达人结构汇总 |
| `data.creator_summary.creator_category_distribution` | array | 达人类目分布 |
| `data.creator_summary.creator_category_distribution[].creator_category` | string | 达人类目。 |
| `data.creator_summary.creator_category_distribution[].creator_share_percent` | integer | 百分比。 |
| `data.creator_summary.follower_tier_distribution` | array | 达人粉丝量级分布 |
| `data.creator_summary.follower_tier_distribution[].creator_count` | integer | 数量。 |
| `data.creator_summary.follower_tier_distribution[].follower_tier` | string | 粉丝量级。 |
| `data.linked_creators` | object | 商品关联达人列表 |
| `data.linked_creators.list` | array | 结果列表。 |
| `data.linked_creators.list[].audience_summary` | object | 受众摘要。 |
| `data.linked_creators.list[].audience_summary.age_distribution` | array | 年龄分布。 |
| `data.linked_creators.list[].audience_summary.gender_distribution` | array | 性别分布。 |
| `data.linked_creators.list[].creator` | object | 达人资料。 |
| `data.linked_creators.list[].creator.avatar_url` | string | 头像 URL。 |
| `data.linked_creators.list[].creator.creator_category` | object | 达人类目。 |
| `data.linked_creators.list[].creator.creator_category.id` | integer | ID。 |
| `data.linked_creators.list[].creator.creator_category.name` | string | 名称。 |
| `data.linked_creators.list[].creator.creator_handle` | string | 达人唯一用户名。 |
| `data.linked_creators.list[].creator.creator_name` | string | 达人昵称。 |
| `data.linked_creators.list[].creator.creator_uid` | string | 达人 UID。 |
| `data.linked_creators.list[].creator.follower_count` | integer | 粉丝数。 |
| `data.linked_creators.list[].creator.region` | string | 国家或地区代码。 |
| `data.linked_creators.list[].creator_cumulative_performance` | object | 达人累计带货表现。 |
| `data.linked_creators.list[].creator_cumulative_performance.creator_cumulative_gmv` | number | GMV。 |
| `data.linked_creators.list[].creator_cumulative_performance.creator_cumulative_units_sold` | integer | 销量。 |
| `data.linked_creators.list[].creator_cumulative_performance.creator_total_like_count` | integer | 数量。 |
| `data.linked_creators.list[].creator_cumulative_performance.creator_total_play_count` | integer | 数量。 |
| `data.linked_creators.list[].creator_cumulative_performance.creator_video_count_total` | integer | 达人视频总数。 |
| `data.linked_creators.list[].product_contribution` | object | 商品贡献。 |
| `data.linked_creators.list[].product_contribution.product_gmv` | number | GMV。 |
| `data.linked_creators.list[].product_contribution.product_linked_live_count` | integer | 数量。 |
| `data.linked_creators.list[].product_contribution.product_linked_video_count` | integer | 数量。 |
| `data.linked_creators.list[].product_contribution.product_units_sold` | integer | 销量。 |
| `data.linked_creators.list[].product_contribution.product_video_gmv` | integer | GMV。 |
| `data.linked_creators.list[].product_contribution.product_video_units_sold` | integer | 销量。 |
| `data.linked_creators.total` | integer | 符合条件的记录总数。 |

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
    "field" : "units_sold",
    "order" : "desc"
  },
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-creator-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-creator-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "product_id" : "1733683494177178921"
  },
  "orderby" : {
    "field" : "units_sold",
    "order" : "desc"
  },
  "pagesize" : 10
}'
```

# FastMoss `shop_creator_analysis` API 参考

### shop_creator_analysis

分析店铺合作的达人结构

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-creator-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 过滤参数。 |
| `filter.author_product_type` | integer | 否 | 达人商品类型。可选值：1（短视频带货）、2（直播带货）。 |
| `filter.follower_count_range` | object | 否 | 粉丝数范围。 |
| `filter.follower_count_range.max` | number | 否 | 最大值。 |
| `filter.follower_count_range.min` | number | 否 | 最小值。 |
| `filter.seller_id` | string | 是 | 店铺卖家 ID。 |
| `filter.sold_count_range` | object | 否 | 销量范围。 |
| `filter.sold_count_range.max` | number | 否 | 最大值。 |
| `filter.sold_count_range.min` | number | 否 | 最小值。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、28（近 28 天）、90（近 90 天）、-1（累计口径）。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：follower_count（粉丝数）、sold_count（销量）、sale_amount（销售金额）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码。默认值：1。最小值：1。最大值：500。 |
| `pagesize` | integer | 否 | 每页条数。默认值：10。最大值：10。 |
| `filter.creator_uid` | string | 否 | 店铺关联达人uid。 |
| `filter.creator_unique_id` | string | 否 | 店铺关联达人唯一ID @xxxxxxx。 |
| `filter.shop_name` | string | 否 | 店铺名称。 |
| `filter.region` | string | 否 | 店铺所在国家/地区。seller_name 和 region 必须同时传。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.creator_category_distribution` | array | 达人类目分布。 |
| `data.creator_category_distribution[].category_id` | integer | 类目 ID。 |
| `data.creator_category_distribution[].creator_category` | string | 达人类目。 |
| `data.creator_category_distribution[].creator_count` | integer | 数量。 |
| `data.creator_category_distribution[].creator_share_percent` | number | 百分比。 |
| `data.creator_category_distribution[].gmv` | integer | 成交总额 GMV。 |
| `data.creator_category_distribution[].region` | string | 国家或地区代码。 |
| `data.creator_category_distribution[].units_sold` | integer | 销量。 |
| `data.creator_summary` | object | 达人汇总。 |
| `data.creator_summary.linked_creator_count` | integer | 关联达人数。 |
| `data.creator_summary.live_creator_count` | integer | 数量。 |
| `data.creator_summary.newly_linked_creator_count` | integer | 数量。 |
| `data.creator_summary.region` | string | 国家或地区代码。 |
| `data.creator_summary.total_gmv` | integer | 累计 GMV。 |
| `data.creator_summary.total_units_sold` | integer | 累计销量。 |
| `data.creator_summary.video_creator_count` | integer | 数量。 |
| `data.follower_tier_distribution` | array | 粉丝层级分布。 |
| `data.follower_tier_distribution[].creator_count` | integer | 数量。 |
| `data.follower_tier_distribution[].creator_share_percent` | number | 百分比。 |
| `data.follower_tier_distribution[].follower_tier` | string | 粉丝量级。 |
| `data.follower_tier_distribution[].gmv` | integer | 成交总额 GMV。 |
| `data.follower_tier_distribution[].region` | string | 国家或地区代码。 |
| `data.follower_tier_distribution[].units_sold` | integer | 销量。 |
| `data.linked_creators` | object | 关联达人列表。 |
| `data.linked_creators.list` | array | 结果列表。 |
| `data.linked_creators.total` | integer | 符合条件的记录总数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28,
    "author_product_type" : 1
  },
  "orderby" : [ {
    "field" : "units_sold",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/shop-creator-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-creator-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28,
    "author_product_type" : 1
  },
  "orderby" : [ {
    "field" : "units_sold",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

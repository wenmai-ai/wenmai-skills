# FastMoss `shop_live_analysis` API 参考

### shop_live_analysis

分析店铺的直播表现

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-live-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 过滤参数。 |
| `filter.is_shop` | integer | 否 | 是否为店铺账号。 |
| `filter.seller_id` | string | 是 | 店铺卖家 ID。 |
| `filter.summary_end_date` | string | 否 | 汇总结束日期。 |
| `filter.summary_start_date` | string | 否 | 汇总开始日期。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、28（近 28 天）、90（近 90 天）。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：start_time（开始时间）、product_count（商品数）、total_user_count（累计用户数）、units_sold（销量）、gmv（GMV）。 |
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
| `data.live_performance_summary` | object | 店铺直播表现汇总 |
| `data.live_performance_summary.avg_gmv_per_live` | integer | 场均直播 GMV。 |
| `data.live_performance_summary.avg_units_sold_per_live` | integer | 场均直播销量。 |
| `data.live_performance_summary.avg_viewer_entries_per_live` | integer | 场均进入直播间人数。 |
| `data.live_performance_summary.total_gmv` | number | 累计 GMV。 |
| `data.live_performance_summary.total_live_session_count` | integer | 数量。 |
| `data.live_performance_summary.total_units_sold` | integer | 累计销量。 |
| `data.live_performance_summary.total_viewer_entries` | integer | 进入直播间总人次。 |
| `data.lives` | object | 直播列表。 |
| `data.lives.list` | array | 结果列表。 |
| `data.lives.list[].commerce_metrics` | object | 电商指标。 |
| `data.lives.list[].commerce_metrics.gmv` | number | 成交总额 GMV。 |
| `data.lives.list[].commerce_metrics.main_product_category_id` | integer | ID。 |
| `data.lives.list[].commerce_metrics.main_product_category_name` | string | 名称。 |
| `data.lives.list[].commerce_metrics.product_count` | integer | 商品数。 |
| `data.lives.list[].commerce_metrics.units_sold` | integer | 销量。 |
| `data.lives.list[].creator` | object | 达人资料。 |
| `data.lives.list[].creator.avatar_url` | string | 头像 URL。 |
| `data.lives.list[].creator.category_id` | integer | 类目 ID。 |
| `data.lives.list[].creator.category_name` | string | 类目名称。 |
| `data.lives.list[].creator.creator_handle` | string | 达人唯一用户名。 |
| `data.lives.list[].creator.creator_uid` | string | 达人 UID。 |
| `data.lives.list[].creator.follower_count` | integer | 粉丝数。 |
| `data.lives.list[].creator.nickname` | string | 昵称。 |
| `data.lives.list[].creator.region` | string | 国家或地区代码。 |
| `data.lives.list[].live` | object | 直播场次资料。 |
| `data.lives.list[].live.cover_url` | string | 封面 URL。 |
| `data.lives.list[].live.duration_seconds` | integer | 时长（秒）。 |
| `data.lives.list[].live.is_live_now` | boolean | 是否标记。 |
| `data.lives.list[].live.live_type_code` | integer | 直播类型编码。 |
| `data.lives.list[].live.live_type_label` | string | 直播类型展示文案。 |
| `data.lives.list[].live.room_id` | string | 直播间 ID。 |
| `data.lives.list[].live.started_at` | integer | 时间。 |
| `data.lives.list[].live.title` | string | 标题。 |
| `data.lives.list[].traffic_metrics` | object | 流量指标。 |
| `data.lives.list[].traffic_metrics.follower_gain` | integer | 粉丝增量。 |
| `data.lives.list[].traffic_metrics.peak_concurrent_viewers` | integer | 峰值在线人数。 |
| `data.lives.list[].traffic_metrics.share_count` | integer | 分享数。 |
| `data.lives.list[].traffic_metrics.viewer_entries` | integer | 进入直播间人次。 |
| `data.lives.total` | integer | 符合条件的记录总数。 |
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
  "page" : 1,
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28
  },
  "orderby" : [ {
    "field" : "start_time",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/shop-live-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-live-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28
  },
  "orderby" : [ {
    "field" : "start_time",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

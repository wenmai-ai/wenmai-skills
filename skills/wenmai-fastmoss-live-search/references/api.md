# FastMoss `live_search` API 参考

### live_search

用标题/主播搜索直播场次

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/live-search` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤参数。 |
| `filter.creator_category` | integer | 否 | 达人分类。 |
| `filter.follower_range` | object | 否 | 粉丝数区间:{'min':10,'max':1000}。 |
| `filter.follower_range.max` | number | 否 | 最大值。 |
| `filter.follower_range.min` | number | 否 | 最小值。 |
| `filter.live_type` | integer | 否 | 直播类型：1店铺播 2达人播。 |
| `filter.product_category` | integer | 否 | 商品分类(一级)。 |
| `filter.region` | string | 否 | 国家/地区。region 范围: ['US','GB','MX','ES','DE','IT','FR','ID','VN','MY','TH','PH','BR','JP','SG']。 |
| `filter.room_id` | string | 否 | 直播间 ID。 |
| `filter.sold_range` | object | 否 | 直播间销量区间:{'min':10,'max':100}。 |
| `filter.sold_range.max` | number | 否 | 最大值。 |
| `filter.sold_range.min` | number | 否 | 最小值。 |
| `filter.start_time` | object | 是 | 开播时间区间:{'min':1742976585,'max':1742976585}。 |
| `filter.start_time.max` | integer | 否 | 最大值。 |
| `filter.start_time.min` | integer | 否 | 最小值。 |
| `filter.viewer_range` | object | 否 | 观看人数区间:{'min':10,'max':100}。 |
| `filter.viewer_range.max` | number | 否 | 最大值。 |
| `filter.viewer_range.min` | number | 否 | 最小值。 |
| `keywords` | string | 否 | 搜索关键词。 |
| `lang` | string | 否 | 语言设置，英语(默认值)：EN_US 中文：ZH_CN。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：start_time（开始时间）、total_viewer_count（累计观看人数）、total_units_sold（累计销量）、total_gmv（累计 GMV）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 默认:1。page * pagesize <= 5000。 |
| `pagesize` | integer | 否 | 默认:10。page * pagesize <= 5000。pagesize 范围[1,100]。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.list` | array | 直播搜索结果 |
| `data.list[].creator` | object | 达人资料 |
| `data.list[].creator.creator_handle` | string | 达人唯一用户名。 |
| `data.list[].creator.creator_name` | string | 达人昵称。 |
| `data.list[].creator.creator_region` | string | 达人所在地区。 |
| `data.list[].creator.creator_uid` | string | 达人 UID。 |
| `data.list[].creator.follower_count` | integer | 粉丝数 |
| `data.list[].live` | object | 直播场次资料 |
| `data.list[].live.cover_url` | string | 封面 URL。 |
| `data.list[].live.duration_seconds` | integer | 时长（秒）。 |
| `data.list[].live.ended_at` | integer | 时间。 |
| `data.list[].live.linked_product_count` | integer | 数量。 |
| `data.list[].live.room_id` | string | 直播间 ID |
| `data.list[].live.started_at` | integer | 时间。 |
| `data.list[].live.title` | string | 直播标题 |
| `data.list[].performance_summary` | object | 直播表现摘要 |
| `data.list[].performance_summary.currency` | string | 币种。 |
| `data.list[].performance_summary.gmv_per_viewer` | integer | GMV。 |
| `data.list[].performance_summary.live_gmv` | integer | 直播 GMV。 |
| `data.list[].performance_summary.live_units_sold` | integer | 直播销量。 |
| `data.list[].performance_summary.total_viewer_count` | integer | 数量。 |
| `data.total` | integer | 符合条件的记录总数。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "live_type" : 1,
    "start_time" : {
      "max" : 1755388799,
      "min" : 1755302400
    },
    "follower_range" : {
      "max" : 10000,
      "min" : 1000
    },
    "product_category" : 1
  },
  "orderby" : [ {
    "field" : "start_time",
    "order" : "desc"
  } ],
  "keywords" : "daisycabral_",
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/live-search" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/live-search" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "live_type" : 1,
    "start_time" : {
      "max" : 1755388799,
      "min" : 1755302400
    },
    "follower_range" : {
      "max" : 10000,
      "min" : 1000
    },
    "product_category" : 1
  },
  "orderby" : [ {
    "field" : "start_time",
    "order" : "desc"
  } ],
  "keywords" : "daisycabral_",
  "pagesize" : 10
}'
```

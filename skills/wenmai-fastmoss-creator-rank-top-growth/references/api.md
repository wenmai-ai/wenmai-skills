# FastMoss `creator_rank_top_growth` API 参考

### creator_rank_top_growth

查看涨粉最快的达人排行榜

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/creator-rank-top-growth` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤参数。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.date_type` | string | 是 | 统计周期类型。可选值：day（按日）、week（按周）、month（按月）。 |
| `filter.date_value` | string | 是 | 统计周期值。 |
| `filter.region` | string | 否 | 国家/地区。region 范围: ['US','GB','MX','ES','DE','IT','FR','ID','VN','MY','TH','PH','BR','JP','SG']。 |
| `filter.verify_type` | integer | 否 | 认证类型。可选值：1（普通达人）、2（蓝 V 认证达人）。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：follower_inc_count（新增粉丝数）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 默认:1。page * pagesize <= 500。 |
| `pagesize` | integer | 否 | 默认:10。page * pagesize <= 500。pagesize 范围 [1, 100]。 |
| `filter.date_info` | object | 是 | 日期信息。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.date_type` | string | 榜单周期类型 |
| `data.date_value` | string | 榜单周期值；周榜格式为 YYYY-Www |
| `data.list` | array | 结果列表。 |
| `data.list[].creator` | object | 达人资料。 |
| `data.list[].creator.avatar` | string | 头像 URL。 |
| `data.list[].creator.creator_category` | object | 达人类目。 |
| `data.list[].creator.creator_category.id` | integer | ID。 |
| `data.list[].creator.creator_category.name` | string | 名称。 |
| `data.list[].creator.follower_count` | integer | 粉丝数。 |
| `data.list[].creator.nickname` | string | 昵称。 |
| `data.list[].creator.region` | string | 国家或地区代码。 |
| `data.list[].creator.uid` | string | 达人 UID。 |
| `data.list[].creator.unique_id` | string | 达人唯一用户名。 |
| `data.list[].creator.video_count_total` | integer | 视频总数。 |
| `data.list[].growth_metrics` | object | 增长指标。 |
| `data.list[].growth_metrics.follower_increase_count` | integer | 数量。 |
| `data.list[].growth_metrics.follower_increase_rate_percent` | number | 百分比。 |
| `data.normalized_period_key` | string | 归一化周期键。 |
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
    "date_info" : {
      "type" : "day",
      "value" : "2026-03-15"
    },
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "verify_type" : 1
  },
  "orderby" : [ {
    "field" : "follower_inc_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/creator-rank-top-growth" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/creator-rank-top-growth" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "date_info" : {
      "type" : "day",
      "value" : "2026-03-15"
    },
    "date_type" : "day",
    "date_value" : "2026-08-25",
    "verify_type" : 1
  },
  "orderby" : [ {
    "field" : "follower_inc_count",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

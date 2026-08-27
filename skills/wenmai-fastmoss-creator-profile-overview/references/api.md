# FastMoss `creator_profile_overview` API 参考

### creator_profile_overview

查看达人的整体画像与带货数据

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/creator-profile-overview` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.lang` | string | 否 | 返回语言。 |
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
| `data.performance_overview` | object | 达人历史累计画像与带货表现 |
| `data.performance_overview.currency` | string | 币种。 |
| `data.performance_overview.live_avg_duration_seconds` | integer | 直播平均时长（秒）。 |
| `data.performance_overview.live_avg_duration_text` | string | 直播平均时长展示文案。 |
| `data.performance_overview.live_gmv` | number | 直播 GMV。 |
| `data.performance_overview.live_gpm_max` | integer | 直播 GPM 最大值。 |
| `data.performance_overview.live_gpm_min` | integer | 直播 GPM 最小值。 |
| `data.performance_overview.live_peak_concurrent_viewer_count_avg` | integer | 直播平均峰值在线人数。 |
| `data.performance_overview.live_peak_concurrent_viewer_count_max` | integer | 直播峰值在线人数最大值。 |
| `data.performance_overview.live_peak_concurrent_viewer_count_median` | integer | 直播峰值在线人数中位数。 |
| `data.performance_overview.live_total_count` | integer | 直播总场次。 |
| `data.performance_overview.live_total_viewer_count_avg` | integer | 直播场均观看人数。 |
| `data.performance_overview.live_total_viewer_count_max` | integer | 直播观看人数最大值。 |
| `data.performance_overview.live_total_viewer_count_median` | integer | 直播观看人数中位数。 |
| `data.performance_overview.previous_total_gmv_region_rank_text` | string | 上一期地区 GMV 排名展示文案。 |
| `data.performance_overview.region` | string | 国家或地区代码。 |
| `data.performance_overview.total_gmv` | number | 累计 GMV。 |
| `data.performance_overview.total_gmv_region_rank` | integer | 累计 GMV 地区排名。 |
| `data.performance_overview.total_gmv_region_rank_change_percent` | number | 累计 GMV 地区排名变化百分比。 |
| `data.performance_overview.total_gmv_region_rank_trend` | string | 累计 GMV 地区排名趋势。 |
| `data.performance_overview.video_avg_engagement_rate_percent` | number | 视频平均互动率。 |
| `data.performance_overview.video_avg_play_count` | integer | 视频平均播放量。 |
| `data.performance_overview.video_gmv` | number | 视频 GMV。 |
| `data.performance_overview.video_gpm_max` | integer | 视频 GPM 最大值。 |
| `data.performance_overview.video_gpm_min` | integer | 视频 GPM 最小值。 |
| `data.performance_overview.video_ipm` | integer | 视频 IPM。 |
| `data.performance_overview.video_median_play_count` | integer | 视频播放量中位数。 |
| `data.performance_overview.video_pop_rate_percent` | number | 视频爆款率。 |
| `data.performance_overview.video_total_count_all` | integer | 视频总数。 |
| `data.performance_overview.video_total_count_with_product` | integer | 带货视频数。 |
| `data.performance_overview.video_total_count_without_product` | integer | 非带货视频数。 |
| `data.performance_overview.video_total_play_count` | integer | 视频总播放量。 |
| `data.profile` | object | 达人资料 |
| `data.profile.account_type_code` | integer | 账号类型编码。 |
| `data.profile.avatar_url` | string | 头像 URL。 |
| `data.profile.bio` | string | 达人简介。 |
| `data.profile.creator_category_name` | string | 达人类目名称。 |
| `data.profile.creator_handle` | string | 达人唯一用户名。 |
| `data.profile.creator_name` | string | 达人昵称。 |
| `data.profile.creator_uid` | string | 达人 UID。 |
| `data.profile.first_video_date` | string | 首条视频日期。 |
| `data.profile.first_video_timestamp` | integer | 首条视频时间戳。 |
| `data.profile.has_shop_tab` | boolean | 是否开通店铺 Tab。 |
| `data.profile.intelligent_type_code` | integer | 智能账号类型编码。 |
| `data.profile.is_shop_creator` | boolean | 是否为带货达人。 |
| `data.profile.live_type_code` | integer | 直播类型编码。 |
| `data.profile.market_category_l1_names` | array | 市场一级类目名称列表。 |
| `data.profile.product_category_ids` | array | 商品类目 ID 列表。 |
| `data.profile.region` | string | 达人所属国家或地区代码 |
| `data.profile.seller_id` | string | 店铺卖家 ID。 |
| `data.profile.updated_at` | integer | 数据更新时间。 |
| `data.profile.verification_type_code` | integer | 认证类型编码。 |

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
  -Uri "$BASE_URL/fastmoss/creator-profile-overview" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/creator-profile-overview" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "uid" : "6861118469497553925"
  }
}'
```

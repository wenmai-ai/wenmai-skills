# FastMoss `shop_base_info` API 参考

### shop_base_info

查看店铺基本资料与概况

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-base-info` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.seller_id` | string | 是 | 店铺卖家 ID。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.brand_account` | object | 品牌账号信息。 |
| `data.brand_account.account` | object | 账号资料。 |
| `data.brand_account.account.avatar_url` | string | 头像 URL。 |
| `data.brand_account.account.follower_count` | integer | 粉丝数。 |
| `data.brand_account.account.handle` | string | 账号 unique_id。 |
| `data.brand_account.account.nickname` | string | 昵称。 |
| `data.brand_account.account.region` | string | 国家或地区代码。 |
| `data.brand_account.account.total_like_count` | integer | 获赞总数。 |
| `data.brand_account.account.uid` | string | 达人 UID。 |
| `data.brand_account.account.video_count` | integer | 视频数。 |
| `data.brand_account.count` | integer | 数量。 |
| `data.brand_account.follower_count_total` | integer | 粉丝合计。 |
| `data.category_benchmark` | object | 同类目均值对照。 |
| `data.category_benchmark.category_avg_creator_count` | integer | 同类目平均达人数。 |
| `data.category_benchmark.category_avg_gmv` | number | 同类目平均 GMV。 |
| `data.category_benchmark.category_avg_live_count` | integer | 同类目平均直播数。 |
| `data.category_benchmark.category_avg_units_sold` | integer | 同类目平均销量。 |
| `data.category_benchmark.category_avg_video_count` | integer | 同类目平均视频数。 |
| `data.performance_summary` | object | 销售表现摘要。 |
| `data.performance_summary.active_product_count` | integer | 在售商品数。 |
| `data.performance_summary.linked_creator_count` | integer | 关联达人数。 |
| `data.performance_summary.linked_live_count` | integer | 关联直播数。 |
| `data.performance_summary.linked_video_count` | integer | 关联视频数。 |
| `data.performance_summary.price_range` | object | 价格区间。 |
| `data.performance_summary.price_range.avg_ceiling_price` | number | 平均最高价。 |
| `data.performance_summary.price_range.avg_floor_price` | number | 平均最低价。 |
| `data.performance_summary.price_range.max_price` | number | 最高价。 |
| `data.performance_summary.price_range.min_price` | number | 最低价。 |
| `data.performance_summary.total_gmv` | number | 累计 GMV。 |
| `data.performance_summary.total_product_count` | integer | 商品总数。 |
| `data.performance_summary.total_units_sold` | integer | 累计销量。 |
| `data.ranking_summary` | object | 榜单摘要。 |
| `data.ranking_summary.category_rank` | integer | 类目排名。 |
| `data.ranking_summary.category_rank_change` | integer | 类目排名变化。 |
| `data.ranking_summary.category_rank_previous` | integer | 上一期类目排名。 |
| `data.ranking_summary.is_category_ranked` | boolean | 是否进入类目榜。 |
| `data.ranking_summary.is_region_ranked` | boolean | 是否进入地区榜。 |
| `data.ranking_summary.ranking_period_month` | string | 榜单月份。 |
| `data.ranking_summary.region_rank` | integer | 地区排名。 |
| `data.ranking_summary.region_rank_change` | integer | 地区排名变化。 |
| `data.ranking_summary.region_rank_previous` | integer | 上一期地区排名。 |
| `data.service_metrics` | object | 服务指标。 |
| `data.service_metrics.delivery_rate_percent` | integer | 发货及时率。 |
| `data.service_metrics.positive_feedback_rate_percent` | integer | 好评率。 |
| `data.service_metrics.response_rate_percent` | integer | 回复率。 |
| `data.service_metrics.shop_rating` | number | 店铺评分。 |
| `data.service_metrics.shop_rating_full_score` | integer | 店铺评分满分。 |
| `data.shop` | object | 店铺资料 |
| `data.shop.currency_code` | string | 币种代码。 |
| `data.shop.is_fully_managed` | boolean | 是否为全托管模式。 |
| `data.shop.primary_category_id` | integer | 主营类目 ID。 |
| `data.shop.primary_category_name` | string | 主营类目名称。 |
| `data.shop.region` | string | 店铺所属国家或地区代码 |
| `data.shop.seller_id` | string | 店铺卖家 ID |
| `data.shop.shop_avatar_url` | string | 店铺头像 URL。 |
| `data.shop.shop_created_date` | string | 店铺创建日期。 |
| `data.shop.shop_name` | string | 店铺名称 |
| `data.shop.shop_type_code` | string | 店铺类型编码。 |
| `data.shop.snapshot_at` | string | 数据快照时间。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "seller_id" : "7496313543931234624"
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/shop-base-info" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-base-info" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "seller_id" : "7496313543931234624"
  }
}'
```

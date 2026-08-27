# FastMoss `shop_product_analysis` API 参考

### shop_product_analysis

分析店铺商品组合（类目、价格带等）

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-product-analysis` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 过滤参数。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.listing_end_date` | string | 否 | 上架结束日期。 |
| `filter.listing_start_date` | string | 否 | 上架开始日期。 |
| `filter.listing_time_range_days` | integer | 否 | 上架时间范围（天）。可选值：7（上架不超过 7 天）、14（上架不超过 14 天）、28（上架不超过 28 天）、90（上架不超过 90 天）。 |
| `filter.seller_id` | string | 是 | 店铺卖家 ID。 |
| `filter.time_range_days` | integer | 否 | 统计时间范围（天）。可选值：7（近 7 天）、28（近 28 天）、90（近 90 天）。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：launch_time（上架时间）、commission_rate_percent（佣金率百分比）、day7_units_sold（近 7 天销量）、day28_units_sold（近 28 天销量）、day90_units_sold（近 90 天销量）、day7_gmv（近 7 天 GMV）、day28_gmv（近 28 天 GMV）、day90_gmv（近 90 天 GMV）、total_units_sold（累计销量）、total_gmv（累计 GMV）。 |
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
| `data.category_distribution` | object | 店铺商品类目分布 |
| `data.category_distribution.by_gmv` | object | GMV。 |
| `data.category_distribution.by_gmv.level_1` | array | 一级。 |
| `data.category_distribution.by_gmv.level_1[].category_id` | integer | 类目 ID。 |
| `data.category_distribution.by_gmv.level_1[].category_name` | string | 类目名称。 |
| `data.category_distribution.by_gmv.level_1[].gmv` | number | 成交总额 GMV。 |
| `data.category_distribution.by_gmv.level_1[].gmv_share_percent` | number | 百分比。 |
| `data.category_distribution.by_gmv.level_2` | array | 二级。 |
| `data.category_distribution.by_gmv.level_2[].category_id` | integer | 类目 ID。 |
| `data.category_distribution.by_gmv.level_2[].category_name` | string | 类目名称。 |
| `data.category_distribution.by_gmv.level_2[].gmv` | number | 成交总额 GMV。 |
| `data.category_distribution.by_gmv.level_2[].gmv_share_percent` | number | 百分比。 |
| `data.category_distribution.by_product_count` | object | 数量。 |
| `data.category_distribution.by_product_count.level_1` | array | 一级。 |
| `data.category_distribution.by_product_count.level_1[].category_id` | integer | 类目 ID。 |
| `data.category_distribution.by_product_count.level_1[].category_name` | string | 类目名称。 |
| `data.category_distribution.by_product_count.level_1[].product_count` | integer | 商品数。 |
| `data.category_distribution.by_product_count.level_1[].product_share_percent` | integer | 百分比。 |
| `data.category_distribution.by_product_count.level_2` | array | 二级。 |
| `data.category_distribution.by_product_count.level_2[].category_id` | integer | 类目 ID。 |
| `data.category_distribution.by_product_count.level_2[].category_name` | string | 类目名称。 |
| `data.category_distribution.by_product_count.level_2[].product_count` | integer | 商品数。 |
| `data.category_distribution.by_product_count.level_2[].product_share_percent` | integer | 百分比。 |
| `data.category_distribution.by_units_sold` | object | 销量。 |
| `data.category_distribution.by_units_sold.level_1` | array | 一级。 |
| `data.category_distribution.by_units_sold.level_1[].category_id` | integer | 类目 ID。 |
| `data.category_distribution.by_units_sold.level_1[].category_name` | string | 类目名称。 |
| `data.category_distribution.by_units_sold.level_1[].units_sold` | integer | 销量。 |
| `data.category_distribution.by_units_sold.level_1[].units_sold_share_percent` | number | 百分比。 |
| `data.category_distribution.by_units_sold.level_2` | array | 二级。 |
| `data.category_distribution.by_units_sold.level_2[].category_id` | integer | 类目 ID。 |
| `data.category_distribution.by_units_sold.level_2[].category_name` | string | 类目名称。 |
| `data.category_distribution.by_units_sold.level_2[].units_sold` | integer | 销量。 |
| `data.category_distribution.by_units_sold.level_2[].units_sold_share_percent` | number | 百分比。 |
| `data.price_band_distribution` | object | 店铺商品价格带分布 |
| `data.price_band_distribution.by_gmv` | array | GMV。 |
| `data.price_band_distribution.by_gmv[].gmv` | number | 成交总额 GMV。 |
| `data.price_band_distribution.by_gmv[].gmv_share_percent` | number | 百分比。 |
| `data.price_band_distribution.by_gmv[].max_price_boundary` | integer | 价格上限。 |
| `data.price_band_distribution.by_gmv[].price_band` | string | 价格带。 |
| `data.price_band_distribution.by_product_count` | array | 数量。 |
| `data.price_band_distribution.by_product_count[].max_price_boundary` | integer | 价格上限。 |
| `data.price_band_distribution.by_product_count[].price_band` | string | 价格带。 |
| `data.price_band_distribution.by_product_count[].product_count` | integer | 商品数。 |
| `data.price_band_distribution.by_product_count[].product_share_percent` | integer | 百分比。 |
| `data.price_band_distribution.by_units_sold` | array | 销量。 |
| `data.price_band_distribution.by_units_sold[].max_price_boundary` | integer | 价格上限。 |
| `data.price_band_distribution.by_units_sold[].price_band` | string | 价格带。 |
| `data.price_band_distribution.by_units_sold[].units_sold` | integer | 销量。 |
| `data.price_band_distribution.by_units_sold[].units_sold_share_percent` | number | 百分比。 |
| `data.product_catalog_summary` | object | 商品目录摘要。 |
| `data.product_catalog_summary.active_product_count` | integer | 在售商品数。 |
| `data.product_catalog_summary.commission_rate_max_percent` | integer | 百分比。 |
| `data.product_catalog_summary.commission_rate_min_percent` | integer | 百分比。 |
| `data.product_catalog_summary.historical_product_count` | integer | 数量。 |
| `data.products` | object | 店铺商品列表 |
| `data.products.list` | array | 结果列表。 |
| `data.products.total` | integer | 符合条件的记录总数。 |
| `data.shop` | object | 店铺资料 |
| `data.shop.category_id` | integer | 类目 ID。 |
| `data.shop.currency_symbol` | string | 币种符号。 |
| `data.shop.listing_time_range_days` | integer | 上架时间范围天数。 |
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
    "time_range_days" : 28,
    "listing_time_range_days" : 7
  },
  "orderby" : [ {
    "field" : "day7_units_sold",
    "order" : "desc"
  } ],
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/shop-product-analysis" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-product-analysis" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "seller_id" : "7496313543931234624",
    "time_range_days" : 28,
    "listing_time_range_days" : 7
  },
  "orderby" : [ {
    "field" : "day7_units_sold",
    "order" : "desc"
  } ],
  "pagesize" : 10
}'
```

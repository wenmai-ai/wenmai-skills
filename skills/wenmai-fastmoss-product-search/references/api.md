# FastMoss `product_search` API 参考

### product_search

用关键词/价格搜索商品

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-search` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤参数。 |
| `filter.category_path` | array | 否 | 类目路径。 |
| `filter.commission_rate_range` | object | 否 | 佣金比例区间，例如：{'min': 1, 'max': 10}。 |
| `filter.commission_rate_range.max` | number | 否 | 最大值。 |
| `filter.commission_rate_range.min` | number | 否 | 最小值。 |
| `filter.creator_count_range` | object | 否 | 带货达人数量区间，例如：{'min': 1, 'max': 10}。 |
| `filter.creator_count_range.max` | number | 否 | 最大值。 |
| `filter.creator_count_range.min` | number | 否 | 最小值。 |
| `filter.day28_gmv_range` | object | 否 | 近 28 天 GMV 范围。 |
| `filter.day28_gmv_range.max` | number | 否 | 最大值。 |
| `filter.day28_gmv_range.min` | number | 否 | 最小值。 |
| `filter.day28_units_sold_range` | object | 否 | 近 28 天销量范围。 |
| `filter.day28_units_sold_range.max` | number | 否 | 最大值。 |
| `filter.day28_units_sold_range.min` | number | 否 | 最小值。 |
| `filter.day7_gmv_range` | object | 否 | 近 7 天 GMV 范围。 |
| `filter.day7_gmv_range.max` | number | 否 | 最大值。 |
| `filter.day7_gmv_range.min` | number | 否 | 最小值。 |
| `filter.day7_units_sold_range` | object | 否 | 近 7 天销量范围。 |
| `filter.day7_units_sold_range.max` | number | 否 | 最大值。 |
| `filter.day7_units_sold_range.min` | number | 否 | 最小值。 |
| `filter.floor_price_range` | object | 否 | 最低价范围。 |
| `filter.floor_price_range.max` | number | 否 | 最大值。 |
| `filter.floor_price_range.min` | number | 否 | 最小值。 |
| `filter.is_cross_border` | boolean | 否 | 是否跨境 1是，0否。 |
| `filter.is_free_shipping` | boolean | 否 | 是否为免邮商品。 |
| `filter.is_fully_managed` | boolean | 否 | 是否全托管 1是，0否。 |
| `filter.is_local_warehouse` | boolean | 否 | 是否为本地仓商品。 |
| `filter.is_new_listed` | boolean | 否 | 是否为近期上新商品。 |
| `filter.is_sshop` | boolean | 否 | 是否为全托管店铺商品(deprecated)。 |
| `filter.is_top_selling` | boolean | 否 | 是否为热销商品。 |
| `filter.listing_status` | string | 否 | 上架状态。可选值：on_sale（在售）、off_shelf（已下架）。 |
| `filter.product_id` | string | 否 | 商品ID，string 或 array。 |
| `filter.region` | string | 否 | 国家/地区。region 范围: ['US','GB','MX','ES','DE','IT','FR','ID','VN','MY','TH','PH','BR','JP','SG'] 获取全部分类列表：/product/v1/category。 |
| `filter.shop_type` | integer | 否 | 店铺类型：1（本土），2（跨境）(deprecated)。 |
| `filter.total_gmv_range` | object | 否 | 累计 GMV 范围。 |
| `filter.total_gmv_range.max` | number | 否 | 最大值。 |
| `filter.total_gmv_range.min` | number | 否 | 最小值。 |
| `filter.units_sold_range` | object | 否 | 销量区间，例如：{'min': 1, 'max': 10}。 |
| `filter.units_sold_range.max` | number | 否 | 最大值。 |
| `filter.units_sold_range.min` | number | 否 | 最小值。 |
| `keywords` | string | 否 | 搜索关键词。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：day7_units_sold（近 7 天销量）、day7_gmv（近 7 天 GMV）、day28_units_sold（近 28 天销量）、day28_gmv（近 28 天 GMV）、commission_rate（佣金率）、total_units_sold（累计销量）、total_gmv（累计 GMV）、creator_count（达人数）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 页码，默认值：1。page * pagesize <= 5000。 |
| `pagesize` | integer | 否 | 每页条数，默认值：10。page * pagesize <= 5000。pagesize 范围[1,100]。 |
| `filter.l1_category_id` | integer | 否 | 一级类目 ID。 |
| `filter.l2_category_id` | integer | 否 | 二级类目 ID。 |
| `filter.l3_category_id` | integer | 否 | 三级类目 ID。 |
| `filter.seller_id` | string | 否 | 店铺 ID。 |
| `filter.price_range` | object | 否 | 商品最低价区间，例如：{'min': 1, 'max': 10}。需配合 region 或 seller_id 使用，因为不同地区价格单位不同。 |
| `filter.price_range.min` | number | 否 | 最小值。 |
| `filter.price_range.max` | number | 否 | 最大值。 |
| `filter.off_shelves` | integer | 否 | 商品状态：0 在售，1 下架。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.list` | array | 商品搜索结果 |
| `data.list[].distribution_summary` | object | 渠道与内容分布摘要 |
| `data.list[].distribution_summary.linked_creator_count` | integer | 关联达人数。 |
| `data.list[].distribution_summary.linked_video_count` | integer | 关联视频数。 |
| `data.list[].product` | object | 商品资料 |
| `data.list[].product.category` | object | 类目。 |
| `data.list[].product.category.l1` | object | 一级类目。 |
| `data.list[].product.category.l1.id` | integer | ID。 |
| `data.list[].product.category.l1.name` | string | 名称。 |
| `data.list[].product.category.l2` | object | 二级类目。 |
| `data.list[].product.category.l2.id` | integer | ID。 |
| `data.list[].product.category.l2.name` | string | 名称。 |
| `data.list[].product.category.l3` | object | 三级类目。 |
| `data.list[].product.category.l3.id` | integer | ID。 |
| `data.list[].product.category.l3.name` | string | 名称。 |
| `data.list[].product.ceiling_price` | number | 最高价。 |
| `data.list[].product.commission_rate_percent` | integer | 佣金率百分比。 |
| `data.list[].product.cover_url` | string | 封面 URL。 |
| `data.list[].product.currency_code` | string | 币种代码。 |
| `data.list[].product.fastmoss_detail_url` | string | FastMoss 详情页 URL。 |
| `data.list[].product.floor_price` | number | 最低价。 |
| `data.list[].product.is_cross_border` | boolean | 是否为跨境店铺或商品。 |
| `data.list[].product.is_free_shipping` | boolean | 是否包邮。 |
| `data.list[].product.is_fully_managed` | boolean | 是否为全托管模式。 |
| `data.list[].product.launch_date` | string | 上架日期。 |
| `data.list[].product.launch_time` | integer | 上架时间戳。 |
| `data.list[].product.price_display` | string | 价格展示文案。 |
| `data.list[].product.product_id` | string | 商品 ID |
| `data.list[].product.product_rating` | number | 商品评分。 |
| `data.list[].product.product_source` | string | 商品来源。 |
| `data.list[].product.region` | string | 国家或地区代码。 |
| `data.list[].product.sku_count` | integer | SKU 数量。 |
| `data.list[].product.tiktok_product_url` | string | TikTok 商品链接。 |
| `data.list[].product.title` | string | 商品标题 |
| `data.list[].sales_summary` | object | 商品销售摘要 |
| `data.list[].sales_summary.last_28d_gmv` | integer | 近 28 天 GMV。 |
| `data.list[].sales_summary.last_28d_units_sold` | integer | 近 28 天销量。 |
| `data.list[].sales_summary.last_7d_gmv` | number | 近 7 天 GMV。 |
| `data.list[].sales_summary.last_7d_units_sold` | integer | 近 7 天销量。 |
| `data.list[].sales_summary.last_90d_gmv` | number | 近 90 天 GMV。 |
| `data.list[].sales_summary.last_90d_units_sold` | integer | 近 90 天销量。 |
| `data.list[].sales_summary.total_gmv` | integer | 累计 GMV。 |
| `data.list[].sales_summary.total_units_sold` | integer | 累计销量。 |
| `data.list[].sales_summary.yesterday_gmv` | number | 昨日 GMV。 |
| `data.list[].sales_summary.yesterday_units_sold` | integer | 昨日销量。 |
| `data.list[].shop` | object | 店铺资料 |
| `data.list[].shop.avatar_url` | string | 头像 URL。 |
| `data.list[].shop.shop_id` | string | 店铺 ID。 |
| `data.list[].shop.shop_name` | string | 店铺名称 |
| `data.list[].shop.total_units_sold` | integer | 累计销量。 |
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
    "off_shelves" : 0,
    "price_range" : {
      "max" : 30,
      "min" : 10
    },
    "l1_category_id" : 2,
    "commission_rate_range" : {
      "max" : 15,
      "min" : 10
    }
  },
  "orderby" : [ {
    "field" : "day7_units_sold",
    "order" : "desc"
  } ],
  "keywords" : "test",
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-search" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-search" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "off_shelves" : 0,
    "price_range" : {
      "max" : 30,
      "min" : 10
    },
    "l1_category_id" : 2,
    "commission_rate_range" : {
      "max" : 15,
      "min" : 10
    }
  },
  "orderby" : [ {
    "field" : "day7_units_sold",
    "order" : "desc"
  } ],
  "keywords" : "test",
  "pagesize" : 10
}'
```

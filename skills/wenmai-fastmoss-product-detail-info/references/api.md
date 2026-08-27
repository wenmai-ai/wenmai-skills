# FastMoss `product_detail_info` API 参考

### product_detail_info

查看商品基本资料（价格、评分、物流等）

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/product-detail-info` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 是 | 筛选条件。 |
| `filter.product_id` | string | 是 | 商品 ID。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.product` | object | 商品资料 |
| `data.product.category_l1` | object | 一级类目。 |
| `data.product.category_l1.id` | integer | ID。 |
| `data.product.category_l1.name` | string | 名称。 |
| `data.product.category_l2` | object | 二级类目。 |
| `data.product.category_l2.id` | integer | ID。 |
| `data.product.category_l2.name` | string | 名称。 |
| `data.product.category_l3` | object | 三级类目。 |
| `data.product.category_l3.id` | integer | ID。 |
| `data.product.category_l3.name` | string | 名称。 |
| `data.product.category_sales_rank` | string | 类目销量排名。 |
| `data.product.ceiling_price` | number | 最高价。 |
| `data.product.ceiling_price_display` | string | 最高价展示文案。 |
| `data.product.commission_rate_percent` | integer | 佣金率百分比。 |
| `data.product.country_sales_rank` | string | 国家销量排名。 |
| `data.product.cover_url` | string | 封面 URL。 |
| `data.product.currency_code` | string | 币种代码。 |
| `data.product.currency_symbol` | string | 币种符号。 |
| `data.product.detail_url` | string | 详情页 URL。 |
| `data.product.floor_price` | number | 最低价。 |
| `data.product.floor_price_display` | string | 最低价展示文案。 |
| `data.product.has_paid_promotion` | boolean | 是否有付费推广。 |
| `data.product.has_sku_options` | boolean | 是否有 SKU 规格。 |
| `data.product.is_new_product` | boolean | 是否为新品。 |
| `data.product.is_off_shelf` | boolean | 是否已下架。 |
| `data.product.launch_time` | integer | 上架时间戳。 |
| `data.product.linked_creator_count` | integer | 关联达人数。 |
| `data.product.linked_live_count` | integer | 关联直播数。 |
| `data.product.linked_video_count` | integer | 关联视频数。 |
| `data.product.popularity_index` | integer | 热度指数。 |
| `data.product.product_rating` | number | 商品评分。 |
| `data.product.region` | string | 国家或地区代码。 |
| `data.product.review_count` | integer | 评论数。 |
| `data.product.shipping_fee` | string | 运费说明。 |
| `data.product.shipping_method_code` | integer | 物流方式编码。 |
| `data.product.stock_count` | integer | 库存数量。 |
| `data.product.stock_count_label` | string | 库存数量展示文案。 |
| `data.product.title` | string | 商品标题 |
| `data.product.total_gmv` | number | 累计 GMV。 |
| `data.product.total_units_sold` | integer | 累计销量。 |
| `data.product.viral_index` | integer | 传播指数。 |
| `data.shop` | object | 店铺资料 |
| `data.shop.avatar_url` | string | 头像 URL。 |
| `data.shop.region` | string | 店铺所属国家或地区代码 |
| `data.shop.shop_category_l1` | object | 店铺主营一级类目。 |
| `data.shop.shop_category_l1.id` | integer | ID。 |
| `data.shop.shop_category_l1.name` | string | 名称。 |
| `data.shop.shop_id` | string | 店铺 ID。 |
| `data.shop.shop_name` | string | 店铺名称 |
| `data.shop.shop_total_gmv` | number | 店铺累计 GMV。 |
| `data.shop.shop_total_units_sold` | integer | 店铺累计销量。 |

#### PowerShell 请求示例

```powershell
$API_KEY = "你的网关APIKey"

$BASE_URL = "https://all-api.wenmai-ai.com/wmapi/v1"

$body = @'
{
  "filter" : {
    "product_id" : "1733683494177178921"
  }
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/product-detail-info" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/product-detail-info" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "filter" : {
    "product_id" : "1733683494177178921"
  }
}'
```

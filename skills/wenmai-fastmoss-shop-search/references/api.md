# FastMoss `shop_search` API 参考

### shop_search

用店名/关键词搜索店铺

| 项目 | 内容 |
| --- | --- |
| 请求方法 | `POST` |
| 版本 | `v1` |
| 请求地址 | `/fastmoss/shop-search` |
| 供应商 | FASTMOSS |

#### 请求参数

| 字段 | 类型 | 是否必填 | 中文描述 |
| --- | --- | --- | --- |
| `filter` | object | 否 | 过滤参数。 |
| `filter.brand_name` | string | 否 | 品牌名称。 |
| `filter.category_id` | integer | 否 | 类目 ID。 |
| `filter.creator_range` | object | 否 | 关联达人数量范围:{"min":1,"max":123}。 |
| `filter.creator_range.max` | number | 否 | 最大值。 |
| `filter.creator_range.min` | number | 否 | 最小值。 |
| `filter.creator_uid` | string | 否 | 达人 UID。 |
| `filter.creator_unique_id` | string | 否 | 达人唯一id @xxxxxxx。 |
| `filter.is_fully_managed` | boolean | 否 | 是否为全托管模式。 |
| `filter.is_local` | boolean | 否 | 是否为本地店铺或商品。 |
| `filter.rating_range` | object | 否 | 店铺评分范围:{"min":1,"max":123}。 |
| `filter.rating_range.max` | number | 否 | 最大值。 |
| `filter.rating_range.min` | number | 否 | 最小值。 |
| `filter.region` | string | 否 | 国家/地区。region 范围: ['US','GB','MX','ES','DE','IT','FR','ID','VN','MY','TH','PH','BR','JP','SG']。 |
| `filter.seller_id` | string | 否 | 店铺卖家 ID。 |
| `filter.shop_name` | string | 否 | 店铺名称。 |
| `keywords` | string | 否 | 搜索关键词。 |
| `orderby` | array | 否 | 排序参数。 |
| `orderby[].field` | string | 否 | 排序或统计字段。可选值：day7_units_sold（近 7 天销量）、day7_gmv（近 7 天 GMV）、total_units_sold（累计销量）、total_gmv（累计 GMV）。 |
| `orderby[].order` | string | 否 | 排序方向。可选值：asc（升序）、desc（降序）。默认值："desc"。 |
| `page` | integer | 否 | 默认:1。page * pagesize <= 5000。 |
| `pagesize` | integer | 否 | 默认:10。page * pagesize <= 5000。pagesize 范围[1,100]。 |
| `filter.is_sshop` | boolean | 否 | 是否为S店铺。 |

#### 响应参数

| 字段 | 类型 | 中文描述 |
| --- | --- | --- |
| `code` | string | 网关状态码；成功时为 `OK`。 |
| `message` | string | 网关响应消息；成功时通常为 `成功`。 |
| `requestId` | string | 请求链路 ID，用于日志追踪和问题排查。 |
| `supplier` | string | 实际数据供应商代码；FastMoss 接口返回 `FASTMOSS`。 |
| `apiCode` | string | 本次调用的标准 API 接口代码。 |
| `data` | object | 业务响应对象；以下 `data.*` 字段均位于此对象内。 |
| `data.page` | integer | 当前页码。 |
| `data.pagesize` | integer | 每页条数。 |
| `data.shops` | array | 店铺列表。 |
| `data.shops[].active_product_count` | integer | 在售商品数。 |
| `data.shops[].brand_name` | string | 品牌名称。 |
| `data.shops[].currency_code` | string | 币种代码。 |
| `data.shops[].gmv_last_7d` | integer | 近 7 天 GMV。 |
| `data.shops[].is_fully_managed` | boolean | 是否为全托管模式。 |
| `data.shops[].linked_creator` | object | 关联达人。 |
| `data.shops[].linked_creator.avatar_url` | string | 头像 URL。 |
| `data.shops[].linked_creator.category_id` | integer | 类目 ID。 |
| `data.shops[].linked_creator.category_name` | string | 类目名称。 |
| `data.shops[].linked_creator.follower_count` | integer | 粉丝数。 |
| `data.shops[].linked_creator.nickname` | string | 昵称。 |
| `data.shops[].linked_creator.region` | string | 国家或地区代码。 |
| `data.shops[].linked_creator.uid` | string | 达人 UID。 |
| `data.shops[].linked_creator.unique_id` | string | 达人唯一用户名。 |
| `data.shops[].linked_creator_count` | integer | 关联达人数。 |
| `data.shops[].main_category` | object | 主营类目。 |
| `data.shops[].main_category.id` | integer | ID。 |
| `data.shops[].main_category.name` | string | 名称。 |
| `data.shops[].region` | string | 国家或地区代码。 |
| `data.shops[].seller_id` | string | 店铺卖家 ID。 |
| `data.shops[].shop_name` | string | 店铺名称。 |
| `data.shops[].shop_rating` | number | 店铺评分。 |
| `data.shops[].shop_type_code` | string | 店铺类型编码。 |
| `data.shops[].total_gmv` | number | 累计 GMV。 |
| `data.shops[].total_units_sold` | integer | 累计销量。 |
| `data.shops[].units_sold_last_7d` | integer | 近 7 天销量。 |
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
    "shop_name" : "xxxx"
  },
  "orderby" : [ {
    "field" : "day7_units_sold",
    "order" : "desc"
  } ],
  "keywords" : "",
  "pagesize" : 10
}
'@

$response = Invoke-WebRequest `
  -Uri "$BASE_URL/fastmoss/shop-search" `
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
  "https://all-api.wenmai-ai.com/wmapi/v1/fastmoss/shop-search" \
  -H "secret-key: 你的网关APIKey" \
  -H "Content-Type: application/json" \
  -d '{
  "page" : 1,
  "filter" : {
    "region" : "US",
    "shop_name" : "xxxx"
  },
  "orderby" : [ {
    "field" : "day7_units_sold",
    "order" : "desc"
  } ],
  "keywords" : "",
  "pagesize" : 10
}'
```

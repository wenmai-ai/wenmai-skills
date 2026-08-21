# Wenmai SellerSprite ASIN 销量趋势 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/asin-sales-trend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口编码**：`asin_sales_trend`
- **脚本入口**：`scripts/asin_sales_trend.py`
- **API Key / 充值**：https://agent.wenmai-ai.com/

调用前先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。仅当两个环境变量都未获取到时提示用户在本机配置；不得在未检查环境变量的情况下声称缺少 API Key，也不要在对话、文件或日志中复述密钥。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `marketplace` | string | 是 | Amazon 市场站点。可选值：`US`、`JP`、`UK`、`DE`、`FR`、`IT`、`ES`、`CA`、`IN`。含义依次为美国站（USD）、日本站（JPY）、英国站（GBP）、德国站（EUR）、法国站（EUR）、意大利站（EUR）、西班牙站（EUR）、加拿大站（CAD）、印度站（INR）。 |
| `asin` | string | 是 | Amazon 商品标识（ASIN），例如 `B08GHW4TBS`。 |

## 请求示例

```json
{"marketplace":"US","asin":"B08GHW4TBS"}
```

## 响应结构

公共响应字段为 `code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 中文说明 |
|------|------|----------|
| `asin` | object | ASIN 商品基础信息及销量趋势。 |
| `asin.asin` | string | ASIN 商品标识。 |
| `asin.asinUrl` | string | ASIN 商品链接。 |
| `asin.parent` | string | 父体 ASIN。 |
| `asin.marketplace` | string | Amazon 市场站点。枚举同请求参数。 |
| `asin.title` | string | 商品标题。 |
| `asin.price` | number | 当前价格。 |
| `asin.rating` | number | 商品评分。 |
| `asin.ratings` | integer | 评分数量。 |
| `asin.reviews` | integer / null | 评论数量。 |
| `asin.availableDate` | integer | 商品上架日期，Unix 毫秒时间戳。 |
| `asin.brand` | string | 品牌名称。 |
| `asin.brandUrl` | string | 品牌链接。 |
| `asin.bsrId` | string | 大类目标识。 |
| `asin.bsrLabel` | string | 大类目名称。 |
| `asin.bsrRank` | integer | 大类目排名。 |
| `asin.createdTime` | integer | 商品创建时间，Unix 毫秒时间戳。 |
| `asin.dimensions` | string | 商品尺寸。 |
| `asin.firstRatingDate` | integer | 首次评分日期，Unix 毫秒时间戳。 |
| `asin.imageUrl` | string | 商品主图链接。 |
| `asin.lqs` | integer | Listing 页面质量得分。 |
| `asin.nodeId` | integer | 类目节点标识。 |
| `asin.nodeIdPath` | string | 类目节点路径。 |
| `asin.nodeLabelPath` | string | 类目名称路径。 |
| `asin.nodeLabelPathLocale` | string / null | 本地语言类目名称路径。 |
| `asin.primePrice` | number | Prime 价格；`-1` 表示没有 Prime 价格。 |
| `asin.deliveryPrice` | number | 配送价格；`-1` 表示没有配送价格。 |
| `asin.coupon` | string | 优惠券信息。 |
| `asin.questions` | integer / null | 买家问题数量。 |
| `asin.variantRatings` | integer / null | 变体评分数量。 |
| `asin.variantReviews` | integer / null | 变体评论数量。 |
| `asin.sellerId` | string | 卖家标识。 |
| `asin.sellerName` | string | 卖家名称。 |
| `asin.fulfillment` | string | 配送方式。 |
| `asin.sellers` | integer | 卖家数量。 |
| `asin.updatedTime` | integer | 数据更新时间，Unix 毫秒时间戳。 |
| `asin.variations` | integer | 变体数量。 |
| `asin.weight` | string | 商品重量。 |
| `asin.zoomImageUrl` | string | 商品大图链接。 |
| `asin.skuList` | array<string> | SKU 属性列表。 |
| `asin.features` | array<string> | 商品五点描述列表。 |
| `asin.overviews` | string | 商品详情属性，JSON 字符串。 |
| `asin.subcategories` | array<object> | 子类目信息数组。 |
| `asin.subcategories[].rank` | integer | 子类目排名。 |
| `asin.subcategories[].code` | string | 子类目编码。 |
| `asin.subcategories[].label` | string | 子类目名称。 |
| `asin.variationList` | array<object> | 变体列表。 |
| `asin.variationList[].asin` | string | 变体 ASIN。 |
| `asin.variationList[].attribute` | string | 变体属性。 |
| `asin.badge` | object | 商品标识对象。 |
| `asin.badge.bestSeller` | string | Best Seller 标识，枚举：`Y`、`N`。 |
| `asin.badge.amazonChoice` | string | Amazon Choice 标识，枚举：`Y`、`N`。 |
| `asin.badge.newRelease` | string | 新品标识，枚举：`Y`、`N`。 |
| `asin.badge.ebc` | string | A+ 页面标识，枚举：`Y`、`N`。 |
| `asin.badge.video` | string | 视频介绍标识，枚举：`Y`、`N`。 |
| `salesTrendPoints` | array<object> | 按月份返回 ASIN 销量趋势数据；与 `asin` 同为 `data` 顶层字段。 |
| `salesTrendPoints[].month` | string | 统计月份。 |
| `salesTrendPoints[].price` | number / null | 该月份商品价格。 |
| `salesTrendPoints[].averagePrice` | number / null | 该月份平均价格。 |
| `salesTrendPoints[].parentUnitSales` | integer | 该月份父体销量。 |
| `salesTrendPoints[].childUnitSales` | integer / null | 该月份子体销量。 |
| `salesTrendPoints[].parentSalesRevenue` | number / null | 该月份父体销售额。 |
| `salesTrendPoints[].childSalesRevenue` | number / null | 该月份子体销售额。 |

## 使用要点

- `salesTrendPoints` 位于 `data` 顶层，不位于 `asin` 内。
- 数值为 `null` 表示上游未返回该月份对应数据，不应当作 `0`。
- `asin.subcategories` 和 `asin.variationList` 均按数组处理。
- 保留趋势记录原始月份、价格、销量和销售额，不推算缺失数据。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 先检查 `WENMAI_API_KEY`，再检查 `WENMAI_SECRET_KEY`；两者都缺少时提示用户在本机配置，不要求在对话中粘贴密钥。 |
| 余额或额度不足 | 到 https://agent.wenmai-ai.com/ 充值后重试。 |
| 参数错误 | 检查 `marketplace`、`asin` 和站点枚举。 |
| 非 OK 响应 | 读取 `message` 与 `requestId`，不要将错误响应当作业务数据。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/asin-sales-trend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"marketplace":"US","asin":"B08GHW4TBS"}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（2026-08-21 访问）。

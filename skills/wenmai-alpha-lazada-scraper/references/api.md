# Wenmai Alpha Lazada Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/lazada-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_lazada_scraper`
- **接口说明**：Lazada Products + Reviews + SKUs + Vouchers
- **脚本入口**：`scripts/alpha_lazada_scraper.py`，脚本参数即标准 API POST Body JSON

### 运行时覆盖

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `WENMAI_API_ORIGIN` | Wenmai API 地址 | `https://all-api.wenmai-ai.com` |
| `WENMAI_API_BASE_PATH` | 标准 API Base Path | `/wmapi/v1` |
| `WENMAI_API_TIMEOUT` | HTTP 超时时间，单位秒 | `120` |

## 请求参数

POST Body（JSON）：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `mode` | string | 是 | 采集模式。可选值：search、url。 |
| `country` | string | 否 | 国家或站点。可选值：sg、my、th、vn、ph、id。 |
| `queries` | array | 否 | 搜索关键词列表。 |
| `categoryId` | string | 否 | 分类。 |
| `minPrice` | integer | 否 | 价格。 |
| `maxPrice` | integer | 否 | 最大采集或返回数量。 |
| `minRating` | integer | 否 | 最大采集或返回数量。 |
| `freeShippingOnly` | boolean | 否 | freeShippingOnly 字段。 |
| `sortBy` | string | 否 | 排序方式。可选值：popularity、priceAsc、priceDesc、ratingDesc、newest、bestSelling。 |
| `urls` | array | 否 | 页面链接列表。 |
| `reviewsOnly` | boolean | 否 | 评论列表。 |
| `fetchReviews` | boolean | 否 | 是否启用该选项。 |
| `maxReviewsPerProduct` | integer | 否 | 最大采集或返回数量。 |
| `fetchDetails` | boolean | 否 | 是否抓取商品详情页增强信息。设为 `true` 后会启用单独计费的详情增强能力；仅在用户明确要求时使用。 |
| `maxPages` | integer | 否 | 最大采集或返回数量。 |
| `maxListings` | integer | 否 | 最大采集或返回数量。 |
| `maxNotifyListings` | integer | 否 | 最大采集或返回数量。 |

### 额外计费提醒

`fetchDetails: true` 会启用单独计费的详情页增强能力。普通列表或搜索请求应省略该参数或保持 `false`。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "mode": "search",
  "urls": [
    "https://www.lazada.sg/catalog/?q=earbuds"
  ],
  "sortBy": "popularity",
  "country": "sg",
  "queries": [
    "laptop"
  ],
  "maxPages": 0,
  "maxPrice": 3,
  "minPrice": 1,
  "minRating": 1,
  "categoryId": "keyboard",
  "maxListings": 3,
  "reviewsOnly": false,
  "fetchDetails": false,
  "fetchReviews": false,
  "freeShippingOnly": false,
  "maxNotifyListings": 3,
  "maxReviewsPerProduct": 3
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `type` | string | 采集模式。 |
| `id` | number | ID 标识。 |
| `url` | string | 链接地址。 |
| `productName` | string | productName 字段。 |
| `productId` | number | ID 标识。 |
| `productUrl` | string | 链接地址。 |
| `sourceUrl` | string | 链接地址。 |
| `seedType` | string | seedType 字段。 |
| `seedValue` | string | seedValue 字段。 |
| `country` | number | 国家或站点。 |
| `currency` | string | 币种。 |
| `currentPrice` | number | 价格。 |
| `originalPrice` | number | 价格。 |
| `discountText` | boolean | 数量。 |
| `discountPct` | number | 数量。 |
| `ratingScore` | number | 评分。 |
| `reviewCount` | number | 评论列表。 |
| `itemSold` | array | itemSold 字段。 |
| `inStock` | number | 库存信息。 |
| `isSponsored` | boolean | 是否启用该选项。 |
| `freeShipping` | string | freeShipping 字段。 |
| `sellerName` | string | 卖家信息。 |
| `sellerId` | number | 卖家信息。 |
| `primaryImage` | string | primaryImage 字段。 |
| `fetchedAt` | string | 是否启用该选项。 |

## 使用要点

- 本接口适合：Lazada 东南亚电商商品。
- 优先使用用户给定的 URL、关键词、商品 ID、站点、国家、语言、排序、分页和数量限制。
- 采集类接口的字段会随目标平台页面结构变化；输出分析时保留原始字段名和 URL，避免把缺失字段补写成事实。
- 当用户需要多平台对比时，分别调用对应 Alpha 原子 Skill，再在上层分析中合并结果。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按上方请求参数表修正枚举值、日期格式、分页范围、URL/关键词数组、数量范围或必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/lazada-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode": "search", "urls": ["https://www.lazada.sg/catalog/?q=earbuds"], "sortBy": "popularity", "country": "sg", "queries": ["laptop"], "maxPages": 0, "maxPrice": 3, "minPrice": 1, "minRating": 1, "categoryId": "keyboard", "maxListings": 3, "reviewsOnly": false, "fetchDetails": false, "fetchReviews": false, "freeShippingOnly": false, "maxNotifyListings": 3, "maxReviewsPerProduct": 3}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。

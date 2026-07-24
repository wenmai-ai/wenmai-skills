# Wenmai Alpha Free Amazon Product Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/free-amazon-product-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_free_amazon_product_scraper`
- **接口说明**：Amazon Scraper
- **脚本入口**：`scripts/alpha_free_amazon_product_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `categoryUrls` | array | 是 | 页面链接列表。 |
| `maxItemsPerStartUrl` | integer | 否 | 链接地址。 |
| `maxSearchPagesPerStartUrl` | integer | 否 | 链接地址。 |
| `maxProductVariantsAsSeparateResults` | integer | 否 | 最大采集或返回数量。 |
| `useCaptchaSolver` | boolean | 否 | useCaptchaSolver 字段。 |
| `scrapeProductVariantPrices` | boolean | 否 | 价格。 |
| `scrapeProductDetails` | boolean | 否 | scrapeProductDetails 字段。 |

## 请求示例

脚本入参示例：

```json
{
  "categoryUrls": [
    {
      "url": "https://www.amazon.com/s?k=keyboard"
    }
  ],
  "useCaptchaSolver": false,
  "maxItemsPerStartUrl": 3,
  "scrapeProductDetails": true,
  "maxSearchPagesPerStartUrl": 3,
  "scrapeProductVariantPrices": false,
  "maxProductVariantsAsSeparateResults": 0
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 标题。 |
| `url` | string | 链接地址。 |
| `asin` | string | ID 标识。 |
| `originalAsin` | string | ID 标识。 |
| `brand` | string | 品牌。 |
| `author` | string | 作者信息。 |
| `price` | object | 价格。 |
| `price.value` | number | value 字段。 |
| `price.currency` | string | 币种。 |
| `listPrice` | object | 价格。 |
| `listPrice.value` | number | value 字段。 |
| `listPrice.currency` | string | 币种。 |
| `shippingPrice` | object | 价格。 |
| `shippingPrice.value` | number | value 字段。 |
| `shippingPrice.currency` | string | 币种。 |
| `inStock` | boolean | 库存信息。 |
| `inStockText` | string | 库存信息。 |
| `delivery` | string | delivery 字段。 |
| `fastestDelivery` | string | fastestDelivery 字段。 |
| `condition` | string | condition 字段。 |
| `stars` | number | stars 字段。 |
| `starsBreakdown` | object | starsBreakdown 字段。 |
| `reviewsCount` | number | 评论列表。 |
| `answeredQuestions` | number | answeredQuestions 字段。 |
| `breadCrumbs` | string | breadCrumbs 字段。 |
| `sustainabilityFeatures` | array | sustainabilityFeatures 字段。 |
| `description` | string | 描述。 |
| `features` | array<string> | features 字段。 |
| `videosCount` | number | 数量。 |
| `visitStoreLink` | object | 店铺信息。 |
| `visitStoreLink.text` | string | 文本内容。 |
| `visitStoreLink.url` | string | 链接地址。 |
| `thumbnailImage` | string | thumbnailImage 字段。 |
| `galleryThumbnails` | array<string> | galleryThumbnails 字段。 |
| `highResolutionImages` | array<string> | highResolutionImages 字段。 |
| `importantInformation` | object | importantInformation 字段。 |
| `importantInformation.title` | string | 标题。 |
| `importantInformation.items` | array | items 字段。 |
| `returnPolicy` | string | returnPolicy 字段。 |
| `support` | string | support 字段。 |
| `variantAsins` | array<string> | ID 标识。 |
| `variantDetails` | array | variantDetails 字段。 |
| `reviewsLink` | string | 评论列表。 |
| `hasReviews` | boolean | 是否启用该选项。 |
| `variantAttributes` | array | variantAttributes 字段。 |
| `attributes` | array | attributes 字段。 |
| `attributesMapped` | object | attributesMapped 字段。 |
| `productOverview` | array | productOverview 字段。 |
| `manufacturerAttributes` | array | manufacturerAttributes 字段。 |
| `seller` | object | 卖家信息。 |
| `bestsellerRanks` | array | 卖家信息。 |
| `isAmazonChoice` | boolean | 是否启用该选项。 |
| `amazonChoiceText` | string | amazonChoiceText 字段。 |
| `bookDescription` | string | 描述。 |
| `priceRange` | object | 价格。 |
| `priceRange.min` | object | 最大采集或返回数量。 |
| `priceRange.max` | object | 最大采集或返回数量。 |
| `aPlusContent` | object | aPlusContent 字段。 |
| `brandStory` | object | 品牌。 |
| `productComparison` | object | productComparison 字段。 |
| `aiReviewsSummary` | object | 评论列表。 |
| `monthlyPurchaseVolume` | string | monthlyPurchaseVolume 字段。 |
| `productPageReviews` | array | 评论列表。 |
| `productPageReviewsFromOtherCountries` | array | 评论列表。 |
| `offers` | array | offers 字段。 |
| `locationText` | string | locationText 字段。 |
| `unNormalizedProductUrl` | string | 链接地址。 |
| `loadedCountryCode` | string | 国家或站点。 |
| `categoryPageData` | object | 分类。 |
| `categoryPageData.categoryUrl` | string | 链接地址。 |
| `categoryPageData.saleSummary` | string | saleSummary 字段。 |
| `categoryPageData.isSponsored` | boolean | 是否启用该选项。 |
| `categoryPageData.bestsellerBadge` | string | 卖家信息。 |
| `categoryPageData.productPosition` | number | productPosition 字段。 |
| `categoryPageData.pageNumber` | number | 数量。 |
| `bestsellerPageData` | object | 卖家信息。 |
| `bestsellerPageData.position` | number | position 字段。 |
| `bestsellerPageData.categoryUrl` | string | 链接地址。 |
| `bestsellerPageData.categoryName` | string | 分类。 |
| `bestsellerPageData.categoryFullName` | string | 分类。 |

## 使用要点

- 本接口适合：Amazon 商品、评论、Listing、竞品或搜索结果。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/free-amazon-product-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"categoryUrls": [{"url": "https://www.amazon.com/s?k=keyboard"}], "useCaptchaSolver": false, "maxItemsPerStartUrl": 3, "scrapeProductDetails": true, "maxSearchPagesPerStartUrl": 3, "scrapeProductVariantPrices": false, "maxProductVariantsAsSeparateResults": 0}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

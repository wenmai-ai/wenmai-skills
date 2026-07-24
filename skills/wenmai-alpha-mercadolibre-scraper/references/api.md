# Wenmai Alpha Mercadolibre Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/mercadolibre-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_mercadolibre_scraper`
- **接口说明**：MercadoLibre Scraper \| Multi-Country + Reviews + Q&A + Seller
- **脚本入口**：`scripts/alpha_mercadolibre_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `mode` | string | 否 | 采集模式。可选值：reviews、product、search、seller。 |
| `country` | string | 否 | 国家或站点。可选值：MX、AR、BR、EC、DO、CL、CO、PE、UY。 |
| `productUrls` | array | 否 | 页面链接列表。 |
| `maxItems` | integer | 否 | 最大采集或返回数量。 |
| `reviewRating` | string | 否 | 评分。可选值：all、1、2、3、4、5。 |
| `reviewOrder` | string | 否 | 排序方式。可选值：relevance、dateCreated。 |
| `searchQuery` | string | 否 | 搜索关键词。 |
| `sellerUrls` | array | 否 | 页面链接列表。 |
| `includeSellerProfile` | boolean | 否 | 是否启用该选项。 |
| `includeFeaturedItems` | boolean | 否 | 是否启用该选项。 |
| `maxItemsPerSeller` | integer | 否 | 最大采集或返回数量。 |
| `includeReviews` | boolean | 否 | 是否启用该选项。 |
| `includeQuestions` | boolean | 否 | 是否启用该选项。 |
| `includeVariations` | boolean | 否 | 是否启用该选项。 |
| `startUrls` | array | 否 | 页面链接列表。 |
| `maxConcurrency` | integer | 否 | 币种。 |

## 请求示例

脚本入参示例：

```json
{
  "mode": "reviews",
  "country": "MX",
  "maxItems": 3,
  "sellerUrls": [
    "https://www.mercadolibre.com.mx/tienda/phone-depot"
  ],
  "productUrls": [
    "https://www.mercadolibre.com.mx/apple-iphone-15-256-gb-negro/p/MLM27172669"
  ],
  "reviewOrder": "relevance",
  "searchQuery": "iphone",
  "reviewRating": "all",
  "includeReviews": true,
  "maxConcurrency": 3,
  "includeQuestions": true,
  "includeVariations": true,
  "maxItemsPerSeller": 0,
  "includeFeaturedItems": false,
  "includeSellerProfile": true
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `mode` | string | 采集模式。 |
| `country` | string | 国家或站点。 |
| `siteId` | string | ID 标识。 |
| `productId` | string | ID 标识。 |
| `catalogProductId` | string | ID 标识。 |
| `title` | string | 标题。 |
| `url` | string | 链接地址。 |
| `thumbnail` | string | 图片链接。 |
| `images` | array | 图片列表。 |
| `brand` | string | 品牌。 |
| `description` | string | 描述。 |
| `price` | number | 价格。 |
| `originalPrice` | number | 价格。 |
| `discountPercentage` | number | 数量。 |
| `currency` | string | 币种。 |
| `availability` | string | 库存信息。 |
| `condition` | string | condition 字段。 |
| `sku` | string | ID 标识。 |
| `rating` | number | 评分。 |
| `ratingCount` | number | 评分。 |
| `reviewCount` | number | 评论列表。 |
| `installments` | object | installments 字段。 |
| `freeShipping` | boolean | freeShipping 字段。 |
| `shippingText` | string | shippingText 字段。 |
| `shipping` | object | shipping 字段。 |
| `returnPolicy` | object | returnPolicy 字段。 |
| `sellerId` | string/number | 卖家信息。 |
| `sellerName` | string | 卖家信息。 |
| `sellerReputation` | string | 卖家信息。 |
| `sellerPowerStatus` | string | 卖家信息。 |
| `isOfficialStore` | boolean | 是否启用该选项。 |
| `officialStoreName` | string | 店铺信息。 |
| `breadcrumbs` | array | breadcrumbs 字段。 |
| `categoryId` | string | 分类。 |
| `domainId` | string | ID 标识。 |
| `attributes` | array | attributes 字段。 |
| `variations` | array | variations 字段。 |
| `reviews` | array | 评论列表。 |
| `questions` | array | questions 字段。 |
| `promotions` | array | promotions 字段。 |
| `position` | number | position 字段。 |
| `listingType` | string | listingType 字段。 |
| `reviewId` | number | ID 标识。 |
| `reviewRating` | number | 评分。 |
| `reviewText` | string | 评论列表。 |
| `reviewDate` | string | 时间或日期。 |
| `reviewCountry` | string | 国家或站点。 |
| `reviewLikes` | number | 评论列表。 |
| `reviewMedia` | array | 评论列表。 |
| `kind` | string | kind 字段。 |
| `sellerSlug` | string | 卖家信息。 |
| `sellerProfileUrl` | string | 链接地址。 |
| `sellerListingUrl` | string | 链接地址。 |
| `shopId` | string | 店铺信息。 |
| `shopName` | string | 店铺信息。 |
| `shopType` | string | 店铺信息。 |
| `storefrontType` | string | 店铺信息。 |
| `officialStoreId` | number | 店铺信息。 |
| `totalFollowers` | number | 数量。 |
| `dateCreated` | string | 时间或日期。 |
| `substatus` | string | 状态。 |
| `hasModerations` | boolean | 是否启用该选项。 |
| `hasDebts` | boolean | 是否启用该选项。 |
| `restrictions` | array | restrictions 字段。 |
| `tags` | array | tags 字段。 |
| `freeTrialStart` | string | freeTrialStart 字段。 |
| `freeTrialEnd` | string | freeTrialEnd 字段。 |
| `freeTrialPeriod` | number | freeTrialPeriod 字段。 |
| `brandId` | string | 品牌。 |
| `brandName` | string | 品牌。 |
| `brandRegistryId` | string | 品牌。 |
| `multiseller` | boolean | 卖家信息。 |
| `bannerUrl` | string | 链接地址。 |
| `bannerMobileUrl` | string | 链接地址。 |
| `logoUrl` | string | 链接地址。 |
| `eshopsLogo` | string | 店铺信息。 |
| `headerType` | string | headerType 字段。 |
| `subdomain` | string | subdomain 字段。 |
| `storefrontUrl` | string | 链接地址。 |
| `sellerDescription` | string | 卖家信息。 |
| `sellerAddress` | object | 卖家信息。 |
| `sellerPhone` | string | 卖家信息。 |
| `sellerEmail` | string | 卖家信息。 |
| `menuCorridors` | array | menuCorridors 字段。 |
| `itemsCount` | number | 数量。 |
| `corridorName` | string | corridorName 字段。 |
| `corridorUrl` | string | 链接地址。 |
| `scrapedAt` | string | scrapedAt 字段。 |

## 使用要点

- 本接口适合：MercadoLibre 拉美商品、卖家、评论和问答。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/mercadolibre-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode": "reviews", "country": "MX", "maxItems": 3, "sellerUrls": ["https://www.mercadolibre.com.mx/tienda/phone-depot"], "productUrls": ["https://www.mercadolibre.com.mx/apple-iphone-15-256-gb-negro/p/MLM27172669"], "reviewOrder": "relevance", "searchQuery": "iphone", "reviewRating": "all", "includeReviews": true, "maxConcurrency": 3, "includeQuestions": true, "includeVariations": true, "maxItemsPerSeller": 0, "includeFeaturedItems": false, "includeSellerProfile": true}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

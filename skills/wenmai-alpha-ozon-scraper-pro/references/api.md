# Wenmai Alpha Ozon Scraper Pro API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/ozon-scraper-pro`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_ozon_scraper_pro`
- **接口说明**：Ozon — Product Scraper
- **脚本入口**：`scripts/alpha_ozon_scraper_pro.py`，脚本参数即标准 API POST Body JSON

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
| `queries` | array<string> | 否 | 搜索关键词列表。传入非空列表会启用单独计费的搜索结果能力；不要自动补充或扩展关键词。 |
| `urls` | array | 否 | 页面链接列表。 |
| `maxResults` | integer | 否 | 最大采集或返回数量。 |
| `skipDetails` | boolean | 否 | skipDetails 字段。 |
| `includeSellerDetails` | boolean | 否 | 是否启用该选项。 |
| `sorting` | string | 否 | 排序方式。可选值：score、new、price、price_desc、rating、discount。 |
| `minPrice` | integer | 否 | 价格。 |
| `maxPrice` | integer | 否 | 最大采集或返回数量。 |
| `delivery` | string | 否 | delivery 字段。可选值：1、2、4、8。 |
| `onSale` | boolean | 否 | onSale 字段。 |
| `hasDiscount` | boolean | 否 | 是否启用该选项。 |
| `brandCertified` | boolean | 否 | 品牌。 |
| `isInstallment` | boolean | 否 | 是否启用该选项。 |
| `hasReviewPoints` | boolean | 否 | 是否启用该选项。 |
| `language` | string | 否 | 语言代码。可选值：ru、en、zh-Hans、kk、hy、uz-Latn。 |
| `currency` | string | 否 | 币种。可选值：RUB、USD、BYN、KZT、ILS、AMD、UZS、KGS、AZN、GEL、MNT、AUD、CAD、CHF、CNY、CZK、DKK、GBP、JPY、MDL、NOK、PLN、SEK、SGD、TRY、UAH。 |

### 额外计费提醒

非空 `queries` 会触发单独计费的搜索结果能力。仅在用户明确要求关键词搜索时传入，并在请求前提醒用户。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "urls": [
    "https://www.ozon.ru/category/noutbuki-15692/"
  ],
  "onSale": false,
  "sorting": "score",
  "currency": "RUB",
  "language": "ru",
  "maxPrice": 3,
  "minPrice": 1,
  "maxResults": 3,
  "hasDiscount": false,
  "skipDetails": false,
  "isInstallment": false,
  "brandCertified": false,
  "hasReviewPoints": false,
  "includeSellerDetails": false
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `sku` | string | ID 标识。 |
| `url` | string | 链接地址。 |
| `title` | string | 标题。 |
| `cardPrice` | number | 价格。 |
| `cardPriceDecimal` | number | 价格。 |
| `price` | number | 价格。 |
| `priceDecimal` | number | 价格。 |
| `originalPrice` | number | 价格。 |
| `originalPriceDecimal` | number | 价格。 |
| `isAvailable` | boolean | 是否启用该选项。 |
| `showOriginalPrice` | number | 价格。 |
| `offerType` | string | offerType 字段。 |
| `coverImageUrl` | string | 链接地址。 |
| `images` | array | 图片列表。 |
| `customerMedia` | array | customerMedia 字段。 |
| `customerMedia.totalCount` | number | 数量。 |
| `customerMedia.preview` | array | 评论列表。 |
| `customerMedia.preview.type` | array | 采集模式。 |
| `customerMedia.preview.uuid` | number | ID 标识。 |
| `customerMedia.preview.previewUrl` | array | 链接地址。 |
| `rating` | number | 评分。 |
| `reviewCount` | number | 评论列表。 |
| `productId` | number | ID 标识。 |
| `questionCount` | number | 数量。 |
| `variants` | array | variants 字段。 |
| `variants.aspectName` | array | aspectName 字段。 |
| `variants.aspectKey` | array | aspectKey 字段。 |
| `variants.type` | array | 采集模式。 |
| `variants.options` | array | options 字段。 |
| `variants.options.sku` | array | ID 标识。 |
| `variants.options.name` | array | 名称。 |
| `variants.options.price` | number | 价格。 |
| `variants.options.formattedPrice` | number | 价格。 |
| `variants.options.originalPrice` | number | 价格。 |
| `variants.options.active` | array | active 字段。 |
| `variants.options.availability` | array | 库存信息。 |
| `variants.options.url` | array | 链接地址。 |
| `variants.options.image` | array | 图片链接。 |
| `seller` | string | 卖家信息。 |
| `seller.name` | string | 名称。 |
| `seller.url` | string | 链接地址。 |
| `seller.logo` | string | logo 字段。 |
| `seller.rating` | number | 评分。 |
| `brand` | string | 品牌。 |
| `brand.name` | string | 名称。 |
| `brand.url` | string | 链接地址。 |
| `brand.logo` | string | logo 字段。 |
| `brand.description` | string | 描述。 |
| `bestSellerPrice` | number | 价格。 |
| `otherSellersCount` | number | 卖家信息。 |
| `installment` | string | installment 字段。 |
| `marketingLabels` | string | marketingLabels 字段。 |
| `shortCharacteristics` | boolean | shortCharacteristics 字段。 |
| `shortCharacteristics.name` | boolean | 名称。 |
| `shortCharacteristics.value` | boolean | value 字段。 |
| `breadcrumbs` | string | breadcrumbs 字段。 |
| `breadcrumbs.name` | string | 名称。 |
| `breadcrumbs.url` | string | 链接地址。 |
| `categoryPath` | string | 分类。 |
| `isAuthentic` | boolean | 是否启用该选项。 |
| `discount` | number | 数量。 |
| `hasPriceDecreased` | number | 是否启用该选项。 |
| `characteristics` | boolean | characteristics 字段。 |
| `characteristics.key` | boolean | key 字段。 |
| `characteristics.name` | boolean | 名称。 |
| `characteristics.value` | boolean | value 字段。 |
| `characteristics.hint` | boolean | hint 字段。 |
| `characteristicsCount` | number | 数量。 |
| `description` | string | 描述。 |
| `richDescription` | string | 描述。 |
| `descriptionImages` | array | 描述。 |
| `hashtags` | boolean | 搜索关键词列表。 |
| `recommendedProducts` | array | recommendedProducts 字段。 |
| `recommendedProducts.sku` | array | ID 标识。 |
| `recommendedProducts.url` | array | 链接地址。 |
| `recommendedProducts.image` | array | 图片链接。 |
| `recommendedProducts.title` | array | 标题。 |
| `recommendedProducts.price` | number | 价格。 |
| `recommendedProducts.rating` | number | 评分。 |
| `recommendedProducts.reviewCount` | number | 评论列表。 |
| `recommendedProducts.section` | array | section 字段。 |
| `reviews` | number | 评论列表。 |
| `reviews.reviewId` | number | ID 标识。 |
| `reviews.itemId` | number | ID 标识。 |
| `reviews.rating` | number | 评分。 |
| `reviews.author` | number | 作者信息。 |
| `reviews.isAnonymous` | number | 是否启用该选项。 |
| `reviews.publishedAt` | number | 时间或日期。 |
| `reviews.publishedAtTimestamp` | boolean | 时间或日期。 |
| `reviews.comment` | number | 评论列表。 |
| `reviews.positive` | number | positive 字段。 |
| `reviews.negative` | number | negative 字段。 |
| `reviews.photos` | number | photos 字段。 |
| `reviews.videos` | number | videos 字段。 |
| `reviews.aspectRatings` | number | 评分。 |
| `reviews.useful` | number | useful 字段。 |
| `reviews.unuseful` | number | unuseful 字段。 |
| `reviews.isEdited` | number | 是否启用该选项。 |
| `reviews.commentCount` | number | 评论列表。 |
| `reviewsTotal` | number | 评论列表。 |
| `reviewRatingBreakdown` | number | 评分。 |
| `reviewRatingBreakdown.stars` | number | stars 字段。 |
| `reviewRatingBreakdown.count` | number | 数量。 |
| `otherSellers` | string | 卖家信息。 |
| `hasGoodPrice` | number | 是否启用该选项。 |

## 使用要点

- 本接口适合：Ozon 商品池。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/ozon-scraper-pro" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://www.ozon.ru/category/noutbuki-15692/"], "onSale": false, "sorting": "score", "currency": "RUB", "language": "ru", "maxPrice": 3, "minPrice": 1, "maxResults": 3, "hasDiscount": false, "skipDetails": false, "isInstallment": false, "brandCertified": false, "hasReviewPoints": false, "includeSellerDetails": false}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。

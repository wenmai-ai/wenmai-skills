# Wenmai Alpha Trendyol Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/trendyol-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_trendyol_scraper`
- **接口说明**：Trendyol Product Scraper, Reviews & Q&A
- **脚本入口**：`scripts/alpha_trendyol_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `mode` | string | 是 | 采集模式。可选值：search、url、reviews。 |
| `queries` | array<string> | 否 | 搜索关键词列表。 |
| `minPrice` | integer | 否 | 价格。 |
| `maxPrice` | integer | 否 | 最大采集或返回数量。 |
| `minRating` | string | 否 | 最大采集或返回数量。可选值：0、1、2、3、4、4.5。 |
| `sortBy` | string | 否 | 排序方式。可选值：BEST_SCORE、BEST_SELLER、NEWEST、PRICE_BY_ASC、PRICE_BY_DESC、MOST_RATED、MOST_FAVOURITE。 |
| `freeCargoOnly` | boolean | 否 | freeCargoOnly 字段。 |
| `fastDeliveryOnly` | boolean | 否 | fastDeliveryOnly 字段。 |
| `officialSellerOnly` | boolean | 否 | 卖家信息。 |
| `couponsOnly` | boolean | 否 | couponsOnly 字段。 |
| `inStockOnly` | boolean | 否 | 库存信息。 |
| `urls` | array<string> | 否 | 页面链接列表。 |
| `productInputs` | array<string> | 否 | productInputs 字段。 |
| `maxReviewsPerProduct` | integer | 否 | 最大采集或返回数量。 |
| `maxPages` | integer | 否 | 最大采集或返回数量。 |
| `maxListings` | integer | 否 | 最大采集或返回数量。 |
| `fetchDetails` | boolean | 否 | 是否启用该选项。 |
| `fetchReviews` | boolean | 否 | 是否启用该选项。 |
| `fetchQna` | boolean | 否 | 是否启用该选项。 |
| `maxQnaPerProduct` | integer | 否 | 最大采集或返回数量。 |
| `maxNotifyListings` | integer | 否 | 最大采集或返回数量。 |

## 请求示例

脚本入参示例：

```json
{
  "mode": "url",
  "urls": [
    "https://www.trendyol.com/apple/iphone-15-128-gb-siyah-p-762254032"
  ],
  "maxPages": 1
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `kind` | string | kind 字段。 |
| `contentId` | integer | ID 标识。 |
| `id` | integer | ID 标识。 |
| `groupId` | integer | ID 标识。 |
| `url` | string | 链接地址。 |
| `name` | string | 名称。 |
| `brand` | string | 品牌。 |
| `brandId` | integer | 品牌。 |
| `category` | object | 分类。 |
| `category.id` | integer | ID 标识。 |
| `category.name` | string | 名称。 |
| `price` | object | 价格。 |
| `price.current` | number | current 字段。 |
| `price.original` | string | original 字段。 |
| `price.recommendedRetail` | string | recommendedRetail 字段。 |
| `price.discountPercent` | string | 数量。 |
| `price.currency` | string | 币种。 |
| `rating` | object | 评分。 |
| `rating.score` | string | 评分。 |
| `rating.totalRatings` | string | 评分。 |
| `rating.totalComments` | integer | 评论列表。 |
| `rating.breakdown` | string | breakdown 字段。 |
| `seller` | object | 卖家信息。 |
| `seller.id` | integer | ID 标识。 |
| `seller.name` | string | 名称。 |
| `image` | string | 图片链接。 |
| `images` | array | 图片列表。 |
| `stock` | integer | 库存信息。 |
| `inStock` | boolean | 库存信息。 |
| `boutiqueId` | string | ID 标识。 |
| `campaignId` | string | ID 标识。 |
| `listingId` | string | ID 标识。 |
| `itemNumber` | integer | 数量。 |
| `variantValue` | string | variantValue 字段。 |
| `variantId` | string | ID 标识。 |
| `freeCargo` | boolean | freeCargo 字段。 |
| `fastDelivery` | boolean | fastDelivery 字段。 |
| `officialSeller` | boolean | 卖家信息。 |
| `sameDayShipping` | boolean | sameDayShipping 字段。 |
| `rushDelivery` | boolean | rushDelivery 字段。 |
| `hasCoupon` | boolean | 是否启用该选项。 |
| `hasCodePromo` | boolean | 是否启用该选项。 |
| `hasFlashSale` | boolean | 是否启用该选项。 |
| `isInfluencerPreferred` | boolean | 是否启用该选项。 |
| `hasReviewPhoto` | boolean | 是否启用该选项。 |
| `dealBadge` | string | dealBadge 字段。 |
| `stripBadge` | string | stripBadge 字段。 |
| `promotions` | string | promotions 字段。 |
| `stamps` | string | stamps 字段。 |
| `badges` | string | badges 字段。 |
| `socialProof` | string | socialProof 字段。 |
| `reviews` | string | 评论列表。 |
| `qna` | string | qna 字段。 |
| `scrapedAt` | string | scrapedAt 字段。 |
| `productCode` | string | productCode 字段。 |
| `productGroupId` | integer | ID 标识。 |
| `isGlobalBrand` | boolean | 是否启用该选项。 |
| `webBrand` | object | 品牌。 |
| `webBrand.id` | integer | ID 标识。 |
| `webBrand.name` | string | 名称。 |
| `webBrand.url` | string | 链接地址。 |
| `gender` | object | gender 字段。 |
| `gender.id` | integer | ID 标识。 |
| `gender.name` | string | 名称。 |
| `webCategory` | object | 分类。 |
| `webCategory.id` | integer | ID 标识。 |
| `webCategory.name` | string | 名称。 |
| `webCategoryTree` | array | 分类。 |
| `webCategoryTree.name` | string | 名称。 |
| `webCategoryTree.id` | integer | ID 标识。 |
| `webCategoryTree.level` | integer | level 字段。 |
| `categoryTree` | array | 分类。 |
| `categoryTree.id` | integer | ID 标识。 |
| `categoryTree.name` | string | 名称。 |
| `categoryHierarchy` | string | 分类。 |
| `categoryTopRankings` | array | 分类。 |
| `businessUnit` | object | businessUnit 字段。 |
| `businessUnit.id` | integer | ID 标识。 |
| `businessUnit.name` | string | 名称。 |
| `businessUnit.isDigitalGoods` | boolean | 是否启用该选项。 |
| `attributes` | array | attributes 字段。 |
| `attributes.key` | object | key 字段。 |
| `attributes.key.id` | integer | ID 标识。 |
| `attributes.key.name` | string | 名称。 |
| `attributes.value` | object | value 字段。 |
| `attributes.value.id` | integer | ID 标识。 |
| `attributes.value.name` | string | 名称。 |
| `attributes.searchable` | boolean | searchable 字段。 |
| `attributes.type` | string | 采集模式。 |
| `attributes.isStarred` | boolean | 是否启用该选项。 |
| `attributes.typeId` | integer | ID 标识。 |
| `attributes.description` | string | 描述。 |
| `attributes.mediaUrls` | array | 页面链接列表。 |
| `favoriteCount` | integer | 数量。 |
| `tax` | integer | tax 字段。 |
| `maxInstallment` | integer | 最大采集或返回数量。 |
| `isRefundable` | boolean | 是否启用该选项。 |
| `uxLayout` | string | uxLayout 字段。 |
| `filterableLabelIds` | string | filterableLabelIds 字段。 |
| `englishTranslation` | object | englishTranslation 字段。 |
| `englishTranslation.webBrandCategoryGenders` | object | 分类。 |
| `englishTranslation.webBrandCategoryGenders.genders` | array | genders 字段。 |
| `englishTranslation.webBrandCategoryGenders.brands` | array | 品牌。 |
| `englishTranslation.webBrandCategoryGenders.brands.name` | string | 名称。 |
| `englishTranslation.webBrandCategoryGenders.brands.id` | integer | ID 标识。 |
| `englishTranslation.webBrandCategoryGenders.categories` | array | categories 字段。 |
| `englishTranslation.webBrandCategoryGenders.categories.name` | string | 名称。 |
| `englishTranslation.webBrandCategoryGenders.categories.id` | integer | ID 标识。 |
| `englishTranslation.productName` | string | productName 字段。 |
| `englishTranslation.brandName` | string | 品牌。 |
| `englishTranslation.webColorName` | string | webColorName 字段。 |
| `merchantDetails` | object | merchantDetails 字段。 |
| `merchantDetails.id` | integer | ID 标识。 |
| `merchantDetails.name` | string | 名称。 |
| `merchantDetails.officialName` | string | officialName 字段。 |
| `merchantDetails.cityName` | string | cityName 字段。 |
| `merchantDetails.countryName` | string | 国家或站点。 |
| `merchantDetails.registeredEmailAddress` | string | registeredEmailAddress 字段。 |
| `merchantDetails.taxNumber` | string | 数量。 |
| `merchantDetails.taxOffice` | string | taxOffice 字段。 |
| `merchantDetails.address` | string | address 字段。 |
| `merchantDetails.sellerScore` | object | 评分。 |
| `merchantDetails.sellerScore.value` | number | value 字段。 |
| `merchantDetails.sellerScore.color` | string | color 字段。 |
| `merchantDetails.corporateInvoiceApplicable` | boolean | corporateInvoiceApplicable 字段。 |
| `merchantDetails.logoUrl` | string | 链接地址。 |
| `merchantDetails.hasLocationBasedSales` | boolean | 是否启用该选项。 |
| `merchantDetails.shipmentPreference` | object | shipmentPreference 字段。 |
| `merchantDetails.shipmentPreference.alternativeDeliveryAllowed` | boolean | alternativeDeliveryAllowed 字段。 |
| `merchantDetails.stickerIds` | array | stickerIds 字段。 |
| `merchantDetails.bulkSalesLimit` | integer | 最大采集或返回数量。 |
| `merchantDetails.mpTyCoverageD` | boolean | mpTyCoverageD 字段。 |
| `merchantDetails.codEligible` | boolean | codEligible 字段。 |
| `campaign` | object | campaign 字段。 |
| `campaign.id` | integer | ID 标识。 |
| `campaign.name` | string | 名称。 |
| `campaign.stockTypeId` | integer | ID 标识。 |
| `campaign.startDate` | string | 时间或日期。 |
| `campaign.endDate` | string | 时间或日期。 |
| `campaign.isMultipleSupplied` | boolean | 是否启用该选项。 |
| `detailPromotions` | array | detailPromotions 字段。 |
| `detailPromotions.id` | integer | ID 标识。 |
| `detailPromotions.name` | string | 名称。 |
| `detailPromotions.discountType` | integer | 数量。 |
| `detailPromotions.promotionDiscountType` | string | 数量。 |
| `detailPromotions.promotionEndDate` | string | 时间或日期。 |
| `detailPromotions.promotionRemainingDays` | integer | promotionRemainingDays 字段。 |
| `detailPromotions.promotionRemainingHours` | integer | promotionRemainingHours 字段。 |
| `detailPromotions.promotionRemainingMinutes` | integer | promotionRemainingMinutes 字段。 |
| `detailPromotions.isLimitSatisfied` | boolean | 最大采集或返回数量。 |
| `detailPromotions.shortName` | string | shortName 字段。 |
| `detailPromotions.mocPerUser` | integer | 作者信息。 |
| `detailPromotions.isOnlyAz` | boolean | 是否启用该选项。 |
| `detailPromotions.isTyPlus` | boolean | 是否启用该选项。 |
| `detailPromotions.isApplied` | boolean | 是否启用该选项。 |
| `winnerVariant` | object | winnerVariant 字段。 |
| `winnerVariant.itemNumber` | integer | 数量。 |
| `winnerVariant.listingId` | string | ID 标识。 |
| `winnerVariant.price` | object | 价格。 |
| `winnerVariant.price.currency` | string | 币种。 |

## 使用要点

- 本接口适合：Trendyol 商品。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/trendyol-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode": "url", "urls": ["https://www.trendyol.com/apple/iphone-15-128-gb-siyah-p-762254032"], "maxPages": 1}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

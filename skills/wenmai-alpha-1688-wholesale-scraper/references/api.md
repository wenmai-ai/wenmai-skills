# Wenmai Alpha 1688 Wholesale Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/1688-wholesale-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_1688_wholesale_scraper`
- **接口说明**：1688 Wholesale Scraper - 50+ Fields, 250+ Products/Min
- **脚本入口**：`scripts/alpha_1688_wholesale_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `keywords` | array | 否 | 搜索关键词列表。 |
| `offerIds` | array | 否 | offerIds 字段。 |
| `maxResults` | integer | 否 | 最大采集或返回数量。 |
| `sortBy` | string | 否 | 排序方式。可选值：relevance、bestSelling、priceAsc、priceDesc。 |
| `includeSkuDetails` | boolean | 否 | 是否启用该选项。 |
| `includeDescriptionHtml` | boolean | 否 | 是否启用该选项。 |
| `includeSupplierIntelligence` | boolean | 否 | 是否返回供应商情报。设为 `true` 后会启用单独计费的供应商情报能力；仅在用户明确要求时使用。 |
| `priceMin` | integer | 否 | 价格。 |
| `priceMax` | integer | 否 | 价格。 |
| `minOrderQuantity` | integer | 否 | 排序方式。 |
| `merchantType` | string | 否 | merchantType 字段。可选值：any、superFactory、verifiedMerchant。 |
| `province` | string | 否 | province 字段。 |
| `city` | string | 否 | city 字段。 |

### 额外计费提醒

`includeSupplierIntelligence: true` 会启用单独计费的供应商情报能力。普通商品搜索或详情请求应省略该参数或保持 `false`。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "sortBy": "relevance",
  "keywords": [
    "phone case"
  ],
  "maxResults": 10
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `offerId` | number | ID 标识。 |
| `title` | string | 标题。 |
| `detailUrl` | string | 链接地址。 |
| `price` | number | 价格。 |
| `price.min` | number | 最大采集或返回数量。 |
| `price.max` | number | 最大采集或返回数量。 |
| `price.currency` | number | 币种。 |
| `price.priceType` | number | 价格。 |
| `price.promoLabel` | number | promoLabel 字段。 |
| `quantityPrices` | number | 价格。 |
| `quantityPrices.quantityRange` | number | quantityRange 字段。 |
| `quantityPrices.quantityMin` | number | quantityMin 字段。 |
| `quantityPrices.quantityMax` | number | quantityMax 字段。 |
| `quantityPrices.price` | number | 价格。 |
| `images` | array | 图片列表。 |
| `province` | string | province 字段。 |
| `city` | string | city 字段。 |
| `orderCount` | number | 排序方式。 |
| `soldDisplay` | boolean | soldDisplay 字段。 |
| `returnRate` | string | returnRate 字段。 |
| `repurchaseRate` | boolean | repurchaseRate 字段。 |
| `offerRepurchaseRate` | boolean | offerRepurchaseRate 字段。 |
| `isPromoted` | boolean | 是否启用该选项。 |
| `block` | string | block 字段。 |
| `tags` | array | tags 字段。 |
| `serviceTags` | array | serviceTags 字段。 |
| `promotionTags` | array | promotionTags 字段。 |
| `supplier` | string | supplier 字段。 |
| `supplier.memberId` | number | ID 标识。 |
| `supplier.companyName` | string | companyName 字段。 |
| `supplier.shopUrl` | string | 链接地址。 |
| `supplier.loginId` | number | ID 标识。 |
| `supplier.tpYear` | string | tpYear 字段。 |
| `supplier.bizType` | string | bizType 字段。 |
| `supplier.supportsDistribution` | boolean | supportsDistribution 字段。 |
| `supplier.isFactoryInspected` | boolean | 是否启用该选项。 |
| `supplier.isBusinessInspected` | boolean | 是否启用该选项。 |
| `supplier.isSuperFactory` | boolean | 是否启用该选项。 |
| `supplier.inspectionCreditUrl` | string | 链接地址。 |
| `supplier.sameDesignUrl` | string | 链接地址。 |
| `supplier.scores` | number | 评分。 |
| `supplier.scores.composite` | number | composite 字段。 |
| `supplier.scores.goods` | number | goods 字段。 |
| `supplier.scores.logistics` | number | logistics 字段。 |
| `supplier.scores.dispute` | number | dispute 字段。 |
| `supplier.scores.return` | number | return 字段。 |
| `supplier.scores.consultation` | number | consultation 字段。 |
| `supplier.flags` | string | flags 字段。 |
| `supplier.flags.isChtMember` | boolean | 是否启用该选项。 |
| `supplier.flags.isIndustrySeller` | boolean | 是否启用该选项。 |
| `supplier.flags.isEaseBuyDealer` | boolean | 是否启用该选项。 |
| `supplier.flags.isFactoryDealer` | boolean | 是否启用该选项。 |
| `supplier.flags.isSuperFactory` | boolean | 是否启用该选项。 |
| `supplier.flags.isTpFactory` | boolean | 是否启用该选项。 |
| `supplier.flags.isShiliFactory` | boolean | 是否启用该选项。 |
| `supplier.flags.isSiliCertifiedBrand` | boolean | 是否启用该选项。 |
| `supplier.flags.isFactory` | boolean | 是否启用该选项。 |
| `supplier.flags.isTp` | boolean | 是否启用该选项。 |
| `supplier.flags.isHyper` | boolean | 是否启用该选项。 |
| `supplier.flags.isBrandPlus` | boolean | 是否启用该选项。 |
| `supplier.flags.isProcessingTag` | boolean | 是否启用该选项。 |
| `supplier.flags.isSmt` | boolean | 是否启用该选项。 |
| `supplier.flags.isImall` | boolean | 是否启用该选项。 |
| `supplier.flags.isFullOnline` | boolean | 是否启用该选项。 |
| `supplier.flags.isTuoguan` | boolean | 是否启用该选项。 |
| `supplier.flags.isYuantouFlagship` | boolean | 是否启用该选项。 |
| `supplier.featureBadge` | string | featureBadge 字段。 |
| `supplier.userId` | number | ID 标识。 |
| `supplier.videos` | number | videos 字段。 |
| `supplier.foundedYear` | string | foundedYear 字段。 |
| `supplier.sellerType` | string | 卖家信息。 |
| `supplier.isOnline` | boolean | 是否启用该选项。 |
| `supplier.fans` | string | fans 字段。 |
| `supplier.mainCategory` | string | 分类。 |
| `supplier.address` | string | address 字段。 |
| `supplier.coordinates` | string | coordinates 字段。 |
| `supplier.rank` | number | rank 字段。 |
| `supplier.rank.text` | string | 文本内容。 |
| `supplier.rank.url` | string | 链接地址。 |
| `supplier.rank.type` | number | 采集模式。 |
| `supplier.certification` | string | certification 字段。 |
| `supplier.certification.type` | string | 采集模式。 |
| `supplier.certification.number` | number | 数量。 |
| `supplier.certification.reportUrl` | string | 链接地址。 |
| `supplier.legalCompanyName` | string | legalCompanyName 字段。 |
| `supplier.originMerchant` | string | originMerchant 字段。 |
| `supplier.originMerchant.type` | string | 采集模式。 |
| `supplier.originMerchant.description` | string | 描述。 |
| `supplier.originMerchant.url` | string | 链接地址。 |
| `supplier.imUrl` | string | 链接地址。 |
| `supplier.factoryTags` | array | factoryTags 字段。 |
| `sameDesignUrl` | string | 链接地址。 |
| `sourceKeyword` | string | sourceKeyword 字段。 |
| `scrapedAt` | string | scrapedAt 字段。 |
| `specs` | string | specs 字段。 |
| `specs.name` | string | 名称。 |
| `specs.value` | string | value 字段。 |
| `videoUrl` | string | 链接地址。 |
| `dropship` | string | dropship 字段。 |
| `dropship.enabled` | boolean | enabled 字段。 |
| `dropship.consignPrice` | number | 价格。 |
| `dropship.consignPriceTiers` | number | 价格。 |
| `dropship.channels` | string | channels 字段。 |
| `dropship.channelDetails` | string | channelDetails 字段。 |
| `dropship.protections` | string | protections 字段。 |
| `dropship.downstreamPerformance` | string | downstreamPerformance 字段。 |
| `dropship.metrics` | string | metrics 字段。 |
| `dropship.metrics.orders30d` | string | 排序方式。 |
| `dropship.metrics.orders7d` | string | 排序方式。 |
| `dropship.metrics.pickupRate48h` | string | pickupRate48h 字段。 |
| `dropship.metrics.pickupRate24h` | string | pickupRate24h 字段。 |
| `dropship.metrics.distributorCount` | number | 数量。 |
| `dropship.metrics.downstreamStoreCount` | number | 店铺信息。 |
| `dropship.metrics.publishDate` | boolean | 时间或日期。 |
| `shipping` | string | shipping 字段。 |
| `shipping.deliveryHours` | string | deliveryHours 字段。 |
| `shipping.deliveryDays` | string | deliveryDays 字段。 |
| `shipping.carrier` | string | carrier 字段。 |
| `shipping.logisticsText` | boolean | logisticsText 字段。 |
| `shipping.unitWeight` | string | unitWeight 字段。 |
| `shipping.location` | string | location 字段。 |
| `shipping.postFee` | string | postFee 字段。 |
| `shipping.isFreeShipping` | boolean | 是否启用该选项。 |
| `shipping.freeShippingThreshold` | string | freeShippingThreshold 字段。 |
| `shipping.protectionInfos` | string | protectionInfos 字段。 |
| `shipping.protectionInfos.name` | string | 名称。 |
| `shipping.protectionInfos.code` | string | code 字段。 |
| `shipping.protectionInfos.description` | string | 描述。 |
| `shipping.templateRemark` | string | templateRemark 字段。 |
| `shipping.locationCode` | string | locationCode 字段。 |
| `categoryId` | number | 分类。 |
| `topCategoryId` | number | 分类。 |
| `categoryName` | string | 分类。 |
| `categoryPath` | string | 分类。 |
| `unit` | string | unit 字段。 |
| `saledCount` | number | 数量。 |
| `saledCountStr` | number | 数量。 |
| `winportUrl` | string | 链接地址。 |
| `descriptionUrl` | string | 链接地址。 |
| `isOutOfStock` | number | 是否启用该选项。 |
| `isCrossBorderTrade` | boolean | 排序方式。 |
| `wantBuyCount` | number | 数量。 |
| `recentSoldCount` | number | 数量。 |
| `stock` | number | 库存信息。 |
| `minOrderQuantity` | number | 排序方式。 |
| `supportsMix` | string | supportsMix 字段。 |
| `mixWholesale` | string | mixWholesale 字段。 |
| `serviceLabels` | string | serviceLabels 字段。 |
| `skuImages` | array | ID 标识。 |
| `promotions` | string | promotions 字段。 |
| `promotions.type` | string | 采集模式。 |
| `promotions.name` | string | 名称。 |
| `promotions.label` | string | label 字段。 |
| `promotions.activityId` | number | ID 标识。 |
| `promotions.url` | string | 链接地址。 |
| `promotions.countdown` | number | 数量。 |
| `promotions.originalPriceRange` | number | 价格。 |
| `productFlags` | string | productFlags 字段。 |
| `productFlags.isSkuOffer` | boolean | 是否启用该选项。 |
| `productFlags.isPreSell` | boolean | 是否启用该选项。 |
| `productFlags.isConsignMarket` | boolean | 是否启用该选项。 |
| `productFlags.isFreeSample` | boolean | 是否启用该选项。 |
| `productFlags.isBuyerProtection` | boolean | 是否启用该选项。 |
| `productFlags.isWeChatSupply` | boolean | 是否启用该选项。 |
| `productFlags.isCrossBorder` | boolean | 排序方式。 |
| `productFlags.isOnePiece` | boolean | 是否启用该选项。 |
| `productFlags.isWholesale` | boolean | 是否启用该选项。 |
| `productFlags.isToTikTok` | boolean | 是否启用该选项。 |
| `productFlags.isToKuaiShou` | boolean | 是否启用该选项。 |
| `productFlags.isSupportMix` | boolean | 是否启用该选项。 |
| `productFlags.hasRelationOffer` | boolean | 是否启用该选项。 |
| `productFlags.isChtSingleOffer` | boolean | 是否启用该选项。 |
| `productFlags.isDetailForbidden` | number | 是否启用该选项。 |
| `productFlags.supportsCustomization` | string | supportsCustomization 字段。 |
| `unitWeight` | string | unitWeight 字段。 |
| `purchaseLimits` | boolean | 最大采集或返回数量。 |
| `purchaseLimits.personalLimit` | boolean | 最大采集或返回数量。 |
| `purchaseLimits.promotionLimit` | boolean | 最大采集或返回数量。 |
| `supportsSampling` | string | supportsSampling 字段。 |
| `customization` | string | customization 字段。 |

## 使用要点

- 本接口适合：1688 批发商品、供应商、MOQ、价格与销量。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/1688-wholesale-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sortBy": "relevance", "keywords": ["phone case"], "maxResults": 10}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。

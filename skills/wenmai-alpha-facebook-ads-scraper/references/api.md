# Wenmai Alpha Facebook Ads Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/facebook-ads-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_facebook_ads_scraper`
- **接口说明**：facebook-ads-scraper
- **脚本入口**：`scripts/alpha_facebook_ads_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `startUrls` | array | 是 | 页面链接列表。 |
| `resultsLimit` | integer | 否 | 最大采集或返回数量。 |
| `onlyTotal` | boolean | 否 | 是否启用该选项。 |
| `includeAboutPage` | boolean | 否 | 是否启用该选项。 |
| `isDetailsPerAd` | boolean | 否 | 是否启用该选项。 |
| `enrichWithEcommerceData` | boolean | 否 | 是否使用广告落地页补充实时商品与价格信息。设为 `true` 后会启用单独计费的电商信息增强能力；仅在用户明确要求时使用。 |
| `activeStatus` | string | 否 | 状态。可选值：active、inactive。 |
| `sorting` | string | 否 | 排序方式。可选值：total_impressions、relevancy_monthly_grouped。 |
| `onlyAdsNewerThan` | string | 否 | 是否启用该选项。 |
| `onlyAdsOlderThan` | string | 否 | 是否启用该选项。 |

### 额外计费提醒

`enrichWithEcommerceData: true` 会启用单独计费的电商信息增强能力。普通广告采集请求应省略该参数或保持 `false`。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "sorting": "relevancy_monthly_grouped",
  "onlyTotal": false,
  "startUrls": [
    {
      "url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&is_targeted_country=false&media_type=all&search_type=keyword_unordered&q=nike"
    }
  ],
  "activeStatus": "active",
  "resultsLimit": 5
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `inputUrl` | string | 链接地址。 |
| `pageInfo` | object | pageInfo 字段。 |
| `pageInfo.adLibrarySystemStatus` | object | 状态。 |
| `pageInfo.adLibrarySystemStatus.systemStatus` | object | 状态。 |
| `pageInfo.adLibrarySystemStatus.systemStatus.status` | string | 状态。 |
| `pageInfo.adLibrarySystemStatus.systemStatus.activeIssues` | array | activeIssues 字段。 |
| `pageInfo.xfbAdLibraryIsCaptchaRequired` | boolean | xfbAdLibraryIsCaptchaRequired 字段。 |
| `pageInfo.page` | string | page 字段。 |
| `pageInfo.adLibraryUser` | string | 作者信息。 |
| `pageID` | string | ID 标识。 |
| `adArchiveID` | string | ID 标识。 |
| `startDateFormatted` | string | 时间或日期。 |
| `endDateFormatted` | string | 时间或日期。 |
| `adArchiveId` | string | ID 标识。 |
| `collationCount` | string | 数量。 |
| `collationId` | string | ID 标识。 |
| `pageId` | string | ID 标识。 |
| `snapshot` | object | snapshot 字段。 |
| `snapshot.brandedContent` | string | 品牌。 |
| `snapshot.pageId` | string | ID 标识。 |
| `snapshot.pageIsDeleted` | boolean | pageIsDeleted 字段。 |
| `snapshot.pageProfileUri` | string | 作者信息。 |
| `snapshot.rootResharedPost` | string | rootResharedPost 字段。 |
| `snapshot.byline` | string | byline 字段。 |
| `snapshot.disclaimerLabel` | string | disclaimerLabel 字段。 |
| `snapshot.pageName` | string | pageName 字段。 |
| `snapshot.pageProfilePictureUrl` | string | 链接地址。 |
| `snapshot.event` | string | event 字段。 |
| `snapshot.caption` | string | 标题。 |
| `snapshot.ctaText` | string | ctaText 字段。 |
| `snapshot.cards` | array | cards 字段。 |
| `snapshot.body` | object | body 字段。 |
| `snapshot.body.text` | string | 文本内容。 |
| `snapshot.ctaType` | string | ctaType 字段。 |
| `snapshot.displayFormat` | string | displayFormat 字段。 |
| `snapshot.linkDescription` | string | 描述。 |
| `snapshot.linkUrl` | string | 链接地址。 |
| `snapshot.images` | array | 图片列表。 |
| `snapshot.images.imageCrops` | array | imageCrops 字段。 |
| `snapshot.images.originalImageUrl` | string | 链接地址。 |
| `snapshot.images.resizedImageUrl` | string | 链接地址。 |
| `snapshot.images.watermarkedResizedImageUrl` | string | 链接地址。 |
| `snapshot.pageCategories` | array | pageCategories 字段。 |
| `snapshot.pageLikeCount` | integer | 数量。 |
| `snapshot.title` | string | 标题。 |
| `snapshot.videos` | array | videos 字段。 |
| `snapshot.isReshared` | boolean | 是否启用该选项。 |
| `snapshot.extraLinks` | array | extraLinks 字段。 |
| `snapshot.extraTexts` | array | extraTexts 字段。 |
| `snapshot.extraImages` | array | extraImages 字段。 |
| `snapshot.extraVideos` | array | extraVideos 字段。 |
| `snapshot.countryIsoCode` | string | 国家或站点。 |
| `snapshot.brazilTaxId` | string | ID 标识。 |
| `snapshot.additionalInfo` | string | additionalInfo 字段。 |
| `snapshot.ecCertificates` | array | ecCertificates 字段。 |
| `isActive` | boolean | 是否启用该选项。 |
| `hasUserReported` | boolean | 是否启用该选项。 |
| `reportCount` | string | 数量。 |
| `menuItems` | array | menuItems 字段。 |
| `stateMediaRunLabel` | string | stateMediaRunLabel 字段。 |
| `pageIsDeleted` | boolean | pageIsDeleted 字段。 |
| `pageName` | string | pageName 字段。 |
| `impressionsWithIndex` | object | impressionsWithIndex 字段。 |
| `impressionsWithIndex.impressionsText` | string | impressionsText 字段。 |
| `impressionsWithIndex.impressionsIndex` | integer | impressionsIndex 字段。 |
| `gatedType` | string | gatedType 字段。 |
| `categories` | array | categories 字段。 |
| `isAaaEligible` | boolean | 是否启用该选项。 |
| `containsDigitalCreatedMedia` | boolean | containsDigitalCreatedMedia 字段。 |
| `reachEstimate` | string | reachEstimate 字段。 |
| `currency` | string | 币种。 |
| `spend` | string | spend 字段。 |
| `endDate` | integer | 时间或日期。 |
| `publisherPlatform` | array | publisherPlatform 字段。 |
| `startDate` | integer | 时间或日期。 |
| `containsSensitiveContent` | boolean | containsSensitiveContent 字段。 |
| `totalActiveTime` | integer | 时间或日期。 |
| `regionalRegulationData` | object | regionalRegulationData 字段。 |
| `regionalRegulationData.finserv` | object | finserv 字段。 |
| `regionalRegulationData.finserv.isDeemedFinserv` | boolean | 是否启用该选项。 |
| `regionalRegulationData.finserv.isLimitedDelivery` | boolean | 最大采集或返回数量。 |
| `regionalRegulationData.twAntiScam` | object | twAntiScam 字段。 |
| `regionalRegulationData.twAntiScam.isLimitedDelivery` | boolean | 最大采集或返回数量。 |
| `hideDataStatus` | string | 状态。 |
| `fevInfo` | string | fevInfo 字段。 |
| `adId` | string | ID 标识。 |
| `targetedOrReachedCountries` | array | 数量。 |

## 使用要点

- 本接口适合：Facebook/Meta 广告库素材。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/facebook-ads-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sorting": "relevancy_monthly_grouped", "onlyTotal": false, "startUrls": [{"url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&is_targeted_country=false&media_type=all&search_type=keyword_unordered&q=nike"}], "activeStatus": "active", "resultsLimit": 5}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。

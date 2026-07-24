# Wenmai Alpha Amazon Reviews Extractor API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/amazon-reviews-extractor`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_amazon_reviews_extractor`
- **接口说明**：Amazon Reviews Extractor
- **脚本入口**：`scripts/alpha_amazon_reviews_extractor.py`，脚本参数即标准 API POST Body JSON

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
| `personal_data` | boolean | 否 | personal_data 字段。 |
| `products` | array | 是 | products 字段。 |
| `limit` | integer | 否 | 最大采集或返回数量。 |
| `sort` | string | 否 | 排序方式。可选值：helpful、recent。 |
| `stars` | array<string> | 否 | stars 字段。 |
| `all_stars` | boolean | 否 | all_stars 字段。 |
| `rating` | string | 否 | 评分。可选值：all、five_star、four_star、three_star、two_star、one_star、positive、critical。 |
| `keywords` | array | 否 | 搜索关键词列表。 |
| `avp_reviews` | boolean | 否 | 评论列表。 |
| `include_variants` | boolean | 否 | 是否启用该选项。 |
| `start_date` | string | 否 | 时间或日期。 |
| `end_date` | string | 否 | 时间或日期。 |
| `scrape_image_reviews` | boolean | 否 | 评论列表。 |
| `scrape_video_reviews` | boolean | 否 | 评论列表。 |
| `region` | string | 否 | 国家或站点。可选值：amazon.com、amazon.ca、amazon.de、amazon.fr、amazon.co.uk、amazon.it、amazon.es、amazon.com.au、amazon.co.jp、amazon.com.br、amazon.com.mx、amazon.nl、amazon.ie、amazon.se、amazon.com.tr、amazon.ae、amazon.sg、amazon.sa、amazon.pl、amazon.com.be、amazon.eg、amazon.in。 |
| `language` | string | 否 | 语言代码。可选值：all、en、es、fr、de、pt、it、nl、pl、sv、cs、zh_CN、zh_TW、ja、ko、ar、tr。 |

## 请求示例

脚本入参示例：

```json
{
  "sort": "helpful",
  "limit": 3,
  "rating": "all",
  "region": "amazon.com",
  "keywords": [
    "keyboard"
  ],
  "language": "all",
  "products": [
    "https://www.amazon.com/Logitech-LIGHTSPEED-Wireless-Gaming-Mouse/product-reviews/B07CMS5Q6P/ref=cm_cr_getr_mb_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2&formatType=current_format",
    "B07MVJZQTC"
  ],
  "all_stars": false,
  "avp_reviews": false,
  "personal_data": false,
  "include_variants": true,
  "scrape_image_reviews": true,
  "scrape_video_reviews": true
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `reviewId` | number | ID 标识。 |
| `productAsin` | string | ID 标识。 |
| `profileName` | string | 作者信息。 |
| `profileId` | number | ID 标识。 |
| `profilePhoto` | string | 作者信息。 |
| `rating` | number | 评分。 |
| `verifiedPurchase` | boolean | verifiedPurchase 字段。 |
| `vineReview` | string | 评论列表。 |
| `reviewTitle` | string | 评论列表。 |
| `reviewedIn` | string | 评论列表。 |
| `reviewDate` | string | 时间或日期。 |
| `reviewText` | string | 评论列表。 |
| `language` | string | 语言代码。 |
| `country` | number | 国家或站点。 |
| `images` | array | 图片列表。 |
| `videos` | number | videos 字段。 |
| `variantSpecs` | array | variantSpecs 字段。 |
| `variantAsin` | string | ID 标识。 |
| `helpfulVoteCount` | number | 数量。 |
| `reviewUrl` | string | 链接地址。 |
| `reviewsAISummary` | number | 评论列表。 |
| `aspects` | string | aspects 字段。 |
| `aspects.aspectName` | string | aspectName 字段。 |
| `aspects.aspectSentiment` | string | 时间或日期。 |
| `aspects.aspectMention` | string | aspectMention 字段。 |
| `aspects.aspectMentionPositive` | string | aspectMentionPositive 字段。 |
| `aspects.aspectMentionNegative` | string | aspectMentionNegative 字段。 |
| `aspects.aspectSummary` | string | aspectSummary 字段。 |
| `productTitle` | string | productTitle 字段。 |
| `productUrl` | string | 链接地址。 |
| `sellerName` | string | 卖家信息。 |
| `sellerProfileUrl` | string | 链接地址。 |
| `averageRating` | number | 评分。 |
| `totalRatings` | number | 评分。 |
| `ratingSummary` | number | 评分。 |
| `ratingSummary.five_stars` | number | five_stars 字段。 |
| `ratingSummary.four_stars` | number | four_stars 字段。 |
| `ratingSummary.three_stars` | number | three_stars 字段。 |
| `ratingSummary.two_stars` | number | two_stars 字段。 |
| `ratingSummary.one_star` | number | one_star 字段。 |
| `scrapedAt` | string | scrapedAt 字段。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/amazon-reviews-extractor" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sort": "helpful", "limit": 3, "rating": "all", "region": "amazon.com", "keywords": ["keyboard"], "language": "all", "products": ["https://www.amazon.com/Logitech-LIGHTSPEED-Wireless-Gaming-Mouse/product-reviews/B07CMS5Q6P/ref=cm_cr_getr_mb_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2&formatType=current_format", "B07MVJZQTC"], "all_stars": false, "avp_reviews": false, "personal_data": false, "include_variants": true, "scrape_image_reviews": true, "scrape_video_reviews": true}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

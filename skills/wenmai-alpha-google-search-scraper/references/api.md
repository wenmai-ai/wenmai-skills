# Wenmai Alpha Google Search Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/google-search-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_google_search_scraper`
- **接口说明**：Google Search Results Scraper
- **脚本入口**：`scripts/alpha_google_search_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `queries` | string | 是 | 搜索关键词列表。 |
| `maxPagesPerQuery` | integer | 否 | 最大采集或返回数量。 |
| `aiOverview` | object | 否 | Google AI Overview 配置。启用内部开关后会单独计费；仅在用户明确要求时传入。 |
| `aiModeSearch` | object | 否 | Google AI Mode 配置。启用内部开关后会单独计费；仅在用户明确要求时传入。 |
| `geminiSearch` | object | 否 | Gemini 搜索配置，完整结构见下方。只有 `enableGemini` 为 `true` 时才启用该能力并单独计费。 |
| `geminiSearch.enableGemini` | boolean | 否 | 是否启用 Gemini 搜索。默认或普通搜索使用 `false`；设为 `true` 后单独计费。 |
| `perplexitySearch` | object | 否 | Perplexity 搜索配置，完整结构见下方。只有 `enablePerplexity` 为 `true` 时才启用该能力并单独计费。 |
| `perplexitySearch.enablePerplexity` | boolean | 否 | 是否启用 Perplexity 搜索。默认或普通搜索使用 `false`；设为 `true` 后单独计费。 |
| `perplexitySearch.returnImages` | boolean | 否 | 是否在 Perplexity 搜索结果中返回图片；仅在启用 Perplexity 搜索时生效。 |
| `perplexitySearch.returnRelatedQuestions` | boolean | 否 | 是否在 Perplexity 搜索结果中返回相关问题；仅在启用 Perplexity 搜索时生效。 |
| `chatGptSearch` | object | 否 | ChatGPT 搜索配置，完整结构见下方。只有 `enableChatGpt` 为 `true` 时才启用该能力并单独计费。 |
| `chatGptSearch.enableChatGpt` | boolean | 否 | 是否启用 ChatGPT 搜索。默认或普通搜索使用 `false`；设为 `true` 后单独计费。 |
| `copilotSearch` | object | 否 | Copilot 搜索配置，完整结构见下方。只有 `enableCopilot` 为 `true` 时才启用该能力并单独计费。 |
| `copilotSearch.enableCopilot` | boolean | 否 | 是否启用 Copilot 搜索。默认或普通搜索使用 `false`；设为 `true` 后单独计费。 |
| `maximumLeadsEnrichmentRecords` | integer | 否 | 每个域名最多补全的商机记录数。大于 `0` 时会启用单独计费的商机补全能力。 |
| `leadsEnrichmentDepartments` | array<string> | 否 | leadsEnrichmentDepartments 字段。 |
| `verifyLeadsEnrichmentEmails` | boolean | 否 | 是否验证补全后的邮箱。设为 `true` 后会启用单独计费的邮箱验证能力，且需要先启用商机补全。 |
| `linkProspecting` | object | 否 | 链接拓展配置。传入有效配置后会启用单独计费的网页抓取与链接拓展能力。 |
| `focusOnPaidAds` | boolean | 否 | 是否启用付费广告结果提取。设为 `true` 后会单独计费。 |
| `countryCode` | string | 否 | 国家或站点。可选值：af、al、dz、as、ad、ao、ai、aq、ag、ar、am、aw、au、at、az、bs、bh、bd、bb、by、be、bz、bj、bm、bt、bo、ba、bw、bv、br、io、bn、bg、bf、bi、kh、cm、ca、cv、ky、cf、td、cl、cn、cx、cc、co、km、cg、cd、ck、cr、ci、hr、cu、cy、cz、dk、dj、dm、do、ec、eg、sv、gq、er、ee、et、fk、fo、fj、fi、fr、gf、pf、tf、ga、gm、ge、de、等。 |
| `searchLanguage` | string | 否 | 语言代码。可选值：ar、bg、ca、cs、da、de、el、en、es、et、fi、fr、hr、hu、id、is、it、iw、ja、ko、lt、lv、nl、no、pl、pt、ro、ru、sk、sl、sr、sv、th、tr、zh-CN、zh-TW。 |
| `languageCode` | string | 否 | 语言代码。可选值：af、sq、sm、ar、az、eu、be、bn、bh、bs、bg、ca、zh-CN、zh-TW、hr、cs、da、nl、en、eo、et、fo、fi、fr、fy、gl、ka、de、el、gu、iw、hi、hu、is、id、ia、ga、it、ja、jw、kn、ko、la、lv、lt、mk、ms、ml、mt、mr、ne、no、nn、oc、fa、pl、pt-BR、pt-PT、pa、ro、ru、gd、sr、si、sk、sl、es、su、sw、sv、tl、ta、te、th、ti、tr、uk、ur、uz、vi、等。 |
| `locationUule` | string | 否 | locationUule 字段。 |
| `forceExactMatch` | boolean | 否 | forceExactMatch 字段。 |
| `site` | string | 否 | site 字段。 |
| `relatedToSite` | string | 否 | relatedToSite 字段。 |
| `wordsInTitle` | array<string> | 否 | wordsInTitle 字段。 |
| `wordsInText` | array<string> | 否 | wordsInText 字段。 |
| `wordsInUrl` | array<string> | 否 | 链接地址。 |
| `quickDateRange` | string | 否 | 时间或日期。 |
| `beforeDate` | string | 否 | 时间或日期。 |
| `afterDate` | string | 否 | 时间或日期。 |
| `fileTypes` | array<string> | 否 | fileTypes 字段。 |
| `mobileResults` | boolean | 否 | mobileResults 字段。 |
| `includeUnfilteredResults` | boolean | 否 | 是否启用该选项。 |
| `saveHtml` | boolean | 否 | saveHtml 字段。 |
| `saveHtmlToKeyValueStore` | boolean | 否 | 店铺信息。 |
| `includeIcons` | boolean | 否 | 是否启用该选项。 |

### 收费对象参数结构

以下为四个可选搜索对象的完整关闭状态。普通 Google 搜索应直接省略这些对象；如需显式传入，保持对应 `enable*` 字段为 `false` 不会启用该收费能力。

```json
{
  "geminiSearch": {
    "enableGemini": false
  },
  "perplexitySearch": {
    "enablePerplexity": false,
    "returnImages": false,
    "returnRelatedQuestions": false
  },
  "chatGptSearch": {
    "enableChatGpt": false
  },
  "copilotSearch": {
    "enableCopilot": false
  }
}
```

### 额外计费提醒

上述标记的 AI 搜索、商机补全、邮箱验证、链接拓展和广告提取能力均为显式选择项。普通 Google 搜索请求应完全省略这些参数，不要仅为“结果更丰富”而自动开启。调用前应提醒用户相关能力需要单独计费。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "queries": "best wireless earbuds",
  "countryCode": "us",
  "languageCode": "en",
  "searchLanguage": "en",
  "maxPagesPerQuery": 1
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `searchQuery` | object | 搜索关键词。 |
| `searchQuery.term` | string | 搜索关键词。 |
| `searchQuery.url` | string | 链接地址。 |
| `searchQuery.device` | string | device 字段。 |
| `searchQuery.page` | integer | page 字段。 |
| `searchQuery.type` | string | 采集模式。 |
| `searchQuery.domain` | string | domain 字段。 |
| `searchQuery.countryCode` | string | 国家或站点。 |
| `searchQuery.languageCode` | string | 语言代码。 |
| `searchQuery.locationUule` | string | locationUule 字段。 |
| `searchQuery.resultsPerPage` | integer | resultsPerPage 字段。 |
| `url` | string | 链接地址。 |
| `hasNextPage` | boolean | 是否启用该选项。 |
| `serpProviderCode` | string | serpProviderCode 字段。 |
| `resultsTotal` | string | 数量。 |
| `relatedQueries` | array | relatedQueries 字段。 |
| `relatedQueries.title` | string | 标题。 |
| `relatedQueries.url` | string | 链接地址。 |
| `paidResults` | array | paidResults 字段。 |
| `paidProducts` | array | paidProducts 字段。 |
| `organicResults` | array | organicResults 字段。 |
| `organicResults.title` | string | 标题。 |
| `organicResults.websiteTitle` | string | websiteTitle 字段。 |
| `organicResults.url` | string | 链接地址。 |
| `organicResults.displayedUrl` | string | 链接地址。 |
| `organicResults.description` | string | 描述。 |
| `organicResults.date` | string | 时间或日期。 |
| `organicResults.emphasizedKeywords` | array | emphasizedKeywords 字段。 |
| `organicResults.siteLinks` | array | siteLinks 字段。 |
| `organicResults.productInfo` | object | productInfo 字段。 |
| `organicResults.type` | string | 采集模式。 |
| `organicResults.position` | integer | position 字段。 |
| `suggestedResults` | array | suggestedResults 字段。 |
| `peopleAlsoAsk` | array | peopleAlsoAsk 字段。 |
| `peopleAlsoAsk.answer` | string | answer 字段。 |
| `peopleAlsoAsk.question` | string | question 字段。 |
| `peopleAlsoAsk.title` | string | 标题。 |
| `peopleAlsoAsk.url` | string | 链接地址。 |
| `peopleAlsoAsk.date` | string | 时间或日期。 |
| `aiOverview` | object | aiOverview 字段。 |
| `aiOverview.type` | string | 采集模式。 |
| `aiOverview.content` | string | 文本内容。 |
| `aiOverview.sources` | array | sources 字段。 |
| `aiOverview.sources.url` | string | 链接地址。 |
| `aiOverview.sources.title` | string | 标题。 |
| `aiOverview.sources.description` | string | 描述。 |
| `customData` | string | customData 字段。 |
| `htmlSnapshotUrl` | string | 链接地址。 |

## 使用要点

- 本接口适合：Google Search / SERP / Trends。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/google-search-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"queries": "best wireless earbuds", "countryCode": "us", "languageCode": "en", "searchLanguage": "en", "maxPagesPerQuery": 1}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。

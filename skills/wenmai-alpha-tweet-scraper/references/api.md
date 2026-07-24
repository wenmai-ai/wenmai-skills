# Wenmai Alpha Tweet Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/tweet-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_tweet_scraper`
- **接口说明**：tweet-scraper
- **脚本入口**：`scripts/alpha_tweet_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `startUrls` | array | 否 | 页面链接列表。 |
| `searchTerms` | array | 否 | 搜索关键词列表。 |
| `twitterHandles` | array | 否 | twitterHandles 字段。 |
| `conversationIds` | array | 否 | conversationIds 字段。 |
| `maxItems` | integer | 否 | 最大采集或返回数量。 |
| `sort` | string | 否 | 排序方式。可选值：Top、Latest、Latest + Top。 |
| `tweetLanguage` | string | 否 | 语言代码。可选值：ab、aa、af、ak、sq、am、ar、an、hy、as、av、ae、ay、az、bm、ba、eu、be、bn、bi、bs、br、bg、my、ca、ch、ce、ny、zh、cu、cv、kw、co、cr、hr、cs、da、dv、nl、dz、en、eo、et、ee、fo、fj、fi、fr、fy、ff、gd、gl、lg、ka、de、el、kl、gn、gu、ht、ha、he、hz、hi、ho、hu、is、io、ig、id、ia、ie、iu、ik、ga、it、ja、jv、kn、kr、等。 |
| `onlyVerifiedUsers` | boolean | 否 | 是否启用该选项。 |
| `onlyTwitterBlue` | boolean | 否 | 是否启用该选项。 |
| `onlyImage` | boolean | 否 | 是否启用该选项。 |
| `onlyVideo` | boolean | 否 | 是否启用该选项。 |
| `onlyQuote` | boolean | 否 | 是否启用该选项。 |
| `author` | string | 否 | 作者信息。 |
| `inReplyTo` | string | 否 | inReplyTo 字段。 |
| `mentioning` | string | 否 | mentioning 字段。 |
| `geotaggedNear` | string | 否 | geotaggedNear 字段。 |
| `withinRadius` | string | 否 | withinRadius 字段。 |
| `geocode` | string | 否 | geocode 字段。 |
| `placeObjectId` | string | 否 | ID 标识。 |
| `minimumRetweets` | integer | 否 | 最大采集或返回数量。 |
| `minimumFavorites` | integer | 否 | 最大采集或返回数量。 |
| `minimumReplies` | integer | 否 | 最大采集或返回数量。 |
| `start` | string | 否 | 时间或日期。 |
| `end` | string | 否 | 时间或日期。 |
| `includeSearchTerms` | boolean | 否 | 是否启用该选项。 |
| `customMapFunction` | string | 否 | customMapFunction 字段。 |

## 请求示例

脚本入参示例：

```json
{
  "sort": "Latest",
  "maxItems": 3,
  "onlyImage": false,
  "onlyQuote": false,
  "onlyVideo": false,
  "startUrls": [
    "https://twitter.com/apify",
    "https://twitter.com/search?q=apify%20&src=typed_query",
    "https://twitter.com/i/lists/78783491",
    "https://twitter.com/elonmusk/with_replies"
  ],
  "searchTerms": [
    "web scraping",
    "scraping from:apify"
  ],
  "tweetLanguage": "en",
  "minimumReplies": 1,
  "twitterHandles": [
    "elonmusk",
    "taylorswift13"
  ],
  "minimumRetweets": 1,
  "onlyTwitterBlue": false,
  "minimumFavorites": 1,
  "customMapFunction": "(object) => { return {...object} }",
  "onlyVerifiedUsers": false,
  "includeSearchTerms": false
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `type` | string | 采集模式。 |
| `id` | number | ID 标识。 |
| `url` | string | 链接地址。 |
| `twitterUrl` | string | 链接地址。 |
| `text` | string | 文本内容。 |
| `fullText` | string | 文本内容。 |
| `source` | string | source 字段。 |
| `retweetCount` | number | 数量。 |
| `replyCount` | number | 数量。 |
| `likeCount` | number | 数量。 |
| `quoteCount` | number | 数量。 |
| `viewCount` | number | 数量。 |
| `createdAt` | string | 时间或日期。 |
| `lang` | string | 语言代码。 |
| `bookmarkCount` | number | 数量。 |
| `isReply` | boolean | 是否启用该选项。 |
| `inReplyToId` | number | ID 标识。 |
| `conversationId` | number | ID 标识。 |
| `inReplyToUserId` | number | ID 标识。 |
| `inReplyToUsername` | string | 作者信息。 |
| `author` | string | 作者信息。 |
| `author.type` | string | 采集模式。 |
| `author.userName` | string | 作者信息。 |
| `author.url` | string | 链接地址。 |
| `author.twitterUrl` | string | 链接地址。 |
| `author.id` | number | ID 标识。 |
| `author.name` | string | 名称。 |
| `author.isVerified` | boolean | 是否启用该选项。 |
| `author.isBlueVerified` | boolean | 是否启用该选项。 |
| `author.profilePicture` | string | 图片链接。 |
| `author.coverPicture` | string | 图片链接。 |
| `author.description` | string | 描述。 |
| `author.location` | string | location 字段。 |
| `author.followers` | number | followers 字段。 |
| `author.following` | string | following 字段。 |
| `author.protected` | string | protected 字段。 |
| `author.status` | string | 状态。 |
| `author.canDm` | string | canDm 字段。 |
| `author.canMediaTag` | array | canMediaTag 字段。 |
| `author.createdAt` | string | 时间或日期。 |
| `author.entities` | string | entities 字段。 |
| `author.entities.description` | string | 描述。 |
| `author.entities.description.urls` | array | 页面链接列表。 |
| `author.entities.description.urls.display_url` | boolean | 链接地址。 |
| `author.entities.description.urls.expanded_url` | array | 链接地址。 |
| `author.entities.description.urls.indices` | array | indices 字段。 |
| `author.entities.description.urls.url` | array | 链接地址。 |
| `author.fastFollowersCount` | number | 数量。 |
| `author.favouritesCount` | number | 数量。 |
| `author.hasCustomTimelines` | boolean | 是否启用该选项。 |
| `author.isTranslator` | boolean | 是否启用该选项。 |
| `author.mediaCount` | number | 数量。 |
| `author.statusesCount` | number | 数量。 |
| `author.affiliatesHighlightedLabel` | string | affiliatesHighlightedLabel 字段。 |
| `author.possiblySensitive` | string | possiblySensitive 字段。 |
| `extendedEntities` | string | extendedEntities 字段。 |
| `card` | string | card 字段。 |
| `place` | string | place 字段。 |
| `entities` | string | entities 字段。 |
| `isRetweet` | boolean | 是否启用该选项。 |
| `isQuote` | boolean | 是否启用该选项。 |
| `media` | array | 图片列表。 |
| `isConversationControlled` | boolean | 是否启用该选项。 |

## 使用要点

- 本接口适合：X/Twitter 推文、账号和列表。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/tweet-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sort": "Latest", "maxItems": 3, "onlyImage": false, "onlyQuote": false, "onlyVideo": false, "startUrls": ["https://twitter.com/apify", "https://twitter.com/search?q=apify%20&src=typed_query", "https://twitter.com/i/lists/78783491", "https://twitter.com/elonmusk/with_replies"], "searchTerms": ["web scraping", "scraping from:apify"], "tweetLanguage": "en", "minimumReplies": 1, "twitterHandles": ["elonmusk", "taylorswift13"], "minimumRetweets": 1, "onlyTwitterBlue": false, "minimumFavorites": 1, "customMapFunction": "(object) => { return {...object} }", "onlyVerifiedUsers": false, "includeSearchTerms": false}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

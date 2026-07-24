# Wenmai Alpha Tiktok Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/tiktok-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_tiktok_scraper`
- **接口说明**：Tiktok Scraper
- **脚本入口**：`scripts/alpha_tiktok_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `hashtags` | array | 否 | 搜索关键词列表。 |
| `resultsPerPage` | integer | 否 | resultsPerPage 字段。 |
| `profiles` | array | 否 | 作者信息。 |
| `profileScrapeSections` | array<string> | 否 | 作者信息。 |
| `profileSorting` | string | 否 | 排序方式。可选值：latest、popular、oldest。 |
| `excludePinnedPosts` | boolean | 否 | excludePinnedPosts 字段。 |
| `oldestPostDateUnified` | string | 否 | 最早发布日期筛选。传入后会启用单独计费的日期筛选能力。 |
| `newestPostDate` | string | 否 | 最新发布日期筛选。传入后会启用单独计费的日期筛选能力。 |
| `mostDiggs` | integer | 否 | 点赞数上限筛选。传入后会启用单独计费的热度筛选能力。 |
| `leastDiggs` | integer | 否 | 点赞数下限筛选。传入后会启用单独计费的热度筛选能力。 |
| `maxFollowersPerProfile` | integer | 否 | 每个账号最多采集的粉丝数量。大于 0 时会启用单独计费的粉丝数据采集能力。 |
| `maxFollowingPerProfile` | integer | 否 | 每个账号最多采集的关注数量。大于 0 时会启用单独计费的关注数据采集能力。 |
| `searchQueries` | array | 否 | 搜索关键词列表。 |
| `searchSection` | string | 否 | searchSection 字段。可选值：/video、/user。 |
| `maxProfilesPerQuery` | integer | 否 | 最大采集或返回数量。 |
| `videoSearchSorting` | string | 否 | 视频搜索排序。可选值：MOST_RELEVANT、MOST_LIKED、LATEST。显式设置会启用单独计费的搜索排序能力。 |
| `videoSearchDateFilter` | string | 否 | 视频搜索日期筛选。可选值：ALL_TIME、PAST_24_HOURS、PAST_WEEK、PAST_MONTH、LAST_3_MONTHS、LAST_6_MONTHS。使用非默认筛选会启用单独计费的日期筛选能力。 |
| `scrapeRelatedSearchWords` | boolean | 否 | scrapeRelatedSearchWords 字段。 |
| `postURLs` | array | 否 | 页面链接列表。 |
| `scrapeRelatedVideos` | boolean | 否 | scrapeRelatedVideos 字段。 |
| `scrapeAdditionalAuthorMeta` | boolean | 否 | 作者信息。 |
| `shouldDownloadVideos` | boolean | 否 | 是否下载视频。设为 `true` 后会启用单独计费的视频下载能力。 |
| `shouldDownloadCovers` | boolean | 否 | 是否启用该选项。 |
| `shouldDownloadSlideshowImages` | boolean | 否 | 是否启用该选项。 |
| `shouldDownloadAvatars` | boolean | 否 | 是否启用该选项。 |
| `shouldDownloadMusicCovers` | boolean | 否 | 是否启用该选项。 |
| `videoKvStoreIdOrName` | string | 否 | 店铺信息。 |
| `downloadSubtitlesOptions` | string | 否 | 字幕处理方式。可选值：NEVER_DOWNLOAD_SUBTITLES、DOWNLOAD_SUBTITLES、DOWNLOAD_AND_TRANSCRIBE_VIDEOS_WITHOUT_SUBTITLES、TRANSCRIBE_ALL_VIDEOS。后两个转录模式会启用单独计费的转录能力。 |
| `commentsPerPost` | integer | 否 | 每条内容采集的评论数量。大于 0 时会启用单独计费的评论能力。 |
| `topLevelCommentsPerPost` | integer | 否 | 每条内容采集的顶级评论数量。大于 0 时会启用单独计费的评论能力。 |
| `maxRepliesPerComment` | integer | 否 | 每条评论采集的最大回复数。大于 0 时会启用单独计费的评论能力。 |

### 额外计费提醒

上述标记的能力只能在用户明确要求时启用，并应在请求前提醒用户需要单独计费。普通请求应省略这些参数或保持关闭状态。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "searchQueries": [
    "keyboard"
  ],
  "searchSection": "/video",
  "resultsPerPage": 10
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | ID 标识。 |
| `text` | string | 文本内容。 |
| `textLanguage` | string | 语言代码。 |
| `createTime` | number | 时间或日期。 |
| `createTimeISO` | string | 时间或日期。 |
| `isMuted` | boolean | 是否启用该选项。 |
| `webVideoUrl` | string | 链接地址。 |
| `locationCreated` | string | locationCreated 字段。 |
| `isAd` | boolean | 是否启用该选项。 |
| `authorMeta` | object | 作者信息。 |
| `authorMeta.id` | string | ID 标识。 |
| `authorMeta.name` | string | 名称。 |
| `authorMeta.profileUrl` | string | 链接地址。 |
| `authorMeta.verified` | boolean | verified 字段。 |
| `authorMeta.privateAccount` | boolean | 数量。 |
| `authorMeta.nickName` | string | nickName 字段。 |
| `authorMeta.avatar` | string | 图片链接。 |
| `authorMeta.signature` | string | signature 字段。 |
| `authorMeta.bioLink` | string | bioLink 字段。 |
| `authorMeta.region` | string | 国家或站点。 |
| `authorMeta.following` | number | following 字段。 |
| `authorMeta.fans` | number | fans 字段。 |
| `authorMeta.video` | number | video 字段。 |
| `authorMeta.heart` | number | heart 字段。 |
| `authorMeta.digg` | number | digg 字段。 |
| `authorMeta.friends` | number | friends 字段。 |
| `authorMeta.commerceUserInfo` | object | 作者信息。 |
| `authorMeta.commerceUserInfo.commerceUser` | boolean | 作者信息。 |
| `authorMeta.commerceUserInfo.category` | string | 分类。 |
| `authorMeta.isUnderAge18` | boolean | 是否启用该选项。 |
| `authorMeta.roomId` | string | ID 标识。 |
| `authorMeta.ttSeller` | boolean | 卖家信息。 |
| `authorMeta.createTime` | number | 时间或日期。 |
| `authorMeta.followDatasetUrl` | string | 链接地址。 |
| `authorMeta.originalAvatarUrl` | string | 链接地址。 |
| `musicMeta` | object | musicMeta 字段。 |
| `musicMeta.musicName` | string | musicName 字段。 |
| `musicMeta.musicAuthor` | string | 作者信息。 |
| `musicMeta.playUrl` | string | 链接地址。 |
| `musicMeta.coverMediumUrl` | string | 链接地址。 |
| `musicMeta.musicOriginal` | boolean | musicOriginal 字段。 |
| `musicMeta.musicAlbum` | string | musicAlbum 字段。 |
| `musicMeta.musicId` | string | ID 标识。 |
| `musicMeta.originalCoverMediumUrl` | string | 链接地址。 |
| `videoMeta` | object | videoMeta 字段。 |
| `videoMeta.height` | number | height 字段。 |
| `videoMeta.width` | number | width 字段。 |
| `videoMeta.duration` | number | duration 字段。 |
| `videoMeta.coverUrl` | string | 链接地址。 |
| `videoMeta.originalCoverUrl` | string | 链接地址。 |
| `videoMeta.definition` | string | definition 字段。 |
| `videoMeta.format` | string | format 字段。 |
| `videoMeta.subtitleLinks` | array | subtitleLinks 字段。 |
| `videoMeta.subtitleLinks.language` | string | 语言代码。 |
| `videoMeta.subtitleLinks.downloadLink` | string | 是否启用该选项。 |
| `videoMeta.subtitleLinks.tiktokLink` | string | tiktokLink 字段。 |
| `videoMeta.subtitleLinks.source` | string | source 字段。 |
| `videoMeta.subtitleLinks.sourceUnabbreviated` | string | sourceUnabbreviated 字段。 |
| `videoMeta.subtitleLinks.version` | string | version 字段。 |
| `videoMeta.transcriptionLink` | string | transcriptionLink 字段。 |
| `videoMeta.downloadAddr` | string | 是否启用该选项。 |
| `locationMeta` | object | locationMeta 字段。 |
| `locationMeta.address` | string | address 字段。 |
| `locationMeta.city` | string | city 字段。 |
| `locationMeta.cityCode` | string | cityCode 字段。 |
| `locationMeta.countryCode` | string | 国家或站点。 |
| `locationMeta.locationName` | string | locationName 字段。 |
| `locationMeta.locationId` | string | ID 标识。 |
| `mediaUrls` | array<string> | 页面链接列表。 |
| `slideshowImageLinks` | array | slideshowImageLinks 字段。 |
| `slideshowImageLinks.tiktokLink` | string | tiktokLink 字段。 |
| `slideshowImageLinks.downloadLink` | string | 是否启用该选项。 |
| `diggCount` | number | 数量。 |
| `shareCount` | number | 数量。 |
| `playCount` | number | 数量。 |
| `commentCount` | number | 评论列表。 |
| `collectCount` | number | 数量。 |
| `repostCount` | number | 数量。 |
| `mentions` | array<string> | mentions 字段。 |
| `detailedMentions` | array | detailedMentions 字段。 |
| `detailedMentions.id` | string | ID 标识。 |
| `detailedMentions.name` | string | 名称。 |
| `detailedMentions.nickName` | string | nickName 字段。 |
| `detailedMentions.profileUrl` | string | 链接地址。 |
| `detailedMentions.postUrl` | string | 链接地址。 |
| `detailedMentions.secUid` | string | ID 标识。 |
| `hashtags` | array | 搜索关键词列表。 |
| `hashtags.id` | string | ID 标识。 |
| `hashtags.name` | string | 名称。 |
| `hashtags.title` | string | 标题。 |
| `hashtags.cover` | string | 图片链接。 |
| `effectStickers` | array | effectStickers 字段。 |
| `effectStickers.ID` | string | ID 标识。 |
| `effectStickers.name` | string | 名称。 |
| `effectStickers.stickerStats` | object | stickerStats 字段。 |
| `effectStickers.stickerStats.useCount` | number | 数量。 |
| `isSlideshow` | boolean | 是否启用该选项。 |
| `isPinned` | boolean | 是否启用该选项。 |
| `isSponsored` | boolean | 是否启用该选项。 |
| `commentsDatasetUrl` | string | 链接地址。 |
| `url` | string | 链接地址。 |
| `errorCode` | string | errorCode 字段。 |
| `invalidUrls` | array | 页面链接列表。 |
| `comments` | array | 评论列表。 |
| `comments.cid` | string | ID 标识。 |
| `comments.text` | string | 文本内容。 |
| `comments.createTime` | number | 时间或日期。 |
| `comments.createTimeISO` | string | 时间或日期。 |
| `comments.diggCount` | number | 数量。 |
| `comments.replyCommentTotal` | number | 评论列表。 |
| `comments.uid` | string | ID 标识。 |
| `comments.uniqueId` | string | ID 标识。 |
| `comments.repliesToId` | string | ID 标识。 |
| `comments.avatarThumbnail` | string | avatarThumbnail 字段。 |
| `comments.likedByAuthor` | boolean | 作者信息。 |
| `comments.pinnedByAuthor` | boolean | 作者信息。 |
| `comments.mentions` | array<string> | mentions 字段。 |
| `comments.detailedMentions` | array | detailedMentions 字段。 |
| `submittedVideoUrl` | string | 链接地址。 |
| `fromProfileSection` | string | 作者信息。 |
| `searchQuery` | string | 搜索关键词。 |
| `searchHashtag` | object | searchHashtag 字段。 |
| `searchMusic` | object | searchMusic 字段。 |

## 使用要点

- 本接口适合：TikTok 视频、账号、话题和趋势。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/tiktok-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"searchQueries": ["keyboard"], "searchSection": "/video", "resultsPerPage": 10}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。

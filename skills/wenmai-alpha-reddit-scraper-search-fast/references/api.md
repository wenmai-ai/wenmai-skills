# Wenmai Alpha Reddit Scraper Search Fast API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/reddit-scraper-search-fast`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_reddit_scraper_search_fast`
- **接口说明**：Reddit Scraper \| Enterprise Grade
- **脚本入口**：`scripts/alpha_reddit_scraper_search_fast.py`，脚本参数即标准 API POST Body JSON

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
| `queries` | array | 否 | 搜索关键词列表。 |
| `sort` | string | 否 | 排序方式。可选值：relevance、hot、top、new、comments。 |
| `timeframe` | string | 否 | 时间或日期。可选值：all、year、month、week、day、hour。 |
| `subredditName` | string | 否 | subredditName 字段。 |
| `subredditKeywords` | array | 否 | subredditKeywords 字段。 |
| `subredditSort` | string | 否 | 排序方式。可选值：relevance、hot、top、new、comments。 |
| `subredditTimeframe` | string | 否 | 时间或日期。可选值：all、year、month、week、day、hour。 |
| `urls` | array | 否 | 页面链接列表。 |
| `scrapeComments` | boolean | 否 | 评论列表。 |
| `maxComments` | integer | 否 | 最大采集或返回数量。 |
| `dateFrom` | string | 否 | 时间或日期。 |
| `dateTo` | string | 否 | 时间或日期。 |
| `commentDateFrom` | string | 否 | 时间或日期。 |
| `commentDateTo` | string | 否 | 时间或日期。 |
| `forceSortNewForTimeFilteredRuns` | boolean | 否 | 排序方式。 |
| `includeNsfw` | boolean | 否 | 是否启用该选项。 |
| `strictSearch` | boolean | 否 | strictSearch 字段。 |
| `strictTokenFilter` | boolean | 否 | strictTokenFilter 字段。 |
| `maxPosts` | integer | 否 | 最大采集或返回数量。 |
| `maximize_coverage` | boolean | 否 | 最大采集或返回数量。 |
| `sentiment_analysis` | boolean | 否 | 时间或日期。 |
| `content_analysis` | boolean | 否 | content_analysis 字段。 |

## 请求示例

脚本入参示例：

```json
{
  "sort": "relevance",
  "queries": [
    "Cheesecake",
    "Swimming Pool"
  ],
  "maxPosts": 3,
  "timeframe": "all",
  "includeNsfw": false,
  "maxComments": 3,
  "strictSearch": false,
  "subredditSort": "relevance",
  "scrapeComments": false,
  "content_analysis": false,
  "maximize_coverage": false,
  "strictTokenFilter": false,
  "subredditKeywords": [
    "keyboard"
  ],
  "sentiment_analysis": false,
  "subredditTimeframe": "all",
  "forceSortNewForTimeFilteredRuns": false
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `query` | string | 搜索关键词。 |
| `kind` | string | kind 字段。 |
| `id` | string | ID 标识。 |
| `title` | string | 标题。 |
| `body` | string | body 字段。 |
| `sentiment_score` | integer | 时间或日期。 |
| `sentiment_label` | string | 时间或日期。 |
| `sentiment_confidence` | number | 时间或日期。 |
| `sentiment_score_normalized` | number | 时间或日期。 |
| `content_category_label` | string | 分类。 |
| `content_category_path` | array<string> | 分类。 |
| `content_category_confidence` | number | 分类。 |
| `content_category_match_type` | string | 分类。 |
| `post_content_category_label` | string | 分类。 |
| `post_content_category_path` | array<string> | 分类。 |
| `post_content_category_confidence` | number | 分类。 |
| `post_content_category_match_type` | string | 分类。 |
| `author` | string | 作者信息。 |
| `score` | integer | 评分。 |
| `upvote_ratio` | number | upvote_ratio 字段。 |
| `num_comments` | integer | 评论列表。 |
| `subreddit` | string | subreddit 字段。 |
| `created_utc` | string | created_utc 字段。 |
| `url` | string | 链接地址。 |
| `permalink` | string | permalink 字段。 |
| `canonical_url` | string | 链接地址。 |
| `old_reddit_url` | string | 链接地址。 |
| `flair` | string | flair 字段。 |
| `post_hint` | string | post_hint 字段。 |
| `over_18` | boolean | over_18 字段。 |
| `is_self` | boolean | 是否启用该选项。 |
| `spoiler` | boolean | spoiler 字段。 |
| `locked` | boolean | locked 字段。 |
| `is_video` | boolean | 是否启用该选项。 |
| `is_gallery` | boolean | 是否启用该选项。 |
| `hidden` | boolean | hidden 字段。 |
| `edited` | boolean/number | edited 字段。 |
| `archived` | boolean | archived 字段。 |
| `pinned` | boolean | pinned 字段。 |
| `domain` | string | domain 字段。 |
| `thumbnail` | string | 图片链接。 |
| `url_overridden_by_dest` | string | 链接地址。 |
| `num_duplicates` | integer | num_duplicates 字段。 |
| `subreddit_id` | string | ID 标识。 |
| `subreddit_name_prefixed` | string | subreddit_name_prefixed 字段。 |
| `subreddit_subscribers` | integer | subreddit_subscribers 字段。 |
| `media` | object | 图片列表。 |
| `media_metadata` | object | media_metadata 字段。 |
| `gallery_data` | object | gallery_data 字段。 |
| `gallery_images` | array | gallery_images 字段。 |
| `gallery_images.media_id` | string | ID 标识。 |
| `gallery_images.caption` | string | 标题。 |
| `gallery_images.width` | integer | width 字段。 |
| `gallery_images.height` | integer | height 字段。 |
| `gallery_images.url` | string | 链接地址。 |
| `gallery_images.previews` | array<string> | 评论列表。 |
| `media_assets` | array | media_assets 字段。 |
| `media_assets.type` | string | 采集模式。 |
| `media_assets.media_id` | string | ID 标识。 |
| `media_assets.mime_type` | string | mime_type 字段。 |
| `media_assets.original_url` | string | 链接地址。 |
| `media_assets.preview_urls` | array<string> | 页面链接列表。 |
| `age_hours` | number | age_hours 字段。 |
| `retrieved_at` | string | retrieved_at 字段。 |
| `media_type` | string | media_type 字段。 |
| `has_media` | boolean | 是否启用该选项。 |
| `gallery_count` | integer | 数量。 |
| `outbound_url_host` | string | 链接地址。 |
| `title_length` | integer | title_length 字段。 |
| `body_length` | integer | body_length 字段。 |
| `word_count` | integer | 数量。 |
| `score_per_hour` | number | 评分。 |
| `comments_per_hour` | number | 评论列表。 |
| `is_deleted_or_removed` | boolean | 是否启用该选项。 |
| `engagement_total` | integer | 数量。 |
| `comment_to_score_ratio` | number | 评分。 |
| `is_high_engagement` | boolean | 是否启用该选项。 |
| `content_flags` | array<string> | content_flags 字段。 |
| `stickied` | boolean | stickied 字段。 |
| `distinguished` | string | distinguished 字段。 |
| `total_awards_received` | integer | 数量。 |
| `all_awardings` | array | all_awardings 字段。 |
| `gilded` | integer | gilded 字段。 |
| `num_crossposts` | integer | num_crossposts 字段。 |
| `is_original_content` | boolean | 是否启用该选项。 |
| `author_fullname` | string | 作者信息。 |
| `author_flair_text` | string | 作者信息。 |
| `author_premium` | boolean | 作者信息。 |
| `body_html` | string | body_html 字段。 |
| `preview` | object | 评论列表。 |
| `secure_media` | object | secure_media 字段。 |
| `secure_media_embed` | object | secure_media_embed 字段。 |
| `crosspost_parent_list` | array | crosspost_parent_list 字段。 |
| `postId` | string | ID 标识。 |
| `postUrl` | string | 链接地址。 |
| `parentId` | string | ID 标识。 |
| `root_comment_id` | string | ID 标识。 |
| `parent_kind` | string | parent_kind 字段。 |
| `is_submitter` | boolean | 是否启用该选项。 |
| `score_hidden` | boolean | 评分。 |
| `controversiality` | integer | controversiality 字段。 |
| `depth` | integer | depth 字段。 |
| `collapsed` | boolean | collapsed 字段。 |
| `collapsed_reason` | string | collapsed_reason 字段。 |
| `collapsed_because_crowd_control` | boolean | collapsed_because_crowd_control 字段。 |
| `unrepliable_reason` | string | unrepliable_reason 字段。 |

## 使用要点

- 本接口适合：Reddit 搜索、帖子、评论和舆情。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/reddit-scraper-search-fast" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sort": "relevance", "queries": ["Cheesecake", "Swimming Pool"], "maxPosts": 3, "timeframe": "all", "includeNsfw": false, "maxComments": 3, "strictSearch": false, "subredditSort": "relevance", "scrapeComments": false, "content_analysis": false, "maximize_coverage": false, "strictTokenFilter": false, "subredditKeywords": ["keyboard"], "sentiment_analysis": false, "subredditTimeframe": "all", "forceSortNewForTimeFilteredRuns": false}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

# Wenmai SCRAPECREATORS scrapecreators_reddit_search API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/reddit-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_reddit_search`
- **脚本入口**：`modules/search/scripts/search.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `query` | string | 是 | 全站搜索词。 |
| `filter` | string | 否 | posts 或 comments，默认 posts。 |
| `sort` | string | 否 | 排序：relevance、new、top、comment_count。 |
| `timeframe` | string | 否 | 帖子搜索时间范围。 |
| `trim` | boolean | 否 | 为 true 时返回精简字段。不要当默认。 |
| `after` | string | 否 | 上一页响应里的 after。 |

## 请求示例

```json
{
  "query": "gymshark",
  "filter": "posts"
}
```

```bash
python3 modules/search/scripts/search.py '{"query": "gymshark", "filter": "posts"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `posts` | array | 帖子列表。 |
| `posts[].approved_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].subreddit` | string | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `posts[].selftext` | string | 官方字段 `selftext`；官方未单独提供业务说明。 |
| `posts[].author_fullname` | string | 官方字段 `author_fullname`；官方未单独提供业务说明。 |
| `posts[].saved` | boolean | 官方字段 `saved`；官方未单独提供业务说明。 |
| `posts[].mod_reason_title` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].gilded` | integer | 官方字段 `gilded`；官方未单独提供业务说明。 |
| `posts[].clicked` | boolean | 官方字段 `clicked`；官方未单独提供业务说明。 |
| `posts[].title` | string | 标题。 |
| `posts[].link_flair_richtext` | array | 官方示例为空数组，未提供元素结构。 |
| `posts[].subreddit_name_prefixed` | string | 官方字段 `subreddit_name_prefixed`；官方未单独提供业务说明。 |
| `posts[].hidden` | boolean | 官方字段 `hidden`；官方未单独提供业务说明。 |
| `posts[].pwls` | integer | 官方字段 `pwls`；官方未单独提供业务说明。 |
| `posts[].link_flair_css_class` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].downs` | integer | 官方字段 `downs`；官方未单独提供业务说明。 |
| `posts[].thumbnail_height` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].top_awarded_type` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].hide_score` | boolean | 官方字段 `hide_score`；官方未单独提供业务说明。 |
| `posts[].name` | string | 名称。 |
| `posts[].quarantine` | boolean | 官方字段 `quarantine`；官方未单独提供业务说明。 |
| `posts[].link_flair_text_color` | string | 官方字段 `link_flair_text_color`；官方未单独提供业务说明。 |
| `posts[].upvote_ratio` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].author_flair_background_color` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].subreddit_type` | string | 官方字段 `subreddit_type`；官方未单独提供业务说明。 |
| `posts[].ups` | integer | 官方字段 `ups`；官方未单独提供业务说明。 |
| `posts[].total_awards_received` | integer | 官方字段 `total_awards_received`；官方未单独提供业务说明。 |
| `posts[].media_embed` | object | 官方示例为空对象，未提供子字段。 |
| `posts[].thumbnail_width` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].author_flair_template_id` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].is_original_content` | boolean | 官方字段 `is_original_content`；官方未单独提供业务说明。 |
| `posts[].user_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `posts[].secure_media` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].is_reddit_media_domain` | boolean | 官方字段 `is_reddit_media_domain`；官方未单独提供业务说明。 |
| `posts[].is_meta` | boolean | 官方字段 `is_meta`；官方未单独提供业务说明。 |
| `posts[].category` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].secure_media_embed` | object | 官方示例为空对象，未提供子字段。 |
| `posts[].link_flair_text` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].can_mod_post` | boolean | 官方字段 `can_mod_post`；官方未单独提供业务说明。 |
| `posts[].score` | integer | 官方字段 `score`；官方未单独提供业务说明。 |
| `posts[].approved_by` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].is_created_from_ads_ui` | boolean | 官方字段 `is_created_from_ads_ui`；官方未单独提供业务说明。 |
| `posts[].author_premium` | boolean | 官方字段 `author_premium`；官方未单独提供业务说明。 |
| `posts[].thumbnail` | string | 缩略图。 |
| `posts[].edited` | integer | 官方字段 `edited`；官方未单独提供业务说明。 |
| `posts[].author_flair_css_class` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].author_flair_richtext` | array | 官方示例为空数组，未提供元素结构。 |
| `posts[].gildings` | object | 官方示例为空对象，未提供子字段。 |
| `posts[].content_categories` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].is_self` | boolean | 官方字段 `is_self`；官方未单独提供业务说明。 |
| `posts[].mod_note` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].created` | integer | 官方字段 `created`；官方未单独提供业务说明。 |
| `posts[].link_flair_type` | string | 官方字段 `link_flair_type`；官方未单独提供业务说明。 |
| `posts[].wls` | integer | 官方字段 `wls`；官方未单独提供业务说明。 |
| `posts[].removed_by_category` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].banned_by` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].author_flair_type` | string | 官方字段 `author_flair_type`；官方未单独提供业务说明。 |
| `posts[].domain` | string | 域名。 |
| `posts[].allow_live_comments` | boolean | 官方字段 `allow_live_comments`；官方未单独提供业务说明。 |
| `posts[].selftext_html` | string | 官方字段 `selftext_html`；官方未单独提供业务说明。 |
| `posts[].likes` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].suggested_sort` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].banned_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].view_count` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].archived` | boolean | 官方字段 `archived`；官方未单独提供业务说明。 |
| `posts[].no_follow` | boolean | 官方字段 `no_follow`；官方未单独提供业务说明。 |
| `posts[].is_crosspostable` | boolean | 官方字段 `is_crosspostable`；官方未单独提供业务说明。 |
| `posts[].pinned` | boolean | 官方字段 `pinned`；官方未单独提供业务说明。 |
| `posts[].over_18` | boolean | 官方字段 `over_18`；官方未单独提供业务说明。 |
| `posts[].all_awardings` | array | 官方示例为空数组，未提供元素结构。 |
| `posts[].awarders` | array | 官方示例为空数组，未提供元素结构。 |
| `posts[].media_only` | boolean | 官方字段 `media_only`；官方未单独提供业务说明。 |
| `posts[].can_gild` | boolean | 官方字段 `can_gild`；官方未单独提供业务说明。 |
| `posts[].spoiler` | boolean | 官方字段 `spoiler`；官方未单独提供业务说明。 |
| `posts[].locked` | boolean | 官方字段 `locked`；官方未单独提供业务说明。 |
| `posts[].author_flair_text` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].treatment_tags` | array | 官方示例为空数组，未提供元素结构。 |
| `posts[].visited` | boolean | 官方字段 `visited`；官方未单独提供业务说明。 |
| `posts[].removed_by` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].num_reports` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].distinguished` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].subreddit_id` | string | 官方字段 `subreddit_id`；官方未单独提供业务说明。 |
| `posts[].author_is_blocked` | boolean | 官方字段 `author_is_blocked`；官方未单独提供业务说明。 |
| `posts[].mod_reason_by` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].removal_reason` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].link_flair_background_color` | string | 官方字段 `link_flair_background_color`；官方未单独提供业务说明。 |
| `posts[].id` | string | 标识符。 |
| `posts[].is_robot_indexable` | boolean | 官方字段 `is_robot_indexable`；官方未单独提供业务说明。 |
| `posts[].report_reasons` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].author` | string | 作者信息。 |
| `posts[].discussion_type` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].num_comments` | integer | 官方字段 `num_comments`；官方未单独提供业务说明。 |
| `posts[].send_replies` | boolean | 官方字段 `send_replies`；官方未单独提供业务说明。 |
| `posts[].contest_mode` | boolean | 官方字段 `contest_mode`；官方未单独提供业务说明。 |
| `posts[].mod_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `posts[].author_patreon_flair` | boolean | 官方字段 `author_patreon_flair`；官方未单独提供业务说明。 |
| `posts[].author_flair_text_color` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `posts[].stickied` | boolean | 官方字段 `stickied`；官方未单独提供业务说明。 |
| `posts[].url` | string | 链接。 |
| `posts[].subreddit_subscribers` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].created_utc` | integer | 官方字段 `created_utc`；官方未单独提供业务说明。 |
| `posts[].num_crossposts` | integer | 官方字段 `num_crossposts`；官方未单独提供业务说明。 |
| `posts[].media` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].is_video` | boolean | 官方字段 `is_video`；官方未单独提供业务说明。 |
| `posts[].created_at_iso` | string | 官方字段 `created_at_iso`；官方未单独提供业务说明。 |
| `after` | string | 后续分页标识。 |

## 使用要点

- 全站搜索。trim 不要当默认。每次成功扣 3 稳卖积分。
- 顶层直接传业务字段，不要增加 `request` 包装层。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、handle、推文链接、社群链接、cursor 和分页。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/reddit-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "gymshark", "filter": "posts"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/reddit/search/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

# Wenmai SCRAPECREATORS scrapecreators_reddit_post_comments API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/reddit-post-comments`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_reddit_post_comments`
- **脚本入口**：`modules/post-comments/scripts/post_comments.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | Reddit 帖子链接。可用桌面版或移动分享链接。 |
| `trim` | boolean | 否 | 为 true 时返回精简字段。不要当默认。 |
| `cursor` | string | 否 | 上一页响应里的 cursor。评论翻页一次只传一个，不要拼接多个。 |

## 请求示例

```json
{
  "url": "https://www.reddit.com/r/AskReddit/comments/1xzu5c9/mamdani_wants_to_have_social_workers_handle/"
}
```

```bash
python3 modules/post-comments/scripts/post_comments.py '{"url": "https://www.reddit.com/r/AskReddit/comments/1xzu5c9/mamdani_wants_to_have_social_workers_handle/"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `post` | object | 官方字段 `post`；官方未单独提供业务说明。 |
| `post.approved_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `post.subreddit` | string | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `post.selftext` | string | 官方字段 `selftext`；官方未单独提供业务说明。 |
| `post.user_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `post.saved` | boolean | 官方字段 `saved`；官方未单独提供业务说明。 |
| `post.mod_reason_title` | null | 官方示例为 null，未说明非空类型。 |
| `post.gilded` | integer | 官方字段 `gilded`；官方未单独提供业务说明。 |
| `post.clicked` | boolean | 官方字段 `clicked`；官方未单独提供业务说明。 |
| `post.title` | string | 标题。 |
| `post.link_flair_richtext` | array | 官方示例为空数组，未提供元素结构。 |
| `post.subreddit_name_prefixed` | string | 官方字段 `subreddit_name_prefixed`；官方未单独提供业务说明。 |
| `post.hidden` | boolean | 官方字段 `hidden`；官方未单独提供业务说明。 |
| `post.pwls` | integer | 官方字段 `pwls`；官方未单独提供业务说明。 |
| `post.link_flair_css_class` | null | 官方示例为 null，未说明非空类型。 |
| `post.downs` | integer | 官方字段 `downs`；官方未单独提供业务说明。 |
| `post.top_awarded_type` | null | 官方示例为 null，未说明非空类型。 |
| `post.hide_score` | boolean | 官方字段 `hide_score`；官方未单独提供业务说明。 |
| `post.name` | string | 名称。 |
| `post.quarantine` | boolean | 官方字段 `quarantine`；官方未单独提供业务说明。 |
| `post.link_flair_text_color` | string | 官方字段 `link_flair_text_color`；官方未单独提供业务说明。 |
| `post.upvote_ratio` | number | 官方字段 `upvote_ratio`；官方未单独提供业务说明。 |
| `post.subreddit_type` | string | 官方字段 `subreddit_type`；官方未单独提供业务说明。 |
| `post.ups` | integer | 官方字段 `ups`；官方未单独提供业务说明。 |
| `post.total_awards_received` | integer | 官方字段 `total_awards_received`；官方未单独提供业务说明。 |
| `post.media_embed` | object | 官方示例为空对象，未提供子字段。 |
| `post.is_original_content` | boolean | 官方字段 `is_original_content`；官方未单独提供业务说明。 |
| `post.author_fullname` | string | 官方字段 `author_fullname`；官方未单独提供业务说明。 |
| `post.secure_media` | null | 官方示例为 null，未说明非空类型。 |
| `post.is_reddit_media_domain` | boolean | 官方字段 `is_reddit_media_domain`；官方未单独提供业务说明。 |
| `post.is_meta` | boolean | 官方字段 `is_meta`；官方未单独提供业务说明。 |
| `post.category` | null | 官方示例为 null，未说明非空类型。 |
| `post.secure_media_embed` | object | 官方示例为空对象，未提供子字段。 |
| `post.link_flair_text` | null | 官方示例为 null，未说明非空类型。 |
| `post.can_mod_post` | boolean | 官方字段 `can_mod_post`；官方未单独提供业务说明。 |
| `post.score` | integer | 官方字段 `score`；官方未单独提供业务说明。 |
| `post.approved_by` | null | 官方示例为 null，未说明非空类型。 |
| `post.is_created_from_ads_ui` | boolean | 官方字段 `is_created_from_ads_ui`；官方未单独提供业务说明。 |
| `post.author_premium` | boolean | 官方字段 `author_premium`；官方未单独提供业务说明。 |
| `post.thumbnail` | string | 缩略图。 |
| `post.edited` | integer | 官方字段 `edited`；官方未单独提供业务说明。 |
| `post.gildings` | object | 官方示例为空对象，未提供子字段。 |
| `post.content_categories` | null | 官方示例为 null，未说明非空类型。 |
| `post.is_self` | boolean | 官方字段 `is_self`；官方未单独提供业务说明。 |
| `post.mod_note` | null | 官方示例为 null，未说明非空类型。 |
| `post.created` | integer | 官方字段 `created`；官方未单独提供业务说明。 |
| `post.link_flair_type` | string | 官方字段 `link_flair_type`；官方未单独提供业务说明。 |
| `post.wls` | integer | 官方字段 `wls`；官方未单独提供业务说明。 |
| `post.removed_by_category` | null | 官方示例为 null，未说明非空类型。 |
| `post.banned_by` | null | 官方示例为 null，未说明非空类型。 |
| `post.domain` | string | 域名。 |
| `post.allow_live_comments` | boolean | 官方字段 `allow_live_comments`；官方未单独提供业务说明。 |
| `post.selftext_html` | null | 官方示例为 null，未说明非空类型。 |
| `post.likes` | null | 官方示例为 null，未说明非空类型。 |
| `post.suggested_sort` | null | 官方示例为 null，未说明非空类型。 |
| `post.banned_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `post.view_count` | null | 官方示例为 null，未说明非空类型。 |
| `post.archived` | boolean | 官方字段 `archived`；官方未单独提供业务说明。 |
| `post.no_follow` | boolean | 官方字段 `no_follow`；官方未单独提供业务说明。 |
| `post.is_crosspostable` | boolean | 官方字段 `is_crosspostable`；官方未单独提供业务说明。 |
| `post.pinned` | boolean | 官方字段 `pinned`；官方未单独提供业务说明。 |
| `post.over_18` | boolean | 官方字段 `over_18`；官方未单独提供业务说明。 |
| `post.all_awardings` | array | 官方示例为空数组，未提供元素结构。 |
| `post.awarders` | array | 官方示例为空数组，未提供元素结构。 |
| `post.media_only` | boolean | 官方字段 `media_only`；官方未单独提供业务说明。 |
| `post.can_gild` | boolean | 官方字段 `can_gild`；官方未单独提供业务说明。 |
| `post.spoiler` | boolean | 官方字段 `spoiler`；官方未单独提供业务说明。 |
| `post.locked` | boolean | 官方字段 `locked`；官方未单独提供业务说明。 |
| `post.treatment_tags` | array | 官方示例为空数组，未提供元素结构。 |
| `post.visited` | boolean | 官方字段 `visited`；官方未单独提供业务说明。 |
| `post.removed_by` | null | 官方示例为 null，未说明非空类型。 |
| `post.num_reports` | null | 官方示例为 null，未说明非空类型。 |
| `post.distinguished` | null | 官方示例为 null，未说明非空类型。 |
| `post.subreddit_id` | string | 官方字段 `subreddit_id`；官方未单独提供业务说明。 |
| `post.author_is_blocked` | boolean | 官方字段 `author_is_blocked`；官方未单独提供业务说明。 |
| `post.mod_reason_by` | null | 官方示例为 null，未说明非空类型。 |
| `post.removal_reason` | null | 官方示例为 null，未说明非空类型。 |
| `post.link_flair_background_color` | string | 官方字段 `link_flair_background_color`；官方未单独提供业务说明。 |
| `post.id` | string | 标识符。 |
| `post.is_robot_indexable` | boolean | 官方字段 `is_robot_indexable`；官方未单独提供业务说明。 |
| `post.num_duplicates` | integer | 官方字段 `num_duplicates`；官方未单独提供业务说明。 |
| `post.report_reasons` | null | 官方示例为 null，未说明非空类型。 |
| `post.author` | string | 作者信息。 |
| `post.discussion_type` | null | 官方示例为 null，未说明非空类型。 |
| `post.num_comments` | integer | 官方字段 `num_comments`；官方未单独提供业务说明。 |
| `post.send_replies` | boolean | 官方字段 `send_replies`；官方未单独提供业务说明。 |
| `post.media` | null | 官方示例为 null，未说明非空类型。 |
| `post.contest_mode` | boolean | 官方字段 `contest_mode`；官方未单独提供业务说明。 |
| `post.author_patreon_flair` | boolean | 官方字段 `author_patreon_flair`；官方未单独提供业务说明。 |
| `post.permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `post.stickied` | boolean | 官方字段 `stickied`；官方未单独提供业务说明。 |
| `post.url` | string | 链接。 |
| `post.subreddit_subscribers` | integer | 官方字段 `subreddit_subscribers`；官方未单独提供业务说明。 |
| `post.created_utc` | integer | 官方字段 `created_utc`；官方未单独提供业务说明。 |
| `post.num_crossposts` | integer | 官方字段 `num_crossposts`；官方未单独提供业务说明。 |
| `post.mod_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `post.is_video` | boolean | 官方字段 `is_video`；官方未单独提供业务说明。 |
| `comments` | array | 评论列表。 |
| `comments[].url` | string | 链接。 |
| `comments[].created_utc` | integer | 官方字段 `created_utc`；官方未单独提供业务说明。 |
| `comments[].created_at_iso` | string | 官方字段 `created_at_iso`；官方未单独提供业务说明。 |
| `comments[].subreddit_id` | string | 官方字段 `subreddit_id`；官方未单独提供业务说明。 |
| `comments[].approved_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].author_is_blocked` | boolean | 官方字段 `author_is_blocked`；官方未单独提供业务说明。 |
| `comments[].comment_type` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].awarders` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].mod_reason_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].banned_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].total_awards_received` | integer | 官方字段 `total_awards_received`；官方未单独提供业务说明。 |
| `comments[].subreddit` | string | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `comments[].likes` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies` | object | 回复列表。 |
| `comments[].replies.items` | array | 结果条目。 |
| `comments[].replies.items[].url` | string | 链接。 |
| `comments[].replies.items[].created_utc` | integer | 官方字段 `created_utc`；官方未单独提供业务说明。 |
| `comments[].replies.items[].created_at_iso` | string | 官方字段 `created_at_iso`；官方未单独提供业务说明。 |
| `comments[].replies.items[].subreddit_id` | string | 官方字段 `subreddit_id`；官方未单独提供业务说明。 |
| `comments[].replies.items[].approved_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].author_is_blocked` | boolean | 官方字段 `author_is_blocked`；官方未单独提供业务说明。 |
| `comments[].replies.items[].comment_type` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].awarders` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].mod_reason_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].banned_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].total_awards_received` | integer | 官方字段 `total_awards_received`；官方未单独提供业务说明。 |
| `comments[].replies.items[].subreddit` | string | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `comments[].replies.items[].likes` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies` | object | 回复列表。 |
| `comments[].replies.items[].replies.items` | array | 结果条目。 |
| `comments[].replies.items[].replies.items[].url` | string | 链接。 |
| `comments[].replies.items[].replies.items[].created_utc` | integer | 官方字段 `created_utc`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].created_at_iso` | string | 官方字段 `created_at_iso`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].total_awards_received` | integer | 官方字段 `total_awards_received`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].approved_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].author_is_blocked` | boolean | 官方字段 `author_is_blocked`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].comment_type` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].awarders` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].mod_reason_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].banned_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].ups` | integer | 官方字段 `ups`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].removal_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].link_id` | string | 官方字段 `link_id`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].likes` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies` | object | 回复列表。 |
| `comments[].replies.items[].replies.items[].replies.items` | array | 结果条目。 |
| `comments[].replies.items[].replies.items[].replies.items[].url` | string | 链接。 |
| `comments[].replies.items[].replies.items[].replies.items[].created_utc` | integer | 官方字段 `created_utc`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].created_at_iso` | string | 官方字段 `created_at_iso`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].subreddit_id` | string | 官方字段 `subreddit_id`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].approved_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].author_is_blocked` | boolean | 官方字段 `author_is_blocked`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].comment_type` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].awarders` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].replies.items[].mod_reason_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].banned_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].total_awards_received` | integer | 官方字段 `total_awards_received`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].subreddit` | string | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].likes` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].replies` | object | 回复列表。 |
| `comments[].replies.items[].replies.items[].replies.items[].replies.items` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].replies.items[].replies.more` | object | 官方字段 `more`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].replies.more.has_more` | boolean | 是否还有更多结果。 |
| `comments[].replies.items[].replies.items[].replies.items[].replies.more.next_cursor` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].user_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].replies.items[].saved` | boolean | 官方字段 `saved`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].id` | string | 标识符。 |
| `comments[].replies.items[].replies.items[].replies.items[].banned_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].mod_reason_title` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].gilded` | integer | 官方字段 `gilded`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].archived` | boolean | 官方字段 `archived`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].collapsed_reason_code` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].no_follow` | boolean | 官方字段 `no_follow`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].author` | string | 作者信息。 |
| `comments[].replies.items[].replies.items[].replies.items[].can_mod_post` | boolean | 官方字段 `can_mod_post`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].send_replies` | boolean | 官方字段 `send_replies`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].parent_id` | string | 官方字段 `parent_id`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].score` | integer | 官方字段 `score`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].author_fullname` | string | 官方字段 `author_fullname`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].removal_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].approved_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].mod_note` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].all_awardings` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].replies.items[].collapsed` | boolean | 官方字段 `collapsed`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].body` | string | 官方字段 `body`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].edited` | boolean | 官方字段 `edited`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].top_awarded_type` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].name` | string | 名称。 |
| `comments[].replies.items[].replies.items[].replies.items[].is_submitter` | boolean | 官方字段 `is_submitter`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].downs` | integer | 官方字段 `downs`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].author_patreon_flair` | boolean | 官方字段 `author_patreon_flair`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].body_html` | string | 官方字段 `body_html`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].gildings` | object | 官方示例为空对象，未提供子字段。 |
| `comments[].replies.items[].replies.items[].replies.items[].collapsed_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].distinguished` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].associated_award` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].stickied` | boolean | 官方字段 `stickied`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].author_premium` | boolean | 官方字段 `author_premium`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].can_gild` | boolean | 官方字段 `can_gild`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].link_id` | string | 官方字段 `link_id`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].unrepliable_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].score_hidden` | boolean | 官方字段 `score_hidden`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].subreddit_type` | string | 官方字段 `subreddit_type`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].locked` | boolean | 官方字段 `locked`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].report_reasons` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].created` | integer | 官方字段 `created`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].treatment_tags` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].replies.items[].subreddit_name_prefixed` | string | 官方字段 `subreddit_name_prefixed`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].controversiality` | integer | 官方字段 `controversiality`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].depth` | integer | 官方字段 `depth`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.items[].collapsed_because_crowd_control` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].mod_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].replies.items[].num_reports` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].replies.items[].ups` | integer | 官方字段 `ups`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.more` | object | 官方字段 `more`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].replies.more.has_more` | boolean | 是否还有更多结果。 |
| `comments[].replies.items[].replies.items[].replies.more.cursor` | string | 分页游标。 |
| `comments[].replies.items[].replies.items[].user_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].saved` | boolean | 官方字段 `saved`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].id` | string | 标识符。 |
| `comments[].replies.items[].replies.items[].banned_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].mod_reason_title` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].gilded` | integer | 官方字段 `gilded`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].archived` | boolean | 官方字段 `archived`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].collapsed_reason_code` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].no_follow` | boolean | 官方字段 `no_follow`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].author` | string | 作者信息。 |
| `comments[].replies.items[].replies.items[].can_mod_post` | boolean | 官方字段 `can_mod_post`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].send_replies` | boolean | 官方字段 `send_replies`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].parent_id` | string | 官方字段 `parent_id`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].score` | integer | 官方字段 `score`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].approved_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].report_reasons` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].all_awardings` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].subreddit_id` | string | 官方字段 `subreddit_id`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].body` | string | 官方字段 `body`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].edited` | boolean | 官方字段 `edited`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].downs` | integer | 官方字段 `downs`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].is_submitter` | boolean | 官方字段 `is_submitter`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].body_html` | string | 官方字段 `body_html`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].gildings` | object | 官方示例为空对象，未提供子字段。 |
| `comments[].replies.items[].replies.items[].collapsed_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].associated_award` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].stickied` | boolean | 官方字段 `stickied`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].subreddit_type` | string | 官方字段 `subreddit_type`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].can_gild` | boolean | 官方字段 `can_gild`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].top_awarded_type` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].unrepliable_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].score_hidden` | boolean | 官方字段 `score_hidden`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].num_reports` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].locked` | boolean | 官方字段 `locked`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].name` | string | 名称。 |
| `comments[].replies.items[].replies.items[].created` | integer | 官方字段 `created`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].subreddit` | string | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].treatment_tags` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].collapsed` | boolean | 官方字段 `collapsed`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].subreddit_name_prefixed` | string | 官方字段 `subreddit_name_prefixed`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].controversiality` | integer | 官方字段 `controversiality`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].depth` | integer | 官方字段 `depth`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.items[].collapsed_because_crowd_control` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].mod_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].replies.items[].mod_note` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.items[].distinguished` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].replies.more` | object | 官方字段 `more`；官方未单独提供业务说明。 |
| `comments[].replies.items[].replies.more.has_more` | boolean | 是否还有更多结果。 |
| `comments[].replies.items[].replies.more.cursor` | string | 分页游标。 |
| `comments[].replies.items[].user_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].saved` | boolean | 官方字段 `saved`；官方未单独提供业务说明。 |
| `comments[].replies.items[].id` | string | 标识符。 |
| `comments[].replies.items[].banned_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].mod_reason_title` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].gilded` | integer | 官方字段 `gilded`；官方未单独提供业务说明。 |
| `comments[].replies.items[].archived` | boolean | 官方字段 `archived`；官方未单独提供业务说明。 |
| `comments[].replies.items[].collapsed_reason_code` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].no_follow` | boolean | 官方字段 `no_follow`；官方未单独提供业务说明。 |
| `comments[].replies.items[].author` | string | 作者信息。 |
| `comments[].replies.items[].can_mod_post` | boolean | 官方字段 `can_mod_post`；官方未单独提供业务说明。 |
| `comments[].replies.items[].send_replies` | boolean | 官方字段 `send_replies`；官方未单独提供业务说明。 |
| `comments[].replies.items[].parent_id` | string | 官方字段 `parent_id`；官方未单独提供业务说明。 |
| `comments[].replies.items[].score` | integer | 官方字段 `score`；官方未单独提供业务说明。 |
| `comments[].replies.items[].author_fullname` | string | 官方字段 `author_fullname`；官方未单独提供业务说明。 |
| `comments[].replies.items[].removal_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].approved_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].mod_note` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].all_awardings` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].body` | string | 官方字段 `body`；官方未单独提供业务说明。 |
| `comments[].replies.items[].edited` | boolean | 官方字段 `edited`；官方未单独提供业务说明。 |
| `comments[].replies.items[].top_awarded_type` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].name` | string | 名称。 |
| `comments[].replies.items[].is_submitter` | boolean | 官方字段 `is_submitter`；官方未单独提供业务说明。 |
| `comments[].replies.items[].downs` | integer | 官方字段 `downs`；官方未单独提供业务说明。 |
| `comments[].replies.items[].author_patreon_flair` | boolean | 官方字段 `author_patreon_flair`；官方未单独提供业务说明。 |
| `comments[].replies.items[].body_html` | string | 官方字段 `body_html`；官方未单独提供业务说明。 |
| `comments[].replies.items[].gildings` | object | 官方示例为空对象，未提供子字段。 |
| `comments[].replies.items[].collapsed_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].distinguished` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].associated_award` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].stickied` | boolean | 官方字段 `stickied`；官方未单独提供业务说明。 |
| `comments[].replies.items[].author_premium` | boolean | 官方字段 `author_premium`；官方未单独提供业务说明。 |
| `comments[].replies.items[].can_gild` | boolean | 官方字段 `can_gild`；官方未单独提供业务说明。 |
| `comments[].replies.items[].link_id` | string | 官方字段 `link_id`；官方未单独提供业务说明。 |
| `comments[].replies.items[].unrepliable_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].score_hidden` | boolean | 官方字段 `score_hidden`；官方未单独提供业务说明。 |
| `comments[].replies.items[].permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `comments[].replies.items[].subreddit_type` | string | 官方字段 `subreddit_type`；官方未单独提供业务说明。 |
| `comments[].replies.items[].locked` | boolean | 官方字段 `locked`；官方未单独提供业务说明。 |
| `comments[].replies.items[].report_reasons` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].created` | integer | 官方字段 `created`；官方未单独提供业务说明。 |
| `comments[].replies.items[].treatment_tags` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].collapsed` | boolean | 官方字段 `collapsed`；官方未单独提供业务说明。 |
| `comments[].replies.items[].subreddit_name_prefixed` | string | 官方字段 `subreddit_name_prefixed`；官方未单独提供业务说明。 |
| `comments[].replies.items[].controversiality` | integer | 官方字段 `controversiality`；官方未单独提供业务说明。 |
| `comments[].replies.items[].depth` | integer | 官方字段 `depth`；官方未单独提供业务说明。 |
| `comments[].replies.items[].collapsed_because_crowd_control` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].mod_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].replies.items[].num_reports` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].replies.items[].ups` | integer | 官方字段 `ups`；官方未单独提供业务说明。 |
| `comments[].replies.more` | object | 官方字段 `more`；官方未单独提供业务说明。 |
| `comments[].replies.more.has_more` | boolean | 是否还有更多结果。 |
| `comments[].replies.more.cursor` | string | 分页游标。 |
| `comments[].user_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].saved` | boolean | 官方字段 `saved`；官方未单独提供业务说明。 |
| `comments[].id` | string | 标识符。 |
| `comments[].banned_at_utc` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].mod_reason_title` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].gilded` | integer | 官方字段 `gilded`；官方未单独提供业务说明。 |
| `comments[].archived` | boolean | 官方字段 `archived`；官方未单独提供业务说明。 |
| `comments[].collapsed_reason_code` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].no_follow` | boolean | 官方字段 `no_follow`；官方未单独提供业务说明。 |
| `comments[].author` | string | 作者信息。 |
| `comments[].can_mod_post` | boolean | 官方字段 `can_mod_post`；官方未单独提供业务说明。 |
| `comments[].send_replies` | boolean | 官方字段 `send_replies`；官方未单独提供业务说明。 |
| `comments[].parent_id` | string | 官方字段 `parent_id`；官方未单独提供业务说明。 |
| `comments[].score` | integer | 官方字段 `score`；官方未单独提供业务说明。 |
| `comments[].author_fullname` | string | 官方字段 `author_fullname`；官方未单独提供业务说明。 |
| `comments[].approved_by` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].mod_note` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].all_awardings` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].collapsed` | boolean | 官方字段 `collapsed`；官方未单独提供业务说明。 |
| `comments[].body` | string | 官方字段 `body`；官方未单独提供业务说明。 |
| `comments[].edited` | boolean | 官方字段 `edited`；官方未单独提供业务说明。 |
| `comments[].top_awarded_type` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].name` | string | 名称。 |
| `comments[].is_submitter` | boolean | 官方字段 `is_submitter`；官方未单独提供业务说明。 |
| `comments[].downs` | integer | 官方字段 `downs`；官方未单独提供业务说明。 |
| `comments[].author_patreon_flair` | boolean | 官方字段 `author_patreon_flair`；官方未单独提供业务说明。 |
| `comments[].body_html` | string | 官方字段 `body_html`；官方未单独提供业务说明。 |
| `comments[].removal_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].collapsed_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].distinguished` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].associated_award` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].stickied` | boolean | 官方字段 `stickied`；官方未单独提供业务说明。 |
| `comments[].author_premium` | boolean | 官方字段 `author_premium`；官方未单独提供业务说明。 |
| `comments[].can_gild` | boolean | 官方字段 `can_gild`；官方未单独提供业务说明。 |
| `comments[].gildings` | object | 官方示例为空对象，未提供子字段。 |
| `comments[].unrepliable_reason` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].score_hidden` | boolean | 官方字段 `score_hidden`；官方未单独提供业务说明。 |
| `comments[].permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `comments[].subreddit_type` | string | 官方字段 `subreddit_type`；官方未单独提供业务说明。 |
| `comments[].locked` | boolean | 官方字段 `locked`；官方未单独提供业务说明。 |
| `comments[].report_reasons` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].created` | integer | 官方字段 `created`；官方未单独提供业务说明。 |
| `comments[].treatment_tags` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].link_id` | string | 官方字段 `link_id`；官方未单独提供业务说明。 |
| `comments[].subreddit_name_prefixed` | string | 官方字段 `subreddit_name_prefixed`；官方未单独提供业务说明。 |
| `comments[].controversiality` | integer | 官方字段 `controversiality`；官方未单独提供业务说明。 |
| `comments[].depth` | integer | 官方字段 `depth`；官方未单独提供业务说明。 |
| `comments[].collapsed_because_crowd_control` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].mod_reports` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].num_reports` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].ups` | integer | 官方字段 `ups`；官方未单独提供业务说明。 |
| `more` | object | 官方字段 `more`；官方未单独提供业务说明。 |
| `more.has_more` | boolean | 是否还有更多结果。 |
| `more.cursor` | string | 分页游标。 |
| `comments[].replies.items[].replies.more.next_cursor` | null | 官方示例为 null，未说明非空类型。 |

## 使用要点

- 按帖子链接拉评论。一次只传一个 cursor。trim 不要当默认。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/reddit-post-comments" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.reddit.com/r/AskReddit/comments/1xzu5c9/mamdani_wants_to_have_social_workers_handle/"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/reddit/post/comments/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

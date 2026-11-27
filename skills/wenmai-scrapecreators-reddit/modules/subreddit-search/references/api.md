# Wenmai SCRAPECREATORS scrapecreators_reddit_subreddit_search API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/reddit-subreddit-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_reddit_subreddit_search`
- **脚本入口**：`modules/subreddit-search/scripts/subreddit_search.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `subreddit` | string | 是 | Subreddit 名称，只要名字，不要带 r/ 或完整 URL。 |
| `query` | string | 否 | 社群内搜索词。 |
| `sort` | string | 否 | 排序：relevance、hot、top、new、comments。 |
| `timeframe` | string | 否 | 时间范围：all、year、month、week、day、hour。 |
| `cursor` | string | 否 | 上一页响应里的 cursor。评论翻页一次只传一个，不要拼接多个。 |

## 请求示例

```json
{
  "subreddit": "AskReddit",
  "query": "amazon"
}
```

```bash
python3 modules/subreddit-search/scripts/subreddit_search.py '{"subreddit": "AskReddit", "query": "amazon"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `posts` | array | 帖子列表。 |
| `posts[].id` | string | 标识符。 |
| `posts[].post_id` | string | 官方字段 `post_id`；官方未单独提供业务说明。 |
| `posts[].title` | string | 标题。 |
| `posts[].url` | string | 链接。 |
| `posts[].permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `posts[].nsfw` | boolean | 官方字段 `nsfw`；官方未单独提供业务说明。 |
| `posts[].spoiler` | boolean | 官方字段 `spoiler`；官方未单独提供业务说明。 |
| `posts[].is_crosspost` | boolean | 官方字段 `is_crosspost`；官方未单独提供业务说明。 |
| `posts[].subreddit` | object | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `posts[].subreddit.id` | string | 标识符。 |
| `posts[].subreddit.name` | string | 名称。 |
| `posts[].subreddit.nsfw` | boolean | 官方字段 `nsfw`；官方未单独提供业务说明。 |
| `posts[].subreddit.quarantined` | boolean | 官方字段 `quarantined`；官方未单独提供业务说明。 |
| `posts[].subreddit.icon` | string | 官方字段 `icon`；官方未单独提供业务说明。 |
| `posts[].subreddit.banner` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].subreddit.description` | string | 描述。 |
| `posts[].subreddit.weekly_visitors` | integer | 官方字段 `weekly_visitors`；官方未单独提供业务说明。 |
| `posts[].subreddit.weekly_contributions` | integer | 官方字段 `weekly_contributions`；官方未单独提供业务说明。 |
| `posts[].votes` | integer | 官方字段 `votes`；官方未单独提供业务说明。 |
| `posts[].num_comments` | integer | 官方字段 `num_comments`；官方未单独提供业务说明。 |
| `posts[].created_at` | string | 创建时间。 |
| `posts[].created_at_iso` | string | 官方字段 `created_at_iso`；官方未单独提供业务说明。 |
| `posts[].thumbnail` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].thumbnail_blurred` | boolean | 官方字段 `thumbnail_blurred`；官方未单独提供业务说明。 |
| `posts[].position` | integer | 位置或排序值。 |
| `posts[].relative_position` | integer | 官方字段 `relative_position`；官方未单独提供业务说明。 |
| `comments` | array | 评论列表。 |
| `comments[].id` | string | 标识符。 |
| `comments[].post_id` | string | 官方字段 `post_id`；官方未单独提供业务说明。 |
| `comments[].parent_comment_id` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].is_reply_to_comment` | boolean | 官方字段 `is_reply_to_comment`；官方未单独提供业务说明。 |
| `comments[].author` | string | 作者信息。 |
| `comments[].author_avatar` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].author_nsfw` | boolean | 官方字段 `author_nsfw`；官方未单独提供业务说明。 |
| `comments[].body` | string | 官方字段 `body`；官方未单独提供业务说明。 |
| `comments[].body_html` | string | 官方字段 `body_html`；官方未单独提供业务说明。 |
| `comments[].images` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].votes` | integer | 官方字段 `votes`；官方未单独提供业务说明。 |
| `comments[].url` | string | 链接。 |
| `comments[].permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `comments[].created_at` | string | 创建时间。 |
| `comments[].created_at_iso` | string | 官方字段 `created_at_iso`；官方未单独提供业务说明。 |
| `comments[].post` | object | 官方字段 `post`；官方未单独提供业务说明。 |
| `comments[].post.id` | string | 标识符。 |
| `comments[].post.title` | string | 标题。 |
| `comments[].post.url` | string | 链接。 |
| `comments[].post.permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `comments[].post.nsfw` | boolean | 官方字段 `nsfw`；官方未单独提供业务说明。 |
| `comments[].post.spoiler` | boolean | 官方字段 `spoiler`；官方未单独提供业务说明。 |
| `comments[].post.votes` | integer | 官方字段 `votes`；官方未单独提供业务说明。 |
| `comments[].post.num_comments` | integer | 官方字段 `num_comments`；官方未单独提供业务说明。 |
| `comments[].post.created_at` | string | 创建时间。 |
| `comments[].post.created_at_iso` | string | 官方字段 `created_at_iso`；官方未单独提供业务说明。 |
| `comments[].subreddit` | object | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `comments[].subreddit.id` | string | 标识符。 |
| `comments[].subreddit.name` | string | 名称。 |
| `comments[].subreddit.nsfw` | boolean | 官方字段 `nsfw`；官方未单独提供业务说明。 |
| `comments[].subreddit.quarantined` | boolean | 官方字段 `quarantined`；官方未单独提供业务说明。 |
| `comments[].subreddit.icon` | string | 官方字段 `icon`；官方未单独提供业务说明。 |
| `comments[].position` | integer | 位置或排序值。 |
| `media` | array | 官方字段 `media`；官方未单独提供业务说明。 |
| `media[].id` | string | 标识符。 |
| `media[].title` | string | 标题。 |
| `media[].url` | string | 链接。 |
| `media[].permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `media[].media_type` | string | 官方字段 `media_type`；官方未单独提供业务说明。 |
| `media[].video` | null | 官方示例为 null，未说明非空类型。 |
| `media[].image` | object | 图片信息。 |
| `media[].image.src` | string | 官方字段 `src`；官方未单独提供业务说明。 |
| `media[].image.width` | integer | 宽度。 |
| `media[].image.height` | integer | 高度。 |
| `media[].image.resolutions` | array | 官方字段 `resolutions`；官方未单独提供业务说明。 |
| `media[].image.resolutions[].url` | string | 链接。 |
| `media[].image.resolutions[].width` | integer | 宽度。 |
| `media[].gallery_count` | null | 官方示例为 null，未说明非空类型。 |
| `media[].aspect_ratio` | number | 官方字段 `aspect_ratio`；官方未单独提供业务说明。 |
| `media[].nsfw` | boolean | 官方字段 `nsfw`；官方未单独提供业务说明。 |
| `media[].spoiler` | boolean | 官方字段 `spoiler`；官方未单独提供业务说明。 |
| `media[].is_blurred` | boolean | 官方字段 `is_blurred`；官方未单独提供业务说明。 |
| `media[].subreddit` | object | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `media[].subreddit.id` | string | 标识符。 |
| `media[].subreddit.name` | string | 名称。 |
| `media[].subreddit.nsfw` | boolean | 官方字段 `nsfw`；官方未单独提供业务说明。 |
| `media[].subreddit.quarantined` | boolean | 官方字段 `quarantined`；官方未单独提供业务说明。 |
| `media[].position` | integer | 位置或排序值。 |
| `media[].safe_search` | string | 官方字段 `safe_search`；官方未单独提供业务说明。 |
| `cursor` | string | 分页游标。 |

## 使用要点

- 在单个社群内搜索。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/reddit-subreddit-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit": "AskReddit", "query": "amazon"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/reddit/subreddit/search/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

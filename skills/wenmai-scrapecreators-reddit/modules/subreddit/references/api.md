# Wenmai SCRAPECREATORS scrapecreators_reddit_subreddit API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/reddit-subreddit`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_reddit_subreddit`
- **脚本入口**：`modules/subreddit/scripts/subreddit.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `subreddit` | string | 是 | Subreddit 名称，只要名字，不要带 r/ 或完整 URL。 |
| `timeframe` | string | 否 | 时间范围：all、day、week、month、year。 |
| `sort` | string | 否 | 排序：best、hot、new、top、rising。 |
| `trim` | boolean | 否 | 为 true 时返回精简字段。不要当默认。 |
| `cache_max_age` | string | 否 | 若缓存中有不晚于该时效的数据则直接返回，官方不计 credit。 |
| `after` | string | 否 | 上一页响应里的 after。 |

## 请求示例

```json
{
  "subreddit": "AskReddit",
  "sort": "hot"
}
```

```bash
python3 modules/subreddit/scripts/subreddit.py '{"subreddit": "AskReddit", "sort": "hot"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `posts` | array | 帖子列表。 |
| `posts[].id` | string | 标识符。 |
| `posts[].author` | string | 作者信息。 |
| `posts[].author_fullname` | string | 官方字段 `author_fullname`；官方未单独提供业务说明。 |
| `posts[].subreddit` | string | 官方字段 `subreddit`；官方未单独提供业务说明。 |
| `posts[].title` | string | 标题。 |
| `posts[].link_flair_text` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].selftext` | string | 官方字段 `selftext`；官方未单独提供业务说明。 |
| `posts[].selftext_html` | string | 官方字段 `selftext_html`；官方未单独提供业务说明。 |
| `posts[].downs` | integer | 官方字段 `downs`；官方未单独提供业务说明。 |
| `posts[].name` | string | 名称。 |
| `posts[].upvote_ratio` | number | 官方字段 `upvote_ratio`；官方未单独提供业务说明。 |
| `posts[].ups` | integer | 官方字段 `ups`；官方未单独提供业务说明。 |
| `posts[].total_awards_received` | integer | 官方字段 `total_awards_received`；官方未单独提供业务说明。 |
| `posts[].score` | integer | 官方字段 `score`；官方未单独提供业务说明。 |
| `posts[].created` | integer | 官方字段 `created`；官方未单独提供业务说明。 |
| `posts[].created_utc` | integer | 官方字段 `created_utc`；官方未单独提供业务说明。 |
| `posts[].created_at_iso` | string | 官方字段 `created_at_iso`；官方未单独提供业务说明。 |
| `posts[].num_comments` | integer | 官方字段 `num_comments`；官方未单独提供业务说明。 |
| `posts[].url` | string | 链接。 |
| `posts[].permalink` | string | 官方字段 `permalink`；官方未单独提供业务说明。 |
| `posts[].subreddit_subscribers` | integer\|null | 官方字段 `subreddit_subscribers`；官方未单独提供业务说明。 |
| `posts[].is_video` | boolean | 官方字段 `is_video`；官方未单独提供业务说明。 |
| `posts[].over_18` | boolean | 官方字段 `over_18`；官方未单独提供业务说明。 |
| `posts[].spoiler` | boolean | 官方字段 `spoiler`；官方未单独提供业务说明。 |
| `posts[].domain` | string | 域名。 |
| `posts[].subreddit_id` | string | 官方字段 `subreddit_id`；官方未单独提供业务说明。 |
| `posts[].post_hint` | string | 官方字段 `post_hint`；官方未单独提供业务说明。 |
| `after` | string | 后续分页标识。 |

## 使用要点

- 按社群名拉帖子。trim 不要当默认。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/reddit-subreddit" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit": "AskReddit", "sort": "hot"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/reddit/subreddit/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

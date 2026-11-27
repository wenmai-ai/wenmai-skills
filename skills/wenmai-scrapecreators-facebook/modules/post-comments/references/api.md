# Wenmai SCRAPECREATORS scrapecreators_facebook_post_comments API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-post-comments`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_facebook_post_comments`
- **脚本入口**：`modules/post-comments/scripts/post_comments.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 否 | 帖子链接，与 feedback_id 二选一。 |
| `feedback_id` | string | 否 | 来自帖子详情。 |
| `sort` | string | 否 | most_relevant 或 all。 |
| `cursor` | string | 否 | 分页游标。 |

## 请求示例

```json
{
  "url": "https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l",
  "sort": "most_relevant"
}
```

```bash
python3 modules/post-comments/scripts/post_comments.py '{"url": "https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l", "sort": "most_relevant"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `comments` | array | 评论列表。 |
| `comments[].id` | string | 标识符。 |
| `comments[].text` | string | 文本内容。 |
| `comments[].created_at` | string | 创建时间。 |
| `comments[].reply_count` | integer | 回复数量。 |
| `comments[].reaction_count` | integer | 官方字段 `reaction_count`；官方未单独提供业务说明。 |
| `comments[].reactions` | object | 官方字段 `reactions`；官方未单独提供业务说明。 |
| `comments[].reactions.thankful` | integer | 官方字段 `thankful`；官方未单独提供业务说明。 |
| `comments[].reactions.like` | integer | 官方字段 `like`；官方未单独提供业务说明。 |
| `comments[].reactions.love` | integer | 官方字段 `love`；官方未单独提供业务说明。 |
| `comments[].reactions.care` | integer | 官方字段 `care`；官方未单独提供业务说明。 |
| `comments[].reactions.haha` | integer | 官方字段 `haha`；官方未单独提供业务说明。 |
| `comments[].reactions.wow` | integer | 官方字段 `wow`；官方未单独提供业务说明。 |
| `comments[].reactions.sad` | integer | 官方字段 `sad`；官方未单独提供业务说明。 |
| `comments[].reactions.anger` | integer | 官方字段 `anger`；官方未单独提供业务说明。 |
| `comments[].reactions.pride` | integer | 官方字段 `pride`；官方未单独提供业务说明。 |
| `comments[].reactions.confused` | integer | 官方字段 `confused`；官方未单独提供业务说明。 |
| `comments[].author` | object | 作者信息。 |
| `comments[].author.id` | string | 标识符。 |
| `comments[].author.name` | string | 名称。 |
| `comments[].author.gender` | string | 官方字段 `gender`；官方未单独提供业务说明。 |
| `comments[].author.short_name` | string | 官方字段 `short_name`；官方未单独提供业务说明。 |
| `cursor` | string | 分页游标。 |
| `has_next_page` | boolean | 是否存在下一页。 |

## 使用要点

- 评论。回复用评论上的 feedback_id 和 expansion_token。每次成功扣 3 稳卖积分。
- 顶层直接传业务字段，不要增加 `request` 包装层。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、主页/帖子链接、pageId、商品/广告 ID、cursor 和分页。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-post-comments" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l", "sort": "most_relevant"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/facebook/post/comments/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

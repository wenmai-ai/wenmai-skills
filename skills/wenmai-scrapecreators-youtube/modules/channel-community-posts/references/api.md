# Wenmai SCRAPECREATORS scrapecreators_youtube_channel_community_posts API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/youtube-channel-community-posts`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_youtube_channel_community_posts`
- **脚本入口**：`modules/channel-community-posts/scripts/channel_community_posts.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `channelId` | string | 否 | YouTube 频道 ID。与 handle 二选一。 |
| `handle` | string | 否 | YouTube 频道 handle，带或不带 @。 |
| `continuationToken` | string | 否 | 分页游标，传入上一页响应中的 continuationToken。 |

## 请求示例

```json
{
  "handle": "gymshark"
}
```

```bash
python3 modules/channel-community-posts/scripts/channel_community_posts.py '{"handle": "gymshark"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `posts` | array | 帖子列表。 |
| `posts[].id` | string | 标识符。 |
| `posts[].url` | string | 链接。 |
| `posts[].channel` | object | 频道。 |
| `posts[].channel.id` | string | 标识符。 |
| `posts[].channel.title` | string | 标题。 |
| `posts[].channel.url` | string | 链接。 |
| `posts[].channel.handle` | string | 账号名称。 |
| `posts[].content` | string | 官方字段 `content`；官方未单独提供业务说明。 |
| `posts[].image` | string | 图片信息。 |
| `posts[].images` | array | 图片列表。 |
| `posts[].images[]` | string | 图片列表中的元素。 |
| `posts[].likeCountText` | string | 官方字段 `likeCountText`；官方未单独提供业务说明。 |
| `posts[].likeCount` | integer | 官方字段 `likeCount`；官方未单独提供业务说明。 |
| `posts[].publishedTimeText` | string | 发布时间展示文本。 |
| `posts[].publishedTime` | string | 发布时间。 |
| `posts[].video` | object | 视频信息。 |
| `posts[].video.id` | string | 标识符。 |
| `posts[].video.title` | string | 标题。 |
| `posts[].video.thumbnail` | string | 缩略图。 |
| `posts[].video.url` | string | 链接。 |
| `posts[].video.viewCountText` | string | 浏览量展示文本。 |
| `posts[].video.viewCountInt` | integer | 浏览量。 |
| `posts[].video.publishedTimeText` | string | 发布时间展示文本。 |
| `posts[].video.lengthText` | string | 时长展示文本。 |
| `posts[].video.lengthSeconds` | integer | 官方字段 `lengthSeconds`；官方未单独提供业务说明。 |
| `continuationToken` | string | 续页令牌。 |

## 使用要点

- 获取频道社区帖。每次成功扣 3 稳卖积分。
- 顶层直接传业务字段，不要增加 `request` 包装层。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、handle、channelId、视频链接、播放列表 ID、continuationToken 和分页。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/youtube-channel-community-posts" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "gymshark"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/youtube/channel/community-posts/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

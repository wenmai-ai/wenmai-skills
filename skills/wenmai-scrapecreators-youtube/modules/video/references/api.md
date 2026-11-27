# Wenmai SCRAPECREATORS scrapecreators_youtube_video API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/youtube-video`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_youtube_video`
- **脚本入口**：`modules/video/scripts/video.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | YouTube 视频或 Short 链接。 |
| `language` | string | 否 | 希望返回的两位语言码，如 en。 |
| `cache_max_age` | string | 否 | 若缓存中有不晚于该时效的数据则直接返回，官方不计 credit。 |

## 请求示例

```json
{
  "url": "https://www.youtube.com/watch?v=Y2Ah_DFr8cw"
}
```

```bash
python3 modules/video/scripts/video.py '{"url": "https://www.youtube.com/watch?v=Y2Ah_DFr8cw"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `id` | string | 标识符。 |
| `thumbnail` | string | 缩略图。 |
| `storyboardSpec` | string | 官方字段 `storyboardSpec`；官方未单独提供业务说明。 |
| `url` | string | 链接。 |
| `publishDate` | string | 官方字段 `publishDate`；官方未单独提供业务说明。 |
| `type` | string | 类型。 |
| `title` | string | 标题。 |
| `description` | null | 官方示例为 null，未说明非空类型。 |
| `descriptionLinks` | array | 官方示例为空数组，未提供元素结构。 |
| `commentCountText` | string | 官方字段 `commentCountText`；官方未单独提供业务说明。 |
| `commentCountInt` | integer | 官方字段 `commentCountInt`；官方未单独提供业务说明。 |
| `likeCountText` | string | 官方字段 `likeCountText`；官方未单独提供业务说明。 |
| `likeCountInt` | integer | 官方字段 `likeCountInt`；官方未单独提供业务说明。 |
| `viewCountText` | string | 浏览量展示文本。 |
| `viewCountInt` | integer | 浏览量。 |
| `publishDateText` | string | 官方字段 `publishDateText`；官方未单独提供业务说明。 |
| `collaborators` | array | 官方示例为空数组，未提供元素结构。 |
| `channel` | object | 频道。 |
| `channel.id` | string | 标识符。 |
| `channel.url` | string | 链接。 |
| `channel.handle` | string | 账号名称。 |
| `channel.title` | string | 标题。 |
| `chapters` | array | 官方示例为空数组，未提供元素结构。 |
| `watchNextVideos` | array | 官方字段 `watchNextVideos`；官方未单独提供业务说明。 |
| `watchNextVideos[].id` | string | 标识符。 |
| `watchNextVideos[].title` | string | 标题。 |
| `watchNextVideos[].thumbnail` | string | 缩略图。 |
| `watchNextVideos[].channel` | object | 频道。 |
| `watchNextVideos[].channel.title` | string | 标题。 |
| `watchNextVideos[].channel.url` | string | 链接。 |
| `watchNextVideos[].channel.handle` | string | 账号名称。 |
| `watchNextVideos[].channel.id` | string | 标识符。 |
| `watchNextVideos[].publishedTimeText` | string | 发布时间展示文本。 |
| `watchNextVideos[].publishedTime` | string | 发布时间。 |
| `watchNextVideos[].publishDateText` | string | 官方字段 `publishDateText`；官方未单独提供业务说明。 |
| `watchNextVideos[].publishDate` | string | 官方字段 `publishDate`；官方未单独提供业务说明。 |
| `watchNextVideos[].viewCountText` | string | 浏览量展示文本。 |
| `watchNextVideos[].viewCountInt` | integer | 浏览量。 |
| `watchNextVideos[].lengthText` | string | 时长展示文本。 |
| `watchNextVideos[].lengthInSeconds` | integer | 官方字段 `lengthInSeconds`；官方未单独提供业务说明。 |
| `watchNextVideos[].videoUrl` | string | 官方字段 `videoUrl`；官方未单独提供业务说明。 |
| `keywords` | array | 官方示例为空数组，未提供元素结构。 |
| `genre` | string | 官方字段 `genre`；官方未单独提供业务说明。 |
| `durationMs` | integer | 官方字段 `durationMs`；官方未单独提供业务说明。 |
| `durationFormatted` | string | 官方字段 `durationFormatted`；官方未单独提供业务说明。 |
| `isPaidPromotion` | boolean | 官方字段 `isPaidPromotion`；官方未单独提供业务说明。 |
| `descriptionCards` | array | 官方示例为空数组，未提供元素结构。 |
| `isMadeWithAI` | boolean | 官方字段 `isMadeWithAI`；官方未单独提供业务说明。 |
| `aiDisclosure` | string | 官方字段 `aiDisclosure`；官方未单独提供业务说明。 |
| `ownerByline` | object | 官方字段 `ownerByline`；官方未单独提供业务说明。 |
| `ownerByline.channelId` | string | 官方字段 `channelId`；官方未单独提供业务说明。 |
| `ownerByline.name` | string | 名称。 |
| `ownerByline.url` | string | 链接。 |
| `ownerByline.subscriberCountText` | string | 官方字段 `subscriberCountText`；官方未单独提供业务说明。 |
| `ownerByline.badges` | array | 官方示例为空数组，未提供元素结构。 |
| `uploader` | object | 官方字段 `uploader`；官方未单独提供业务说明。 |
| `uploader.channelId` | string | 官方字段 `channelId`；官方未单独提供业务说明。 |
| `uploader.author` | string | 作者信息。 |
| `uploader.url` | string | 链接。 |
| `most_replayed` | null | 官方示例为 null，未说明非空类型。 |
| `captionTracks` | array | 官方字段 `captionTracks`；官方未单独提供业务说明。 |
| `captionTracks[].baseUrl` | string | 官方字段 `baseUrl`；官方未单独提供业务说明。 |
| `captionTracks[].name` | object | 名称。 |
| `captionTracks[].name.simpleText` | string | 官方字段 `simpleText`；官方未单独提供业务说明。 |
| `captionTracks[].vssId` | string | 官方字段 `vssId`；官方未单独提供业务说明。 |
| `captionTracks[].languageCode` | string | 官方字段 `languageCode`；官方未单独提供业务说明。 |
| `captionTracks[].kind` | string | 官方字段 `kind`；官方未单独提供业务说明。 |
| `captionTracks[].isTranslatable` | boolean | 官方字段 `isTranslatable`；官方未单独提供业务说明。 |
| `captionTracks[].trackName` | string | 官方字段 `trackName`；官方未单独提供业务说明。 |

## 使用要点

- 获取视频或 Short 详情。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/youtube-video" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=Y2Ah_DFr8cw"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/youtube/video/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

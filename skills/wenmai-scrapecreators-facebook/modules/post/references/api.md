# Wenmai SCRAPECREATORS scrapecreators_facebook_post API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-post`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_facebook_post`
- **脚本入口**：`modules/post/scripts/post.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | 帖子或 Reel 链接。 |
| `get_transcript` | boolean | 否 | 不要当默认。 |
| `allow_long_transcription` | boolean | 否 | 长视频付费转写，不要当默认。 |
| `cache_max_age` | string | 否 | 缓存时效。 |

## 请求示例

```json
{
  "url": "https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l"
}
```

```bash
python3 modules/post/scripts/post.py '{"url": "https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `post_id` | string | 官方字段 `post_id`；官方未单独提供业务说明。 |
| `shared_post_id` | null | 官方示例为 null，未说明非空类型。 |
| `shared_post_url` | null | 官方示例为 null，未说明非空类型。 |
| `is_paid_partnership` | null | 官方示例为 null，未说明非空类型。 |
| `like_count` | integer | 点赞数量。 |
| `comment_count` | integer | 评论数量。 |
| `share_count` | integer | 分享数量。 |
| `view_count` | integer | 官方字段 `view_count`；官方未单独提供业务说明。 |
| `description` | string | 描述。 |
| `creation_time` | string | 官方字段 `creation_time`；官方未单独提供业务说明。 |
| `feedback_id` | string | 官方字段 `feedback_id`；官方未单独提供业务说明。 |
| `url` | string | 链接。 |
| `image_url` | null | 官方示例为 null，未说明非空类型。 |
| `video` | object | 视频信息。 |
| `video.id` | string | 标识符。 |
| `video.sd_url` | string | 官方字段 `sd_url`；官方未单独提供业务说明。 |
| `video.hd_url` | string | 官方字段 `hd_url`；官方未单独提供业务说明。 |
| `video.height` | integer | 高度。 |
| `video.width` | integer | 宽度。 |
| `video.length_in_second` | number | 官方字段 `length_in_second`；官方未单独提供业务说明。 |
| `video.thumbnail` | string | 缩略图。 |
| `video.captions_url` | string | 官方字段 `captions_url`；官方未单独提供业务说明。 |
| `author` | object | 作者信息。 |
| `author.id` | string | 标识符。 |
| `author.name` | string | 名称。 |
| `author.handle` | string | 账号名称。 |
| `author.is_verified` | boolean | 是否认证。 |
| `author.url` | string | 链接。 |
| `author.image` | string | 图片信息。 |
| `music` | object | 官方字段 `music`；官方未单独提供业务说明。 |
| `music.id` | string | 标识符。 |
| `music.type` | string | 类型。 |
| `music.track_title` | string | 官方字段 `track_title`；官方未单独提供业务说明。 |
| `music.music_album_art` | string | 官方字段 `music_album_art`；官方未单独提供业务说明。 |

## 使用要点

- 帖子详情。get_transcript / allow_long_transcription 不要当默认。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-post" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/facebook/post/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

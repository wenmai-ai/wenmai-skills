# Wenmai SCRAPECREATORS scrapecreators_instagram_search_hashtag API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-search-hashtag`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_instagram_search_hashtag`
- **脚本入口**：`modules/search-hashtag/scripts/search_hashtag.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `hashtag` | string | 是 | 话题名，带或不带 # 都可以。 |
| `date_posted` | string | 否 | 只返回该时间窗口内被 Google 收录的帖子。可选值：last-hour、last-day、last-week、last-month、last-year。 |
| `media_type` | string | 否 | all 搜公开帖和 Reels，reels 只返回 Reels。默认 all。可选值：all、reels。 |
| `cursor` | string | 否 | 上一页返回的 Google 结果页码，最大 11；12 及以上会 400。 |

## 请求示例

```json
{
  "hashtag": "gymshark",
  "media_type": "all"
}
```

```bash
python3 modules/search-hashtag/scripts/search_hashtag.py '{"hashtag": "gymshark", "media_type": "all"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `hashtag` | string | 官方字段 `hashtag`；官方未单独提供业务说明。 |
| `media_type` | string | 官方字段 `media_type`；官方未单独提供业务说明。 |
| `posts` | array | 帖子列表。 |
| `posts[].id` | string | 标识符。 |
| `posts[].__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `posts[].shortcode` | string | 官方字段 `shortcode`；官方未单独提供业务说明。 |
| `posts[].url` | string | 链接。 |
| `posts[].caption` | string | 说明文字。 |
| `posts[].thumbnail_src` | string | 官方字段 `thumbnail_src`；官方未单独提供业务说明。 |
| `posts[].display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `posts[].video_url` | string | 官方字段 `video_url`；官方未单独提供业务说明。 |
| `posts[].has_audio` | boolean | 官方字段 `has_audio`；官方未单独提供业务说明。 |
| `posts[].accessibility_caption` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].product_type` | string | 官方字段 `product_type`；官方未单独提供业务说明。 |
| `posts[].video_duration` | number | 视频时长。 |
| `posts[].clips_music_attribution_info` | object | 官方字段 `clips_music_attribution_info`；官方未单独提供业务说明。 |
| `posts[].clips_music_attribution_info.artist_name` | string | 官方字段 `artist_name`；官方未单独提供业务说明。 |
| `posts[].clips_music_attribution_info.song_name` | string | 官方字段 `song_name`；官方未单独提供业务说明。 |
| `posts[].clips_music_attribution_info.uses_original_audio` | boolean | 官方字段 `uses_original_audio`；官方未单独提供业务说明。 |
| `posts[].clips_music_attribution_info.should_mute_audio` | boolean | 官方字段 `should_mute_audio`；官方未单独提供业务说明。 |
| `posts[].clips_music_attribution_info.should_mute_audio_reason` | string | 官方字段 `should_mute_audio_reason`；官方未单独提供业务说明。 |
| `posts[].clips_music_attribution_info.audio_id` | string | 官方字段 `audio_id`；官方未单独提供业务说明。 |
| `posts[].is_video` | boolean | 官方字段 `is_video`；官方未单独提供业务说明。 |
| `posts[].owner` | object | 所属账号。 |
| `posts[].owner.id` | string | 标识符。 |
| `posts[].owner.username` | string | 用户名。 |
| `posts[].owner.is_verified` | boolean | 是否认证。 |
| `posts[].owner.profile_pic_url` | string | 头像链接。 |
| `posts[].owner.full_name` | string | 完整名称。 |
| `posts[].owner.is_private` | boolean | 是否为私密账号。 |
| `posts[].owner.is_unpublished` | boolean | 官方字段 `is_unpublished`；官方未单独提供业务说明。 |
| `posts[].owner.follower_count` | integer | 粉丝数量。 |
| `posts[].owner.post_count` | integer | 官方字段 `post_count`；官方未单独提供业务说明。 |
| `posts[].taken_at` | string | 官方字段 `taken_at`；官方未单独提供业务说明。 |
| `posts[].is_ad` | boolean | 官方字段 `is_ad`；官方未单独提供业务说明。 |
| `posts[].like_count` | integer | 点赞数量。 |
| `posts[].is_affiliate` | boolean | 官方字段 `is_affiliate`；官方未单独提供业务说明。 |
| `posts[].is_paid_partnership` | boolean | 是否为付费合作内容。 |
| `posts[].location` | null | 官方示例为 null，未说明非空类型。 |
| `posts[].comment_count` | integer | 评论数量。 |
| `posts[].comments` | array | 评论列表。 |
| `posts[].comments[].id` | string | 标识符。 |
| `posts[].comments[].text` | string | 文本内容。 |
| `posts[].comments[].owner` | object | 所属账号。 |
| `posts[].comments[].owner.id` | string | 标识符。 |
| `posts[].comments[].owner.is_verified` | boolean | 是否认证。 |
| `posts[].comments[].owner.profile_pic_url` | string | 头像链接。 |
| `posts[].comments[].owner.username` | string | 用户名。 |
| `posts[].comments[].like_count` | integer | 点赞数量。 |
| `posts[].comments[].created_at` | string | 创建时间。 |
| `cursor` | string | 分页游标。 |

## 使用要点

- hashtag 可带或不带 #。cursor 最大 11。每次成功扣 3 稳卖积分。
- 顶层直接传业务字段，不要增加 `request` 包装层。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、handle、userId、帖子链接、视频链接和分页。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-search-hashtag" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "gymshark", "media_type": "all"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/instagram/search/hashtag/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

# Wenmai SCRAPECREATORS scrapecreators_instagram_reels_trending API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-reels-trending`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_instagram_reels_trending`
- **脚本入口**：`modules/reels-trending/scripts/reels_trending.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|

## 请求示例

```json
{}
```

```bash
python3 modules/reels-trending/scripts/reels_trending.py '{}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `reels` | array | 官方字段 `reels`；官方未单独提供业务说明。 |
| `reels[].id` | string | 标识符。 |
| `reels[].pk` | string | 主键标识。 |
| `reels[].shortcode` | string | 官方字段 `shortcode`；官方未单独提供业务说明。 |
| `reels[].url` | string | 链接。 |
| `reels[].caption` | string | 说明文字。 |
| `reels[].taken_at` | string | 官方字段 `taken_at`；官方未单独提供业务说明。 |
| `reels[].media_type` | integer | 官方字段 `media_type`；官方未单独提供业务说明。 |
| `reels[].product_type` | string | 官方字段 `product_type`；官方未单独提供业务说明。 |
| `reels[].video_url` | string | 官方字段 `video_url`；官方未单独提供业务说明。 |
| `reels[].video_versions` | array | 官方字段 `video_versions`；官方未单独提供业务说明。 |
| `reels[].video_versions[].type` | integer | 类型。 |
| `reels[].video_versions[].url` | string | 链接。 |
| `reels[].image_url` | string | 官方字段 `image_url`；官方未单独提供业务说明。 |
| `reels[].image_versions2` | object | 官方字段 `image_versions2`；官方未单独提供业务说明。 |
| `reels[].image_versions2.additional_candidates` | object | 官方字段 `additional_candidates`；官方未单独提供业务说明。 |
| `reels[].image_versions2.additional_candidates.first_frame` | object | 官方字段 `first_frame`；官方未单独提供业务说明。 |
| `reels[].image_versions2.additional_candidates.first_frame.url` | string | 链接。 |
| `reels[].image_versions2.candidates` | array | 官方字段 `candidates`；官方未单独提供业务说明。 |
| `reels[].image_versions2.candidates[].url` | string | 链接。 |
| `reels[].image_versions2.candidates[].height` | integer | 高度。 |
| `reels[].image_versions2.candidates[].width` | integer | 宽度。 |
| `reels[].original_width` | integer | 官方字段 `original_width`；官方未单独提供业务说明。 |
| `reels[].original_height` | integer | 官方字段 `original_height`；官方未单独提供业务说明。 |
| `reels[].has_audio` | boolean | 官方字段 `has_audio`；官方未单独提供业务说明。 |
| `reels[].like_count` | integer | 点赞数量。 |
| `reels[].comment_count` | integer | 评论数量。 |
| `reels[].play_count` | integer | 播放数量。 |
| `reels[].ig_play_count` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata` | object | 官方字段 `clips_metadata`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.original_sound_info` | object | 官方字段 `original_sound_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.original_sound_info.audio_asset_id` | string | 官方字段 `audio_asset_id`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.original_sound_info.original_audio_title` | string | 官方字段 `original_audio_title`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.original_sound_info.ig_artist` | object | 官方字段 `ig_artist`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.original_sound_info.ig_artist.username` | string | 用户名。 |
| `reels[].clips_metadata.original_sound_info.ig_artist.id` | string | 标识符。 |
| `reels[].clips_metadata.original_sound_info.is_explicit` | boolean | 官方字段 `is_explicit`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.original_sound_info.should_mute_audio` | boolean | 官方字段 `should_mute_audio`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.original_sound_info.consumption_info` | object | 官方字段 `consumption_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.original_sound_info.consumption_info.should_mute_audio_reason` | string | 官方字段 `should_mute_audio_reason`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.original_sound_info.consumption_info.is_trending_in_clips` | boolean | 官方字段 `is_trending_in_clips`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.original_sound_info.audio_filter_infos` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user` | object | 用户信息。 |
| `reels[].user.id` | string | 标识符。 |
| `reels[].user.pk` | string | 主键标识。 |
| `reels[].user.username` | string | 用户名。 |
| `reels[].user.full_name` | string | 完整名称。 |
| `reels[].user.profile_pic_url` | string | 头像链接。 |
| `reels[].user.is_verified` | boolean | 是否认证。 |
| `reels[].user.is_private` | boolean | 是否为私密账号。 |

## 使用要点

- 无必填参数。样本不足时上游可能 503 且不计费。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-reels-trending" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/instagram/reels/trending/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

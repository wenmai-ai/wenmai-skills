# Wenmai SCRAPECREATORS scrapecreators_tiktok_song API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-song`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_song`
- **脚本入口**：`modules/song/scripts/song.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `clipId` | string | 是 | 音乐片段 clipId，不是 songId / music.id。来自 https://www.tiktok.com/music/歌曲名-{clipId}。 |

## 请求示例

```json
{
  "clipId": "7694359127636265750"
}
```

```bash
python3 modules/song/scripts/song.py '{"clipId": "7694359127636265750"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `music_info` | object | 官方字段 `music_info`；官方未单独提供业务说明。 |
| `music_info.album` | string | 官方字段 `album`；官方未单独提供业务说明。 |
| `music_info.allow_offline_music_to_detail_page` | boolean | 官方字段 `allow_offline_music_to_detail_page`；官方未单独提供业务说明。 |
| `music_info.artists` | array | 官方字段 `artists`；官方未单独提供业务说明。 |
| `music_info.artists[].avatar` | object | 头像信息。 |
| `music_info.artists[].avatar.uri` | string | 资源标识。 |
| `music_info.artists[].avatar.url_list` | array | 资源链接列表。 |
| `music_info.artists[].avatar.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.artists[].avatar.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.artists[].enter_type` | integer | 官方字段 `enter_type`；官方未单独提供业务说明。 |
| `music_info.artists[].follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `music_info.artists[].follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `music_info.artists[].handle` | string | 账号名称。 |
| `music_info.artists[].is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `music_info.artists[].is_blocked` | boolean | 官方字段 `is_blocked`；官方未单独提供业务说明。 |
| `music_info.artists[].is_private_account` | boolean | 官方字段 `is_private_account`；官方未单独提供业务说明。 |
| `music_info.artists[].is_verified` | boolean | 是否认证。 |
| `music_info.artists[].is_visible` | boolean | 官方字段 `is_visible`；官方未单独提供业务说明。 |
| `music_info.artists[].nick_name` | string | 官方字段 `nick_name`；官方未单独提供业务说明。 |
| `music_info.artists[].sec_uid` | string | TikTok 安全用户标识。 |
| `music_info.artists[].status` | integer | 状态。 |
| `music_info.artists[].uid` | string | 用户标识。 |
| `music_info.audition_duration` | integer | 官方字段 `audition_duration`；官方未单独提供业务说明。 |
| `music_info.author` | string | 作者信息。 |
| `music_info.author_deleted` | boolean | 官方字段 `author_deleted`；官方未单独提供业务说明。 |
| `music_info.author_position` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.avatar_medium` | object | 中等尺寸头像。 |
| `music_info.avatar_medium.height` | integer | 高度。 |
| `music_info.avatar_medium.uri` | string | 资源标识。 |
| `music_info.avatar_medium.url_list` | array | 资源链接列表。 |
| `music_info.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.avatar_medium.width` | integer | 宽度。 |
| `music_info.avatar_thumb` | object | 缩略头像。 |
| `music_info.avatar_thumb.height` | integer | 高度。 |
| `music_info.avatar_thumb.uri` | string | 资源标识。 |
| `music_info.avatar_thumb.url_list` | array | 资源链接列表。 |
| `music_info.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.avatar_thumb.width` | integer | 宽度。 |
| `music_info.binded_challenge_id` | integer | 官方字段 `binded_challenge_id`；官方未单独提供业务说明。 |
| `music_info.can_be_stitched` | boolean | 官方字段 `can_be_stitched`；官方未单独提供业务说明。 |
| `music_info.can_not_reuse` | boolean | 官方字段 `can_not_reuse`；官方未单独提供业务说明。 |
| `music_info.collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `music_info.commercial_right_type` | integer | 官方字段 `commercial_right_type`；官方未单独提供业务说明。 |
| `music_info.cover_large` | object | 官方字段 `cover_large`；官方未单独提供业务说明。 |
| `music_info.cover_large.height` | integer | 高度。 |
| `music_info.cover_large.uri` | string | 资源标识。 |
| `music_info.cover_large.url_list` | array | 资源链接列表。 |
| `music_info.cover_large.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.cover_large.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.cover_large.width` | integer | 宽度。 |
| `music_info.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `music_info.cover_medium.height` | integer | 高度。 |
| `music_info.cover_medium.uri` | string | 资源标识。 |
| `music_info.cover_medium.url_list` | array | 资源链接列表。 |
| `music_info.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.cover_medium.width` | integer | 宽度。 |
| `music_info.cover_thumb` | object | 官方字段 `cover_thumb`；官方未单独提供业务说明。 |
| `music_info.cover_thumb.height` | integer | 高度。 |
| `music_info.cover_thumb.uri` | string | 资源标识。 |
| `music_info.cover_thumb.url_list` | array | 资源链接列表。 |
| `music_info.cover_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.cover_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.cover_thumb.width` | integer | 宽度。 |
| `music_info.create_time` | integer | 创建时间。 |
| `music_info.dmv_auto_show` | boolean | 官方字段 `dmv_auto_show`；官方未单独提供业务说明。 |
| `music_info.duration` | integer | 时长。 |
| `music_info.duration_high_precision` | object | 官方字段 `duration_high_precision`；官方未单独提供业务说明。 |
| `music_info.duration_high_precision.audition_duration_precision` | integer | 官方字段 `audition_duration_precision`；官方未单独提供业务说明。 |
| `music_info.duration_high_precision.duration_precision` | integer | 官方字段 `duration_precision`；官方未单独提供业务说明。 |
| `music_info.duration_high_precision.shoot_duration_precision` | integer | 官方字段 `shoot_duration_precision`；官方未单独提供业务说明。 |
| `music_info.duration_high_precision.video_duration_precision` | integer | 官方字段 `video_duration_precision`；官方未单独提供业务说明。 |
| `music_info.external_song_info` | array | 官方示例为空数组，未提供元素结构。 |
| `music_info.extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `music_info.full_song` | object | 官方字段 `full_song`；官方未单独提供业务说明。 |
| `music_info.full_song.full_song_duration` | integer | 官方字段 `full_song_duration`；官方未单独提供业务说明。 |
| `music_info.full_song.full_song_duration_precision` | number | 官方字段 `full_song_duration_precision`；官方未单独提供业务说明。 |
| `music_info.full_song.full_song_id` | string | 官方字段 `full_song_id`；官方未单独提供业务说明。 |
| `music_info.full_song.full_song_play_url` | object | 官方字段 `full_song_play_url`；官方未单独提供业务说明。 |
| `music_info.full_song.full_song_play_url.uri` | string | 资源标识。 |
| `music_info.full_song.full_song_play_url.url_list` | array | 资源链接列表。 |
| `music_info.full_song.full_song_play_url.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.full_song.full_song_play_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.full_song.full_song_shoot_duration` | integer | 官方字段 `full_song_shoot_duration`；官方未单独提供业务说明。 |
| `music_info.full_song.full_song_shoot_duration_precision` | integer | 官方字段 `full_song_shoot_duration_precision`；官方未单独提供业务说明。 |
| `music_info.has_commerce_right` | boolean | 官方字段 `has_commerce_right`；官方未单独提供业务说明。 |
| `music_info.id` | integer | 标识符。 |
| `music_info.id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `music_info.is_audio_url_with_cookie` | boolean | 官方字段 `is_audio_url_with_cookie`；官方未单独提供业务说明。 |
| `music_info.is_author_artist` | boolean | 官方字段 `is_author_artist`；官方未单独提供业务说明。 |
| `music_info.is_commerce_music` | boolean | 官方字段 `is_commerce_music`；官方未单独提供业务说明。 |
| `music_info.is_matched_metadata` | boolean | 官方字段 `is_matched_metadata`；官方未单独提供业务说明。 |
| `music_info.is_original` | boolean | 官方字段 `is_original`；官方未单独提供业务说明。 |
| `music_info.is_original_sound` | boolean | 官方字段 `is_original_sound`；官方未单独提供业务说明。 |
| `music_info.is_pgc` | boolean | 官方字段 `is_pgc`；官方未单独提供业务说明。 |
| `music_info.is_shooting_allow` | boolean | 官方字段 `is_shooting_allow`；官方未单独提供业务说明。 |
| `music_info.log_extra` | string | 官方字段 `log_extra`；官方未单独提供业务说明。 |
| `music_info.lyric_short_position` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.matched_song` | object | 官方字段 `matched_song`；官方未单独提供业务说明。 |
| `music_info.matched_song.author` | string | 作者信息。 |
| `music_info.matched_song.chorus_info` | object | 官方字段 `chorus_info`；官方未单独提供业务说明。 |
| `music_info.matched_song.chorus_info.duration_ms` | integer | 官方字段 `duration_ms`；官方未单独提供业务说明。 |
| `music_info.matched_song.chorus_info.start_ms` | integer | 官方字段 `start_ms`；官方未单独提供业务说明。 |
| `music_info.matched_song.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `music_info.matched_song.cover_medium.height` | integer | 高度。 |
| `music_info.matched_song.cover_medium.uri` | string | 资源标识。 |
| `music_info.matched_song.cover_medium.url_list` | array | 资源链接列表。 |
| `music_info.matched_song.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.matched_song.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.matched_song.cover_medium.width` | integer | 宽度。 |
| `music_info.matched_song.full_duration` | integer | 官方字段 `full_duration`；官方未单独提供业务说明。 |
| `music_info.matched_song.h5_url` | string | 官方字段 `h5_url`；官方未单独提供业务说明。 |
| `music_info.matched_song.id` | string | 标识符。 |
| `music_info.matched_song.performers` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.matched_song.title` | string | 标题。 |
| `music_info.meme_song_info` | object | 官方示例为空对象，未提供子字段。 |
| `music_info.mid` | string | 官方字段 `mid`；官方未单独提供业务说明。 |
| `music_info.music_release_info` | object | 官方字段 `music_release_info`；官方未单独提供业务说明。 |
| `music_info.music_release_info.group_release_date` | integer | 官方字段 `group_release_date`；官方未单独提供业务说明。 |
| `music_info.music_release_info.is_new_release_song` | boolean | 官方字段 `is_new_release_song`；官方未单独提供业务说明。 |
| `music_info.mute_share` | boolean | 官方字段 `mute_share`；官方未单独提供业务说明。 |
| `music_info.offline_desc` | string | 官方字段 `offline_desc`；官方未单独提供业务说明。 |
| `music_info.owner_handle` | string | 官方字段 `owner_handle`；官方未单独提供业务说明。 |
| `music_info.owner_nickname` | string | 官方字段 `owner_nickname`；官方未单独提供业务说明。 |
| `music_info.play_url` | object | 官方字段 `play_url`；官方未单独提供业务说明。 |
| `music_info.play_url.height` | integer | 高度。 |
| `music_info.play_url.uri` | string | 资源标识。 |
| `music_info.play_url.url_list` | array | 资源链接列表。 |
| `music_info.play_url.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.play_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.play_url.width` | integer | 宽度。 |
| `music_info.position` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `music_info.preview_end_time` | integer | 官方字段 `preview_end_time`；官方未单独提供业务说明。 |
| `music_info.preview_start_time` | integer | 官方字段 `preview_start_time`；官方未单独提供业务说明。 |
| `music_info.recommend_status` | integer | 官方字段 `recommend_status`；官方未单独提供业务说明。 |
| `music_info.share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `music_info.share_info.bool_persist` | integer | 官方字段 `bool_persist`；官方未单独提供业务说明。 |
| `music_info.share_info.now_invitation_card_image_urls` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.share_info.share_desc` | string | 官方字段 `share_desc`；官方未单独提供业务说明。 |
| `music_info.share_info.share_desc_info` | string | 官方字段 `share_desc_info`；官方未单独提供业务说明。 |
| `music_info.share_info.share_quote` | string | 官方字段 `share_quote`；官方未单独提供业务说明。 |
| `music_info.share_info.share_signature_desc` | string | 官方字段 `share_signature_desc`；官方未单独提供业务说明。 |
| `music_info.share_info.share_signature_url` | string | 官方字段 `share_signature_url`；官方未单独提供业务说明。 |
| `music_info.share_info.share_title` | string | 官方字段 `share_title`；官方未单独提供业务说明。 |
| `music_info.share_info.share_title_myself` | string | 官方字段 `share_title_myself`；官方未单独提供业务说明。 |
| `music_info.share_info.share_title_other` | string | 官方字段 `share_title_other`；官方未单独提供业务说明。 |
| `music_info.share_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `music_info.shoot_duration` | integer | 官方字段 `shoot_duration`；官方未单独提供业务说明。 |
| `music_info.source_platform` | integer | 官方字段 `source_platform`；官方未单独提供业务说明。 |
| `music_info.status` | integer | 状态。 |
| `music_info.strong_beat_url` | object | 官方字段 `strong_beat_url`；官方未单独提供业务说明。 |
| `music_info.strong_beat_url.height` | integer | 高度。 |
| `music_info.strong_beat_url.uri` | string | 资源标识。 |
| `music_info.strong_beat_url.url_list` | array | 资源链接列表。 |
| `music_info.strong_beat_url.url_list[]` | string | 资源链接列表中的元素。 |
| `music_info.strong_beat_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.strong_beat_url.width` | integer | 宽度。 |
| `music_info.suggest_words` | object | 官方字段 `suggest_words`；官方未单独提供业务说明。 |
| `music_info.suggest_words.suggest_words` | array | 官方字段 `suggest_words`；官方未单独提供业务说明。 |
| `music_info.suggest_words.suggest_words[].scene` | string | 官方字段 `scene`；官方未单独提供业务说明。 |
| `music_info.suggest_words.suggest_words[].words` | array | 官方字段 `words`；官方未单独提供业务说明。 |
| `music_info.suggest_words.suggest_words[].words[].word` | string | 官方字段 `word`；官方未单独提供业务说明。 |
| `music_info.suggest_words.suggest_words[].words[].word_id` | string | 官方字段 `word_id`；官方未单独提供业务说明。 |
| `music_info.tag_list` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.title` | string | 标题。 |
| `music_info.tt_to_dsp_song_infos` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.uncert_artists` | null | 官方示例为 null，未说明非空类型。 |
| `music_info.user_count` | integer | 官方字段 `user_count`；官方未单独提供业务说明。 |
| `music_info.vid_volume_info` | string | 官方字段 `vid_volume_info`；官方未单独提供业务说明。 |
| `music_info.video_duration` | integer | 视频时长。 |
| `rec_list` | array | 官方示例为空数组，未提供元素结构。 |
| `similar_music` | array | 官方示例为空数组，未提供元素结构。 |
| `similar_music_ids` | null | 官方示例为 null，未说明非空类型。 |
| `status_code` | integer | 状态码。 |
| `status_msg` | string | 状态说明。 |

## 使用要点

- 必须传音乐 URL 上的 clipId，不要传 music.id。每次成功扣 3 稳卖积分。
- 顶层直接传业务字段，不要增加 `request` 包装层。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、clipId、handle、视频链接和分页。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-song" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"clipId": "7694359127636265750"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/song/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

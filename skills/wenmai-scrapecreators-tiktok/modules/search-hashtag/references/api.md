# Wenmai SCRAPECREATORS scrapecreators_tiktok_search_hashtag API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-search-hashtag`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_search_hashtag`
- **脚本入口**：`modules/search-hashtag/scripts/search_hashtag.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `hashtag` | string | 是 | 话题名，不要带 #。 |
| `region` | string | 否 | 代理所在地区，两位国家码。不是只返回该地区作品，只是把代理放到该地区。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |
| `cursor` | number | 否 | 分页游标，传入上一页响应中的 cursor。 |

## 请求示例

```json
{
  "hashtag": "amazonfinds",
  "trim": true
}
```

```bash
python3 modules/search-hashtag/scripts/search_hashtag.py '{"hashtag": "amazonfinds", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `aweme_list` | array | TikTok 视频列表。 |
| `aweme_list[].add_yours_info` | object | 官方字段 `add_yours_info`；官方未单独提供业务说明。 |
| `aweme_list[].add_yours_info.video_source` | integer | 官方字段 `video_source`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info` | object | 官方字段 `added_sound_music_info`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.album` | string | 官方字段 `album`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists` | array | 官方字段 `artists`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists[].avatar` | object | 头像信息。 |
| `aweme_list[].added_sound_music_info.artists[].avatar.uri` | string | 资源标识。 |
| `aweme_list[].added_sound_music_info.artists[].avatar.url_list` | array | 资源链接列表。 |
| `aweme_list[].added_sound_music_info.artists[].avatar.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].added_sound_music_info.artists[].avatar.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.artists[].enter_type` | integer | 官方字段 `enter_type`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists[].follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists[].follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists[].handle` | string | 账号名称。 |
| `aweme_list[].added_sound_music_info.artists[].is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists[].is_blocked` | boolean | 官方字段 `is_blocked`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists[].is_private_account` | boolean | 官方字段 `is_private_account`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists[].is_verified` | boolean | 是否认证。 |
| `aweme_list[].added_sound_music_info.artists[].is_visible` | boolean | 官方字段 `is_visible`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists[].nick_name` | string | 官方字段 `nick_name`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.artists[].sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_list[].added_sound_music_info.artists[].status` | integer | 状态。 |
| `aweme_list[].added_sound_music_info.artists[].uid` | string | 用户标识。 |
| `aweme_list[].added_sound_music_info.audition_duration` | integer | 官方字段 `audition_duration`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.author` | string | 作者信息。 |
| `aweme_list[].added_sound_music_info.author_deleted` | boolean | 官方字段 `author_deleted`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.author_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.avatar_medium` | object | 中等尺寸头像。 |
| `aweme_list[].added_sound_music_info.avatar_medium.height` | integer | 高度。 |
| `aweme_list[].added_sound_music_info.avatar_medium.uri` | string | 资源标识。 |
| `aweme_list[].added_sound_music_info.avatar_medium.url_list` | array | 资源链接列表。 |
| `aweme_list[].added_sound_music_info.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].added_sound_music_info.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.avatar_medium.width` | integer | 宽度。 |
| `aweme_list[].added_sound_music_info.avatar_thumb` | object | 缩略头像。 |
| `aweme_list[].added_sound_music_info.avatar_thumb.height` | integer | 高度。 |
| `aweme_list[].added_sound_music_info.avatar_thumb.uri` | string | 资源标识。 |
| `aweme_list[].added_sound_music_info.avatar_thumb.url_list` | array | 资源链接列表。 |
| `aweme_list[].added_sound_music_info.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].added_sound_music_info.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.avatar_thumb.width` | integer | 宽度。 |
| `aweme_list[].added_sound_music_info.binded_challenge_id` | integer | 官方字段 `binded_challenge_id`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.can_not_reuse` | boolean | 官方字段 `can_not_reuse`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.commercial_right_type` | integer | 官方字段 `commercial_right_type`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.cover_large` | object | 官方字段 `cover_large`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.cover_large.height` | integer | 高度。 |
| `aweme_list[].added_sound_music_info.cover_large.uri` | string | 资源标识。 |
| `aweme_list[].added_sound_music_info.cover_large.url_list` | array | 资源链接列表。 |
| `aweme_list[].added_sound_music_info.cover_large.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].added_sound_music_info.cover_large.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.cover_large.width` | integer | 宽度。 |
| `aweme_list[].added_sound_music_info.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.cover_medium.height` | integer | 高度。 |
| `aweme_list[].added_sound_music_info.cover_medium.uri` | string | 资源标识。 |
| `aweme_list[].added_sound_music_info.cover_medium.url_list` | array | 资源链接列表。 |
| `aweme_list[].added_sound_music_info.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].added_sound_music_info.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.cover_medium.width` | integer | 宽度。 |
| `aweme_list[].added_sound_music_info.cover_thumb` | object | 官方字段 `cover_thumb`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.cover_thumb.height` | integer | 高度。 |
| `aweme_list[].added_sound_music_info.cover_thumb.uri` | string | 资源标识。 |
| `aweme_list[].added_sound_music_info.cover_thumb.url_list` | array | 资源链接列表。 |
| `aweme_list[].added_sound_music_info.cover_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].added_sound_music_info.cover_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.cover_thumb.width` | integer | 宽度。 |
| `aweme_list[].added_sound_music_info.dmv_auto_show` | boolean | 官方字段 `dmv_auto_show`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.duration` | integer | 时长。 |
| `aweme_list[].added_sound_music_info.duration_high_precision` | object | 官方字段 `duration_high_precision`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.duration_high_precision.audition_duration_precision` | integer | 官方字段 `audition_duration_precision`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.duration_high_precision.duration_precision` | integer | 官方字段 `duration_precision`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.duration_high_precision.shoot_duration_precision` | integer | 官方字段 `shoot_duration_precision`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.duration_high_precision.video_duration_precision` | integer | 官方字段 `video_duration_precision`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.external_song_info` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].added_sound_music_info.extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.has_commerce_right` | boolean | 官方字段 `has_commerce_right`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.id` | integer | 标识符。 |
| `aweme_list[].added_sound_music_info.id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.is_audio_url_with_cookie` | boolean | 官方字段 `is_audio_url_with_cookie`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.is_author_artist` | boolean | 官方字段 `is_author_artist`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.is_commerce_music` | boolean | 官方字段 `is_commerce_music`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.is_matched_metadata` | boolean | 官方字段 `is_matched_metadata`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.is_original` | boolean | 官方字段 `is_original`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.is_original_sound` | boolean | 官方字段 `is_original_sound`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.is_pgc` | boolean | 官方字段 `is_pgc`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.is_play_music` | boolean | 官方字段 `is_play_music`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.is_shooting_allow` | boolean | 官方字段 `is_shooting_allow`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.language` | string | 语言。 |
| `aweme_list[].added_sound_music_info.log_extra` | string | 官方字段 `log_extra`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.lyric_short_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.matched_song` | object | 官方字段 `matched_song`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.matched_song.author` | string | 作者信息。 |
| `aweme_list[].added_sound_music_info.matched_song.chorus_info` | object | 官方字段 `chorus_info`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.matched_song.chorus_info.duration_ms` | integer | 官方字段 `duration_ms`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.matched_song.chorus_info.start_ms` | integer | 官方字段 `start_ms`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.matched_song.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.matched_song.cover_medium.height` | integer | 高度。 |
| `aweme_list[].added_sound_music_info.matched_song.cover_medium.uri` | string | 资源标识。 |
| `aweme_list[].added_sound_music_info.matched_song.cover_medium.url_list` | array | 资源链接列表。 |
| `aweme_list[].added_sound_music_info.matched_song.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].added_sound_music_info.matched_song.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.matched_song.cover_medium.width` | integer | 宽度。 |
| `aweme_list[].added_sound_music_info.matched_song.full_duration` | integer | 官方字段 `full_duration`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.matched_song.h5_url` | string | 官方字段 `h5_url`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.matched_song.id` | string | 标识符。 |
| `aweme_list[].added_sound_music_info.matched_song.performers` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.matched_song.title` | string | 标题。 |
| `aweme_list[].added_sound_music_info.meme_song_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_list[].added_sound_music_info.mid` | string | 官方字段 `mid`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.multi_bit_rate_play_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.music_release_info` | object | 官方字段 `music_release_info`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.music_release_info.group_release_date` | integer | 官方字段 `group_release_date`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.music_release_info.is_new_release_song` | boolean | 官方字段 `is_new_release_song`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.mute_share` | boolean | 官方字段 `mute_share`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.offline_desc` | string | 官方字段 `offline_desc`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.owner_handle` | string | 官方字段 `owner_handle`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.owner_nickname` | string | 官方字段 `owner_nickname`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.play_url` | object | 官方字段 `play_url`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.play_url.height` | integer | 高度。 |
| `aweme_list[].added_sound_music_info.play_url.uri` | string | 资源标识。 |
| `aweme_list[].added_sound_music_info.play_url.url_list` | array | 资源链接列表。 |
| `aweme_list[].added_sound_music_info.play_url.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].added_sound_music_info.play_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.play_url.width` | integer | 宽度。 |
| `aweme_list[].added_sound_music_info.position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.preview_end_time` | integer | 官方字段 `preview_end_time`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.preview_start_time` | number | 官方字段 `preview_start_time`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.recommend_status` | integer | 官方字段 `recommend_status`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.shoot_duration` | integer | 官方字段 `shoot_duration`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.source_platform` | integer | 官方字段 `source_platform`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.status` | integer | 状态。 |
| `aweme_list[].added_sound_music_info.strong_beat_url` | object | 官方字段 `strong_beat_url`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.strong_beat_url.height` | integer | 高度。 |
| `aweme_list[].added_sound_music_info.strong_beat_url.uri` | string | 资源标识。 |
| `aweme_list[].added_sound_music_info.strong_beat_url.url_list` | array | 资源链接列表。 |
| `aweme_list[].added_sound_music_info.strong_beat_url.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].added_sound_music_info.strong_beat_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.strong_beat_url.width` | integer | 宽度。 |
| `aweme_list[].added_sound_music_info.style_value` | array | 官方字段 `style_value`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.style_value[]` | integer | 官方数组 `style_value` 的元素。 |
| `aweme_list[].added_sound_music_info.tag_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.theme_value` | array | 官方字段 `theme_value`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.theme_value[]` | integer | 官方数组 `theme_value` 的元素。 |
| `aweme_list[].added_sound_music_info.title` | string | 标题。 |
| `aweme_list[].added_sound_music_info.tt_to_dsp_song_infos` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.uncert_artists` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].added_sound_music_info.user_count` | integer | 官方字段 `user_count`；官方未单独提供业务说明。 |
| `aweme_list[].added_sound_music_info.video_duration` | integer | 视频时长。 |
| `aweme_list[].aigc_info` | object | 官方字段 `aigc_info`；官方未单独提供业务说明。 |
| `aweme_list[].aigc_info.aigc_label_type` | integer | 官方字段 `aigc_label_type`；官方未单独提供业务说明。 |
| `aweme_list[].aigc_info.created_by_ai` | boolean | 官方字段 `created_by_ai`；官方未单独提供业务说明。 |
| `aweme_list[].anchors` | array | 官方字段 `anchors`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].actions` | array | 官方字段 `actions`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].actions[].action_type` | integer | 官方字段 `action_type`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].actions[].icon` | object | 官方字段 `icon`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].actions[].icon.height` | integer | 高度。 |
| `aweme_list[].anchors[].actions[].icon.uri` | string | 资源标识。 |
| `aweme_list[].anchors[].actions[].icon.url_list` | array | 资源链接列表。 |
| `aweme_list[].anchors[].actions[].icon.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].anchors[].actions[].icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].anchors[].actions[].icon.width` | integer | 宽度。 |
| `aweme_list[].anchors[].actions[].schema` | string | 官方字段 `schema`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].anchor_strong` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].anchors[].component_key` | string | 官方字段 `component_key`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].description` | string | 描述。 |
| `aweme_list[].anchors[].extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].icon` | object | 官方字段 `icon`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].icon.height` | integer | 高度。 |
| `aweme_list[].anchors[].icon.uri` | string | 资源标识。 |
| `aweme_list[].anchors[].icon.url_list` | array | 资源链接列表。 |
| `aweme_list[].anchors[].icon.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].anchors[].icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].anchors[].icon.width` | integer | 宽度。 |
| `aweme_list[].anchors[].id` | string | 标识符。 |
| `aweme_list[].anchors[].keyword` | string | 官方字段 `keyword`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].log_extra` | string | 官方字段 `log_extra`；官方未单独提供业务说明。 |
| `aweme_list[].anchors[].thumbnail` | object | 缩略图。 |
| `aweme_list[].anchors[].thumbnail.height` | integer | 高度。 |
| `aweme_list[].anchors[].thumbnail.uri` | string | 资源标识。 |
| `aweme_list[].anchors[].thumbnail.url_list` | array | 资源链接列表。 |
| `aweme_list[].anchors[].thumbnail.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].anchors[].thumbnail.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].anchors[].thumbnail.width` | integer | 宽度。 |
| `aweme_list[].anchors[].type` | integer | 类型。 |
| `aweme_list[].anchors_extras` | string | 官方字段 `anchors_extras`；官方未单独提供业务说明。 |
| `aweme_list[].animated_image_info` | object | 官方字段 `animated_image_info`；官方未单独提供业务说明。 |
| `aweme_list[].animated_image_info.effect` | integer | 官方字段 `effect`；官方未单独提供业务说明。 |
| `aweme_list[].animated_image_info.type` | integer | 类型。 |
| `aweme_list[].author` | object | 作者信息。 |
| `aweme_list[].author.accept_private_policy` | boolean | 官方字段 `accept_private_policy`；官方未单独提供业务说明。 |
| `aweme_list[].author.account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.account_region` | string | 官方字段 `account_region`；官方未单独提供业务说明。 |
| `aweme_list[].author.ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.apple_account` | integer | 官方字段 `apple_account`；官方未单独提供业务说明。 |
| `aweme_list[].author.authority_status` | integer | 官方字段 `authority_status`；官方未单独提供业务说明。 |
| `aweme_list[].author.avatar_168x168` | object | 官方字段 `avatar_168x168`；官方未单独提供业务说明。 |
| `aweme_list[].author.avatar_168x168.height` | integer | 高度。 |
| `aweme_list[].author.avatar_168x168.uri` | string | 资源标识。 |
| `aweme_list[].author.avatar_168x168.url_list` | array | 资源链接列表。 |
| `aweme_list[].author.avatar_168x168.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].author.avatar_168x168.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.avatar_168x168.width` | integer | 宽度。 |
| `aweme_list[].author.avatar_300x300` | object | 官方字段 `avatar_300x300`；官方未单独提供业务说明。 |
| `aweme_list[].author.avatar_300x300.height` | integer | 高度。 |
| `aweme_list[].author.avatar_300x300.uri` | string | 资源标识。 |
| `aweme_list[].author.avatar_300x300.url_list` | array | 资源链接列表。 |
| `aweme_list[].author.avatar_300x300.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].author.avatar_300x300.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.avatar_300x300.width` | integer | 宽度。 |
| `aweme_list[].author.avatar_larger` | object | 官方字段 `avatar_larger`；官方未单独提供业务说明。 |
| `aweme_list[].author.avatar_larger.height` | integer | 高度。 |
| `aweme_list[].author.avatar_larger.uri` | string | 资源标识。 |
| `aweme_list[].author.avatar_larger.url_list` | array | 资源链接列表。 |
| `aweme_list[].author.avatar_larger.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].author.avatar_larger.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.avatar_larger.width` | integer | 宽度。 |
| `aweme_list[].author.avatar_medium` | object | 中等尺寸头像。 |
| `aweme_list[].author.avatar_medium.height` | integer | 高度。 |
| `aweme_list[].author.avatar_medium.uri` | string | 资源标识。 |
| `aweme_list[].author.avatar_medium.url_list` | array | 资源链接列表。 |
| `aweme_list[].author.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].author.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.avatar_medium.width` | integer | 宽度。 |
| `aweme_list[].author.avatar_thumb` | object | 缩略头像。 |
| `aweme_list[].author.avatar_thumb.height` | integer | 高度。 |
| `aweme_list[].author.avatar_thumb.uri` | string | 资源标识。 |
| `aweme_list[].author.avatar_thumb.url_list` | array | 资源链接列表。 |
| `aweme_list[].author.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].author.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.avatar_thumb.width` | integer | 宽度。 |
| `aweme_list[].author.avatar_uri` | string | 官方字段 `avatar_uri`；官方未单独提供业务说明。 |
| `aweme_list[].author.aweme_count` | integer | 官方字段 `aweme_count`；官方未单独提供业务说明。 |
| `aweme_list[].author.bind_phone` | string | 官方字段 `bind_phone`；官方未单独提供业务说明。 |
| `aweme_list[].author.bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.can_message_follow_status_list` | array | 官方字段 `can_message_follow_status_list`；官方未单独提供业务说明。 |
| `aweme_list[].author.can_message_follow_status_list[]` | integer | 官方数组 `can_message_follow_status_list` 的元素。 |
| `aweme_list[].author.can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.comment_filter_status` | integer | 官方字段 `comment_filter_status`；官方未单独提供业务说明。 |
| `aweme_list[].author.comment_setting` | integer | 官方字段 `comment_setting`；官方未单独提供业务说明。 |
| `aweme_list[].author.commerce_user_level` | integer | 官方字段 `commerce_user_level`；官方未单独提供业务说明。 |
| `aweme_list[].author.cover_url` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].author.create_time` | integer | 创建时间。 |
| `aweme_list[].author.custom_verify` | string | 官方字段 `custom_verify`；官方未单独提供业务说明。 |
| `aweme_list[].author.cv_level` | string | 官方字段 `cv_level`；官方未单独提供业务说明。 |
| `aweme_list[].author.download_prompt_ts` | integer | 官方字段 `download_prompt_ts`；官方未单独提供业务说明。 |
| `aweme_list[].author.download_setting` | integer | 官方字段 `download_setting`；官方未单独提供业务说明。 |
| `aweme_list[].author.duet_setting` | integer | 官方字段 `duet_setting`；官方未单独提供业务说明。 |
| `aweme_list[].author.enabled_filter_all_comments` | boolean | 官方字段 `enabled_filter_all_comments`；官方未单独提供业务说明。 |
| `aweme_list[].author.enterprise_verify_reason` | string | 官方字段 `enterprise_verify_reason`；官方未单独提供业务说明。 |
| `aweme_list[].author.events` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.fake_data_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_list[].author.favoriting_count` | integer | 官方字段 `favoriting_count`；官方未单独提供业务说明。 |
| `aweme_list[].author.fb_expire_time` | integer | 官方字段 `fb_expire_time`；官方未单独提供业务说明。 |
| `aweme_list[].author.follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `aweme_list[].author.follower_count` | integer | 粉丝数量。 |
| `aweme_list[].author.follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `aweme_list[].author.followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.following_count` | integer | 关注数量。 |
| `aweme_list[].author.friends_status` | integer | 官方字段 `friends_status`；官方未单独提供业务说明。 |
| `aweme_list[].author.gender` | integer | 官方字段 `gender`；官方未单独提供业务说明。 |
| `aweme_list[].author.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.google_account` | string | 官方字段 `google_account`；官方未单独提供业务说明。 |
| `aweme_list[].author.has_email` | boolean | 官方字段 `has_email`；官方未单独提供业务说明。 |
| `aweme_list[].author.has_facebook_token` | boolean | 官方字段 `has_facebook_token`；官方未单独提供业务说明。 |
| `aweme_list[].author.has_insights` | boolean | 官方字段 `has_insights`；官方未单独提供业务说明。 |
| `aweme_list[].author.has_orders` | boolean | 官方字段 `has_orders`；官方未单独提供业务说明。 |
| `aweme_list[].author.has_twitter_token` | boolean | 官方字段 `has_twitter_token`；官方未单独提供业务说明。 |
| `aweme_list[].author.has_youtube_token` | boolean | 官方字段 `has_youtube_token`；官方未单独提供业务说明。 |
| `aweme_list[].author.hide_search` | boolean | 官方字段 `hide_search`；官方未单独提供业务说明。 |
| `aweme_list[].author.homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.ins_id` | string | 官方字段 `ins_id`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_ad_fake` | boolean | 官方字段 `is_ad_fake`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_discipline_member` | boolean | 官方字段 `is_discipline_member`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_mute` | integer | 官方字段 `is_mute`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_phone_binded` | boolean | 官方字段 `is_phone_binded`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_star` | boolean | 官方字段 `is_star`；官方未单独提供业务说明。 |
| `aweme_list[].author.item_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.language` | string | 语言。 |
| `aweme_list[].author.live_agreement` | integer | 官方字段 `live_agreement`；官方未单独提供业务说明。 |
| `aweme_list[].author.live_commerce` | boolean | 官方字段 `live_commerce`；官方未单独提供业务说明。 |
| `aweme_list[].author.live_verify` | integer | 官方字段 `live_verify`；官方未单独提供业务说明。 |
| `aweme_list[].author.mention_status` | integer | 官方字段 `mention_status`；官方未单独提供业务说明。 |
| `aweme_list[].author.mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.need_points` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.need_recommend` | integer | 官方字段 `need_recommend`；官方未单独提供业务说明。 |
| `aweme_list[].author.nickname` | string | 昵称。 |
| `aweme_list[].author.platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `aweme_list[].author.react_setting` | integer | 官方字段 `react_setting`；官方未单独提供业务说明。 |
| `aweme_list[].author.region` | string | 地区。 |
| `aweme_list[].author.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.reply_with_video_flag` | integer | 官方字段 `reply_with_video_flag`；官方未单独提供业务说明。 |
| `aweme_list[].author.room_id` | integer | 官方字段 `room_id`；官方未单独提供业务说明。 |
| `aweme_list[].author.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_list[].author.secret` | integer | 官方字段 `secret`；官方未单独提供业务说明。 |
| `aweme_list[].author.share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `aweme_list[].author.share_info.now_invitation_card_image_urls` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.share_info.share_desc` | string | 官方字段 `share_desc`；官方未单独提供业务说明。 |
| `aweme_list[].author.share_info.share_desc_info` | string | 官方字段 `share_desc_info`；官方未单独提供业务说明。 |
| `aweme_list[].author.share_info.share_qrcode_url` | object | 官方字段 `share_qrcode_url`；官方未单独提供业务说明。 |
| `aweme_list[].author.share_info.share_qrcode_url.height` | integer | 高度。 |
| `aweme_list[].author.share_info.share_qrcode_url.uri` | string | 资源标识。 |
| `aweme_list[].author.share_info.share_qrcode_url.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].author.share_info.share_qrcode_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.share_info.share_qrcode_url.width` | integer | 宽度。 |
| `aweme_list[].author.share_info.share_title` | string | 官方字段 `share_title`；官方未单独提供业务说明。 |
| `aweme_list[].author.share_info.share_title_myself` | string | 官方字段 `share_title_myself`；官方未单独提供业务说明。 |
| `aweme_list[].author.share_info.share_title_other` | string | 官方字段 `share_title_other`；官方未单独提供业务说明。 |
| `aweme_list[].author.share_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `aweme_list[].author.share_qrcode_uri` | string | 官方字段 `share_qrcode_uri`；官方未单独提供业务说明。 |
| `aweme_list[].author.shield_comment_notice` | integer | 官方字段 `shield_comment_notice`；官方未单独提供业务说明。 |
| `aweme_list[].author.shield_digg_notice` | integer | 官方字段 `shield_digg_notice`；官方未单独提供业务说明。 |
| `aweme_list[].author.shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.shield_follow_notice` | integer | 官方字段 `shield_follow_notice`；官方未单独提供业务说明。 |
| `aweme_list[].author.short_id` | string | 官方字段 `short_id`；官方未单独提供业务说明。 |
| `aweme_list[].author.show_image_bubble` | boolean | 官方字段 `show_image_bubble`；官方未单独提供业务说明。 |
| `aweme_list[].author.signature` | string | 官方字段 `signature`；官方未单独提供业务说明。 |
| `aweme_list[].author.special_account` | object | 官方字段 `special_account`；官方未单独提供业务说明。 |
| `aweme_list[].author.special_account.special_account_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.special_lock` | integer | 官方字段 `special_lock`；官方未单独提供业务说明。 |
| `aweme_list[].author.status` | integer | 状态。 |
| `aweme_list[].author.stitch_setting` | integer | 官方字段 `stitch_setting`；官方未单独提供业务说明。 |
| `aweme_list[].author.total_favorited` | integer | 官方字段 `total_favorited`；官方未单独提供业务说明。 |
| `aweme_list[].author.tw_expire_time` | integer | 官方字段 `tw_expire_time`；官方未单独提供业务说明。 |
| `aweme_list[].author.twitter_id` | string | 官方字段 `twitter_id`；官方未单独提供业务说明。 |
| `aweme_list[].author.twitter_name` | string | 官方字段 `twitter_name`；官方未单独提供业务说明。 |
| `aweme_list[].author.type_label` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.uid` | string | 用户标识。 |
| `aweme_list[].author.unique_id` | string | 账号唯一名称。 |
| `aweme_list[].author.unique_id_modify_time` | integer | 官方字段 `unique_id_modify_time`；官方未单独提供业务说明。 |
| `aweme_list[].author.user_canceled` | boolean | 官方字段 `user_canceled`；官方未单独提供业务说明。 |
| `aweme_list[].author.user_mode` | integer | 官方字段 `user_mode`；官方未单独提供业务说明。 |
| `aweme_list[].author.user_now_pack_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_list[].author.user_period` | integer | 官方字段 `user_period`；官方未单独提供业务说明。 |
| `aweme_list[].author.user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.user_rate` | integer | 官方字段 `user_rate`；官方未单独提供业务说明。 |
| `aweme_list[].author.user_spark_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_list[].author.user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.verification_type` | integer | 官方字段 `verification_type`；官方未单独提供业务说明。 |
| `aweme_list[].author.verify_info` | string | 官方字段 `verify_info`；官方未单独提供业务说明。 |
| `aweme_list[].author.video_icon` | object | 官方字段 `video_icon`；官方未单独提供业务说明。 |
| `aweme_list[].author.video_icon.height` | integer | 高度。 |
| `aweme_list[].author.video_icon.uri` | string | 资源标识。 |
| `aweme_list[].author.video_icon.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].author.video_icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.video_icon.width` | integer | 宽度。 |
| `aweme_list[].author.white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.with_commerce_entry` | boolean | 官方字段 `with_commerce_entry`；官方未单独提供业务说明。 |
| `aweme_list[].author.with_shop_entry` | boolean | 官方字段 `with_shop_entry`；官方未单独提供业务说明。 |
| `aweme_list[].author.youtube_channel_id` | string | 官方字段 `youtube_channel_id`；官方未单独提供业务说明。 |
| `aweme_list[].author.youtube_channel_title` | string | 官方字段 `youtube_channel_title`；官方未单独提供业务说明。 |
| `aweme_list[].author.youtube_expire_time` | integer | 官方字段 `youtube_expire_time`；官方未单独提供业务说明。 |
| `aweme_list[].author_user_id` | integer | 官方字段 `author_user_id`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl` | object | 官方字段 `aweme_acl`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.download_general` | object | 官方字段 `download_general`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.download_general.code` | integer | 官方业务编码。 |
| `aweme_list[].aweme_acl.download_general.mute` | boolean | 官方字段 `mute`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.download_general.show_type` | integer | 官方字段 `show_type`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.download_general.transcode` | integer | 官方字段 `transcode`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.download_mask_panel` | object | 官方字段 `download_mask_panel`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.download_mask_panel.code` | integer | 官方业务编码。 |
| `aweme_list[].aweme_acl.download_mask_panel.mute` | boolean | 官方字段 `mute`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.download_mask_panel.show_type` | integer | 官方字段 `show_type`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.download_mask_panel.transcode` | integer | 官方字段 `transcode`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.platform_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].aweme_acl.press_action_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].aweme_acl.share_action_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].aweme_acl.share_general` | object | 官方字段 `share_general`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.share_general.code` | integer | 官方业务编码。 |
| `aweme_list[].aweme_acl.share_general.mute` | boolean | 官方字段 `mute`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.share_general.show_type` | integer | 官方字段 `show_type`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.share_general.transcode` | integer | 官方字段 `transcode`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_acl.share_list_status` | integer | 官方字段 `share_list_status`；官方未单独提供业务说明。 |
| `aweme_list[].aweme_id` | string | TikTok 视频标识。 |
| `aweme_list[].aweme_type` | integer | 官方字段 `aweme_type`；官方未单独提供业务说明。 |
| `aweme_list[].banners` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].behind_the_song_music_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].behind_the_song_video_music_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].bodydance_score` | integer | 官方字段 `bodydance_score`；官方未单独提供业务说明。 |
| `aweme_list[].branded_content_accounts` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cc_template_info` | object | 官方字段 `cc_template_info`；官方未单独提供业务说明。 |
| `aweme_list[].cc_template_info.author_name` | string | 官方字段 `author_name`；官方未单独提供业务说明。 |
| `aweme_list[].cc_template_info.clip_count` | integer | 官方字段 `clip_count`；官方未单独提供业务说明。 |
| `aweme_list[].cc_template_info.desc` | string | 描述。 |
| `aweme_list[].cc_template_info.duration_milliseconds` | integer | 官方字段 `duration_milliseconds`；官方未单独提供业务说明。 |
| `aweme_list[].cc_template_info.related_music_id` | string | 官方字段 `related_music_id`；官方未单独提供业务说明。 |
| `aweme_list[].cc_template_info.template_id` | string | 官方字段 `template_id`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list` | array | 官方字段 `cha_list`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].author` | object | 作者信息。 |
| `aweme_list[].cha_list[].author.account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.can_message_follow_status_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.events` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.item_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.need_points` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.type_label` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].author.white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].banner_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].cha_attrs` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].cha_name` | string | 官方字段 `cha_name`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].cid` | string | 官方字段 `cid`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].connect_music` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].cha_list[].desc` | string | 描述。 |
| `aweme_list[].cha_list[].extra_attr` | object | 官方字段 `extra_attr`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].extra_attr.is_live` | boolean | 是否正在直播。 |
| `aweme_list[].cha_list[].hashtag_profile` | string | 官方字段 `hashtag_profile`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].is_challenge` | integer | 官方字段 `is_challenge`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].is_commerce` | boolean | 官方字段 `is_commerce`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].is_pgcshow` | boolean | 官方字段 `is_pgcshow`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].schema` | string | 官方字段 `schema`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.bool_persist` | integer | 官方字段 `bool_persist`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.now_invitation_card_image_urls` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].share_info.share_desc` | string | 官方字段 `share_desc`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.share_desc_info` | string | 官方字段 `share_desc_info`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.share_quote` | string | 官方字段 `share_quote`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.share_signature_desc` | string | 官方字段 `share_signature_desc`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.share_signature_url` | string | 官方字段 `share_signature_url`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.share_title` | string | 官方字段 `share_title`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.share_title_myself` | string | 官方字段 `share_title_myself`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.share_title_other` | string | 官方字段 `share_title_other`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].share_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].show_items` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cha_list[].sub_type` | integer | 官方字段 `sub_type`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].type` | integer | 类型。 |
| `aweme_list[].cha_list[].use_count` | integer | 官方字段 `use_count`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].user_count` | integer | 官方字段 `user_count`；官方未单独提供业务说明。 |
| `aweme_list[].cha_list[].view_count` | integer | 官方字段 `view_count`；官方未单独提供业务说明。 |
| `aweme_list[].challenge_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].cmt_swt` | boolean | 官方字段 `cmt_swt`；官方未单独提供业务说明。 |
| `aweme_list[].collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `aweme_list[].comment_config` | object | 官方字段 `comment_config`；官方未单独提供业务说明。 |
| `aweme_list[].comment_config.emoji_recommend_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].comment_config.long_press_recommend_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].comment_config.preload` | object | 官方字段 `preload`；官方未单独提供业务说明。 |
| `aweme_list[].comment_config.preload.preds` | string | 官方字段 `preds`；官方未单独提供业务说明。 |
| `aweme_list[].comment_config.preload.type` | integer | 类型。 |
| `aweme_list[].comment_config.quick_comment` | object | 官方字段 `quick_comment`；官方未单独提供业务说明。 |
| `aweme_list[].comment_config.quick_comment.enabled` | boolean | 官方字段 `enabled`；官方未单独提供业务说明。 |
| `aweme_list[].comment_config.quick_comment_emoji_recommend_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].comment_topbar_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].commerce_config_data` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].commerce_info` | object | 官方字段 `commerce_info`；官方未单独提供业务说明。 |
| `aweme_list[].commerce_info.adv_promotable` | boolean | 官方字段 `adv_promotable`；官方未单独提供业务说明。 |
| `aweme_list[].commerce_info.auction_ad_invited` | boolean | 官方字段 `auction_ad_invited`；官方未单独提供业务说明。 |
| `aweme_list[].commerce_info.branded_content_type` | integer | 官方字段 `branded_content_type`；官方未单独提供业务说明。 |
| `aweme_list[].commerce_info.with_comment_filter_words` | boolean | 官方字段 `with_comment_filter_words`；官方未单独提供业务说明。 |
| `aweme_list[].content_desc` | string | 官方字段 `content_desc`；官方未单独提供业务说明。 |
| `aweme_list[].content_desc_extra` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].content_model` | object | 官方字段 `content_model`；官方未单独提供业务说明。 |
| `aweme_list[].content_model.custom_biz` | object | 官方字段 `custom_biz`；官方未单独提供业务说明。 |
| `aweme_list[].content_model.custom_biz.aweme_trace` | string | 官方字段 `aweme_trace`；官方未单独提供业务说明。 |
| `aweme_list[].content_model.standard_biz` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_list[].cover_labels` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].create_time` | integer | 创建时间。 |
| `aweme_list[].creation_info` | object | 官方字段 `creation_info`；官方未单独提供业务说明。 |
| `aweme_list[].creation_info.creation_used_functions` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].desc` | string | 描述。 |
| `aweme_list[].desc_language` | string | 官方字段 `desc_language`；官方未单独提供业务说明。 |
| `aweme_list[].disable_search_trending_bar` | boolean | 官方字段 `disable_search_trending_bar`；官方未单独提供业务说明。 |
| `aweme_list[].distance` | string | 官方字段 `distance`；官方未单独提供业务说明。 |
| `aweme_list[].distribute_type` | integer | 官方字段 `distribute_type`；官方未单独提供业务说明。 |
| `aweme_list[].follow_up_publish_from_id` | integer | 官方字段 `follow_up_publish_from_id`；官方未单独提供业务说明。 |
| `aweme_list[].geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].geofencing_regions` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].green_screen_materials` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].group_id` | string | 官方字段 `group_id`；官方未单独提供业务说明。 |
| `aweme_list[].group_id_list` | object | 官方字段 `group_id_list`；官方未单独提供业务说明。 |
| `aweme_list[].group_id_list.GroupdIdList0` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].group_id_list.GroupdIdList1` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].has_danmaku` | boolean | 官方字段 `has_danmaku`；官方未单独提供业务说明。 |
| `aweme_list[].has_promote_entry` | integer | 官方字段 `has_promote_entry`；官方未单独提供业务说明。 |
| `aweme_list[].has_vs_entry` | boolean | 官方字段 `has_vs_entry`；官方未单独提供业务说明。 |
| `aweme_list[].have_dashboard` | boolean | 官方字段 `have_dashboard`；官方未单独提供业务说明。 |
| `aweme_list[].hybrid_label` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].image_infos` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].interact_permission` | object | 官方字段 `interact_permission`；官方未单独提供业务说明。 |
| `aweme_list[].interact_permission.allow_adding_as_post` | object | 官方字段 `allow_adding_as_post`；官方未单独提供业务说明。 |
| `aweme_list[].interact_permission.allow_adding_as_post.status` | integer | 状态。 |
| `aweme_list[].interact_permission.allow_adding_to_story` | integer | 官方字段 `allow_adding_to_story`；官方未单独提供业务说明。 |
| `aweme_list[].interact_permission.allow_create_sticker` | object | 官方字段 `allow_create_sticker`；官方未单独提供业务说明。 |
| `aweme_list[].interact_permission.allow_create_sticker.status` | integer | 状态。 |
| `aweme_list[].interact_permission.allow_story_switch_to_post` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_list[].interact_permission.duet` | integer | 官方字段 `duet`；官方未单独提供业务说明。 |
| `aweme_list[].interact_permission.duet_privacy_setting` | integer | 官方字段 `duet_privacy_setting`；官方未单独提供业务说明。 |
| `aweme_list[].interact_permission.stitch` | integer | 官方字段 `stitch`；官方未单独提供业务说明。 |
| `aweme_list[].interact_permission.stitch_privacy_setting` | integer | 官方字段 `stitch_privacy_setting`；官方未单独提供业务说明。 |
| `aweme_list[].interact_permission.upvote` | integer | 官方字段 `upvote`；官方未单独提供业务说明。 |
| `aweme_list[].interaction_stickers` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].is_ads` | boolean | 官方字段 `is_ads`；官方未单独提供业务说明。 |
| `aweme_list[].is_description_translatable` | boolean | 官方字段 `is_description_translatable`；官方未单独提供业务说明。 |
| `aweme_list[].is_hash_tag` | integer | 官方字段 `is_hash_tag`；官方未单独提供业务说明。 |
| `aweme_list[].is_nff_or_nr` | boolean | 官方字段 `is_nff_or_nr`；官方未单独提供业务说明。 |
| `aweme_list[].is_on_this_day` | integer | 官方字段 `is_on_this_day`；官方未单独提供业务说明。 |
| `aweme_list[].is_pgcshow` | boolean | 官方字段 `is_pgcshow`；官方未单独提供业务说明。 |
| `aweme_list[].is_preview` | integer | 官方字段 `is_preview`；官方未单独提供业务说明。 |
| `aweme_list[].is_relieve` | boolean | 官方字段 `is_relieve`；官方未单独提供业务说明。 |
| `aweme_list[].is_text_sticker_translatable` | boolean | 官方字段 `is_text_sticker_translatable`；官方未单独提供业务说明。 |
| `aweme_list[].is_title_translatable` | boolean | 官方字段 `is_title_translatable`；官方未单独提供业务说明。 |
| `aweme_list[].is_top` | integer | 官方字段 `is_top`；官方未单独提供业务说明。 |
| `aweme_list[].is_vr` | boolean | 官方字段 `is_vr`；官方未单独提供业务说明。 |
| `aweme_list[].item_comment_settings` | integer | 官方字段 `item_comment_settings`；官方未单独提供业务说明。 |
| `aweme_list[].item_duet` | integer | 官方字段 `item_duet`；官方未单独提供业务说明。 |
| `aweme_list[].item_react` | integer | 官方字段 `item_react`；官方未单独提供业务说明。 |
| `aweme_list[].item_stitch` | integer | 官方字段 `item_stitch`；官方未单独提供业务说明。 |
| `aweme_list[].label_top` | object | 官方字段 `label_top`；官方未单独提供业务说明。 |
| `aweme_list[].label_top.height` | integer | 高度。 |
| `aweme_list[].label_top.uri` | string | 资源标识。 |
| `aweme_list[].label_top.url_list` | array | 资源链接列表。 |
| `aweme_list[].label_top.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].label_top.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].label_top.width` | integer | 宽度。 |
| `aweme_list[].label_top_text` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].long_video` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].main_arch_common` | string | 官方字段 `main_arch_common`；官方未单独提供业务说明。 |
| `aweme_list[].mask_infos` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].misc_info` | string | 官方字段 `misc_info`；官方未单独提供业务说明。 |
| `aweme_list[].muf_comment_info_v2` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music` | object | 官方字段 `music`；官方未单独提供业务说明。 |
| `aweme_list[].music.album` | string | 官方字段 `album`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists` | array | 官方字段 `artists`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists[].avatar` | object | 头像信息。 |
| `aweme_list[].music.artists[].avatar.uri` | string | 资源标识。 |
| `aweme_list[].music.artists[].avatar.url_list` | array | 资源链接列表。 |
| `aweme_list[].music.artists[].avatar.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].music.artists[].avatar.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.artists[].enter_type` | integer | 官方字段 `enter_type`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists[].follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists[].follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists[].handle` | string | 账号名称。 |
| `aweme_list[].music.artists[].is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists[].is_blocked` | boolean | 官方字段 `is_blocked`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists[].is_private_account` | boolean | 官方字段 `is_private_account`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists[].is_verified` | boolean | 是否认证。 |
| `aweme_list[].music.artists[].is_visible` | boolean | 官方字段 `is_visible`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists[].nick_name` | string | 官方字段 `nick_name`；官方未单独提供业务说明。 |
| `aweme_list[].music.artists[].sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_list[].music.artists[].status` | integer | 状态。 |
| `aweme_list[].music.artists[].uid` | string | 用户标识。 |
| `aweme_list[].music.audition_duration` | integer | 官方字段 `audition_duration`；官方未单独提供业务说明。 |
| `aweme_list[].music.author` | string | 作者信息。 |
| `aweme_list[].music.author_deleted` | boolean | 官方字段 `author_deleted`；官方未单独提供业务说明。 |
| `aweme_list[].music.author_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.avatar_medium` | object | 中等尺寸头像。 |
| `aweme_list[].music.avatar_medium.height` | integer | 高度。 |
| `aweme_list[].music.avatar_medium.uri` | string | 资源标识。 |
| `aweme_list[].music.avatar_medium.url_list` | array | 资源链接列表。 |
| `aweme_list[].music.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].music.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.avatar_medium.width` | integer | 宽度。 |
| `aweme_list[].music.avatar_thumb` | object | 缩略头像。 |
| `aweme_list[].music.avatar_thumb.height` | integer | 高度。 |
| `aweme_list[].music.avatar_thumb.uri` | string | 资源标识。 |
| `aweme_list[].music.avatar_thumb.url_list` | array | 资源链接列表。 |
| `aweme_list[].music.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].music.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.avatar_thumb.width` | integer | 宽度。 |
| `aweme_list[].music.binded_challenge_id` | integer | 官方字段 `binded_challenge_id`；官方未单独提供业务说明。 |
| `aweme_list[].music.can_not_reuse` | boolean | 官方字段 `can_not_reuse`；官方未单独提供业务说明。 |
| `aweme_list[].music.collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `aweme_list[].music.commercial_right_type` | integer | 官方字段 `commercial_right_type`；官方未单独提供业务说明。 |
| `aweme_list[].music.cover_large` | object | 官方字段 `cover_large`；官方未单独提供业务说明。 |
| `aweme_list[].music.cover_large.height` | integer | 高度。 |
| `aweme_list[].music.cover_large.uri` | string | 资源标识。 |
| `aweme_list[].music.cover_large.url_list` | array | 资源链接列表。 |
| `aweme_list[].music.cover_large.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].music.cover_large.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.cover_large.width` | integer | 宽度。 |
| `aweme_list[].music.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `aweme_list[].music.cover_medium.height` | integer | 高度。 |
| `aweme_list[].music.cover_medium.uri` | string | 资源标识。 |
| `aweme_list[].music.cover_medium.url_list` | array | 资源链接列表。 |
| `aweme_list[].music.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].music.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.cover_medium.width` | integer | 宽度。 |
| `aweme_list[].music.cover_thumb` | object | 官方字段 `cover_thumb`；官方未单独提供业务说明。 |
| `aweme_list[].music.cover_thumb.height` | integer | 高度。 |
| `aweme_list[].music.cover_thumb.uri` | string | 资源标识。 |
| `aweme_list[].music.cover_thumb.url_list` | array | 资源链接列表。 |
| `aweme_list[].music.cover_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].music.cover_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.cover_thumb.width` | integer | 宽度。 |
| `aweme_list[].music.dmv_auto_show` | boolean | 官方字段 `dmv_auto_show`；官方未单独提供业务说明。 |
| `aweme_list[].music.duration` | integer | 时长。 |
| `aweme_list[].music.duration_high_precision` | object | 官方字段 `duration_high_precision`；官方未单独提供业务说明。 |
| `aweme_list[].music.duration_high_precision.audition_duration_precision` | integer | 官方字段 `audition_duration_precision`；官方未单独提供业务说明。 |
| `aweme_list[].music.duration_high_precision.duration_precision` | integer | 官方字段 `duration_precision`；官方未单独提供业务说明。 |
| `aweme_list[].music.duration_high_precision.shoot_duration_precision` | integer | 官方字段 `shoot_duration_precision`；官方未单独提供业务说明。 |
| `aweme_list[].music.duration_high_precision.video_duration_precision` | integer | 官方字段 `video_duration_precision`；官方未单独提供业务说明。 |
| `aweme_list[].music.external_song_info` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].music.extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `aweme_list[].music.has_commerce_right` | boolean | 官方字段 `has_commerce_right`；官方未单独提供业务说明。 |
| `aweme_list[].music.id` | integer | 标识符。 |
| `aweme_list[].music.id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `aweme_list[].music.is_audio_url_with_cookie` | boolean | 官方字段 `is_audio_url_with_cookie`；官方未单独提供业务说明。 |
| `aweme_list[].music.is_author_artist` | boolean | 官方字段 `is_author_artist`；官方未单独提供业务说明。 |
| `aweme_list[].music.is_commerce_music` | boolean | 官方字段 `is_commerce_music`；官方未单独提供业务说明。 |
| `aweme_list[].music.is_matched_metadata` | boolean | 官方字段 `is_matched_metadata`；官方未单独提供业务说明。 |
| `aweme_list[].music.is_original` | boolean | 官方字段 `is_original`；官方未单独提供业务说明。 |
| `aweme_list[].music.is_original_sound` | boolean | 官方字段 `is_original_sound`；官方未单独提供业务说明。 |
| `aweme_list[].music.is_pgc` | boolean | 官方字段 `is_pgc`；官方未单独提供业务说明。 |
| `aweme_list[].music.is_play_music` | boolean | 官方字段 `is_play_music`；官方未单独提供业务说明。 |
| `aweme_list[].music.is_shooting_allow` | boolean | 官方字段 `is_shooting_allow`；官方未单独提供业务说明。 |
| `aweme_list[].music.language` | string | 语言。 |
| `aweme_list[].music.log_extra` | string | 官方字段 `log_extra`；官方未单独提供业务说明。 |
| `aweme_list[].music.lyric_short_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.matched_song` | object | 官方字段 `matched_song`；官方未单独提供业务说明。 |
| `aweme_list[].music.matched_song.author` | string | 作者信息。 |
| `aweme_list[].music.matched_song.chorus_info` | object | 官方字段 `chorus_info`；官方未单独提供业务说明。 |
| `aweme_list[].music.matched_song.chorus_info.duration_ms` | integer | 官方字段 `duration_ms`；官方未单独提供业务说明。 |
| `aweme_list[].music.matched_song.chorus_info.start_ms` | integer | 官方字段 `start_ms`；官方未单独提供业务说明。 |
| `aweme_list[].music.matched_song.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `aweme_list[].music.matched_song.cover_medium.height` | integer | 高度。 |
| `aweme_list[].music.matched_song.cover_medium.uri` | string | 资源标识。 |
| `aweme_list[].music.matched_song.cover_medium.url_list` | array | 资源链接列表。 |
| `aweme_list[].music.matched_song.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].music.matched_song.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.matched_song.cover_medium.width` | integer | 宽度。 |
| `aweme_list[].music.matched_song.full_duration` | integer | 官方字段 `full_duration`；官方未单独提供业务说明。 |
| `aweme_list[].music.matched_song.h5_url` | string | 官方字段 `h5_url`；官方未单独提供业务说明。 |
| `aweme_list[].music.matched_song.id` | string | 标识符。 |
| `aweme_list[].music.matched_song.performers` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.matched_song.title` | string | 标题。 |
| `aweme_list[].music.meme_song_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_list[].music.mid` | string | 官方字段 `mid`；官方未单独提供业务说明。 |
| `aweme_list[].music.multi_bit_rate_play_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.music_release_info` | object | 官方字段 `music_release_info`；官方未单独提供业务说明。 |
| `aweme_list[].music.music_release_info.group_release_date` | integer | 官方字段 `group_release_date`；官方未单独提供业务说明。 |
| `aweme_list[].music.music_release_info.is_new_release_song` | boolean | 官方字段 `is_new_release_song`；官方未单独提供业务说明。 |
| `aweme_list[].music.mute_share` | boolean | 官方字段 `mute_share`；官方未单独提供业务说明。 |
| `aweme_list[].music.offline_desc` | string | 官方字段 `offline_desc`；官方未单独提供业务说明。 |
| `aweme_list[].music.owner_handle` | string | 官方字段 `owner_handle`；官方未单独提供业务说明。 |
| `aweme_list[].music.owner_nickname` | string | 官方字段 `owner_nickname`；官方未单独提供业务说明。 |
| `aweme_list[].music.play_url` | object | 官方字段 `play_url`；官方未单独提供业务说明。 |
| `aweme_list[].music.play_url.height` | integer | 高度。 |
| `aweme_list[].music.play_url.uri` | string | 资源标识。 |
| `aweme_list[].music.play_url.url_list` | array | 资源链接列表。 |
| `aweme_list[].music.play_url.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].music.play_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.play_url.width` | integer | 宽度。 |
| `aweme_list[].music.position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `aweme_list[].music.preview_end_time` | integer | 官方字段 `preview_end_time`；官方未单独提供业务说明。 |
| `aweme_list[].music.preview_start_time` | number | 官方字段 `preview_start_time`；官方未单独提供业务说明。 |
| `aweme_list[].music.recommend_status` | integer | 官方字段 `recommend_status`；官方未单独提供业务说明。 |
| `aweme_list[].music.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.shoot_duration` | integer | 官方字段 `shoot_duration`；官方未单独提供业务说明。 |
| `aweme_list[].music.source_platform` | integer | 官方字段 `source_platform`；官方未单独提供业务说明。 |
| `aweme_list[].music.status` | integer | 状态。 |
| `aweme_list[].music.strong_beat_url` | object | 官方字段 `strong_beat_url`；官方未单独提供业务说明。 |
| `aweme_list[].music.strong_beat_url.height` | integer | 高度。 |
| `aweme_list[].music.strong_beat_url.uri` | string | 资源标识。 |
| `aweme_list[].music.strong_beat_url.url_list` | array | 资源链接列表。 |
| `aweme_list[].music.strong_beat_url.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].music.strong_beat_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.strong_beat_url.width` | integer | 宽度。 |
| `aweme_list[].music.style_value` | array | 官方字段 `style_value`；官方未单独提供业务说明。 |
| `aweme_list[].music.style_value[]` | integer | 官方数组 `style_value` 的元素。 |
| `aweme_list[].music.tag_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.theme_value` | array | 官方字段 `theme_value`；官方未单独提供业务说明。 |
| `aweme_list[].music.theme_value[]` | integer | 官方数组 `theme_value` 的元素。 |
| `aweme_list[].music.title` | string | 标题。 |
| `aweme_list[].music.tt_to_dsp_song_infos` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.uncert_artists` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].music.user_count` | integer | 官方字段 `user_count`；官方未单独提供业务说明。 |
| `aweme_list[].music.video_duration` | integer | 视频时长。 |
| `aweme_list[].music_begin_time_in_ms` | integer | 官方字段 `music_begin_time_in_ms`；官方未单独提供业务说明。 |
| `aweme_list[].music_selected_from` | string | 官方字段 `music_selected_from`；官方未单独提供业务说明。 |
| `aweme_list[].music_title_style` | integer | 官方字段 `music_title_style`；官方未单独提供业务说明。 |
| `aweme_list[].music_volume` | string | 官方字段 `music_volume`；官方未单独提供业务说明。 |
| `aweme_list[].need_trim_step` | boolean | 官方字段 `need_trim_step`；官方未单独提供业务说明。 |
| `aweme_list[].need_vs_entry` | boolean | 官方字段 `need_vs_entry`；官方未单独提供业务说明。 |
| `aweme_list[].nickname_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].no_selected_music` | boolean | 官方字段 `no_selected_music`；官方未单独提供业务说明。 |
| `aweme_list[].operator_boost_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].origin_comment_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].origin_volume` | string | 官方字段 `origin_volume`；官方未单独提供业务说明。 |
| `aweme_list[].original_client_text` | object | 官方字段 `original_client_text`；官方未单独提供业务说明。 |
| `aweme_list[].original_client_text.markup_text` | string | 官方字段 `markup_text`；官方未单独提供业务说明。 |
| `aweme_list[].original_client_text.text_extra` | array | 官方字段 `text_extra`；官方未单独提供业务说明。 |
| `aweme_list[].original_client_text.text_extra[].hashtag_id` | string | 官方字段 `hashtag_id`；官方未单独提供业务说明。 |
| `aweme_list[].original_client_text.text_extra[].hashtag_name` | string | 官方字段 `hashtag_name`；官方未单独提供业务说明。 |
| `aweme_list[].original_client_text.text_extra[].is_commerce` | boolean | 官方字段 `is_commerce`；官方未单独提供业务说明。 |
| `aweme_list[].original_client_text.text_extra[].sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_list[].original_client_text.text_extra[].tag_id` | string | 官方字段 `tag_id`；官方未单独提供业务说明。 |
| `aweme_list[].original_client_text.text_extra[].type` | integer | 类型。 |
| `aweme_list[].original_client_text.text_extra[].user_id` | string | 用户标识。 |
| `aweme_list[].picked_users` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].playlist_blocked` | boolean | 官方字段 `playlist_blocked`；官方未单独提供业务说明。 |
| `aweme_list[].poi_re_tag_signal` | integer | 官方字段 `poi_re_tag_signal`；官方未单独提供业务说明。 |
| `aweme_list[].position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `aweme_list[].products_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].promote_capcut_toggle` | integer | 官方字段 `promote_capcut_toggle`；官方未单独提供业务说明。 |
| `aweme_list[].promote_icon_text` | string | 官方字段 `promote_icon_text`；官方未单独提供业务说明。 |
| `aweme_list[].promote_toast` | string | 官方字段 `promote_toast`；官方未单独提供业务说明。 |
| `aweme_list[].promote_toast_key` | string | 官方字段 `promote_toast_key`；官方未单独提供业务说明。 |
| `aweme_list[].question_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].quick_reply_emojis` | array | 官方字段 `quick_reply_emojis`；官方未单独提供业务说明。 |
| `aweme_list[].quick_reply_emojis[]` | string | 官方数组 `quick_reply_emojis` 的元素。 |
| `aweme_list[].rate` | integer | 官方字段 `rate`；官方未单独提供业务说明。 |
| `aweme_list[].reference_tts_voice_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].reference_voice_filter_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].region` | string | 地区。 |
| `aweme_list[].risk_infos` | object | 官方字段 `risk_infos`；官方未单独提供业务说明。 |
| `aweme_list[].risk_infos.content` | string | 官方字段 `content`；官方未单独提供业务说明。 |
| `aweme_list[].risk_infos.risk_sink` | boolean | 官方字段 `risk_sink`；官方未单独提供业务说明。 |
| `aweme_list[].risk_infos.type` | integer | 类型。 |
| `aweme_list[].risk_infos.vote` | boolean | 官方字段 `vote`；官方未单独提供业务说明。 |
| `aweme_list[].risk_infos.warn` | boolean | 官方字段 `warn`；官方未单独提供业务说明。 |
| `aweme_list[].search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.bool_persist` | integer | 官方字段 `bool_persist`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.now_invitation_card_image_urls` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].share_info.share_desc` | string | 官方字段 `share_desc`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.share_desc_info` | string | 官方字段 `share_desc_info`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.share_link_desc` | string | 官方字段 `share_link_desc`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.share_quote` | string | 官方字段 `share_quote`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.share_signature_desc` | string | 官方字段 `share_signature_desc`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.share_signature_url` | string | 官方字段 `share_signature_url`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.share_title` | string | 官方字段 `share_title`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.share_title_myself` | string | 官方字段 `share_title_myself`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.share_title_other` | string | 官方字段 `share_title_other`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `aweme_list[].share_info.whatsapp_desc` | string | 官方字段 `whatsapp_desc`；官方未单独提供业务说明。 |
| `aweme_list[].share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `aweme_list[].sort_label` | string | 官方字段 `sort_label`；官方未单独提供业务说明。 |
| `aweme_list[].statistics` | object | 官方字段 `statistics`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.aweme_id` | string | TikTok 视频标识。 |
| `aweme_list[].statistics.collect_count` | integer | 官方字段 `collect_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.comment_count` | integer | 评论数量。 |
| `aweme_list[].statistics.digg_count` | integer | 点赞数量。 |
| `aweme_list[].statistics.download_count` | integer | 官方字段 `download_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.forward_count` | integer | 官方字段 `forward_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.lose_comment_count` | integer | 官方字段 `lose_comment_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.lose_count` | integer | 官方字段 `lose_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.play_count` | integer | 播放数量。 |
| `aweme_list[].statistics.repost_count` | integer | 转发数量。 |
| `aweme_list[].statistics.share_count` | integer | 分享数量。 |
| `aweme_list[].statistics.whatsapp_share_count` | integer | 官方字段 `whatsapp_share_count`；官方未单独提供业务说明。 |
| `aweme_list[].status` | object | 状态。 |
| `aweme_list[].status.allow_comment` | boolean | 官方字段 `allow_comment`；官方未单独提供业务说明。 |
| `aweme_list[].status.allow_share` | boolean | 官方字段 `allow_share`；官方未单独提供业务说明。 |
| `aweme_list[].status.aweme_id` | string | TikTok 视频标识。 |
| `aweme_list[].status.download_status` | integer | 官方字段 `download_status`；官方未单独提供业务说明。 |
| `aweme_list[].status.in_reviewing` | boolean | 官方字段 `in_reviewing`；官方未单独提供业务说明。 |
| `aweme_list[].status.is_delete` | boolean | 官方字段 `is_delete`；官方未单独提供业务说明。 |
| `aweme_list[].status.is_prohibited` | boolean | 官方字段 `is_prohibited`；官方未单独提供业务说明。 |
| `aweme_list[].status.private_status` | integer | 官方字段 `private_status`；官方未单独提供业务说明。 |
| `aweme_list[].status.review_result` | object | 官方字段 `review_result`；官方未单独提供业务说明。 |
| `aweme_list[].status.review_result.review_status` | integer | 官方字段 `review_status`；官方未单独提供业务说明。 |
| `aweme_list[].status.reviewed` | integer | 官方字段 `reviewed`；官方未单独提供业务说明。 |
| `aweme_list[].status.self_see` | boolean | 官方字段 `self_see`；官方未单独提供业务说明。 |
| `aweme_list[].sticker_detail` | object | 官方字段 `sticker_detail`；官方未单独提供业务说明。 |
| `aweme_list[].sticker_detail.attributions` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].sticker_detail.children` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].sticker_detail.icon_url` | object | 官方字段 `icon_url`；官方未单独提供业务说明。 |
| `aweme_list[].sticker_detail.icon_url.height` | integer | 高度。 |
| `aweme_list[].sticker_detail.icon_url.uri` | string | 资源标识。 |
| `aweme_list[].sticker_detail.icon_url.url_list` | array | 资源链接列表。 |
| `aweme_list[].sticker_detail.icon_url.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].sticker_detail.icon_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].sticker_detail.icon_url.width` | integer | 宽度。 |
| `aweme_list[].sticker_detail.id` | string | 标识符。 |
| `aweme_list[].sticker_detail.linked_anchors` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].sticker_detail.name` | string | 名称。 |
| `aweme_list[].sticker_detail.owner_id` | string | 官方字段 `owner_id`；官方未单独提供业务说明。 |
| `aweme_list[].sticker_detail.sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_list[].sticker_detail.tags` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].stickers` | string | 官方字段 `stickers`；官方未单独提供业务说明。 |
| `aweme_list[].suggest_words` | object | 官方字段 `suggest_words`；官方未单独提供业务说明。 |
| `aweme_list[].suggest_words.suggest_words` | array | 官方字段 `suggest_words`；官方未单独提供业务说明。 |
| `aweme_list[].suggest_words.suggest_words[].hint_text` | string | 官方字段 `hint_text`；官方未单独提供业务说明。 |
| `aweme_list[].suggest_words.suggest_words[].qrec_virtual_enable` | string | 官方字段 `qrec_virtual_enable`；官方未单独提供业务说明。 |
| `aweme_list[].suggest_words.suggest_words[].scene` | string | 官方字段 `scene`；官方未单独提供业务说明。 |
| `aweme_list[].suggest_words.suggest_words[].words` | array | 官方字段 `words`；官方未单独提供业务说明。 |
| `aweme_list[].suggest_words.suggest_words[].words[].penetrate_info` | string | 官方字段 `penetrate_info`；官方未单独提供业务说明。 |
| `aweme_list[].suggest_words.suggest_words[].words[].word` | string | 官方字段 `word`；官方未单独提供业务说明。 |
| `aweme_list[].suggest_words.suggest_words[].words[].word_id` | string | 官方字段 `word_id`；官方未单独提供业务说明。 |
| `aweme_list[].support_danmaku` | boolean | 官方字段 `support_danmaku`；官方未单独提供业务说明。 |
| `aweme_list[].text_extra` | array | 官方字段 `text_extra`；官方未单独提供业务说明。 |
| `aweme_list[].text_extra[].end` | integer | 官方字段 `end`；官方未单独提供业务说明。 |
| `aweme_list[].text_extra[].hashtag_id` | string | 官方字段 `hashtag_id`；官方未单独提供业务说明。 |
| `aweme_list[].text_extra[].hashtag_name` | string | 官方字段 `hashtag_name`；官方未单独提供业务说明。 |
| `aweme_list[].text_extra[].is_commerce` | boolean | 官方字段 `is_commerce`；官方未单独提供业务说明。 |
| `aweme_list[].text_extra[].sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_list[].text_extra[].start` | integer | 官方字段 `start`；官方未单独提供业务说明。 |
| `aweme_list[].text_extra[].type` | integer | 类型。 |
| `aweme_list[].text_extra[].user_id` | string | 用户标识。 |
| `aweme_list[].text_sticker_major_lang` | string | 官方字段 `text_sticker_major_lang`；官方未单独提供业务说明。 |
| `aweme_list[].title_language` | string | 官方字段 `title_language`；官方未单独提供业务说明。 |
| `aweme_list[].ttec_suggest_words` | object | 官方字段 `ttec_suggest_words`；官方未单独提供业务说明。 |
| `aweme_list[].ttec_suggest_words.ttec_suggest_words` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].tts_voice_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].ttt_product_recall_type` | integer | 官方字段 `ttt_product_recall_type`；官方未单独提供业务说明。 |
| `aweme_list[].uniqid_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].used_full_song` | boolean | 官方字段 `used_full_song`；官方未单独提供业务说明。 |
| `aweme_list[].user_digged` | integer | 官方字段 `user_digged`；官方未单独提供业务说明。 |
| `aweme_list[].video` | object | 视频信息。 |
| `aweme_list[].video.CoverTsp` | number | 官方字段 `CoverTsp`；官方未单独提供业务说明。 |
| `aweme_list[].video.ai_dynamic_cover` | object | 官方字段 `ai_dynamic_cover`；官方未单独提供业务说明。 |
| `aweme_list[].video.ai_dynamic_cover.uri` | string | 资源标识。 |
| `aweme_list[].video.ai_dynamic_cover.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.ai_dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.ai_dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.ai_dynamic_cover_bak` | object | 官方字段 `ai_dynamic_cover_bak`；官方未单独提供业务说明。 |
| `aweme_list[].video.ai_dynamic_cover_bak.uri` | string | 资源标识。 |
| `aweme_list[].video.ai_dynamic_cover_bak.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.ai_dynamic_cover_bak.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.ai_dynamic_cover_bak.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.animated_cover` | object | 官方字段 `animated_cover`；官方未单独提供业务说明。 |
| `aweme_list[].video.animated_cover.uri` | string | 资源标识。 |
| `aweme_list[].video.animated_cover.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.animated_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.animated_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.big_thumbs` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].video.bit_rate` | array | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].HDR_bit` | string | 官方字段 `HDR_bit`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].HDR_type` | string | 官方字段 `HDR_type`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].bit_rate` | integer | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].dub_infos` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.bit_rate[].fps` | integer | 官方字段 `fps`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].gear_name` | string | 官方字段 `gear_name`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].play_addr.height` | integer | 高度。 |
| `aweme_list[].video.bit_rate[].play_addr.uri` | string | 资源标识。 |
| `aweme_list[].video.bit_rate[].play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].play_addr.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.bit_rate[].play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.bit_rate[].play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.bit_rate[].play_addr.width` | integer | 宽度。 |
| `aweme_list[].video.bit_rate[].quality_type` | integer | 官方字段 `quality_type`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate[].video_extra` | string | 官方字段 `video_extra`；官方未单独提供业务说明。 |
| `aweme_list[].video.bit_rate_audio` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].video.cdn_url_expired` | integer | 官方字段 `cdn_url_expired`；官方未单独提供业务说明。 |
| `aweme_list[].video.cla_info` | object | 官方字段 `cla_info`；官方未单独提供业务说明。 |
| `aweme_list[].video.cla_info.caption_infos` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.cla_info.captions_type` | integer | 官方字段 `captions_type`；官方未单独提供业务说明。 |
| `aweme_list[].video.cla_info.creator_edited_caption_id` | integer | 官方字段 `creator_edited_caption_id`；官方未单独提供业务说明。 |
| `aweme_list[].video.cla_info.enable_auto_caption` | integer | 官方字段 `enable_auto_caption`；官方未单独提供业务说明。 |
| `aweme_list[].video.cla_info.has_original_audio` | integer | 官方字段 `has_original_audio`；官方未单独提供业务说明。 |
| `aweme_list[].video.cla_info.hide_original_caption` | boolean | 官方字段 `hide_original_caption`；官方未单独提供业务说明。 |
| `aweme_list[].video.cla_info.no_caption_reason` | integer | 官方字段 `no_caption_reason`；官方未单独提供业务说明。 |
| `aweme_list[].video.cla_info.vertical_positions` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.cover` | object | 官方字段 `cover`；官方未单独提供业务说明。 |
| `aweme_list[].video.cover.height` | integer | 高度。 |
| `aweme_list[].video.cover.uri` | string | 资源标识。 |
| `aweme_list[].video.cover.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.cover.width` | integer | 宽度。 |
| `aweme_list[].video.cover_is_custom` | boolean | 官方字段 `cover_is_custom`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_addr` | object | 官方字段 `download_addr`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_addr.height` | integer | 高度。 |
| `aweme_list[].video.download_addr.uri` | string | 资源标识。 |
| `aweme_list[].video.download_addr.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.download_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.download_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.download_addr.width` | integer | 宽度。 |
| `aweme_list[].video.duration` | integer | 时长。 |
| `aweme_list[].video.dynamic_cover` | object | 官方字段 `dynamic_cover`；官方未单独提供业务说明。 |
| `aweme_list[].video.dynamic_cover.height` | integer | 高度。 |
| `aweme_list[].video.dynamic_cover.uri` | string | 资源标识。 |
| `aweme_list[].video.dynamic_cover.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.dynamic_cover.width` | integer | 宽度。 |
| `aweme_list[].video.has_watermark` | boolean | 官方字段 `has_watermark`；官方未单独提供业务说明。 |
| `aweme_list[].video.height` | integer | 高度。 |
| `aweme_list[].video.is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `aweme_list[].video.is_callback` | boolean | 官方字段 `is_callback`；官方未单独提供业务说明。 |
| `aweme_list[].video.meta` | string | 官方字段 `meta`；官方未单独提供业务说明。 |
| `aweme_list[].video.misc_download_addrs` | string | 官方字段 `misc_download_addrs`；官方未单独提供业务说明。 |
| `aweme_list[].video.need_set_token` | boolean | 官方字段 `need_set_token`；官方未单独提供业务说明。 |
| `aweme_list[].video.origin_cover` | object | 官方字段 `origin_cover`；官方未单独提供业务说明。 |
| `aweme_list[].video.origin_cover.height` | integer | 高度。 |
| `aweme_list[].video.origin_cover.uri` | string | 资源标识。 |
| `aweme_list[].video.origin_cover.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.origin_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.origin_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.origin_cover.width` | integer | 宽度。 |
| `aweme_list[].video.play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr.height` | integer | 高度。 |
| `aweme_list[].video.play_addr.uri` | string | 资源标识。 |
| `aweme_list[].video.play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.play_addr.width` | integer | 宽度。 |
| `aweme_list[].video.play_addr_bytevc1` | object | 官方字段 `play_addr_bytevc1`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_bytevc1.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_bytevc1.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_bytevc1.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_bytevc1.height` | integer | 高度。 |
| `aweme_list[].video.play_addr_bytevc1.uri` | string | 资源标识。 |
| `aweme_list[].video.play_addr_bytevc1.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_bytevc1.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.play_addr_bytevc1.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.play_addr_bytevc1.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.play_addr_bytevc1.width` | integer | 宽度。 |
| `aweme_list[].video.play_addr_h264` | object | 官方字段 `play_addr_h264`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_h264.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_h264.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_h264.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_h264.height` | integer | 高度。 |
| `aweme_list[].video.play_addr_h264.uri` | string | 资源标识。 |
| `aweme_list[].video.play_addr_h264.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr_h264.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.play_addr_h264.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.play_addr_h264.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.play_addr_h264.width` | integer | 宽度。 |
| `aweme_list[].video.ratio` | string | 官方字段 `ratio`；官方未单独提供业务说明。 |
| `aweme_list[].video.source_HDR_type` | integer | 官方字段 `source_HDR_type`；官方未单独提供业务说明。 |
| `aweme_list[].video.tags` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.width` | integer | 宽度。 |
| `aweme_list[].video_control` | object | 官方字段 `video_control`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.allow_download` | boolean | 官方字段 `allow_download`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.allow_duet` | boolean | 官方字段 `allow_duet`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.allow_dynamic_wallpaper` | boolean | 官方字段 `allow_dynamic_wallpaper`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.allow_music` | boolean | 官方字段 `allow_music`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.allow_react` | boolean | 官方字段 `allow_react`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.allow_stitch` | boolean | 官方字段 `allow_stitch`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.draft_progress_bar` | integer | 官方字段 `draft_progress_bar`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.prevent_download_type` | integer | 官方字段 `prevent_download_type`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.share_type` | integer | 官方字段 `share_type`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.show_progress_bar` | integer | 官方字段 `show_progress_bar`；官方未单独提供业务说明。 |
| `aweme_list[].video_control.timer_status` | integer | 官方字段 `timer_status`；官方未单独提供业务说明。 |
| `aweme_list[].video_labels` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].video_text` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].voice_filter_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].with_promotional_music` | boolean | 官方字段 `with_promotional_music`；官方未单独提供业务说明。 |
| `aweme_list[].without_watermark` | boolean | 官方字段 `without_watermark`；官方未单独提供业务说明。 |
| `aweme_list[].is_eligible_for_commission` | boolean | 官方字段 `is_eligible_for_commission`；官方未单独提供业务说明。 |
| `aweme_list[].is_paid_partnership` | boolean | 是否为付费合作内容。 |
| `aweme_list[].create_time_utc` | string | 官方字段 `create_time_utc`；官方未单独提供业务说明。 |
| `aweme_list[].url` | string | 链接。 |
| `aweme_list[].shop_product_url` | string | 官方字段 `shop_product_url`；官方未单独提供业务说明。 |
| `cursor` | integer | 分页游标。 |
| `extra` | object | 官方字段 `extra`；官方未单独提供业务说明。 |
| `extra.fatal_item_ids` | array | 官方示例为空数组，未提供元素结构。 |
| `extra.logid` | string | 官方字段 `logid`；官方未单独提供业务说明。 |
| `extra.now` | integer | 官方字段 `now`；官方未单独提供业务说明。 |
| `has_more` | integer | 是否还有更多结果。 |
| `log_pb` | object | 官方字段 `log_pb`；官方未单独提供业务说明。 |
| `log_pb.impr_id` | string | 官方字段 `impr_id`；官方未单独提供业务说明。 |
| `status_code` | integer | 状态码。 |
| `status_msg` | string | 状态说明。 |
| `aweme_list[].video.bit_rate[].fid_profile_labels` | string | 官方字段 `fid_profile_labels`；官方未单独提供业务说明。 |
| `aweme_list[].video.did_profile_labels` | string | 官方字段 `did_profile_labels`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_no_watermark_addr` | object | 官方字段 `download_no_watermark_addr`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_no_watermark_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_no_watermark_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_no_watermark_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_no_watermark_addr.height` | integer | 高度。 |
| `aweme_list[].video.download_no_watermark_addr.uri` | string | 资源标识。 |
| `aweme_list[].video.download_no_watermark_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_no_watermark_addr.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.download_no_watermark_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.download_no_watermark_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.download_no_watermark_addr.width` | integer | 宽度。 |
| `aweme_list[].video.vid_profile_labels` | string | 官方字段 `vid_profile_labels`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_mute_lives` | integer | 官方字段 `is_mute_lives`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_mute_non_story_post` | integer | 官方字段 `is_mute_non_story_post`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_mute_story` | integer | 官方字段 `is_mute_story`；官方未单独提供业务说明。 |

## 使用要点

- hashtag 不要带 #。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-search-hashtag" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "amazonfinds", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/search/hashtag/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

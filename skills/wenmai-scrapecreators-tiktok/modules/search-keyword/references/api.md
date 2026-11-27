# Wenmai SCRAPECREATORS scrapecreators_tiktok_search_keyword API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-search-keyword`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_search_keyword`
- **脚本入口**：`modules/search-keyword/scripts/search_keyword.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `query` | string | 是 | 搜索关键词。 |
| `date_posted` | string | 否 | 发布时间筛选。可选值：yesterday、this-week、this-month、last-3-months、last-6-months、all-time。 |
| `sort_by` | string | 否 | 排序方式：相关性、最多点赞或最新发布。可选值：relevance、most-liked、date-posted。 |
| `region` | string | 否 | 代理所在地区，两位国家码如 US。这不是硬性国家过滤，只是把代理放到该地区，用于抓取部分国家才能看到的内容。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |
| `cursor` | number | 否 | 分页游标，传入上一页响应中的 cursor。 |

## 请求示例

```json
{
  "query": "amazon finds",
  "region": "US",
  "trim": true
}
```

```bash
python3 modules/search-keyword/scripts/search_keyword.py '{"query": "amazon finds", "region": "US", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `cursor` | integer | 分页游标。 |
| `search_item_list` | array | 官方字段 `search_item_list`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info` | object | 官方字段 `aweme_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info` | object | 官方字段 `added_sound_music_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.album` | string | 官方字段 `album`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.allow_offline_music_to_detail_page` | boolean | 官方字段 `allow_offline_music_to_detail_page`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists` | array | 官方字段 `artists`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].avatar` | object | 头像信息。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].avatar.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].avatar.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].avatar.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].avatar.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].enter_type` | integer | 官方字段 `enter_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].handle` | string | 账号名称。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].is_blocked` | boolean | 官方字段 `is_blocked`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].is_private_account` | boolean | 官方字段 `is_private_account`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].is_verified` | boolean | 是否认证。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].is_visible` | boolean | 官方字段 `is_visible`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].nick_name` | string | 官方字段 `nick_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].sec_uid` | string | TikTok 安全用户标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].status` | integer | 状态。 |
| `search_item_list[].aweme_info.added_sound_music_info.artists[].uid` | string | 用户标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.audition_duration` | integer | 官方字段 `audition_duration`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.author` | string | 作者信息。 |
| `search_item_list[].aweme_info.added_sound_music_info.author_deleted` | boolean | 官方字段 `author_deleted`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.author_position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_medium` | object | 中等尺寸头像。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_medium.height` | integer | 高度。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_medium.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_medium.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_medium.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_thumb` | object | 缩略头像。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_thumb.height` | integer | 高度。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_thumb.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_thumb.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.avatar_thumb.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.added_sound_music_info.binded_challenge_id` | integer | 官方字段 `binded_challenge_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.can_be_stitched` | boolean | 官方字段 `can_be_stitched`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.can_not_reuse` | boolean | 官方字段 `can_not_reuse`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.commercial_right_type` | integer | 官方字段 `commercial_right_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_large` | object | 官方字段 `cover_large`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_large.height` | integer | 高度。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_large.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_large.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_large.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_large.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_large.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_medium.height` | integer | 高度。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_medium.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_medium.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_medium.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_thumb` | object | 官方字段 `cover_thumb`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_thumb.height` | integer | 高度。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_thumb.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_thumb.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.cover_thumb.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.added_sound_music_info.create_time` | integer | 创建时间。 |
| `search_item_list[].aweme_info.added_sound_music_info.dmv_auto_show` | boolean | 官方字段 `dmv_auto_show`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.duration` | integer | 时长。 |
| `search_item_list[].aweme_info.added_sound_music_info.duration_high_precision` | object | 官方字段 `duration_high_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.duration_high_precision.audition_duration_precision` | integer | 官方字段 `audition_duration_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.duration_high_precision.duration_precision` | integer | 官方字段 `duration_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.duration_high_precision.shoot_duration_precision` | integer | 官方字段 `shoot_duration_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.duration_high_precision.video_duration_precision` | integer | 官方字段 `video_duration_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.external_song_info` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.added_sound_music_info.extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.has_commerce_right` | boolean | 官方字段 `has_commerce_right`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.id` | integer | 标识符。 |
| `search_item_list[].aweme_info.added_sound_music_info.id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.is_audio_url_with_cookie` | boolean | 官方字段 `is_audio_url_with_cookie`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.is_author_artist` | boolean | 官方字段 `is_author_artist`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.is_commerce_music` | boolean | 官方字段 `is_commerce_music`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.is_matched_metadata` | boolean | 官方字段 `is_matched_metadata`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.is_original` | boolean | 官方字段 `is_original`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.is_original_sound` | boolean | 官方字段 `is_original_sound`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.is_pgc` | boolean | 官方字段 `is_pgc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.is_play_music` | boolean | 官方字段 `is_play_music`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.is_shooting_allow` | boolean | 官方字段 `is_shooting_allow`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.language` | string | 语言。 |
| `search_item_list[].aweme_info.added_sound_music_info.log_extra` | string | 官方字段 `log_extra`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.lyric_short_position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song` | object | 官方字段 `matched_song`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.author` | string | 作者信息。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.chorus_info` | object | 官方字段 `chorus_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.chorus_info.duration_ms` | integer | 官方字段 `duration_ms`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.chorus_info.start_ms` | integer | 官方字段 `start_ms`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.cover_medium.height` | integer | 高度。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.cover_medium.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.cover_medium.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.cover_medium.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.full_duration` | integer | 官方字段 `full_duration`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.h5_url` | string | 官方字段 `h5_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.id` | string | 标识符。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.performers` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.matched_song.title` | string | 标题。 |
| `search_item_list[].aweme_info.added_sound_music_info.meme_song_info` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].aweme_info.added_sound_music_info.mid` | string | 官方字段 `mid`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.multi_bit_rate_play_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.music_release_info` | object | 官方字段 `music_release_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.music_release_info.group_release_date` | integer | 官方字段 `group_release_date`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.music_release_info.is_new_release_song` | boolean | 官方字段 `is_new_release_song`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.mute_share` | boolean | 官方字段 `mute_share`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.offline_desc` | string | 官方字段 `offline_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.owner_handle` | string | 官方字段 `owner_handle`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.owner_nickname` | string | 官方字段 `owner_nickname`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.play_url` | object | 官方字段 `play_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.play_url.height` | integer | 高度。 |
| `search_item_list[].aweme_info.added_sound_music_info.play_url.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.play_url.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.added_sound_music_info.play_url.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.play_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.play_url.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.added_sound_music_info.position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.preview_end_time` | integer | 官方字段 `preview_end_time`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.preview_start_time` | integer | 官方字段 `preview_start_time`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.recommend_status` | integer | 官方字段 `recommend_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.shoot_duration` | integer | 官方字段 `shoot_duration`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.source_platform` | integer | 官方字段 `source_platform`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.status` | integer | 状态。 |
| `search_item_list[].aweme_info.added_sound_music_info.strong_beat_url` | object | 官方字段 `strong_beat_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.strong_beat_url.height` | integer | 高度。 |
| `search_item_list[].aweme_info.added_sound_music_info.strong_beat_url.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.added_sound_music_info.strong_beat_url.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.added_sound_music_info.strong_beat_url.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.strong_beat_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.strong_beat_url.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.added_sound_music_info.style_value` | array | 官方字段 `style_value`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.style_value[]` | integer | 官方数组 `style_value` 的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.tag_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.theme_value` | array | 官方字段 `theme_value`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.theme_value[]` | integer | 官方数组 `theme_value` 的元素。 |
| `search_item_list[].aweme_info.added_sound_music_info.title` | string | 标题。 |
| `search_item_list[].aweme_info.added_sound_music_info.tt_to_dsp_song_infos` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.uncert_artists` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.added_sound_music_info.user_count` | integer | 官方字段 `user_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.added_sound_music_info.video_duration` | integer | 视频时长。 |
| `search_item_list[].aweme_info.aigc_info` | object | 官方字段 `aigc_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aigc_info.aigc_label_type` | integer | 官方字段 `aigc_label_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aigc_info.created_by_ai` | boolean | 官方字段 `created_by_ai`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.anchors` | array | 官方字段 `anchors`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.anchors[].actions` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.anchors[].anchor_strong` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.anchors[].component_key` | string | 官方字段 `component_key`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.anchors[].description` | string | 描述。 |
| `search_item_list[].aweme_info.anchors[].extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.anchors[].general_type` | integer | 官方字段 `general_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.anchors[].icon` | object | 官方字段 `icon`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.anchors[].icon.height` | integer | 高度。 |
| `search_item_list[].aweme_info.anchors[].icon.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.anchors[].icon.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.anchors[].icon.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.anchors[].icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.anchors[].icon.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.anchors[].id` | string | 标识符。 |
| `search_item_list[].aweme_info.anchors[].keyword` | string | 官方字段 `keyword`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.anchors[].log_extra` | string | 官方字段 `log_extra`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.anchors[].schema` | string | 官方字段 `schema`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.anchors[].thumbnail` | object | 缩略图。 |
| `search_item_list[].aweme_info.anchors[].thumbnail.height` | integer | 高度。 |
| `search_item_list[].aweme_info.anchors[].thumbnail.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.anchors[].thumbnail.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.anchors[].thumbnail.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.anchors[].thumbnail.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.anchors[].thumbnail.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.anchors[].type` | integer | 类型。 |
| `search_item_list[].aweme_info.anchors_extras` | string | 官方字段 `anchors_extras`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.animated_image_info` | object | 官方字段 `animated_image_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.animated_image_info.effect` | integer | 官方字段 `effect`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.animated_image_info.type` | integer | 类型。 |
| `search_item_list[].aweme_info.author` | object | 作者信息。 |
| `search_item_list[].aweme_info.author.accept_private_policy` | boolean | 官方字段 `accept_private_policy`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.authority_status` | integer | 官方字段 `authority_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.avatar_168x168` | object | 官方字段 `avatar_168x168`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.avatar_168x168.height` | integer | 高度。 |
| `search_item_list[].aweme_info.author.avatar_168x168.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.author.avatar_168x168.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.author.avatar_168x168.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.author.avatar_168x168.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.avatar_168x168.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.author.avatar_300x300` | object | 官方字段 `avatar_300x300`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.avatar_300x300.height` | integer | 高度。 |
| `search_item_list[].aweme_info.author.avatar_300x300.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.author.avatar_300x300.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.author.avatar_300x300.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.author.avatar_300x300.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.avatar_300x300.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.author.avatar_larger` | object | 官方字段 `avatar_larger`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.avatar_larger.height` | integer | 高度。 |
| `search_item_list[].aweme_info.author.avatar_larger.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.author.avatar_larger.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.author.avatar_larger.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.author.avatar_larger.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.avatar_larger.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.author.avatar_medium` | object | 中等尺寸头像。 |
| `search_item_list[].aweme_info.author.avatar_medium.height` | integer | 高度。 |
| `search_item_list[].aweme_info.author.avatar_medium.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.author.avatar_medium.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.author.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.author.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.avatar_medium.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.author.avatar_thumb` | object | 缩略头像。 |
| `search_item_list[].aweme_info.author.avatar_thumb.height` | integer | 高度。 |
| `search_item_list[].aweme_info.author.avatar_thumb.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.author.avatar_thumb.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.author.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.author.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.avatar_thumb.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.author.avatar_uri` | string | 官方字段 `avatar_uri`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.aweme_count` | integer | 官方字段 `aweme_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.can_message_follow_status_list` | array | 官方字段 `can_message_follow_status_list`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.can_message_follow_status_list[]` | integer | 官方数组 `can_message_follow_status_list` 的元素。 |
| `search_item_list[].aweme_info.author.can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.comment_filter_status` | integer | 官方字段 `comment_filter_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.comment_setting` | integer | 官方字段 `comment_setting`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.commerce_user_level` | integer | 官方字段 `commerce_user_level`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.custom_verify` | string | 官方字段 `custom_verify`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.cv_level` | string | 官方字段 `cv_level`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.download_prompt_ts` | integer | 官方字段 `download_prompt_ts`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.enabled_filter_all_comments` | boolean | 官方字段 `enabled_filter_all_comments`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.enterprise_verify_reason` | string | 官方字段 `enterprise_verify_reason`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.events` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.fake_data_info` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].aweme_info.author.fb_expire_time` | integer | 官方字段 `fb_expire_time`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.follower_count` | integer | 粉丝数量。 |
| `search_item_list[].aweme_info.author.follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.following_count` | integer | 关注数量。 |
| `search_item_list[].aweme_info.author.friends_status` | integer | 官方字段 `friends_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.hide_search` | boolean | 官方字段 `hide_search`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.ins_id` | string | 官方字段 `ins_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.is_ad_fake` | boolean | 官方字段 `is_ad_fake`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.is_discipline_member` | boolean | 官方字段 `is_discipline_member`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.is_mute` | integer | 官方字段 `is_mute`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.is_mute_lives` | integer | 官方字段 `is_mute_lives`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.is_mute_non_story_post` | integer | 官方字段 `is_mute_non_story_post`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.is_mute_story` | integer | 官方字段 `is_mute_story`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.is_star` | boolean | 官方字段 `is_star`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.item_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.live_agreement` | integer | 官方字段 `live_agreement`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.live_commerce` | boolean | 官方字段 `live_commerce`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.live_verify` | integer | 官方字段 `live_verify`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.mention_status` | integer | 官方字段 `mention_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.name_field` | string | 官方字段 `name_field`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.need_points` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.need_recommend` | integer | 官方字段 `need_recommend`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.nickname` | string | 昵称。 |
| `search_item_list[].aweme_info.author.platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.reply_with_video_flag` | integer | 官方字段 `reply_with_video_flag`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.room_id` | integer | 官方字段 `room_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.search_user_desc` | string | 官方字段 `search_user_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.search_user_name` | string | 官方字段 `search_user_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.sec_uid` | string | TikTok 安全用户标识。 |
| `search_item_list[].aweme_info.author.secret` | integer | 官方字段 `secret`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.shield_comment_notice` | integer | 官方字段 `shield_comment_notice`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.shield_digg_notice` | integer | 官方字段 `shield_digg_notice`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.shield_follow_notice` | integer | 官方字段 `shield_follow_notice`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.short_id` | string | 官方字段 `short_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.show_image_bubble` | boolean | 官方字段 `show_image_bubble`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.special_account` | object | 官方字段 `special_account`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.special_account.special_account_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.special_lock` | integer | 官方字段 `special_lock`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.status` | integer | 状态。 |
| `search_item_list[].aweme_info.author.stitch_setting` | integer | 官方字段 `stitch_setting`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.story_status` | integer | 官方字段 `story_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.total_favorited` | integer | 官方字段 `total_favorited`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.type_label` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.uid` | string | 用户标识。 |
| `search_item_list[].aweme_info.author.unique_id` | string | 账号唯一名称。 |
| `search_item_list[].aweme_info.author.user_canceled` | boolean | 官方字段 `user_canceled`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.user_mode` | integer | 官方字段 `user_mode`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.user_now_pack_info` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].aweme_info.author.user_period` | integer | 官方字段 `user_period`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.user_rate` | integer | 官方字段 `user_rate`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.user_spark_info` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].aweme_info.author.user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.verification_type` | integer | 官方字段 `verification_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.verify_info` | string | 官方字段 `verify_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.video_icon` | object | 官方字段 `video_icon`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.video_icon.height` | integer | 高度。 |
| `search_item_list[].aweme_info.author.video_icon.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.author.video_icon.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.author.video_icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.video_icon.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.author.white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.author.with_commerce_entry` | boolean | 官方字段 `with_commerce_entry`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author.with_shop_entry` | boolean | 官方字段 `with_shop_entry`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.author_user_id` | integer | 官方字段 `author_user_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl` | object | 官方字段 `aweme_acl`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.download_general` | object | 官方字段 `download_general`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.download_general.code` | integer | 官方业务编码。 |
| `search_item_list[].aweme_info.aweme_acl.download_general.mute` | boolean | 官方字段 `mute`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.download_general.show_type` | integer | 官方字段 `show_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.download_general.transcode` | integer | 官方字段 `transcode`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.download_mask_panel` | object | 官方字段 `download_mask_panel`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.download_mask_panel.code` | integer | 官方业务编码。 |
| `search_item_list[].aweme_info.aweme_acl.download_mask_panel.mute` | boolean | 官方字段 `mute`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.download_mask_panel.show_type` | integer | 官方字段 `show_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.download_mask_panel.transcode` | integer | 官方字段 `transcode`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.platform_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.aweme_acl.press_action_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.aweme_acl.share_action_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.aweme_acl.share_general` | object | 官方字段 `share_general`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.share_general.code` | integer | 官方业务编码。 |
| `search_item_list[].aweme_info.aweme_acl.share_general.mute` | boolean | 官方字段 `mute`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.share_general.show_type` | integer | 官方字段 `show_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.share_general.transcode` | integer | 官方字段 `transcode`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_acl.share_list_status` | integer | 官方字段 `share_list_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.aweme_id` | string | TikTok 视频标识。 |
| `search_item_list[].aweme_info.aweme_type` | integer | 官方字段 `aweme_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.banners` | array | 官方字段 `banners`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.banners[].key` | object | 官方字段 `key`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.banners[].key.component_key` | string | 官方字段 `component_key`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.behind_the_song_music_ids` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.behind_the_song_video_music_ids` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.bodydance_score` | integer | 官方字段 `bodydance_score`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.branded_content_accounts` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cc_template_info` | object | 官方字段 `cc_template_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cc_template_info.author_name` | string | 官方字段 `author_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cc_template_info.clip_count` | integer | 官方字段 `clip_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cc_template_info.desc` | string | 描述。 |
| `search_item_list[].aweme_info.cc_template_info.duration_milliseconds` | integer | 官方字段 `duration_milliseconds`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cc_template_info.related_music_id` | string | 官方字段 `related_music_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cc_template_info.template_id` | string | 官方字段 `template_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list` | array | 官方字段 `cha_list`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].author` | object | 作者信息。 |
| `search_item_list[].aweme_info.cha_list[].author.account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.can_message_follow_status_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.events` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.item_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.need_points` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.type_label` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].author.white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].banner_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].cha_attrs` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].cha_name` | string | 官方字段 `cha_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].cid` | string | 官方字段 `cid`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].connect_music` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.cha_list[].desc` | string | 描述。 |
| `search_item_list[].aweme_info.cha_list[].extra_attr` | object | 官方字段 `extra_attr`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].extra_attr.is_live` | boolean | 是否正在直播。 |
| `search_item_list[].aweme_info.cha_list[].hashtag_profile` | string | 官方字段 `hashtag_profile`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].is_challenge` | integer | 官方字段 `is_challenge`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].is_commerce` | boolean | 官方字段 `is_commerce`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].is_pgcshow` | boolean | 官方字段 `is_pgcshow`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].schema` | string | 官方字段 `schema`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.bool_persist` | integer | 官方字段 `bool_persist`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.now_invitation_card_image_urls` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].share_info.share_desc` | string | 官方字段 `share_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.share_desc_info` | string | 官方字段 `share_desc_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.share_quote` | string | 官方字段 `share_quote`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.share_signature_desc` | string | 官方字段 `share_signature_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.share_signature_url` | string | 官方字段 `share_signature_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.share_title` | string | 官方字段 `share_title`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.share_title_myself` | string | 官方字段 `share_title_myself`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.share_title_other` | string | 官方字段 `share_title_other`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].share_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].show_items` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cha_list[].sub_type` | integer | 官方字段 `sub_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].type` | integer | 类型。 |
| `search_item_list[].aweme_info.cha_list[].use_count` | integer | 官方字段 `use_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].user_count` | integer | 官方字段 `user_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cha_list[].view_count` | integer | 官方字段 `view_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.challenge_position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.cmt_swt` | boolean | 官方字段 `cmt_swt`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.comment_config` | object | 官方字段 `comment_config`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.comment_config.comment_panel_show_tab_config` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.comment_config.emoji_recommend_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.comment_config.long_press_recommend_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.comment_config.preload` | object | 官方字段 `preload`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.comment_config.preload.preds` | string | 官方字段 `preds`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.comment_config.quick_comment` | object | 官方字段 `quick_comment`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.comment_config.quick_comment.enabled` | boolean | 官方字段 `enabled`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.comment_config.quick_comment_emoji_recommend_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.comment_topbar_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.commerce_config_data` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.commerce_info` | object | 官方字段 `commerce_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.commerce_info.adv_promotable` | boolean | 官方字段 `adv_promotable`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.commerce_info.auction_ad_invited` | boolean | 官方字段 `auction_ad_invited`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.commerce_info.branded_content_type` | integer | 官方字段 `branded_content_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.commerce_info.with_comment_filter_words` | boolean | 官方字段 `with_comment_filter_words`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_desc` | string | 官方字段 `content_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_desc_extra` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.content_model` | object | 官方字段 `content_model`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.custom_biz` | object | 官方字段 `custom_biz`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.custom_biz.aweme_trace` | string | 官方字段 `aweme_trace`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz` | object | 官方字段 `standard_biz`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz.e_commerce` | object | 官方字段 `e_commerce`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz.e_commerce.ttec_content_tag` | object | 官方字段 `ttec_content_tag`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz.e_commerce.ttec_content_tag.recommendation_tag_consumer_str` | string | 官方字段 `recommendation_tag_consumer_str`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz.e_commerce.ttec_content_tag.recommendation_tag_creator_str` | string | 官方字段 `recommendation_tag_creator_str`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz.tts_voice_info` | object | 官方字段 `tts_voice_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz.tts_voice_info.tts_voice_attr` | string | 官方字段 `tts_voice_attr`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz.tts_voice_info.tts_voice_reuse_params` | string | 官方字段 `tts_voice_reuse_params`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz.vc_filter_info` | object | 官方字段 `vc_filter_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_model.standard_biz.vc_filter_info.vc_filter_attr` | string | 官方字段 `vc_filter_attr`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_original_type` | integer | 官方字段 `content_original_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_size_type` | integer | 官方字段 `content_size_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.content_type` | string | 官方字段 `content_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.cover_labels` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.create_time` | integer | 创建时间。 |
| `search_item_list[].aweme_info.creation_info` | object | 官方字段 `creation_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.creation_info.creation_used_functions` | array | 官方字段 `creation_used_functions`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.creation_info.creation_used_functions[]` | string | 官方数组 `creation_used_functions` 的元素。 |
| `search_item_list[].aweme_info.desc` | string | 描述。 |
| `search_item_list[].aweme_info.desc_language` | string | 官方字段 `desc_language`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.disable_search_trending_bar` | boolean | 官方字段 `disable_search_trending_bar`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.distance` | string | 官方字段 `distance`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.distribute_type` | integer | 官方字段 `distribute_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.follow_up_item_id_groups` | string | 官方字段 `follow_up_item_id_groups`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.follow_up_publish_from_id` | integer | 官方字段 `follow_up_publish_from_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.geofencing_regions` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.green_screen_materials` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.group_id` | string | 官方字段 `group_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.group_id_list` | object | 官方字段 `group_id_list`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.group_id_list.GroupdIdList0` | array | 官方字段 `GroupdIdList0`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.group_id_list.GroupdIdList0[]` | integer | 官方数组 `GroupdIdList0` 的元素。 |
| `search_item_list[].aweme_info.group_id_list.GroupdIdList1` | array | 官方字段 `GroupdIdList1`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.group_id_list.GroupdIdList1[]` | integer | 官方数组 `GroupdIdList1` 的元素。 |
| `search_item_list[].aweme_info.has_danmaku` | boolean | 官方字段 `has_danmaku`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.has_promote_entry` | integer | 官方字段 `has_promote_entry`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.has_vs_entry` | boolean | 官方字段 `has_vs_entry`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.have_dashboard` | boolean | 官方字段 `have_dashboard`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.hybrid_label` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.image_infos` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.interact_permission` | object | 官方字段 `interact_permission`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.interact_permission.allow_adding_as_post` | object | 官方字段 `allow_adding_as_post`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.interact_permission.allow_adding_as_post.status` | integer | 状态。 |
| `search_item_list[].aweme_info.interact_permission.allow_adding_to_story` | integer | 官方字段 `allow_adding_to_story`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.interact_permission.allow_create_sticker` | object | 官方字段 `allow_create_sticker`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.interact_permission.allow_create_sticker.status` | integer | 状态。 |
| `search_item_list[].aweme_info.interact_permission.allow_story_switch_to_post` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].aweme_info.interact_permission.duet` | integer | 官方字段 `duet`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.interact_permission.duet_privacy_setting` | integer | 官方字段 `duet_privacy_setting`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.interact_permission.stitch` | integer | 官方字段 `stitch`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.interact_permission.stitch_privacy_setting` | integer | 官方字段 `stitch_privacy_setting`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.interact_permission.upvote` | integer | 官方字段 `upvote`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.interaction_stickers` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.is_ads` | boolean | 官方字段 `is_ads`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_description_translatable` | boolean | 官方字段 `is_description_translatable`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_hash_tag` | integer | 官方字段 `is_hash_tag`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_nff_or_nr` | boolean | 官方字段 `is_nff_or_nr`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_on_this_day` | integer | 官方字段 `is_on_this_day`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_pgcshow` | boolean | 官方字段 `is_pgcshow`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_preview` | integer | 官方字段 `is_preview`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_relieve` | boolean | 官方字段 `is_relieve`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_text_sticker_translatable` | boolean | 官方字段 `is_text_sticker_translatable`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_title_translatable` | boolean | 官方字段 `is_title_translatable`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_top` | integer | 官方字段 `is_top`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_vr` | boolean | 官方字段 `is_vr`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.item_comment_settings` | integer | 官方字段 `item_comment_settings`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.item_duet` | integer | 官方字段 `item_duet`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.item_react` | integer | 官方字段 `item_react`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.item_stitch` | integer | 官方字段 `item_stitch`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.label_top` | object | 官方字段 `label_top`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.label_top.height` | integer | 高度。 |
| `search_item_list[].aweme_info.label_top.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.label_top.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.label_top.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.label_top.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.label_top.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.label_top_text` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.long_video` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.main_arch_common` | string | 官方字段 `main_arch_common`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.mask_infos` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.misc_info` | string | 官方字段 `misc_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.muf_comment_info_v2` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music` | object | 官方字段 `music`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.album` | string | 官方字段 `album`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.allow_offline_music_to_detail_page` | boolean | 官方字段 `allow_offline_music_to_detail_page`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists` | array | 官方字段 `artists`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists[].avatar` | object | 头像信息。 |
| `search_item_list[].aweme_info.music.artists[].avatar.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.music.artists[].avatar.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.music.artists[].avatar.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.music.artists[].avatar.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.artists[].enter_type` | integer | 官方字段 `enter_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists[].follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists[].follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists[].handle` | string | 账号名称。 |
| `search_item_list[].aweme_info.music.artists[].is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists[].is_blocked` | boolean | 官方字段 `is_blocked`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists[].is_private_account` | boolean | 官方字段 `is_private_account`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists[].is_verified` | boolean | 是否认证。 |
| `search_item_list[].aweme_info.music.artists[].is_visible` | boolean | 官方字段 `is_visible`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists[].nick_name` | string | 官方字段 `nick_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.artists[].sec_uid` | string | TikTok 安全用户标识。 |
| `search_item_list[].aweme_info.music.artists[].status` | integer | 状态。 |
| `search_item_list[].aweme_info.music.artists[].uid` | string | 用户标识。 |
| `search_item_list[].aweme_info.music.audition_duration` | integer | 官方字段 `audition_duration`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.author` | string | 作者信息。 |
| `search_item_list[].aweme_info.music.author_deleted` | boolean | 官方字段 `author_deleted`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.author_position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.avatar_medium` | object | 中等尺寸头像。 |
| `search_item_list[].aweme_info.music.avatar_medium.height` | integer | 高度。 |
| `search_item_list[].aweme_info.music.avatar_medium.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.music.avatar_medium.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.music.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.music.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.avatar_medium.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.music.avatar_thumb` | object | 缩略头像。 |
| `search_item_list[].aweme_info.music.avatar_thumb.height` | integer | 高度。 |
| `search_item_list[].aweme_info.music.avatar_thumb.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.music.avatar_thumb.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.music.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.music.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.avatar_thumb.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.music.binded_challenge_id` | integer | 官方字段 `binded_challenge_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.can_be_stitched` | boolean | 官方字段 `can_be_stitched`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.can_not_reuse` | boolean | 官方字段 `can_not_reuse`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.commercial_right_type` | integer | 官方字段 `commercial_right_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.cover_large` | object | 官方字段 `cover_large`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.cover_large.height` | integer | 高度。 |
| `search_item_list[].aweme_info.music.cover_large.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.music.cover_large.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.music.cover_large.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.music.cover_large.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.cover_large.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.music.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.cover_medium.height` | integer | 高度。 |
| `search_item_list[].aweme_info.music.cover_medium.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.music.cover_medium.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.music.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.music.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.cover_medium.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.music.cover_thumb` | object | 官方字段 `cover_thumb`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.cover_thumb.height` | integer | 高度。 |
| `search_item_list[].aweme_info.music.cover_thumb.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.music.cover_thumb.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.music.cover_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.music.cover_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.cover_thumb.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.music.create_time` | integer | 创建时间。 |
| `search_item_list[].aweme_info.music.dmv_auto_show` | boolean | 官方字段 `dmv_auto_show`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.duration` | integer | 时长。 |
| `search_item_list[].aweme_info.music.duration_high_precision` | object | 官方字段 `duration_high_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.duration_high_precision.audition_duration_precision` | integer | 官方字段 `audition_duration_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.duration_high_precision.duration_precision` | integer | 官方字段 `duration_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.duration_high_precision.shoot_duration_precision` | integer | 官方字段 `shoot_duration_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.duration_high_precision.video_duration_precision` | integer | 官方字段 `video_duration_precision`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.external_song_info` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.music.extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.has_commerce_right` | boolean | 官方字段 `has_commerce_right`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.id` | integer | 标识符。 |
| `search_item_list[].aweme_info.music.id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.is_audio_url_with_cookie` | boolean | 官方字段 `is_audio_url_with_cookie`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.is_author_artist` | boolean | 官方字段 `is_author_artist`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.is_commerce_music` | boolean | 官方字段 `is_commerce_music`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.is_matched_metadata` | boolean | 官方字段 `is_matched_metadata`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.is_original` | boolean | 官方字段 `is_original`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.is_original_sound` | boolean | 官方字段 `is_original_sound`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.is_pgc` | boolean | 官方字段 `is_pgc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.is_play_music` | boolean | 官方字段 `is_play_music`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.is_shooting_allow` | boolean | 官方字段 `is_shooting_allow`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.language` | string | 语言。 |
| `search_item_list[].aweme_info.music.log_extra` | string | 官方字段 `log_extra`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.lyric_short_position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.matched_song` | object | 官方字段 `matched_song`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.matched_song.author` | string | 作者信息。 |
| `search_item_list[].aweme_info.music.matched_song.chorus_info` | object | 官方字段 `chorus_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.matched_song.chorus_info.duration_ms` | integer | 官方字段 `duration_ms`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.matched_song.chorus_info.start_ms` | integer | 官方字段 `start_ms`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.matched_song.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.matched_song.cover_medium.height` | integer | 高度。 |
| `search_item_list[].aweme_info.music.matched_song.cover_medium.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.music.matched_song.cover_medium.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.music.matched_song.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.music.matched_song.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.matched_song.cover_medium.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.music.matched_song.full_duration` | integer | 官方字段 `full_duration`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.matched_song.h5_url` | string | 官方字段 `h5_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.matched_song.id` | string | 标识符。 |
| `search_item_list[].aweme_info.music.matched_song.performers` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.matched_song.title` | string | 标题。 |
| `search_item_list[].aweme_info.music.meme_song_info` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].aweme_info.music.mid` | string | 官方字段 `mid`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.multi_bit_rate_play_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.music_release_info` | object | 官方字段 `music_release_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.music_release_info.group_release_date` | integer | 官方字段 `group_release_date`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.music_release_info.is_new_release_song` | boolean | 官方字段 `is_new_release_song`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.mute_share` | boolean | 官方字段 `mute_share`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.offline_desc` | string | 官方字段 `offline_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.owner_handle` | string | 官方字段 `owner_handle`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.owner_nickname` | string | 官方字段 `owner_nickname`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.play_url` | object | 官方字段 `play_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.play_url.height` | integer | 高度。 |
| `search_item_list[].aweme_info.music.play_url.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.music.play_url.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.music.play_url.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.music.play_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.play_url.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.music.position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.preview_end_time` | integer | 官方字段 `preview_end_time`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.preview_start_time` | integer | 官方字段 `preview_start_time`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.recommend_status` | integer | 官方字段 `recommend_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.shoot_duration` | integer | 官方字段 `shoot_duration`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.source_platform` | integer | 官方字段 `source_platform`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.status` | integer | 状态。 |
| `search_item_list[].aweme_info.music.strong_beat_url` | object | 官方字段 `strong_beat_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.strong_beat_url.height` | integer | 高度。 |
| `search_item_list[].aweme_info.music.strong_beat_url.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.music.strong_beat_url.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.music.strong_beat_url.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.music.strong_beat_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.strong_beat_url.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.music.style_value` | array | 官方字段 `style_value`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.style_value[]` | integer | 官方数组 `style_value` 的元素。 |
| `search_item_list[].aweme_info.music.tag_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.theme_value` | array | 官方字段 `theme_value`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.theme_value[]` | integer | 官方数组 `theme_value` 的元素。 |
| `search_item_list[].aweme_info.music.title` | string | 标题。 |
| `search_item_list[].aweme_info.music.tt_to_dsp_song_infos` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.uncert_artists` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.music.user_count` | integer | 官方字段 `user_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music.video_duration` | integer | 视频时长。 |
| `search_item_list[].aweme_info.music_begin_time_in_ms` | integer | 官方字段 `music_begin_time_in_ms`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music_end_time_in_ms` | integer | 官方字段 `music_end_time_in_ms`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music_selected_from` | string | 官方字段 `music_selected_from`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music_title_style` | integer | 官方字段 `music_title_style`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.music_volume` | string | 官方字段 `music_volume`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.need_trim_step` | boolean | 官方字段 `need_trim_step`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.need_vs_entry` | boolean | 官方字段 `need_vs_entry`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.nickname_position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.no_selected_music` | boolean | 官方字段 `no_selected_music`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.operator_boost_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.origin_comment_ids` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.origin_volume` | string | 官方字段 `origin_volume`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.original_client_text` | object | 官方字段 `original_client_text`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.original_client_text.markup_text` | string | 官方字段 `markup_text`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.original_client_text.text_extra` | array | 官方字段 `text_extra`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.original_client_text.text_extra[].hashtag_id` | string | 官方字段 `hashtag_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.original_client_text.text_extra[].hashtag_name` | string | 官方字段 `hashtag_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.original_client_text.text_extra[].is_commerce` | boolean | 官方字段 `is_commerce`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.original_client_text.text_extra[].sec_uid` | string | TikTok 安全用户标识。 |
| `search_item_list[].aweme_info.original_client_text.text_extra[].tag_id` | string | 官方字段 `tag_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.original_client_text.text_extra[].type` | integer | 类型。 |
| `search_item_list[].aweme_info.original_client_text.text_extra[].user_id` | string | 用户标识。 |
| `search_item_list[].aweme_info.picked_users` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.playlist_blocked` | boolean | 官方字段 `playlist_blocked`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data` | object | 官方字段 `poi_data`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.address_info` | object | 官方字段 `address_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.address_info.address` | string | 官方字段 `address`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.address_info.city_code` | string | 官方字段 `city_code`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.address_info.city_name` | string | 官方字段 `city_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.address_info.geohash` | string | 官方字段 `geohash`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.address_info.l0_geoname_id` | string | 官方字段 `l0_geoname_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.address_info.lat` | string | 官方字段 `lat`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.address_info.lng` | string | 官方字段 `lng`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.address_info.region_code` | string | 官方字段 `region_code`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.collect_info` | string | 官方字段 `collect_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor` | object | 官方字段 `comment_anchor`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.has_sub_arrow` | boolean | 官方字段 `has_sub_arrow`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.hide_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.sub_tag_exp_time` | integer | 官方字段 `sub_tag_exp_time`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.sub_tag_exp_type` | integer | 官方字段 `sub_tag_exp_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.sub_tags` | array | 官方字段 `sub_tags`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.sub_tags[].name` | string | 名称。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.sub_tags[].priority` | integer | 官方字段 `priority`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.sub_tags[].type` | integer | 类型。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.suffix` | string | 官方字段 `suffix`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.comment_anchor.track_info` | string | 官方字段 `track_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.icon` | object | 官方字段 `icon`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.icon.height` | integer | 高度。 |
| `search_item_list[].aweme_info.poi_data.icon.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.poi_data.icon.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.poi_data.icon.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.poi_data.icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.poi_data.icon.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.poi_data.info_source` | string | 官方字段 `info_source`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.poi_id` | string | 官方字段 `poi_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.poi_mapkit_collect` | boolean | 官方字段 `poi_mapkit_collect`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.poi_name` | string | 官方字段 `poi_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.poi_review_config` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].aweme_info.poi_data.poi_type` | string | 官方字段 `poi_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.thumbnail` | object | 缩略图。 |
| `search_item_list[].aweme_info.poi_data.thumbnail.height` | integer | 高度。 |
| `search_item_list[].aweme_info.poi_data.thumbnail.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.poi_data.thumbnail.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.poi_data.thumbnail.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.poi_data.thumbnail.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.poi_data.thumbnail.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.poi_data.type_level` | string | 官方字段 `type_level`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.video_anchor` | object | 官方字段 `video_anchor`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.has_sub_arrow` | boolean | 官方字段 `has_sub_arrow`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.hide_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.sub_tag_exp_time` | integer | 官方字段 `sub_tag_exp_time`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.sub_tag_exp_type` | integer | 官方字段 `sub_tag_exp_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.sub_tags` | array | 官方字段 `sub_tags`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.sub_tags[].name` | string | 名称。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.sub_tags[].priority` | integer | 官方字段 `priority`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.sub_tags[].type` | integer | 类型。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.suffix` | string | 官方字段 `suffix`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.video_anchor.track_info` | string | 官方字段 `track_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_data.video_count` | integer | 官方字段 `video_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.poi_re_tag_signal` | integer | 官方字段 `poi_re_tag_signal`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.products_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.promote_capcut_toggle` | integer | 官方字段 `promote_capcut_toggle`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.promote_icon_text` | string | 官方字段 `promote_icon_text`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.promote_toast` | string | 官方字段 `promote_toast`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.promote_toast_key` | string | 官方字段 `promote_toast_key`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.question_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.quick_reply_emojis` | array | 官方字段 `quick_reply_emojis`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.quick_reply_emojis[]` | string | 官方数组 `quick_reply_emojis` 的元素。 |
| `search_item_list[].aweme_info.rate` | integer | 官方字段 `rate`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.reference_tts_voice_ids` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.reference_voice_filter_ids` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.region` | string | 地区。 |
| `search_item_list[].aweme_info.risk_infos` | object | 官方字段 `risk_infos`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.risk_infos.content` | string | 官方字段 `content`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.risk_infos.risk_sink` | boolean | 官方字段 `risk_sink`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.risk_infos.type` | integer | 类型。 |
| `search_item_list[].aweme_info.risk_infos.vote` | boolean | 官方字段 `vote`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.risk_infos.warn` | boolean | 官方字段 `warn`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.search_desc` | string | 官方字段 `search_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.search_highlight` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.bool_persist` | integer | 官方字段 `bool_persist`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.now_invitation_card_image_urls` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.share_info.share_desc` | string | 官方字段 `share_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.share_desc_info` | string | 官方字段 `share_desc_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.share_link_desc` | string | 官方字段 `share_link_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.share_quote` | string | 官方字段 `share_quote`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.share_signature_desc` | string | 官方字段 `share_signature_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.share_signature_url` | string | 官方字段 `share_signature_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.share_title` | string | 官方字段 `share_title`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.share_title_myself` | string | 官方字段 `share_title_myself`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.share_title_other` | string | 官方字段 `share_title_other`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_info.whatsapp_desc` | string | 官方字段 `whatsapp_desc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.shoot_tab_name` | string | 官方字段 `shoot_tab_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.social_interaction_blob` | object | 官方字段 `social_interaction_blob`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.social_interaction_blob.auxiliary_model_content` | string | 官方字段 `auxiliary_model_content`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.solaria_profile` | object | 官方字段 `solaria_profile`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.solaria_profile.profile` | string | 官方字段 `profile`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.sort_label` | string | 官方字段 `sort_label`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.standard_component_info` | object | 官方字段 `standard_component_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.standard_component_info.banner_enabled` | boolean | 官方字段 `banner_enabled`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.statistics` | object | 官方字段 `statistics`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.statistics.aweme_id` | string | TikTok 视频标识。 |
| `search_item_list[].aweme_info.statistics.collect_count` | integer | 官方字段 `collect_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.statistics.comment_count` | integer | 评论数量。 |
| `search_item_list[].aweme_info.statistics.digg_count` | integer | 点赞数量。 |
| `search_item_list[].aweme_info.statistics.download_count` | integer | 官方字段 `download_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.statistics.forward_count` | integer | 官方字段 `forward_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.statistics.lose_comment_count` | integer | 官方字段 `lose_comment_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.statistics.lose_count` | integer | 官方字段 `lose_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.statistics.play_count` | integer | 播放数量。 |
| `search_item_list[].aweme_info.statistics.repost_count` | integer | 转发数量。 |
| `search_item_list[].aweme_info.statistics.share_count` | integer | 分享数量。 |
| `search_item_list[].aweme_info.statistics.whatsapp_share_count` | integer | 官方字段 `whatsapp_share_count`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status` | object | 状态。 |
| `search_item_list[].aweme_info.status.allow_comment` | boolean | 官方字段 `allow_comment`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.allow_share` | boolean | 官方字段 `allow_share`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.aweme_id` | string | TikTok 视频标识。 |
| `search_item_list[].aweme_info.status.download_status` | integer | 官方字段 `download_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.in_reviewing` | boolean | 官方字段 `in_reviewing`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.is_delete` | boolean | 官方字段 `is_delete`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.is_prohibited` | boolean | 官方字段 `is_prohibited`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.private_status` | integer | 官方字段 `private_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.review_result` | object | 官方字段 `review_result`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.review_result.review_status` | integer | 官方字段 `review_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.reviewed` | integer | 官方字段 `reviewed`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.status.self_see` | boolean | 官方字段 `self_see`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words` | object | 官方字段 `suggest_words`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words` | array | 官方字段 `suggest_words`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words[].hint_text` | string | 官方字段 `hint_text`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words[].qrec_virtual_enable` | string | 官方字段 `qrec_virtual_enable`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words[].scene` | string | 官方字段 `scene`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words[].words` | array | 官方字段 `words`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words[].words[].penetrate_info` | string | 官方字段 `penetrate_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words[].words[].word` | string | 官方字段 `word`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words[].words[].word_id` | string | 官方字段 `word_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words[].words[].word_record` | object | 官方字段 `word_record`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.suggest_words.suggest_words[].words[].word_record.words_lang` | string | 官方字段 `words_lang`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.support_danmaku` | boolean | 官方字段 `support_danmaku`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.text_extra` | array | 官方字段 `text_extra`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.text_extra[].end` | integer | 官方字段 `end`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.text_extra[].hashtag_id` | string | 官方字段 `hashtag_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.text_extra[].hashtag_name` | string | 官方字段 `hashtag_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.text_extra[].is_commerce` | boolean | 官方字段 `is_commerce`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.text_extra[].sec_uid` | string | TikTok 安全用户标识。 |
| `search_item_list[].aweme_info.text_extra[].start` | integer | 官方字段 `start`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.text_extra[].type` | integer | 类型。 |
| `search_item_list[].aweme_info.text_extra[].user_id` | string | 用户标识。 |
| `search_item_list[].aweme_info.text_sticker_major_lang` | string | 官方字段 `text_sticker_major_lang`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.title_language` | string | 官方字段 `title_language`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.ttec_suggest_words` | object | 官方字段 `ttec_suggest_words`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.ttec_suggest_words.ttec_suggest_words` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.tts_voice_ids` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.ttt_product_recall_type` | integer | 官方字段 `ttt_product_recall_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.uniqid_position` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.upvote_info` | object | 官方字段 `upvote_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.upvote_info.friends_recall_info` | string | 官方字段 `friends_recall_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.upvote_info.repost_initiate_score` | integer | 官方字段 `repost_initiate_score`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.upvote_info.user_upvoted` | boolean | 官方字段 `user_upvoted`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.upvote_preload` | object | 官方字段 `upvote_preload`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.upvote_preload.need_pull_upvote_info` | boolean | 官方字段 `need_pull_upvote_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.used_full_song` | boolean | 官方字段 `used_full_song`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.user_digged` | integer | 官方字段 `user_digged`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video` | object | 视频信息。 |
| `search_item_list[].aweme_info.video.CoverTsp` | integer | 官方字段 `CoverTsp`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover` | object | 官方字段 `ai_dynamic_cover`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover_bak` | object | 官方字段 `ai_dynamic_cover_bak`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover_bak.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover_bak.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover_bak.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.ai_dynamic_cover_bak.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.animated_cover` | object | 官方字段 `animated_cover`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.animated_cover.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.animated_cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.animated_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.animated_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.big_thumbs` | array | 官方字段 `big_thumbs`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].duration` | number | 时长。 |
| `search_item_list[].aweme_info.video.big_thumbs[].fext` | string | 官方字段 `fext`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_num` | integer | 官方字段 `img_num`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_uris` | array | 官方字段 `img_uris`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_uris[]` | string | 官方数组 `img_uris` 的元素。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_url` | string | 官方字段 `img_url`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_urls` | array | 官方字段 `img_urls`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_urls[]` | string | 官方数组 `img_urls` 的元素。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_x_len` | integer | 官方字段 `img_x_len`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_x_size` | integer | 官方字段 `img_x_size`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_y_len` | integer | 官方字段 `img_y_len`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].img_y_size` | integer | 官方字段 `img_y_size`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].interval` | integer | 官方字段 `interval`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.big_thumbs[].uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.bit_rate` | array | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].HDR_bit` | string | 官方字段 `HDR_bit`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].HDR_type` | string | 官方字段 `HDR_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].bit_rate` | integer | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].dub_infos` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.bit_rate[].fps` | integer | 官方字段 `fps`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].gear_name` | string | 官方字段 `gear_name`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.bit_rate[].play_addr.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video.bit_rate[].quality_type` | integer | 官方字段 `quality_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate[].video_extra` | string | 官方字段 `video_extra`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.bit_rate_audio` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.video.cdn_url_expired` | integer | 官方字段 `cdn_url_expired`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info` | object | 官方字段 `cla_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos` | array | 官方字段 `caption_infos`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].caption_format` | string | 官方字段 `caption_format`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].caption_length` | integer | 官方字段 `caption_length`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].cla_subtitle_id` | integer | 官方字段 `cla_subtitle_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].complaint_id` | integer | 官方字段 `complaint_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].expire` | integer | 官方字段 `expire`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].is_auto_generated` | boolean | 官方字段 `is_auto_generated`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].is_original_caption` | boolean | 官方字段 `is_original_caption`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].lang` | string | 官方字段 `lang`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].language_code` | string | 官方字段 `language_code`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].language_id` | integer | 官方字段 `language_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].source_tag` | string | 官方字段 `source_tag`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].sub_id` | integer | 官方字段 `sub_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].sub_version` | string | 官方字段 `sub_version`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].subtitle_type` | integer | 官方字段 `subtitle_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].translation_type` | integer | 官方字段 `translation_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].translator_id` | integer | 官方字段 `translator_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].url` | string | 链接。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.cla_info.caption_infos[].variant` | string | 官方字段 `variant`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.captions_type` | integer | 官方字段 `captions_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.creator_edited_caption_id` | integer | 官方字段 `creator_edited_caption_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.enable_auto_caption` | integer | 官方字段 `enable_auto_caption`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.has_original_audio` | integer | 官方字段 `has_original_audio`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.hide_original_caption` | boolean | 官方字段 `hide_original_caption`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.no_caption_reason` | integer | 官方字段 `no_caption_reason`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.original_language_info` | object | 官方字段 `original_language_info`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.original_language_info.can_translate_realtime` | boolean | 官方字段 `can_translate_realtime`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.original_language_info.can_translate_realtime_skip_translation_lang_check` | boolean | 官方字段 `can_translate_realtime_skip_translation_lang_check`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.original_language_info.first_subtitle_time` | integer | 官方字段 `first_subtitle_time`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.original_language_info.is_burnin_caption` | boolean | 官方字段 `is_burnin_caption`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.original_language_info.lang` | string | 官方字段 `lang`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.original_language_info.language_code` | string | 官方字段 `language_code`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.original_language_info.language_id` | integer | 官方字段 `language_id`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.original_language_info.original_caption_type` | integer | 官方字段 `original_caption_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cla_info.vertical_positions` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.cover` | object | 官方字段 `cover`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.cover.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.cover.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.cover.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video.download_addr` | object | 官方字段 `download_addr`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.download_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.download_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.download_addr.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.download_addr.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.download_addr.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.download_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.download_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.download_addr.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr` | object | 官方字段 `download_no_watermark_addr`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.download_no_watermark_addr.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video.duration` | integer | 时长。 |
| `search_item_list[].aweme_info.video.dynamic_cover` | object | 官方字段 `dynamic_cover`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.dynamic_cover.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.dynamic_cover.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.dynamic_cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.dynamic_cover.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video.has_watermark` | boolean | 官方字段 `has_watermark`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.is_callback` | boolean | 官方字段 `is_callback`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.is_long_video` | integer | 官方字段 `is_long_video`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.meta` | string | 官方字段 `meta`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.need_set_token` | boolean | 官方字段 `need_set_token`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.origin_cover` | object | 官方字段 `origin_cover`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.origin_cover.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.origin_cover.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.origin_cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.origin_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.origin_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.origin_cover.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video.play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.play_addr.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.play_addr.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1` | object | 官方字段 `play_addr_bytevc1`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.play_addr_bytevc1.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video.play_addr_h264` | object | 官方字段 `play_addr_h264`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_h264.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_h264.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_h264.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_h264.height` | integer | 高度。 |
| `search_item_list[].aweme_info.video.play_addr_h264.uri` | string | 资源标识。 |
| `search_item_list[].aweme_info.video.play_addr_h264.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.play_addr_h264.url_list` | array | 资源链接列表。 |
| `search_item_list[].aweme_info.video.play_addr_h264.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].aweme_info.video.play_addr_h264.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.play_addr_h264.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video.ratio` | string | 官方字段 `ratio`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.source_HDR_type` | integer | 官方字段 `source_HDR_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.tags` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.video.video_model` | string | 官方字段 `video_model`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video.width` | integer | 宽度。 |
| `search_item_list[].aweme_info.video_control` | object | 官方字段 `video_control`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.allow_download` | boolean | 官方字段 `allow_download`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.allow_duet` | boolean | 官方字段 `allow_duet`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.allow_dynamic_wallpaper` | boolean | 官方字段 `allow_dynamic_wallpaper`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.allow_music` | boolean | 官方字段 `allow_music`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.allow_react` | boolean | 官方字段 `allow_react`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.allow_stitch` | boolean | 官方字段 `allow_stitch`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.draft_progress_bar` | integer | 官方字段 `draft_progress_bar`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.prevent_download_type` | integer | 官方字段 `prevent_download_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.share_type` | integer | 官方字段 `share_type`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.show_progress_bar` | integer | 官方字段 `show_progress_bar`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_control.timer_status` | integer | 官方字段 `timer_status`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.video_labels` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.video_text` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].aweme_info.visual_search_info` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].aweme_info.voice_filter_ids` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].aweme_info.with_promotional_music` | boolean | 官方字段 `with_promotional_music`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.without_watermark` | boolean | 官方字段 `without_watermark`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_ad` | boolean | 官方字段 `is_ad`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_eligible_for_commission` | boolean | 官方字段 `is_eligible_for_commission`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.is_paid_partnership` | boolean | 是否为付费合作内容。 |
| `search_item_list[].aweme_info.create_time_utc` | string | 官方字段 `create_time_utc`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_info.url` | string | 链接。 |
| `search_item_list[].aweme_info.shop_product_url` | string | 官方字段 `shop_product_url`；官方未单独提供业务说明。 |
| `search_item_list[].search_aweme_info` | object | 官方字段 `search_aweme_info`；官方未单独提供业务说明。 |
| `search_item_list[].search_aweme_info.has_creation_intention` | boolean | 官方字段 `has_creation_intention`；官方未单独提供业务说明。 |
| `search_item_list[].aweme_id` | string | TikTok 视频标识。 |
| `search_item_list[].desc` | string | 描述。 |
| `search_item_list[].desc_language` | string | 官方字段 `desc_language`；官方未单独提供业务说明。 |
| `search_item_list[].region` | string | 地区。 |
| `search_item_list[].statistics` | object | 官方字段 `statistics`；官方未单独提供业务说明。 |
| `search_item_list[].statistics.aweme_id` | string | TikTok 视频标识。 |
| `search_item_list[].statistics.collect_count` | integer | 官方字段 `collect_count`；官方未单独提供业务说明。 |
| `search_item_list[].statistics.comment_count` | integer | 评论数量。 |
| `search_item_list[].statistics.digg_count` | integer | 点赞数量。 |
| `search_item_list[].statistics.download_count` | integer | 官方字段 `download_count`；官方未单独提供业务说明。 |
| `search_item_list[].statistics.forward_count` | integer | 官方字段 `forward_count`；官方未单独提供业务说明。 |
| `search_item_list[].statistics.lose_comment_count` | integer | 官方字段 `lose_comment_count`；官方未单独提供业务说明。 |
| `search_item_list[].statistics.lose_count` | integer | 官方字段 `lose_count`；官方未单独提供业务说明。 |
| `search_item_list[].statistics.play_count` | integer | 播放数量。 |
| `search_item_list[].statistics.repost_count` | integer | 转发数量。 |
| `search_item_list[].statistics.share_count` | integer | 分享数量。 |
| `search_item_list[].statistics.whatsapp_share_count` | integer | 官方字段 `whatsapp_share_count`；官方未单独提供业务说明。 |
| `search_item_list[].video` | object | 视频信息。 |
| `search_item_list[].video.CoverTsp` | integer | 官方字段 `CoverTsp`；官方未单独提供业务说明。 |
| `search_item_list[].video.ai_dynamic_cover` | object | 官方字段 `ai_dynamic_cover`；官方未单独提供业务说明。 |
| `search_item_list[].video.ai_dynamic_cover.uri` | string | 资源标识。 |
| `search_item_list[].video.ai_dynamic_cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.ai_dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.ai_dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.ai_dynamic_cover_bak` | object | 官方字段 `ai_dynamic_cover_bak`；官方未单独提供业务说明。 |
| `search_item_list[].video.ai_dynamic_cover_bak.uri` | string | 资源标识。 |
| `search_item_list[].video.ai_dynamic_cover_bak.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.ai_dynamic_cover_bak.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.ai_dynamic_cover_bak.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.animated_cover` | object | 官方字段 `animated_cover`；官方未单独提供业务说明。 |
| `search_item_list[].video.animated_cover.uri` | string | 资源标识。 |
| `search_item_list[].video.animated_cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.animated_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.animated_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.big_thumbs` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].video.bit_rate` | array | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].HDR_bit` | string | 官方字段 `HDR_bit`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].HDR_type` | string | 官方字段 `HDR_type`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].bit_rate` | integer | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].dub_infos` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.bit_rate[].fid_profile_labels` | string | 官方字段 `fid_profile_labels`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].fps` | integer | 官方字段 `fps`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].gear_name` | string | 官方字段 `gear_name`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].play_addr.height` | integer | 高度。 |
| `search_item_list[].video.bit_rate[].play_addr.uri` | string | 资源标识。 |
| `search_item_list[].video.bit_rate[].play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate[].play_addr.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.bit_rate[].play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.bit_rate[].play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.bit_rate[].play_addr.width` | integer | 宽度。 |
| `search_item_list[].video.bit_rate[].quality_type` | integer | 官方字段 `quality_type`；官方未单独提供业务说明。 |
| `search_item_list[].video.bit_rate_audio` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].video.cdn_url_expired` | integer | 官方字段 `cdn_url_expired`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info` | object | 官方字段 `cla_info`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos` | array | 官方字段 `caption_infos`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].caption_format` | string | 官方字段 `caption_format`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].caption_length` | integer | 官方字段 `caption_length`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].cla_subtitle_id` | integer | 官方字段 `cla_subtitle_id`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].complaint_id` | integer | 官方字段 `complaint_id`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].expire` | integer | 官方字段 `expire`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].is_auto_generated` | boolean | 官方字段 `is_auto_generated`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].is_original_caption` | boolean | 官方字段 `is_original_caption`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].lang` | string | 官方字段 `lang`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].language_code` | string | 官方字段 `language_code`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].language_id` | integer | 官方字段 `language_id`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].source_tag` | string | 官方字段 `source_tag`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].sub_id` | integer | 官方字段 `sub_id`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].sub_version` | string | 官方字段 `sub_version`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].subtitle_type` | integer | 官方字段 `subtitle_type`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].translation_type` | integer | 官方字段 `translation_type`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].translator_id` | integer | 官方字段 `translator_id`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.caption_infos[].url` | string | 链接。 |
| `search_item_list[].video.cla_info.caption_infos[].url_list` | array | 资源链接列表。 |
| `search_item_list[].video.cla_info.caption_infos[].url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.cla_info.caption_infos[].variant` | string | 官方字段 `variant`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.captions_type` | integer | 官方字段 `captions_type`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.creator_edited_caption_id` | integer | 官方字段 `creator_edited_caption_id`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.enable_auto_caption` | integer | 官方字段 `enable_auto_caption`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.has_original_audio` | integer | 官方字段 `has_original_audio`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.hide_original_caption` | boolean | 官方字段 `hide_original_caption`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.no_caption_reason` | integer | 官方字段 `no_caption_reason`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.original_language_info` | object | 官方字段 `original_language_info`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.original_language_info.can_translate_realtime` | boolean | 官方字段 `can_translate_realtime`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.original_language_info.can_translate_realtime_skip_translation_lang_check` | boolean | 官方字段 `can_translate_realtime_skip_translation_lang_check`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.original_language_info.first_subtitle_time` | integer | 官方字段 `first_subtitle_time`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.original_language_info.is_burnin_caption` | boolean | 官方字段 `is_burnin_caption`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.original_language_info.lang` | string | 官方字段 `lang`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.original_language_info.language_code` | string | 官方字段 `language_code`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.original_language_info.language_id` | integer | 官方字段 `language_id`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.original_language_info.original_caption_type` | integer | 官方字段 `original_caption_type`；官方未单独提供业务说明。 |
| `search_item_list[].video.cla_info.vertical_positions` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.cover` | object | 官方字段 `cover`；官方未单独提供业务说明。 |
| `search_item_list[].video.cover.height` | integer | 高度。 |
| `search_item_list[].video.cover.uri` | string | 资源标识。 |
| `search_item_list[].video.cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.cover.width` | integer | 宽度。 |
| `search_item_list[].video.did_profile_labels` | string | 官方字段 `did_profile_labels`；官方未单独提供业务说明。 |
| `search_item_list[].video.download_addr` | object | 官方字段 `download_addr`；官方未单独提供业务说明。 |
| `search_item_list[].video.download_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].video.download_addr.height` | integer | 高度。 |
| `search_item_list[].video.download_addr.uri` | string | 资源标识。 |
| `search_item_list[].video.download_addr.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.download_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.download_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.download_addr.width` | integer | 宽度。 |
| `search_item_list[].video.download_no_watermark_addr` | object | 官方字段 `download_no_watermark_addr`；官方未单独提供业务说明。 |
| `search_item_list[].video.download_no_watermark_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].video.download_no_watermark_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `search_item_list[].video.download_no_watermark_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `search_item_list[].video.download_no_watermark_addr.height` | integer | 高度。 |
| `search_item_list[].video.download_no_watermark_addr.uri` | string | 资源标识。 |
| `search_item_list[].video.download_no_watermark_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `search_item_list[].video.download_no_watermark_addr.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.download_no_watermark_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.download_no_watermark_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.download_no_watermark_addr.width` | integer | 宽度。 |
| `search_item_list[].video.duration` | integer | 时长。 |
| `search_item_list[].video.dynamic_cover` | object | 官方字段 `dynamic_cover`；官方未单独提供业务说明。 |
| `search_item_list[].video.dynamic_cover.height` | integer | 高度。 |
| `search_item_list[].video.dynamic_cover.uri` | string | 资源标识。 |
| `search_item_list[].video.dynamic_cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.dynamic_cover.width` | integer | 宽度。 |
| `search_item_list[].video.has_watermark` | boolean | 官方字段 `has_watermark`；官方未单独提供业务说明。 |
| `search_item_list[].video.height` | integer | 高度。 |
| `search_item_list[].video.is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `search_item_list[].video.is_callback` | boolean | 官方字段 `is_callback`；官方未单独提供业务说明。 |
| `search_item_list[].video.need_set_token` | boolean | 官方字段 `need_set_token`；官方未单独提供业务说明。 |
| `search_item_list[].video.origin_cover` | object | 官方字段 `origin_cover`；官方未单独提供业务说明。 |
| `search_item_list[].video.origin_cover.height` | integer | 高度。 |
| `search_item_list[].video.origin_cover.uri` | string | 资源标识。 |
| `search_item_list[].video.origin_cover.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.origin_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.origin_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.origin_cover.width` | integer | 宽度。 |
| `search_item_list[].video.play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `search_item_list[].video.play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `search_item_list[].video.play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `search_item_list[].video.play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `search_item_list[].video.play_addr.height` | integer | 高度。 |
| `search_item_list[].video.play_addr.uri` | string | 资源标识。 |
| `search_item_list[].video.play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `search_item_list[].video.play_addr.url_list` | array | 资源链接列表。 |
| `search_item_list[].video.play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].video.play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.play_addr.width` | integer | 宽度。 |
| `search_item_list[].video.ratio` | string | 官方字段 `ratio`；官方未单独提供业务说明。 |
| `search_item_list[].video.source_HDR_type` | integer | 官方字段 `source_HDR_type`；官方未单独提供业务说明。 |
| `search_item_list[].video.tags` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].video.vid_profile_labels` | string | 官方字段 `vid_profile_labels`；官方未单独提供业务说明。 |
| `search_item_list[].video.width` | integer | 宽度。 |
| `search_item_list[].author` | object | 作者信息。 |
| `search_item_list[].author.accept_private_policy` | boolean | 官方字段 `accept_private_policy`；官方未单独提供业务说明。 |
| `search_item_list[].author.account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.authority_status` | integer | 官方字段 `authority_status`；官方未单独提供业务说明。 |
| `search_item_list[].author.avatar_168x168` | object | 官方字段 `avatar_168x168`；官方未单独提供业务说明。 |
| `search_item_list[].author.avatar_168x168.height` | integer | 高度。 |
| `search_item_list[].author.avatar_168x168.uri` | string | 资源标识。 |
| `search_item_list[].author.avatar_168x168.url_list` | array | 资源链接列表。 |
| `search_item_list[].author.avatar_168x168.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].author.avatar_168x168.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.avatar_168x168.width` | integer | 宽度。 |
| `search_item_list[].author.avatar_300x300` | object | 官方字段 `avatar_300x300`；官方未单独提供业务说明。 |
| `search_item_list[].author.avatar_300x300.height` | integer | 高度。 |
| `search_item_list[].author.avatar_300x300.uri` | string | 资源标识。 |
| `search_item_list[].author.avatar_300x300.url_list` | array | 资源链接列表。 |
| `search_item_list[].author.avatar_300x300.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].author.avatar_300x300.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.avatar_300x300.width` | integer | 宽度。 |
| `search_item_list[].author.avatar_larger` | object | 官方字段 `avatar_larger`；官方未单独提供业务说明。 |
| `search_item_list[].author.avatar_larger.height` | integer | 高度。 |
| `search_item_list[].author.avatar_larger.uri` | string | 资源标识。 |
| `search_item_list[].author.avatar_larger.url_list` | array | 资源链接列表。 |
| `search_item_list[].author.avatar_larger.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].author.avatar_larger.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.avatar_larger.width` | integer | 宽度。 |
| `search_item_list[].author.avatar_medium` | object | 中等尺寸头像。 |
| `search_item_list[].author.avatar_medium.height` | integer | 高度。 |
| `search_item_list[].author.avatar_medium.uri` | string | 资源标识。 |
| `search_item_list[].author.avatar_medium.url_list` | array | 资源链接列表。 |
| `search_item_list[].author.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].author.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.avatar_medium.width` | integer | 宽度。 |
| `search_item_list[].author.avatar_thumb` | object | 缩略头像。 |
| `search_item_list[].author.avatar_thumb.height` | integer | 高度。 |
| `search_item_list[].author.avatar_thumb.uri` | string | 资源标识。 |
| `search_item_list[].author.avatar_thumb.url_list` | array | 资源链接列表。 |
| `search_item_list[].author.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `search_item_list[].author.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.avatar_thumb.width` | integer | 宽度。 |
| `search_item_list[].author.avatar_uri` | string | 官方字段 `avatar_uri`；官方未单独提供业务说明。 |
| `search_item_list[].author.aweme_count` | integer | 官方字段 `aweme_count`；官方未单独提供业务说明。 |
| `search_item_list[].author.bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.can_message_follow_status_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.comment_filter_status` | integer | 官方字段 `comment_filter_status`；官方未单独提供业务说明。 |
| `search_item_list[].author.comment_setting` | integer | 官方字段 `comment_setting`；官方未单独提供业务说明。 |
| `search_item_list[].author.commerce_user_level` | integer | 官方字段 `commerce_user_level`；官方未单独提供业务说明。 |
| `search_item_list[].author.cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.custom_verify` | string | 官方字段 `custom_verify`；官方未单独提供业务说明。 |
| `search_item_list[].author.cv_level` | string | 官方字段 `cv_level`；官方未单独提供业务说明。 |
| `search_item_list[].author.download_prompt_ts` | integer | 官方字段 `download_prompt_ts`；官方未单独提供业务说明。 |
| `search_item_list[].author.enabled_filter_all_comments` | boolean | 官方字段 `enabled_filter_all_comments`；官方未单独提供业务说明。 |
| `search_item_list[].author.enterprise_verify_reason` | string | 官方字段 `enterprise_verify_reason`；官方未单独提供业务说明。 |
| `search_item_list[].author.events` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.fake_data_info` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].author.fb_expire_time` | integer | 官方字段 `fb_expire_time`；官方未单独提供业务说明。 |
| `search_item_list[].author.follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `search_item_list[].author.follower_count` | integer | 粉丝数量。 |
| `search_item_list[].author.follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `search_item_list[].author.followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.following_count` | integer | 关注数量。 |
| `search_item_list[].author.friends_status` | integer | 官方字段 `friends_status`；官方未单独提供业务说明。 |
| `search_item_list[].author.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.hide_search` | boolean | 官方字段 `hide_search`；官方未单独提供业务说明。 |
| `search_item_list[].author.homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.ins_id` | string | 官方字段 `ins_id`；官方未单独提供业务说明。 |
| `search_item_list[].author.is_ad_fake` | boolean | 官方字段 `is_ad_fake`；官方未单独提供业务说明。 |
| `search_item_list[].author.is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `search_item_list[].author.is_discipline_member` | boolean | 官方字段 `is_discipline_member`；官方未单独提供业务说明。 |
| `search_item_list[].author.is_mute` | integer | 官方字段 `is_mute`；官方未单独提供业务说明。 |
| `search_item_list[].author.is_mute_lives` | integer | 官方字段 `is_mute_lives`；官方未单独提供业务说明。 |
| `search_item_list[].author.is_mute_non_story_post` | integer | 官方字段 `is_mute_non_story_post`；官方未单独提供业务说明。 |
| `search_item_list[].author.is_mute_story` | integer | 官方字段 `is_mute_story`；官方未单独提供业务说明。 |
| `search_item_list[].author.is_star` | boolean | 官方字段 `is_star`；官方未单独提供业务说明。 |
| `search_item_list[].author.item_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.live_agreement` | integer | 官方字段 `live_agreement`；官方未单独提供业务说明。 |
| `search_item_list[].author.live_commerce` | boolean | 官方字段 `live_commerce`；官方未单独提供业务说明。 |
| `search_item_list[].author.live_verify` | integer | 官方字段 `live_verify`；官方未单独提供业务说明。 |
| `search_item_list[].author.mention_status` | integer | 官方字段 `mention_status`；官方未单独提供业务说明。 |
| `search_item_list[].author.mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.name_field` | string | 官方字段 `name_field`；官方未单独提供业务说明。 |
| `search_item_list[].author.need_points` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.need_recommend` | integer | 官方字段 `need_recommend`；官方未单独提供业务说明。 |
| `search_item_list[].author.nickname` | string | 昵称。 |
| `search_item_list[].author.platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `search_item_list[].author.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.reply_with_video_flag` | integer | 官方字段 `reply_with_video_flag`；官方未单独提供业务说明。 |
| `search_item_list[].author.room_id` | integer | 官方字段 `room_id`；官方未单独提供业务说明。 |
| `search_item_list[].author.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.search_user_desc` | string | 官方字段 `search_user_desc`；官方未单独提供业务说明。 |
| `search_item_list[].author.search_user_name` | string | 官方字段 `search_user_name`；官方未单独提供业务说明。 |
| `search_item_list[].author.sec_uid` | string | TikTok 安全用户标识。 |
| `search_item_list[].author.secret` | integer | 官方字段 `secret`；官方未单独提供业务说明。 |
| `search_item_list[].author.shield_comment_notice` | integer | 官方字段 `shield_comment_notice`；官方未单独提供业务说明。 |
| `search_item_list[].author.shield_digg_notice` | integer | 官方字段 `shield_digg_notice`；官方未单独提供业务说明。 |
| `search_item_list[].author.shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.shield_follow_notice` | integer | 官方字段 `shield_follow_notice`；官方未单独提供业务说明。 |
| `search_item_list[].author.short_id` | string | 官方字段 `short_id`；官方未单独提供业务说明。 |
| `search_item_list[].author.show_image_bubble` | boolean | 官方字段 `show_image_bubble`；官方未单独提供业务说明。 |
| `search_item_list[].author.special_account` | object | 官方字段 `special_account`；官方未单独提供业务说明。 |
| `search_item_list[].author.special_account.special_account_list` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.special_lock` | integer | 官方字段 `special_lock`；官方未单独提供业务说明。 |
| `search_item_list[].author.status` | integer | 状态。 |
| `search_item_list[].author.stitch_setting` | integer | 官方字段 `stitch_setting`；官方未单独提供业务说明。 |
| `search_item_list[].author.total_favorited` | integer | 官方字段 `total_favorited`；官方未单独提供业务说明。 |
| `search_item_list[].author.type_label` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.uid` | string | 用户标识。 |
| `search_item_list[].author.unique_id` | string | 账号唯一名称。 |
| `search_item_list[].author.user_canceled` | boolean | 官方字段 `user_canceled`；官方未单独提供业务说明。 |
| `search_item_list[].author.user_mode` | integer | 官方字段 `user_mode`；官方未单独提供业务说明。 |
| `search_item_list[].author.user_period` | integer | 官方字段 `user_period`；官方未单独提供业务说明。 |
| `search_item_list[].author.user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.user_rate` | integer | 官方字段 `user_rate`；官方未单独提供业务说明。 |
| `search_item_list[].author.user_spark_info` | object | 官方示例为空对象，未提供子字段。 |
| `search_item_list[].author.user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.verification_type` | integer | 官方字段 `verification_type`；官方未单独提供业务说明。 |
| `search_item_list[].author.verify_info` | string | 官方字段 `verify_info`；官方未单独提供业务说明。 |
| `search_item_list[].author.video_icon` | object | 官方字段 `video_icon`；官方未单独提供业务说明。 |
| `search_item_list[].author.video_icon.height` | integer | 高度。 |
| `search_item_list[].author.video_icon.uri` | string | 资源标识。 |
| `search_item_list[].author.video_icon.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `search_item_list[].author.video_icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.video_icon.width` | integer | 宽度。 |
| `search_item_list[].author.white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `search_item_list[].author.with_commerce_entry` | boolean | 官方字段 `with_commerce_entry`；官方未单独提供业务说明。 |
| `search_item_list[].author.with_shop_entry` | boolean | 官方字段 `with_shop_entry`；官方未单独提供业务说明。 |
| `search_item_list[].create_time` | integer | 创建时间。 |
| `search_item_list[].is_ad` | boolean | 官方字段 `is_ad`；官方未单独提供业务说明。 |
| `search_item_list[].is_eligible_for_commission` | boolean | 官方字段 `is_eligible_for_commission`；官方未单独提供业务说明。 |
| `search_item_list[].create_time_utc` | string | 官方字段 `create_time_utc`；官方未单独提供业务说明。 |
| `search_item_list[].url` | string | 链接。 |

## 使用要点

- 按关键词搜 TikTok 视频。trim=true 体积更小。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-search-keyword" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "amazon finds", "region": "US", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/search/keyword/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

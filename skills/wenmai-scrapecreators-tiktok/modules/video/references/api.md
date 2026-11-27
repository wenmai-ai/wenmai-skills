# Wenmai SCRAPECREATORS scrapecreators_tiktok_video API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-video`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_video`
- **脚本入口**：`modules/video/scripts/video.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | TikTok 视频或图文轮播链接。 |
| `region` | string | 否 | 两位国家码，默认 US。作品不可用时可尝试创作者所在国家。 |
| `get_transcript` | boolean | 否 | 是否在本次详情中附带原生字幕。不走 AI 转写，没有字幕时不会补。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |
| `download_media` | boolean | 否 | 是否下载视频/图片并返回长期可访问地址。找到媒体时官方可能收 10 credit，不要默认开启。 |
| `cache_max_age` | string | 否 | 若缓存中有不晚于该时效的数据则直接返回。可选值：1d、3d、7d、14d、30d。 |

## 请求示例

```json
{
  "url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335",
  "trim": true
}
```

```bash
python3 modules/video/scripts/video.py '{"url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `aweme_detail` | object | TikTok 视频详情。 |
| `aweme_detail.added_sound_music_info` | object | 官方字段 `added_sound_music_info`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.album` | string | 官方字段 `album`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.allow_offline_music_to_detail_page` | boolean | 官方字段 `allow_offline_music_to_detail_page`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.artists` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.added_sound_music_info.audition_duration` | integer | 官方字段 `audition_duration`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.author` | string | 作者信息。 |
| `aweme_detail.added_sound_music_info.author_deleted` | boolean | 官方字段 `author_deleted`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.author_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.avatar_medium` | object | 中等尺寸头像。 |
| `aweme_detail.added_sound_music_info.avatar_medium.height` | integer | 高度。 |
| `aweme_detail.added_sound_music_info.avatar_medium.uri` | string | 资源标识。 |
| `aweme_detail.added_sound_music_info.avatar_medium.url_list` | array | 资源链接列表。 |
| `aweme_detail.added_sound_music_info.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.added_sound_music_info.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.avatar_medium.width` | integer | 宽度。 |
| `aweme_detail.added_sound_music_info.avatar_thumb` | object | 缩略头像。 |
| `aweme_detail.added_sound_music_info.avatar_thumb.height` | integer | 高度。 |
| `aweme_detail.added_sound_music_info.avatar_thumb.uri` | string | 资源标识。 |
| `aweme_detail.added_sound_music_info.avatar_thumb.url_list` | array | 资源链接列表。 |
| `aweme_detail.added_sound_music_info.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.added_sound_music_info.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.avatar_thumb.width` | integer | 宽度。 |
| `aweme_detail.added_sound_music_info.binded_challenge_id` | integer | 官方字段 `binded_challenge_id`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.can_be_stitched` | boolean | 官方字段 `can_be_stitched`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.can_not_reuse` | boolean | 官方字段 `can_not_reuse`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.commercial_right_type` | integer | 官方字段 `commercial_right_type`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.cover_large` | object | 官方字段 `cover_large`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.cover_large.height` | integer | 高度。 |
| `aweme_detail.added_sound_music_info.cover_large.uri` | string | 资源标识。 |
| `aweme_detail.added_sound_music_info.cover_large.url_list` | array | 资源链接列表。 |
| `aweme_detail.added_sound_music_info.cover_large.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.added_sound_music_info.cover_large.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.cover_large.width` | integer | 宽度。 |
| `aweme_detail.added_sound_music_info.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.cover_medium.height` | integer | 高度。 |
| `aweme_detail.added_sound_music_info.cover_medium.uri` | string | 资源标识。 |
| `aweme_detail.added_sound_music_info.cover_medium.url_list` | array | 资源链接列表。 |
| `aweme_detail.added_sound_music_info.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.added_sound_music_info.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.cover_medium.width` | integer | 宽度。 |
| `aweme_detail.added_sound_music_info.cover_thumb` | object | 官方字段 `cover_thumb`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.cover_thumb.height` | integer | 高度。 |
| `aweme_detail.added_sound_music_info.cover_thumb.uri` | string | 资源标识。 |
| `aweme_detail.added_sound_music_info.cover_thumb.url_list` | array | 资源链接列表。 |
| `aweme_detail.added_sound_music_info.cover_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.added_sound_music_info.cover_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.cover_thumb.width` | integer | 宽度。 |
| `aweme_detail.added_sound_music_info.create_time` | integer | 创建时间。 |
| `aweme_detail.added_sound_music_info.dmv_auto_show` | boolean | 官方字段 `dmv_auto_show`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.duration` | integer | 时长。 |
| `aweme_detail.added_sound_music_info.duration_high_precision` | object | 官方字段 `duration_high_precision`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.duration_high_precision.audition_duration_precision` | number | 官方字段 `audition_duration_precision`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.duration_high_precision.duration_precision` | number | 官方字段 `duration_precision`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.duration_high_precision.shoot_duration_precision` | number | 官方字段 `shoot_duration_precision`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.duration_high_precision.video_duration_precision` | number | 官方字段 `video_duration_precision`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.external_song_info` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.added_sound_music_info.extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.has_commerce_right` | boolean | 官方字段 `has_commerce_right`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.id` | integer | 标识符。 |
| `aweme_detail.added_sound_music_info.id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.is_audio_url_with_cookie` | boolean | 官方字段 `is_audio_url_with_cookie`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.is_author_artist` | boolean | 官方字段 `is_author_artist`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.is_commerce_music` | boolean | 官方字段 `is_commerce_music`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.is_matched_metadata` | boolean | 官方字段 `is_matched_metadata`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.is_original` | boolean | 官方字段 `is_original`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.is_original_sound` | boolean | 官方字段 `is_original_sound`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.is_pgc` | boolean | 官方字段 `is_pgc`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.is_play_music` | boolean | 官方字段 `is_play_music`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.is_shooting_allow` | boolean | 官方字段 `is_shooting_allow`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.log_extra` | string | 官方字段 `log_extra`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.lyric_short_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.meme_song_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_detail.added_sound_music_info.mid` | string | 官方字段 `mid`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.multi_bit_rate_play_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.mute_share` | boolean | 官方字段 `mute_share`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.offline_desc` | string | 官方字段 `offline_desc`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.owner_handle` | string | 官方字段 `owner_handle`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.owner_id` | string | 官方字段 `owner_id`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.owner_nickname` | string | 官方字段 `owner_nickname`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.play_url` | object | 官方字段 `play_url`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.play_url.height` | integer | 高度。 |
| `aweme_detail.added_sound_music_info.play_url.uri` | string | 资源标识。 |
| `aweme_detail.added_sound_music_info.play_url.url_list` | array | 资源链接列表。 |
| `aweme_detail.added_sound_music_info.play_url.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.added_sound_music_info.play_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.play_url.width` | integer | 宽度。 |
| `aweme_detail.added_sound_music_info.position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.preview_end_time` | integer | 官方字段 `preview_end_time`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.preview_start_time` | integer | 官方字段 `preview_start_time`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.recommend_status` | integer | 官方字段 `recommend_status`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_detail.added_sound_music_info.shoot_duration` | integer | 官方字段 `shoot_duration`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.source_platform` | integer | 官方字段 `source_platform`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.status` | integer | 状态。 |
| `aweme_detail.added_sound_music_info.tag_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.title` | string | 标题。 |
| `aweme_detail.added_sound_music_info.tt_to_dsp_song_infos` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.added_sound_music_info.uncert_artists` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.added_sound_music_info.user_count` | integer | 官方字段 `user_count`；官方未单独提供业务说明。 |
| `aweme_detail.added_sound_music_info.video_duration` | integer | 视频时长。 |
| `aweme_detail.aigc_info` | object | 官方字段 `aigc_info`；官方未单独提供业务说明。 |
| `aweme_detail.aigc_info.aigc_label_type` | integer | 官方字段 `aigc_label_type`；官方未单独提供业务说明。 |
| `aweme_detail.aigc_info.created_by_ai` | boolean | 官方字段 `created_by_ai`；官方未单独提供业务说明。 |
| `aweme_detail.anchors` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.anchors_extras` | string | 官方字段 `anchors_extras`；官方未单独提供业务说明。 |
| `aweme_detail.animated_image_info` | object | 官方字段 `animated_image_info`；官方未单独提供业务说明。 |
| `aweme_detail.animated_image_info.effect` | integer | 官方字段 `effect`；官方未单独提供业务说明。 |
| `aweme_detail.animated_image_info.type` | integer | 类型。 |
| `aweme_detail.author` | object | 作者信息。 |
| `aweme_detail.author.accept_private_policy` | boolean | 官方字段 `accept_private_policy`；官方未单独提供业务说明。 |
| `aweme_detail.author.account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.account_region` | string | 官方字段 `account_region`；官方未单独提供业务说明。 |
| `aweme_detail.author.ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.apple_account` | integer | 官方字段 `apple_account`；官方未单独提供业务说明。 |
| `aweme_detail.author.authority_status` | integer | 官方字段 `authority_status`；官方未单独提供业务说明。 |
| `aweme_detail.author.avatar_168x168` | object | 官方字段 `avatar_168x168`；官方未单独提供业务说明。 |
| `aweme_detail.author.avatar_168x168.height` | integer | 高度。 |
| `aweme_detail.author.avatar_168x168.uri` | string | 资源标识。 |
| `aweme_detail.author.avatar_168x168.url_list` | array | 资源链接列表。 |
| `aweme_detail.author.avatar_168x168.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.author.avatar_168x168.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.avatar_168x168.width` | integer | 宽度。 |
| `aweme_detail.author.avatar_300x300` | object | 官方字段 `avatar_300x300`；官方未单独提供业务说明。 |
| `aweme_detail.author.avatar_300x300.height` | integer | 高度。 |
| `aweme_detail.author.avatar_300x300.uri` | string | 资源标识。 |
| `aweme_detail.author.avatar_300x300.url_list` | array | 资源链接列表。 |
| `aweme_detail.author.avatar_300x300.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.author.avatar_300x300.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.avatar_300x300.width` | integer | 宽度。 |
| `aweme_detail.author.avatar_larger` | object | 官方字段 `avatar_larger`；官方未单独提供业务说明。 |
| `aweme_detail.author.avatar_larger.height` | integer | 高度。 |
| `aweme_detail.author.avatar_larger.uri` | string | 资源标识。 |
| `aweme_detail.author.avatar_larger.url_list` | array | 资源链接列表。 |
| `aweme_detail.author.avatar_larger.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.author.avatar_larger.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.avatar_larger.width` | integer | 宽度。 |
| `aweme_detail.author.avatar_medium` | object | 中等尺寸头像。 |
| `aweme_detail.author.avatar_medium.height` | integer | 高度。 |
| `aweme_detail.author.avatar_medium.uri` | string | 资源标识。 |
| `aweme_detail.author.avatar_medium.url_list` | array | 资源链接列表。 |
| `aweme_detail.author.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.author.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.avatar_medium.width` | integer | 宽度。 |
| `aweme_detail.author.avatar_thumb` | object | 缩略头像。 |
| `aweme_detail.author.avatar_thumb.height` | integer | 高度。 |
| `aweme_detail.author.avatar_thumb.uri` | string | 资源标识。 |
| `aweme_detail.author.avatar_thumb.url_list` | array | 资源链接列表。 |
| `aweme_detail.author.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.author.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.avatar_thumb.width` | integer | 宽度。 |
| `aweme_detail.author.avatar_uri` | string | 官方字段 `avatar_uri`；官方未单独提供业务说明。 |
| `aweme_detail.author.aweme_count` | integer | 官方字段 `aweme_count`；官方未单独提供业务说明。 |
| `aweme_detail.author.bind_phone` | string | 官方字段 `bind_phone`；官方未单独提供业务说明。 |
| `aweme_detail.author.bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.can_message_follow_status_list` | array | 官方字段 `can_message_follow_status_list`；官方未单独提供业务说明。 |
| `aweme_detail.author.can_message_follow_status_list[]` | integer | 官方数组 `can_message_follow_status_list` 的元素。 |
| `aweme_detail.author.can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.comment_filter_status` | integer | 官方字段 `comment_filter_status`；官方未单独提供业务说明。 |
| `aweme_detail.author.comment_setting` | integer | 官方字段 `comment_setting`；官方未单独提供业务说明。 |
| `aweme_detail.author.commerce_user_level` | integer | 官方字段 `commerce_user_level`；官方未单独提供业务说明。 |
| `aweme_detail.author.cover_url` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.author.create_time` | integer | 创建时间。 |
| `aweme_detail.author.custom_verify` | string | 官方字段 `custom_verify`；官方未单独提供业务说明。 |
| `aweme_detail.author.cv_level` | string | 官方字段 `cv_level`；官方未单独提供业务说明。 |
| `aweme_detail.author.download_prompt_ts` | integer | 官方字段 `download_prompt_ts`；官方未单独提供业务说明。 |
| `aweme_detail.author.download_setting` | integer | 官方字段 `download_setting`；官方未单独提供业务说明。 |
| `aweme_detail.author.duet_setting` | integer | 官方字段 `duet_setting`；官方未单独提供业务说明。 |
| `aweme_detail.author.enabled_filter_all_comments` | boolean | 官方字段 `enabled_filter_all_comments`；官方未单独提供业务说明。 |
| `aweme_detail.author.enterprise_verify_reason` | string | 官方字段 `enterprise_verify_reason`；官方未单独提供业务说明。 |
| `aweme_detail.author.events` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.fake_data_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_detail.author.favoriting_count` | integer | 官方字段 `favoriting_count`；官方未单独提供业务说明。 |
| `aweme_detail.author.fb_expire_time` | integer | 官方字段 `fb_expire_time`；官方未单独提供业务说明。 |
| `aweme_detail.author.follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `aweme_detail.author.follower_count` | integer | 粉丝数量。 |
| `aweme_detail.author.follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `aweme_detail.author.followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.following_count` | integer | 关注数量。 |
| `aweme_detail.author.friends_status` | integer | 官方字段 `friends_status`；官方未单独提供业务说明。 |
| `aweme_detail.author.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.google_account` | string | 官方字段 `google_account`；官方未单独提供业务说明。 |
| `aweme_detail.author.has_email` | boolean | 官方字段 `has_email`；官方未单独提供业务说明。 |
| `aweme_detail.author.has_facebook_token` | boolean | 官方字段 `has_facebook_token`；官方未单独提供业务说明。 |
| `aweme_detail.author.has_insights` | boolean | 官方字段 `has_insights`；官方未单独提供业务说明。 |
| `aweme_detail.author.has_orders` | boolean | 官方字段 `has_orders`；官方未单独提供业务说明。 |
| `aweme_detail.author.has_twitter_token` | boolean | 官方字段 `has_twitter_token`；官方未单独提供业务说明。 |
| `aweme_detail.author.has_youtube_token` | boolean | 官方字段 `has_youtube_token`；官方未单独提供业务说明。 |
| `aweme_detail.author.hide_search` | boolean | 官方字段 `hide_search`；官方未单独提供业务说明。 |
| `aweme_detail.author.homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.ins_id` | string | 官方字段 `ins_id`；官方未单独提供业务说明。 |
| `aweme_detail.author.is_ad_fake` | boolean | 官方字段 `is_ad_fake`；官方未单独提供业务说明。 |
| `aweme_detail.author.is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `aweme_detail.author.is_discipline_member` | boolean | 官方字段 `is_discipline_member`；官方未单独提供业务说明。 |
| `aweme_detail.author.is_mute` | integer | 官方字段 `is_mute`；官方未单独提供业务说明。 |
| `aweme_detail.author.is_mute_lives` | integer | 官方字段 `is_mute_lives`；官方未单独提供业务说明。 |
| `aweme_detail.author.is_mute_non_story_post` | integer | 官方字段 `is_mute_non_story_post`；官方未单独提供业务说明。 |
| `aweme_detail.author.is_mute_story` | integer | 官方字段 `is_mute_story`；官方未单独提供业务说明。 |
| `aweme_detail.author.is_phone_binded` | boolean | 官方字段 `is_phone_binded`；官方未单独提供业务说明。 |
| `aweme_detail.author.is_star` | boolean | 官方字段 `is_star`；官方未单独提供业务说明。 |
| `aweme_detail.author.item_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.language` | string | 语言。 |
| `aweme_detail.author.live_agreement` | integer | 官方字段 `live_agreement`；官方未单独提供业务说明。 |
| `aweme_detail.author.live_commerce` | boolean | 官方字段 `live_commerce`；官方未单独提供业务说明。 |
| `aweme_detail.author.live_verify` | integer | 官方字段 `live_verify`；官方未单独提供业务说明。 |
| `aweme_detail.author.mention_status` | integer | 官方字段 `mention_status`；官方未单独提供业务说明。 |
| `aweme_detail.author.mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.need_points` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.need_recommend` | integer | 官方字段 `need_recommend`；官方未单独提供业务说明。 |
| `aweme_detail.author.nickname` | string | 昵称。 |
| `aweme_detail.author.platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `aweme_detail.author.react_setting` | integer | 官方字段 `react_setting`；官方未单独提供业务说明。 |
| `aweme_detail.author.region` | string | 地区。 |
| `aweme_detail.author.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.reply_with_video_flag` | integer | 官方字段 `reply_with_video_flag`；官方未单独提供业务说明。 |
| `aweme_detail.author.room_id` | integer | 官方字段 `room_id`；官方未单独提供业务说明。 |
| `aweme_detail.author.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_detail.author.secret` | integer | 官方字段 `secret`；官方未单独提供业务说明。 |
| `aweme_detail.author.share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `aweme_detail.author.share_info.now_invitation_card_image_urls` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.share_info.share_desc` | string | 官方字段 `share_desc`；官方未单独提供业务说明。 |
| `aweme_detail.author.share_info.share_desc_info` | string | 官方字段 `share_desc_info`；官方未单独提供业务说明。 |
| `aweme_detail.author.share_info.share_qrcode_url` | object | 官方字段 `share_qrcode_url`；官方未单独提供业务说明。 |
| `aweme_detail.author.share_info.share_qrcode_url.height` | integer | 高度。 |
| `aweme_detail.author.share_info.share_qrcode_url.uri` | string | 资源标识。 |
| `aweme_detail.author.share_info.share_qrcode_url.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.author.share_info.share_qrcode_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.share_info.share_qrcode_url.width` | integer | 宽度。 |
| `aweme_detail.author.share_info.share_title` | string | 官方字段 `share_title`；官方未单独提供业务说明。 |
| `aweme_detail.author.share_info.share_title_myself` | string | 官方字段 `share_title_myself`；官方未单独提供业务说明。 |
| `aweme_detail.author.share_info.share_title_other` | string | 官方字段 `share_title_other`；官方未单独提供业务说明。 |
| `aweme_detail.author.share_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `aweme_detail.author.share_qrcode_uri` | string | 官方字段 `share_qrcode_uri`；官方未单独提供业务说明。 |
| `aweme_detail.author.shield_comment_notice` | integer | 官方字段 `shield_comment_notice`；官方未单独提供业务说明。 |
| `aweme_detail.author.shield_digg_notice` | integer | 官方字段 `shield_digg_notice`；官方未单独提供业务说明。 |
| `aweme_detail.author.shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.shield_follow_notice` | integer | 官方字段 `shield_follow_notice`；官方未单独提供业务说明。 |
| `aweme_detail.author.short_id` | string | 官方字段 `short_id`；官方未单独提供业务说明。 |
| `aweme_detail.author.show_image_bubble` | boolean | 官方字段 `show_image_bubble`；官方未单独提供业务说明。 |
| `aweme_detail.author.signature` | string | 官方字段 `signature`；官方未单独提供业务说明。 |
| `aweme_detail.author.special_account` | object | 官方字段 `special_account`；官方未单独提供业务说明。 |
| `aweme_detail.author.special_account.special_account_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.special_lock` | integer | 官方字段 `special_lock`；官方未单独提供业务说明。 |
| `aweme_detail.author.status` | integer | 状态。 |
| `aweme_detail.author.stitch_setting` | integer | 官方字段 `stitch_setting`；官方未单独提供业务说明。 |
| `aweme_detail.author.story_status` | integer | 官方字段 `story_status`；官方未单独提供业务说明。 |
| `aweme_detail.author.total_favorited` | integer | 官方字段 `total_favorited`；官方未单独提供业务说明。 |
| `aweme_detail.author.tw_expire_time` | integer | 官方字段 `tw_expire_time`；官方未单独提供业务说明。 |
| `aweme_detail.author.twitter_id` | string | 官方字段 `twitter_id`；官方未单独提供业务说明。 |
| `aweme_detail.author.twitter_name` | string | 官方字段 `twitter_name`；官方未单独提供业务说明。 |
| `aweme_detail.author.type_label` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.uid` | string | 用户标识。 |
| `aweme_detail.author.unique_id` | string | 账号唯一名称。 |
| `aweme_detail.author.unique_id_modify_time` | integer | 官方字段 `unique_id_modify_time`；官方未单独提供业务说明。 |
| `aweme_detail.author.user_canceled` | boolean | 官方字段 `user_canceled`；官方未单独提供业务说明。 |
| `aweme_detail.author.user_mode` | integer | 官方字段 `user_mode`；官方未单独提供业务说明。 |
| `aweme_detail.author.user_now_pack_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_detail.author.user_period` | integer | 官方字段 `user_period`；官方未单独提供业务说明。 |
| `aweme_detail.author.user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.user_rate` | integer | 官方字段 `user_rate`；官方未单独提供业务说明。 |
| `aweme_detail.author.user_spark_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_detail.author.user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.verification_type` | integer | 官方字段 `verification_type`；官方未单独提供业务说明。 |
| `aweme_detail.author.verify_info` | string | 官方字段 `verify_info`；官方未单独提供业务说明。 |
| `aweme_detail.author.video_icon` | object | 官方字段 `video_icon`；官方未单独提供业务说明。 |
| `aweme_detail.author.video_icon.height` | integer | 高度。 |
| `aweme_detail.author.video_icon.uri` | string | 资源标识。 |
| `aweme_detail.author.video_icon.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.author.video_icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.video_icon.width` | integer | 宽度。 |
| `aweme_detail.author.white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.author.with_commerce_entry` | boolean | 官方字段 `with_commerce_entry`；官方未单独提供业务说明。 |
| `aweme_detail.author.with_shop_entry` | boolean | 官方字段 `with_shop_entry`；官方未单独提供业务说明。 |
| `aweme_detail.author.youtube_channel_id` | string | 官方字段 `youtube_channel_id`；官方未单独提供业务说明。 |
| `aweme_detail.author.youtube_channel_title` | string | 官方字段 `youtube_channel_title`；官方未单独提供业务说明。 |
| `aweme_detail.author.youtube_expire_time` | integer | 官方字段 `youtube_expire_time`；官方未单独提供业务说明。 |
| `aweme_detail.author_user_id` | integer | 官方字段 `author_user_id`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl` | object | 官方字段 `aweme_acl`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.download_general` | object | 官方字段 `download_general`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.download_general.code` | integer | 官方业务编码。 |
| `aweme_detail.aweme_acl.download_general.mute` | boolean | 官方字段 `mute`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.download_general.show_type` | integer | 官方字段 `show_type`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.download_general.transcode` | integer | 官方字段 `transcode`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.download_mask_panel` | object | 官方字段 `download_mask_panel`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.download_mask_panel.code` | integer | 官方业务编码。 |
| `aweme_detail.aweme_acl.download_mask_panel.mute` | boolean | 官方字段 `mute`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.download_mask_panel.show_type` | integer | 官方字段 `show_type`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.download_mask_panel.transcode` | integer | 官方字段 `transcode`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.platform_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.aweme_acl.press_action_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.aweme_acl.share_action_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.aweme_acl.share_general` | object | 官方字段 `share_general`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.share_general.code` | integer | 官方业务编码。 |
| `aweme_detail.aweme_acl.share_general.mute` | boolean | 官方字段 `mute`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.share_general.show_type` | integer | 官方字段 `show_type`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.share_general.transcode` | integer | 官方字段 `transcode`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_acl.share_list_status` | integer | 官方字段 `share_list_status`；官方未单独提供业务说明。 |
| `aweme_detail.aweme_id` | string | TikTok 视频标识。 |
| `aweme_detail.aweme_type` | integer | 官方字段 `aweme_type`；官方未单独提供业务说明。 |
| `aweme_detail.banners` | array | 官方字段 `banners`；官方未单独提供业务说明。 |
| `aweme_detail.banners[].key` | object | 官方字段 `key`；官方未单独提供业务说明。 |
| `aweme_detail.banners[].key.component_key` | string | 官方字段 `component_key`；官方未单独提供业务说明。 |
| `aweme_detail.behind_the_song_music_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.behind_the_song_video_music_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.bodydance_score` | integer | 官方字段 `bodydance_score`；官方未单独提供业务说明。 |
| `aweme_detail.branded_content_accounts` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.c2pa_info` | object | 官方字段 `c2pa_info`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.aigc_src` | string | 官方字段 `aigc_src`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.dedup_err` | string | 官方字段 `dedup_err`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.dedup_src` | string | 官方字段 `dedup_src`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.first_aigc_src` | string | 官方字段 `first_aigc_src`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.first_src` | string | 官方字段 `first_src`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.is_capcut` | boolean | 官方字段 `is_capcut`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.is_tiktok` | boolean | 官方字段 `is_tiktok`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.last_aigc_src` | string | 官方字段 `last_aigc_src`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.last_src` | string | 官方字段 `last_src`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.total_audio` | integer | 官方字段 `total_audio`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.total_err` | integer | 官方字段 `total_err`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.total_img` | integer | 官方字段 `total_img`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.total_src` | integer | 官方字段 `total_src`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.total_vid` | integer | 官方字段 `total_vid`；官方未单独提供业务说明。 |
| `aweme_detail.c2pa_info.upload_dur` | number | 官方字段 `upload_dur`；官方未单独提供业务说明。 |
| `aweme_detail.cc_template_info` | object | 官方字段 `cc_template_info`；官方未单独提供业务说明。 |
| `aweme_detail.cc_template_info.author_name` | string | 官方字段 `author_name`；官方未单独提供业务说明。 |
| `aweme_detail.cc_template_info.clip_count` | integer | 官方字段 `clip_count`；官方未单独提供业务说明。 |
| `aweme_detail.cc_template_info.desc` | string | 描述。 |
| `aweme_detail.cc_template_info.duration_milliseconds` | integer | 官方字段 `duration_milliseconds`；官方未单独提供业务说明。 |
| `aweme_detail.cc_template_info.related_music_id` | string | 官方字段 `related_music_id`；官方未单独提供业务说明。 |
| `aweme_detail.cc_template_info.template_id` | string | 官方字段 `template_id`；官方未单独提供业务说明。 |
| `aweme_detail.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.challenge_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.cmt_swt` | boolean | 官方字段 `cmt_swt`；官方未单独提供业务说明。 |
| `aweme_detail.collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `aweme_detail.comment_config` | object | 官方字段 `comment_config`；官方未单独提供业务说明。 |
| `aweme_detail.comment_config.comment_panel_show_tab_config` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.comment_config.emoji_recommend_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.comment_config.long_press_recommend_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.comment_config.preload` | object | 官方字段 `preload`；官方未单独提供业务说明。 |
| `aweme_detail.comment_config.preload.preds` | string | 官方字段 `preds`；官方未单独提供业务说明。 |
| `aweme_detail.comment_config.quick_comment` | object | 官方字段 `quick_comment`；官方未单独提供业务说明。 |
| `aweme_detail.comment_config.quick_comment.enabled` | boolean | 官方字段 `enabled`；官方未单独提供业务说明。 |
| `aweme_detail.comment_config.quick_comment_emoji_recommend_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.comment_topbar_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.commerce_config_data` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.commerce_info` | object | 官方字段 `commerce_info`；官方未单独提供业务说明。 |
| `aweme_detail.commerce_info.adv_promotable` | boolean | 官方字段 `adv_promotable`；官方未单独提供业务说明。 |
| `aweme_detail.commerce_info.auction_ad_invited` | boolean | 官方字段 `auction_ad_invited`；官方未单独提供业务说明。 |
| `aweme_detail.commerce_info.branded_content_type` | integer | 官方字段 `branded_content_type`；官方未单独提供业务说明。 |
| `aweme_detail.commerce_info.with_comment_filter_words` | boolean | 官方字段 `with_comment_filter_words`；官方未单独提供业务说明。 |
| `aweme_detail.content_desc` | string | 官方字段 `content_desc`；官方未单独提供业务说明。 |
| `aweme_detail.content_desc_extra` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.content_model` | object | 官方字段 `content_model`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.custom_biz` | object | 官方字段 `custom_biz`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.custom_biz.aweme_trace` | string | 官方字段 `aweme_trace`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz` | object | 官方字段 `standard_biz`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.creator_analytics` | object | 官方字段 `creator_analytics`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.creator_analytics.creator_analytics_entrance_status` | integer | 官方字段 `creator_analytics_entrance_status`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.e_commerce` | object | 官方字段 `e_commerce`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.e_commerce.ttec_content_tag` | object | 官方字段 `ttec_content_tag`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.e_commerce.ttec_content_tag.recommendation_tag_consumer_str` | string | 官方字段 `recommendation_tag_consumer_str`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.e_commerce.ttec_content_tag.recommendation_tag_creator_str` | string | 官方字段 `recommendation_tag_creator_str`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.tts_voice_info` | object | 官方字段 `tts_voice_info`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.tts_voice_info.tts_voice_attr` | string | 官方字段 `tts_voice_attr`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.tts_voice_info.tts_voice_reuse_params` | string | 官方字段 `tts_voice_reuse_params`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.vc_filter_info` | object | 官方字段 `vc_filter_info`；官方未单独提供业务说明。 |
| `aweme_detail.content_model.standard_biz.vc_filter_info.vc_filter_attr` | string | 官方字段 `vc_filter_attr`；官方未单独提供业务说明。 |
| `aweme_detail.content_original_type` | integer | 官方字段 `content_original_type`；官方未单独提供业务说明。 |
| `aweme_detail.content_size_type` | integer | 官方字段 `content_size_type`；官方未单独提供业务说明。 |
| `aweme_detail.content_type` | string | 官方字段 `content_type`；官方未单独提供业务说明。 |
| `aweme_detail.cover_labels` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.create_time` | integer | 创建时间。 |
| `aweme_detail.creation_info` | object | 官方字段 `creation_info`；官方未单独提供业务说明。 |
| `aweme_detail.creation_info.creation_used_functions` | array | 官方字段 `creation_used_functions`；官方未单独提供业务说明。 |
| `aweme_detail.creation_info.creation_used_functions[]` | string | 官方数组 `creation_used_functions` 的元素。 |
| `aweme_detail.desc` | string | 描述。 |
| `aweme_detail.desc_language` | string | 官方字段 `desc_language`；官方未单独提供业务说明。 |
| `aweme_detail.disable_search_trending_bar` | boolean | 官方字段 `disable_search_trending_bar`；官方未单独提供业务说明。 |
| `aweme_detail.distance` | string | 官方字段 `distance`；官方未单独提供业务说明。 |
| `aweme_detail.distribute_type` | integer | 官方字段 `distribute_type`；官方未单独提供业务说明。 |
| `aweme_detail.follow_up_publish_from_id` | integer | 官方字段 `follow_up_publish_from_id`；官方未单独提供业务说明。 |
| `aweme_detail.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.geofencing_regions` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.green_screen_materials` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.group_id` | string | 官方字段 `group_id`；官方未单独提供业务说明。 |
| `aweme_detail.group_id_list` | object | 官方字段 `group_id_list`；官方未单独提供业务说明。 |
| `aweme_detail.group_id_list.GroupdIdList0` | array | 官方字段 `GroupdIdList0`；官方未单独提供业务说明。 |
| `aweme_detail.group_id_list.GroupdIdList0[]` | integer | 官方数组 `GroupdIdList0` 的元素。 |
| `aweme_detail.group_id_list.GroupdIdList1` | array | 官方字段 `GroupdIdList1`；官方未单独提供业务说明。 |
| `aweme_detail.group_id_list.GroupdIdList1[]` | integer | 官方数组 `GroupdIdList1` 的元素。 |
| `aweme_detail.has_danmaku` | boolean | 官方字段 `has_danmaku`；官方未单独提供业务说明。 |
| `aweme_detail.has_promote_entry` | integer | 官方字段 `has_promote_entry`；官方未单独提供业务说明。 |
| `aweme_detail.has_vs_entry` | boolean | 官方字段 `has_vs_entry`；官方未单独提供业务说明。 |
| `aweme_detail.have_dashboard` | boolean | 官方字段 `have_dashboard`；官方未单独提供业务说明。 |
| `aweme_detail.hybrid_label` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.image_infos` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.interact_permission` | object | 官方字段 `interact_permission`；官方未单独提供业务说明。 |
| `aweme_detail.interact_permission.allow_adding_as_post` | object | 官方字段 `allow_adding_as_post`；官方未单独提供业务说明。 |
| `aweme_detail.interact_permission.allow_adding_as_post.status` | integer | 状态。 |
| `aweme_detail.interact_permission.allow_adding_to_story` | integer | 官方字段 `allow_adding_to_story`；官方未单独提供业务说明。 |
| `aweme_detail.interact_permission.allow_create_sticker` | object | 官方字段 `allow_create_sticker`；官方未单独提供业务说明。 |
| `aweme_detail.interact_permission.allow_create_sticker.status` | integer | 状态。 |
| `aweme_detail.interact_permission.allow_story_switch_to_post` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_detail.interact_permission.duet` | integer | 官方字段 `duet`；官方未单独提供业务说明。 |
| `aweme_detail.interact_permission.duet_privacy_setting` | integer | 官方字段 `duet_privacy_setting`；官方未单独提供业务说明。 |
| `aweme_detail.interact_permission.stitch` | integer | 官方字段 `stitch`；官方未单独提供业务说明。 |
| `aweme_detail.interact_permission.stitch_privacy_setting` | integer | 官方字段 `stitch_privacy_setting`；官方未单独提供业务说明。 |
| `aweme_detail.interact_permission.upvote` | integer | 官方字段 `upvote`；官方未单独提供业务说明。 |
| `aweme_detail.interaction_stickers` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.is_ads` | boolean | 官方字段 `is_ads`；官方未单独提供业务说明。 |
| `aweme_detail.is_description_translatable` | boolean | 官方字段 `is_description_translatable`；官方未单独提供业务说明。 |
| `aweme_detail.is_hash_tag` | integer | 官方字段 `is_hash_tag`；官方未单独提供业务说明。 |
| `aweme_detail.is_nff_or_nr` | boolean | 官方字段 `is_nff_or_nr`；官方未单独提供业务说明。 |
| `aweme_detail.is_on_this_day` | integer | 官方字段 `is_on_this_day`；官方未单独提供业务说明。 |
| `aweme_detail.is_pgcshow` | boolean | 官方字段 `is_pgcshow`；官方未单独提供业务说明。 |
| `aweme_detail.is_preview` | integer | 官方字段 `is_preview`；官方未单独提供业务说明。 |
| `aweme_detail.is_relieve` | boolean | 官方字段 `is_relieve`；官方未单独提供业务说明。 |
| `aweme_detail.is_text_sticker_translatable` | boolean | 官方字段 `is_text_sticker_translatable`；官方未单独提供业务说明。 |
| `aweme_detail.is_title_translatable` | boolean | 官方字段 `is_title_translatable`；官方未单独提供业务说明。 |
| `aweme_detail.is_top` | integer | 官方字段 `is_top`；官方未单独提供业务说明。 |
| `aweme_detail.is_vr` | boolean | 官方字段 `is_vr`；官方未单独提供业务说明。 |
| `aweme_detail.item_comment_settings` | integer | 官方字段 `item_comment_settings`；官方未单独提供业务说明。 |
| `aweme_detail.item_duet` | integer | 官方字段 `item_duet`；官方未单独提供业务说明。 |
| `aweme_detail.item_react` | integer | 官方字段 `item_react`；官方未单独提供业务说明。 |
| `aweme_detail.item_stitch` | integer | 官方字段 `item_stitch`；官方未单独提供业务说明。 |
| `aweme_detail.label_top` | object | 官方字段 `label_top`；官方未单独提供业务说明。 |
| `aweme_detail.label_top.height` | integer | 高度。 |
| `aweme_detail.label_top.uri` | string | 资源标识。 |
| `aweme_detail.label_top.url_list` | array | 资源链接列表。 |
| `aweme_detail.label_top.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.label_top.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.label_top.width` | integer | 宽度。 |
| `aweme_detail.label_top_text` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.long_video` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.main_arch_common` | string | 官方字段 `main_arch_common`；官方未单独提供业务说明。 |
| `aweme_detail.mask_infos` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.misc_info` | string | 官方字段 `misc_info`；官方未单独提供业务说明。 |
| `aweme_detail.muf_comment_info_v2` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music` | object | 官方字段 `music`；官方未单独提供业务说明。 |
| `aweme_detail.music.album` | string | 官方字段 `album`；官方未单独提供业务说明。 |
| `aweme_detail.music.allow_offline_music_to_detail_page` | boolean | 官方字段 `allow_offline_music_to_detail_page`；官方未单独提供业务说明。 |
| `aweme_detail.music.artists` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.music.audition_duration` | integer | 官方字段 `audition_duration`；官方未单独提供业务说明。 |
| `aweme_detail.music.author` | string | 作者信息。 |
| `aweme_detail.music.author_deleted` | boolean | 官方字段 `author_deleted`；官方未单独提供业务说明。 |
| `aweme_detail.music.author_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.avatar_medium` | object | 中等尺寸头像。 |
| `aweme_detail.music.avatar_medium.height` | integer | 高度。 |
| `aweme_detail.music.avatar_medium.uri` | string | 资源标识。 |
| `aweme_detail.music.avatar_medium.url_list` | array | 资源链接列表。 |
| `aweme_detail.music.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.music.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.avatar_medium.width` | integer | 宽度。 |
| `aweme_detail.music.avatar_thumb` | object | 缩略头像。 |
| `aweme_detail.music.avatar_thumb.height` | integer | 高度。 |
| `aweme_detail.music.avatar_thumb.uri` | string | 资源标识。 |
| `aweme_detail.music.avatar_thumb.url_list` | array | 资源链接列表。 |
| `aweme_detail.music.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.music.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.avatar_thumb.width` | integer | 宽度。 |
| `aweme_detail.music.binded_challenge_id` | integer | 官方字段 `binded_challenge_id`；官方未单独提供业务说明。 |
| `aweme_detail.music.can_be_stitched` | boolean | 官方字段 `can_be_stitched`；官方未单独提供业务说明。 |
| `aweme_detail.music.can_not_reuse` | boolean | 官方字段 `can_not_reuse`；官方未单独提供业务说明。 |
| `aweme_detail.music.collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `aweme_detail.music.commercial_right_type` | integer | 官方字段 `commercial_right_type`；官方未单独提供业务说明。 |
| `aweme_detail.music.cover_large` | object | 官方字段 `cover_large`；官方未单独提供业务说明。 |
| `aweme_detail.music.cover_large.height` | integer | 高度。 |
| `aweme_detail.music.cover_large.uri` | string | 资源标识。 |
| `aweme_detail.music.cover_large.url_list` | array | 资源链接列表。 |
| `aweme_detail.music.cover_large.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.music.cover_large.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.cover_large.width` | integer | 宽度。 |
| `aweme_detail.music.cover_medium` | object | 官方字段 `cover_medium`；官方未单独提供业务说明。 |
| `aweme_detail.music.cover_medium.height` | integer | 高度。 |
| `aweme_detail.music.cover_medium.uri` | string | 资源标识。 |
| `aweme_detail.music.cover_medium.url_list` | array | 资源链接列表。 |
| `aweme_detail.music.cover_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.music.cover_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.cover_medium.width` | integer | 宽度。 |
| `aweme_detail.music.cover_thumb` | object | 官方字段 `cover_thumb`；官方未单独提供业务说明。 |
| `aweme_detail.music.cover_thumb.height` | integer | 高度。 |
| `aweme_detail.music.cover_thumb.uri` | string | 资源标识。 |
| `aweme_detail.music.cover_thumb.url_list` | array | 资源链接列表。 |
| `aweme_detail.music.cover_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.music.cover_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.cover_thumb.width` | integer | 宽度。 |
| `aweme_detail.music.create_time` | integer | 创建时间。 |
| `aweme_detail.music.dmv_auto_show` | boolean | 官方字段 `dmv_auto_show`；官方未单独提供业务说明。 |
| `aweme_detail.music.duration` | integer | 时长。 |
| `aweme_detail.music.duration_high_precision` | object | 官方字段 `duration_high_precision`；官方未单独提供业务说明。 |
| `aweme_detail.music.duration_high_precision.audition_duration_precision` | number | 官方字段 `audition_duration_precision`；官方未单独提供业务说明。 |
| `aweme_detail.music.duration_high_precision.duration_precision` | number | 官方字段 `duration_precision`；官方未单独提供业务说明。 |
| `aweme_detail.music.duration_high_precision.shoot_duration_precision` | number | 官方字段 `shoot_duration_precision`；官方未单独提供业务说明。 |
| `aweme_detail.music.duration_high_precision.video_duration_precision` | number | 官方字段 `video_duration_precision`；官方未单独提供业务说明。 |
| `aweme_detail.music.external_song_info` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.music.extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `aweme_detail.music.has_commerce_right` | boolean | 官方字段 `has_commerce_right`；官方未单独提供业务说明。 |
| `aweme_detail.music.id` | integer | 标识符。 |
| `aweme_detail.music.id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `aweme_detail.music.is_audio_url_with_cookie` | boolean | 官方字段 `is_audio_url_with_cookie`；官方未单独提供业务说明。 |
| `aweme_detail.music.is_author_artist` | boolean | 官方字段 `is_author_artist`；官方未单独提供业务说明。 |
| `aweme_detail.music.is_commerce_music` | boolean | 官方字段 `is_commerce_music`；官方未单独提供业务说明。 |
| `aweme_detail.music.is_matched_metadata` | boolean | 官方字段 `is_matched_metadata`；官方未单独提供业务说明。 |
| `aweme_detail.music.is_original` | boolean | 官方字段 `is_original`；官方未单独提供业务说明。 |
| `aweme_detail.music.is_original_sound` | boolean | 官方字段 `is_original_sound`；官方未单独提供业务说明。 |
| `aweme_detail.music.is_pgc` | boolean | 官方字段 `is_pgc`；官方未单独提供业务说明。 |
| `aweme_detail.music.is_play_music` | boolean | 官方字段 `is_play_music`；官方未单独提供业务说明。 |
| `aweme_detail.music.is_shooting_allow` | boolean | 官方字段 `is_shooting_allow`；官方未单独提供业务说明。 |
| `aweme_detail.music.log_extra` | string | 官方字段 `log_extra`；官方未单独提供业务说明。 |
| `aweme_detail.music.lyric_short_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.meme_song_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_detail.music.mid` | string | 官方字段 `mid`；官方未单独提供业务说明。 |
| `aweme_detail.music.multi_bit_rate_play_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.mute_share` | boolean | 官方字段 `mute_share`；官方未单独提供业务说明。 |
| `aweme_detail.music.offline_desc` | string | 官方字段 `offline_desc`；官方未单独提供业务说明。 |
| `aweme_detail.music.owner_handle` | string | 官方字段 `owner_handle`；官方未单独提供业务说明。 |
| `aweme_detail.music.owner_id` | string | 官方字段 `owner_id`；官方未单独提供业务说明。 |
| `aweme_detail.music.owner_nickname` | string | 官方字段 `owner_nickname`；官方未单独提供业务说明。 |
| `aweme_detail.music.play_url` | object | 官方字段 `play_url`；官方未单独提供业务说明。 |
| `aweme_detail.music.play_url.height` | integer | 高度。 |
| `aweme_detail.music.play_url.uri` | string | 资源标识。 |
| `aweme_detail.music.play_url.url_list` | array | 资源链接列表。 |
| `aweme_detail.music.play_url.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.music.play_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.play_url.width` | integer | 宽度。 |
| `aweme_detail.music.position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `aweme_detail.music.preview_end_time` | integer | 官方字段 `preview_end_time`；官方未单独提供业务说明。 |
| `aweme_detail.music.preview_start_time` | integer | 官方字段 `preview_start_time`；官方未单独提供业务说明。 |
| `aweme_detail.music.recommend_status` | integer | 官方字段 `recommend_status`；官方未单独提供业务说明。 |
| `aweme_detail.music.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_detail.music.shoot_duration` | integer | 官方字段 `shoot_duration`；官方未单独提供业务说明。 |
| `aweme_detail.music.source_platform` | integer | 官方字段 `source_platform`；官方未单独提供业务说明。 |
| `aweme_detail.music.status` | integer | 状态。 |
| `aweme_detail.music.tag_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.title` | string | 标题。 |
| `aweme_detail.music.tt_to_dsp_song_infos` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.music.uncert_artists` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.music.user_count` | integer | 官方字段 `user_count`；官方未单独提供业务说明。 |
| `aweme_detail.music.video_duration` | integer | 视频时长。 |
| `aweme_detail.music_begin_time_in_ms` | integer | 官方字段 `music_begin_time_in_ms`；官方未单独提供业务说明。 |
| `aweme_detail.music_end_time_in_ms` | integer | 官方字段 `music_end_time_in_ms`；官方未单独提供业务说明。 |
| `aweme_detail.music_selected_from` | string | 官方字段 `music_selected_from`；官方未单独提供业务说明。 |
| `aweme_detail.music_title_style` | integer | 官方字段 `music_title_style`；官方未单独提供业务说明。 |
| `aweme_detail.music_volume` | string | 官方字段 `music_volume`；官方未单独提供业务说明。 |
| `aweme_detail.need_trim_step` | boolean | 官方字段 `need_trim_step`；官方未单独提供业务说明。 |
| `aweme_detail.need_vs_entry` | boolean | 官方字段 `need_vs_entry`；官方未单独提供业务说明。 |
| `aweme_detail.nickname_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.no_selected_music` | boolean | 官方字段 `no_selected_music`；官方未单独提供业务说明。 |
| `aweme_detail.operator_boost_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.origin_comment_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.origin_volume` | string | 官方字段 `origin_volume`；官方未单独提供业务说明。 |
| `aweme_detail.original_client_text` | object | 官方字段 `original_client_text`；官方未单独提供业务说明。 |
| `aweme_detail.original_client_text.markup_text` | string | 官方字段 `markup_text`；官方未单独提供业务说明。 |
| `aweme_detail.original_client_text.text_extra` | array | 官方字段 `text_extra`；官方未单独提供业务说明。 |
| `aweme_detail.original_client_text.text_extra[].sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_detail.original_client_text.text_extra[].tag_id` | string | 官方字段 `tag_id`；官方未单独提供业务说明。 |
| `aweme_detail.original_client_text.text_extra[].type` | integer | 类型。 |
| `aweme_detail.original_client_text.text_extra[].user_id` | string | 用户标识。 |
| `aweme_detail.picked_users` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.playlist_blocked` | boolean | 官方字段 `playlist_blocked`；官方未单独提供业务说明。 |
| `aweme_detail.playlist_info` | object | 官方字段 `playlist_info`；官方未单独提供业务说明。 |
| `aweme_detail.playlist_info.index` | integer | 官方字段 `index`；官方未单独提供业务说明。 |
| `aweme_detail.playlist_info.item_total` | integer | 官方字段 `item_total`；官方未单独提供业务说明。 |
| `aweme_detail.playlist_info.mix_id` | string | 官方字段 `mix_id`；官方未单独提供业务说明。 |
| `aweme_detail.playlist_info.name` | string | 名称。 |
| `aweme_detail.poi_re_tag_signal` | integer | 官方字段 `poi_re_tag_signal`；官方未单独提供业务说明。 |
| `aweme_detail.position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `aweme_detail.products_info` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.promote_capcut_toggle` | integer | 官方字段 `promote_capcut_toggle`；官方未单独提供业务说明。 |
| `aweme_detail.promote_icon_text` | string | 官方字段 `promote_icon_text`；官方未单独提供业务说明。 |
| `aweme_detail.promote_toast` | string | 官方字段 `promote_toast`；官方未单独提供业务说明。 |
| `aweme_detail.promote_toast_key` | string | 官方字段 `promote_toast_key`；官方未单独提供业务说明。 |
| `aweme_detail.question_list` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.quick_reply_emojis` | array | 官方字段 `quick_reply_emojis`；官方未单独提供业务说明。 |
| `aweme_detail.quick_reply_emojis[]` | string | 官方数组 `quick_reply_emojis` 的元素。 |
| `aweme_detail.rate` | integer | 官方字段 `rate`；官方未单独提供业务说明。 |
| `aweme_detail.reference_tts_voice_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.reference_voice_filter_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.region` | string | 地区。 |
| `aweme_detail.risk_infos` | object | 官方字段 `risk_infos`；官方未单独提供业务说明。 |
| `aweme_detail.risk_infos.content` | string | 官方字段 `content`；官方未单独提供业务说明。 |
| `aweme_detail.risk_infos.risk_sink` | boolean | 官方字段 `risk_sink`；官方未单独提供业务说明。 |
| `aweme_detail.risk_infos.type` | integer | 类型。 |
| `aweme_detail.risk_infos.vote` | boolean | 官方字段 `vote`；官方未单独提供业务说明。 |
| `aweme_detail.risk_infos.warn` | boolean | 官方字段 `warn`；官方未单独提供业务说明。 |
| `aweme_detail.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.bool_persist` | integer | 官方字段 `bool_persist`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.now_invitation_card_image_urls` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.share_info.share_desc` | string | 官方字段 `share_desc`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.share_desc_info` | string | 官方字段 `share_desc_info`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.share_link_desc` | string | 官方字段 `share_link_desc`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.share_quote` | string | 官方字段 `share_quote`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.share_signature_desc` | string | 官方字段 `share_signature_desc`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.share_signature_url` | string | 官方字段 `share_signature_url`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.share_title` | string | 官方字段 `share_title`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.share_title_myself` | string | 官方字段 `share_title_myself`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.share_title_other` | string | 官方字段 `share_title_other`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `aweme_detail.share_info.whatsapp_desc` | string | 官方字段 `whatsapp_desc`；官方未单独提供业务说明。 |
| `aweme_detail.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `aweme_detail.shoot_tab_name` | string | 官方字段 `shoot_tab_name`；官方未单独提供业务说明。 |
| `aweme_detail.social_interaction_blob` | object | 官方字段 `social_interaction_blob`；官方未单独提供业务说明。 |
| `aweme_detail.social_interaction_blob.auxiliary_model_content` | string | 官方字段 `auxiliary_model_content`；官方未单独提供业务说明。 |
| `aweme_detail.solaria_profile` | object | 官方字段 `solaria_profile`；官方未单独提供业务说明。 |
| `aweme_detail.solaria_profile.profile` | string | 官方字段 `profile`；官方未单独提供业务说明。 |
| `aweme_detail.sort_label` | string | 官方字段 `sort_label`；官方未单独提供业务说明。 |
| `aweme_detail.standard_component_info` | object | 官方字段 `standard_component_info`；官方未单独提供业务说明。 |
| `aweme_detail.standard_component_info.banner_enabled` | boolean | 官方字段 `banner_enabled`；官方未单独提供业务说明。 |
| `aweme_detail.statistics` | object | 官方字段 `statistics`；官方未单独提供业务说明。 |
| `aweme_detail.statistics.aweme_id` | string | TikTok 视频标识。 |
| `aweme_detail.statistics.collect_count` | integer | 官方字段 `collect_count`；官方未单独提供业务说明。 |
| `aweme_detail.statistics.comment_count` | integer | 评论数量。 |
| `aweme_detail.statistics.digg_count` | integer | 点赞数量。 |
| `aweme_detail.statistics.download_count` | integer | 官方字段 `download_count`；官方未单独提供业务说明。 |
| `aweme_detail.statistics.forward_count` | integer | 官方字段 `forward_count`；官方未单独提供业务说明。 |
| `aweme_detail.statistics.lose_comment_count` | integer | 官方字段 `lose_comment_count`；官方未单独提供业务说明。 |
| `aweme_detail.statistics.lose_count` | integer | 官方字段 `lose_count`；官方未单独提供业务说明。 |
| `aweme_detail.statistics.play_count` | integer | 播放数量。 |
| `aweme_detail.statistics.repost_count` | integer | 转发数量。 |
| `aweme_detail.statistics.share_count` | integer | 分享数量。 |
| `aweme_detail.statistics.whatsapp_share_count` | integer | 官方字段 `whatsapp_share_count`；官方未单独提供业务说明。 |
| `aweme_detail.status` | object | 状态。 |
| `aweme_detail.status.allow_comment` | boolean | 官方字段 `allow_comment`；官方未单独提供业务说明。 |
| `aweme_detail.status.allow_share` | boolean | 官方字段 `allow_share`；官方未单独提供业务说明。 |
| `aweme_detail.status.aweme_id` | string | TikTok 视频标识。 |
| `aweme_detail.status.download_status` | integer | 官方字段 `download_status`；官方未单独提供业务说明。 |
| `aweme_detail.status.in_reviewing` | boolean | 官方字段 `in_reviewing`；官方未单独提供业务说明。 |
| `aweme_detail.status.is_delete` | boolean | 官方字段 `is_delete`；官方未单独提供业务说明。 |
| `aweme_detail.status.is_prohibited` | boolean | 官方字段 `is_prohibited`；官方未单独提供业务说明。 |
| `aweme_detail.status.private_status` | integer | 官方字段 `private_status`；官方未单独提供业务说明。 |
| `aweme_detail.status.review_result` | object | 官方字段 `review_result`；官方未单独提供业务说明。 |
| `aweme_detail.status.review_result.review_status` | integer | 官方字段 `review_status`；官方未单独提供业务说明。 |
| `aweme_detail.status.reviewed` | integer | 官方字段 `reviewed`；官方未单独提供业务说明。 |
| `aweme_detail.status.self_see` | boolean | 官方字段 `self_see`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words` | object | 官方字段 `suggest_words`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words` | array | 官方字段 `suggest_words`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words[].hint_text` | string | 官方字段 `hint_text`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words[].qrec_virtual_enable` | string | 官方字段 `qrec_virtual_enable`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words[].scene` | string | 官方字段 `scene`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words[].words` | array | 官方字段 `words`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words[].words[].penetrate_info` | string | 官方字段 `penetrate_info`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words[].words[].word` | string | 官方字段 `word`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words[].words[].word_id` | string | 官方字段 `word_id`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words[].words[].word_record` | object | 官方字段 `word_record`；官方未单独提供业务说明。 |
| `aweme_detail.suggest_words.suggest_words[].words[].word_record.words_lang` | string | 官方字段 `words_lang`；官方未单独提供业务说明。 |
| `aweme_detail.support_danmaku` | boolean | 官方字段 `support_danmaku`；官方未单独提供业务说明。 |
| `aweme_detail.text_extra` | array | 官方字段 `text_extra`；官方未单独提供业务说明。 |
| `aweme_detail.text_extra[].end` | integer | 官方字段 `end`；官方未单独提供业务说明。 |
| `aweme_detail.text_extra[].sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_detail.text_extra[].start` | integer | 官方字段 `start`；官方未单独提供业务说明。 |
| `aweme_detail.text_extra[].type` | integer | 类型。 |
| `aweme_detail.text_extra[].user_id` | string | 用户标识。 |
| `aweme_detail.text_sticker_major_lang` | string | 官方字段 `text_sticker_major_lang`；官方未单独提供业务说明。 |
| `aweme_detail.title_language` | string | 官方字段 `title_language`；官方未单独提供业务说明。 |
| `aweme_detail.ttec_suggest_words` | object | 官方字段 `ttec_suggest_words`；官方未单独提供业务说明。 |
| `aweme_detail.ttec_suggest_words.ttec_suggest_words` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.tts_voice_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.ttt_product_recall_type` | integer | 官方字段 `ttt_product_recall_type`；官方未单独提供业务说明。 |
| `aweme_detail.uniqid_position` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.upvote_info` | object | 官方字段 `upvote_info`；官方未单独提供业务说明。 |
| `aweme_detail.upvote_info.friends_recall_info` | string | 官方字段 `friends_recall_info`；官方未单独提供业务说明。 |
| `aweme_detail.upvote_info.repost_initiate_score` | integer | 官方字段 `repost_initiate_score`；官方未单独提供业务说明。 |
| `aweme_detail.upvote_info.user_upvoted` | boolean | 官方字段 `user_upvoted`；官方未单独提供业务说明。 |
| `aweme_detail.upvote_preload` | object | 官方字段 `upvote_preload`；官方未单独提供业务说明。 |
| `aweme_detail.upvote_preload.need_pull_upvote_info` | boolean | 官方字段 `need_pull_upvote_info`；官方未单独提供业务说明。 |
| `aweme_detail.used_full_song` | boolean | 官方字段 `used_full_song`；官方未单独提供业务说明。 |
| `aweme_detail.user_digged` | integer | 官方字段 `user_digged`；官方未单独提供业务说明。 |
| `aweme_detail.video` | object | 视频信息。 |
| `aweme_detail.video.CoverTsp` | number | 官方字段 `CoverTsp`；官方未单独提供业务说明。 |
| `aweme_detail.video.ai_dynamic_cover` | object | 官方字段 `ai_dynamic_cover`；官方未单独提供业务说明。 |
| `aweme_detail.video.ai_dynamic_cover.uri` | string | 资源标识。 |
| `aweme_detail.video.ai_dynamic_cover.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.ai_dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.ai_dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.ai_dynamic_cover_bak` | object | 官方字段 `ai_dynamic_cover_bak`；官方未单独提供业务说明。 |
| `aweme_detail.video.ai_dynamic_cover_bak.uri` | string | 资源标识。 |
| `aweme_detail.video.ai_dynamic_cover_bak.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.ai_dynamic_cover_bak.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.ai_dynamic_cover_bak.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.animated_cover` | object | 官方字段 `animated_cover`；官方未单独提供业务说明。 |
| `aweme_detail.video.animated_cover.uri` | string | 资源标识。 |
| `aweme_detail.video.animated_cover.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.animated_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.animated_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.big_thumbs` | array | 官方字段 `big_thumbs`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].duration` | number | 时长。 |
| `aweme_detail.video.big_thumbs[].fext` | string | 官方字段 `fext`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].img_num` | integer | 官方字段 `img_num`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].img_uris` | array | 官方字段 `img_uris`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].img_uris[]` | string | 官方数组 `img_uris` 的元素。 |
| `aweme_detail.video.big_thumbs[].img_url` | string | 官方字段 `img_url`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].img_urls` | array | 官方字段 `img_urls`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].img_urls[]` | string | 官方数组 `img_urls` 的元素。 |
| `aweme_detail.video.big_thumbs[].img_x_len` | integer | 官方字段 `img_x_len`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].img_x_size` | integer | 官方字段 `img_x_size`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].img_y_len` | integer | 官方字段 `img_y_len`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].img_y_size` | integer | 官方字段 `img_y_size`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].interval` | integer | 官方字段 `interval`；官方未单独提供业务说明。 |
| `aweme_detail.video.big_thumbs[].uri` | string | 资源标识。 |
| `aweme_detail.video.bit_rate` | array | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].HDR_bit` | string | 官方字段 `HDR_bit`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].HDR_type` | string | 官方字段 `HDR_type`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].bit_rate` | integer | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].dub_infos` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.bit_rate[].fps` | integer | 官方字段 `fps`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].gear_name` | string | 官方字段 `gear_name`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].play_addr.height` | integer | 高度。 |
| `aweme_detail.video.bit_rate[].play_addr.uri` | string | 资源标识。 |
| `aweme_detail.video.bit_rate[].play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].play_addr.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.bit_rate[].play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.bit_rate[].play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.bit_rate[].play_addr.width` | integer | 宽度。 |
| `aweme_detail.video.bit_rate[].quality_type` | integer | 官方字段 `quality_type`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate[].video_extra` | string | 官方字段 `video_extra`；官方未单独提供业务说明。 |
| `aweme_detail.video.bit_rate_audio` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.video.cdn_url_expired` | integer | 官方字段 `cdn_url_expired`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info` | object | 官方字段 `cla_info`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos` | array | 官方字段 `caption_infos`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].caption_format` | string | 官方字段 `caption_format`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].caption_length` | integer | 官方字段 `caption_length`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].cla_subtitle_id` | integer | 官方字段 `cla_subtitle_id`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].complaint_id` | integer | 官方字段 `complaint_id`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].expire` | integer | 官方字段 `expire`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].is_auto_generated` | boolean | 官方字段 `is_auto_generated`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].is_original_caption` | boolean | 官方字段 `is_original_caption`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].lang` | string | 官方字段 `lang`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].language_code` | string | 官方字段 `language_code`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].language_id` | integer | 官方字段 `language_id`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].source_tag` | string | 官方字段 `source_tag`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].sub_id` | integer | 官方字段 `sub_id`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].sub_version` | string | 官方字段 `sub_version`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].subtitle_type` | integer | 官方字段 `subtitle_type`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].translation_type` | integer | 官方字段 `translation_type`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].translator_id` | integer | 官方字段 `translator_id`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.caption_infos[].url` | string | 链接。 |
| `aweme_detail.video.cla_info.caption_infos[].url_list` | array | 资源链接列表。 |
| `aweme_detail.video.cla_info.caption_infos[].url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.cla_info.caption_infos[].variant` | string | 官方字段 `variant`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.captions_type` | integer | 官方字段 `captions_type`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.creator_edited_caption_id` | integer | 官方字段 `creator_edited_caption_id`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.enable_auto_caption` | integer | 官方字段 `enable_auto_caption`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.has_original_audio` | integer | 官方字段 `has_original_audio`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.hide_original_caption` | boolean | 官方字段 `hide_original_caption`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.no_caption_reason` | integer | 官方字段 `no_caption_reason`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.original_language_info` | object | 官方字段 `original_language_info`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.original_language_info.can_translate_realtime` | boolean | 官方字段 `can_translate_realtime`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.original_language_info.can_translate_realtime_skip_translation_lang_check` | boolean | 官方字段 `can_translate_realtime_skip_translation_lang_check`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.original_language_info.first_subtitle_time` | integer | 官方字段 `first_subtitle_time`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.original_language_info.is_burnin_caption` | boolean | 官方字段 `is_burnin_caption`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.original_language_info.lang` | string | 官方字段 `lang`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.original_language_info.language_code` | string | 官方字段 `language_code`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.original_language_info.language_id` | integer | 官方字段 `language_id`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.original_language_info.original_caption_type` | integer | 官方字段 `original_caption_type`；官方未单独提供业务说明。 |
| `aweme_detail.video.cla_info.vertical_positions` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.cover` | object | 官方字段 `cover`；官方未单独提供业务说明。 |
| `aweme_detail.video.cover.height` | integer | 高度。 |
| `aweme_detail.video.cover.uri` | string | 资源标识。 |
| `aweme_detail.video.cover.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.cover.width` | integer | 宽度。 |
| `aweme_detail.video.cover_is_custom` | boolean | 官方字段 `cover_is_custom`；官方未单独提供业务说明。 |
| `aweme_detail.video.download_addr` | object | 官方字段 `download_addr`；官方未单独提供业务说明。 |
| `aweme_detail.video.download_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_detail.video.download_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_detail.video.download_addr.height` | integer | 高度。 |
| `aweme_detail.video.download_addr.uri` | string | 资源标识。 |
| `aweme_detail.video.download_addr.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.download_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.download_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.download_addr.width` | integer | 宽度。 |
| `aweme_detail.video.download_no_watermark_addr` | object | 官方字段 `download_no_watermark_addr`；官方未单独提供业务说明。 |
| `aweme_detail.video.download_no_watermark_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_detail.video.download_no_watermark_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_detail.video.download_no_watermark_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_detail.video.download_no_watermark_addr.height` | integer | 高度。 |
| `aweme_detail.video.download_no_watermark_addr.uri` | string | 资源标识。 |
| `aweme_detail.video.download_no_watermark_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_detail.video.download_no_watermark_addr.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.download_no_watermark_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.download_no_watermark_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.download_no_watermark_addr.width` | integer | 宽度。 |
| `aweme_detail.video.duration` | integer | 时长。 |
| `aweme_detail.video.dynamic_cover` | object | 官方字段 `dynamic_cover`；官方未单独提供业务说明。 |
| `aweme_detail.video.dynamic_cover.height` | integer | 高度。 |
| `aweme_detail.video.dynamic_cover.uri` | string | 资源标识。 |
| `aweme_detail.video.dynamic_cover.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.dynamic_cover.width` | integer | 宽度。 |
| `aweme_detail.video.has_watermark` | boolean | 官方字段 `has_watermark`；官方未单独提供业务说明。 |
| `aweme_detail.video.height` | integer | 高度。 |
| `aweme_detail.video.is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `aweme_detail.video.is_callback` | boolean | 官方字段 `is_callback`；官方未单独提供业务说明。 |
| `aweme_detail.video.is_long_video` | integer | 官方字段 `is_long_video`；官方未单独提供业务说明。 |
| `aweme_detail.video.meta` | string | 官方字段 `meta`；官方未单独提供业务说明。 |
| `aweme_detail.video.misc_download_addrs` | string | 官方字段 `misc_download_addrs`；官方未单独提供业务说明。 |
| `aweme_detail.video.need_set_token` | boolean | 官方字段 `need_set_token`；官方未单独提供业务说明。 |
| `aweme_detail.video.origin_cover` | object | 官方字段 `origin_cover`；官方未单独提供业务说明。 |
| `aweme_detail.video.origin_cover.height` | integer | 高度。 |
| `aweme_detail.video.origin_cover.uri` | string | 资源标识。 |
| `aweme_detail.video.origin_cover.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.origin_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.origin_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.origin_cover.width` | integer | 宽度。 |
| `aweme_detail.video.play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr.height` | integer | 高度。 |
| `aweme_detail.video.play_addr.uri` | string | 资源标识。 |
| `aweme_detail.video.play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.play_addr.width` | integer | 宽度。 |
| `aweme_detail.video.play_addr_bytevc1` | object | 官方字段 `play_addr_bytevc1`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_bytevc1.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_bytevc1.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_bytevc1.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_bytevc1.height` | integer | 高度。 |
| `aweme_detail.video.play_addr_bytevc1.uri` | string | 资源标识。 |
| `aweme_detail.video.play_addr_bytevc1.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_bytevc1.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.play_addr_bytevc1.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.play_addr_bytevc1.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.play_addr_bytevc1.width` | integer | 宽度。 |
| `aweme_detail.video.play_addr_h264` | object | 官方字段 `play_addr_h264`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_h264.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_h264.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_h264.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_h264.height` | integer | 高度。 |
| `aweme_detail.video.play_addr_h264.uri` | string | 资源标识。 |
| `aweme_detail.video.play_addr_h264.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_detail.video.play_addr_h264.url_list` | array | 资源链接列表。 |
| `aweme_detail.video.play_addr_h264.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_detail.video.play_addr_h264.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.play_addr_h264.width` | integer | 宽度。 |
| `aweme_detail.video.ratio` | string | 官方字段 `ratio`；官方未单独提供业务说明。 |
| `aweme_detail.video.source_HDR_type` | integer | 官方字段 `source_HDR_type`；官方未单独提供业务说明。 |
| `aweme_detail.video.tags` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.video.video_model` | string | 官方字段 `video_model`；官方未单独提供业务说明。 |
| `aweme_detail.video.width` | integer | 宽度。 |
| `aweme_detail.video_control` | object | 官方字段 `video_control`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.allow_download` | boolean | 官方字段 `allow_download`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.allow_duet` | boolean | 官方字段 `allow_duet`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.allow_dynamic_wallpaper` | boolean | 官方字段 `allow_dynamic_wallpaper`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.allow_music` | boolean | 官方字段 `allow_music`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.allow_react` | boolean | 官方字段 `allow_react`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.allow_stitch` | boolean | 官方字段 `allow_stitch`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.draft_progress_bar` | integer | 官方字段 `draft_progress_bar`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.prevent_download_type` | integer | 官方字段 `prevent_download_type`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.share_type` | integer | 官方字段 `share_type`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.show_progress_bar` | integer | 官方字段 `show_progress_bar`；官方未单独提供业务说明。 |
| `aweme_detail.video_control.timer_status` | integer | 官方字段 `timer_status`；官方未单独提供业务说明。 |
| `aweme_detail.video_labels` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.video_text` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_detail.visual_search_info` | object | 官方示例为空对象，未提供子字段。 |
| `aweme_detail.voice_filter_ids` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_detail.with_promotional_music` | boolean | 官方字段 `with_promotional_music`；官方未单独提供业务说明。 |
| `aweme_detail.without_watermark` | boolean | 官方字段 `without_watermark`；官方未单独提供业务说明。 |
| `aweme_detail.is_eligible_for_commission` | boolean | 官方字段 `is_eligible_for_commission`；官方未单独提供业务说明。 |
| `aweme_detail.is_paid_partnership` | boolean | 是否为付费合作内容。 |
| `aweme_detail.create_time_utc` | string | 官方字段 `create_time_utc`；官方未单独提供业务说明。 |
| `aweme_detail.url` | string | 链接。 |
| `aweme_detail.shop_product_url` | string | 官方字段 `shop_product_url`；官方未单独提供业务说明。 |
| `extra` | object | 官方字段 `extra`；官方未单独提供业务说明。 |
| `extra.fatal_item_ids` | array | 官方示例为空数组，未提供元素结构。 |
| `extra.logid` | string | 官方字段 `logid`；官方未单独提供业务说明。 |
| `extra.now` | integer | 官方字段 `now`；官方未单独提供业务说明。 |
| `log_pb` | object | 官方字段 `log_pb`；官方未单独提供业务说明。 |
| `log_pb.impr_id` | string | 官方字段 `impr_id`；官方未单独提供业务说明。 |
| `status_code` | integer | 状态码。 |
| `status_msg` | string | 状态说明。 |
| `transcript` | string | 转写内容。 |
| `aweme_detail.video.bit_rate[].fid_profile_labels` | string | 官方字段 `fid_profile_labels`；官方未单独提供业务说明。 |
| `aweme_detail.video.did_profile_labels` | string | 官方字段 `did_profile_labels`；官方未单独提供业务说明。 |
| `aweme_detail.video.vid_profile_labels` | string | 官方字段 `vid_profile_labels`；官方未单独提供业务说明。 |
| `aweme_detail.is_ad` | boolean | 官方字段 `is_ad`；官方未单独提供业务说明。 |

## 使用要点

- 不要默认 download_media=true。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-video" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v2/tiktok/video/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

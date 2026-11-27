# Wenmai SCRAPECREATORS scrapecreators_tiktok_search_top API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-search-top`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_search_top`
- **脚本入口**：`modules/search-top/scripts/search_top.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `query` | string | 是 | 搜索关键词。 |
| `publish_time` | string | 否 | 发布时间筛选。可选值：yesterday、this-week、this-month、last-3-months、last-6-months、all-time。 |
| `sort_by` | string | 否 | 排序方式。可选值：relevance、most-liked、date-posted。 |
| `region` | string | 否 | 代理所在地区，两位国家码如 US。这不是硬性国家过滤，只是把代理放到该地区，用于抓取部分国家才能看到的内容。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |
| `cursor` | number | 否 | 分页游标，传入上一页响应中的 cursor。 |

## 请求示例

```json
{
  "query": "amazon finds",
  "trim": true
}
```

```bash
python3 modules/search-top/scripts/search_top.py '{"query": "amazon finds", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `items` | array | 结果条目。 |
| `items[].id` | string | 标识符。 |
| `items[].desc` | string | 描述。 |
| `items[].content_type` | string | 官方字段 `content_type`；官方未单独提供业务说明。 |
| `items[].create_time` | string | 创建时间。 |
| `items[].desc_language` | string | 官方字段 `desc_language`；官方未单独提供业务说明。 |
| `items[].region` | string | 地区。 |
| `items[].is_top` | integer | 官方字段 `is_top`；官方未单独提供业务说明。 |
| `items[].statistics` | object | 官方字段 `statistics`；官方未单独提供业务说明。 |
| `items[].statistics.aweme_id` | string | TikTok 视频标识。 |
| `items[].statistics.collect_count` | integer | 官方字段 `collect_count`；官方未单独提供业务说明。 |
| `items[].statistics.comment_count` | integer | 评论数量。 |
| `items[].statistics.digg_count` | integer | 点赞数量。 |
| `items[].statistics.download_count` | integer | 官方字段 `download_count`；官方未单独提供业务说明。 |
| `items[].statistics.forward_count` | integer | 官方字段 `forward_count`；官方未单独提供业务说明。 |
| `items[].statistics.lose_comment_count` | integer | 官方字段 `lose_comment_count`；官方未单独提供业务说明。 |
| `items[].statistics.lose_count` | integer | 官方字段 `lose_count`；官方未单独提供业务说明。 |
| `items[].statistics.play_count` | integer | 播放数量。 |
| `items[].statistics.repost_count` | integer | 转发数量。 |
| `items[].statistics.share_count` | integer | 分享数量。 |
| `items[].statistics.whatsapp_share_count` | integer | 官方字段 `whatsapp_share_count`；官方未单独提供业务说明。 |
| `items[].video` | object | 视频信息。 |
| `items[].video.ai_dynamic_cover` | object | 官方字段 `ai_dynamic_cover`；官方未单独提供业务说明。 |
| `items[].video.ai_dynamic_cover.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.ai_dynamic_cover.height` | integer | 高度。 |
| `items[].video.ai_dynamic_cover.uri` | string | 资源标识。 |
| `items[].video.ai_dynamic_cover.url_list` | array | 资源链接列表。 |
| `items[].video.ai_dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.ai_dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.ai_dynamic_cover.width` | integer | 宽度。 |
| `items[].video.ai_dynamic_cover_bak` | object | 官方字段 `ai_dynamic_cover_bak`；官方未单独提供业务说明。 |
| `items[].video.ai_dynamic_cover_bak.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.ai_dynamic_cover_bak.height` | integer | 高度。 |
| `items[].video.ai_dynamic_cover_bak.uri` | string | 资源标识。 |
| `items[].video.ai_dynamic_cover_bak.url_list` | array | 资源链接列表。 |
| `items[].video.ai_dynamic_cover_bak.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.ai_dynamic_cover_bak.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.ai_dynamic_cover_bak.width` | integer | 宽度。 |
| `items[].video.big_thumbs` | array | 官方字段 `big_thumbs`；官方未单独提供业务说明。 |
| `items[].video.bit_rate` | array | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `items[].video.bit_rate_audio` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].video.cdn_url_expired` | integer | 官方字段 `cdn_url_expired`；官方未单独提供业务说明。 |
| `items[].video.cla_info` | object | 官方字段 `cla_info`；官方未单独提供业务说明。 |
| `items[].video.cla_info.caption_infos` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.cla_info.captions_type` | integer | 官方字段 `captions_type`；官方未单独提供业务说明。 |
| `items[].video.cla_info.creator_edited_caption_id` | integer | 官方字段 `creator_edited_caption_id`；官方未单独提供业务说明。 |
| `items[].video.cla_info.enable_auto_caption` | integer | 官方字段 `enable_auto_caption`；官方未单独提供业务说明。 |
| `items[].video.cla_info.has_original_audio` | integer | 官方字段 `has_original_audio`；官方未单独提供业务说明。 |
| `items[].video.cla_info.hide_original_caption` | boolean | 官方字段 `hide_original_caption`；官方未单独提供业务说明。 |
| `items[].video.cla_info.is_author_dubbing_qualified` | boolean | 官方字段 `is_author_dubbing_qualified`；官方未单独提供业务说明。 |
| `items[].video.cla_info.no_caption_reason` | integer | 官方字段 `no_caption_reason`；官方未单独提供业务说明。 |
| `items[].video.cla_info.no_caption_reason_v2` | integer | 官方字段 `no_caption_reason_v2`；官方未单独提供业务说明。 |
| `items[].video.cla_info.vertical_positions` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.cover` | object | 官方字段 `cover`；官方未单独提供业务说明。 |
| `items[].video.cover.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.cover.height` | integer | 高度。 |
| `items[].video.cover.uri` | string | 资源标识。 |
| `items[].video.cover.url_list` | array | 资源链接列表。 |
| `items[].video.cover.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.cover.width` | integer | 宽度。 |
| `items[].video.download_addr` | object | 官方字段 `download_addr`；官方未单独提供业务说明。 |
| `items[].video.download_addr.height` | integer | 高度。 |
| `items[].video.download_addr.uri` | string | 资源标识。 |
| `items[].video.download_addr.url_list` | array | 资源链接列表。 |
| `items[].video.download_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.download_addr.width` | integer | 宽度。 |
| `items[].video.duration` | integer | 时长。 |
| `items[].video.dynamic_cover` | object | 官方字段 `dynamic_cover`；官方未单独提供业务说明。 |
| `items[].video.dynamic_cover.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.dynamic_cover.height` | integer | 高度。 |
| `items[].video.dynamic_cover.uri` | string | 资源标识。 |
| `items[].video.dynamic_cover.url_list` | array | 资源链接列表。 |
| `items[].video.dynamic_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.dynamic_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.dynamic_cover.width` | integer | 宽度。 |
| `items[].video.has_watermark` | boolean | 官方字段 `has_watermark`；官方未单独提供业务说明。 |
| `items[].video.height` | integer | 高度。 |
| `items[].video.is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `items[].video.is_callback` | boolean | 官方字段 `is_callback`；官方未单独提供业务说明。 |
| `items[].video.meta` | string | 官方字段 `meta`；官方未单独提供业务说明。 |
| `items[].video.need_set_token` | boolean | 官方字段 `need_set_token`；官方未单独提供业务说明。 |
| `items[].video.origin_cover` | object | 官方字段 `origin_cover`；官方未单独提供业务说明。 |
| `items[].video.origin_cover.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.origin_cover.height` | integer | 高度。 |
| `items[].video.origin_cover.uri` | string | 资源标识。 |
| `items[].video.origin_cover.url_list` | array | 资源链接列表。 |
| `items[].video.origin_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.origin_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.origin_cover.width` | integer | 宽度。 |
| `items[].video.play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `items[].video.play_addr.height` | integer | 高度。 |
| `items[].video.play_addr.uri` | string | 资源标识。 |
| `items[].video.play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `items[].video.play_addr.url_list` | array | 资源链接列表。 |
| `items[].video.play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.play_addr.width` | integer | 宽度。 |
| `items[].video.ratio` | string | 官方字段 `ratio`；官方未单独提供业务说明。 |
| `items[].video.tags` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.width` | integer | 宽度。 |
| `items[].author` | object | 作者信息。 |
| `items[].author.accept_private_policy` | boolean | 官方字段 `accept_private_policy`；官方未单独提供业务说明。 |
| `items[].author.account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.authority_status` | integer | 官方字段 `authority_status`；官方未单独提供业务说明。 |
| `items[].author.avatar_168x168` | object | 官方字段 `avatar_168x168`；官方未单独提供业务说明。 |
| `items[].author.avatar_168x168.height` | integer | 高度。 |
| `items[].author.avatar_168x168.uri` | string | 资源标识。 |
| `items[].author.avatar_168x168.url_list` | array | 资源链接列表。 |
| `items[].author.avatar_168x168.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].author.avatar_168x168.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.avatar_168x168.width` | integer | 宽度。 |
| `items[].author.avatar_300x300` | object | 官方字段 `avatar_300x300`；官方未单独提供业务说明。 |
| `items[].author.avatar_300x300.height` | integer | 高度。 |
| `items[].author.avatar_300x300.uri` | string | 资源标识。 |
| `items[].author.avatar_300x300.url_list` | array | 资源链接列表。 |
| `items[].author.avatar_300x300.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].author.avatar_300x300.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.avatar_300x300.width` | integer | 宽度。 |
| `items[].author.avatar_larger` | object | 官方字段 `avatar_larger`；官方未单独提供业务说明。 |
| `items[].author.avatar_larger.height` | integer | 高度。 |
| `items[].author.avatar_larger.uri` | string | 资源标识。 |
| `items[].author.avatar_larger.url_list` | array | 资源链接列表。 |
| `items[].author.avatar_larger.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].author.avatar_larger.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.avatar_larger.width` | integer | 宽度。 |
| `items[].author.avatar_medium` | object | 中等尺寸头像。 |
| `items[].author.avatar_medium.height` | integer | 高度。 |
| `items[].author.avatar_medium.uri` | string | 资源标识。 |
| `items[].author.avatar_medium.url_list` | array | 资源链接列表。 |
| `items[].author.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].author.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.avatar_medium.width` | integer | 宽度。 |
| `items[].author.avatar_thumb` | object | 缩略头像。 |
| `items[].author.avatar_thumb.height` | integer | 高度。 |
| `items[].author.avatar_thumb.uri` | string | 资源标识。 |
| `items[].author.avatar_thumb.url_list` | array | 资源链接列表。 |
| `items[].author.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].author.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.avatar_thumb.width` | integer | 宽度。 |
| `items[].author.avatar_uri` | string | 官方字段 `avatar_uri`；官方未单独提供业务说明。 |
| `items[].author.aweme_count` | integer | 官方字段 `aweme_count`；官方未单独提供业务说明。 |
| `items[].author.bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.can_message_follow_status_list` | array | 官方字段 `can_message_follow_status_list`；官方未单独提供业务说明。 |
| `items[].author.can_message_follow_status_list[]` | integer | 官方数组 `can_message_follow_status_list` 的元素。 |
| `items[].author.can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.comment_filter_status` | integer | 官方字段 `comment_filter_status`；官方未单独提供业务说明。 |
| `items[].author.comment_setting` | integer | 官方字段 `comment_setting`；官方未单独提供业务说明。 |
| `items[].author.commerce_user_level` | integer | 官方字段 `commerce_user_level`；官方未单独提供业务说明。 |
| `items[].author.cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.custom_verify` | string | 官方字段 `custom_verify`；官方未单独提供业务说明。 |
| `items[].author.cv_level` | string | 官方字段 `cv_level`；官方未单独提供业务说明。 |
| `items[].author.download_prompt_ts` | integer | 官方字段 `download_prompt_ts`；官方未单独提供业务说明。 |
| `items[].author.enabled_filter_all_comments` | boolean | 官方字段 `enabled_filter_all_comments`；官方未单独提供业务说明。 |
| `items[].author.enterprise_verify_reason` | string | 官方字段 `enterprise_verify_reason`；官方未单独提供业务说明。 |
| `items[].author.events` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.fake_data_info` | object | 官方示例为空对象，未提供子字段。 |
| `items[].author.fb_expire_time` | integer | 官方字段 `fb_expire_time`；官方未单独提供业务说明。 |
| `items[].author.follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `items[].author.follower_count` | integer | 粉丝数量。 |
| `items[].author.follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `items[].author.followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.following_count` | integer | 关注数量。 |
| `items[].author.friends_status` | integer | 官方字段 `friends_status`；官方未单独提供业务说明。 |
| `items[].author.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.hide_search` | boolean | 官方字段 `hide_search`；官方未单独提供业务说明。 |
| `items[].author.homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.ins_id` | string | 官方字段 `ins_id`；官方未单独提供业务说明。 |
| `items[].author.is_ad_fake` | boolean | 官方字段 `is_ad_fake`；官方未单独提供业务说明。 |
| `items[].author.is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `items[].author.is_discipline_member` | boolean | 官方字段 `is_discipline_member`；官方未单独提供业务说明。 |
| `items[].author.is_mute` | integer | 官方字段 `is_mute`；官方未单独提供业务说明。 |
| `items[].author.is_mute_lives` | integer | 官方字段 `is_mute_lives`；官方未单独提供业务说明。 |
| `items[].author.is_mute_non_story_post` | integer | 官方字段 `is_mute_non_story_post`；官方未单独提供业务说明。 |
| `items[].author.is_mute_story` | integer | 官方字段 `is_mute_story`；官方未单独提供业务说明。 |
| `items[].author.is_star` | boolean | 官方字段 `is_star`；官方未单独提供业务说明。 |
| `items[].author.item_list` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.live_agreement` | integer | 官方字段 `live_agreement`；官方未单独提供业务说明。 |
| `items[].author.live_commerce` | boolean | 官方字段 `live_commerce`；官方未单独提供业务说明。 |
| `items[].author.live_verify` | integer | 官方字段 `live_verify`；官方未单独提供业务说明。 |
| `items[].author.mention_status` | integer | 官方字段 `mention_status`；官方未单独提供业务说明。 |
| `items[].author.mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.name_field` | string | 官方字段 `name_field`；官方未单独提供业务说明。 |
| `items[].author.need_points` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.need_recommend` | integer | 官方字段 `need_recommend`；官方未单独提供业务说明。 |
| `items[].author.nickname` | string | 昵称。 |
| `items[].author.platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `items[].author.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.reply_with_video_flag` | integer | 官方字段 `reply_with_video_flag`；官方未单独提供业务说明。 |
| `items[].author.room_id` | integer | 官方字段 `room_id`；官方未单独提供业务说明。 |
| `items[].author.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.search_user_desc` | string | 官方字段 `search_user_desc`；官方未单独提供业务说明。 |
| `items[].author.search_user_name` | string | 官方字段 `search_user_name`；官方未单独提供业务说明。 |
| `items[].author.sec_uid` | string | TikTok 安全用户标识。 |
| `items[].author.secret` | integer | 官方字段 `secret`；官方未单独提供业务说明。 |
| `items[].author.shield_comment_notice` | integer | 官方字段 `shield_comment_notice`；官方未单独提供业务说明。 |
| `items[].author.shield_digg_notice` | integer | 官方字段 `shield_digg_notice`；官方未单独提供业务说明。 |
| `items[].author.shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.shield_follow_notice` | integer | 官方字段 `shield_follow_notice`；官方未单独提供业务说明。 |
| `items[].author.short_id` | string | 官方字段 `short_id`；官方未单独提供业务说明。 |
| `items[].author.show_image_bubble` | boolean | 官方字段 `show_image_bubble`；官方未单独提供业务说明。 |
| `items[].author.special_account` | object | 官方字段 `special_account`；官方未单独提供业务说明。 |
| `items[].author.special_account.special_account_list` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.special_lock` | integer | 官方字段 `special_lock`；官方未单独提供业务说明。 |
| `items[].author.status` | integer | 状态。 |
| `items[].author.stitch_setting` | integer | 官方字段 `stitch_setting`；官方未单独提供业务说明。 |
| `items[].author.story_status` | integer | 官方字段 `story_status`；官方未单独提供业务说明。 |
| `items[].author.total_favorited` | integer | 官方字段 `total_favorited`；官方未单独提供业务说明。 |
| `items[].author.type_label` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.uid` | string | 用户标识。 |
| `items[].author.unique_id` | string | 账号唯一名称。 |
| `items[].author.user_canceled` | boolean | 官方字段 `user_canceled`；官方未单独提供业务说明。 |
| `items[].author.user_mode` | integer | 官方字段 `user_mode`；官方未单独提供业务说明。 |
| `items[].author.user_now_pack_info` | object | 官方示例为空对象，未提供子字段。 |
| `items[].author.user_period` | integer | 官方字段 `user_period`；官方未单独提供业务说明。 |
| `items[].author.user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.user_rate` | integer | 官方字段 `user_rate`；官方未单独提供业务说明。 |
| `items[].author.user_spark_info` | object | 官方示例为空对象，未提供子字段。 |
| `items[].author.user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.verification_type` | integer | 官方字段 `verification_type`；官方未单独提供业务说明。 |
| `items[].author.verify_info` | string | 官方字段 `verify_info`；官方未单独提供业务说明。 |
| `items[].author.video_icon` | object | 官方字段 `video_icon`；官方未单独提供业务说明。 |
| `items[].author.video_icon.height` | integer | 高度。 |
| `items[].author.video_icon.uri` | string | 资源标识。 |
| `items[].author.video_icon.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].author.video_icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.video_icon.width` | integer | 宽度。 |
| `items[].author.white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `items[].author.with_commerce_entry` | boolean | 官方字段 `with_commerce_entry`；官方未单独提供业务说明。 |
| `items[].author.with_shop_entry` | boolean | 官方字段 `with_shop_entry`；官方未单独提供业务说明。 |
| `items[].images` | array | 图片列表。 |
| `items[].images[]` | string | 图片列表中的元素。 |
| `items[].music` | object | 官方字段 `music`；官方未单独提供业务说明。 |
| `items[].music.author` | string | 作者信息。 |
| `items[].music.duration` | integer | 时长。 |
| `items[].music.id` | integer | 标识符。 |
| `items[].music.title` | string | 标题。 |
| `items[].music.play_url` | string | 官方字段 `play_url`；官方未单独提供业务说明。 |
| `items[].music.matched_song` | object | 官方字段 `matched_song`；官方未单独提供业务说明。 |
| `items[].music.matched_song.author` | string | 作者信息。 |
| `items[].music.matched_song.id` | string | 标识符。 |
| `items[].music.matched_song.title` | string | 标题。 |
| `items[].is_eligible_for_commission` | boolean | 官方字段 `is_eligible_for_commission`；官方未单独提供业务说明。 |
| `items[].is_paid_partnership` | boolean | 是否为付费合作内容。 |
| `items[].is_ad` | boolean | 官方字段 `is_ad`；官方未单独提供业务说明。 |
| `items[].url` | string | 链接。 |
| `items[].shop_product_url` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.CoverTsp` | number | 官方字段 `CoverTsp`；官方未单独提供业务说明。 |
| `items[].video.animated_cover` | object | 官方字段 `animated_cover`；官方未单独提供业务说明。 |
| `items[].video.animated_cover.uri` | string | 资源标识。 |
| `items[].video.animated_cover.url_list` | array | 资源链接列表。 |
| `items[].video.animated_cover.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.animated_cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.big_thumbs[].duration` | number | 时长。 |
| `items[].video.big_thumbs[].fext` | string | 官方字段 `fext`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].img_num` | integer | 官方字段 `img_num`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].img_uris` | array | 官方字段 `img_uris`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].img_uris[]` | string | 官方数组 `img_uris` 的元素。 |
| `items[].video.big_thumbs[].img_url` | string | 官方字段 `img_url`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].img_urls` | array | 官方字段 `img_urls`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].img_urls[]` | string | 官方数组 `img_urls` 的元素。 |
| `items[].video.big_thumbs[].img_x_len` | integer | 官方字段 `img_x_len`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].img_x_size` | integer | 官方字段 `img_x_size`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].img_y_len` | integer | 官方字段 `img_y_len`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].img_y_size` | integer | 官方字段 `img_y_size`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].interval` | integer | 官方字段 `interval`；官方未单独提供业务说明。 |
| `items[].video.big_thumbs[].uri` | string | 资源标识。 |
| `items[].video.bit_rate[].HDR_bit` | string | 官方字段 `HDR_bit`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].HDR_type` | string | 官方字段 `HDR_type`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].bit_rate` | integer | 官方字段 `bit_rate`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].dub_infos` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.bit_rate[].fid_profile_labels` | string | 官方字段 `fid_profile_labels`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].fps` | integer | 官方字段 `fps`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].gear_name` | string | 官方字段 `gear_name`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].is_bytevc1` | integer | 官方字段 `is_bytevc1`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].play_addr.height` | integer | 高度。 |
| `items[].video.bit_rate[].play_addr.uri` | string | 资源标识。 |
| `items[].video.bit_rate[].play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].play_addr.url_list` | array | 资源链接列表。 |
| `items[].video.bit_rate[].play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.bit_rate[].play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.bit_rate[].play_addr.width` | integer | 宽度。 |
| `items[].video.bit_rate[].quality_type` | integer | 官方字段 `quality_type`；官方未单独提供业务说明。 |
| `items[].video.bit_rate[].video_extra` | string | 官方字段 `video_extra`；官方未单独提供业务说明。 |
| `items[].video.cover_is_custom` | boolean | 官方字段 `cover_is_custom`；官方未单独提供业务说明。 |
| `items[].video.did_profile_labels` | string | 官方字段 `did_profile_labels`；官方未单独提供业务说明。 |
| `items[].video.download_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.download_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `items[].video.download_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.download_no_watermark_addr` | object | 官方字段 `download_no_watermark_addr`；官方未单独提供业务说明。 |
| `items[].video.download_no_watermark_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.download_no_watermark_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `items[].video.download_no_watermark_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `items[].video.download_no_watermark_addr.height` | integer | 高度。 |
| `items[].video.download_no_watermark_addr.uri` | string | 资源标识。 |
| `items[].video.download_no_watermark_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `items[].video.download_no_watermark_addr.url_list` | array | 资源链接列表。 |
| `items[].video.download_no_watermark_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.download_no_watermark_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.download_no_watermark_addr.width` | integer | 宽度。 |
| `items[].video.is_long_video` | integer | 官方字段 `is_long_video`；官方未单独提供业务说明。 |
| `items[].video.play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.play_addr.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `items[].video.play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `items[].video.play_addr_bytevc1` | object | 官方字段 `play_addr_bytevc1`；官方未单独提供业务说明。 |
| `items[].video.play_addr_bytevc1.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.play_addr_bytevc1.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `items[].video.play_addr_bytevc1.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `items[].video.play_addr_bytevc1.height` | integer | 高度。 |
| `items[].video.play_addr_bytevc1.uri` | string | 资源标识。 |
| `items[].video.play_addr_bytevc1.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `items[].video.play_addr_bytevc1.url_list` | array | 资源链接列表。 |
| `items[].video.play_addr_bytevc1.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.play_addr_bytevc1.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.play_addr_bytevc1.width` | integer | 宽度。 |
| `items[].video.play_addr_h264` | object | 官方字段 `play_addr_h264`；官方未单独提供业务说明。 |
| `items[].video.play_addr_h264.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `items[].video.play_addr_h264.file_cs` | string | 官方字段 `file_cs`；官方未单独提供业务说明。 |
| `items[].video.play_addr_h264.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `items[].video.play_addr_h264.height` | integer | 高度。 |
| `items[].video.play_addr_h264.uri` | string | 资源标识。 |
| `items[].video.play_addr_h264.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `items[].video.play_addr_h264.url_list` | array | 资源链接列表。 |
| `items[].video.play_addr_h264.url_list[]` | string | 资源链接列表中的元素。 |
| `items[].video.play_addr_h264.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video.play_addr_h264.width` | integer | 宽度。 |
| `items[].video.source_HDR_type` | integer | 官方字段 `source_HDR_type`；官方未单独提供业务说明。 |
| `items[].video.vid_profile_labels` | string | 官方字段 `vid_profile_labels`；官方未单独提供业务说明。 |
| `items[].video.video_model` | string | 官方字段 `video_model`；官方未单独提供业务说明。 |
| `cursor` | integer | 分页游标。 |

## 使用要点

- 综合搜索视频和图文。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-search-top" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "amazon finds", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/search/top/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

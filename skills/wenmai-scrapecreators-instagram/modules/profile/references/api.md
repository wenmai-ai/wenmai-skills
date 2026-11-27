# Wenmai SCRAPECREATORS scrapecreators_instagram_profile API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-profile`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_instagram_profile`
- **脚本入口**：`modules/profile/scripts/profile.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `handle` | string | 是 | Instagram 用户名，不带 @。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |
| `cache_max_age` | string | 否 | 若缓存中有不晚于该时效的数据则直接返回，官方不计 credit。 可选值：1d、3d、7d、14d、30d。 |

## 请求示例

```json
{
  "handle": "gymshark"
}
```

```bash
python3 modules/profile/scripts/profile.py '{"handle": "gymshark"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `data` | object | 官方响应中的内层业务数据。 |
| `data.user` | object | 用户信息。 |
| `data.user.ai_agent_type` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.biography` | string | 官方字段 `biography`；官方未单独提供业务说明。 |
| `data.user.bio_links` | array | 官方字段 `bio_links`；官方未单独提供业务说明。 |
| `data.user.bio_links[].title` | string | 标题。 |
| `data.user.bio_links[].lynx_url` | string | 官方字段 `lynx_url`；官方未单独提供业务说明。 |
| `data.user.bio_links[].url` | string | 链接。 |
| `data.user.bio_links[].link_type` | string | 官方字段 `link_type`；官方未单独提供业务说明。 |
| `data.user.fb_profile_biolink` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.biography_with_entities` | object | 官方字段 `biography_with_entities`；官方未单独提供业务说明。 |
| `data.user.biography_with_entities.raw_text` | string | 官方字段 `raw_text`；官方未单独提供业务说明。 |
| `data.user.biography_with_entities.entities` | array | 官方示例为空数组，未提供元素结构。 |
| `data.user.blocked_by_viewer` | boolean | 官方字段 `blocked_by_viewer`；官方未单独提供业务说明。 |
| `data.user.restricted_by_viewer` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.country_block` | boolean | 官方字段 `country_block`；官方未单独提供业务说明。 |
| `data.user.eimu_id` | string | 官方字段 `eimu_id`；官方未单独提供业务说明。 |
| `data.user.external_url` | string | 官方字段 `external_url`；官方未单独提供业务说明。 |
| `data.user.external_url_linkshimmed` | string | 官方字段 `external_url_linkshimmed`；官方未单独提供业务说明。 |
| `data.user.edge_followed_by` | object | 官方字段 `edge_followed_by`；官方未单独提供业务说明。 |
| `data.user.edge_followed_by.count` | integer | 数量。 |
| `data.user.fbid` | string | 官方字段 `fbid`；官方未单独提供业务说明。 |
| `data.user.followed_by_viewer` | boolean | 官方字段 `followed_by_viewer`；官方未单独提供业务说明。 |
| `data.user.edge_follow` | object | 官方字段 `edge_follow`；官方未单独提供业务说明。 |
| `data.user.edge_follow.count` | integer | 数量。 |
| `data.user.follows_viewer` | boolean | 官方字段 `follows_viewer`；官方未单独提供业务说明。 |
| `data.user.full_name` | string | 完整名称。 |
| `data.user.group_metadata` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.has_ar_effects` | boolean | 官方字段 `has_ar_effects`；官方未单独提供业务说明。 |
| `data.user.has_clips` | boolean | 官方字段 `has_clips`；官方未单独提供业务说明。 |
| `data.user.has_guides` | boolean | 官方字段 `has_guides`；官方未单独提供业务说明。 |
| `data.user.has_channel` | boolean | 官方字段 `has_channel`；官方未单独提供业务说明。 |
| `data.user.has_blocked_viewer` | boolean | 官方字段 `has_blocked_viewer`；官方未单独提供业务说明。 |
| `data.user.highlight_reel_count` | integer | 官方字段 `highlight_reel_count`；官方未单独提供业务说明。 |
| `data.user.has_onboarded_to_text_post_app` | boolean | 官方字段 `has_onboarded_to_text_post_app`；官方未单独提供业务说明。 |
| `data.user.has_requested_viewer` | boolean | 官方字段 `has_requested_viewer`；官方未单独提供业务说明。 |
| `data.user.hide_like_and_view_counts` | boolean | 官方字段 `hide_like_and_view_counts`；官方未单独提供业务说明。 |
| `data.user.id` | string | 标识符。 |
| `data.user.is_business_account` | boolean | 官方字段 `is_business_account`；官方未单独提供业务说明。 |
| `data.user.is_professional_account` | boolean | 官方字段 `is_professional_account`；官方未单独提供业务说明。 |
| `data.user.is_supervision_enabled` | boolean | 官方字段 `is_supervision_enabled`；官方未单独提供业务说明。 |
| `data.user.is_guardian_of_viewer` | boolean | 官方字段 `is_guardian_of_viewer`；官方未单独提供业务说明。 |
| `data.user.is_supervised_by_viewer` | boolean | 官方字段 `is_supervised_by_viewer`；官方未单独提供业务说明。 |
| `data.user.is_supervised_user` | boolean | 官方字段 `is_supervised_user`；官方未单独提供业务说明。 |
| `data.user.is_embeds_disabled` | boolean | 官方字段 `is_embeds_disabled`；官方未单独提供业务说明。 |
| `data.user.is_joined_recently` | boolean | 官方字段 `is_joined_recently`；官方未单独提供业务说明。 |
| `data.user.guardian_id` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.business_address_json` | object\|string | 官方字段 `business_address_json`；官方未单独提供业务说明。 |
| `data.user.business_contact_method` | string | 官方字段 `business_contact_method`；官方未单独提供业务说明。 |
| `data.user.business_email` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.business_phone_number` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.business_category_name` | string | 官方字段 `business_category_name`；官方未单独提供业务说明。 |
| `data.user.overall_category_name` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.category_enum` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.category_name` | string | 官方字段 `category_name`；官方未单独提供业务说明。 |
| `data.user.is_private` | boolean | 是否为私密账号。 |
| `data.user.is_verified` | boolean | 是否认证。 |
| `data.user.is_verified_by_mv4b` | boolean | 官方字段 `is_verified_by_mv4b`；官方未单独提供业务说明。 |
| `data.user.is_regulated_c18` | boolean | 官方字段 `is_regulated_c18`；官方未单独提供业务说明。 |
| `data.user.edge_mutual_followed_by` | object | 官方字段 `edge_mutual_followed_by`；官方未单独提供业务说明。 |
| `data.user.edge_mutual_followed_by.count` | integer | 数量。 |
| `data.user.edge_mutual_followed_by.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.user.pinned_channels_list_count` | integer | 官方字段 `pinned_channels_list_count`；官方未单独提供业务说明。 |
| `data.user.profile_pic_url` | string | 头像链接。 |
| `data.user.profile_pic_url_hd` | string | 官方字段 `profile_pic_url_hd`；官方未单独提供业务说明。 |
| `data.user.requested_by_viewer` | boolean | 官方字段 `requested_by_viewer`；官方未单独提供业务说明。 |
| `data.user.should_show_category` | boolean | 官方字段 `should_show_category`；官方未单独提供业务说明。 |
| `data.user.should_show_public_contacts` | boolean | 官方字段 `should_show_public_contacts`；官方未单独提供业务说明。 |
| `data.user.show_account_transparency_details` | boolean | 官方字段 `show_account_transparency_details`；官方未单独提供业务说明。 |
| `data.user.show_text_post_app_badge` | boolean | 官方字段 `show_text_post_app_badge`；官方未单独提供业务说明。 |
| `data.user.remove_message_entrypoint` | boolean | 官方字段 `remove_message_entrypoint`；官方未单独提供业务说明。 |
| `data.user.transparency_label` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.transparency_product` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.username` | string | 用户名。 |
| `data.user.connected_fb_page` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.pronouns` | array | 官方示例为空数组，未提供元素结构。 |
| `data.user.edge_felix_video_timeline` | object | 官方字段 `edge_felix_video_timeline`；官方未单独提供业务说明。 |
| `data.user.edge_felix_video_timeline.count` | integer | 数量。 |
| `data.user.edge_felix_video_timeline.page_info` | object | 官方字段 `page_info`；官方未单独提供业务说明。 |
| `data.user.edge_felix_video_timeline.page_info.has_next_page` | boolean | 是否存在下一页。 |
| `data.user.edge_felix_video_timeline.page_info.end_cursor` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_felix_video_timeline.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.user.edge_owner_to_timeline_media` | object | 官方字段 `edge_owner_to_timeline_media`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.count` | integer | 数量。 |
| `data.user.edge_owner_to_timeline_media.page_info` | object | 官方字段 `page_info`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.page_info.has_next_page` | boolean | 是否存在下一页。 |
| `data.user.edge_owner_to_timeline_media.page_info.end_cursor` | string | 官方字段 `end_cursor`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges` | array | 关联数据条目。 |
| `data.user.edge_owner_to_timeline_media.edges[].node` | object | 关联数据节点。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.id` | string | 标识符。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.shortcode` | string | 官方字段 `shortcode`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.dimensions` | object | 官方字段 `dimensions`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.dimensions.height` | integer | 高度。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.dimensions.width` | integer | 宽度。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_media_to_tagged_user` | object | 官方字段 `edge_media_to_tagged_user`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_media_to_tagged_user.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.fact_check_overall_rating` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.fact_check_information` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.gating_info` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.sharing_friction_info` | object | 官方字段 `sharing_friction_info`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.sharing_friction_info.should_have_sharing_friction` | boolean | 官方字段 `should_have_sharing_friction`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.sharing_friction_info.bloks_app_url` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.media_overlay_info` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.media_preview` | string | 官方字段 `media_preview`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.owner` | object | 所属账号。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.owner.id` | string | 标识符。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.owner.username` | string | 用户名。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.is_video` | boolean | 官方字段 `is_video`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.has_upcoming_event` | boolean | 官方字段 `has_upcoming_event`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.accessibility_caption` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.has_audio` | boolean | 官方字段 `has_audio`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.tracking_token` | string | 官方字段 `tracking_token`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.video_url` | string | 官方字段 `video_url`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.video_view_count` | integer | 官方字段 `video_view_count`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_media_to_caption` | object | 官方字段 `edge_media_to_caption`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_media_to_caption.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_media_to_comment` | object | 官方字段 `edge_media_to_comment`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_media_to_comment.count` | integer | 数量。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.comments_disabled` | boolean | 官方字段 `comments_disabled`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.taken_at_timestamp` | integer | 官方字段 `taken_at_timestamp`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_liked_by` | object | 官方字段 `edge_liked_by`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_liked_by.count` | integer | 数量。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_media_preview_like` | object | 官方字段 `edge_media_preview_like`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.edge_media_preview_like.count` | integer | 数量。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.location` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.nft_asset_info` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.thumbnail_src` | string | 官方字段 `thumbnail_src`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.thumbnail_resources` | array | 官方字段 `thumbnail_resources`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.thumbnail_resources[].src` | string | 官方字段 `src`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.thumbnail_resources[].config_width` | integer | 官方字段 `config_width`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.thumbnail_resources[].config_height` | integer | 官方字段 `config_height`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.felix_profile_grid_crop` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.coauthor_producers` | array | 官方示例为空数组，未提供元素结构。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.viewer_can_reshare` | boolean | 官方字段 `viewer_can_reshare`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.like_and_view_counts_disabled` | boolean | 官方字段 `like_and_view_counts_disabled`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.product_type` | string | 官方字段 `product_type`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.clips_music_attribution_info` | object | 官方字段 `clips_music_attribution_info`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.clips_music_attribution_info.artist_name` | string | 官方字段 `artist_name`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.clips_music_attribution_info.song_name` | string | 官方字段 `song_name`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.clips_music_attribution_info.uses_original_audio` | boolean | 官方字段 `uses_original_audio`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.clips_music_attribution_info.should_mute_audio` | boolean | 官方字段 `should_mute_audio`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.clips_music_attribution_info.should_mute_audio_reason` | string | 官方字段 `should_mute_audio_reason`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.clips_music_attribution_info.audio_id` | string | 官方字段 `audio_id`；官方未单独提供业务说明。 |
| `data.user.edge_saved_media` | object | 官方字段 `edge_saved_media`；官方未单独提供业务说明。 |
| `data.user.edge_saved_media.count` | integer | 数量。 |
| `data.user.edge_saved_media.page_info` | object | 官方字段 `page_info`；官方未单独提供业务说明。 |
| `data.user.edge_saved_media.page_info.has_next_page` | boolean | 是否存在下一页。 |
| `data.user.edge_saved_media.page_info.end_cursor` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_saved_media.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.user.edge_media_collections` | object | 官方字段 `edge_media_collections`；官方未单独提供业务说明。 |
| `data.user.edge_media_collections.count` | integer | 数量。 |
| `data.user.edge_media_collections.page_info` | object | 官方字段 `page_info`；官方未单独提供业务说明。 |
| `data.user.edge_media_collections.page_info.has_next_page` | boolean | 是否存在下一页。 |
| `data.user.edge_media_collections.page_info.end_cursor` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_media_collections.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.user.edge_related_profiles` | object | 官方字段 `edge_related_profiles`；官方未单独提供业务说明。 |
| `data.user.edge_related_profiles.edges` | array | 关联数据条目。 |
| `data.user.edge_related_profiles.edges[].node` | object | 关联数据节点。 |
| `data.user.edge_related_profiles.edges[].node.id` | string | 标识符。 |
| `data.user.edge_related_profiles.edges[].node.full_name` | string | 完整名称。 |
| `data.user.edge_related_profiles.edges[].node.is_private` | boolean | 是否为私密账号。 |
| `data.user.edge_related_profiles.edges[].node.is_verified` | boolean | 是否认证。 |
| `data.user.edge_related_profiles.edges[].node.profile_pic_url` | string | 头像链接。 |
| `data.user.edge_related_profiles.edges[].node.username` | string | 用户名。 |
| `status` | string | 状态。 |
| `data.user.business_address_json.city_name` | string | 官方字段 `city_name`；官方未单独提供业务说明。 |
| `data.user.business_address_json.city_id` | integer | 官方字段 `city_id`；官方未单独提供业务说明。 |
| `data.user.business_address_json.latitude` | number | 官方字段 `latitude`；官方未单独提供业务说明。 |
| `data.user.business_address_json.longitude` | number | 官方字段 `longitude`；官方未单独提供业务说明。 |
| `data.user.business_address_json.street_address` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.business_address_json.zip_code` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.dash_info` | object | 官方字段 `dash_info`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.dash_info.is_dash_eligible` | boolean | 官方字段 `is_dash_eligible`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.dash_info.video_dash_manifest` | string | 官方字段 `video_dash_manifest`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.dash_info.number_of_qualities` | integer | 官方字段 `number_of_qualities`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.thumbnail_tall_src` | string | 官方字段 `thumbnail_tall_src`；官方未单独提供业务说明。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.tall_profile_grid_crop` | null | 官方示例为 null，未说明非空类型。 |
| `data.user.edge_owner_to_timeline_media.edges[].node.profile_grid_thumbnail_fitting_style` | string | 官方字段 `profile_grid_thumbnail_fitting_style`；官方未单独提供业务说明。 |

## 使用要点

- handle 不带 @。直连曾出现 SSL 中断，失败时保留 requestId，不要改打贵参数重试。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-profile" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "gymshark"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/instagram/profile/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

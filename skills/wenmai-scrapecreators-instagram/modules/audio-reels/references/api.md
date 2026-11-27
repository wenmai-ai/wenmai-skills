# Wenmai SCRAPECREATORS scrapecreators_instagram_audio_reels API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-audio-reels`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_instagram_audio_reels`
- **脚本入口**：`modules/audio-reels/scripts/audio_reels.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `audio_id` | string | 是 | Instagram 音频页 URL 上的 audio id。 |
| `cursor` | string | 否 | 上一页响应返回的 Instagram 分页游标。 |

## 请求示例

```json
{
  "audio_id": "1392969992841787"
}
```

```bash
python3 modules/audio-reels/scripts/audio_reels.py '{"audio_id": "1392969992841787"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `reels` | array | 官方字段 `reels`；官方未单独提供业务说明。 |
| `reels[].gen_ai_chat_with_ai_cta_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].collaborator_edit_eligibility` | boolean | 官方字段 `collaborator_edit_eligibility`；官方未单独提供业务说明。 |
| `reels[].number_of_qualities` | integer | 官方字段 `number_of_qualities`；官方未单独提供业务说明。 |
| `reels[].related_ads_pivots_media_info` | string | 官方字段 `related_ads_pivots_media_info`；官方未单独提供业务说明。 |
| `reels[].is_artist_pick` | boolean | 官方字段 `is_artist_pick`；官方未单独提供业务说明。 |
| `reels[].translated_langs_for_autodub` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].subtype_name_for_REST__` | string | 官方字段 `subtype_name_for_REST__`；官方未单独提供业务说明。 |
| `reels[].is_eligible_for_poe` | boolean | 官方字段 `is_eligible_for_poe`；官方未单独提供业务说明。 |
| `reels[].original_lang_for_translations` | string | 官方字段 `original_lang_for_translations`；官方未单独提供业务说明。 |
| `reels[].eligible_insights_entrypoints` | string | 官方字段 `eligible_insights_entrypoints`；官方未单独提供业务说明。 |
| `reels[].igbio_product` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].hidden_likes_string_variant` | integer | 官方字段 `hidden_likes_string_variant`；官方未单独提供业务说明。 |
| `reels[].is_social_ufi_disabled` | boolean | 官方字段 `is_social_ufi_disabled`；官方未单独提供业务说明。 |
| `reels[].boost_unavailable_reason` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].boost_unavailable_identifier` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].boost_unavailable_reason_v2` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].client_cache_key` | string | 官方字段 `client_cache_key`；官方未单独提供业务说明。 |
| `reels[].can_reply` | boolean | 官方字段 `can_reply`；官方未单独提供业务说明。 |
| `reels[].photo_of_you` | boolean | 官方字段 `photo_of_you`；官方未单独提供业务说明。 |
| `reels[].media_attributions_data` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].can_view_more_preview_comments` | boolean | 官方字段 `can_view_more_preview_comments`；官方未单独提供业务说明。 |
| `reels[].mezql_token` | string | 官方字段 `mezql_token`；官方未单独提供业务说明。 |
| `reels[].has_tagged_users` | boolean | 官方字段 `has_tagged_users`；官方未单独提供业务说明。 |
| `reels[].is_eligible_content_for_post_roll_ad` | boolean | 官方字段 `is_eligible_content_for_post_roll_ad`；官方未单独提供业务说明。 |
| `reels[].is_cutout_sticker_allowed` | boolean | 官方字段 `is_cutout_sticker_allowed`；官方未单独提供业务说明。 |
| `reels[].is_photo_comments_composer_enabled_for_author` | boolean | 官方字段 `is_photo_comments_composer_enabled_for_author`；官方未单独提供业务说明。 |
| `reels[].hide_view_all_comment_entrypoint` | boolean | 官方字段 `hide_view_all_comment_entrypoint`；官方未单独提供业务说明。 |
| `reels[].has_liked` | boolean | 官方字段 `has_liked`；官方未单独提供业务说明。 |
| `reels[].is_organic_product_tagging_eligible` | boolean | 官方字段 `is_organic_product_tagging_eligible`；官方未单独提供业务说明。 |
| `reels[].view_state_item_type` | integer | 官方字段 `view_state_item_type`；官方未单独提供业务说明。 |
| `reels[].video_sticker_locales` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].is_paid_partnership` | boolean | 是否为付费合作内容。 |
| `reels[].is_in_profile_grid` | boolean | 官方字段 `is_in_profile_grid`；官方未单独提供业务说明。 |
| `reels[].is_tagged_media_shared_to_viewer_profile_grid` | boolean | 官方字段 `is_tagged_media_shared_to_viewer_profile_grid`；官方未单独提供业务说明。 |
| `reels[].should_show_author_pog_for_tagged_media_shared_to_profile_grid` | boolean | 官方字段 `should_show_author_pog_for_tagged_media_shared_to_profile_grid`；官方未单独提供业务说明。 |
| `reels[].inventory_source` | string | 官方字段 `inventory_source`；官方未单独提供业务说明。 |
| `reels[].integrity_review_decision` | string | 官方字段 `integrity_review_decision`；官方未单独提供业务说明。 |
| `reels[].has_delayed_metadata` | boolean | 官方字段 `has_delayed_metadata`；官方未单独提供业务说明。 |
| `reels[].filter_type` | integer | 官方字段 `filter_type`；官方未单独提供业务说明。 |
| `reels[].deleted_reason` | integer | 官方字段 `deleted_reason`；官方未单独提供业务说明。 |
| `reels[].device_timestamp` | integer | 官方字段 `device_timestamp`；官方未单独提供业务说明。 |
| `reels[].is_reshare_of_text_post_app_media_in_ig` | boolean | 官方字段 `is_reshare_of_text_post_app_media_in_ig`；官方未单独提供业务说明。 |
| `reels[].timeline_pinned_user_ids` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].is_open_to_public_submission` | boolean | 官方字段 `is_open_to_public_submission`；官方未单独提供业务说明。 |
| `reels[].profile_grid_control_enabled` | boolean | 官方字段 `profile_grid_control_enabled`；官方未单独提供业务说明。 |
| `reels[].can_see_insights_as_brand` | boolean | 官方字段 `can_see_insights_as_brand`；官方未单独提供业务说明。 |
| `reels[].media_reposter_bottomsheet_enabled` | boolean | 官方字段 `media_reposter_bottomsheet_enabled`；官方未单独提供业务说明。 |
| `reels[].coauthor_producer_can_see_organic_insights` | boolean | 官方字段 `coauthor_producer_can_see_organic_insights`；官方未单独提供业务说明。 |
| `reels[].share_count_disabled` | boolean | 官方字段 `share_count_disabled`；官方未单独提供业务说明。 |
| `reels[].is_visual_reply_commenter_notice_enabled` | boolean | 官方字段 `is_visual_reply_commenter_notice_enabled`；官方未单独提供业务说明。 |
| `reels[].should_request_ads` | boolean | 官方字段 `should_request_ads`；官方未单独提供业务说明。 |
| `reels[].subscribe_cta_visible` | boolean | 官方字段 `subscribe_cta_visible`；官方未单独提供业务说明。 |
| `reels[].sharing_friction_info` | object | 官方字段 `sharing_friction_info`；官方未单独提供业务说明。 |
| `reels[].sharing_friction_info.bloks_app_url` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].sharing_friction_info.sharing_friction_payload` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].sharing_friction_info.should_have_sharing_friction` | boolean | 官方字段 `should_have_sharing_friction`；官方未单独提供业务说明。 |
| `reels[].media_overlay_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].fb_user_tags` | object | 官方字段 `fb_user_tags`；官方未单独提供业务说明。 |
| `reels[].fb_user_tags.in` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].coauthor_producers` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].cutout_sticker_info` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].invited_coauthor_producers` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].gen_ai_detection_method` | object | 官方字段 `gen_ai_detection_method`；官方未单独提供业务说明。 |
| `reels[].gen_ai_detection_method.detection_method` | string | 官方字段 `detection_method`；官方未单独提供业务说明。 |
| `reels[].comment_inform_treatment` | object | 官方字段 `comment_inform_treatment`；官方未单独提供业务说明。 |
| `reels[].comment_inform_treatment.should_have_inform_treatment` | boolean | 官方字段 `should_have_inform_treatment`；官方未单独提供业务说明。 |
| `reels[].comment_inform_treatment.text` | string | 文本内容。 |
| `reels[].comment_inform_treatment.action_type` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].comment_inform_treatment.url` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].creative_config` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].caption` | object | 说明文字。 |
| `reels[].caption.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `reels[].caption.pk` | string | 主键标识。 |
| `reels[].caption.bit_flags` | integer | 官方字段 `bit_flags`；官方未单独提供业务说明。 |
| `reels[].caption.content_type` | string | 官方字段 `content_type`；官方未单独提供业务说明。 |
| `reels[].caption.created_at` | integer | 创建时间。 |
| `reels[].caption.created_at_utc` | integer | 官方字段 `created_at_utc`；官方未单独提供业务说明。 |
| `reels[].caption.did_report_as_spam` | boolean | 官方字段 `did_report_as_spam`；官方未单独提供业务说明。 |
| `reels[].caption.is_covered` | boolean | 官方字段 `is_covered`；官方未单独提供业务说明。 |
| `reels[].caption.is_ranked_comment` | boolean | 官方字段 `is_ranked_comment`；官方未单独提供业务说明。 |
| `reels[].caption.media_id` | string | 官方字段 `media_id`；官方未单独提供业务说明。 |
| `reels[].caption.private_reply_status` | integer | 官方字段 `private_reply_status`；官方未单独提供业务说明。 |
| `reels[].caption.share_enabled` | boolean | 官方字段 `share_enabled`；官方未单独提供业务说明。 |
| `reels[].caption.status` | string | 状态。 |
| `reels[].caption.text` | string | 文本内容。 |
| `reels[].caption.type` | integer | 类型。 |
| `reels[].caption.user` | object | 用户信息。 |
| `reels[].caption.user.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `reels[].caption.user.id` | string | 标识符。 |
| `reels[].caption.user.pk` | integer | 主键标识。 |
| `reels[].caption.user.pk_id` | string | 主键标识。 |
| `reels[].caption.user.username` | string | 用户名。 |
| `reels[].caption.user.full_name` | string | 完整名称。 |
| `reels[].caption.user.is_private` | boolean | 是否为私密账号。 |
| `reels[].caption.user.is_verified` | boolean | 是否认证。 |
| `reels[].caption.user.profile_pic_id` | string | 头像标识。 |
| `reels[].caption.user.profile_pic_url` | string | 头像链接。 |
| `reels[].caption.user.fbid_v2` | string | 官方字段 `fbid_v2`；官方未单独提供业务说明。 |
| `reels[].caption.user.is_unpublished` | boolean | 官方字段 `is_unpublished`；官方未单独提供业务说明。 |
| `reels[].caption.user_id` | integer | 用户标识。 |
| `reels[].music_metadata` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].meta_ai_suggested_prompts` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].user` | object | 用户信息。 |
| `reels[].user.is_embeds_disabled` | boolean | 官方字段 `is_embeds_disabled`；官方未单独提供业务说明。 |
| `reels[].user.id` | string | 标识符。 |
| `reels[].user.pk` | integer | 主键标识。 |
| `reels[].user.pk_id` | string | 主键标识。 |
| `reels[].user.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `reels[].user.fbid_v2` | string | 官方字段 `fbid_v2`；官方未单独提供业务说明。 |
| `reels[].user.profile_pic_id` | string | 头像标识。 |
| `reels[].user.profile_pic_url` | string | 头像链接。 |
| `reels[].user.eligible_for_text_app_activation_badge` | boolean | 官方字段 `eligible_for_text_app_activation_badge`；官方未单独提供业务说明。 |
| `reels[].user.interop_messaging_user_fbid` | string | 官方字段 `interop_messaging_user_fbid`；官方未单独提供业务说明。 |
| `reels[].user.username` | string | 用户名。 |
| `reels[].user.full_name` | string | 完整名称。 |
| `reels[].user.is_private` | boolean | 是否为私密账号。 |
| `reels[].user.is_unpublished` | boolean | 官方字段 `is_unpublished`；官方未单独提供业务说明。 |
| `reels[].user.is_verified` | boolean | 是否认证。 |
| `reels[].user.show_account_transparency_details` | boolean | 官方字段 `show_account_transparency_details`；官方未单独提供业务说明。 |
| `reels[].user.transparency_product_enabled` | boolean | 官方字段 `transparency_product_enabled`；官方未单独提供业务说明。 |
| `reels[].user.third_party_downloads_enabled` | integer | 官方字段 `third_party_downloads_enabled`；官方未单独提供业务说明。 |
| `reels[].user.feed_post_reshare_disabled` | boolean | 官方字段 `feed_post_reshare_disabled`；官方未单独提供业务说明。 |
| `reels[].user.account_badges` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].user.account_type` | integer | 官方字段 `account_type`；官方未单独提供业务说明。 |
| `reels[].user.has_anonymous_profile_picture` | boolean | 官方字段 `has_anonymous_profile_picture`；官方未单独提供业务说明。 |
| `reels[].user.fan_club_info` | object | 官方字段 `fan_club_info`；官方未单独提供业务说明。 |
| `reels[].user.fan_club_info.autosave_to_exclusive_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.connected_member_count` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.fan_club_id` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.fan_club_name` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.fan_consideration_page_revamp_eligiblity` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.has_enough_subscribers_for_ssc` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.is_fan_club_gifting_eligible` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.is_fan_club_referral_eligible` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.subscriber_count` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.has_created_ssc` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.is_free_trial_eligible` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.largest_public_bc_id` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].user.fan_club_info.should_show_playlists_in_profile_tab` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata` | object | 官方字段 `clips_metadata`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.achievements_info` | object | 官方字段 `achievements_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.achievements_info.num_earned_achievements` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.achievements_info.show_achievements` | boolean | 官方字段 `show_achievements`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.additional_audio_info` | object | 官方字段 `additional_audio_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.additional_audio_info.additional_audio_username` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.additional_audio_info.audio_reattribution_info` | object | 官方字段 `audio_reattribution_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.additional_audio_info.audio_reattribution_info.should_allow_restore` | boolean | 官方字段 `should_allow_restore`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.asset_recommendation_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.audio_ranking_info` | object | 官方字段 `audio_ranking_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.audio_ranking_info.best_audio_cluster_id` | string | 官方字段 `best_audio_cluster_id`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.audio_type` | string | 官方字段 `audio_type`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.branded_content_tag_info` | object | 官方字段 `branded_content_tag_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.branded_content_tag_info.can_add_tag` | boolean | 官方字段 `can_add_tag`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.clips_creation_entry_point` | string | 官方字段 `clips_creation_entry_point`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.content_appreciation_info` | object | 官方字段 `content_appreciation_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.content_appreciation_info.enabled` | boolean | 官方字段 `enabled`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.content_appreciation_info.entry_point_container` | object | 官方字段 `entry_point_container`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.content_appreciation_info.entry_point_container.comment` | object | 评论内容。 |
| `reels[].clips_metadata.content_appreciation_info.entry_point_container.comment.action_type` | string | 官方字段 `action_type`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.content_appreciation_info.entry_point_container.overflow` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.content_appreciation_info.entry_point_container.pill` | object | 官方字段 `pill`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.content_appreciation_info.entry_point_container.pill.action_type` | string | 官方字段 `action_type`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.content_appreciation_info.entry_point_container.pill.priority` | integer | 官方字段 `priority`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.contextual_highlight_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.cutout_sticker_info` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].clips_metadata.disable_use_in_clips_client_cache` | boolean | 官方字段 `disable_use_in_clips_client_cache`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.featured_label` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.is_fan_club_promo_video` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.is_public_chat_welcome_video` | boolean | 官方字段 `is_public_chat_welcome_video`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.is_shared_to_fb` | boolean | 官方字段 `is_shared_to_fb`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info` | object | 官方字段 `mashup_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.can_toggle_mashups_allowed` | boolean | 官方字段 `can_toggle_mashups_allowed`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.formatted_mashups_count` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.mashup_info.has_been_mashed_up` | boolean | 官方字段 `has_been_mashed_up`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.has_nonmimicable_additional_audio` | boolean | 官方字段 `has_nonmimicable_additional_audio`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.is_creator_requesting_mashup` | boolean | 官方字段 `is_creator_requesting_mashup`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.is_light_weight_check` | boolean | 官方字段 `is_light_weight_check`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.is_pivot_page_available` | boolean | 官方字段 `is_pivot_page_available`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.is_light_weight_reuse_allowed_check` | boolean | 官方字段 `is_light_weight_reuse_allowed_check`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.is_reuse_allowed` | boolean | 官方字段 `is_reuse_allowed`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.mashup_type` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.mashup_info.mashups_allowed` | boolean | 官方字段 `mashups_allowed`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.non_privacy_filtered_mashups_media_count` | integer | 官方字段 `non_privacy_filtered_mashups_media_count`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.mashup_info.original_media` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.mashup_info.privacy_filtered_mashups_media_count` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_canonical_id` | string | 官方字段 `music_canonical_id`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info` | object | 官方字段 `music_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info` | object | 官方字段 `music_asset_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.allows_saving` | boolean | 官方字段 `allows_saving`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.artist_id` | string | 官方字段 `artist_id`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.audio_asset_id` | string | 官方字段 `audio_asset_id`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.audio_cluster_id` | string | 官方字段 `audio_cluster_id`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.cover_artwork_thumbnail_uri` | string | 官方字段 `cover_artwork_thumbnail_uri`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.cover_artwork_uri` | string | 官方字段 `cover_artwork_uri`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.dark_message` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_asset_info.dash_manifest` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_asset_info.display_artist` | string | 官方字段 `display_artist`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.duration_in_ms` | integer | 官方字段 `duration_in_ms`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.fast_start_progressive_download_url` | string | 官方字段 `fast_start_progressive_download_url`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.has_lyrics` | boolean | 官方字段 `has_lyrics`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.highlight_start_times_in_ms` | array | 官方字段 `highlight_start_times_in_ms`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.highlight_start_times_in_ms[]` | integer | 官方数组 `highlight_start_times_in_ms` 的元素。 |
| `reels[].clips_metadata.music_info.music_asset_info.id` | string | 标识符。 |
| `reels[].clips_metadata.music_info.music_asset_info.ig_username` | string | 官方字段 `ig_username`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.is_eligible_for_audio_effects` | boolean | 官方字段 `is_eligible_for_audio_effects`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.is_explicit` | boolean | 官方字段 `is_explicit`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.progressive_download_url` | string | 官方字段 `progressive_download_url`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.reactive_audio_download_url` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_asset_info.sanitized_title` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_asset_info.subtitle` | string | 官方字段 `subtitle`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.title` | string | 标题。 |
| `reels[].clips_metadata.music_info.music_asset_info.spotify_track_metadata` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_asset_info.lyrics` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_asset_info.song_monetization_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_asset_info.licensed_music_subtype` | string | 官方字段 `licensed_music_subtype`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.is_eligible_for_vinyl_sticker` | boolean | 官方字段 `is_eligible_for_vinyl_sticker`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_asset_info.web_30s_preview_download_url` | string | 官方字段 `web_30s_preview_download_url`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info` | object | 官方字段 `music_consumption_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.allow_media_creation_with_music` | boolean | 官方字段 `allow_media_creation_with_music`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.audio_asset_start_time_in_ms` | integer | 官方字段 `audio_asset_start_time_in_ms`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.derived_content_start_time_in_composition_in_ms` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_consumption_info.display_labels` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_consumption_info.audio_filter_infos` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].clips_metadata.music_info.music_consumption_info.audio_muting_info` | object | 官方字段 `audio_muting_info`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.audio_muting_info.allow_audio_editing` | boolean | 官方字段 `allow_audio_editing`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.audio_muting_info.mute_audio` | boolean | 官方字段 `mute_audio`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.audio_muting_info.mute_reason_str` | string | 官方字段 `mute_reason_str`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.audio_muting_info.show_muted_audio_toast` | boolean | 官方字段 `show_muted_audio_toast`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.contains_lyrics` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_consumption_info.derived_content_id` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist` | object | 官方字段 `ig_artist`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.id` | string | 标识符。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.full_name` | string | 完整名称。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.is_private` | boolean | 是否为私密账号。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.is_verified` | boolean | 是否认证。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.pk` | integer | 主键标识。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.pk_id` | string | 主键标识。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.profile_pic_id` | string | 头像标识。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.profile_pic_url` | string | 头像链接。 |
| `reels[].clips_metadata.music_info.music_consumption_info.ig_artist.username` | string | 用户名。 |
| `reels[].clips_metadata.music_info.music_consumption_info.is_bookmarked` | boolean | 官方字段 `is_bookmarked`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.is_trending_in_clips` | boolean | 官方字段 `is_trending_in_clips`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.overlap_duration_in_ms` | integer | 官方字段 `overlap_duration_in_ms`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.placeholder_profile_pic_url` | string | 官方字段 `placeholder_profile_pic_url`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.should_allow_music_editing` | boolean | 官方字段 `should_allow_music_editing`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.should_mute_audio` | boolean | 官方字段 `should_mute_audio`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.should_mute_audio_reason` | string | 官方字段 `should_mute_audio_reason`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.should_render_soundwave` | boolean | 官方字段 `should_render_soundwave`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.music_info.music_consumption_info.trend_rank` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.music_info.music_consumption_info.previous_trend_rank` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.nux_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.original_sound_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.originality_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.professional_clips_upsell_type` | integer | 官方字段 `professional_clips_upsell_type`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.show_achievements` | boolean | 官方字段 `show_achievements`；官方未单独提供业务说明。 |
| `reels[].clips_metadata.reels_on_the_rise_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.reusable_text_attribute_string` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.reusable_text_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.shopping_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.template_info` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].clips_metadata.viewer_interaction_settings` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].id` | string | 标识符。 |
| `reels[].strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `reels[].pk` | string | 主键标识。 |
| `reels[].fbid` | string | 官方字段 `fbid`；官方未单独提供业务说明。 |
| `reels[].media_type` | integer | 官方字段 `media_type`；官方未单独提供业务说明。 |
| `reels[].like_and_view_counts_disabled` | boolean | 官方字段 `like_and_view_counts_disabled`；官方未单独提供业务说明。 |
| `reels[].code` | string | 官方业务编码。 |
| `reels[].taken_at` | integer | 官方字段 `taken_at`；官方未单独提供业务说明。 |
| `reels[].product_type` | string | 官方字段 `product_type`；官方未单独提供业务说明。 |
| `reels[].caption_is_edited` | boolean | 官方字段 `caption_is_edited`；官方未单独提供业务说明。 |
| `reels[].can_viewer_reshare` | boolean | 官方字段 `can_viewer_reshare`；官方未单独提供业务说明。 |
| `reels[].can_viewer_save` | boolean | 官方字段 `can_viewer_save`；官方未单独提供业务说明。 |
| `reels[].comment_count` | integer | 评论数量。 |
| `reels[].are_remixes_crosspostable` | boolean | 官方字段 `are_remixes_crosspostable`；官方未单独提供业务说明。 |
| `reels[].video_versions` | array | 官方字段 `video_versions`；官方未单独提供业务说明。 |
| `reels[].video_versions[].url` | string | 链接。 |
| `reels[].video_versions[].height` | integer | 高度。 |
| `reels[].video_versions[].width` | integer | 宽度。 |
| `reels[].video_versions[].type` | integer | 类型。 |
| `reels[].video_versions[].id` | string | 标识符。 |
| `reels[].video_versions[].fallback` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].video_versions[].url_expiration_timestamp_us` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].video_versions[].bandwidth` | integer | 官方字段 `bandwidth`；官方未单独提供业务说明。 |
| `reels[].image_versions2` | object | 官方字段 `image_versions2`；官方未单独提供业务说明。 |
| `reels[].image_versions2.candidates` | array | 官方字段 `candidates`；官方未单独提供业务说明。 |
| `reels[].image_versions2.candidates[].estimated_scans_sizes` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].image_versions2.candidates[].height` | integer | 高度。 |
| `reels[].image_versions2.candidates[].scans_profile` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].image_versions2.candidates[].url` | string | 链接。 |
| `reels[].image_versions2.candidates[].width` | integer | 宽度。 |
| `reels[].image_versions2.additional_candidates` | object | 官方字段 `additional_candidates`；官方未单独提供业务说明。 |
| `reels[].image_versions2.additional_candidates.first_frame` | object | 官方字段 `first_frame`；官方未单独提供业务说明。 |
| `reels[].image_versions2.additional_candidates.first_frame.estimated_scans_sizes` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].image_versions2.additional_candidates.first_frame.height` | integer | 高度。 |
| `reels[].image_versions2.additional_candidates.first_frame.scans_profile` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].image_versions2.additional_candidates.first_frame.url` | string | 链接。 |
| `reels[].image_versions2.additional_candidates.first_frame.width` | integer | 宽度。 |
| `reels[].image_versions2.additional_candidates.igtv_first_frame` | object | 官方字段 `igtv_first_frame`；官方未单独提供业务说明。 |
| `reels[].image_versions2.additional_candidates.igtv_first_frame.estimated_scans_sizes` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].image_versions2.additional_candidates.igtv_first_frame.height` | integer | 高度。 |
| `reels[].image_versions2.additional_candidates.igtv_first_frame.scans_profile` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].image_versions2.additional_candidates.igtv_first_frame.url` | string | 链接。 |
| `reels[].image_versions2.additional_candidates.igtv_first_frame.width` | integer | 宽度。 |
| `reels[].image_versions2.additional_candidates.smart_frame` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates` | object | 官方字段 `scrubber_spritesheet_info_candidates`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default` | object | 官方字段 `default`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.sprite_urls` | array | 官方字段 `sprite_urls`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.sprite_urls[]` | string | 官方数组 `sprite_urls` 的元素。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.file_size_kb` | integer | 官方字段 `file_size_kb`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.max_thumbnails_per_sprite` | integer | 官方字段 `max_thumbnails_per_sprite`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.rendered_width` | integer | 官方字段 `rendered_width`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.sprite_height` | integer | 官方字段 `sprite_height`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.sprite_width` | integer | 官方字段 `sprite_width`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.thumbnail_duration` | number | 官方字段 `thumbnail_duration`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.thumbnail_height` | integer | 官方字段 `thumbnail_height`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.thumbnail_width` | integer | 官方字段 `thumbnail_width`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.thumbnails_per_row` | integer | 官方字段 `thumbnails_per_row`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.total_thumbnail_num_per_sprite` | integer | 官方字段 `total_thumbnail_num_per_sprite`；官方未单独提供业务说明。 |
| `reels[].image_versions2.scrubber_spritesheet_info_candidates.default.video_length` | number | 官方字段 `video_length`；官方未单独提供业务说明。 |
| `reels[].image_versions2.smart_thumbnail_enabled` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].has_audio` | boolean | 官方字段 `has_audio`；官方未单独提供业务说明。 |
| `reels[].like_count` | integer | 点赞数量。 |
| `reels[].locations` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].is_dash_eligible` | integer | 官方字段 `is_dash_eligible`；官方未单独提供业务说明。 |
| `reels[].is_unified_video` | boolean | 官方字段 `is_unified_video`；官方未单独提供业务说明。 |
| `reels[].enable_media_notes_production` | boolean | 官方字段 `enable_media_notes_production`；官方未单独提供业务说明。 |
| `reels[].play_count` | integer | 播放数量。 |
| `reels[].fb_play_count` | integer | 官方字段 `fb_play_count`；官方未单独提供业务说明。 |
| `reels[].ig_play_count` | integer | 官方字段 `ig_play_count`；官方未单独提供业务说明。 |
| `reels[].is_third_party_downloads_eligible` | boolean | 官方字段 `is_third_party_downloads_eligible`；官方未单独提供业务说明。 |
| `reels[].original_width` | integer | 官方字段 `original_width`；官方未单独提供业务说明。 |
| `reels[].original_height` | integer | 官方字段 `original_height`；官方未单独提供业务说明。 |
| `reels[].is_reuse_allowed` | boolean | 官方字段 `is_reuse_allowed`；官方未单独提供业务说明。 |
| `reels[].has_shared_to_fb` | integer | 官方字段 `has_shared_to_fb`；官方未单独提供业务说明。 |
| `reels[].has_privately_liked` | boolean | 官方字段 `has_privately_liked`；官方未单独提供业务说明。 |
| `reels[].ig_media_sharing_disabled` | boolean | 官方字段 `ig_media_sharing_disabled`；官方未单独提供业务说明。 |
| `reels[].organic_tracking_token` | string | 官方字段 `organic_tracking_token`；官方未单独提供业务说明。 |
| `reels[].has_views_fetching` | boolean | 官方字段 `has_views_fetching`；官方未单独提供业务说明。 |
| `reels[].video_duration` | number | 视频时长。 |
| `reels[].is_post_live_clips_media` | boolean | 官方字段 `is_post_live_clips_media`；官方未单独提供业务说明。 |
| `reels[].is_quiet_post` | boolean | 官方字段 `is_quiet_post`；官方未单独提供业务说明。 |
| `reels[].is_comments_gif_composer_enabled` | boolean | 官方字段 `is_comments_gif_composer_enabled`；官方未单独提供业务说明。 |
| `reels[].clips_tab_pinned_user_ids` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].media_ui_attributions_data` | array | 官方示例为空数组，未提供元素结构。 |
| `reels[].usertags` | object | 官方字段 `usertags`；官方未单独提供业务说明。 |
| `reels[].usertags.in` | array | 官方字段 `in`；官方未单独提供业务说明。 |
| `reels[].usertags.in[].show_category_of_user` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].usertags.in[].position` | array | 位置或排序值。 |
| `reels[].usertags.in[].position[]` | integer | 位置或排序值中的元素。 |
| `reels[].usertags.in[].user` | object | 用户信息。 |
| `reels[].usertags.in[].user.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `reels[].usertags.in[].user.id` | string | 标识符。 |
| `reels[].usertags.in[].user.full_name` | string | 完整名称。 |
| `reels[].usertags.in[].user.has_onboarded_to_text_post_app` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].usertags.in[].user.is_private` | boolean | 是否为私密账号。 |
| `reels[].usertags.in[].user.is_verified` | boolean | 是否认证。 |
| `reels[].usertags.in[].user.pk` | string | 主键标识。 |
| `reels[].usertags.in[].user.pk_id` | string | 主键标识。 |
| `reels[].usertags.in[].user.profile_pic_id` | string | 头像标识。 |
| `reels[].usertags.in[].user.profile_pic_url` | string | 头像链接。 |
| `reels[].usertags.in[].user.username` | string | 用户名。 |
| `reels[].media_cropping_info` | object | 官方字段 `media_cropping_info`；官方未单独提供业务说明。 |
| `reels[].media_cropping_info.four_by_three_crop` | object | 官方字段 `four_by_three_crop`；官方未单独提供业务说明。 |
| `reels[].media_cropping_info.four_by_three_crop.crop_left` | integer | 官方字段 `crop_left`；官方未单独提供业务说明。 |
| `reels[].media_cropping_info.four_by_three_crop.crop_right` | integer | 官方字段 `crop_right`；官方未单独提供业务说明。 |
| `reels[].media_cropping_info.four_by_three_crop.crop_top` | number | 官方字段 `crop_top`；官方未单独提供业务说明。 |
| `reels[].media_cropping_info.four_by_three_crop.crop_bottom` | number | 官方字段 `crop_bottom`；官方未单独提供业务说明。 |
| `cursor` | string | 分页游标。 |
| `has_more` | boolean | 是否还有更多结果。 |

## 使用要点

- audio_id 来自音频页 URL。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-audio-reels" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"audio_id": "1392969992841787"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/instagram/audio/reels/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

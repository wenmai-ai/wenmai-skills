# Wenmai SCRAPECREATORS scrapecreators_instagram_user_posts API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-user-posts`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_instagram_user_posts`
- **脚本入口**：`modules/user-posts/scripts/user_posts.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `handle` | string | 是 | Instagram 用户名，不带 @。 |
| `require_play_counts` | boolean | 否 | 仅字面量 true 生效。要求每条视频帖都有非负 play_count，缺了会 503 且不计费。默认 false。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |
| `next_max_id` | string | 否 | 下一页游标，传入上一页响应中的 next_max_id。 |

## 请求示例

```json
{
  "handle": "gymshark",
  "trim": true
}
```

```bash
python3 modules/user-posts/scripts/user_posts.py '{"handle": "gymshark", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `profile_grid_items` | null | 官方示例为 null，未说明非空类型。 |
| `profile_grid_items_cursor` | null | 官方示例为 null，未说明非空类型。 |
| `pinned_profile_grid_items_ids` | null | 官方示例为 null，未说明非空类型。 |
| `special_empty_state` | null | 官方示例为 null，未说明非空类型。 |
| `num_results` | integer | 官方字段 `num_results`；官方未单独提供业务说明。 |
| `more_available` | boolean | 官方字段 `more_available`；官方未单独提供业务说明。 |
| `items` | array | 结果条目。 |
| `items[].pk` | string | 主键标识。 |
| `items[].id` | string | 标识符。 |
| `items[].fbid` | string | 官方字段 `fbid`；官方未单独提供业务说明。 |
| `items[].device_timestamp` | integer | 官方字段 `device_timestamp`；官方未单独提供业务说明。 |
| `items[].caption_is_edited` | boolean | 官方字段 `caption_is_edited`；官方未单独提供业务说明。 |
| `items[].strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `items[].deleted_reason` | integer | 官方字段 `deleted_reason`；官方未单独提供业务说明。 |
| `items[].has_shared_to_fb` | integer | 官方字段 `has_shared_to_fb`；官方未单独提供业务说明。 |
| `items[].has_delayed_metadata` | boolean | 官方字段 `has_delayed_metadata`；官方未单独提供业务说明。 |
| `items[].mezql_token` | string | 官方字段 `mezql_token`；官方未单独提供业务说明。 |
| `items[].share_count_disabled` | boolean | 官方字段 `share_count_disabled`；官方未单独提供业务说明。 |
| `items[].should_request_ads` | boolean | 官方字段 `should_request_ads`；官方未单独提供业务说明。 |
| `items[].is_reshare_of_text_post_app_media_in_ig` | boolean | 官方字段 `is_reshare_of_text_post_app_media_in_ig`；官方未单独提供业务说明。 |
| `items[].integrity_review_decision` | string | 官方字段 `integrity_review_decision`；官方未单独提供业务说明。 |
| `items[].client_cache_key` | string | 官方字段 `client_cache_key`；官方未单独提供业务说明。 |
| `items[].is_visual_reply_commenter_notice_enabled` | boolean | 官方字段 `is_visual_reply_commenter_notice_enabled`；官方未单独提供业务说明。 |
| `items[].like_and_view_counts_disabled` | boolean | 官方字段 `like_and_view_counts_disabled`；官方未单独提供业务说明。 |
| `items[].is_post_live_clips_media` | boolean | 官方字段 `is_post_live_clips_media`；官方未单独提供业务说明。 |
| `items[].is_quiet_post` | boolean | 官方字段 `is_quiet_post`；官方未单独提供业务说明。 |
| `items[].profile_grid_thumbnail_fitting_style` | string | 官方字段 `profile_grid_thumbnail_fitting_style`；官方未单独提供业务说明。 |
| `items[].comment_threading_enabled` | boolean | 官方字段 `comment_threading_enabled`；官方未单独提供业务说明。 |
| `items[].is_unified_video` | boolean | 官方字段 `is_unified_video`；官方未单独提供业务说明。 |
| `items[].commerciality_status` | string | 官方字段 `commerciality_status`；官方未单独提供业务说明。 |
| `items[].has_privately_liked` | boolean | 官方字段 `has_privately_liked`；官方未单独提供业务说明。 |
| `items[].filter_type` | integer | 官方字段 `filter_type`；官方未单独提供业务说明。 |
| `items[].taken_at` | integer | 官方字段 `taken_at`；官方未单独提供业务说明。 |
| `items[].created_at` | string | 创建时间。 |
| `items[].usertags` | object | 官方字段 `usertags`；官方未单独提供业务说明。 |
| `items[].usertags.in` | array | 官方字段 `in`；官方未单独提供业务说明。 |
| `items[].usertags.in[].position` | array | 位置或排序值。 |
| `items[].usertags.in[].position[]` | integer | 位置或排序值中的元素。 |
| `items[].usertags.in[].user` | object | 用户信息。 |
| `items[].usertags.in[].user.pk` | string | 主键标识。 |
| `items[].usertags.in[].user.pk_id` | string | 主键标识。 |
| `items[].usertags.in[].user.id` | string | 标识符。 |
| `items[].usertags.in[].user.username` | string | 用户名。 |
| `items[].usertags.in[].user.full_name` | string | 完整名称。 |
| `items[].usertags.in[].user.is_private` | boolean | 是否为私密账号。 |
| `items[].usertags.in[].user.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `items[].usertags.in[].user.is_verified` | boolean | 是否认证。 |
| `items[].usertags.in[].user.profile_pic_id` | string | 头像标识。 |
| `items[].usertags.in[].user.profile_pic_url` | string | 头像链接。 |
| `items[].photo_of_you` | boolean | 官方字段 `photo_of_you`；官方未单独提供业务说明。 |
| `items[].can_see_insights_as_brand` | boolean | 官方字段 `can_see_insights_as_brand`；官方未单独提供业务说明。 |
| `items[].media_type` | integer | 官方字段 `media_type`；官方未单独提供业务说明。 |
| `items[].code` | string | 官方业务编码。 |
| `items[].caption` | object | 说明文字。 |
| `items[].caption.bit_flags` | integer | 官方字段 `bit_flags`；官方未单独提供业务说明。 |
| `items[].caption.created_at` | integer | 创建时间。 |
| `items[].caption.created_at_utc` | integer | 官方字段 `created_at_utc`；官方未单独提供业务说明。 |
| `items[].caption.did_report_as_spam` | boolean | 官方字段 `did_report_as_spam`；官方未单独提供业务说明。 |
| `items[].caption.is_ranked_comment` | boolean | 官方字段 `is_ranked_comment`；官方未单独提供业务说明。 |
| `items[].caption.pk` | string | 主键标识。 |
| `items[].caption.share_enabled` | boolean | 官方字段 `share_enabled`；官方未单独提供业务说明。 |
| `items[].caption.content_type` | string | 官方字段 `content_type`；官方未单独提供业务说明。 |
| `items[].caption.media_id` | string | 官方字段 `media_id`；官方未单独提供业务说明。 |
| `items[].caption.status` | string | 状态。 |
| `items[].caption.type` | integer | 类型。 |
| `items[].caption.user_id` | string | 用户标识。 |
| `items[].caption.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `items[].caption.text` | string | 文本内容。 |
| `items[].caption.user` | object | 用户信息。 |
| `items[].caption.user.pk` | string | 主键标识。 |
| `items[].caption.user.pk_id` | string | 主键标识。 |
| `items[].caption.user.id` | string | 标识符。 |
| `items[].caption.user.username` | string | 用户名。 |
| `items[].caption.user.full_name` | string | 完整名称。 |
| `items[].caption.user.is_private` | boolean | 是否为私密账号。 |
| `items[].caption.user.is_unpublished` | boolean | 官方字段 `is_unpublished`；官方未单独提供业务说明。 |
| `items[].caption.user.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `items[].caption.user.fbid_v2` | string | 官方字段 `fbid_v2`；官方未单独提供业务说明。 |
| `items[].caption.user.is_verified` | boolean | 是否认证。 |
| `items[].caption.user.profile_pic_id` | string | 头像标识。 |
| `items[].caption.user.profile_pic_url` | string | 头像链接。 |
| `items[].caption.is_covered` | boolean | 官方字段 `is_covered`；官方未单独提供业务说明。 |
| `items[].caption.private_reply_status` | integer | 官方字段 `private_reply_status`；官方未单独提供业务说明。 |
| `items[].sharing_friction_info` | object | 官方字段 `sharing_friction_info`；官方未单独提供业务说明。 |
| `items[].sharing_friction_info.bloks_app_url` | null | 官方示例为 null，未说明非空类型。 |
| `items[].sharing_friction_info.should_have_sharing_friction` | boolean | 官方字段 `should_have_sharing_friction`；官方未单独提供业务说明。 |
| `items[].sharing_friction_info.sharing_friction_payload` | null | 官方示例为 null，未说明非空类型。 |
| `items[].timeline_pinned_user_ids` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].play_count` | integer | 播放数量。 |
| `items[].has_views_fetching` | boolean | 官方字段 `has_views_fetching`；官方未单独提供业务说明。 |
| `items[].ig_play_count` | integer | 官方字段 `ig_play_count`；官方未单独提供业务说明。 |
| `items[].creator_viewer_insights` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].display_uri` | string | 官方字段 `display_uri`；官方未单独提供业务说明。 |
| `items[].fb_user_tags` | object | 官方字段 `fb_user_tags`；官方未单独提供业务说明。 |
| `items[].fb_user_tags.in` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].coauthor_producers` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].coauthor_producer_can_see_organic_insights` | boolean | 官方字段 `coauthor_producer_can_see_organic_insights`；官方未单独提供业务说明。 |
| `items[].invited_coauthor_producers` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].is_in_profile_grid` | boolean | 官方字段 `is_in_profile_grid`；官方未单独提供业务说明。 |
| `items[].profile_grid_control_enabled` | boolean | 官方字段 `profile_grid_control_enabled`；官方未单独提供业务说明。 |
| `items[].media_cropping_info` | object | 官方字段 `media_cropping_info`；官方未单独提供业务说明。 |
| `items[].media_cropping_info.four_by_three_crop` | object | 官方字段 `four_by_three_crop`；官方未单独提供业务说明。 |
| `items[].media_cropping_info.four_by_three_crop.crop_left` | integer | 官方字段 `crop_left`；官方未单独提供业务说明。 |
| `items[].media_cropping_info.four_by_three_crop.crop_right` | integer | 官方字段 `crop_right`；官方未单独提供业务说明。 |
| `items[].media_cropping_info.four_by_three_crop.crop_top` | number | 官方字段 `crop_top`；官方未单独提供业务说明。 |
| `items[].media_cropping_info.four_by_three_crop.crop_bottom` | number | 官方字段 `crop_bottom`；官方未单独提供业务说明。 |
| `items[].user` | object | 用户信息。 |
| `items[].user.fbid_v2` | string | 官方字段 `fbid_v2`；官方未单独提供业务说明。 |
| `items[].user.feed_post_reshare_disabled` | boolean | 官方字段 `feed_post_reshare_disabled`；官方未单独提供业务说明。 |
| `items[].user.full_name` | string | 完整名称。 |
| `items[].user.id` | string | 标识符。 |
| `items[].user.is_private` | boolean | 是否为私密账号。 |
| `items[].user.is_unpublished` | boolean | 官方字段 `is_unpublished`；官方未单独提供业务说明。 |
| `items[].user.pk` | string | 主键标识。 |
| `items[].user.pk_id` | string | 主键标识。 |
| `items[].user.show_account_transparency_details` | boolean | 官方字段 `show_account_transparency_details`；官方未单独提供业务说明。 |
| `items[].user.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `items[].user.third_party_downloads_enabled` | integer | 官方字段 `third_party_downloads_enabled`；官方未单独提供业务说明。 |
| `items[].user.username` | string | 用户名。 |
| `items[].user.account_type` | integer | 官方字段 `account_type`；官方未单独提供业务说明。 |
| `items[].user.account_badges` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].user.fan_club_info` | object | 官方字段 `fan_club_info`；官方未单独提供业务说明。 |
| `items[].user.fan_club_info.autosave_to_exclusive_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.connected_member_count` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.fan_club_id` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.fan_club_name` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.has_created_ssc` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.has_enough_subscribers_for_ssc` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.is_fan_club_gifting_eligible` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.is_fan_club_referral_eligible` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.is_free_trial_eligible` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.largest_public_bc_id` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.subscriber_count` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.fan_club_info.fan_consideration_page_revamp_eligiblity` | null | 官方示例为 null，未说明非空类型。 |
| `items[].user.has_anonymous_profile_picture` | boolean | 官方字段 `has_anonymous_profile_picture`；官方未单独提供业务说明。 |
| `items[].user.hd_profile_pic_url_info` | object | 官方字段 `hd_profile_pic_url_info`；官方未单独提供业务说明。 |
| `items[].user.hd_profile_pic_url_info.height` | integer | 高度。 |
| `items[].user.hd_profile_pic_url_info.url` | string | 链接。 |
| `items[].user.hd_profile_pic_url_info.width` | integer | 宽度。 |
| `items[].user.hd_profile_pic_versions` | array | 官方字段 `hd_profile_pic_versions`；官方未单独提供业务说明。 |
| `items[].user.hd_profile_pic_versions[].height` | integer | 高度。 |
| `items[].user.hd_profile_pic_versions[].url` | string | 链接。 |
| `items[].user.hd_profile_pic_versions[].width` | integer | 宽度。 |
| `items[].user.is_verified` | boolean | 是否认证。 |
| `items[].user.profile_pic_id` | string | 头像标识。 |
| `items[].user.profile_pic_url` | string | 头像链接。 |
| `items[].user.transparency_product_enabled` | boolean | 官方字段 `transparency_product_enabled`；官方未单独提供业务说明。 |
| `items[].user.is_embeds_disabled` | boolean | 官方字段 `is_embeds_disabled`；官方未单独提供业务说明。 |
| `items[].owner` | object | 所属账号。 |
| `items[].owner.fbid_v2` | string | 官方字段 `fbid_v2`；官方未单独提供业务说明。 |
| `items[].owner.feed_post_reshare_disabled` | boolean | 官方字段 `feed_post_reshare_disabled`；官方未单独提供业务说明。 |
| `items[].owner.full_name` | string | 完整名称。 |
| `items[].owner.id` | string | 标识符。 |
| `items[].owner.is_private` | boolean | 是否为私密账号。 |
| `items[].owner.is_unpublished` | boolean | 官方字段 `is_unpublished`；官方未单独提供业务说明。 |
| `items[].owner.pk` | string | 主键标识。 |
| `items[].owner.pk_id` | string | 主键标识。 |
| `items[].owner.show_account_transparency_details` | boolean | 官方字段 `show_account_transparency_details`；官方未单独提供业务说明。 |
| `items[].owner.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `items[].owner.third_party_downloads_enabled` | integer | 官方字段 `third_party_downloads_enabled`；官方未单独提供业务说明。 |
| `items[].owner.username` | string | 用户名。 |
| `items[].owner.account_type` | integer | 官方字段 `account_type`；官方未单独提供业务说明。 |
| `items[].owner.can_see_quiet_post_attribution` | boolean | 官方字段 `can_see_quiet_post_attribution`；官方未单独提供业务说明。 |
| `items[].owner.account_badges` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].owner.fan_club_info` | object | 官方字段 `fan_club_info`；官方未单独提供业务说明。 |
| `items[].owner.fan_club_info.autosave_to_exclusive_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.connected_member_count` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.fan_club_id` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.fan_club_name` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.has_created_ssc` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.has_enough_subscribers_for_ssc` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.is_fan_club_gifting_eligible` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.is_fan_club_referral_eligible` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.is_free_trial_eligible` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.largest_public_bc_id` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.subscriber_count` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.fan_club_info.fan_consideration_page_revamp_eligiblity` | null | 官方示例为 null，未说明非空类型。 |
| `items[].owner.has_anonymous_profile_picture` | boolean | 官方字段 `has_anonymous_profile_picture`；官方未单独提供业务说明。 |
| `items[].owner.hd_profile_pic_url_info` | object | 官方字段 `hd_profile_pic_url_info`；官方未单独提供业务说明。 |
| `items[].owner.hd_profile_pic_url_info.height` | integer | 高度。 |
| `items[].owner.hd_profile_pic_url_info.url` | string | 链接。 |
| `items[].owner.hd_profile_pic_url_info.width` | integer | 宽度。 |
| `items[].owner.hd_profile_pic_versions` | array | 官方字段 `hd_profile_pic_versions`；官方未单独提供业务说明。 |
| `items[].owner.hd_profile_pic_versions[].height` | integer | 高度。 |
| `items[].owner.hd_profile_pic_versions[].url` | string | 链接。 |
| `items[].owner.hd_profile_pic_versions[].width` | integer | 宽度。 |
| `items[].owner.is_verified` | boolean | 是否认证。 |
| `items[].owner.profile_pic_id` | string | 头像标识。 |
| `items[].owner.profile_pic_url` | string | 头像链接。 |
| `items[].owner.transparency_product_enabled` | boolean | 官方字段 `transparency_product_enabled`；官方未单独提供业务说明。 |
| `items[].owner.is_embeds_disabled` | boolean | 官方字段 `is_embeds_disabled`；官方未单独提供业务说明。 |
| `items[].image_versions2` | object | 官方字段 `image_versions2`；官方未单独提供业务说明。 |
| `items[].image_versions2.candidates` | array | 官方字段 `candidates`；官方未单独提供业务说明。 |
| `items[].image_versions2.candidates[].width` | integer | 宽度。 |
| `items[].image_versions2.candidates[].height` | integer | 高度。 |
| `items[].image_versions2.candidates[].url` | string | 链接。 |
| `items[].image_versions2.additional_candidates` | object | 官方字段 `additional_candidates`；官方未单独提供业务说明。 |
| `items[].image_versions2.additional_candidates.igtv_first_frame` | object | 官方字段 `igtv_first_frame`；官方未单独提供业务说明。 |
| `items[].image_versions2.additional_candidates.igtv_first_frame.width` | integer | 宽度。 |
| `items[].image_versions2.additional_candidates.igtv_first_frame.height` | integer | 高度。 |
| `items[].image_versions2.additional_candidates.igtv_first_frame.url` | string | 链接。 |
| `items[].image_versions2.additional_candidates.first_frame` | object | 官方字段 `first_frame`；官方未单独提供业务说明。 |
| `items[].image_versions2.additional_candidates.first_frame.width` | integer | 宽度。 |
| `items[].image_versions2.additional_candidates.first_frame.height` | integer | 高度。 |
| `items[].image_versions2.additional_candidates.first_frame.url` | string | 链接。 |
| `items[].image_versions2.additional_candidates.smart_frame` | null | 官方示例为 null，未说明非空类型。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates` | object | 官方字段 `scrubber_spritesheet_info_candidates`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default` | object | 官方字段 `default`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.video_length` | number | 官方字段 `video_length`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.thumbnail_width` | integer | 官方字段 `thumbnail_width`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.thumbnail_height` | integer | 官方字段 `thumbnail_height`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.thumbnail_duration` | number | 官方字段 `thumbnail_duration`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.sprite_urls` | array | 官方字段 `sprite_urls`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.sprite_urls[]` | string | 官方数组 `sprite_urls` 的元素。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.thumbnails_per_row` | integer | 官方字段 `thumbnails_per_row`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.total_thumbnail_num_per_sprite` | integer | 官方字段 `total_thumbnail_num_per_sprite`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.max_thumbnails_per_sprite` | integer | 官方字段 `max_thumbnails_per_sprite`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.sprite_width` | integer | 官方字段 `sprite_width`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.sprite_height` | integer | 官方字段 `sprite_height`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.rendered_width` | integer | 官方字段 `rendered_width`；官方未单独提供业务说明。 |
| `items[].image_versions2.scrubber_spritesheet_info_candidates.default.file_size_kb` | integer | 官方字段 `file_size_kb`；官方未单独提供业务说明。 |
| `items[].original_width` | integer | 官方字段 `original_width`；官方未单独提供业务说明。 |
| `items[].original_height` | integer | 官方字段 `original_height`；官方未单独提供业务说明。 |
| `items[].is_artist_pick` | boolean | 官方字段 `is_artist_pick`；官方未单独提供业务说明。 |
| `items[].media_reposter_bottomsheet_enabled` | boolean | 官方字段 `media_reposter_bottomsheet_enabled`；官方未单独提供业务说明。 |
| `items[].enable_media_notes_production` | boolean | 官方字段 `enable_media_notes_production`；官方未单独提供业务说明。 |
| `items[].product_type` | string | 官方字段 `product_type`；官方未单独提供业务说明。 |
| `items[].is_paid_partnership` | boolean | 是否为付费合作内容。 |
| `items[].music_metadata` | null | 官方示例为 null，未说明非空类型。 |
| `items[].organic_tracking_token` | string | 官方字段 `organic_tracking_token`；官方未单独提供业务说明。 |
| `items[].is_third_party_downloads_eligible` | boolean | 官方字段 `is_third_party_downloads_eligible`；官方未单独提供业务说明。 |
| `items[].ig_media_sharing_disabled` | boolean | 官方字段 `ig_media_sharing_disabled`；官方未单独提供业务说明。 |
| `items[].are_remixes_crosspostable` | boolean | 官方字段 `are_remixes_crosspostable`；官方未单独提供业务说明。 |
| `items[].boost_unavailable_identifier` | null | 官方示例为 null，未说明非空类型。 |
| `items[].boost_unavailable_reason` | null | 官方示例为 null，未说明非空类型。 |
| `items[].boost_unavailable_reason_v2` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].subscribe_cta_visible` | boolean | 官方字段 `subscribe_cta_visible`；官方未单独提供业务说明。 |
| `items[].is_cutout_sticker_allowed` | boolean | 官方字段 `is_cutout_sticker_allowed`；官方未单独提供业务说明。 |
| `items[].cutout_sticker_info` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].gen_ai_detection_method` | object | 官方字段 `gen_ai_detection_method`；官方未单独提供业务说明。 |
| `items[].gen_ai_detection_method.detection_method` | string | 官方字段 `detection_method`；官方未单独提供业务说明。 |
| `items[].fb_aggregated_like_count` | integer | 官方字段 `fb_aggregated_like_count`；官方未单独提供业务说明。 |
| `items[].fb_aggregated_comment_count` | integer | 官方字段 `fb_aggregated_comment_count`；官方未单独提供业务说明。 |
| `items[].has_high_risk_gen_ai_inform_treatment` | boolean | 官方字段 `has_high_risk_gen_ai_inform_treatment`；官方未单独提供业务说明。 |
| `items[].open_carousel_show_follow_button` | boolean | 官方字段 `open_carousel_show_follow_button`；官方未单独提供业务说明。 |
| `items[].is_tagged_media_shared_to_viewer_profile_grid` | boolean | 官方字段 `is_tagged_media_shared_to_viewer_profile_grid`；官方未单独提供业务说明。 |
| `items[].should_show_author_pog_for_tagged_media_shared_to_profile_grid` | boolean | 官方字段 `should_show_author_pog_for_tagged_media_shared_to_profile_grid`；官方未单独提供业务说明。 |
| `items[].is_eligible_for_media_note_recs_nux` | boolean | 官方字段 `is_eligible_for_media_note_recs_nux`；官方未单独提供业务说明。 |
| `items[].is_social_ufi_disabled` | boolean | 官方字段 `is_social_ufi_disabled`；官方未单独提供业务说明。 |
| `items[].is_eligible_for_meta_ai_share` | boolean | 官方字段 `is_eligible_for_meta_ai_share`；官方未单独提供业务说明。 |
| `items[].meta_ai_suggested_prompts` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].can_reply` | boolean | 官方字段 `can_reply`；官方未单独提供业务说明。 |
| `items[].floating_context_items` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].is_eligible_content_for_post_roll_ad` | boolean | 官方字段 `is_eligible_content_for_post_roll_ad`；官方未单独提供业务说明。 |
| `items[].is_open_to_public_submission` | boolean | 官方字段 `is_open_to_public_submission`；官方未单独提供业务说明。 |
| `items[].can_view_more_preview_comments` | boolean | 官方字段 `can_view_more_preview_comments`；官方未单独提供业务说明。 |
| `items[].preview_comments` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].comment_count` | integer | 评论数量。 |
| `items[].hide_view_all_comment_entrypoint` | boolean | 官方字段 `hide_view_all_comment_entrypoint`；官方未单独提供业务说明。 |
| `items[].inline_composer_display_condition` | string | 官方字段 `inline_composer_display_condition`；官方未单独提供业务说明。 |
| `items[].is_comments_gif_composer_enabled` | boolean | 官方字段 `is_comments_gif_composer_enabled`；官方未单独提供业务说明。 |
| `items[].comment_inform_treatment` | object | 官方字段 `comment_inform_treatment`；官方未单独提供业务说明。 |
| `items[].comment_inform_treatment.action_type` | null | 官方示例为 null，未说明非空类型。 |
| `items[].comment_inform_treatment.should_have_inform_treatment` | boolean | 官方字段 `should_have_inform_treatment`；官方未单独提供业务说明。 |
| `items[].comment_inform_treatment.text` | string | 文本内容。 |
| `items[].comment_inform_treatment.url` | null | 官方示例为 null，未说明非空类型。 |
| `items[].has_liked` | boolean | 官方字段 `has_liked`；官方未单独提供业务说明。 |
| `items[].like_count` | integer | 点赞数量。 |
| `items[].video_sticker_locales` | array | 官方字段 `video_sticker_locales`；官方未单独提供业务说明。 |
| `items[].video_sticker_locales[]` | string | 官方数组 `video_sticker_locales` 的元素。 |
| `items[].is_dash_eligible` | integer | 官方字段 `is_dash_eligible`；官方未单独提供业务说明。 |
| `items[].number_of_qualities` | integer | 官方字段 `number_of_qualities`；官方未单独提供业务说明。 |
| `items[].video_versions` | array | 官方字段 `video_versions`；官方未单独提供业务说明。 |
| `items[].video_versions[].bandwidth` | null | 官方示例为 null，未说明非空类型。 |
| `items[].video_versions[].height` | integer | 高度。 |
| `items[].video_versions[].type` | integer | 类型。 |
| `items[].video_versions[].url` | string | 链接。 |
| `items[].video_versions[].width` | integer | 宽度。 |
| `items[].video_duration` | number | 视频时长。 |
| `items[].has_audio` | boolean | 官方字段 `has_audio`；官方未单独提供业务说明。 |
| `items[].clips_tab_pinned_user_ids` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].clips_metadata` | object | 官方字段 `clips_metadata`；官方未单独提供业务说明。 |
| `items[].clips_metadata.breaking_content_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.breaking_creator_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.clips_creation_entry_point` | string | 官方字段 `clips_creation_entry_point`；官方未单独提供业务说明。 |
| `items[].clips_metadata.featured_label` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.is_public_chat_welcome_video` | boolean | 官方字段 `is_public_chat_welcome_video`；官方未单独提供业务说明。 |
| `items[].clips_metadata.is_shared_to_fb` | boolean | 官方字段 `is_shared_to_fb`；官方未单独提供业务说明。 |
| `items[].clips_metadata.professional_clips_upsell_type` | integer | 官方字段 `professional_clips_upsell_type`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reels_on_the_rise_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.show_tips` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.achievements_info` | object | 官方字段 `achievements_info`；官方未单独提供业务说明。 |
| `items[].clips_metadata.achievements_info.num_earned_achievements` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.achievements_info.show_achievements` | boolean | 官方字段 `show_achievements`；官方未单独提供业务说明。 |
| `items[].clips_metadata.additional_audio_info` | object | 官方字段 `additional_audio_info`；官方未单独提供业务说明。 |
| `items[].clips_metadata.additional_audio_info.additional_audio_username` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.additional_audio_info.audio_reattribution_info` | object | 官方字段 `audio_reattribution_info`；官方未单独提供业务说明。 |
| `items[].clips_metadata.additional_audio_info.audio_reattribution_info.should_allow_restore` | boolean | 官方字段 `should_allow_restore`；官方未单独提供业务说明。 |
| `items[].clips_metadata.asset_recommendation_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.audio_ranking_info` | object | 官方字段 `audio_ranking_info`；官方未单独提供业务说明。 |
| `items[].clips_metadata.audio_ranking_info.best_audio_cluster_id` | string | 官方字段 `best_audio_cluster_id`；官方未单独提供业务说明。 |
| `items[].clips_metadata.audio_type` | string | 官方字段 `audio_type`；官方未单独提供业务说明。 |
| `items[].clips_metadata.branded_content_tag_info` | object | 官方字段 `branded_content_tag_info`；官方未单独提供业务说明。 |
| `items[].clips_metadata.branded_content_tag_info.can_add_tag` | boolean | 官方字段 `can_add_tag`；官方未单独提供业务说明。 |
| `items[].clips_metadata.challenge_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.content_appreciation_info` | object | 官方字段 `content_appreciation_info`；官方未单独提供业务说明。 |
| `items[].clips_metadata.content_appreciation_info.enabled` | boolean | 官方字段 `enabled`；官方未单独提供业务说明。 |
| `items[].clips_metadata.content_appreciation_info.entry_point_container` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.contextual_highlight_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.cutout_sticker_info` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].clips_metadata.disable_use_in_clips_client_cache` | boolean | 官方字段 `disable_use_in_clips_client_cache`；官方未单独提供业务说明。 |
| `items[].clips_metadata.external_media_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.is_fan_club_promo_video` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.merchandising_pill_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.music_canonical_id` | string | 官方字段 `music_canonical_id`；官方未单独提供业务说明。 |
| `items[].clips_metadata.music_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.nux_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info` | object | 官方字段 `original_sound_info`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.allow_creator_to_rename` | boolean | 官方字段 `allow_creator_to_rename`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.audio_asset_id` | string | 官方字段 `audio_asset_id`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.attributed_custom_audio_asset_id` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.can_remix_be_shared_to_fb` | boolean | 官方字段 `can_remix_be_shared_to_fb`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.can_remix_be_shared_to_fb_expansion` | boolean | 官方字段 `can_remix_be_shared_to_fb_expansion`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.duration_in_ms` | integer | 官方字段 `duration_in_ms`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.formatted_clips_media_count` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.hide_remixing` | boolean | 官方字段 `hide_remixing`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.ig_artist` | object | 官方字段 `ig_artist`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.ig_artist.pk` | string | 主键标识。 |
| `items[].clips_metadata.original_sound_info.ig_artist.pk_id` | string | 主键标识。 |
| `items[].clips_metadata.original_sound_info.ig_artist.id` | string | 标识符。 |
| `items[].clips_metadata.original_sound_info.ig_artist.username` | string | 用户名。 |
| `items[].clips_metadata.original_sound_info.ig_artist.full_name` | string | 完整名称。 |
| `items[].clips_metadata.original_sound_info.ig_artist.is_private` | boolean | 是否为私密账号。 |
| `items[].clips_metadata.original_sound_info.ig_artist.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.ig_artist.is_verified` | boolean | 是否认证。 |
| `items[].clips_metadata.original_sound_info.ig_artist.profile_pic_id` | string | 头像标识。 |
| `items[].clips_metadata.original_sound_info.ig_artist.profile_pic_url` | string | 头像链接。 |
| `items[].clips_metadata.original_sound_info.is_audio_automatically_attributed` | boolean | 官方字段 `is_audio_automatically_attributed`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.is_eligible_for_audio_effects` | boolean | 官方字段 `is_eligible_for_audio_effects`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.is_eligible_for_vinyl_sticker` | boolean | 官方字段 `is_eligible_for_vinyl_sticker`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.is_explicit` | boolean | 官方字段 `is_explicit`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.is_original_audio_download_eligible` | boolean | 官方字段 `is_original_audio_download_eligible`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.is_reuse_disabled` | boolean | 官方字段 `is_reuse_disabled`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.is_xpost_from_fb` | boolean | 官方字段 `is_xpost_from_fb`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.music_canonical_id` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.oa_owner_is_music_artist` | boolean | 官方字段 `oa_owner_is_music_artist`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.original_audio_subtype` | string | 官方字段 `original_audio_subtype`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.original_audio_title` | string | 官方字段 `original_audio_title`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.original_media_id` | string | 官方字段 `original_media_id`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.progressive_download_url` | string | 官方字段 `progressive_download_url`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.should_mute_audio` | boolean | 官方字段 `should_mute_audio`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.time_created` | integer | 官方字段 `time_created`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.trend_rank` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.previous_trend_rank` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.overlap_duration_in_ms` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.audio_asset_start_time_in_ms` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.audio_filter_infos` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].clips_metadata.original_sound_info.audio_parts` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].clips_metadata.original_sound_info.audio_parts_by_filter` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].clips_metadata.original_sound_info.consumption_info` | object | 官方字段 `consumption_info`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.consumption_info.display_media_id` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.consumption_info.is_bookmarked` | boolean | 官方字段 `is_bookmarked`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.consumption_info.is_trending_in_clips` | boolean | 官方字段 `is_trending_in_clips`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.consumption_info.should_mute_audio_reason` | string | 官方字段 `should_mute_audio_reason`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.consumption_info.should_mute_audio_reason_type` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.xpost_fb_creator_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.original_sound_info.fb_downstream_use_xpost_metadata` | object | 官方字段 `fb_downstream_use_xpost_metadata`；官方未单独提供业务说明。 |
| `items[].clips_metadata.original_sound_info.fb_downstream_use_xpost_metadata.downstream_use_xpost_deny_reason` | string | 官方字段 `downstream_use_xpost_deny_reason`；官方未单独提供业务说明。 |
| `items[].clips_metadata.originality_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.reusable_text_attribute_string` | string | 官方字段 `reusable_text_attribute_string`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info` | array | 官方字段 `reusable_text_info`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].id` | string | 标识符。 |
| `items[].clips_metadata.reusable_text_info[].text` | string | 文本内容。 |
| `items[].clips_metadata.reusable_text_info[].start_time_ms` | integer | 官方字段 `start_time_ms`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].end_time_ms` | integer | 官方字段 `end_time_ms`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].width` | number | 宽度。 |
| `items[].clips_metadata.reusable_text_info[].height` | number | 高度。 |
| `items[].clips_metadata.reusable_text_info[].offset_x` | number | 官方字段 `offset_x`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].offset_y` | number | 官方字段 `offset_y`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].z_index` | integer | 官方字段 `z_index`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].rotation_degree` | integer | 官方字段 `rotation_degree`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].scale` | integer | 官方字段 `scale`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].alignment` | string | 官方字段 `alignment`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].colors` | array | 官方字段 `colors`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].colors[].count` | integer | 数量。 |
| `items[].clips_metadata.reusable_text_info[].colors[].hex_rgba_color` | string | 官方字段 `hex_rgba_color`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].text_format_type` | string | 官方字段 `text_format_type`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].font_size` | number | 官方字段 `font_size`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].text_emphasis_mode` | string | 官方字段 `text_emphasis_mode`；官方未单独提供业务说明。 |
| `items[].clips_metadata.reusable_text_info[].is_animated` | integer | 官方字段 `is_animated`；官方未单独提供业务说明。 |
| `items[].clips_metadata.shopping_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.show_achievements` | boolean | 官方字段 `show_achievements`；官方未单独提供业务说明。 |
| `items[].clips_metadata.template_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_metadata.viewer_interaction_settings` | null | 官方示例为 null，未说明非空类型。 |
| `items[].clips_text` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].can_viewer_save` | boolean | 官方字段 `can_viewer_save`；官方未单独提供业务说明。 |
| `items[].can_viewer_reshare` | boolean | 官方字段 `can_viewer_reshare`；官方未单独提供业务说明。 |
| `items[].shop_routing_user_id` | null | 官方示例为 null，未说明非空类型。 |
| `items[].is_organic_product_tagging_eligible` | boolean | 官方字段 `is_organic_product_tagging_eligible`；官方未单独提供业务说明。 |
| `items[].igbio_product` | null | 官方示例为 null，未说明非空类型。 |
| `items[].product_suggestions` | array | 官方示例为空数组，未提供元素结构。 |
| `items[].commerce_integrity_review_decision` | string | 官方字段 `commerce_integrity_review_decision`；官方未单独提供业务说明。 |
| `items[].is_reuse_allowed` | boolean | 官方字段 `is_reuse_allowed`；官方未单独提供业务说明。 |
| `items[].has_more_comments` | boolean | 官方字段 `has_more_comments`；官方未单独提供业务说明。 |
| `items[].max_num_visible_preview_comments` | integer | 官方字段 `max_num_visible_preview_comments`；官方未单独提供业务说明。 |
| `items[].explore_hide_comments` | boolean | 官方字段 `explore_hide_comments`；官方未单独提供业务说明。 |
| `items[].url` | string | 链接。 |
| `next_max_id` | string | 后续分页标识。 |
| `user` | object | 用户信息。 |
| `user.pk` | string | 主键标识。 |
| `user.pk_id` | string | 主键标识。 |
| `user.username` | string | 用户名。 |
| `user.full_name` | string | 完整名称。 |
| `user.is_private` | boolean | 是否为私密账号。 |
| `user.is_active_on_text_post_app` | boolean | 官方字段 `is_active_on_text_post_app`；官方未单独提供业务说明。 |
| `user.strong_id__` | string | 官方字段 `strong_id__`；官方未单独提供业务说明。 |
| `user.profile_grid_display_type` | string | 官方字段 `profile_grid_display_type`；官方未单独提供业务说明。 |
| `user.id` | string | 标识符。 |
| `user.is_verified` | boolean | 是否认证。 |
| `user.profile_pic_id` | string | 头像标识。 |
| `user.profile_pic_url` | string | 头像链接。 |
| `auto_load_more_enabled` | boolean | 官方字段 `auto_load_more_enabled`；官方未单独提供业务说明。 |
| `status` | string | 状态。 |
| `items[].user.eligible_for_text_app_activation_badge` | boolean | 官方字段 `eligible_for_text_app_activation_badge`；官方未单独提供业务说明。 |
| `items[].owner.eligible_for_text_app_activation_badge` | boolean | 官方字段 `eligible_for_text_app_activation_badge`；官方未单独提供业务说明。 |

## 使用要点

- 不要默认 require_play_counts=true。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-user-posts" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "gymshark", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v2/instagram/user/posts/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

# Wenmai SCRAPECREATORS scrapecreators_tiktok_user_followers API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-user-followers`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_user_followers`
- **脚本入口**：`modules/user-followers/scripts/user_followers.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `handle` | string | 是 | TikTok 用户名，不带 @。 |
| `user_id` | string | 否 | 用户数字 ID。传入后响应更快。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |
| `min_time` | number | 否 | 分页参数，传入上一页响应中的 min_time。 |

## 请求示例

```json
{
  "handle": "gymshark",
  "trim": true
}
```

```bash
python3 modules/user-followers/scripts/user_followers.py '{"handle": "gymshark", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `extra` | object | 官方字段 `extra`；官方未单独提供业务说明。 |
| `extra.fatal_item_ids` | array | 官方示例为空数组，未提供元素结构。 |
| `extra.logid` | string | 官方字段 `logid`；官方未单独提供业务说明。 |
| `extra.now` | integer | 官方字段 `now`；官方未单独提供业务说明。 |
| `followers` | array | 官方字段 `followers`；官方未单独提供业务说明。 |
| `followers[].accept_private_policy` | boolean | 官方字段 `accept_private_policy`；官方未单独提供业务说明。 |
| `followers[].account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].account_region` | string | 官方字段 `account_region`；官方未单独提供业务说明。 |
| `followers[].ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].apple_account` | integer | 官方字段 `apple_account`；官方未单独提供业务说明。 |
| `followers[].authority_status` | integer | 官方字段 `authority_status`；官方未单独提供业务说明。 |
| `followers[].avatar_168x168` | object | 官方字段 `avatar_168x168`；官方未单独提供业务说明。 |
| `followers[].avatar_168x168.height` | integer | 高度。 |
| `followers[].avatar_168x168.uri` | string | 资源标识。 |
| `followers[].avatar_168x168.url_list` | array | 资源链接列表。 |
| `followers[].avatar_168x168.url_list[]` | string | 资源链接列表中的元素。 |
| `followers[].avatar_168x168.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].avatar_168x168.width` | integer | 宽度。 |
| `followers[].avatar_300x300` | object | 官方字段 `avatar_300x300`；官方未单独提供业务说明。 |
| `followers[].avatar_300x300.height` | integer | 高度。 |
| `followers[].avatar_300x300.uri` | string | 资源标识。 |
| `followers[].avatar_300x300.url_list` | array | 资源链接列表。 |
| `followers[].avatar_300x300.url_list[]` | string | 资源链接列表中的元素。 |
| `followers[].avatar_300x300.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].avatar_300x300.width` | integer | 宽度。 |
| `followers[].avatar_larger` | object | 官方字段 `avatar_larger`；官方未单独提供业务说明。 |
| `followers[].avatar_larger.height` | integer | 高度。 |
| `followers[].avatar_larger.uri` | string | 资源标识。 |
| `followers[].avatar_larger.url_list` | array | 资源链接列表。 |
| `followers[].avatar_larger.url_list[]` | string | 资源链接列表中的元素。 |
| `followers[].avatar_larger.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].avatar_larger.width` | integer | 宽度。 |
| `followers[].avatar_medium` | object | 中等尺寸头像。 |
| `followers[].avatar_medium.height` | integer | 高度。 |
| `followers[].avatar_medium.uri` | string | 资源标识。 |
| `followers[].avatar_medium.url_list` | array | 资源链接列表。 |
| `followers[].avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `followers[].avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].avatar_medium.width` | integer | 宽度。 |
| `followers[].avatar_thumb` | object | 缩略头像。 |
| `followers[].avatar_thumb.height` | integer | 高度。 |
| `followers[].avatar_thumb.uri` | string | 资源标识。 |
| `followers[].avatar_thumb.url_list` | array | 资源链接列表。 |
| `followers[].avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `followers[].avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].avatar_thumb.width` | integer | 宽度。 |
| `followers[].avatar_uri` | string | 官方字段 `avatar_uri`；官方未单独提供业务说明。 |
| `followers[].aweme_count` | integer | 官方字段 `aweme_count`；官方未单独提供业务说明。 |
| `followers[].bind_phone` | string | 官方字段 `bind_phone`；官方未单独提供业务说明。 |
| `followers[].bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].can_message_follow_status_list` | array | 官方字段 `can_message_follow_status_list`；官方未单独提供业务说明。 |
| `followers[].can_message_follow_status_list[]` | integer | 官方数组 `can_message_follow_status_list` 的元素。 |
| `followers[].can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].comment_filter_status` | integer | 官方字段 `comment_filter_status`；官方未单独提供业务说明。 |
| `followers[].comment_setting` | integer | 官方字段 `comment_setting`；官方未单独提供业务说明。 |
| `followers[].commerce_user_level` | integer | 官方字段 `commerce_user_level`；官方未单独提供业务说明。 |
| `followers[].cover_url` | array | 官方示例为空数组，未提供元素结构。 |
| `followers[].create_time` | integer | 创建时间。 |
| `followers[].custom_verify` | string | 官方字段 `custom_verify`；官方未单独提供业务说明。 |
| `followers[].cv_level` | string | 官方字段 `cv_level`；官方未单独提供业务说明。 |
| `followers[].download_prompt_ts` | integer | 官方字段 `download_prompt_ts`；官方未单独提供业务说明。 |
| `followers[].download_setting` | integer | 官方字段 `download_setting`；官方未单独提供业务说明。 |
| `followers[].duet_setting` | integer | 官方字段 `duet_setting`；官方未单独提供业务说明。 |
| `followers[].enabled_filter_all_comments` | boolean | 官方字段 `enabled_filter_all_comments`；官方未单独提供业务说明。 |
| `followers[].enterprise_verify_reason` | string | 官方字段 `enterprise_verify_reason`；官方未单独提供业务说明。 |
| `followers[].events` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].fake_data_info` | object | 官方示例为空对象，未提供子字段。 |
| `followers[].favoriting_count` | integer | 官方字段 `favoriting_count`；官方未单独提供业务说明。 |
| `followers[].fb_expire_time` | integer | 官方字段 `fb_expire_time`；官方未单独提供业务说明。 |
| `followers[].follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `followers[].follower_count` | integer | 粉丝数量。 |
| `followers[].follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `followers[].followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].following_count` | integer | 关注数量。 |
| `followers[].friends_status` | integer | 官方字段 `friends_status`；官方未单独提供业务说明。 |
| `followers[].geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].google_account` | string | 官方字段 `google_account`；官方未单独提供业务说明。 |
| `followers[].has_email` | boolean | 官方字段 `has_email`；官方未单独提供业务说明。 |
| `followers[].has_facebook_token` | boolean | 官方字段 `has_facebook_token`；官方未单独提供业务说明。 |
| `followers[].has_insights` | boolean | 官方字段 `has_insights`；官方未单独提供业务说明。 |
| `followers[].has_orders` | boolean | 官方字段 `has_orders`；官方未单独提供业务说明。 |
| `followers[].has_twitter_token` | boolean | 官方字段 `has_twitter_token`；官方未单独提供业务说明。 |
| `followers[].has_youtube_token` | boolean | 官方字段 `has_youtube_token`；官方未单独提供业务说明。 |
| `followers[].hide_search` | boolean | 官方字段 `hide_search`；官方未单独提供业务说明。 |
| `followers[].homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].ins_id` | string | 官方字段 `ins_id`；官方未单独提供业务说明。 |
| `followers[].is_ad_fake` | boolean | 官方字段 `is_ad_fake`；官方未单独提供业务说明。 |
| `followers[].is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `followers[].is_discipline_member` | boolean | 官方字段 `is_discipline_member`；官方未单独提供业务说明。 |
| `followers[].is_mute` | integer | 官方字段 `is_mute`；官方未单独提供业务说明。 |
| `followers[].is_mute_lives` | integer | 官方字段 `is_mute_lives`；官方未单独提供业务说明。 |
| `followers[].is_mute_non_story_post` | integer | 官方字段 `is_mute_non_story_post`；官方未单独提供业务说明。 |
| `followers[].is_mute_story` | integer | 官方字段 `is_mute_story`；官方未单独提供业务说明。 |
| `followers[].is_phone_binded` | boolean | 官方字段 `is_phone_binded`；官方未单独提供业务说明。 |
| `followers[].is_star` | boolean | 官方字段 `is_star`；官方未单独提供业务说明。 |
| `followers[].item_list` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].language` | string | 语言。 |
| `followers[].live_agreement` | integer | 官方字段 `live_agreement`；官方未单独提供业务说明。 |
| `followers[].live_commerce` | boolean | 官方字段 `live_commerce`；官方未单独提供业务说明。 |
| `followers[].live_verify` | integer | 官方字段 `live_verify`；官方未单独提供业务说明。 |
| `followers[].mention_status` | integer | 官方字段 `mention_status`；官方未单独提供业务说明。 |
| `followers[].mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].need_points` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].need_recommend` | integer | 官方字段 `need_recommend`；官方未单独提供业务说明。 |
| `followers[].nickname` | string | 昵称。 |
| `followers[].original_musician` | object | 官方字段 `original_musician`；官方未单独提供业务说明。 |
| `followers[].original_musician.digg_count` | integer | 点赞数量。 |
| `followers[].original_musician.music_count` | integer | 官方字段 `music_count`；官方未单独提供业务说明。 |
| `followers[].original_musician.music_used_count` | integer | 官方字段 `music_used_count`；官方未单独提供业务说明。 |
| `followers[].original_musician.new_release_clip_ids` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `followers[].react_setting` | integer | 官方字段 `react_setting`；官方未单独提供业务说明。 |
| `followers[].region` | string | 地区。 |
| `followers[].relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].reply_with_video_flag` | integer | 官方字段 `reply_with_video_flag`；官方未单独提供业务说明。 |
| `followers[].room_id` | integer | 官方字段 `room_id`；官方未单独提供业务说明。 |
| `followers[].search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].sec_uid` | string | TikTok 安全用户标识。 |
| `followers[].secret` | integer | 官方字段 `secret`；官方未单独提供业务说明。 |
| `followers[].share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `followers[].share_info.now_invitation_card_image_urls` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].share_info.share_desc` | string | 官方字段 `share_desc`；官方未单独提供业务说明。 |
| `followers[].share_info.share_desc_info` | string | 官方字段 `share_desc_info`；官方未单独提供业务说明。 |
| `followers[].share_info.share_qrcode_url` | object | 官方字段 `share_qrcode_url`；官方未单独提供业务说明。 |
| `followers[].share_info.share_qrcode_url.height` | integer | 高度。 |
| `followers[].share_info.share_qrcode_url.uri` | string | 资源标识。 |
| `followers[].share_info.share_qrcode_url.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `followers[].share_info.share_qrcode_url.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].share_info.share_qrcode_url.width` | integer | 宽度。 |
| `followers[].share_info.share_title` | string | 官方字段 `share_title`；官方未单独提供业务说明。 |
| `followers[].share_info.share_title_myself` | string | 官方字段 `share_title_myself`；官方未单独提供业务说明。 |
| `followers[].share_info.share_title_other` | string | 官方字段 `share_title_other`；官方未单独提供业务说明。 |
| `followers[].share_info.share_url` | string | 官方字段 `share_url`；官方未单独提供业务说明。 |
| `followers[].share_qrcode_uri` | string | 官方字段 `share_qrcode_uri`；官方未单独提供业务说明。 |
| `followers[].shield_comment_notice` | integer | 官方字段 `shield_comment_notice`；官方未单独提供业务说明。 |
| `followers[].shield_digg_notice` | integer | 官方字段 `shield_digg_notice`；官方未单独提供业务说明。 |
| `followers[].shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].shield_follow_notice` | integer | 官方字段 `shield_follow_notice`；官方未单独提供业务说明。 |
| `followers[].short_id` | string | 官方字段 `short_id`；官方未单独提供业务说明。 |
| `followers[].show_image_bubble` | boolean | 官方字段 `show_image_bubble`；官方未单独提供业务说明。 |
| `followers[].signature` | string | 官方字段 `signature`；官方未单独提供业务说明。 |
| `followers[].special_account` | object | 官方字段 `special_account`；官方未单独提供业务说明。 |
| `followers[].special_account.special_account_list` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].special_lock` | integer | 官方字段 `special_lock`；官方未单独提供业务说明。 |
| `followers[].status` | integer | 状态。 |
| `followers[].stitch_setting` | integer | 官方字段 `stitch_setting`；官方未单独提供业务说明。 |
| `followers[].story_status` | integer | 官方字段 `story_status`；官方未单独提供业务说明。 |
| `followers[].total_favorited` | integer | 官方字段 `total_favorited`；官方未单独提供业务说明。 |
| `followers[].tw_expire_time` | integer | 官方字段 `tw_expire_time`；官方未单独提供业务说明。 |
| `followers[].twitter_id` | string | 官方字段 `twitter_id`；官方未单独提供业务说明。 |
| `followers[].twitter_name` | string | 官方字段 `twitter_name`；官方未单独提供业务说明。 |
| `followers[].type_label` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].uid` | string | 用户标识。 |
| `followers[].unique_id` | string | 账号唯一名称。 |
| `followers[].unique_id_modify_time` | integer | 官方字段 `unique_id_modify_time`；官方未单独提供业务说明。 |
| `followers[].user_canceled` | boolean | 官方字段 `user_canceled`；官方未单独提供业务说明。 |
| `followers[].user_mode` | integer | 官方字段 `user_mode`；官方未单独提供业务说明。 |
| `followers[].user_now_pack_info` | object | 官方示例为空对象，未提供子字段。 |
| `followers[].user_period` | integer | 官方字段 `user_period`；官方未单独提供业务说明。 |
| `followers[].user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].user_rate` | integer | 官方字段 `user_rate`；官方未单独提供业务说明。 |
| `followers[].user_spark_info` | object | 官方示例为空对象，未提供子字段。 |
| `followers[].user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].verification_type` | integer | 官方字段 `verification_type`；官方未单独提供业务说明。 |
| `followers[].verify_info` | string | 官方字段 `verify_info`；官方未单独提供业务说明。 |
| `followers[].video_icon` | object | 官方字段 `video_icon`；官方未单独提供业务说明。 |
| `followers[].video_icon.height` | integer | 高度。 |
| `followers[].video_icon.uri` | string | 资源标识。 |
| `followers[].video_icon.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `followers[].video_icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].video_icon.width` | integer | 宽度。 |
| `followers[].white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `followers[].with_commerce_entry` | boolean | 官方字段 `with_commerce_entry`；官方未单独提供业务说明。 |
| `followers[].with_shop_entry` | boolean | 官方字段 `with_shop_entry`；官方未单独提供业务说明。 |
| `followers[].youtube_channel_id` | string | 官方字段 `youtube_channel_id`；官方未单独提供业务说明。 |
| `followers[].youtube_channel_title` | string | 官方字段 `youtube_channel_title`；官方未单独提供业务说明。 |
| `followers[].youtube_expire_time` | integer | 官方字段 `youtube_expire_time`；官方未单独提供业务说明。 |
| `has_more` | boolean | 是否还有更多结果。 |
| `log_pb` | object | 官方字段 `log_pb`；官方未单独提供业务说明。 |
| `log_pb.impr_id` | string | 官方字段 `impr_id`；官方未单独提供业务说明。 |
| `max_time` | integer | 官方字段 `max_time`；官方未单独提供业务说明。 |
| `min_time` | integer | 分页时间标识。 |
| `myself_user_id` | string | 官方字段 `myself_user_id`；官方未单独提供业务说明。 |
| `next_page_token` | string | 官方字段 `next_page_token`；官方未单独提供业务说明。 |
| `offset` | integer | 官方字段 `offset`；官方未单独提供业务说明。 |
| `status_code` | integer | 状态码。 |
| `status_msg` | string | 状态说明。 |
| `total` | integer | 总数。 |

## 使用要点

- 每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-user-followers" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "gymshark", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/user/followers/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

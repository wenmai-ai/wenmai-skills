# Wenmai SCRAPECREATORS scrapecreators_tiktok_search_users API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-search-users`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_search_users`
- **脚本入口**：`modules/search-users/scripts/search_users.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `query` | string | 是 | 用户搜索词，可为昵称、用户名或关键词。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |
| `cursor` | number | 否 | 分页游标，传入上一页响应中的 cursor 以获取更多用户。 |

## 请求示例

```json
{
  "query": "gymshark",
  "trim": true
}
```

```bash
python3 modules/search-users/scripts/search_users.py '{"query": "gymshark", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `cursor` | integer | 分页游标。 |
| `users` | array | 用户列表。 |
| `users[].challenges` | null | 官方示例为 null，未说明非空类型。 |
| `users[].effects` | null | 官方示例为 null，未说明非空类型。 |
| `users[].items` | null | 官方示例为 null，未说明非空类型。 |
| `users[].mix_list` | null | 官方示例为 null，未说明非空类型。 |
| `users[].musics` | null | 官方示例为 null，未说明非空类型。 |
| `users[].position` | null | 官方示例为 null，未说明非空类型。 |
| `users[].uniqid_position` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info` | object | 官方字段 `user_info`；官方未单独提供业务说明。 |
| `users[].user_info.accept_private_policy` | boolean | 官方字段 `accept_private_policy`；官方未单独提供业务说明。 |
| `users[].user_info.account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.authority_status` | integer | 官方字段 `authority_status`；官方未单独提供业务说明。 |
| `users[].user_info.avatar_168x168` | object | 官方字段 `avatar_168x168`；官方未单独提供业务说明。 |
| `users[].user_info.avatar_168x168.height` | integer | 高度。 |
| `users[].user_info.avatar_168x168.uri` | string | 资源标识。 |
| `users[].user_info.avatar_168x168.url_list` | array | 资源链接列表。 |
| `users[].user_info.avatar_168x168.url_list[]` | string | 资源链接列表中的元素。 |
| `users[].user_info.avatar_168x168.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.avatar_168x168.width` | integer | 宽度。 |
| `users[].user_info.avatar_300x300` | object | 官方字段 `avatar_300x300`；官方未单独提供业务说明。 |
| `users[].user_info.avatar_300x300.height` | integer | 高度。 |
| `users[].user_info.avatar_300x300.uri` | string | 资源标识。 |
| `users[].user_info.avatar_300x300.url_list` | array | 资源链接列表。 |
| `users[].user_info.avatar_300x300.url_list[]` | string | 资源链接列表中的元素。 |
| `users[].user_info.avatar_300x300.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.avatar_300x300.width` | integer | 宽度。 |
| `users[].user_info.avatar_larger` | object | 官方字段 `avatar_larger`；官方未单独提供业务说明。 |
| `users[].user_info.avatar_larger.height` | integer | 高度。 |
| `users[].user_info.avatar_larger.uri` | string | 资源标识。 |
| `users[].user_info.avatar_larger.url_list` | array | 资源链接列表。 |
| `users[].user_info.avatar_larger.url_list[]` | string | 资源链接列表中的元素。 |
| `users[].user_info.avatar_larger.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.avatar_larger.width` | integer | 宽度。 |
| `users[].user_info.avatar_medium` | object | 中等尺寸头像。 |
| `users[].user_info.avatar_medium.height` | integer | 高度。 |
| `users[].user_info.avatar_medium.uri` | string | 资源标识。 |
| `users[].user_info.avatar_medium.url_list` | array | 资源链接列表。 |
| `users[].user_info.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `users[].user_info.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.avatar_medium.width` | integer | 宽度。 |
| `users[].user_info.avatar_thumb` | object | 缩略头像。 |
| `users[].user_info.avatar_thumb.height` | integer | 高度。 |
| `users[].user_info.avatar_thumb.uri` | string | 资源标识。 |
| `users[].user_info.avatar_thumb.url_list` | array | 资源链接列表。 |
| `users[].user_info.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `users[].user_info.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.avatar_thumb.width` | integer | 宽度。 |
| `users[].user_info.avatar_uri` | string | 官方字段 `avatar_uri`；官方未单独提供业务说明。 |
| `users[].user_info.aweme_count` | integer | 官方字段 `aweme_count`；官方未单独提供业务说明。 |
| `users[].user_info.block_status` | integer | 官方字段 `block_status`；官方未单独提供业务说明。 |
| `users[].user_info.bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.can_message_follow_status_list` | array | 官方字段 `can_message_follow_status_list`；官方未单独提供业务说明。 |
| `users[].user_info.can_message_follow_status_list[]` | integer | 官方数组 `can_message_follow_status_list` 的元素。 |
| `users[].user_info.can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.comment_filter_status` | integer | 官方字段 `comment_filter_status`；官方未单独提供业务说明。 |
| `users[].user_info.comment_setting` | integer | 官方字段 `comment_setting`；官方未单独提供业务说明。 |
| `users[].user_info.commerce_user_level` | integer | 官方字段 `commerce_user_level`；官方未单独提供业务说明。 |
| `users[].user_info.cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.custom_verify` | string | 官方字段 `custom_verify`；官方未单独提供业务说明。 |
| `users[].user_info.cv_level` | string | 官方字段 `cv_level`；官方未单独提供业务说明。 |
| `users[].user_info.download_prompt_ts` | integer | 官方字段 `download_prompt_ts`；官方未单独提供业务说明。 |
| `users[].user_info.enable_direct_message` | boolean | 官方字段 `enable_direct_message`；官方未单独提供业务说明。 |
| `users[].user_info.enabled_filter_all_comments` | boolean | 官方字段 `enabled_filter_all_comments`；官方未单独提供业务说明。 |
| `users[].user_info.enterprise_verify_reason` | string | 官方字段 `enterprise_verify_reason`；官方未单独提供业务说明。 |
| `users[].user_info.events` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.fake_data_info` | object | 官方示例为空对象，未提供子字段。 |
| `users[].user_info.fb_expire_time` | integer | 官方字段 `fb_expire_time`；官方未单独提供业务说明。 |
| `users[].user_info.follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `users[].user_info.follower_count` | integer | 粉丝数量。 |
| `users[].user_info.follower_status` | integer | 官方字段 `follower_status`；官方未单独提供业务说明。 |
| `users[].user_info.followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.following_count` | integer | 关注数量。 |
| `users[].user_info.friends_status` | integer | 官方字段 `friends_status`；官方未单独提供业务说明。 |
| `users[].user_info.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.hide_search` | boolean | 官方字段 `hide_search`；官方未单独提供业务说明。 |
| `users[].user_info.homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.ins_id` | string | 官方字段 `ins_id`；官方未单独提供业务说明。 |
| `users[].user_info.is_ad_fake` | boolean | 官方字段 `is_ad_fake`；官方未单独提供业务说明。 |
| `users[].user_info.is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `users[].user_info.is_discipline_member` | boolean | 官方字段 `is_discipline_member`；官方未单独提供业务说明。 |
| `users[].user_info.is_mute` | integer | 官方字段 `is_mute`；官方未单独提供业务说明。 |
| `users[].user_info.is_mute_lives` | integer | 官方字段 `is_mute_lives`；官方未单独提供业务说明。 |
| `users[].user_info.is_mute_non_story_post` | integer | 官方字段 `is_mute_non_story_post`；官方未单独提供业务说明。 |
| `users[].user_info.is_mute_story` | integer | 官方字段 `is_mute_story`；官方未单独提供业务说明。 |
| `users[].user_info.is_private_account` | integer | 官方字段 `is_private_account`；官方未单独提供业务说明。 |
| `users[].user_info.is_star` | boolean | 官方字段 `is_star`；官方未单独提供业务说明。 |
| `users[].user_info.item_list` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.live_agreement` | integer | 官方字段 `live_agreement`；官方未单独提供业务说明。 |
| `users[].user_info.live_commerce` | boolean | 官方字段 `live_commerce`；官方未单独提供业务说明。 |
| `users[].user_info.live_verify` | integer | 官方字段 `live_verify`；官方未单独提供业务说明。 |
| `users[].user_info.mention_status` | integer | 官方字段 `mention_status`；官方未单独提供业务说明。 |
| `users[].user_info.mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.name_field` | string | 官方字段 `name_field`；官方未单独提供业务说明。 |
| `users[].user_info.need_points` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.need_recommend` | integer | 官方字段 `need_recommend`；官方未单独提供业务说明。 |
| `users[].user_info.nickname` | string | 昵称。 |
| `users[].user_info.original_musician` | object | 官方字段 `original_musician`；官方未单独提供业务说明。 |
| `users[].user_info.original_musician.digg_count` | integer | 点赞数量。 |
| `users[].user_info.original_musician.music_count` | integer | 官方字段 `music_count`；官方未单独提供业务说明。 |
| `users[].user_info.original_musician.music_used_count` | integer | 官方字段 `music_used_count`；官方未单独提供业务说明。 |
| `users[].user_info.original_musician.new_release_clip_ids` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.prevent_download` | boolean | 官方字段 `prevent_download`；官方未单独提供业务说明。 |
| `users[].user_info.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.reply_with_video_flag` | integer | 官方字段 `reply_with_video_flag`；官方未单独提供业务说明。 |
| `users[].user_info.room_id` | integer | 官方字段 `room_id`；官方未单独提供业务说明。 |
| `users[].user_info.room_id_str` | string | 官方字段 `room_id_str`；官方未单独提供业务说明。 |
| `users[].user_info.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.search_user_desc` | string | 官方字段 `search_user_desc`；官方未单独提供业务说明。 |
| `users[].user_info.search_user_name` | string | 官方字段 `search_user_name`；官方未单独提供业务说明。 |
| `users[].user_info.sec_uid` | string | TikTok 安全用户标识。 |
| `users[].user_info.secret` | integer | 官方字段 `secret`；官方未单独提供业务说明。 |
| `users[].user_info.shield_comment_notice` | integer | 官方字段 `shield_comment_notice`；官方未单独提供业务说明。 |
| `users[].user_info.shield_digg_notice` | integer | 官方字段 `shield_digg_notice`；官方未单独提供业务说明。 |
| `users[].user_info.shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.shield_follow_notice` | integer | 官方字段 `shield_follow_notice`；官方未单独提供业务说明。 |
| `users[].user_info.short_id` | string | 官方字段 `short_id`；官方未单独提供业务说明。 |
| `users[].user_info.show_image_bubble` | boolean | 官方字段 `show_image_bubble`；官方未单独提供业务说明。 |
| `users[].user_info.special_account` | object | 官方字段 `special_account`；官方未单独提供业务说明。 |
| `users[].user_info.special_account.special_account_list` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.special_lock` | integer | 官方字段 `special_lock`；官方未单独提供业务说明。 |
| `users[].user_info.status` | integer | 状态。 |
| `users[].user_info.stitch_setting` | integer | 官方字段 `stitch_setting`；官方未单独提供业务说明。 |
| `users[].user_info.story_status` | integer | 官方字段 `story_status`；官方未单独提供业务说明。 |
| `users[].user_info.total_favorited` | integer | 官方字段 `total_favorited`；官方未单独提供业务说明。 |
| `users[].user_info.type_label` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.uid` | string | 用户标识。 |
| `users[].user_info.unique_id` | string | 账号唯一名称。 |
| `users[].user_info.user_canceled` | boolean | 官方字段 `user_canceled`；官方未单独提供业务说明。 |
| `users[].user_info.user_mode` | integer | 官方字段 `user_mode`；官方未单独提供业务说明。 |
| `users[].user_info.user_now_pack_info` | object | 官方示例为空对象，未提供子字段。 |
| `users[].user_info.user_period` | integer | 官方字段 `user_period`；官方未单独提供业务说明。 |
| `users[].user_info.user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.user_rate` | integer | 官方字段 `user_rate`；官方未单独提供业务说明。 |
| `users[].user_info.user_spark_info` | object | 官方示例为空对象，未提供子字段。 |
| `users[].user_info.user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.verification_type` | integer | 官方字段 `verification_type`；官方未单独提供业务说明。 |
| `users[].user_info.verify_info` | string | 官方字段 `verify_info`；官方未单独提供业务说明。 |
| `users[].user_info.video_icon` | object | 官方字段 `video_icon`；官方未单独提供业务说明。 |
| `users[].user_info.video_icon.height` | integer | 高度。 |
| `users[].user_info.video_icon.uri` | string | 资源标识。 |
| `users[].user_info.video_icon.url_list` | array | 官方示例为空数组，未提供元素结构。 |
| `users[].user_info.video_icon.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.video_icon.width` | integer | 宽度。 |
| `users[].user_info.white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `users[].user_info.with_commerce_entry` | boolean | 官方字段 `with_commerce_entry`；官方未单独提供业务说明。 |
| `users[].follower_count` | integer | 粉丝数量。 |
| `users[].following_count` | integer | 关注数量。 |
| `users[].nickname` | string | 昵称。 |
| `users[].sec_uid` | string | TikTok 安全用户标识。 |
| `users[].uid` | string | 用户标识。 |
| `users[].unique_id` | string | 账号唯一名称。 |
| `users[].avatar_medium` | object | 中等尺寸头像。 |
| `users[].avatar_medium.height` | integer | 高度。 |
| `users[].avatar_medium.uri` | string | 资源标识。 |
| `users[].avatar_medium.url_list` | array | 资源链接列表。 |
| `users[].avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `users[].avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `users[].avatar_medium.width` | integer | 宽度。 |

## 使用要点

- 按昵称或用户名搜达人。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-search-users" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "gymshark", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/search/users/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

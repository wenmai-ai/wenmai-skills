# Wenmai SCRAPECREATORS scrapecreators_instagram_post API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-post`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_instagram_post`
- **脚本入口**：`modules/post/scripts/post.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | Instagram 帖子或 Reels 链接。 |
| `region` | string | 否 | 两位国家码，用于把代理放到该地区。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |
| `download_media` | boolean | 否 | 是否下载视频/图片并返回长期地址。找到媒体时官方收 10 credit，否则仍为 1。不要当默认。 |
| `include_play_count` | boolean | 否 | 是否额外拉取 video_play_count。默认 true；false 会更快。 |
| `cache_max_age` | string | 否 | 若缓存中有不晚于该时效的数据则直接返回，官方不计 credit。 可选值：1d、3d、7d、14d、30d。 |

## 请求示例

```json
{
  "url": "https://www.instagram.com/p/Df5MwAKiCVI/",
  "trim": true
}
```

```bash
python3 modules/post/scripts/post.py '{"url": "https://www.instagram.com/p/Df5MwAKiCVI/", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `data` | object | 官方响应中的内层业务数据。 |
| `data.xdt_shortcode_media` | object | 官方字段 `xdt_shortcode_media`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.__isXDTGraphMediaInterface` | string | 官方字段 `__isXDTGraphMediaInterface`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.id` | string | 标识符。 |
| `data.xdt_shortcode_media.shortcode` | string | 官方字段 `shortcode`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.thumbnail_src` | string | 官方字段 `thumbnail_src`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.dimensions` | object | 官方字段 `dimensions`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.dimensions.height` | integer | 高度。 |
| `data.xdt_shortcode_media.dimensions.width` | integer | 宽度。 |
| `data.xdt_shortcode_media.gating_info` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.fact_check_overall_rating` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.fact_check_information` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.sensitivity_friction_info` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.sharing_friction_info` | object | 官方字段 `sharing_friction_info`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.sharing_friction_info.should_have_sharing_friction` | boolean | 官方字段 `should_have_sharing_friction`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.sharing_friction_info.bloks_app_url` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.media_overlay_info` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.media_preview` | string | 官方字段 `media_preview`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.display_resources` | array | 官方字段 `display_resources`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.display_resources[].src` | string | 官方字段 `src`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.display_resources[].config_width` | integer | 官方字段 `config_width`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.display_resources[].config_height` | integer | 官方字段 `config_height`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.accessibility_caption` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.has_audio` | boolean | 官方字段 `has_audio`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.video_url` | string | 官方字段 `video_url`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.video_view_count` | integer | 官方字段 `video_view_count`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.video_play_count` | integer | 官方字段 `video_play_count`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.encoding_status` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.is_published` | boolean | 官方字段 `is_published`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.product_type` | string | 官方字段 `product_type`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.title` | string | 标题。 |
| `data.xdt_shortcode_media.video_duration` | number | 视频时长。 |
| `data.xdt_shortcode_media.clips_music_attribution_info` | object | 官方字段 `clips_music_attribution_info`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.clips_music_attribution_info.artist_name` | string | 官方字段 `artist_name`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.clips_music_attribution_info.song_name` | string | 官方字段 `song_name`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.clips_music_attribution_info.uses_original_audio` | boolean | 官方字段 `uses_original_audio`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.clips_music_attribution_info.should_mute_audio` | boolean | 官方字段 `should_mute_audio`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.clips_music_attribution_info.should_mute_audio_reason` | string | 官方字段 `should_mute_audio_reason`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.clips_music_attribution_info.audio_id` | string | 官方字段 `audio_id`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.is_video` | boolean | 官方字段 `is_video`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.tracking_token` | string | 官方字段 `tracking_token`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.upcoming_event` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.edge_media_to_tagged_user` | object | 官方字段 `edge_media_to_tagged_user`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_tagged_user.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.xdt_shortcode_media.owner` | object | 所属账号。 |
| `data.xdt_shortcode_media.owner.id` | string | 标识符。 |
| `data.xdt_shortcode_media.owner.username` | string | 用户名。 |
| `data.xdt_shortcode_media.owner.is_verified` | boolean | 是否认证。 |
| `data.xdt_shortcode_media.owner.profile_pic_url` | string | 头像链接。 |
| `data.xdt_shortcode_media.owner.blocked_by_viewer` | boolean | 官方字段 `blocked_by_viewer`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.owner.restricted_by_viewer` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.owner.followed_by_viewer` | boolean | 官方字段 `followed_by_viewer`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.owner.full_name` | string | 完整名称。 |
| `data.xdt_shortcode_media.owner.has_blocked_viewer` | boolean | 官方字段 `has_blocked_viewer`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.owner.is_embeds_disabled` | boolean | 官方字段 `is_embeds_disabled`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.owner.is_private` | boolean | 是否为私密账号。 |
| `data.xdt_shortcode_media.owner.is_unpublished` | boolean | 官方字段 `is_unpublished`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.owner.requested_by_viewer` | boolean | 官方字段 `requested_by_viewer`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.owner.pass_tiering_recommendation` | boolean | 官方字段 `pass_tiering_recommendation`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.owner.edge_owner_to_timeline_media` | object | 官方字段 `edge_owner_to_timeline_media`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.owner.edge_owner_to_timeline_media.count` | integer | 数量。 |
| `data.xdt_shortcode_media.owner.edge_followed_by` | object | 官方字段 `edge_followed_by`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.owner.edge_followed_by.count` | integer | 数量。 |
| `data.xdt_shortcode_media.edge_media_to_caption` | object | 官方字段 `edge_media_to_caption`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_caption.edges` | array | 关联数据条目。 |
| `data.xdt_shortcode_media.edge_media_to_caption.edges[].node` | object | 关联数据节点。 |
| `data.xdt_shortcode_media.edge_media_to_caption.edges[].node.created_at` | string | 创建时间。 |
| `data.xdt_shortcode_media.edge_media_to_caption.edges[].node.text` | string | 文本内容。 |
| `data.xdt_shortcode_media.edge_media_to_caption.edges[].node.id` | string | 标识符。 |
| `data.xdt_shortcode_media.can_see_insights_as_brand` | boolean | 官方字段 `can_see_insights_as_brand`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.caption_is_edited` | boolean | 官方字段 `caption_is_edited`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.has_ranked_comments` | boolean | 官方字段 `has_ranked_comments`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.like_and_view_counts_disabled` | boolean | 官方字段 `like_and_view_counts_disabled`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment` | object | 官方字段 `edge_media_to_parent_comment`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.count` | integer | 数量。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.page_info` | object | 官方字段 `page_info`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.page_info.has_next_page` | boolean | 是否存在下一页。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.page_info.end_cursor` | string | 官方字段 `end_cursor`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges` | array | 关联数据条目。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node` | object | 关联数据节点。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.id` | string | 标识符。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.text` | string | 文本内容。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.created_at` | integer | 创建时间。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.did_report_as_spam` | boolean | 官方字段 `did_report_as_spam`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.owner` | object | 所属账号。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.owner.id` | string | 标识符。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.owner.is_verified` | boolean | 是否认证。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.owner.profile_pic_url` | string | 头像链接。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.owner.username` | string | 用户名。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.viewer_has_liked` | boolean | 官方字段 `viewer_has_liked`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.edge_liked_by` | object | 官方字段 `edge_liked_by`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.edge_liked_by.count` | integer | 数量。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.is_restricted_pending` | boolean | 官方字段 `is_restricted_pending`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.edge_threaded_comments` | object | 官方字段 `edge_threaded_comments`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.edge_threaded_comments.count` | integer | 数量。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.edge_threaded_comments.page_info` | object | 官方字段 `page_info`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.edge_threaded_comments.page_info.has_next_page` | boolean | 是否存在下一页。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.edge_threaded_comments.page_info.end_cursor` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.edge_media_to_parent_comment.edges[].node.edge_threaded_comments.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.xdt_shortcode_media.edge_media_to_hoisted_comment` | object | 官方字段 `edge_media_to_hoisted_comment`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_hoisted_comment.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.xdt_shortcode_media.edge_media_preview_comment` | object | 官方字段 `edge_media_preview_comment`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.count` | integer | 数量。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges` | array | 关联数据条目。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node` | object | 关联数据节点。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.id` | string | 标识符。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.text` | string | 文本内容。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.created_at` | integer | 创建时间。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.did_report_as_spam` | boolean | 官方字段 `did_report_as_spam`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.owner` | object | 所属账号。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.owner.id` | string | 标识符。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.owner.is_verified` | boolean | 是否认证。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.owner.profile_pic_url` | string | 头像链接。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.owner.username` | string | 用户名。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.viewer_has_liked` | boolean | 官方字段 `viewer_has_liked`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.edge_liked_by` | object | 官方字段 `edge_liked_by`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.edge_liked_by.count` | integer | 数量。 |
| `data.xdt_shortcode_media.edge_media_preview_comment.edges[].node.is_restricted_pending` | boolean | 官方字段 `is_restricted_pending`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.comments_disabled` | boolean | 官方字段 `comments_disabled`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.commenting_disabled_for_viewer` | boolean | 官方字段 `commenting_disabled_for_viewer`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.created_at` | string | 创建时间。 |
| `data.xdt_shortcode_media.taken_at_timestamp` | integer | 官方字段 `taken_at_timestamp`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_preview_like` | object | 官方字段 `edge_media_preview_like`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_preview_like.count` | integer | 数量。 |
| `data.xdt_shortcode_media.edge_media_preview_like.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.xdt_shortcode_media.edge_media_to_sponsor_user` | object | 官方字段 `edge_media_to_sponsor_user`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_media_to_sponsor_user.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.xdt_shortcode_media.is_affiliate` | boolean | 官方字段 `is_affiliate`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.is_paid_partnership` | boolean | 是否为付费合作内容。 |
| `data.xdt_shortcode_media.location` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.nft_asset_info` | null | 官方示例为 null，未说明非空类型。 |
| `data.xdt_shortcode_media.viewer_has_liked` | boolean | 官方字段 `viewer_has_liked`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.viewer_has_saved` | boolean | 官方字段 `viewer_has_saved`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.viewer_has_saved_to_collection` | boolean | 官方字段 `viewer_has_saved_to_collection`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.viewer_in_photo_of_you` | boolean | 官方字段 `viewer_in_photo_of_you`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.viewer_can_reshare` | boolean | 官方字段 `viewer_can_reshare`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.is_ad` | boolean | 官方字段 `is_ad`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_web_media_to_related_media` | object | 官方字段 `edge_web_media_to_related_media`；官方未单独提供业务说明。 |
| `data.xdt_shortcode_media.edge_web_media_to_related_media.edges` | array | 官方示例为空数组，未提供元素结构。 |
| `data.xdt_shortcode_media.coauthor_producers` | array | 官方示例为空数组，未提供元素结构。 |
| `data.xdt_shortcode_media.pinned_for_users` | array | 官方示例为空数组，未提供元素结构。 |
| `extensions` | object | 官方字段 `extensions`；官方未单独提供业务说明。 |
| `extensions.is_final` | boolean | 官方字段 `is_final`；官方未单独提供业务说明。 |
| `status` | string | 状态。 |

## 使用要点

- 不要默认 download_media=true。响应顶层是 xdt_shortcode_media，不是 data。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-post" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/p/Df5MwAKiCVI/", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/instagram/post/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

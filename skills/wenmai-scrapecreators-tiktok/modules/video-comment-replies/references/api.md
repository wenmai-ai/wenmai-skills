# Wenmai SCRAPECREATORS scrapecreators_tiktok_video_comment_replies API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-video-comment-replies`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_video_comment_replies`
- **脚本入口**：`modules/video-comment-replies/scripts/video_comment_replies.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `comment_id` | string | 是 | 评论 ID，即评论接口返回的 cid。trim=true 的评论结果里没有该字段。 |
| `url` | string | 是 | 对应视频链接，与评论接口使用的 url 相同。 |
| `cursor` | number | 否 | 分页游标，传入上一页响应中的 cursor 以获取更多回复。 |

## 请求示例

```json
{
  "url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335",
  "comment_id": "7703257909974549279"
}
```

```bash
python3 modules/video-comment-replies/scripts/video_comment_replies.py '{"url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335", "comment_id": "7703257909974549279"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `comments` | array | 评论列表。 |
| `comments[].aweme_id` | string | TikTok 视频标识。 |
| `comments[].cid` | string | 官方字段 `cid`；官方未单独提供业务说明。 |
| `comments[].collect_stat` | integer | 官方字段 `collect_stat`；官方未单独提供业务说明。 |
| `comments[].comment_language` | string | 官方字段 `comment_language`；官方未单独提供业务说明。 |
| `comments[].comment_post_item_ids` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].create_time` | integer | 创建时间。 |
| `comments[].digg_count` | integer | 点赞数量。 |
| `comments[].fold_status` | integer | 官方字段 `fold_status`；官方未单独提供业务说明。 |
| `comments[].image_list` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].is_author_digged` | boolean | 官方字段 `is_author_digged`；官方未单独提供业务说明。 |
| `comments[].is_comment_translatable` | boolean | 官方字段 `is_comment_translatable`；官方未单独提供业务说明。 |
| `comments[].is_high_purchase_intent` | boolean | 官方字段 `is_high_purchase_intent`；官方未单独提供业务说明。 |
| `comments[].label_list` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].no_show` | boolean | 官方字段 `no_show`；官方未单独提供业务说明。 |
| `comments[].reply_comment` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].reply_id` | string | 官方字段 `reply_id`；官方未单独提供业务说明。 |
| `comments[].reply_to_reply_id` | string | 官方字段 `reply_to_reply_id`；官方未单独提供业务说明。 |
| `comments[].share_info` | object | 官方字段 `share_info`；官方未单独提供业务说明。 |
| `comments[].share_info.acl` | object | 官方字段 `acl`；官方未单独提供业务说明。 |
| `comments[].share_info.acl.code` | integer | 官方业务编码。 |
| `comments[].share_info.acl.extra` | string | 官方字段 `extra`；官方未单独提供业务说明。 |
| `comments[].share_info.desc` | string | 描述。 |
| `comments[].share_info.title` | string | 标题。 |
| `comments[].share_info.url` | string | 链接。 |
| `comments[].status` | integer | 状态。 |
| `comments[].stick_position` | integer | 官方字段 `stick_position`；官方未单独提供业务说明。 |
| `comments[].text` | string | 文本内容。 |
| `comments[].text_extra` | array | 官方示例为空数组，未提供元素结构。 |
| `comments[].thread_has_more` | boolean | 官方字段 `thread_has_more`；官方未单独提供业务说明。 |
| `comments[].thread_id` | integer | 官方字段 `thread_id`；官方未单独提供业务说明。 |
| `comments[].trans_btn_style` | integer | 官方字段 `trans_btn_style`；官方未单独提供业务说明。 |
| `comments[].user` | object | 用户信息。 |
| `comments[].user.account_labels` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.ad_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.advance_feature_item_order` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.advanced_feature_info` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.avatar_thumb` | object | 缩略头像。 |
| `comments[].user.avatar_thumb.uri` | string | 资源标识。 |
| `comments[].user.avatar_thumb.url_list` | array | 资源链接列表。 |
| `comments[].user.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `comments[].user.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.bold_fields` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.can_message_follow_status_list` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.can_set_geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.cha_list` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.custom_verify` | string | 官方字段 `custom_verify`；官方未单独提供业务说明。 |
| `comments[].user.enterprise_verify_reason` | string | 官方字段 `enterprise_verify_reason`；官方未单独提供业务说明。 |
| `comments[].user.events` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.followers_detail` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.geofencing` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.homepage_bottom_toast` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.item_list` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.mutual_relation_avatars` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.need_points` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.nickname` | string | 昵称。 |
| `comments[].user.platform_sync_info` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.predicted_age_group` | string | 官方字段 `predicted_age_group`；官方未单独提供业务说明。 |
| `comments[].user.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.search_highlight` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.sec_uid` | string | TikTok 安全用户标识。 |
| `comments[].user.shield_edit_field_info` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.type_label` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.uid` | string | 用户标识。 |
| `comments[].user.unique_id` | string | 账号唯一名称。 |
| `comments[].user.user_profile_guide` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.user_tags` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user.white_cover_url` | null | 官方示例为 null，未说明非空类型。 |
| `comments[].user_buried` | boolean | 官方字段 `user_buried`；官方未单独提供业务说明。 |
| `comments[].user_digged` | integer | 官方字段 `user_digged`；官方未单独提供业务说明。 |
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
| `total` | integer | 总数。 |

## 使用要点

- comment_id 必须来自未 trim 的评论结果 cid。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-video-comment-replies" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335", "comment_id": "7703257909974549279"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/video/comment/replies/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

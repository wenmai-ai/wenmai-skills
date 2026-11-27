# Wenmai SCRAPECREATORS scrapecreators_instagram_highlight_detail API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-highlight-detail`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_instagram_highlight_detail`
- **脚本入口**：`modules/highlight-detail/scripts/highlight_detail.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `id` | string | 否 | 故事精选 ID，来自精选列表接口返回的 id。 |

## 请求示例

```json
{
  "id": "18125552704906006"
}
```

```bash
python3 modules/highlight-detail/scripts/highlight_detail.py '{"id": "18125552704906006"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `can_reshare` | boolean | 官方字段 `can_reshare`；官方未单独提供业务说明。 |
| `cover_media` | object | 官方字段 `cover_media`；官方未单独提供业务说明。 |
| `cover_media.cropped_image_version` | object | 官方字段 `cropped_image_version`；官方未单独提供业务说明。 |
| `cover_media.cropped_image_version.url` | string | 链接。 |
| `cover_media.full_image_version` | null | 官方示例为 null，未说明非空类型。 |
| `id` | string | 标识符。 |
| `is_fit_green` | boolean | 官方字段 `is_fit_green`；官方未单独提供业务说明。 |
| `items` | array | 结果条目。 |
| `items[].boost_unavailable_identifier` | null | 官方示例为 null，未说明非空类型。 |
| `items[].boost_unavailable_reason` | null | 官方示例为 null，未说明非空类型。 |
| `items[].can_reply` | boolean | 官方字段 `can_reply`；官方未单独提供业务说明。 |
| `items[].can_reshare` | boolean | 官方字段 `can_reshare`；官方未单独提供业务说明。 |
| `items[].can_see_insights_as_brand` | boolean | 官方字段 `can_see_insights_as_brand`；官方未单独提供业务说明。 |
| `items[].caption` | null | 官方示例为 null，未说明非空类型。 |
| `items[].code` | string | 官方业务编码。 |
| `items[].has_audio` | boolean\|null | 官方字段 `has_audio`；官方未单独提供业务说明。 |
| `items[].has_translation` | boolean | 官方字段 `has_translation`；官方未单独提供业务说明。 |
| `items[].id` | string | 标识符。 |
| `items[].ig_media_sharing_disabled` | boolean | 官方字段 `ig_media_sharing_disabled`；官方未单独提供业务说明。 |
| `items[].image_versions2` | object | 官方字段 `image_versions2`；官方未单独提供业务说明。 |
| `items[].image_versions2.candidates` | array | 官方字段 `candidates`；官方未单独提供业务说明。 |
| `items[].image_versions2.candidates[].height` | integer | 高度。 |
| `items[].image_versions2.candidates[].url` | string | 链接。 |
| `items[].image_versions2.candidates[].width` | integer | 宽度。 |
| `items[].is_dash_eligible` | integer\|null | 官方字段 `is_dash_eligible`；官方未单独提供业务说明。 |
| `items[].is_paid_partnership` | boolean | 是否为付费合作内容。 |
| `items[].is_story_edited` | boolean | 官方字段 `is_story_edited`；官方未单独提供业务说明。 |
| `items[].media_overlay_info` | null | 官方示例为 null，未说明非空类型。 |
| `items[].media_type` | integer | 官方字段 `media_type`；官方未单独提供业务说明。 |
| `items[].number_of_qualities` | integer\|null | 官方字段 `number_of_qualities`；官方未单独提供业务说明。 |
| `items[].original_height` | integer | 官方字段 `original_height`；官方未单独提供业务说明。 |
| `items[].original_width` | integer | 官方字段 `original_width`；官方未单独提供业务说明。 |
| `items[].pk` | string | 主键标识。 |
| `items[].product_type` | string | 官方字段 `product_type`；官方未单独提供业务说明。 |
| `items[].sharing_friction_info` | object | 官方字段 `sharing_friction_info`；官方未单独提供业务说明。 |
| `items[].sharing_friction_info.bloks_app_url` | null | 官方示例为 null，未说明非空类型。 |
| `items[].sharing_friction_info.should_have_sharing_friction` | boolean | 官方字段 `should_have_sharing_friction`；官方未单独提供业务说明。 |
| `items[].story_link_stickers` | array\|null | 官方字段 `story_link_stickers`；官方未单独提供业务说明。 |
| `items[].taken_at` | integer | 官方字段 `taken_at`；官方未单独提供业务说明。 |
| `items[].user` | object | 用户信息。 |
| `items[].user.id` | string | 标识符。 |
| `items[].user.is_private` | boolean | 是否为私密账号。 |
| `items[].user.is_verified` | boolean | 是否认证。 |
| `items[].user.pk` | string | 主键标识。 |
| `items[].user.profile_pic_url` | string | 头像链接。 |
| `items[].user.username` | string | 用户名。 |
| `items[].video_duration` | null\|number | 视频时长。 |
| `items[].video_versions` | array\|null | 官方字段 `video_versions`；官方未单独提供业务说明。 |
| `items[].video_versions[].type` | integer | 类型。 |
| `items[].video_versions[].url` | string | 链接。 |
| `items[].story_link_stickers[].height` | number | 高度。 |
| `items[].story_link_stickers[].id` | string | 标识符。 |
| `items[].story_link_stickers[].rotation` | integer | 官方字段 `rotation`；官方未单独提供业务说明。 |
| `items[].story_link_stickers[].story_link` | object | 官方字段 `story_link`；官方未单独提供业务说明。 |
| `items[].story_link_stickers[].story_link.url` | string | 链接。 |
| `items[].story_link_stickers[].width` | number | 宽度。 |
| `items[].story_link_stickers[].x` | number | 官方字段 `x`；官方未单独提供业务说明。 |
| `items[].story_link_stickers[].y` | number | 官方字段 `y`；官方未单独提供业务说明。 |
| `latest_reel_media` | integer | 官方字段 `latest_reel_media`；官方未单独提供业务说明。 |
| `reel_type` | string | 官方字段 `reel_type`；官方未单独提供业务说明。 |
| `seen` | null | 官方示例为 null，未说明非空类型。 |
| `title` | string | 标题。 |
| `user` | object | 用户信息。 |
| `user.id` | string | 标识符。 |
| `user.interop_messaging_user_fbid` | string | 官方字段 `interop_messaging_user_fbid`；官方未单独提供业务说明。 |
| `user.is_private` | boolean | 是否为私密账号。 |
| `user.is_verified` | boolean | 是否认证。 |
| `user.pk` | string | 主键标识。 |
| `user.profile_pic_url` | string | 头像链接。 |
| `user.transparency_product_enabled` | boolean | 官方字段 `transparency_product_enabled`；官方未单独提供业务说明。 |
| `user.username` | string | 用户名。 |

## 使用要点

- id 来自 user-highlights。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-highlight-detail" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "18125552704906006"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/instagram/user/highlight/detail/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

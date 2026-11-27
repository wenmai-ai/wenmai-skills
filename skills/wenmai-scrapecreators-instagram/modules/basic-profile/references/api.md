# Wenmai SCRAPECREATORS scrapecreators_instagram_basic_profile API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-basic-profile`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_instagram_basic_profile`
- **脚本入口**：`modules/basic-profile/scripts/basic_profile.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `userId` | string | 否 | Instagram 数字用户 ID。官方用它做快速查询，不含帖子列表。 |
| `cache_max_age` | string | 否 | 若缓存中有不晚于该时效的数据则直接返回，官方不计 credit。 可选值：1d、3d、7d、14d、30d。 |

## 请求示例

```json
{
  "userId": "390927249"
}
```

```bash
python3 modules/basic-profile/scripts/basic_profile.py '{"userId": "390927249"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `friendship_status` | null | 官方示例为 null，未说明非空类型。 |
| `gating` | null | 官方示例为 null，未说明非空类型。 |
| `is_memorialized` | boolean | 官方字段 `is_memorialized`；官方未单独提供业务说明。 |
| `is_private` | boolean | 是否为私密账号。 |
| `has_story_archive` | null | 官方示例为 null，未说明非空类型。 |
| `supervision_info` | null | 官方示例为 null，未说明非空类型。 |
| `is_regulated_c18` | boolean | 官方字段 `is_regulated_c18`；官方未单独提供业务说明。 |
| `regulated_news_in_locations` | array | 官方示例为空数组，未提供元素结构。 |
| `bio_links` | array | 官方示例为空数组，未提供元素结构。 |
| `linked_fb_info` | null | 官方示例为 null，未说明非空类型。 |
| `text_post_app_badge_label` | string | 官方字段 `text_post_app_badge_label`；官方未单独提供业务说明。 |
| `show_text_post_app_badge` | boolean | 官方字段 `show_text_post_app_badge`；官方未单独提供业务说明。 |
| `username` | string | 用户名。 |
| `text_post_new_post_count` | null | 官方示例为 null，未说明非空类型。 |
| `pk` | string | 主键标识。 |
| `live_broadcast_visibility` | null | 官方示例为 null，未说明非空类型。 |
| `live_broadcast_id` | null | 官方示例为 null，未说明非空类型。 |
| `profile_pic_url` | string | 头像链接。 |
| `hd_profile_pic_url_info` | object | 官方字段 `hd_profile_pic_url_info`；官方未单独提供业务说明。 |
| `hd_profile_pic_url_info.url` | string | 链接。 |
| `is_unpublished` | boolean | 官方字段 `is_unpublished`；官方未单独提供业务说明。 |
| `latest_reel_media` | integer | 官方字段 `latest_reel_media`；官方未单独提供业务说明。 |
| `has_profile_pic` | null | 官方示例为 null，未说明非空类型。 |
| `profile_pic_genai_tool_info` | array | 官方示例为空数组，未提供元素结构。 |
| `biography` | string | 官方字段 `biography`；官方未单独提供业务说明。 |
| `full_name` | string | 完整名称。 |
| `is_verified` | boolean | 是否认证。 |
| `show_account_transparency_details` | boolean | 官方字段 `show_account_transparency_details`；官方未单独提供业务说明。 |
| `account_type` | integer | 官方字段 `account_type`；官方未单独提供业务说明。 |
| `follower_count` | integer | 粉丝数量。 |
| `mutual_followers_count` | null | 官方示例为 null，未说明非空类型。 |
| `profile_context_links_with_user_ids` | null | 官方示例为 null，未说明非空类型。 |
| `address_street` | null | 官方示例为 null，未说明非空类型。 |
| `city_name` | null | 官方示例为 null，未说明非空类型。 |
| `is_business` | boolean | 官方字段 `is_business`；官方未单独提供业务说明。 |
| `zip` | null | 官方示例为 null，未说明非空类型。 |
| `biography_with_entities` | object | 官方字段 `biography_with_entities`；官方未单独提供业务说明。 |
| `biography_with_entities.entities` | array | 官方示例为空数组，未提供元素结构。 |
| `category` | null | 官方示例为 null，未说明非空类型。 |
| `should_show_category` | boolean | 官方字段 `should_show_category`；官方未单独提供业务说明。 |
| `account_badges` | array | 官方示例为空数组，未提供元素结构。 |
| `ai_agent_type` | null | 官方示例为 null，未说明非空类型。 |
| `external_lynx_url` | null | 官方示例为 null，未说明非空类型。 |
| `external_url` | string | 官方字段 `external_url`；官方未单独提供业务说明。 |
| `pronouns` | array | 官方示例为空数组，未提供元素结构。 |
| `transparency_label` | null | 官方示例为 null，未说明非空类型。 |
| `transparency_product` | null | 官方示例为 null，未说明非空类型。 |
| `has_chaining` | null | 官方示例为 null，未说明非空类型。 |
| `remove_message_entrypoint` | null | 官方示例为 null，未说明非空类型。 |
| `fbid_v2` | string | 官方字段 `fbid_v2`；官方未单独提供业务说明。 |
| `is_embeds_disabled` | boolean | 官方字段 `is_embeds_disabled`；官方未单独提供业务说明。 |
| `is_professional_account` | null | 官方示例为 null，未说明非空类型。 |
| `following_count` | integer | 关注数量。 |
| `media_count` | integer | 官方字段 `media_count`；官方未单独提供业务说明。 |
| `total_clips_count` | integer | 官方字段 `total_clips_count`；官方未单独提供业务说明。 |
| `latest_besties_reel_media` | null | 官方示例为 null，未说明非空类型。 |
| `reel_media_seen_timestamp` | null | 官方示例为 null，未说明非空类型。 |
| `id` | string | 标识符。 |

## 使用要点

- 不含帖子，通常更快。优先传 userId。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-basic-profile" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "390927249"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/instagram/basic-profile/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

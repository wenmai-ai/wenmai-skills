# Wenmai SCRAPECREATORS scrapecreators_twitter_community_tweets API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/twitter-community-tweets`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_twitter_community_tweets`
- **脚本入口**：`modules/community-tweets/scripts/community_tweets.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | Twitter / X 社群链接，例如 https://x.com/i/communities/{id}。 |

## 请求示例

```json
{
  "url": "https://x.com/i/communities/1926186499399139650"
}
```

```bash
python3 modules/community-tweets/scripts/community_tweets.py '{"url": "https://x.com/i/communities/1926186499399139650"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `tweets` | array | 推文列表。 |
| `tweets[].id` | string | 标识符。 |
| `tweets[].source` | string | 来源。 |
| `tweets[].view_count` | string | 官方字段 `view_count`；官方未单独提供业务说明。 |
| `tweets[].bookmark_count` | integer | 收藏数量。 |
| `tweets[].bookmarked` | boolean | 官方字段 `bookmarked`；官方未单独提供业务说明。 |
| `tweets[].created_at` | string | 创建时间。 |
| `tweets[].conversation_id_str` | string | 官方字段 `conversation_id_str`；官方未单独提供业务说明。 |
| `tweets[].display_text_range` | array | 官方字段 `display_text_range`；官方未单独提供业务说明。 |
| `tweets[].display_text_range[]` | integer | 官方数组 `display_text_range` 的元素。 |
| `tweets[].favorite_count` | integer | 官方字段 `favorite_count`；官方未单独提供业务说明。 |
| `tweets[].favorited` | boolean | 官方字段 `favorited`；官方未单独提供业务说明。 |
| `tweets[].full_text` | string | 官方字段 `full_text`；官方未单独提供业务说明。 |
| `tweets[].is_quote_status` | boolean | 官方字段 `is_quote_status`；官方未单独提供业务说明。 |
| `tweets[].lang` | string | 官方字段 `lang`；官方未单独提供业务说明。 |
| `tweets[].possibly_sensitive` | boolean | 官方字段 `possibly_sensitive`；官方未单独提供业务说明。 |
| `tweets[].possibly_sensitive_editable` | boolean | 官方字段 `possibly_sensitive_editable`；官方未单独提供业务说明。 |
| `tweets[].quote_count` | integer | 引用数量。 |
| `tweets[].reply_count` | integer | 回复数量。 |
| `tweets[].retweet_count` | integer | 转推数量。 |
| `tweets[].retweeted` | boolean | 官方字段 `retweeted`；官方未单独提供业务说明。 |
| `tweets[].user_id_str` | string | 官方字段 `user_id_str`；官方未单独提供业务说明。 |
| `tweets[].id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `tweets[].user` | object | 用户信息。 |
| `tweets[].user.__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `tweets[].user.id` | string | 标识符。 |
| `tweets[].user.rest_id` | string | Twitter 对象标识。 |
| `tweets[].user.affiliates_highlighted_label` | object | 官方示例为空对象，未提供子字段。 |
| `tweets[].user.avatar` | object | 头像信息。 |
| `tweets[].user.avatar.image_url` | string | 官方字段 `image_url`；官方未单独提供业务说明。 |
| `tweets[].user.core` | object | 核心信息。 |
| `tweets[].user.core.created_at` | string | 创建时间。 |
| `tweets[].user.core.name` | string | 名称。 |
| `tweets[].user.core.screen_name` | string | 官方字段 `screen_name`；官方未单独提供业务说明。 |
| `tweets[].user.dm_permissions` | object | 官方示例为空对象，未提供子字段。 |
| `tweets[].user.is_blue_verified` | boolean | 是否为蓝标认证账号。 |
| `tweets[].user.legacy` | object | 官方 legacy 对象。 |
| `tweets[].user.legacy.default_profile` | boolean | 官方字段 `default_profile`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.default_profile_image` | boolean | 官方字段 `default_profile_image`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.description` | string | 描述。 |
| `tweets[].user.legacy.entities` | object | 官方字段 `entities`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.entities.description` | object | 描述。 |
| `tweets[].user.legacy.entities.description.urls` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].user.legacy.fast_followers_count` | integer | 官方字段 `fast_followers_count`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.favourites_count` | integer | 官方字段 `favourites_count`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.followers_count` | integer | 粉丝数量。 |
| `tweets[].user.legacy.friends_count` | integer | 好友数量。 |
| `tweets[].user.legacy.has_custom_timelines` | boolean | 官方字段 `has_custom_timelines`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.is_translator` | boolean | 官方字段 `is_translator`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.listed_count` | integer | 官方字段 `listed_count`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.media_count` | integer | 官方字段 `media_count`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.normal_followers_count` | integer | 官方字段 `normal_followers_count`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.pinned_tweet_ids_str` | array | 官方字段 `pinned_tweet_ids_str`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.pinned_tweet_ids_str[]` | string | 官方数组 `pinned_tweet_ids_str` 的元素。 |
| `tweets[].user.legacy.possibly_sensitive` | boolean | 官方字段 `possibly_sensitive`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.profile_interstitial_type` | string | 官方字段 `profile_interstitial_type`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.statuses_count` | integer | 官方字段 `statuses_count`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.translator_type` | string | 官方字段 `translator_type`；官方未单独提供业务说明。 |
| `tweets[].user.legacy.withheld_in_countries` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].user.location` | object | 位置信息。 |
| `tweets[].user.location.location` | string | 位置信息。 |
| `tweets[].user.media_permissions` | object | 官方示例为空对象，未提供子字段。 |
| `tweets[].user.parody_commentary_fan_label` | string | 官方字段 `parody_commentary_fan_label`；官方未单独提供业务说明。 |
| `tweets[].user.profile_image_shape` | string | 官方字段 `profile_image_shape`；官方未单独提供业务说明。 |
| `tweets[].user.professional` | object | 官方字段 `professional`；官方未单独提供业务说明。 |
| `tweets[].user.professional.rest_id` | string | Twitter 对象标识。 |
| `tweets[].user.professional.professional_type` | string | 官方字段 `professional_type`；官方未单独提供业务说明。 |
| `tweets[].user.professional.category` | array | 官方字段 `category`；官方未单独提供业务说明。 |
| `tweets[].user.professional.category[].id` | integer | 标识符。 |
| `tweets[].user.professional.category[].name` | string | 名称。 |
| `tweets[].user.professional.category[].icon_name` | string | 官方字段 `icon_name`；官方未单独提供业务说明。 |
| `tweets[].user.privacy` | object | 官方字段 `privacy`；官方未单独提供业务说明。 |
| `tweets[].user.privacy.protected` | boolean | 官方字段 `protected`；官方未单独提供业务说明。 |
| `tweets[].user.relationship_perspectives` | object | 官方示例为空对象，未提供子字段。 |
| `tweets[].user.tipjar_settings` | object | 官方字段 `tipjar_settings`；官方未单独提供业务说明。 |
| `tweets[].user.tipjar_settings.is_enabled` | boolean | 官方字段 `is_enabled`；官方未单独提供业务说明。 |
| `tweets[].user.tipjar_settings.bandcamp_handle` | string | 官方字段 `bandcamp_handle`；官方未单独提供业务说明。 |
| `tweets[].user.tipjar_settings.bitcoin_handle` | string | 官方字段 `bitcoin_handle`；官方未单独提供业务说明。 |
| `tweets[].user.tipjar_settings.cash_app_handle` | string | 官方字段 `cash_app_handle`；官方未单独提供业务说明。 |
| `tweets[].user.tipjar_settings.ethereum_handle` | string | 官方字段 `ethereum_handle`；官方未单独提供业务说明。 |
| `tweets[].user.tipjar_settings.gofundme_handle` | string | 官方字段 `gofundme_handle`；官方未单独提供业务说明。 |
| `tweets[].user.tipjar_settings.patreon_handle` | string | 官方字段 `patreon_handle`；官方未单独提供业务说明。 |
| `tweets[].user.tipjar_settings.pay_pal_handle` | string | 官方字段 `pay_pal_handle`；官方未单独提供业务说明。 |
| `tweets[].user.tipjar_settings.venmo_handle` | string | 官方字段 `venmo_handle`；官方未单独提供业务说明。 |
| `tweets[].user.verification` | object | 官方字段 `verification`；官方未单独提供业务说明。 |
| `tweets[].user.verification.verified` | boolean | 是否认证。 |

## 使用要点

- 获取社群帖子。每次成功扣 2 稳卖积分。
- 顶层直接传业务字段，不要增加 `request` 包装层。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、handle、推文链接、社群链接、cursor 和分页。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/twitter-community-tweets" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/i/communities/1926186499399139650"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/twitter/community/tweets/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

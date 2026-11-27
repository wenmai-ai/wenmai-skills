# Wenmai SCRAPECREATORS scrapecreators_twitter_profile API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/twitter-profile`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_twitter_profile`
- **脚本入口**：`modules/profile/scripts/profile.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `handle` | string | 是 | Twitter / X 用户名，不要带 @。 |
| `cache_max_age` | string | 否 | 若缓存中有不晚于该时效的数据则直接返回，官方不计 credit。 |

## 请求示例

```json
{
  "handle": "levelsio"
}
```

```bash
python3 modules/profile/scripts/profile.py '{"handle": "levelsio"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `id` | string | 标识符。 |
| `rest_id` | string | Twitter 对象标识。 |
| `affiliates_highlighted_label` | object | 官方字段 `affiliates_highlighted_label`；官方未单独提供业务说明。 |
| `affiliates_highlighted_label.label` | object | 官方字段 `label`；官方未单独提供业务说明。 |
| `affiliates_highlighted_label.label.url` | object | 链接。 |
| `affiliates_highlighted_label.label.url.url` | string | 链接。 |
| `affiliates_highlighted_label.label.url.urlType` | string | 官方字段 `urlType`；官方未单独提供业务说明。 |
| `affiliates_highlighted_label.label.badge` | object | 官方字段 `badge`；官方未单独提供业务说明。 |
| `affiliates_highlighted_label.label.badge.url` | string | 链接。 |
| `affiliates_highlighted_label.label.description` | string | 描述。 |
| `affiliates_highlighted_label.label.userLabelType` | string | 官方字段 `userLabelType`；官方未单独提供业务说明。 |
| `affiliates_highlighted_label.label.userLabelDisplayType` | string | 官方字段 `userLabelDisplayType`；官方未单独提供业务说明。 |
| `is_blue_verified` | boolean | 是否为蓝标认证账号。 |
| `profile_image_shape` | string | 官方字段 `profile_image_shape`；官方未单独提供业务说明。 |
| `legacy` | object | 官方 legacy 对象。 |
| `legacy.created_at` | string | 创建时间。 |
| `legacy.default_profile` | boolean | 官方字段 `default_profile`；官方未单独提供业务说明。 |
| `legacy.default_profile_image` | boolean | 官方字段 `default_profile_image`；官方未单独提供业务说明。 |
| `legacy.description` | string | 描述。 |
| `legacy.entities` | object | 官方字段 `entities`；官方未单独提供业务说明。 |
| `legacy.entities.description` | object | 描述。 |
| `legacy.entities.description.urls` | array | 官方字段 `urls`；官方未单独提供业务说明。 |
| `legacy.entities.description.urls[].display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `legacy.entities.description.urls[].expanded_url` | string | 官方字段 `expanded_url`；官方未单独提供业务说明。 |
| `legacy.entities.description.urls[].url` | string | 链接。 |
| `legacy.entities.description.urls[].indices` | array | 官方字段 `indices`；官方未单独提供业务说明。 |
| `legacy.entities.description.urls[].indices[]` | integer | 官方数组 `indices` 的元素。 |
| `legacy.entities.url` | object | 链接。 |
| `legacy.entities.url.urls` | array | 官方字段 `urls`；官方未单独提供业务说明。 |
| `legacy.entities.url.urls[].display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `legacy.entities.url.urls[].expanded_url` | string | 官方字段 `expanded_url`；官方未单独提供业务说明。 |
| `legacy.entities.url.urls[].url` | string | 链接。 |
| `legacy.entities.url.urls[].indices` | array | 官方字段 `indices`；官方未单独提供业务说明。 |
| `legacy.entities.url.urls[].indices[]` | integer | 官方数组 `indices` 的元素。 |
| `legacy.fast_followers_count` | integer | 官方字段 `fast_followers_count`；官方未单独提供业务说明。 |
| `legacy.favourites_count` | integer | 官方字段 `favourites_count`；官方未单独提供业务说明。 |
| `legacy.followers_count` | integer | 粉丝数量。 |
| `legacy.friends_count` | integer | 好友数量。 |
| `legacy.has_custom_timelines` | boolean | 官方字段 `has_custom_timelines`；官方未单独提供业务说明。 |
| `legacy.is_translator` | boolean | 官方字段 `is_translator`；官方未单独提供业务说明。 |
| `legacy.listed_count` | integer | 官方字段 `listed_count`；官方未单独提供业务说明。 |
| `legacy.location` | string | 位置信息。 |
| `legacy.media_count` | integer | 官方字段 `media_count`；官方未单独提供业务说明。 |
| `legacy.name` | string | 名称。 |
| `legacy.normal_followers_count` | integer | 官方字段 `normal_followers_count`；官方未单独提供业务说明。 |
| `legacy.pinned_tweet_ids_str` | array | 官方字段 `pinned_tweet_ids_str`；官方未单独提供业务说明。 |
| `legacy.pinned_tweet_ids_str[]` | string | 官方数组 `pinned_tweet_ids_str` 的元素。 |
| `legacy.possibly_sensitive` | boolean | 官方字段 `possibly_sensitive`；官方未单独提供业务说明。 |
| `legacy.profile_banner_url` | string | 官方字段 `profile_banner_url`；官方未单独提供业务说明。 |
| `legacy.profile_image_url_https` | string | 官方字段 `profile_image_url_https`；官方未单独提供业务说明。 |
| `legacy.profile_interstitial_type` | string | 官方字段 `profile_interstitial_type`；官方未单独提供业务说明。 |
| `legacy.screen_name` | string | 官方字段 `screen_name`；官方未单独提供业务说明。 |
| `legacy.statuses_count` | integer | 官方字段 `statuses_count`；官方未单独提供业务说明。 |
| `legacy.translator_type` | string | 官方字段 `translator_type`；官方未单独提供业务说明。 |
| `legacy.url` | string | 链接。 |
| `legacy.verified` | boolean | 是否认证。 |
| `legacy.withheld_in_countries` | array | 官方示例为空数组，未提供元素结构。 |
| `tipjar_settings` | object | 官方字段 `tipjar_settings`；官方未单独提供业务说明。 |
| `tipjar_settings.is_enabled` | boolean | 官方字段 `is_enabled`；官方未单独提供业务说明。 |
| `tipjar_settings.bandcamp_handle` | string | 官方字段 `bandcamp_handle`；官方未单独提供业务说明。 |
| `tipjar_settings.bitcoin_handle` | string | 官方字段 `bitcoin_handle`；官方未单独提供业务说明。 |
| `tipjar_settings.cash_app_handle` | string | 官方字段 `cash_app_handle`；官方未单独提供业务说明。 |
| `tipjar_settings.ethereum_handle` | string | 官方字段 `ethereum_handle`；官方未单独提供业务说明。 |
| `tipjar_settings.gofundme_handle` | string | 官方字段 `gofundme_handle`；官方未单独提供业务说明。 |
| `tipjar_settings.patreon_handle` | string | 官方字段 `patreon_handle`；官方未单独提供业务说明。 |
| `tipjar_settings.pay_pal_handle` | string | 官方字段 `pay_pal_handle`；官方未单独提供业务说明。 |
| `tipjar_settings.venmo_handle` | string | 官方字段 `venmo_handle`；官方未单独提供业务说明。 |
| `legacy_extended_profile` | object | 官方示例为空对象，未提供子字段。 |
| `is_profile_translatable` | boolean | 官方字段 `is_profile_translatable`；官方未单独提供业务说明。 |
| `has_hidden_subscriptions_on_profile` | boolean | 官方字段 `has_hidden_subscriptions_on_profile`；官方未单独提供业务说明。 |
| `verification_info` | object | 官方字段 `verification_info`；官方未单独提供业务说明。 |
| `verification_info.is_identity_verified` | boolean | 官方字段 `is_identity_verified`；官方未单独提供业务说明。 |
| `verification_info.reason` | object | 官方字段 `reason`；官方未单独提供业务说明。 |
| `verification_info.reason.description` | object | 描述。 |
| `verification_info.reason.description.text` | string | 文本内容。 |
| `verification_info.reason.description.entities` | array | 官方字段 `entities`；官方未单独提供业务说明。 |
| `verification_info.reason.description.entities[].from_index` | integer | 官方字段 `from_index`；官方未单独提供业务说明。 |
| `verification_info.reason.description.entities[].to_index` | integer | 官方字段 `to_index`；官方未单独提供业务说明。 |
| `verification_info.reason.description.entities[].ref` | object | 官方字段 `ref`；官方未单独提供业务说明。 |
| `verification_info.reason.description.entities[].ref.url` | string | 链接。 |
| `verification_info.reason.description.entities[].ref.url_type` | string | 官方字段 `url_type`；官方未单独提供业务说明。 |
| `verification_info.reason.verified_since_msec` | string | 官方字段 `verified_since_msec`；官方未单独提供业务说明。 |
| `highlights_info` | object | 官方字段 `highlights_info`；官方未单独提供业务说明。 |
| `highlights_info.can_highlight_tweets` | boolean | 官方字段 `can_highlight_tweets`；官方未单独提供业务说明。 |
| `highlights_info.highlighted_tweets` | string | 官方字段 `highlighted_tweets`；官方未单独提供业务说明。 |
| `user_seed_tweet_count` | integer | 官方字段 `user_seed_tweet_count`；官方未单独提供业务说明。 |
| `business_account` | object | 官方示例为空对象，未提供子字段。 |
| `creator_subscriptions_count` | integer | 官方字段 `creator_subscriptions_count`；官方未单独提供业务说明。 |

## 使用要点

- 按 handle 获取账号资料。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/twitter-profile" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "levelsio"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/twitter/profile/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

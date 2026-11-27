# Wenmai SCRAPECREATORS scrapecreators_twitter_user_tweets API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/twitter-user-tweets`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_twitter_user_tweets`
- **脚本入口**：`modules/user-tweets/scripts/user_tweets.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `handle` | string | 是 | Twitter / X 用户名，不要带 @。 |
| `trim` | boolean | 否 | 为 true 时返回精简字段。不要当默认。 |

## 请求示例

```json
{
  "handle": "levelsio"
}
```

```bash
python3 modules/user-tweets/scripts/user_tweets.py '{"handle": "levelsio"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `tweets` | array | 推文列表。 |
| `tweets[].__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `tweets[].rest_id` | string | Twitter 对象标识。 |
| `tweets[].core` | object | 核心信息。 |
| `tweets[].core.user_results` | object | 官方字段 `user_results`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result` | object | 官方字段 `result`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.id` | string | 标识符。 |
| `tweets[].core.user_results.result.rest_id` | string | Twitter 对象标识。 |
| `tweets[].core.user_results.result.affiliates_highlighted_label` | object | 官方示例为空对象，未提供子字段。 |
| `tweets[].core.user_results.result.is_blue_verified` | boolean | 是否为蓝标认证账号。 |
| `tweets[].core.user_results.result.profile_image_shape` | string | 官方字段 `profile_image_shape`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy` | object | 官方 legacy 对象。 |
| `tweets[].core.user_results.result.legacy.created_at` | string | 创建时间。 |
| `tweets[].core.user_results.result.legacy.default_profile` | boolean | 官方字段 `default_profile`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.default_profile_image` | boolean | 官方字段 `default_profile_image`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.description` | string | 描述。 |
| `tweets[].core.user_results.result.legacy.entities` | object | 官方字段 `entities`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.entities.description` | object | 描述。 |
| `tweets[].core.user_results.result.legacy.entities.description.urls` | array | 官方字段 `urls`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.entities.description.urls[].display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.entities.description.urls[].expanded_url` | string | 官方字段 `expanded_url`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.entities.description.urls[].url` | string | 链接。 |
| `tweets[].core.user_results.result.legacy.entities.description.urls[].indices` | array | 官方字段 `indices`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.entities.description.urls[].indices[]` | integer | 官方数组 `indices` 的元素。 |
| `tweets[].core.user_results.result.legacy.entities.url` | object | 链接。 |
| `tweets[].core.user_results.result.legacy.entities.url.urls` | array | 官方字段 `urls`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.entities.url.urls[].display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.entities.url.urls[].expanded_url` | string | 官方字段 `expanded_url`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.entities.url.urls[].url` | string | 链接。 |
| `tweets[].core.user_results.result.legacy.entities.url.urls[].indices` | array | 官方字段 `indices`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.entities.url.urls[].indices[]` | integer | 官方数组 `indices` 的元素。 |
| `tweets[].core.user_results.result.legacy.fast_followers_count` | integer | 官方字段 `fast_followers_count`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.favourites_count` | integer | 官方字段 `favourites_count`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.followers_count` | integer | 粉丝数量。 |
| `tweets[].core.user_results.result.legacy.friends_count` | integer | 好友数量。 |
| `tweets[].core.user_results.result.legacy.has_custom_timelines` | boolean | 官方字段 `has_custom_timelines`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.is_translator` | boolean | 官方字段 `is_translator`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.listed_count` | integer | 官方字段 `listed_count`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.location` | string | 位置信息。 |
| `tweets[].core.user_results.result.legacy.media_count` | integer | 官方字段 `media_count`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.name` | string | 名称。 |
| `tweets[].core.user_results.result.legacy.normal_followers_count` | integer | 官方字段 `normal_followers_count`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.pinned_tweet_ids_str` | array | 官方字段 `pinned_tweet_ids_str`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.pinned_tweet_ids_str[]` | string | 官方数组 `pinned_tweet_ids_str` 的元素。 |
| `tweets[].core.user_results.result.legacy.possibly_sensitive` | boolean | 官方字段 `possibly_sensitive`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.profile_banner_url` | string | 官方字段 `profile_banner_url`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.profile_image_url_https` | string | 官方字段 `profile_image_url_https`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.profile_interstitial_type` | string | 官方字段 `profile_interstitial_type`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.screen_name` | string | 官方字段 `screen_name`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.statuses_count` | integer | 官方字段 `statuses_count`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.translator_type` | string | 官方字段 `translator_type`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.legacy.url` | string | 链接。 |
| `tweets[].core.user_results.result.legacy.verified` | boolean | 是否认证。 |
| `tweets[].core.user_results.result.legacy.withheld_in_countries` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].core.user_results.result.professional` | object | 官方字段 `professional`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.professional.rest_id` | string | Twitter 对象标识。 |
| `tweets[].core.user_results.result.professional.professional_type` | string | 官方字段 `professional_type`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.professional.category` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].core.user_results.result.tipjar_settings` | object | 官方字段 `tipjar_settings`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.tipjar_settings.is_enabled` | boolean | 官方字段 `is_enabled`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.tipjar_settings.bandcamp_handle` | string | 官方字段 `bandcamp_handle`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.tipjar_settings.bitcoin_handle` | string | 官方字段 `bitcoin_handle`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.tipjar_settings.cash_app_handle` | string | 官方字段 `cash_app_handle`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.tipjar_settings.ethereum_handle` | string | 官方字段 `ethereum_handle`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.tipjar_settings.gofundme_handle` | string | 官方字段 `gofundme_handle`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.tipjar_settings.patreon_handle` | string | 官方字段 `patreon_handle`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.tipjar_settings.pay_pal_handle` | string | 官方字段 `pay_pal_handle`；官方未单独提供业务说明。 |
| `tweets[].core.user_results.result.tipjar_settings.venmo_handle` | string | 官方字段 `venmo_handle`；官方未单独提供业务说明。 |
| `tweets[].unmention_data` | object | 官方示例为空对象，未提供子字段。 |
| `tweets[].edit_control` | object | 官方字段 `edit_control`；官方未单独提供业务说明。 |
| `tweets[].edit_control.edit_tweet_ids` | array | 官方字段 `edit_tweet_ids`；官方未单独提供业务说明。 |
| `tweets[].edit_control.edit_tweet_ids[]` | string | 官方数组 `edit_tweet_ids` 的元素。 |
| `tweets[].edit_control.editable_until_msecs` | string | 官方字段 `editable_until_msecs`；官方未单独提供业务说明。 |
| `tweets[].edit_control.is_edit_eligible` | boolean | 官方字段 `is_edit_eligible`；官方未单独提供业务说明。 |
| `tweets[].edit_control.edits_remaining` | string | 官方字段 `edits_remaining`；官方未单独提供业务说明。 |
| `tweets[].is_translatable` | boolean | 官方字段 `is_translatable`；官方未单独提供业务说明。 |
| `tweets[].views` | object | 官方字段 `views`；官方未单独提供业务说明。 |
| `tweets[].views.count` | string | 数量。 |
| `tweets[].views.state` | string | 官方字段 `state`；官方未单独提供业务说明。 |
| `tweets[].source` | string | 来源。 |
| `tweets[].legacy` | object | 官方 legacy 对象。 |
| `tweets[].legacy.bookmark_count` | integer | 收藏数量。 |
| `tweets[].legacy.bookmarked` | boolean | 官方字段 `bookmarked`；官方未单独提供业务说明。 |
| `tweets[].legacy.created_at` | string | 创建时间。 |
| `tweets[].legacy.conversation_id_str` | string | 官方字段 `conversation_id_str`；官方未单独提供业务说明。 |
| `tweets[].legacy.display_text_range` | array | 官方字段 `display_text_range`；官方未单独提供业务说明。 |
| `tweets[].legacy.display_text_range[]` | integer | 官方数组 `display_text_range` 的元素。 |
| `tweets[].legacy.entities` | object | 官方字段 `entities`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.hashtags` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.entities.media` | array | 官方字段 `media`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].expanded_url` | string | 官方字段 `expanded_url`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].indices` | array | 官方字段 `indices`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].indices[]` | integer | 官方数组 `indices` 的元素。 |
| `tweets[].legacy.entities.media[].media_key` | string | 官方字段 `media_key`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].media_url_https` | string | 官方字段 `media_url_https`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].type` | string | 类型。 |
| `tweets[].legacy.entities.media[].url` | string | 链接。 |
| `tweets[].legacy.entities.media[].ext_media_availability` | object | 官方字段 `ext_media_availability`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].ext_media_availability.status` | string | 状态。 |
| `tweets[].legacy.entities.media[].features` | object | 官方字段 `features`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].features.large` | object | 官方字段 `large`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].features.large.faces` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.entities.media[].features.medium` | object | 官方字段 `medium`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].features.medium.faces` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.entities.media[].features.small` | object | 官方字段 `small`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].features.small.faces` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.entities.media[].features.orig` | object | 官方字段 `orig`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].features.orig.faces` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.entities.media[].sizes` | object | 官方字段 `sizes`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.large` | object | 官方字段 `large`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.large.h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.large.w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.large.resize` | string | 官方字段 `resize`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.medium` | object | 官方字段 `medium`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.medium.h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.medium.w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.medium.resize` | string | 官方字段 `resize`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.small` | object | 官方字段 `small`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.small.h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.small.w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.small.resize` | string | 官方字段 `resize`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.thumb` | object | 官方字段 `thumb`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.thumb.h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.thumb.w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].sizes.thumb.resize` | string | 官方字段 `resize`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].original_info` | object | 官方字段 `original_info`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].original_info.height` | integer | 高度。 |
| `tweets[].legacy.entities.media[].original_info.width` | integer | 宽度。 |
| `tweets[].legacy.entities.media[].original_info.focus_rects` | array | 官方字段 `focus_rects`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].original_info.focus_rects[].x` | integer | 官方字段 `x`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].original_info.focus_rects[].y` | integer | 官方字段 `y`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].original_info.focus_rects[].w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].original_info.focus_rects[].h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].media_results` | object | 官方字段 `media_results`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].media_results.result` | object | 官方字段 `result`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.media[].media_results.result.media_key` | string | 官方字段 `media_key`；官方未单独提供业务说明。 |
| `tweets[].legacy.entities.symbols` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.entities.timestamps` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.entities.urls` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.entities.user_mentions` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.extended_entities` | object | 官方字段 `extended_entities`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media` | array | 官方字段 `media`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].expanded_url` | string | 官方字段 `expanded_url`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].indices` | array | 官方字段 `indices`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].indices[]` | integer | 官方数组 `indices` 的元素。 |
| `tweets[].legacy.extended_entities.media[].media_key` | string | 官方字段 `media_key`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].media_url_https` | string | 官方字段 `media_url_https`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].type` | string | 类型。 |
| `tweets[].legacy.extended_entities.media[].url` | string | 链接。 |
| `tweets[].legacy.extended_entities.media[].ext_media_availability` | object | 官方字段 `ext_media_availability`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].ext_media_availability.status` | string | 状态。 |
| `tweets[].legacy.extended_entities.media[].features` | object | 官方字段 `features`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].features.large` | object | 官方字段 `large`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].features.large.faces` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.extended_entities.media[].features.medium` | object | 官方字段 `medium`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].features.medium.faces` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.extended_entities.media[].features.small` | object | 官方字段 `small`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].features.small.faces` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.extended_entities.media[].features.orig` | object | 官方字段 `orig`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].features.orig.faces` | array | 官方示例为空数组，未提供元素结构。 |
| `tweets[].legacy.extended_entities.media[].sizes` | object | 官方字段 `sizes`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.large` | object | 官方字段 `large`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.large.h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.large.w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.large.resize` | string | 官方字段 `resize`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.medium` | object | 官方字段 `medium`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.medium.h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.medium.w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.medium.resize` | string | 官方字段 `resize`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.small` | object | 官方字段 `small`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.small.h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.small.w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.small.resize` | string | 官方字段 `resize`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.thumb` | object | 官方字段 `thumb`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.thumb.h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.thumb.w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].sizes.thumb.resize` | string | 官方字段 `resize`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].original_info` | object | 官方字段 `original_info`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].original_info.height` | integer | 高度。 |
| `tweets[].legacy.extended_entities.media[].original_info.width` | integer | 宽度。 |
| `tweets[].legacy.extended_entities.media[].original_info.focus_rects` | array | 官方字段 `focus_rects`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].original_info.focus_rects[].x` | integer | 官方字段 `x`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].original_info.focus_rects[].y` | integer | 官方字段 `y`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].original_info.focus_rects[].w` | integer | 官方字段 `w`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].original_info.focus_rects[].h` | integer | 官方字段 `h`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].media_results` | object | 官方字段 `media_results`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].media_results.result` | object | 官方字段 `result`；官方未单独提供业务说明。 |
| `tweets[].legacy.extended_entities.media[].media_results.result.media_key` | string | 官方字段 `media_key`；官方未单独提供业务说明。 |
| `tweets[].legacy.favorite_count` | integer | 官方字段 `favorite_count`；官方未单独提供业务说明。 |
| `tweets[].legacy.favorited` | boolean | 官方字段 `favorited`；官方未单独提供业务说明。 |
| `tweets[].legacy.full_text` | string | 官方字段 `full_text`；官方未单独提供业务说明。 |
| `tweets[].legacy.is_quote_status` | boolean | 官方字段 `is_quote_status`；官方未单独提供业务说明。 |
| `tweets[].legacy.lang` | string | 官方字段 `lang`；官方未单独提供业务说明。 |
| `tweets[].legacy.possibly_sensitive` | boolean | 官方字段 `possibly_sensitive`；官方未单独提供业务说明。 |
| `tweets[].legacy.possibly_sensitive_editable` | boolean | 官方字段 `possibly_sensitive_editable`；官方未单独提供业务说明。 |
| `tweets[].legacy.quote_count` | integer | 引用数量。 |
| `tweets[].legacy.reply_count` | integer | 回复数量。 |
| `tweets[].legacy.retweet_count` | integer | 转推数量。 |
| `tweets[].legacy.retweeted` | boolean | 官方字段 `retweeted`；官方未单独提供业务说明。 |
| `tweets[].legacy.user_id_str` | string | 官方字段 `user_id_str`；官方未单独提供业务说明。 |
| `tweets[].legacy.id_str` | string | 官方字段 `id_str`；官方未单独提供业务说明。 |
| `tweets[].quick_promote_eligibility` | object | 官方字段 `quick_promote_eligibility`；官方未单独提供业务说明。 |
| `tweets[].quick_promote_eligibility.eligibility` | string | 官方字段 `eligibility`；官方未单独提供业务说明。 |
| `tweets[].url` | string | 链接。 |

## 使用要点

- 返回热门推文，不是最新时间线。trim 不要当默认。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/twitter-user-tweets" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "levelsio"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/twitter/user-tweets/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

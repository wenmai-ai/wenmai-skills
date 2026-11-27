# Wenmai SCRAPECREATORS scrapecreators_facebook_ad_library_search_ads API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-ad-library-search-ads`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_facebook_ad_library_search_ads`
- **脚本入口**：`modules/ad-library-search-ads/scripts/ad_library_search_ads.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `query` | string | 是 | 关键词。 |
| `country` | string | 否 | 两位国家码。 |
| `trim` | boolean | 否 | 精简字段。 |
| `cursor` | string | 否 | 分页游标。 |

## 请求示例

```json
{
  "query": "gymshark",
  "country": "US",
  "trim": true
}
```

```bash
python3 modules/ad-library-search-ads/scripts/ad_library_search_ads.py '{"query": "gymshark", "country": "US", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `searchResults` | array | 官方字段 `searchResults`；官方未单独提供业务说明。 |
| `searchResults[].ad_archive_id` | string | 官方字段 `ad_archive_id`；官方未单独提供业务说明。 |
| `searchResults[].ad_id` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].archive_types` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].categories` | array | 官方字段 `categories`；官方未单独提供业务说明。 |
| `searchResults[].categories[]` | string | 官方数组 `categories` 的元素。 |
| `searchResults[].collation_count` | integer | 官方字段 `collation_count`；官方未单独提供业务说明。 |
| `searchResults[].collation_id` | string | 官方字段 `collation_id`；官方未单独提供业务说明。 |
| `searchResults[].contains_digital_created_media` | boolean | 官方字段 `contains_digital_created_media`；官方未单独提供业务说明。 |
| `searchResults[].contains_sensitive_content` | boolean | 官方字段 `contains_sensitive_content`；官方未单独提供业务说明。 |
| `searchResults[].currency` | string | 官方字段 `currency`；官方未单独提供业务说明。 |
| `searchResults[].end_date` | integer | 官方字段 `end_date`；官方未单独提供业务说明。 |
| `searchResults[].entity_type` | string | 官方字段 `entity_type`；官方未单独提供业务说明。 |
| `searchResults[].fev_info` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].finserv_ad_data` | object | 官方字段 `finserv_ad_data`；官方未单独提供业务说明。 |
| `searchResults[].finserv_ad_data.is_deemed_finserv` | boolean | 官方字段 `is_deemed_finserv`；官方未单独提供业务说明。 |
| `searchResults[].finserv_ad_data.is_limited_delivery` | boolean | 官方字段 `is_limited_delivery`；官方未单独提供业务说明。 |
| `searchResults[].gated_type` | string | 官方字段 `gated_type`；官方未单独提供业务说明。 |
| `searchResults[].has_user_reported` | boolean | 官方字段 `has_user_reported`；官方未单独提供业务说明。 |
| `searchResults[].hidden_safety_data` | boolean | 官方字段 `hidden_safety_data`；官方未单独提供业务说明。 |
| `searchResults[].hide_data_status` | string | 官方字段 `hide_data_status`；官方未单独提供业务说明。 |
| `searchResults[].impressions_with_index` | object | 官方字段 `impressions_with_index`；官方未单独提供业务说明。 |
| `searchResults[].impressions_with_index.impressions_text` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].impressions_with_index.impressions_index` | integer | 官方字段 `impressions_index`；官方未单独提供业务说明。 |
| `searchResults[].is_aaa_eligible` | boolean | 官方字段 `is_aaa_eligible`；官方未单独提供业务说明。 |
| `searchResults[].is_active` | boolean | 官方字段 `is_active`；官方未单独提供业务说明。 |
| `searchResults[].is_profile_page` | boolean | 官方字段 `is_profile_page`；官方未单独提供业务说明。 |
| `searchResults[].menu_items` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].page_id` | string | 官方字段 `page_id`；官方未单独提供业务说明。 |
| `searchResults[].page_is_deleted` | boolean | 官方字段 `page_is_deleted`；官方未单独提供业务说明。 |
| `searchResults[].page_name` | string | 官方字段 `page_name`；官方未单独提供业务说明。 |
| `searchResults[].political_countries` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].publisher_platform` | array | 官方字段 `publisher_platform`；官方未单独提供业务说明。 |
| `searchResults[].publisher_platform[]` | string | 官方数组 `publisher_platform` 的元素。 |
| `searchResults[].reach_estimate` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].regional_regulation_data` | object | 官方字段 `regional_regulation_data`；官方未单独提供业务说明。 |
| `searchResults[].regional_regulation_data.finserv` | object | 官方字段 `finserv`；官方未单独提供业务说明。 |
| `searchResults[].regional_regulation_data.finserv.is_deemed_finserv` | boolean | 官方字段 `is_deemed_finserv`；官方未单独提供业务说明。 |
| `searchResults[].regional_regulation_data.finserv.is_limited_delivery` | boolean | 官方字段 `is_limited_delivery`；官方未单独提供业务说明。 |
| `searchResults[].regional_regulation_data.tw_anti_scam` | object | 官方字段 `tw_anti_scam`；官方未单独提供业务说明。 |
| `searchResults[].regional_regulation_data.tw_anti_scam.is_limited_delivery` | boolean | 官方字段 `is_limited_delivery`；官方未单独提供业务说明。 |
| `searchResults[].report_count` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].snapshot` | object | 广告快照。 |
| `searchResults[].snapshot.body` | object | 官方字段 `body`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.body.text` | string | 文本内容。 |
| `searchResults[].snapshot.branded_content` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].snapshot.brazil_tax_id` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].snapshot.byline` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].snapshot.caption` | null\|string | 说明文字。 |
| `searchResults[].snapshot.cards` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].snapshot.cta_text` | string | 官方字段 `cta_text`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.cta_type` | string | 官方字段 `cta_type`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.country_iso_code` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].snapshot.current_page_name` | string | 官方字段 `current_page_name`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.disclaimer_label` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].snapshot.display_format` | string | 官方字段 `display_format`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.event` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].snapshot.images` | array | 图片列表。 |
| `searchResults[].snapshot.images[].original_image_url` | string | 官方字段 `original_image_url`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.images[].resized_image_url` | string | 官方字段 `resized_image_url`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.images[].watermarked_resized_image_url` | string | 官方字段 `watermarked_resized_image_url`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.images[].image_crops` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].snapshot.is_reshared` | boolean | 官方字段 `is_reshared`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.link_description` | null\|string | 官方字段 `link_description`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.link_url` | null\|string | 官方字段 `link_url`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.page_categories` | array | 官方字段 `page_categories`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.page_categories[]` | string | 官方数组 `page_categories` 的元素。 |
| `searchResults[].snapshot.page_entity_type` | string | 官方字段 `page_entity_type`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.page_id` | string | 官方字段 `page_id`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.page_is_deleted` | boolean | 官方字段 `page_is_deleted`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.page_is_profile_page` | boolean | 官方字段 `page_is_profile_page`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.page_like_count` | integer | 官方字段 `page_like_count`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.page_name` | string | 官方字段 `page_name`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.page_profile_picture_url` | string | 官方字段 `page_profile_picture_url`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.page_profile_uri` | string | 官方字段 `page_profile_uri`；官方未单独提供业务说明。 |
| `searchResults[].snapshot.root_reshared_post` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].snapshot.title` | null\|string | 标题。 |
| `searchResults[].snapshot.videos` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].snapshot.additional_info` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].snapshot.ec_certificates` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].snapshot.extra_images` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].snapshot.extra_links` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].snapshot.extra_texts` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].snapshot.extra_videos` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].spend` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].start_date` | integer | 官方字段 `start_date`；官方未单独提供业务说明。 |
| `searchResults[].state_media_run_label` | null | 官方示例为 null，未说明非空类型。 |
| `searchResults[].targeted_or_reached_countries` | array | 官方示例为空数组，未提供元素结构。 |
| `searchResults[].total_active_time` | integer\|null | 官方字段 `total_active_time`；官方未单独提供业务说明。 |
| `searchResultsCount` | integer | 官方字段 `searchResultsCount`；官方未单独提供业务说明。 |
| `cursor` | string | 分页游标。 |
| `searchResults[].url` | string | 链接。 |
| `searchResults[].start_date_string` | string | 官方字段 `start_date_string`；官方未单独提供业务说明。 |
| `searchResults[].end_date_string` | string | 官方字段 `end_date_string`；官方未单独提供业务说明。 |

## 使用要点

- 搜广告。trim 可减小体积。每次成功扣 2 稳卖积分。
- 顶层直接传业务字段，不要增加 `request` 包装层。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、主页/帖子链接、pageId、商品/广告 ID、cursor 和分页。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-ad-library-search-ads" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "gymshark", "country": "US", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/facebook/adLibrary/search/ads/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

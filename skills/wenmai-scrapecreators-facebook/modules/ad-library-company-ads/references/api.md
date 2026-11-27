# Wenmai SCRAPECREATORS scrapecreators_facebook_ad_library_company_ads API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-ad-library-company-ads`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_facebook_ad_library_company_ads`
- **脚本入口**：`modules/ad-library-company-ads/scripts/ad_library_company_ads.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageId` | string | 否 | 主页 ID，优先。 |
| `companyName` | string | 否 | 公司名，可能匹配错误。 |
| `country` | string | 否 | 两位国家码。 |
| `trim` | boolean | 否 | 精简字段。 |

## 请求示例

```json
{
  "companyName": "Gymshark",
  "country": "US",
  "trim": true
}
```

```bash
python3 modules/ad-library-company-ads/scripts/ad_library_company_ads.py '{"companyName": "Gymshark", "country": "US", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `results` | array | 官方字段 `results`；官方未单独提供业务说明。 |
| `results[].ad_archive_id` | string | 官方字段 `ad_archive_id`；官方未单独提供业务说明。 |
| `results[].ad_id` | null | 官方示例为 null，未说明非空类型。 |
| `results[].archive_types` | array | 官方示例为空数组，未提供元素结构。 |
| `results[].categories` | array | 官方字段 `categories`；官方未单独提供业务说明。 |
| `results[].categories[]` | string | 官方数组 `categories` 的元素。 |
| `results[].collation_count` | integer | 官方字段 `collation_count`；官方未单独提供业务说明。 |
| `results[].collation_id` | string | 官方字段 `collation_id`；官方未单独提供业务说明。 |
| `results[].contains_digital_created_media` | boolean | 官方字段 `contains_digital_created_media`；官方未单独提供业务说明。 |
| `results[].contains_sensitive_content` | boolean | 官方字段 `contains_sensitive_content`；官方未单独提供业务说明。 |
| `results[].currency` | string | 官方字段 `currency`；官方未单独提供业务说明。 |
| `results[].end_date` | integer | 官方字段 `end_date`；官方未单独提供业务说明。 |
| `results[].entity_type` | string | 官方字段 `entity_type`；官方未单独提供业务说明。 |
| `results[].fev_info` | null | 官方示例为 null，未说明非空类型。 |
| `results[].finserv_ad_data` | object | 官方字段 `finserv_ad_data`；官方未单独提供业务说明。 |
| `results[].finserv_ad_data.is_deemed_finserv` | boolean | 官方字段 `is_deemed_finserv`；官方未单独提供业务说明。 |
| `results[].finserv_ad_data.is_limited_delivery` | boolean | 官方字段 `is_limited_delivery`；官方未单独提供业务说明。 |
| `results[].gated_type` | string | 官方字段 `gated_type`；官方未单独提供业务说明。 |
| `results[].has_user_reported` | boolean | 官方字段 `has_user_reported`；官方未单独提供业务说明。 |
| `results[].hidden_safety_data` | boolean | 官方字段 `hidden_safety_data`；官方未单独提供业务说明。 |
| `results[].hide_data_status` | string | 官方字段 `hide_data_status`；官方未单独提供业务说明。 |
| `results[].impressions_with_index` | object | 官方字段 `impressions_with_index`；官方未单独提供业务说明。 |
| `results[].impressions_with_index.impressions_text` | null | 官方示例为 null，未说明非空类型。 |
| `results[].impressions_with_index.impressions_index` | integer | 官方字段 `impressions_index`；官方未单独提供业务说明。 |
| `results[].is_aaa_eligible` | boolean | 官方字段 `is_aaa_eligible`；官方未单独提供业务说明。 |
| `results[].is_active` | boolean | 官方字段 `is_active`；官方未单独提供业务说明。 |
| `results[].is_profile_page` | boolean | 官方字段 `is_profile_page`；官方未单独提供业务说明。 |
| `results[].menu_items` | array | 官方示例为空数组，未提供元素结构。 |
| `results[].page_id` | string | 官方字段 `page_id`；官方未单独提供业务说明。 |
| `results[].page_is_deleted` | boolean | 官方字段 `page_is_deleted`；官方未单独提供业务说明。 |
| `results[].page_name` | string | 官方字段 `page_name`；官方未单独提供业务说明。 |
| `results[].political_countries` | array | 官方示例为空数组，未提供元素结构。 |
| `results[].publisher_platform` | array | 官方字段 `publisher_platform`；官方未单独提供业务说明。 |
| `results[].publisher_platform[]` | string | 官方数组 `publisher_platform` 的元素。 |
| `results[].reach_estimate` | null | 官方示例为 null，未说明非空类型。 |
| `results[].regional_regulation_data` | object | 官方字段 `regional_regulation_data`；官方未单独提供业务说明。 |
| `results[].regional_regulation_data.finserv` | object | 官方字段 `finserv`；官方未单独提供业务说明。 |
| `results[].regional_regulation_data.finserv.is_deemed_finserv` | boolean | 官方字段 `is_deemed_finserv`；官方未单独提供业务说明。 |
| `results[].regional_regulation_data.finserv.is_limited_delivery` | boolean | 官方字段 `is_limited_delivery`；官方未单独提供业务说明。 |
| `results[].regional_regulation_data.tw_anti_scam` | object | 官方字段 `tw_anti_scam`；官方未单独提供业务说明。 |
| `results[].regional_regulation_data.tw_anti_scam.is_limited_delivery` | boolean | 官方字段 `is_limited_delivery`；官方未单独提供业务说明。 |
| `results[].report_count` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot` | object | 广告快照。 |
| `results[].snapshot.body` | object | 官方字段 `body`；官方未单独提供业务说明。 |
| `results[].snapshot.body.text` | string | 文本内容。 |
| `results[].snapshot.branded_content` | null\|object | 官方字段 `branded_content`；官方未单独提供业务说明。 |
| `results[].snapshot.branded_content.current_page_name` | string | 官方字段 `current_page_name`；官方未单独提供业务说明。 |
| `results[].snapshot.branded_content.page_categories` | array | 官方字段 `page_categories`；官方未单独提供业务说明。 |
| `results[].snapshot.branded_content.page_categories[]` | string | 官方数组 `page_categories` 的元素。 |
| `results[].snapshot.branded_content.page_id` | string | 官方字段 `page_id`；官方未单独提供业务说明。 |
| `results[].snapshot.branded_content.page_is_deleted` | boolean | 官方字段 `page_is_deleted`；官方未单独提供业务说明。 |
| `results[].snapshot.branded_content.page_name` | string | 官方字段 `page_name`；官方未单独提供业务说明。 |
| `results[].snapshot.branded_content.page_profile_pic_url` | string | 官方字段 `page_profile_pic_url`；官方未单独提供业务说明。 |
| `results[].snapshot.branded_content.page_profile_uri` | string | 官方字段 `page_profile_uri`；官方未单独提供业务说明。 |
| `results[].snapshot.brazil_tax_id` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot.byline` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot.caption` | string | 说明文字。 |
| `results[].snapshot.cards` | array | 官方示例为空数组，未提供元素结构。 |
| `results[].snapshot.cta_text` | string | 官方字段 `cta_text`；官方未单独提供业务说明。 |
| `results[].snapshot.cta_type` | string | 官方字段 `cta_type`；官方未单独提供业务说明。 |
| `results[].snapshot.country_iso_code` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot.current_page_name` | string | 官方字段 `current_page_name`；官方未单独提供业务说明。 |
| `results[].snapshot.disclaimer_label` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot.display_format` | string | 官方字段 `display_format`；官方未单独提供业务说明。 |
| `results[].snapshot.event` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot.images` | array | 官方示例为空数组，未提供元素结构。 |
| `results[].snapshot.is_reshared` | boolean | 官方字段 `is_reshared`；官方未单独提供业务说明。 |
| `results[].snapshot.link_description` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot.link_url` | string | 官方字段 `link_url`；官方未单独提供业务说明。 |
| `results[].snapshot.page_categories` | array | 官方字段 `page_categories`；官方未单独提供业务说明。 |
| `results[].snapshot.page_categories[]` | string | 官方数组 `page_categories` 的元素。 |
| `results[].snapshot.page_entity_type` | string | 官方字段 `page_entity_type`；官方未单独提供业务说明。 |
| `results[].snapshot.page_id` | string | 官方字段 `page_id`；官方未单独提供业务说明。 |
| `results[].snapshot.page_is_deleted` | boolean | 官方字段 `page_is_deleted`；官方未单独提供业务说明。 |
| `results[].snapshot.page_is_profile_page` | boolean | 官方字段 `page_is_profile_page`；官方未单独提供业务说明。 |
| `results[].snapshot.page_like_count` | integer | 官方字段 `page_like_count`；官方未单独提供业务说明。 |
| `results[].snapshot.page_name` | string | 官方字段 `page_name`；官方未单独提供业务说明。 |
| `results[].snapshot.page_profile_picture_url` | string | 官方字段 `page_profile_picture_url`；官方未单独提供业务说明。 |
| `results[].snapshot.page_profile_uri` | string | 官方字段 `page_profile_uri`；官方未单独提供业务说明。 |
| `results[].snapshot.root_reshared_post` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot.title` | null\|string | 标题。 |
| `results[].snapshot.videos` | array | 视频列表。 |
| `results[].snapshot.videos[].video_hd_url` | string | 官方字段 `video_hd_url`；官方未单独提供业务说明。 |
| `results[].snapshot.videos[].video_preview_image_url` | string | 官方字段 `video_preview_image_url`；官方未单独提供业务说明。 |
| `results[].snapshot.videos[].video_sd_url` | string | 官方字段 `video_sd_url`；官方未单独提供业务说明。 |
| `results[].snapshot.videos[].watermarked_video_hd_url` | string | 官方字段 `watermarked_video_hd_url`；官方未单独提供业务说明。 |
| `results[].snapshot.videos[].watermarked_video_sd_url` | string | 官方字段 `watermarked_video_sd_url`；官方未单独提供业务说明。 |
| `results[].snapshot.additional_info` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot.ec_certificates` | array | 官方示例为空数组，未提供元素结构。 |
| `results[].snapshot.extra_images` | array | 官方示例为空数组，未提供元素结构。 |
| `results[].snapshot.extra_links` | array | 官方字段 `extra_links`；官方未单独提供业务说明。 |
| `results[].snapshot.extra_texts` | array | 官方示例为空数组，未提供元素结构。 |
| `results[].snapshot.extra_videos` | array | 官方字段 `extra_videos`；官方未单独提供业务说明。 |
| `results[].spend` | null | 官方示例为 null，未说明非空类型。 |
| `results[].start_date` | integer | 官方字段 `start_date`；官方未单独提供业务说明。 |
| `results[].state_media_run_label` | null | 官方示例为 null，未说明非空类型。 |
| `results[].targeted_or_reached_countries` | array | 官方示例为空数组，未提供元素结构。 |
| `results[].total_active_time` | null | 官方示例为 null，未说明非空类型。 |
| `cursor` | string | 分页游标。 |
| `results[].snapshot.extra_links[]` | string | 官方数组 `extra_links` 的元素。 |
| `results[].snapshot.extra_videos[].video_hd_handle` | string | 官方字段 `video_hd_handle`；官方未单独提供业务说明。 |
| `results[].snapshot.extra_videos[].video_sd_handle` | string | 官方字段 `video_sd_handle`；官方未单独提供业务说明。 |
| `results[].snapshot.extra_videos[].watermarked_video_hd_url` | null | 官方示例为 null，未说明非空类型。 |
| `results[].snapshot.extra_videos[].watermarked_video_sd_url` | null | 官方示例为 null，未说明非空类型。 |
| `results[].url` | string | 链接。 |
| `results[].start_date_string` | string | 官方字段 `start_date_string`；官方未单独提供业务说明。 |
| `results[].end_date_string` | string | 官方字段 `end_date_string`；官方未单独提供业务说明。 |

## 使用要点

- 公司广告。优先 pageId。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-ad-library-company-ads" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"companyName": "Gymshark", "country": "US", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/facebook/adLibrary/company/ads/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

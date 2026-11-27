# Wenmai SCRAPECREATORS scrapecreators_tiktok_trending_feed API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-trending-feed`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_trending_feed`
- **脚本入口**：`modules/trending-feed/scripts/trending_feed.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `region` | string | 是 | 代理所在地区，两位国家码。不会只返回该地区作品，而是返回该地区未被封禁的内容。 |
| `trim` | boolean | 否 | 是否返回精简字段。true 时体积更小，但评论接口会丢掉回复所需的 cid。 |

## 请求示例

```json
{
  "region": "US",
  "trim": true
}
```

```bash
python3 modules/trending-feed/scripts/trending_feed.py '{"region": "US", "trim": true}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `aweme_list` | array | TikTok 视频列表。 |
| `aweme_list[].aweme_id` | string | TikTok 视频标识。 |
| `aweme_list[].desc` | string | 描述。 |
| `aweme_list[].desc_language` | string | 官方字段 `desc_language`；官方未单独提供业务说明。 |
| `aweme_list[].region` | string | 地区。 |
| `aweme_list[].statistics` | object | 官方字段 `statistics`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.aweme_id` | string | TikTok 视频标识。 |
| `aweme_list[].statistics.comment_count` | integer | 评论数量。 |
| `aweme_list[].statistics.digg_count` | integer | 点赞数量。 |
| `aweme_list[].statistics.download_count` | integer | 官方字段 `download_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.play_count` | integer | 播放数量。 |
| `aweme_list[].statistics.share_count` | integer | 分享数量。 |
| `aweme_list[].statistics.forward_count` | integer | 官方字段 `forward_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.lose_count` | integer | 官方字段 `lose_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.lose_comment_count` | integer | 官方字段 `lose_comment_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.whatsapp_share_count` | integer | 官方字段 `whatsapp_share_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.collect_count` | integer | 官方字段 `collect_count`；官方未单独提供业务说明。 |
| `aweme_list[].statistics.repost_count` | integer | 转发数量。 |
| `aweme_list[].video` | object | 视频信息。 |
| `aweme_list[].video.play_addr` | object | 官方字段 `play_addr`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr.uri` | string | 资源标识。 |
| `aweme_list[].video.play_addr.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.play_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.play_addr.width` | integer | 宽度。 |
| `aweme_list[].video.play_addr.height` | integer | 高度。 |
| `aweme_list[].video.play_addr.url_key` | string | 官方字段 `url_key`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].video.cover` | object | 官方字段 `cover`；官方未单独提供业务说明。 |
| `aweme_list[].video.cover.uri` | string | 资源标识。 |
| `aweme_list[].video.cover.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.cover.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.cover.width` | integer | 宽度。 |
| `aweme_list[].video.cover.height` | integer | 高度。 |
| `aweme_list[].video.cover.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].image_post_info` | object | 官方字段 `image_post_info`；官方未单独提供业务说明。 |
| `aweme_list[].image_post_info.images` | array | 图片列表。 |
| `aweme_list[].image_post_info.images[].display_image` | object | 官方字段 `display_image`；官方未单独提供业务说明。 |
| `aweme_list[].image_post_info.images[].display_image.uri` | string | 资源标识。 |
| `aweme_list[].image_post_info.images[].display_image.url_list` | array | 资源链接列表。 |
| `aweme_list[].image_post_info.images[].display_image.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].image_post_info.images[].display_image.width` | integer | 宽度。 |
| `aweme_list[].image_post_info.images[].display_image.height` | integer | 高度。 |
| `aweme_list[].image_post_info.images[].display_image.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].image_post_info.images[].display_image.preview` | object | 官方字段 `preview`；官方未单独提供业务说明。 |
| `aweme_list[].image_post_info.images[].display_image.preview.data` | string | 官方响应中的内层业务数据。 |
| `aweme_list[].image_post_info.images[].display_image.preview.preview_type` | integer | 官方字段 `preview_type`；官方未单独提供业务说明。 |
| `aweme_list[].image_post_info.images[].display_image.preview.meta_key` | string | 官方字段 `meta_key`；官方未单独提供业务说明。 |
| `aweme_list[].image_post_info.title` | string | 标题。 |
| `aweme_list[].image_post_info.post_extra` | string | 官方字段 `post_extra`；官方未单独提供业务说明。 |
| `aweme_list[].author` | object | 作者信息。 |
| `aweme_list[].author.uid` | string | 用户标识。 |
| `aweme_list[].author.short_id` | string | 官方字段 `short_id`；官方未单独提供业务说明。 |
| `aweme_list[].author.nickname` | string | 昵称。 |
| `aweme_list[].author.signature` | string | 官方字段 `signature`；官方未单独提供业务说明。 |
| `aweme_list[].author.avatar_thumb` | object | 缩略头像。 |
| `aweme_list[].author.avatar_thumb.uri` | string | 资源标识。 |
| `aweme_list[].author.avatar_thumb.url_list` | array | 资源链接列表。 |
| `aweme_list[].author.avatar_thumb.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].author.avatar_thumb.width` | integer | 宽度。 |
| `aweme_list[].author.avatar_thumb.height` | integer | 高度。 |
| `aweme_list[].author.avatar_thumb.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.avatar_medium` | object | 中等尺寸头像。 |
| `aweme_list[].author.avatar_medium.uri` | string | 资源标识。 |
| `aweme_list[].author.avatar_medium.url_list` | array | 资源链接列表。 |
| `aweme_list[].author.avatar_medium.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].author.avatar_medium.width` | integer | 宽度。 |
| `aweme_list[].author.avatar_medium.height` | integer | 高度。 |
| `aweme_list[].author.avatar_medium.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.region` | string | 地区。 |
| `aweme_list[].author.language` | string | 语言。 |
| `aweme_list[].author.sec_uid` | string | TikTok 安全用户标识。 |
| `aweme_list[].author.social_info` | string | 官方字段 `social_info`；官方未单独提供业务说明。 |
| `aweme_list[].author.events` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].create_time` | integer | 创建时间。 |
| `aweme_list[].is_ad` | boolean | 官方字段 `is_ad`；官方未单独提供业务说明。 |
| `aweme_list[].is_eligible_for_commission` | boolean | 官方字段 `is_eligible_for_commission`；官方未单独提供业务说明。 |
| `aweme_list[].create_time_utc` | string | 官方字段 `create_time_utc`；官方未单独提供业务说明。 |
| `aweme_list[].url` | string | 链接。 |
| `aweme_list[].video.play_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_list[].video.play_addr.file_hash` | string | 官方字段 `file_hash`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_addr` | object | 官方字段 `download_addr`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_addr.uri` | string | 资源标识。 |
| `aweme_list[].video.download_addr.url_list` | array | 资源链接列表。 |
| `aweme_list[].video.download_addr.url_list[]` | string | 资源链接列表中的元素。 |
| `aweme_list[].video.download_addr.width` | integer | 宽度。 |
| `aweme_list[].video.download_addr.height` | integer | 高度。 |
| `aweme_list[].video.download_addr.data_size` | integer | 官方字段 `data_size`；官方未单独提供业务说明。 |
| `aweme_list[].video.download_addr.url_prefix` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.follow_status` | integer | 官方字段 `follow_status`；官方未单独提供业务说明。 |
| `aweme_list[].author.is_block` | boolean | 官方字段 `is_block`；官方未单独提供业务说明。 |
| `aweme_list[].author.custom_verify` | string | 官方字段 `custom_verify`；官方未单独提供业务说明。 |
| `aweme_list[].author.unique_id` | string | 账号唯一名称。 |
| `aweme_list[].author.is_discipline_member` | boolean | 官方字段 `is_discipline_member`；官方未单独提供业务说明。 |
| `aweme_list[].author.secret` | integer | 官方字段 `secret`；官方未单独提供业务说明。 |
| `aweme_list[].author.type_label` | array | 官方示例为空数组，未提供元素结构。 |
| `aweme_list[].author.relative_users` | null | 官方示例为 null，未说明非空类型。 |
| `aweme_list[].author.cha_list` | null | 官方示例为 null，未说明非空类型。 |

## 使用要点

- region 必填。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-trending-feed" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"region": "US", "trim": true}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/get-trending-feed/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

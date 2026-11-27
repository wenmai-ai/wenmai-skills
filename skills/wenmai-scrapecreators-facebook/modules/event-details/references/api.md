# Wenmai SCRAPECREATORS scrapecreators_facebook_event_details API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-event-details`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_facebook_event_details`
- **脚本入口**：`modules/event-details/scripts/event_details.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `id` | string | 否 | 活动 ID。 |
| `url` | string | 否 | 活动链接。 |

## 请求示例

```json
{
  "url": "https://www.facebook.com/events/2255360061870188"
}
```

```bash
python3 modules/event-details/scripts/event_details.py '{"url": "https://www.facebook.com/events/2255360061870188"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `id` | string | 标识符。 |
| `url` | string | 链接。 |
| `name` | string | 名称。 |
| `description` | string | 描述。 |
| `category` | null | 官方示例为 null，未说明非空类型。 |
| `categories` | array | 官方示例为空数组，未提供元素结构。 |
| `is_online` | boolean | 官方字段 `is_online`；官方未单独提供业务说明。 |
| `is_past` | boolean | 官方字段 `is_past`；官方未单独提供业务说明。 |
| `event_kind` | string | 官方字段 `event_kind`；官方未单独提供业务说明。 |
| `privacy` | string | 官方字段 `privacy`；官方未单独提供业务说明。 |
| `start_time` | null | 官方示例为 null，未说明非空类型。 |
| `end_time` | null | 官方示例为 null，未说明非空类型。 |
| `time_text` | null | 官方示例为 null，未说明非空类型。 |
| `duration` | string | 时长。 |
| `price` | null | 官方示例为 null，未说明非空类型。 |
| `ticket_url` | null | 官方示例为 null，未说明非空类型。 |
| `ticket_source` | null | 官方示例为 null，未说明非空类型。 |
| `ticket_provider` | null | 官方示例为 null，未说明非空类型。 |
| `location_name` | string | 官方字段 `location_name`；官方未单独提供业务说明。 |
| `address` | string | 官方字段 `address`；官方未单独提供业务说明。 |
| `city` | string | 官方字段 `city`；官方未单独提供业务说明。 |
| `city_id` | string | 官方字段 `city_id`；官方未单独提供业务说明。 |
| `latitude` | number | 官方字段 `latitude`；官方未单独提供业务说明。 |
| `longitude` | number | 官方字段 `longitude`；官方未单独提供业务说明。 |
| `attendance_count` | integer | 官方字段 `attendance_count`；官方未单独提供业务说明。 |
| `attendance_facepile_count` | integer | 官方字段 `attendance_facepile_count`；官方未单独提供业务说明。 |
| `can_view_members` | boolean | 官方字段 `can_view_members`；官方未单独提供业务说明。 |
| `host_context_text` | string | 官方字段 `host_context_text`；官方未单独提供业务说明。 |
| `hosts` | array | 官方字段 `hosts`；官方未单独提供业务说明。 |
| `hosts[].id` | string | 标识符。 |
| `hosts[].name` | string | 名称。 |
| `hosts[].type` | string | 类型。 |
| `hosts[].url` | string | 链接。 |
| `hosts[].is_verified` | boolean | 是否认证。 |
| `hosts[].profile_picture_url` | string | 官方字段 `profile_picture_url`；官方未单独提供业务说明。 |
| `host_names` | array | 官方字段 `host_names`；官方未单独提供业务说明。 |
| `host_names[]` | string | 官方数组 `host_names` 的元素。 |
| `creator` | object | 官方字段 `creator`；官方未单独提供业务说明。 |
| `creator.id` | string | 标识符。 |
| `creator.name` | string | 名称。 |
| `creator.type` | string | 类型。 |
| `creator.url` | null | 官方示例为 null，未说明非空类型。 |
| `creator.is_verified` | null | 官方示例为 null，未说明非空类型。 |
| `creator.profile_picture_url` | null | 官方示例为 null，未说明非空类型。 |
| `description_links` | array | 官方示例为空数组，未提供元素结构。 |
| `can_viewer_message` | boolean | 官方字段 `can_viewer_message`；官方未单独提供业务说明。 |
| `is_viewer_host` | boolean | 官方字段 `is_viewer_host`；官方未单独提供业务说明。 |
| `is_canceled` | boolean | 官方字段 `is_canceled`；官方未单独提供业务说明。 |
| `cover_photo_url` | string | 官方字段 `cover_photo_url`；官方未单独提供业务说明。 |
| `day_time_sentence` | string | 官方字段 `day_time_sentence`；官方未单独提供业务说明。 |
| `rsvp_style` | string | 官方字段 `rsvp_style`；官方未单独提供业务说明。 |
| `event_place` | object | 官方字段 `event_place`；官方未单独提供业务说明。 |
| `event_place.__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `event_place.name` | string | 名称。 |
| `event_place.contextual_name` | string | 官方字段 `contextual_name`；官方未单独提供业务说明。 |
| `event_place.__isNode` | string | 官方字段 `__isNode`；官方未单独提供业务说明。 |
| `event_place.id` | string | 标识符。 |
| `price_info` | null | 官方示例为 null，未说明非空类型。 |
| `current_start_timestamp` | integer | 官方字段 `current_start_timestamp`；官方未单独提供业务说明。 |
| `start_timestamp` | integer | 官方字段 `start_timestamp`；官方未单独提供业务说明。 |
| `start_time_formatted` | string | 官方字段 `start_time_formatted`；官方未单独提供业务说明。 |
| `interested_count` | integer | 官方字段 `interested_count`；官方未单独提供业务说明。 |
| `going_count` | integer | 官方字段 `going_count`；官方未单独提供业务说明。 |

## 使用要点

- 活动详情。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-event-details" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/events/2255360061870188"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/facebook/event/details/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

# Wenmai SCRAPECREATORS scrapecreators_facebook_events API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-events`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_facebook_events`
- **脚本入口**：`modules/events/scripts/events.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | 城市 Events 页面链接。 |
| `time` | string | 否 | today / this_week / next_week。 |
| `cursor` | string | 否 | 分页游标。 |

## 请求示例

```json
{
  "url": "https://www.facebook.com/events/explore/los-angeles-california/112035925469106/",
  "time": "this_week"
}
```

```bash
python3 modules/events/scripts/events.py '{"url": "https://www.facebook.com/events/explore/los-angeles-california/112035925469106/", "time": "this_week"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `events` | array | 官方字段 `events`；官方未单独提供业务说明。 |
| `events[].id` | string | 标识符。 |
| `events[].schema_context` | null | 官方示例为 null，未说明非空类型。 |
| `events[].cover_photo` | object | 官方字段 `cover_photo`；官方未单独提供业务说明。 |
| `events[].cover_photo.photo` | object | 官方字段 `photo`；官方未单独提供业务说明。 |
| `events[].cover_photo.photo.accessibility_caption` | string | 官方字段 `accessibility_caption`；官方未单独提供业务说明。 |
| `events[].cover_photo.photo.image` | object | 图片信息。 |
| `events[].cover_photo.photo.image.uri` | string | 资源标识。 |
| `events[].cover_photo.photo.id` | string | 标识符。 |
| `events[].cover_video` | null | 官方示例为 null，未说明非空类型。 |
| `events[].gif_cover_photo` | null | 官方示例为 null，未说明非空类型。 |
| `events[].online_event_setup` | null | 官方示例为 null，未说明非空类型。 |
| `events[].is_happening_now` | boolean | 官方字段 `is_happening_now`；官方未单独提供业务说明。 |
| `events[].day_time_sentence` | string | 官方字段 `day_time_sentence`；官方未单独提供业务说明。 |
| `events[].name` | string | 名称。 |
| `events[].is_online` | boolean | 官方字段 `is_online`；官方未单独提供业务说明。 |
| `events[].ticketing_context_row` | object | 官方字段 `ticketing_context_row`；官方未单独提供业务说明。 |
| `events[].ticketing_context_row.price_range_text` | null | 官方示例为 null，未说明非空类型。 |
| `events[].event_place` | object | 官方字段 `event_place`；官方未单独提供业务说明。 |
| `events[].event_place.__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `events[].event_place.contextual_name` | string | 官方字段 `contextual_name`；官方未单独提供业务说明。 |
| `events[].event_place.__isNode` | string | 官方字段 `__isNode`；官方未单独提供业务说明。 |
| `events[].event_place.id` | string | 标识符。 |
| `events[].eventUrl` | string | 官方字段 `eventUrl`；官方未单独提供业务说明。 |
| `events[].can_page_viewer_invite_as_user` | boolean | 官方字段 `can_page_viewer_invite_as_user`；官方未单独提供业务说明。 |
| `events[].can_viewer_invite` | boolean | 官方字段 `can_viewer_invite`；官方未单独提供业务说明。 |
| `events[].can_viewer_rsvp` | boolean | 官方字段 `can_viewer_rsvp`；官方未单独提供业务说明。 |
| `events[].can_viewer_share` | boolean | 官方字段 `can_viewer_share`；官方未单独提供业务说明。 |
| `events[].event_kind` | string | 官方字段 `event_kind`；官方未单独提供业务说明。 |
| `events[].if_viewer_can_duplicate_event` | null | 官方示例为 null，未说明非空类型。 |
| `events[].is_online_or_detected_online` | boolean | 官方字段 `is_online_or_detected_online`；官方未单独提供业务说明。 |
| `events[].is_past` | boolean | 官方字段 `is_past`；官方未单独提供业务说明。 |
| `events[].is_viewer_host` | boolean | 官方字段 `is_viewer_host`；官方未单独提供业务说明。 |
| `events[].start_timestamp` | integer | 官方字段 `start_timestamp`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer` | object | 官方字段 `rsvp_button_renderer`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.event` | object | 官方字段 `event`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.event.id` | string | 标识符。 |
| `events[].rsvp_button_renderer.event.connection_style` | string | 官方字段 `connection_style`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.event.can_viewer_join` | boolean | 官方字段 `can_viewer_join`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.event.can_viewer_watch` | boolean | 官方字段 `can_viewer_watch`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.event.can_viewer_unwatch` | boolean | 官方字段 `can_viewer_unwatch`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.event.viewer_watch_status` | string | 官方字段 `viewer_watch_status`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.event.if_viewer_can_see_going_button` | null | 官方示例为 null，未说明非空类型。 |
| `events[].rsvp_button_renderer.event.event_connection_data_privacy_scope` | null | 官方示例为 null，未说明非空类型。 |
| `events[].rsvp_button_renderer.event.privacy_scope_for_toast` | null | 官方示例为 null，未说明非空类型。 |
| `events[].rsvp_button_renderer.event.can_join_group_chat` | boolean | 官方字段 `can_join_group_chat`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.event.created_for_group` | null | 官方示例为 null，未说明非空类型。 |
| `events[].rsvp_button_renderer.event.chat` | null | 官方示例为 null，未说明非空类型。 |
| `events[].rsvp_button_renderer.__module_operation_EventCometUniversalRSVPButton_event` | object | 官方字段 `__module_operation_EventCometUniversalRSVPButton_event`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.__module_operation_EventCometUniversalRSVPButton_event.__dr` | string | 官方字段 `__dr`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.__module_component_EventCometUniversalRSVPButton_event` | object | 官方字段 `__module_component_EventCometUniversalRSVPButton_event`；官方未单独提供业务说明。 |
| `events[].rsvp_button_renderer.__module_component_EventCometUniversalRSVPButton_event.__dr` | string | 官方字段 `__dr`；官方未单独提供业务说明。 |
| `events[].parent_if_exists_or_self` | object | 官方字段 `parent_if_exists_or_self`；官方未单独提供业务说明。 |
| `events[].parent_if_exists_or_self.online_event_setup` | null | 官方示例为 null，未说明非空类型。 |
| `events[].parent_if_exists_or_self.id` | string | 标识符。 |
| `events[].live_virtual_event_info` | null | 官方示例为 null，未说明非空类型。 |
| `events[].__typename` | string | 官方字段 `__typename`；官方未单独提供业务说明。 |
| `events[].social_context` | object | 官方字段 `social_context`；官方未单独提供业务说明。 |
| `events[].social_context.text` | string | 文本内容。 |
| `events[].social_context.ranges` | array | 官方示例为空数组，未提供元素结构。 |
| `events[].social_context.interested_count` | integer | 官方字段 `interested_count`；官方未单独提供业务说明。 |
| `events[].social_context.going_count` | integer | 官方字段 `going_count`；官方未单独提供业务说明。 |
| `events[].social_context.went_count` | null | 官方示例为 null，未说明非空类型。 |
| `cursor` | string | 分页游标。 |

## 使用要点

- 城市活动。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-events" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/events/explore/los-angeles-california/112035925469106/", "time": "this_week"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/facebook/events/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

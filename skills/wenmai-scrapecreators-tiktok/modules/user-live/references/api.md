# Wenmai SCRAPECREATORS scrapecreators_tiktok_user_live API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-user-live`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_user_live`
- **脚本入口**：`modules/user-live/scripts/user_live.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `handle` | string | 是 | TikTok 用户名，不带 @。 |

## 请求示例

```json
{
  "handle": "gymshark"
}
```

```bash
python3 modules/user-live/scripts/user_live.py '{"handle": "gymshark"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `is_live` | boolean | 是否正在直播。 |
| `liveRoomUserInfo` | object | 官方字段 `liveRoomUserInfo`；官方未单独提供业务说明。 |
| `liveRoomUserInfo.avatarLarger` | string | 大尺寸头像链接。 |
| `liveRoomUserInfo.avatarMedium` | string | 中等尺寸头像链接。 |
| `liveRoomUserInfo.avatarThumb` | string | 缩略头像链接。 |
| `liveRoomUserInfo.id` | string | 标识符。 |
| `liveRoomUserInfo.nickname` | string | 昵称。 |
| `liveRoomUserInfo.secUid` | string | 官方字段 `secUid`；官方未单独提供业务说明。 |
| `liveRoomUserInfo.secret` | boolean | 官方字段 `secret`；官方未单独提供业务说明。 |
| `liveRoomUserInfo.uniqueId` | string | 账号唯一名称。 |
| `liveRoomUserInfo.verified` | boolean | 是否认证。 |
| `liveRoomUserInfo.roomId` | string | 官方字段 `roomId`；官方未单独提供业务说明。 |
| `liveRoomUserInfo.signature` | string | 官方字段 `signature`；官方未单独提供业务说明。 |
| `liveRoomUserInfo.status` | integer | 状态。 |
| `liveRoomUserInfo.followStatus` | integer | 官方字段 `followStatus`；官方未单独提供业务说明。 |
| `liveRoomUserInfo.followingCount` | integer | 关注数量。 |
| `liveRoomUserInfo.followerCount` | integer | 粉丝数量。 |
| `liveRoom` | object | 官方字段 `liveRoom`；官方未单独提供业务说明。 |
| `liveRoom.coverUrl` | string | 官方字段 `coverUrl`；官方未单独提供业务说明。 |
| `liveRoom.squareCoverImg` | string | 官方字段 `squareCoverImg`；官方未单独提供业务说明。 |
| `liveRoom.title` | string | 标题。 |
| `liveRoom.startTime` | integer | 官方字段 `startTime`；官方未单独提供业务说明。 |
| `liveRoom.status` | integer | 状态。 |
| `liveRoom.paidEvent` | object | 官方字段 `paidEvent`；官方未单独提供业务说明。 |
| `liveRoom.paidEvent.event_id` | integer | 官方字段 `event_id`；官方未单独提供业务说明。 |
| `liveRoom.paidEvent.paid_type` | integer | 官方字段 `paid_type`；官方未单独提供业务说明。 |
| `liveRoom.liveSubOnly` | integer | 官方字段 `liveSubOnly`；官方未单独提供业务说明。 |
| `liveRoom.liveRoomMode` | integer | 官方字段 `liveRoomMode`；官方未单独提供业务说明。 |
| `liveRoom.hashTagId` | integer | 官方字段 `hashTagId`；官方未单独提供业务说明。 |
| `liveRoom.gameTagId` | integer | 官方字段 `gameTagId`；官方未单独提供业务说明。 |
| `liveRoom.liveRoomStats` | object | 官方字段 `liveRoomStats`；官方未单独提供业务说明。 |
| `liveRoom.liveRoomStats.enterCount` | integer | 官方字段 `enterCount`；官方未单独提供业务说明。 |
| `liveRoom.liveRoomStats.userCount` | integer | 官方字段 `userCount`；官方未单独提供业务说明。 |
| `liveRoom.streamData` | object | 官方字段 `streamData`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data` | object | 官方字段 `pull_data`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options` | object | 官方字段 `options`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.default_quality` | object | 官方字段 `default_quality`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.default_quality.icon_type` | integer | 官方字段 `icon_type`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.default_quality.level` | integer | 官方字段 `level`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.default_quality.name` | string | 名称。 |
| `liveRoom.streamData.pull_data.options.default_quality.resolution` | string | 官方字段 `resolution`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.default_quality.sdk_key` | string | 官方字段 `sdk_key`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.default_quality.v_codec` | string | 官方字段 `v_codec`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.qualities` | array | 官方字段 `qualities`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.qualities[].icon_type` | integer | 官方字段 `icon_type`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.qualities[].level` | integer | 官方字段 `level`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.qualities[].name` | string | 名称。 |
| `liveRoom.streamData.pull_data.options.qualities[].resolution` | string | 官方字段 `resolution`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.qualities[].sdk_key` | string | 官方字段 `sdk_key`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.qualities[].v_codec` | string | 官方字段 `v_codec`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.options.show_quality_button` | boolean | 官方字段 `show_quality_button`；官方未单独提供业务说明。 |
| `liveRoom.streamData.pull_data.stream_data` | string | 官方字段 `stream_data`；官方未单独提供业务说明。 |
| `liveRoom.streamId` | string | 官方字段 `streamId`；官方未单独提供业务说明。 |
| `liveRoom.multiStreamScene` | integer | 官方字段 `multiStreamScene`；官方未单独提供业务说明。 |
| `liveRoom.multiStreamSource` | integer | 官方字段 `multiStreamSource`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData` | object | 官方字段 `hevcStreamData`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data` | object | 官方字段 `pull_data`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options` | object | 官方字段 `options`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.default_quality` | object | 官方字段 `default_quality`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.default_quality.icon_type` | integer | 官方字段 `icon_type`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.default_quality.level` | integer | 官方字段 `level`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.default_quality.name` | string | 名称。 |
| `liveRoom.hevcStreamData.pull_data.options.default_quality.resolution` | string | 官方字段 `resolution`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.default_quality.sdk_key` | string | 官方字段 `sdk_key`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.default_quality.v_codec` | string | 官方字段 `v_codec`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.qualities` | array | 官方字段 `qualities`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.qualities[].icon_type` | integer | 官方字段 `icon_type`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.qualities[].level` | integer | 官方字段 `level`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.qualities[].name` | string | 名称。 |
| `liveRoom.hevcStreamData.pull_data.options.qualities[].resolution` | string | 官方字段 `resolution`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.qualities[].sdk_key` | string | 官方字段 `sdk_key`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.qualities[].v_codec` | string | 官方字段 `v_codec`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.options.show_quality_button` | boolean | 官方字段 `show_quality_button`；官方未单独提供业务说明。 |
| `liveRoom.hevcStreamData.pull_data.stream_data` | string | 官方字段 `stream_data`；官方未单独提供业务说明。 |

## 使用要点

- 未开播时 is_live=false 仍算成功。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-user-live" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "gymshark"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/user/live/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

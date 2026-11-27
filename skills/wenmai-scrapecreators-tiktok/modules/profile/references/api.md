# Wenmai SCRAPECREATORS scrapecreators_tiktok_profile API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-profile`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_profile`
- **脚本入口**：`modules/profile/scripts/profile.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `handle` | string | 否 | TikTok 用户名，不带 @。可与 user_id 二选一。 |
| `user_id` | string | 否 | TikTok 用户数字 ID。可与 handle 二选一。 |
| `cache_max_age` | string | 否 | 若缓存中有不晚于该时效的主页数据则直接返回。可选值：1d、3d、7d、14d、30d。 |

## 请求示例

```json
{
  "handle": "gymshark",
  "cache_max_age": "7d"
}
```

```bash
python3 modules/profile/scripts/profile.py '{"handle": "gymshark", "cache_max_age": "7d"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `user` | object | 用户信息。 |
| `user.id` | string | 标识符。 |
| `user.shortId` | string | 官方字段 `shortId`；官方未单独提供业务说明。 |
| `user.uniqueId` | string | 账号唯一名称。 |
| `user.nickname` | string | 昵称。 |
| `user.avatarLarger` | string | 大尺寸头像链接。 |
| `user.avatarMedium` | string | 中等尺寸头像链接。 |
| `user.avatarThumb` | string | 缩略头像链接。 |
| `user.signature` | string | 官方字段 `signature`；官方未单独提供业务说明。 |
| `user.createTime` | integer | 创建时间。 |
| `user.verified` | boolean | 是否认证。 |
| `user.secUid` | string | 官方字段 `secUid`；官方未单独提供业务说明。 |
| `user.ftc` | boolean | 官方字段 `ftc`；官方未单独提供业务说明。 |
| `user.relation` | integer | 官方字段 `relation`；官方未单独提供业务说明。 |
| `user.openFavorite` | boolean | 官方字段 `openFavorite`；官方未单独提供业务说明。 |
| `user.bioLink` | object | 官方字段 `bioLink`；官方未单独提供业务说明。 |
| `user.bioLink.link` | string | 链接。 |
| `user.bioLink.risk` | integer | 官方字段 `risk`；官方未单独提供业务说明。 |
| `user.commentSetting` | integer | 官方字段 `commentSetting`；官方未单独提供业务说明。 |
| `user.commerceUserInfo` | object | 官方字段 `commerceUserInfo`；官方未单独提供业务说明。 |
| `user.commerceUserInfo.commerceUser` | boolean | 官方字段 `commerceUser`；官方未单独提供业务说明。 |
| `user.duetSetting` | integer | 官方字段 `duetSetting`；官方未单独提供业务说明。 |
| `user.stitchSetting` | integer | 官方字段 `stitchSetting`；官方未单独提供业务说明。 |
| `user.privateAccount` | boolean | 是否为私密账号。 |
| `user.secret` | boolean | 官方字段 `secret`；官方未单独提供业务说明。 |
| `user.isADVirtual` | boolean | 官方字段 `isADVirtual`；官方未单独提供业务说明。 |
| `user.roomId` | string | 官方字段 `roomId`；官方未单独提供业务说明。 |
| `user.uniqueIdModifyTime` | integer | 官方字段 `uniqueIdModifyTime`；官方未单独提供业务说明。 |
| `user.ttSeller` | boolean | 官方字段 `ttSeller`；官方未单独提供业务说明。 |
| `user.downloadSetting` | integer | 官方字段 `downloadSetting`；官方未单独提供业务说明。 |
| `user.profileTab` | object | 官方字段 `profileTab`；官方未单独提供业务说明。 |
| `user.profileTab.showMusicTab` | boolean | 官方字段 `showMusicTab`；官方未单独提供业务说明。 |
| `user.profileTab.showQuestionTab` | boolean | 官方字段 `showQuestionTab`；官方未单独提供业务说明。 |
| `user.profileTab.showPlayListTab` | boolean | 官方字段 `showPlayListTab`；官方未单独提供业务说明。 |
| `user.followingVisibility` | integer | 官方字段 `followingVisibility`；官方未单独提供业务说明。 |
| `user.recommendReason` | string | 官方字段 `recommendReason`；官方未单独提供业务说明。 |
| `user.nowInvitationCardUrl` | string | 官方字段 `nowInvitationCardUrl`；官方未单独提供业务说明。 |
| `user.nickNameModifyTime` | integer | 官方字段 `nickNameModifyTime`；官方未单独提供业务说明。 |
| `user.isEmbedBanned` | boolean | 官方字段 `isEmbedBanned`；官方未单独提供业务说明。 |
| `user.canExpPlaylist` | boolean | 官方字段 `canExpPlaylist`；官方未单独提供业务说明。 |
| `user.profileEmbedPermission` | integer | 官方字段 `profileEmbedPermission`；官方未单独提供业务说明。 |
| `user.language` | string | 语言。 |
| `user.eventList` | array | 官方示例为空数组，未提供元素结构。 |
| `user.suggestAccountBind` | boolean | 官方字段 `suggestAccountBind`；官方未单独提供业务说明。 |
| `user.isOrganization` | integer | 官方字段 `isOrganization`；官方未单独提供业务说明。 |
| `stats` | object | 统计信息。 |
| `stats.followerCount` | integer | 粉丝数量。 |
| `stats.followingCount` | integer | 关注数量。 |
| `stats.heart` | integer | 官方字段 `heart`；官方未单独提供业务说明。 |
| `stats.heartCount` | integer | 获赞数量。 |
| `stats.videoCount` | integer | 视频数量。 |
| `stats.diggCount` | integer | 官方字段 `diggCount`；官方未单独提供业务说明。 |
| `stats.friendCount` | integer | 官方字段 `friendCount`；官方未单独提供业务说明。 |
| `itemList` | array | 官方示例为空数组，未提供元素结构。 |

## 使用要点

- handle 与 user_id 二选一。命中缓存时官方可能不扣 credit，稳卖仍按 2 积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-profile" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "gymshark", "cache_max_age": "7d"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/profile/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

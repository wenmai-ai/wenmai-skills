# Wenmai SCRAPECREATORS scrapecreators_tiktok_collection_videos API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-collection-videos`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_tiktok_collection_videos`
- **脚本入口**：`modules/collection-videos/scripts/collection_videos.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | 公开合集链接，例如 https://www.tiktok.com/@user/collection/Name-数字ID。 |
| `cursor` | string | 否 | 分页游标，传入上一页响应中的 max_cursor。 |

## 请求示例

```json
{
  "url": "https://www.tiktok.com/@kibblemaster808/collection/Want-to-go-7665668414573546258"
}
```

```bash
python3 modules/collection-videos/scripts/collection_videos.py '{"url": "https://www.tiktok.com/@kibblemaster808/collection/Want-to-go-7665668414573546258"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `collection_id` | string | 官方字段 `collection_id`；官方未单独提供业务说明。 |
| `has_more` | boolean | 是否还有更多结果。 |
| `max_cursor` | string | 分页游标。 |
| `status_code` | integer | 状态码。 |
| `status_msg` | string | 状态说明。 |
| `videos` | array | 视频列表。 |
| `videos[].AIGCDescription` | string | 官方字段 `AIGCDescription`；官方未单独提供业务说明。 |
| `videos[].CategoryType` | integer | 官方字段 `CategoryType`；官方未单独提供业务说明。 |
| `videos[].IsHDBitrate` | boolean | 官方字段 `IsHDBitrate`；官方未单独提供业务说明。 |
| `videos[].ShowAIGC` | boolean | 官方字段 `ShowAIGC`；官方未单独提供业务说明。 |
| `videos[].anchors` | array | 官方字段 `anchors`；官方未单独提供业务说明。 |
| `videos[].anchors[].description` | string | 描述。 |
| `videos[].anchors[].type` | integer | 类型。 |
| `videos[].author` | object | 作者信息。 |
| `videos[].author.id` | string | 标识符。 |
| `videos[].author.uniqueId` | string | 账号唯一名称。 |
| `videos[].author.nickname` | string | 昵称。 |
| `videos[].createTime` | integer | 创建时间。 |
| `videos[].desc` | string | 描述。 |
| `videos[].id` | string | 标识符。 |
| `videos[].stats` | object | 统计信息。 |
| `videos[].stats.collectCount` | integer | 官方字段 `collectCount`；官方未单独提供业务说明。 |
| `videos[].stats.commentCount` | integer | 官方字段 `commentCount`；官方未单独提供业务说明。 |
| `videos[].stats.diggCount` | integer | 官方字段 `diggCount`；官方未单独提供业务说明。 |
| `videos[].stats.playCount` | integer | 官方字段 `playCount`；官方未单独提供业务说明。 |
| `videos[].stats.shareCount` | integer | 官方字段 `shareCount`；官方未单独提供业务说明。 |
| `videos[].video` | object | 视频信息。 |
| `videos[].video.duration` | integer | 时长。 |
| `videos[].video.height` | integer | 高度。 |
| `videos[].video.width` | integer | 宽度。 |
| `videos[].video.cover` | string | 官方字段 `cover`；官方未单独提供业务说明。 |

## 使用要点

- 只支持公开合集链接。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/tiktok-collection-videos" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@kibblemaster808/collection/Want-to-go-7665668414573546258"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/tiktok/collection/videos/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

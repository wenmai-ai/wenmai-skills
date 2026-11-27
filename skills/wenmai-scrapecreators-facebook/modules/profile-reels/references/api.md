# Wenmai SCRAPECREATORS scrapecreators_facebook_profile_reels API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-profile-reels`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_facebook_profile_reels`
- **脚本入口**：`modules/profile-reels/scripts/profile_reels.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | 公开 Facebook 主页链接。 |
| `cursor` | string | 否 | 分页游标。 |
| `next_page_id` | string | 否 | 与 cursor 一起翻页。 |

## 请求示例

```json
{
  "url": "https://www.facebook.com/gymshark"
}
```

```bash
python3 modules/profile-reels/scripts/profile_reels.py '{"url": "https://www.facebook.com/gymshark"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `reels` | array | 官方字段 `reels`；官方未单独提供业务说明。 |
| `reels[].id` | string | 标识符。 |
| `reels[].is_paid_partnership` | null | 官方示例为 null，未说明非空类型。 |
| `reels[].post_id` | string | 官方字段 `post_id`；官方未单独提供业务说明。 |
| `reels[].creation_time` | string | 官方字段 `creation_time`；官方未单独提供业务说明。 |
| `reels[].url` | string | 链接。 |
| `reels[].view_count` | integer | 官方字段 `view_count`；官方未单独提供业务说明。 |
| `reels[].feedback_id` | string | 官方字段 `feedback_id`；官方未单独提供业务说明。 |
| `reels[].description` | string | 描述。 |
| `reels[].video_id` | string | 官方字段 `video_id`；官方未单独提供业务说明。 |
| `reels[].thumbnail` | string | 缩略图。 |
| `reels[].play_time_in_ms` | integer | 官方字段 `play_time_in_ms`；官方未单独提供业务说明。 |
| `reels[].video_url` | string | 官方字段 `video_url`；官方未单独提供业务说明。 |
| `reels[].music` | object | 官方字段 `music`；官方未单独提供业务说明。 |
| `reels[].music.id` | string | 标识符。 |
| `reels[].music.track_title` | string | 官方字段 `track_title`；官方未单独提供业务说明。 |
| `reels[].author` | object | 作者信息。 |
| `reels[].author.id` | string | 标识符。 |
| `reels[].author.name` | string | 名称。 |
| `reels[].author.is_verified` | boolean | 是否认证。 |
| `reels[].author.url` | string | 链接。 |
| `reels[].author.image` | string | 图片信息。 |
| `cursor` | string | 分页游标。 |
| `next_page_id` | string | 官方字段 `next_page_id`；官方未单独提供业务说明。 |

## 使用要点

- 主页 Reels。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-profile-reels" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/gymshark"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/facebook/profile/reels/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

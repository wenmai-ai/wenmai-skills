# Wenmai SCRAPECREATORS scrapecreators_facebook_profile API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-profile`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_facebook_profile`
- **脚本入口**：`modules/profile/scripts/profile.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | 是 | 公开 Facebook 主页链接。 |
| `get_business_hours` | string | 否 | 为 true 时附带营业时间。 |
| `include_gated_profile` | string | 否 | 为 true 时对年龄门/私密主页也返回有限公开字段。 |
| `cache_max_age` | string | 否 | 若缓存中有不晚于该时效的数据则直接返回，官方不计 credit。 |

## 请求示例

```json
{
  "url": "https://www.facebook.com/gymshark"
}
```

```bash
python3 modules/profile/scripts/profile.py '{"url": "https://www.facebook.com/gymshark"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `adLibrary` | object | 官方字段 `adLibrary`；官方未单独提供业务说明。 |
| `adLibrary.adStatus` | string | 官方字段 `adStatus`；官方未单独提供业务说明。 |
| `adLibrary.pageId` | string | 官方字段 `pageId`；官方未单独提供业务说明。 |
| `creationDate` | string | 官方字段 `creationDate`；官方未单独提供业务说明。 |
| `businessHours` | array | 官方字段 `businessHours`；官方未单独提供业务说明。 |
| `businessHours[].monday` | object | 官方字段 `monday`；官方未单独提供业务说明。 |
| `businessHours[].monday.open` | null | 官方示例为 null，未说明非空类型。 |
| `businessHours[].monday.close` | null | 官方示例为 null，未说明非空类型。 |
| `businessHours[].monday.intervals` | array | 官方示例为空数组，未提供元素结构。 |
| `businessHours[].monday.fullText` | string | 官方字段 `fullText`；官方未单独提供业务说明。 |
| `businessHours[].tuesday` | object | 官方字段 `tuesday`；官方未单独提供业务说明。 |
| `businessHours[].tuesday.open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].tuesday.close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].tuesday.intervals` | array | 官方字段 `intervals`；官方未单独提供业务说明。 |
| `businessHours[].tuesday.intervals[].open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].tuesday.intervals[].close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].tuesday.fullText` | string | 官方字段 `fullText`；官方未单独提供业务说明。 |
| `businessHours[].wednesday` | object | 官方字段 `wednesday`；官方未单独提供业务说明。 |
| `businessHours[].wednesday.open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].wednesday.close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].wednesday.intervals` | array | 官方字段 `intervals`；官方未单独提供业务说明。 |
| `businessHours[].wednesday.intervals[].open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].wednesday.intervals[].close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].wednesday.fullText` | string | 官方字段 `fullText`；官方未单独提供业务说明。 |
| `businessHours[].thursday` | object | 官方字段 `thursday`；官方未单独提供业务说明。 |
| `businessHours[].thursday.open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].thursday.close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].thursday.intervals` | array | 官方字段 `intervals`；官方未单独提供业务说明。 |
| `businessHours[].thursday.intervals[].open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].thursday.intervals[].close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].thursday.fullText` | string | 官方字段 `fullText`；官方未单独提供业务说明。 |
| `businessHours[].friday` | object | 官方字段 `friday`；官方未单独提供业务说明。 |
| `businessHours[].friday.open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].friday.close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].friday.intervals` | array | 官方字段 `intervals`；官方未单独提供业务说明。 |
| `businessHours[].friday.intervals[].open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].friday.intervals[].close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].friday.fullText` | string | 官方字段 `fullText`；官方未单独提供业务说明。 |
| `businessHours[].saturday` | object | 官方字段 `saturday`；官方未单独提供业务说明。 |
| `businessHours[].saturday.open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].saturday.close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].saturday.intervals` | array | 官方字段 `intervals`；官方未单独提供业务说明。 |
| `businessHours[].saturday.intervals[].open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].saturday.intervals[].close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].saturday.fullText` | string | 官方字段 `fullText`；官方未单独提供业务说明。 |
| `businessHours[].sunday` | object | 官方字段 `sunday`；官方未单独提供业务说明。 |
| `businessHours[].sunday.open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].sunday.close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].sunday.intervals` | array | 官方字段 `intervals`；官方未单独提供业务说明。 |
| `businessHours[].sunday.intervals[].open` | string | 官方字段 `open`；官方未单独提供业务说明。 |
| `businessHours[].sunday.intervals[].close` | string | 官方字段 `close`；官方未单独提供业务说明。 |
| `businessHours[].sunday.fullText` | string | 官方字段 `fullText`；官方未单独提供业务说明。 |
| `id` | string | 标识符。 |
| `isPrivate` | boolean | 官方字段 `isPrivate`；官方未单独提供业务说明。 |
| `name` | string | 名称。 |
| `url` | string | 链接。 |
| `gender` | string | 官方字段 `gender`；官方未单独提供业务说明。 |
| `coverPhoto` | object | 官方字段 `coverPhoto`；官方未单独提供业务说明。 |
| `coverPhoto.focus` | object | 官方字段 `focus`；官方未单独提供业务说明。 |
| `coverPhoto.focus.x` | number | 官方字段 `x`；官方未单独提供业务说明。 |
| `coverPhoto.focus.y` | integer | 官方字段 `y`；官方未单独提供业务说明。 |
| `coverPhoto.photo` | object | 官方字段 `photo`；官方未单独提供业务说明。 |
| `coverPhoto.photo.id` | string | 标识符。 |
| `coverPhoto.photo.image` | object | 图片信息。 |
| `coverPhoto.photo.image.uri` | string | 资源标识。 |
| `coverPhoto.photo.image.width` | integer | 宽度。 |
| `coverPhoto.photo.image.height` | integer | 高度。 |
| `coverPhoto.photo.viewer_image` | object | 官方字段 `viewer_image`；官方未单独提供业务说明。 |
| `coverPhoto.photo.viewer_image.height` | integer | 高度。 |
| `coverPhoto.photo.viewer_image.width` | integer | 宽度。 |
| `coverPhoto.photo.blurred_image` | object | 官方字段 `blurred_image`；官方未单独提供业务说明。 |
| `coverPhoto.photo.blurred_image.uri` | string | 资源标识。 |
| `coverPhoto.photo.blurred_image.width` | integer | 宽度。 |
| `coverPhoto.photo.blurred_image.height` | integer | 高度。 |
| `coverPhoto.photo.url` | string | 链接。 |
| `isBusinessPageActive` | boolean | 官方字段 `isBusinessPageActive`；官方未单独提供业务说明。 |
| `profilePhoto` | object | 官方字段 `profilePhoto`；官方未单独提供业务说明。 |
| `profilePhoto.url` | string | 链接。 |
| `profilePhoto.viewer_image` | object | 官方字段 `viewer_image`；官方未单独提供业务说明。 |
| `profilePhoto.viewer_image.height` | integer | 高度。 |
| `profilePhoto.viewer_image.width` | integer | 宽度。 |
| `profilePhoto.id` | string | 标识符。 |
| `profilePicLarge` | string | 官方字段 `profilePicLarge`；官方未单独提供业务说明。 |
| `profilePicMedium` | string | 官方字段 `profilePicMedium`；官方未单独提供业务说明。 |
| `profilePicSmall` | string | 官方字段 `profilePicSmall`；官方未单独提供业务说明。 |
| `pageIntro` | string | 官方字段 `pageIntro`；官方未单独提供业务说明。 |
| `category` | string | 官方字段 `category`；官方未单独提供业务说明。 |
| `address` | string | 官方字段 `address`；官方未单独提供业务说明。 |
| `email` | string | 官方字段 `email`；官方未单独提供业务说明。 |
| `links` | array | 官方示例为空数组，未提供元素结构。 |
| `phone` | string | 官方字段 `phone`；官方未单独提供业务说明。 |
| `website` | string | 官方字段 `website`；官方未单独提供业务说明。 |
| `services` | string | 官方字段 `services`；官方未单独提供业务说明。 |
| `priceRange` | string | 官方字段 `priceRange`；官方未单独提供业务说明。 |
| `rating` | string | 官方字段 `rating`；官方未单独提供业务说明。 |
| `ratingCount` | null | 官方示例为 null，未说明非空类型。 |
| `likeCount` | integer | 官方字段 `likeCount`；官方未单独提供业务说明。 |
| `talkingAboutCount` | integer | 官方字段 `talkingAboutCount`；官方未单独提供业务说明。 |
| `followerCount` | integer | 粉丝数量。 |

## 使用要点

- 获取主页详情。每次成功扣 3 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-profile" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/gymshark"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/facebook/profile/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

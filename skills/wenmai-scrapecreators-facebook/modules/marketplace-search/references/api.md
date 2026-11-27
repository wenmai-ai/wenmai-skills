# Wenmai SCRAPECREATORS scrapecreators_facebook_marketplace_search API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-marketplace-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_facebook_marketplace_search`
- **脚本入口**：`modules/marketplace-search/scripts/marketplace_search.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `query` | string | 否 | 关键词。 |
| `lat` | number | 是 | 纬度。 |
| `lng` | number | 是 | 经度。 |
| `cursor` | string | 否 | 分页游标。 |

## 请求示例

```json
{
  "query": "gymshark",
  "lat": 34.0522,
  "lng": -118.2437
}
```

```bash
python3 modules/marketplace-search/scripts/marketplace_search.py '{"query": "gymshark", "lat": 34.0522, "lng": -118.2437}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `listings` | array | 官方字段 `listings`；官方未单独提供业务说明。 |
| `listings[].id` | string | 标识符。 |
| `listings[].url` | string | 链接。 |
| `listings[].title` | string | 标题。 |
| `listings[].creation_time` | null | 官方示例为 null，未说明非空类型。 |
| `listings[].listing_date_text` | null | 官方示例为 null，未说明非空类型。 |
| `listings[].price` | object | 官方字段 `price`；官方未单独提供业务说明。 |
| `listings[].price.formatted_amount` | string | 官方字段 `formatted_amount`；官方未单独提供业务说明。 |
| `listings[].price.amount_with_offset_in_currency` | integer | 官方字段 `amount_with_offset_in_currency`；官方未单独提供业务说明。 |
| `listings[].price.amount` | integer | 官方字段 `amount`；官方未单独提供业务说明。 |
| `listings[].strikethrough_price` | null | 官方示例为 null，未说明非空类型。 |
| `listings[].location` | object | 位置信息。 |
| `listings[].location.city` | string | 官方字段 `city`；官方未单独提供业务说明。 |
| `listings[].location.state` | string | 官方字段 `state`；官方未单独提供业务说明。 |
| `listings[].location.display_name` | string | 官方字段 `display_name`；官方未单独提供业务说明。 |
| `listings[].location.city_page_id` | string | 官方字段 `city_page_id`；官方未单独提供业务说明。 |
| `listings[].primary_photo` | object | 官方字段 `primary_photo`；官方未单独提供业务说明。 |
| `listings[].primary_photo.id` | string | 标识符。 |
| `listings[].primary_photo.url` | string | 链接。 |
| `listings[].category_id` | string | 官方字段 `category_id`；官方未单独提供业务说明。 |
| `listings[].is_hidden` | boolean | 官方字段 `is_hidden`；官方未单独提供业务说明。 |
| `listings[].is_live` | boolean | 是否正在直播。 |
| `listings[].is_pending` | boolean | 官方字段 `is_pending`；官方未单独提供业务说明。 |
| `listings[].is_sold` | boolean | 官方字段 `is_sold`；官方未单独提供业务说明。 |
| `listings[].is_viewer_seller` | boolean | 官方字段 `is_viewer_seller`；官方未单独提供业务说明。 |
| `listings[].delivery_types` | array | 官方字段 `delivery_types`；官方未单独提供业务说明。 |
| `listings[].delivery_types[]` | string | 官方数组 `delivery_types` 的元素。 |
| `listings[].story_type` | string | 官方字段 `story_type`；官方未单独提供业务说明。 |
| `listings[].story_key` | string | 官方字段 `story_key`；官方未单独提供业务说明。 |
| `cursor` | string | 分页游标。 |
| `has_next_page` | boolean | 是否存在下一页。 |

## 使用要点

- Marketplace 搜索。lat/lng 必填。每次成功扣 2 稳卖积分。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/facebook-marketplace-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "gymshark", "lat": 34.0522, "lng": -118.2437}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/facebook/marketplace/search/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

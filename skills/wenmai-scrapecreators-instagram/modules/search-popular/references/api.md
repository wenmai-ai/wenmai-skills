# Wenmai SCRAPECREATORS scrapecreators_instagram_search_popular API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-search-popular`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_instagram_search_popular`
- **脚本入口**：`modules/search-popular/scripts/search_popular.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `2`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `query` | string | 是 | Instagram Popular 专题词，例如 music。不要传品牌名或账号名。 |
| `cursor` | string | 否 | 上一页返回的不透明游标，需与同一 query 一起传入。 |

## 请求示例

```json
{
  "query": "music"
}
```

```bash
python3 modules/search-popular/scripts/search_popular.py '{"query": "music"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `query` | string | 本次查询词。 |
| `title` | string | 标题。 |
| `total_media_count` | integer | 官方字段 `total_media_count`；官方未单独提供业务说明。 |
| `description` | object | 描述。 |
| `description.plain_text` | string | 官方字段 `plain_text`；官方未单独提供业务说明。 |
| `description.source_uris` | array | 官方字段 `source_uris`；官方未单独提供业务说明。 |
| `description.source_uris[]` | string | 官方数组 `source_uris` 的元素。 |
| `description.linked_terms` | array | 官方示例为空数组，未提供元素结构。 |
| `suggested_terms` | array | 官方字段 `suggested_terms`；官方未单独提供业务说明。 |
| `suggested_terms[]` | string | 官方数组 `suggested_terms` 的元素。 |
| `posts` | array | 帖子列表。 |
| `posts[].id` | string | 标识符。 |
| `posts[].shortcode` | string | 官方字段 `shortcode`；官方未单独提供业务说明。 |
| `posts[].url` | string | 链接。 |
| `posts[].type` | string | 类型。 |
| `posts[].caption` | string | 说明文字。 |
| `posts[].display_url` | string | 官方字段 `display_url`；官方未单独提供业务说明。 |
| `posts[].video_url` | string | 官方字段 `video_url`；官方未单独提供业务说明。 |
| `posts[].play_count` | integer | 播放数量。 |
| `posts[].owner` | object | 所属账号。 |
| `posts[].owner.id` | string | 标识符。 |
| `posts[].owner.username` | string | 用户名。 |
| `posts[].owner.is_verified` | boolean | 是否认证。 |
| `posts[].owner.profile_pic_url` | string | 头像链接。 |
| `cursor` | string | 分页游标。 |
| `has_more` | boolean | 是否还有更多结果。 |

## 使用要点

- 刮的是 Instagram 公开专题页 /popular/{词}，不是普通搜索。只用 music、travel 这类专题词；品牌名 gymshark、官方示例 basketball 都可能没有专题页。失败后改打 search-hashtag 或 reels-search。每次成功扣 2 稳卖积分。
- 顶层直接传业务字段，不要增加 `request` 包装层。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、handle、userId、帖子链接、视频链接和分页。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/instagram-search-popular" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "music"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/instagram/search/popular/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

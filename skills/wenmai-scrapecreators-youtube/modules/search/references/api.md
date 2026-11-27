# Wenmai SCRAPECREATORS scrapecreators_youtube_search API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/youtube-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`scrapecreators_youtube_search`
- **脚本入口**：`modules/search/scripts/search.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值
- **稳卖积分**：成功时 `costCredit` 为 `3`。

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `query` | string | 是 | 搜索词。可用 intitle: 做更严格的标题匹配。 |
| `uploadDate` | string | 否 | 按上传时间筛选：today、this_week、this_month、this_year。 |
| `sortBy` | string | 否 | 排序方式：relevance 或 popular。 |
| `type` | string | 否 | 搜索内容类型：videos、shorts、channels、playlists。 |
| `duration` | string | 否 | 视频时长筛选，只对普通视频生效。 |
| `region` | string | 否 | 代理所在地区，两位国家码如 US。 |
| `includeExtras` | string | 否 | 是否附带点赞、评论数和简介。会变慢，不要当默认。 |
| `continuationToken` | string | 否 | 分页游标，传入上一页响应中的 continuationToken。 |

## 请求示例

```json
{
  "query": "gymshark",
  "region": "US"
}
```

```bash
python3 modules/search/scripts/search.py '{"query": "gymshark", "region": "US"}'
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode`、`costCredit` 和 `data`；下表描述文档所列业务数据字段。对外 `data` 不包含官方 `credits_remaining`、`credits_charged`。

| 字段 | 类型 | 说明 |
|---|---|---|
| `success` | boolean | 请求是否成功。 本表按官方成功示例整理（2026-11-26），非本次线上实测；字段是示例并集，不表示每次必返。 |
| `videos` | array | 视频列表。 |
| `videos[].type` | string | 类型。 |
| `videos[].id` | string | 标识符。 |
| `videos[].url` | string | 链接。 |
| `videos[].title` | string | 标题。 |
| `videos[].thumbnail` | string | 缩略图。 |
| `videos[].channel` | object | 频道。 |
| `videos[].channel.id` | string | 标识符。 |
| `videos[].channel.title` | string | 标题。 |
| `videos[].channel.handle` | string | 账号名称。 |
| `videos[].channel.thumbnail` | string | 缩略图。 |
| `videos[].viewCountText` | string | 浏览量展示文本。 |
| `videos[].viewCountInt` | integer | 浏览量。 |
| `videos[].publishedTimeText` | string | 发布时间展示文本。 |
| `videos[].publishedTime` | string | 发布时间。 |
| `videos[].lengthText` | string | 时长展示文本。 |
| `videos[].lengthSeconds` | integer | 官方字段 `lengthSeconds`；官方未单独提供业务说明。 |
| `videos[].badges` | array | 徽章信息。 |
| `videos[].badges[]` | string | 徽章信息中的元素。 |
| `channels` | array | 官方示例为空数组，未提供元素结构。 |
| `playlists` | array | 官方示例为空数组，未提供元素结构。 |
| `shorts` | array | 官方字段 `shorts`；官方未单独提供业务说明。 |
| `shorts[].type` | string | 类型。 |
| `shorts[].id` | string | 标识符。 |
| `shorts[].url` | string | 链接。 |
| `shorts[].title` | string | 标题。 |
| `shorts[].thumbnail` | string | 缩略图。 |
| `shorts[].channel` | object | 频道。 |
| `shorts[].channel.id` | string | 标识符。 |
| `shorts[].channel.title` | string | 标题。 |
| `shorts[].channel.handle` | string | 账号名称。 |
| `shorts[].channel.thumbnail` | string | 缩略图。 |
| `shorts[].viewCountText` | string | 浏览量展示文本。 |
| `shorts[].viewCountInt` | integer | 浏览量。 |
| `shorts[].publishedTimeText` | string | 发布时间展示文本。 |
| `shorts[].publishedTime` | string | 发布时间。 |
| `shorts[].lengthText` | string | 时长展示文本。 |
| `shorts[].lengthSeconds` | integer | 官方字段 `lengthSeconds`；官方未单独提供业务说明。 |
| `shorts[].badges` | array | 官方示例为空数组，未提供元素结构。 |
| `shelves` | array | 官方字段 `shelves`；官方未单独提供业务说明。 |
| `shelves[].type` | string | 类型。 |
| `shelves[].title` | string | 标题。 |
| `shelves[].items` | array | 结果条目。 |
| `shelves[].items[].type` | string | 类型。 |
| `shelves[].items[].id` | string | 标识符。 |
| `shelves[].items[].url` | string | 链接。 |
| `shelves[].items[].title` | string | 标题。 |
| `shelves[].items[].thumbnail` | string | 缩略图。 |
| `shelves[].items[].viewCountText` | string | 浏览量展示文本。 |
| `shelves[].items[].viewCountInt` | integer | 浏览量。 |
| `lives` | array | 官方示例为空数组，未提供元素结构。 |
| `continuationToken` | string | 续页令牌。 |

## 使用要点

- 搜索视频、频道、播放列表、Shorts 和直播。每次成功扣 3 稳卖积分。
- 顶层直接传业务字段，不要增加 `request` 包装层。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、handle、channelId、视频链接、播放列表 ID、continuationToken 和分页。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/scrapecreators/youtube-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "gymshark", "region": "US"}'
```

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。官方接口文档：https://docs.scrapecreators.com/v1/youtube/search/；响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

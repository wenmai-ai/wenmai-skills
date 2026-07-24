# Wenmai Alpha Instagram Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/instagram-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_instagram_scraper`
- **接口说明**：Instagram Scraper
- **脚本入口**：`scripts/alpha_instagram_scraper.py`，脚本参数即标准 API POST Body JSON

### 运行时覆盖

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `WENMAI_API_ORIGIN` | Wenmai API 地址 | `https://all-api.wenmai-ai.com` |
| `WENMAI_API_BASE_PATH` | 标准 API Base Path | `/wmapi/v1` |
| `WENMAI_API_TIMEOUT` | HTTP 超时时间，单位秒 | `120` |

## 请求参数

POST Body（JSON）：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `resultsType` | string | 否 | resultsType 字段。可选值：posts、details、comments、reels、mentions、stories。 |
| `directUrls` | array | 否 | 页面链接列表。 |
| `resultsLimit` | integer | 否 | 最大采集或返回数量。 |
| `onlyPostsNewerThan` | string | 否 | 是否启用该选项。 |
| `search` | string | 否 | search 字段。 |
| `searchType` | string | 否 | searchType 字段。可选值：hashtag、profile、place、user。 |
| `searchLimit` | integer | 否 | 最大采集或返回数量。 |
| `addParentData` | boolean | 否 | addParentData 字段。 |

## 请求示例

脚本入参示例：

```json
{
  "search": "keyboard",
  "directUrls": [
    "https://www.instagram.com/humansofny/"
  ],
  "searchType": "hashtag",
  "resultsType": "posts",
  "searchLimit": 3,
  "resultsLimit": 3,
  "addParentData": false
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | number | ID 标识。 |
| `type` | string | 采集模式。 |
| `shortCode` | string | shortCode 字段。 |
| `caption` | string | 标题。 |
| `hashtags` | boolean | 搜索关键词列表。 |
| `mentions` | string | mentions 字段。 |
| `url` | string | 链接地址。 |
| `commentsCount` | number | 评论列表。 |
| `firstComment` | string | 评论列表。 |
| `latestComments` | array | 评论列表。 |
| `latestComments.id` | number | ID 标识。 |
| `latestComments.text` | array | 文本内容。 |
| `latestComments.ownerUsername` | array | 作者信息。 |
| `latestComments.ownerProfilePicUrl` | array | 链接地址。 |
| `latestComments.timestamp` | array | 时间或日期。 |
| `latestComments.repliesCount` | number | 数量。 |
| `latestComments.replies` | array | replies 字段。 |
| `latestComments.likesCount` | number | 数量。 |
| `latestComments.owner` | array | owner 字段。 |
| `latestComments.owner.username` | array | 作者信息。 |
| `latestComments.owner.profile_pic_url` | array | 链接地址。 |
| `latestComments.owner.is_verified` | boolean | 是否启用该选项。 |
| `latestComments.owner.id` | number | ID 标识。 |
| `latestComments.owner.full_name` | array | full_name 字段。 |
| `latestComments.owner.is_mentionable` | boolean | 是否启用该选项。 |
| `latestComments.owner.is_private` | boolean | 是否启用该选项。 |
| `latestComments.owner.profile_pic_id` | number | ID 标识。 |
| `latestComments.owner.latest_reel_media` | array | latest_reel_media 字段。 |
| `dimensionsHeight` | string | dimensionsHeight 字段。 |
| `dimensionsWidth` | number | dimensionsWidth 字段。 |
| `displayUrl` | boolean | 链接地址。 |
| `images` | array | 图片列表。 |
| `alt` | string | alt 字段。 |
| `likesCount` | number | 数量。 |
| `timestamp` | string | 时间或日期。 |
| `childPosts` | string | childPosts 字段。 |
| `childPosts.id` | number | ID 标识。 |
| `childPosts.type` | string | 采集模式。 |
| `childPosts.caption` | string | 标题。 |
| `childPosts.hashtags` | boolean | 搜索关键词列表。 |
| `childPosts.mentions` | string | mentions 字段。 |
| `childPosts.url` | string | 链接地址。 |
| `childPosts.commentsCount` | number | 评论列表。 |
| `childPosts.firstComment` | string | 评论列表。 |
| `childPosts.latestComments` | array | 评论列表。 |
| `childPosts.dimensionsHeight` | string | dimensionsHeight 字段。 |
| `childPosts.dimensionsWidth` | number | dimensionsWidth 字段。 |
| `childPosts.displayUrl` | boolean | 链接地址。 |
| `childPosts.images` | array | 图片列表。 |
| `childPosts.alt` | string | alt 字段。 |
| `childPosts.likesCount` | number | 数量。 |
| `childPosts.timestamp` | string | 时间或日期。 |
| `childPosts.childPosts` | string | childPosts 字段。 |
| `childPosts.ownerId` | number | ID 标识。 |
| `childPosts.shortCode` | string | shortCode 字段。 |
| `childPosts.originalHeight` | string | originalHeight 字段。 |
| `childPosts.originalWidth` | number | originalWidth 字段。 |
| `childPosts.ownerUsername` | string | 作者信息。 |
| `ownerFullName` | string | ownerFullName 字段。 |
| `ownerUsername` | string | 作者信息。 |
| `ownerId` | number | ID 标识。 |
| `isPinned` | boolean | 是否启用该选项。 |
| `isCommentsDisabled` | boolean | 是否启用该选项。 |
| `inputUrl` | string | 链接地址。 |
| `originalHeight` | string | originalHeight 字段。 |
| `originalWidth` | number | originalWidth 字段。 |
| `productType` | string | productType 字段。 |

## 使用要点

- 本接口适合：Instagram 账号、话题和内容。
- 优先使用用户给定的 URL、关键词、商品 ID、站点、国家、语言、排序、分页和数量限制。
- 采集类接口的字段会随目标平台页面结构变化；输出分析时保留原始字段名和 URL，避免把缺失字段补写成事实。
- 当用户需要多平台对比时，分别调用对应 Alpha 原子 Skill，再在上层分析中合并结果。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按上方请求参数表修正枚举值、日期格式、分页范围、URL/关键词数组、数量范围或必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/instagram-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search": "keyboard", "directUrls": ["https://www.instagram.com/humansofny/"], "searchType": "hashtag", "resultsType": "posts", "searchLimit": 3, "resultsLimit": 3, "addParentData": false}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

# Wenmai Alpha Xiaohongshu Pro Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/xiaohongshu-pro-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_xiaohongshu_pro_scraper`
- **接口说明**：Xiaohongshu (RedNote) Pro Scraper
- **脚本入口**：`scripts/alpha_xiaohongshu_pro_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `mode` | string | 否 | 采集模式。常用值包括 search、notes、user、topic、hotsearch、suggest、trending。使用 `notes` 会启用单独计费的完整笔记详情能力。 |
| `keywords` | array | 否 | 搜索关键词列表。 |
| `noteUrls` | array | 否 | `mode` 为 `notes` 时要抓取完整详情的笔记链接。该模式会单独计费；仅在用户明确要求时传入。 |
| `noteType` | string | 否 | noteType 字段。 |
| `sortType` | string | 否 | 排序方式。 |
| `timeFilter` | string | 否 | 时间或日期。 |
| `fetchComments` | boolean | 否 | 是否额外抓取笔记评论。设为 `true` 会启用额外的详情处理并需要单独计费；仅在用户明确要求时使用。 |
| `maxItemsPerInput` | integer | 否 | 最大采集或返回数量。 |

### 额外计费提醒

不要自动选择 `mode: "notes"`、补充 `noteUrls` 或启用 `fetchComments`。只有用户明确要求完整笔记详情或评论时才使用，并在请求前提醒用户相关能力需要单独计费。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "mode": "search",
  "keywords": [
    "AI"
  ],
  "noteType": "不限",
  "sortType": "general",
  "timeFilter": "不限",
  "fetchComments": false,
  "maxItemsPerInput": 3
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `noteId` | number | ID 标识。 |
| `title` | string | 标题。 |
| `bodyText` | string | 文本内容。 |
| `author` | string | 作者信息。 |
| `authorId` | number | ID 标识。 |
| `likes` | number | likes 字段。 |
| `collects` | string | collects 字段。 |
| `commentsCount` | number | 评论列表。 |
| `shares` | number | shares 字段。 |
| `hashtags` | boolean | 搜索关键词列表。 |
| `imageUrls` | array | 页面链接列表。 |
| `videoUrl` | string | 链接地址。 |
| `publishedAt` | boolean | 时间或日期。 |
| `isVideo` | number | 是否启用该选项。 |
| `location` | string | location 字段。 |
| `noteUrl` | string | 链接地址。 |
| `comments` | array | 评论列表。 |
| `_cursorScore` | number | 评分。 |
| `_createTime` | string | 时间或日期。 |
| `keyword` | string | 搜索关键词。 |
| `scrapedAt` | string | scrapedAt 字段。 |

## 使用要点

- 本接口适合：小红书笔记、关键词和内容趋势。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/xiaohongshu-pro-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode": "search", "keywords": ["AI"], "noteType": "不限", "sortType": "general", "timeFilter": "不限", "fetchComments": false, "maxItemsPerInput": 3}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。

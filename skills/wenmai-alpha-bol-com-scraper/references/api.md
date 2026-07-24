# Wenmai Alpha Bol Com Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/bol-com-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_bol_com_scraper`
- **接口说明**：Bol.com Price Tracker - NL/BE Drops + AI Briefs
- **脚本入口**：`scripts/alpha_bol_com_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `bolClientId` | string | 否 | ID 标识。 |
| `bolClientSecret` | string | 否 | bolClientSecret 字段。 |
| `mode` | string | 否 | 采集模式。可选值：search、product_url、bestsellers。 |
| `searchQuery` | string | 否 | 搜索关键词。 |
| `query` | string | 否 | 搜索关键词。 |
| `q` | string | 否 | q 字段。 |
| `keyword` | string | 否 | 搜索关键词。 |
| `searchTerm` | string | 否 | searchTerm 字段。 |
| `productUrls` | array<string> | 否 | 页面链接列表。 |
| `urls` | array<string> | 否 | 页面链接列表。 |
| `url` | string | 否 | 链接地址。 |
| `productUrl` | string | 否 | 链接地址。 |
| `links` | array<string> | 否 | 页面链接列表。 |
| `category` | string | 否 | 分类。 |
| `maxProducts` | integer | 否 | 最大采集或返回数量。 |
| `sortBy` | string | 否 | 排序方式。可选值：relevance、popularity、price_asc、price_desc、rating、newest。 |
| `maxItems` | integer | 否 | 最大采集或返回数量。 |
| `maxResults` | integer | 否 | 最大采集或返回数量。 |
| `fetchDetails` | boolean | 否 | 是否启用该选项。 |
| `includeDetails` | boolean | 否 | 是否启用该选项。 |
| `country` | string | 否 | 国家或站点。可选值：nl、be。 |
| `watchMode` | boolean | 否 | 是否跨运行保存价格历史并检测变化。设为 `true` 后会启用单独计费的价格监控能力；仅在用户明确要求时使用。 |
| `enableAiAnalysis` | boolean | 否 | 是否生成 AI 市场分析。设为 `true` 后会启用单独计费的 AI 分析能力；仅在用户明确要求时使用。 |
| `llmProvider` | string | 否 | llmProvider 字段。可选值：openrouter、anthropic、google、openai、ollama。 |
| `llmModel` | string | 否 | llmModel 字段。 |
| `openrouterApiKey` | string | 否 | openrouterApiKey 字段。 |
| `anthropicApiKey` | string | 否 | anthropicApiKey 字段。 |
| `googleApiKey` | string | 否 | googleApiKey 字段。 |
| `openaiApiKey` | string | 否 | openaiApiKey 字段。 |
| `ollamaBaseUrl` | string | 否 | 链接地址。 |

### 额外计费提醒

`watchMode: true` 和 `enableAiAnalysis: true` 会分别启用单独计费的能力。普通商品采集请求应省略这两个参数或保持 `false`。没有对应输入参数的供应商事件不得描述成可选参数。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "q": "keyboard",
  "url": "https://www.amazon.com/s?k=keyboard",
  "mode": "search",
  "urls": [
    "https://www.amazon.com/s?k=keyboard"
  ],
  "query": "keyboard",
  "sortBy": "relevance",
  "country": "be",
  "keyword": "keyboard",
  "category": "keyboard",
  "llmModel": "keyboard",
  "maxItems": 3,
  "watchMode": false,
  "maxResults": 3,
  "productUrl": "https://www.amazon.com/s?k=keyboard",
  "searchTerm": "keyboard",
  "bolClientId": "keyboard",
  "llmProvider": "openrouter",
  "maxProducts": 3,
  "productUrls": [
    "https://www.amazon.com/s?k=keyboard"
  ],
  "searchQuery": "PlayStation 5",
  "fetchDetails": false,
  "googleApiKey": "keyboard",
  "openaiApiKey": "keyboard",
  "ollamaBaseUrl": "http://localhost:11434",
  "includeDetails": false,
  "anthropicApiKey": "keyboard",
  "bolClientSecret": "keyboard",
  "enableAiAnalysis": false,
  "openrouterApiKey": "keyboard"
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `alternative_prices` | array | 价格。 |
| `categories` | array | categories 字段。 |
| `images` | array<string> | 图片列表。 |
| `has_refurbished` | boolean | 是否启用该选项。 |
| `has_select_deal` | boolean | 是否启用该选项。 |
| `sponsored` | boolean | sponsored 字段。 |
| `discount_percentage` | number | 数量。 |
| `in_stock` | null | 库存信息。 |
| `list_price` | number | 价格。 |
| `price` | number | 价格。 |
| `products_found` | number | products_found 字段。 |
| `rating` | number | 评分。 |
| `rating_count` | number | 评分。 |
| `availability` | string | 库存信息。 |
| `brand` | string | 品牌。 |
| `country` | string | 国家或站点。 |
| `currency` | string | 币种。 |
| `delivery_text` | string | delivery_text 字段。 |
| `description` | string | 描述。 |
| `ean` | string | ean 字段。 |
| `generated_at` | string | generated_at 字段。 |
| `mode` | string | 采集模式。 |
| `price_currency` | string | 币种。 |
| `product_id` | string | ID 标识。 |
| `scraped_at` | string | scraped_at 字段。 |
| `search_query` | string | search_query 字段。 |
| `seller` | string | 卖家信息。 |
| `title` | string | 标题。 |
| `type` | string | 采集模式。 |
| `url` | string | 链接地址。 |
| `product_urls_count` | number | 页面链接列表。 |
| `category` | string | 分类。 |

## 使用要点

- 本接口适合：Bol.com 商品池。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/bol-com-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "keyboard", "url": "https://www.amazon.com/s?k=keyboard", "mode": "search", "urls": ["https://www.amazon.com/s?k=keyboard"], "query": "keyboard", "sortBy": "relevance", "country": "be", "keyword": "keyboard", "category": "keyboard", "llmModel": "keyboard", "maxItems": 3, "watchMode": false, "maxResults": 3, "productUrl": "https://www.amazon.com/s?k=keyboard", "searchTerm": "keyboard", "bolClientId": "keyboard", "llmProvider": "openrouter", "maxProducts": 3, "productUrls": ["https://www.amazon.com/s?k=keyboard"], "searchQuery": "PlayStation 5", "fetchDetails": false, "googleApiKey": "keyboard", "openaiApiKey": "keyboard", "ollamaBaseUrl": "http://localhost:11434", "includeDetails": false, "anthropicApiKey": "keyboard", "bolClientSecret": "keyboard", "enableAiAnalysis": false, "openrouterApiKey": "keyboard"}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。

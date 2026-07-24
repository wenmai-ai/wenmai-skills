# Wenmai Alpha Google Trends Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/google-trends-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_google_trends_scraper`
- **接口说明**：google-trends-scraper
- **脚本入口**：`scripts/alpha_google_trends_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `searchTerms` | array | 否 | 搜索关键词列表。 |
| `isMultiple` | boolean | 否 | 是否启用该选项。 |
| `timeRange` | string | 否 | 时间或日期。可选值：now 1-H、now 4-H、now 1-d、now 7-d、today 1-m、today 3-m、today 5-y、all。 |
| `geo` | string | 否 | 国家或站点。可选值：AF、AL、DZ、AS、AD、AO、AI、AQ、AG、AR、AM、AW、AU、AT、AZ、BS、BH、BD、BB、BY、BE、BZ、BJ、BM、BT、BO、BQ、BA、BW、BV、BR、IO、BN、BG、BF、BI、CV、KH、CM、CA、KY、CF、TD、CL、CN、CX、Keeling Islands 、CO、KM、CG、CD、CK、CR、CI、HR、CU、CW、CY、CZ、DK、DJ、DM、DO、EC、EG、SV、GQ、ER、EE、ET、Malvinas 、FO、FJ、FI、FR、GF、PF、TF、GA、GM、等。 |
| `viewedFrom` | string | 否 | viewedFrom 字段。可选值：us、af、al、dz、as、ad、ao、ai、aq、ag、ar、am、aw、au、at、az、bs、bh、bd、bb、by、be、bz、bj、bm、bt、bo、ba、bw、bv、br、io、bn、bg、bf、bi、kh、cm、ca、cv、ky、cf、td、cl、cn、cx、cc、co、km、cg、cd、ck、cr、ci、hr、cu、cy、cz、dk、dj、dm、do、ec、eg、sv、gq、er、ee、et、fk、fo、fj、fi、fr、gf、pf、tf、ga、gm、ge、等。 |
| `skipDebugScreen` | boolean | 否 | skipDebugScreen 字段。 |
| `startUrls` | array | 否 | 页面链接列表。 |
| `spreadsheetId` | string | 否 | ID 标识。 |
| `category` | string | 否 | 分类。可选值：3、47、44、22、12、5、7、71、8、45、65、11、13、958、19、16、299、14、66、29、533、174、18、20、67。 |
| `maxItems` | integer | 否 | 最大采集或返回数量。 |
| `customTimeRange` | string | 否 | 时间或日期。 |
| `maxConcurrency` | integer | 否 | 币种。 |
| `maxRequestRetries` | integer | 否 | 最大采集或返回数量。 |
| `pageLoadTimeoutSecs` | integer | 否 | 时间或日期。 |

## 请求示例

脚本入参示例：

```json
{
  "geo": "",
  "category": "",
  "maxItems": 0,
  "startUrls": [
    {
      "url": "https://trends.google.com/trends/explore?q=web+scraping&geo=US"
    }
  ],
  "timeRange": "",
  "isMultiple": false,
  "viewedFrom": "",
  "searchTerms": [
    "webscraping"
  ],
  "spreadsheetId": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms",
  "maxConcurrency": 3,
  "customTimeRange": "2024-01-01 2024-12-31",
  "skipDebugScreen": false,
  "maxRequestRetries": 3,
  "pageLoadTimeoutSecs": 3
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `searchTerm` | string | 搜索关键词。 |
| `date` | string | 日期。 |
| `value` | number | 趋势热度值。 |
| `geo` | string | 地区代码。 |
| `timeRange` | string | 时间范围。 |
| `relatedQueries` | array | 相关查询列表。 |
| `risingQueries` | array | 上升查询列表。 |

## 使用要点

- 本接口适合：Google Search / SERP / Trends。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/google-trends-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"geo": "", "category": "", "maxItems": 0, "startUrls": [{"url": "https://trends.google.com/trends/explore?q=web+scraping&geo=US"}], "timeRange": "", "isMultiple": false, "viewedFrom": "", "searchTerms": ["webscraping"], "spreadsheetId": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms", "maxConcurrency": 3, "customTimeRange": "2024-01-01 2024-12-31", "skipDebugScreen": false, "maxRequestRetries": 3, "pageLoadTimeoutSecs": 3}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

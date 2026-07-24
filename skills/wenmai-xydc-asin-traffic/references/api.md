# Wenmai XYDC asin流量得分 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/xydc/get-asin-traffic`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`get_asin_traffic`
- **接口说明**：asin流量得分。
- **脚本入口**：`scripts/xydc_asin_traffic.py`，脚本参数即标准 API POST Body JSON

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
| `asins` | Array | 是 | ASIN 列表；示例：`["B09PCSR9SX"]`。 |
| `country` | string | 是 | 站点国家码，如 US/UK/DE；示例：`US`。 |

## 请求示例

```json
{
  "asins": [
    "B09PCSR9SX"
  ],
  "country": "US"
}
```

## 响应结构

公共响应字段：`code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.entities` | Array | data.entities 字段。 |
| `data.entities[].country` | string | 国家。 |
| `data.entities[].asin` | string | ASIN。 |
| `data.entities[].organicTrafficScore` | integer | 近7天自然流量得分。 |
| `data.entities[].advertisingTrafficScore` | integer | 近7天广告流量得分。 |
| `data.entities[].totalTrafficScore` | integer | 近7天总流量得分。 |
| `data.entities[].organicSearchTermCount` | integer | 近7天自然关键词数量。 |
| `data.entities[].advertisingSearchTermCount` | integer | 近7天广告关键词数量。 |
| `data.entities[].previous7DaysOrganicTrafficScore` | integer | 前一个7天自然流量得分。 |
| `data.entities[].previous7DaysAdvertisingTrafficScore` | integer | 前一个7天广告流量得分。 |
| `data.entities[].previous7DaysTotalTrafficScore` | integer | 前一个7天总流量得分。 |
| `data.entities[].organicTrafficScoreRatio` | number | 近7天自然流量得分占比。 |
| `data.entities[].advertisingTrafficScoreRatio` | number | 近7天广告流量得分占比。 |
| `data.entities[].organicTrafficScoreGrowthRate` | number | 近7天自然流量得分增长率（环比）。 |
| `data.entities[].advertisingTrafficScoreGrowthRate` | number | 近7天广告流量得分增长率（环比）。 |
| `data.entities[].totalTrafficScoreGrowthRate` | number | 近7天总流量得分增长率（环比）。 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/xydc/get-asin-traffic`。
- 成功响应位于 `data`；失败时优先读取 `code`、`message`、`requestId` 和 HTTP 状态。
- 保留用户给出的 ASIN、关键词、站点国家码、日期/月/周范围、分页和筛选条件，不要擅自扩大查询窗口。
- 输出分析时保留原始字段名，确保 ASIN、关键词、日期、排名、流量分数、订单量、BSR、ABA 或广告活动 ID 可追溯。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按请求参数表修正 ASIN、关键词、站点国家码、日期/月/周格式、分页范围和必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/xydc/get-asin-traffic" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asins": ["B09PCSR9SX"], "country": "US"}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs#xydc-get_asin_traffic（2026-07-07 访问）。

# Wenmai XYDC 关键词信息（最近一周） API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/xydc/get-keyword-info`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`get_keyword_info`
- **接口说明**：关键词信息（最近一周）。
- **脚本入口**：`scripts/xydc_keyword_info.py`，脚本参数即标准 API POST Body JSON

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
| `country` | string | 是 | 站点国家码；示例：`US`。 |
| `keywords` | Array | 是 | 关键词列表；示例：`["usb c cable"]`。 |

## 请求示例

```json
{
  "keywords": [
    "usb c cable"
  ],
  "country": "US"
}
```

## 响应结构

公共响应字段：`code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.list` | Array | 数据列表。 |
| `data.list[].searchTerm` | string | 关键词。 |
| `data.list[].clickConversionRate` | string | 点击转化率(均值)。 |
| `data.list[].competitiveDifficulty` | integer | 竞争难度。 |
| `data.list[].abaReport` | object | ABA报告。 |
| `data.list[].abaReport.reportFromDate` | string | 周报告开始日-周日（YYYY-MM-DD格式）。 |
| `data.list[].abaReport.reportToDate` | string | 周报告结束日-周六（YYYY-MM-DD格式）。 |
| `data.list[].abaReport.searchFrequencyRank` | integer | 关键词排名。 |
| `data.list[].abaReport.weeklySearchVolume` | integer | 周搜索量。 |
| `data.list[].abaReport.topAsins` | Array | Top3Asins。 |
| `data.list[].abaReport.topAsins[].asin` | string | ASIN。 |
| `data.list[].abaReport.topAsins[].clickShare` | string | 点击份额。 |
| `data.list[].abaReport.topAsins[].conversionShare` | string | 转化份额。 |
| `data.list[].organicRotation` | string | 自然滚动率。 |
| `data.list[].costPerClick` | object | 建议竞价。 |
| `data.list[].costPerClick.value` | string | 建议竞价。 |
| `data.list[].costPerClick.minSuggestedBid` | string | 最小建议竞价。 |
| `data.list[].costPerClick.maxSuggestedBid` | string | 最大建议竞价。 |
| `data.total` | integer | 总条数（1个关键词为1条）。 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/xydc/get-keyword-info`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/xydc/get-keyword-info" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["usb c cable"], "country": "US"}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs#xydc-get_keyword_info（2026-07-07 访问）。

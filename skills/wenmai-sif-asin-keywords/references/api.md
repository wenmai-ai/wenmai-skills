# Wenmai SIF ASIN 关键词 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-asin-keyword-signals`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；在 https://agent.wenmai-ai.com/ 获取 secret-key，额度不足时在同一入口充值。
- **接口编码**：`market_get_asin_keyword_signals`
- **脚本入口**：`scripts/sif_asin_keywords.py`，脚本参数即标准 API POST Body JSON

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
| `asin` | string | 是 | ASIN，示例 `B0CLPGQWNB`。 |
| `country` | string | 否 | 站点代码；可选值示例：`US`、`UK`、`DE`、`CA`、`JP`、`FR`、`ES`、`IT`、`MX`、`AU`、`AE`、`BR`、`SA`；默认 `US`。 |
| `listingSearch` | boolean | 否 | 是否使用 listing search 口径；可选值：`true`、`false`；默认 `false`。 |
| `time_type` | string | 否 | 时间类型；可选值：`lately`、`week`、`month`。 |
| `time_value` | string | 否 | 时间值；`lately` 可选 `7` 或 `30`，默认 `7`；`week` 填周日日期如 `2026-03-29`；`month` 填月份首日如 `2026-03-01`。 |
| `topN` | integer | 否 | 返回关键词数量；默认 `50`，最大 `300`。 |

## 请求示例

脚本入参示例：

```json
{
  "asin": "B08GHW4TBS",
  "country": "US",
  "time_type": "lately",
  "time_value": "7",
  "topN": 50
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.primary_signals` | string/object | 核心信号分区。 |
| `data.declining[]` | array | 贡献下降关键词。 |
| `data.gaining[]` | array | 贡献上升关键词。 |
| `data.rank_gaps[]` | array | 排名断档关键词。 |
| `data.top_keywords[]` | array | Top 关键词列表。 |


## 使用要点

- SIF 周窗口以周日为每周第一天；当周数据可能因 T+1 延迟不可用。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按上方请求参数表修正枚举值、日期格式、分页范围或必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-asin-keyword-signals" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B08GHW4TBS", "country": "US", "time_type": "lately", "time_value": "7", "topN": 50}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。

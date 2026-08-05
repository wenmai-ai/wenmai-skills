# Wenmai SIF 关键词竞争流量 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-keyword-competition`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；在 https://agent.wenmai-ai.com/ 获取 secret-key，额度不足时在同一入口充值。
- **接口编码**：`market_get_keyword_competition`
- **脚本入口**：`scripts/sif_keyword_traffic.py`，脚本参数即标准 API POST Body JSON

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
| `keyword` | string | 是 | 单个关键词，示例 `wireless earbuds`。 |
| `asin` | string | 否 | ASIN，用于对标分析。 |
| `country` | string | 否 | 站点代码，示例 `US`；默认 `US`。 |
| `time_type` | string | 否 | 时间类型；可选值：`all`、`week`、`month`。 |
| `time_value` | string | 否 | 时间值；`week` 必填周日日期如 `2026-03-29`；`month` 填月份首日如 `2026-03-01`。 |
| `rank_evolution` | boolean | 否 | 是否返回排名演变数据；可选值：`true`、`false`。 |

## 请求示例

脚本入参示例：

```json
{
  "keyword": "wireless earbuds",
  "country": "US",
  "time_type": "all",
  "rank_evolution": false
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.total_asin_trend` | string | 可见 ASIN 集合方向，可能为 rising/stable/falling。 |
| `data.asins[]` | array | 按流量份额排列的 ASIN。 |
| `data.natural / sp / sb / sbv` | mixed | 自然、SP、SB、SBV 流量份额。 |
| `data.rank_evolution` | mixed | 排名演变数据，需启用 `rank_evolution`。 |


## 使用要点

- 返回头部竞争 ASIN 和不同广告/自然流量来源份额。

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-keyword-competition" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "wireless earbuds", "country": "US", "time_type": "all", "rank_evolution": false}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。

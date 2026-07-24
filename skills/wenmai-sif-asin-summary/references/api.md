# Wenmai SIF ASIN 流量概览 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-listing-traffic-overview`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`ops_get_listing_traffic_overview`
- **脚本入口**：`scripts/sif_asin_summary.py`，脚本参数即标准 API POST Body JSON

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
| `isListingSearch` | boolean | 否 | 是否使用 listing search 口径；可选值：`true`、`false`。 |
| `timePieceType` | string | 否 | 时间类型；可选值：`latelyDay`、`week`、`month`。 |
| `timePieceValue` | string | 否 | 时间值；`latelyDay` 可选 `7` 或 `30`；`week` 填周日日期如 `2026-03-29`；`month` 填月份首日如 `2026-03-01`。 |

## 请求示例

脚本入参示例：

```json
{
  "asin": "B08GHW4TBS",
  "country": "US",
  "timePieceType": "latelyDay",
  "timePieceValue": "7"
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.overview` | string/object | 自然/广告流量汇总概览。 |
| `data.totalScore` | string/number | 总流量分数。 |
| `data.organic / data.ads` | mixed | 自然流量与广告流量拆解。 |
| `data.recommendation` | mixed | 推荐位来源分布。 |


## 使用要点

- SIF 周窗口以周日为每周第一天；查当周失败时可改用最近 7 天。

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-listing-traffic-overview" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B08GHW4TBS", "country": "US", "timePieceType": "latelyDay", "timePieceValue": "7"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。

# Wenmai SIF 关键词需求概览 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-keyword-history`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；在 https://agent.wenmai-ai.com/ 获取 secret-key，额度不足时在同一入口充值。
- **接口编码**：`market_get_keyword_history`
- **脚本入口**：`scripts/sif_keyword_overview.py`，脚本参数即标准 API POST Body JSON

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
| `keywords` | array | 是 | 关键词列表；数量范围 `1`-`10`。 |
| `country` | string | 否 | 站点代码，示例 `US`；默认 `US`。 |
| `granularity` | string | 否 | 时间粒度；可选值：`week`、`month`；默认 `week`。 |
| `keywords[]` | string | 是 | 单个关键词字符串，示例 `wireless earbuds`。 |

## 请求示例

脚本入参示例：

```json
{
  "keywords": [
    "wireless earbuds"
  ],
  "country": "US",
  "granularity": "week"
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.keyword` | string | 关键词原文。 |
| `data.data_points` | string/integer | 历史数据点数量。 |
| `data.dates[]` | array | 时间周期列表。 |
| `data.search_volume / aba_rank` | mixed | 搜索量、ABA 排名等历史指标。 |


## 使用要点

- 用于回答关键词当前需求量、趋势、集中度。

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-keyword-history" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["wireless earbuds"], "country": "US", "granularity": "week"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。

# Wenmai Sorftime `walmart_product_trend_by_product_id` API 参考

产品历史趋势。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/walmart-product-trend-by-product-id`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`walmart_product_trend_by_product_id`
- **脚本入口**：`scripts/walmart_product_trend_by_product_id.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_id` | String | 是 | 商品 ID，仅支持单个商品 ID 查询。 |
| `trend_type` | String；可选值："UnKonw"、"SalesVolume"、"SalesAmount"、"Price"、"Rank"、"Reviews"、"Star" | 否 | 要查询的趋势类型，可选值：MonthlySalesVolume / MonthlySalesAmount / Price / Rank / Reviews / Star。 |
| `begin_date` | String | 否 | 历史回溯的起始时间（格式：yyyy-MM-dd），默认（未传或参数无效时）返回近 2 年的数据。 |
| `end_date` | String | 否 | 历史回溯的结束时间（格式：yyyy-MM-dd），默认（未传或参数无效时）返回到当前时间。 |

## 请求示例

```json
{
  "product_id": "11381374703"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data[]` | string | 所查询 Walmart 商品及趋势指标的扁平序列，日期与对应指标值交替排列。 |

## 使用要点

- 必填字段：`product_id`。
- 保留源文档字段名、类型和层级；数组字段以 `[]` 标识。
- 结果摘要必须保留到原始响应字段的映射，不推断缺失值。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 设置 `WENMAI_API_KEY` 或兼容的 `WENMAI_SECRET_KEY`，不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/ 充值。 |
| 参数错误 | 按请求表检查必填字段、字段类型、站点、日期和分页范围。 |
| HTTP、网络或超时错误 | 保留状态码和脱敏错误摘要，检查网关地址、网络和超时配置。 |
| 响应不是 JSON | 停止解析并报告响应格式错误，不把异常正文当作业务数据。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/walmart-product-trend-by-product-id" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id":"11381374703"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

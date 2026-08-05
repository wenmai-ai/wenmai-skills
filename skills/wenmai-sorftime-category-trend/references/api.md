# Wenmai Sorftime `category_trend` API 参考

类目市场趋势。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/category-trend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`category_trend`
- **脚本入口**：`scripts/category_trend.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `node_id` | String | 是 | 要查询的子类目 node_id；数据类型：string。 |
| `trend_index` | String；可选值："SalesCount"、"BrandProductCount"、"SellerProductCount"、"AvgPrice"、"AvgRatingCount"、"AvgScore"、"NewProductSalesAmountShare"、"AmazonSalesAmountShare"、"Top3ProductSalesAmountShare"、"Top3BrandSalesAmountShare"、"Top3SellerSalesAmountShare" | 否 | 趋势类型。允许值：SalesCount、BrandProductCount、SellerProductCount、AvgPrice、AvgRatingCount、AvgScore、NewProductSalesAmountShare、AmazonSalesAmountShare、Top3ProductSalesAmountShare、Top3BrandSalesAmountShare、Top3SellerSalesAmountShare；默认 SalesCount。 |
| `amz_site` | String；允许值："US"、"GB"、"DE"、"FR"、"IN"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、IN、CA、JP、ES、IT、MX、AE、AU、BR、SA。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "node_id": "1055398",
  "amz_site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.category_monthly_sales_volume_trend[]` | Array | 子类目月度趋势点数组；每个元素为 "yyyy-MM=N" 格式的文本。 |

## 使用要点

- 必填字段：`node_id`, `amz_site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/category-trend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"node_id":"1055398","amz_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

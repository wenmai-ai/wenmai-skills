# Wenmai Sorftime `shopee_product_trend` API 参考

产品历史趋势。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-product-trend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`shopee_product_trend`
- **脚本入口**：`scripts/shopee_product_trend.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_id` | String | 是 | 要查询的商品 ID。 |
| `query_start` | String | 否 | 查询起始时间（yyyy-MM-dd）。默认近 1 年。当跨度 > 1 年时，每次调用消耗 10 积分。 |
| `query_end` | String | 否 | 查询结束时间（yyyy-MM-dd）。默认为当前时间。 |
| `site` | String；允许值："VN"、"ID"、"SG"、"TH"、"MY"、"TW"、"PH"、"BR" | 是 | Shopee 站点，支持：201:VN、202:ID、203:SG、204:TH、205:MY、206:TW、207:PH、208:BR。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "product_id": "51953524682",
  "site": "TH"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.price_trend[]` | Array | 价格历史趋势（日度），扁平数组 [日期, 价格, ...]。 |
| `data.product_id` | String | Shopee 商品 ID。 |
| `data.review_count_trend[]` | Array | 评论数趋势（月度），扁平数组 [月份(YYYY-MM), 数量, ...]。 |
| `data.sale_count_trend[]` | Array | 近 30 天销量趋势（日度），扁平数组 [日期(YYYY-MM-DD), 数值, 日期, 数值, ...]。 |
| `data.sale_total_count_trend[]` | Array | 累计销量趋势（日度），扁平数组。 |
| `data.star_trend[]` | Array | 星级趋势（月度），扁平数组 [月份(YYYY-MM), 星级, ...]。 |

## 使用要点

- 必填字段：`product_id`, `site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-product-trend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id":"51953524682","site":"TH"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

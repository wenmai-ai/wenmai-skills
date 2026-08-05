# Wenmai Sorftime `tiktok_category_report` API 参考

类目数据报告。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/tiktok-category-report`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`tiktok_category_report`
- **脚本入口**：`scripts/tiktok_category_report.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `node_id` | String | 是 | 类目 node_id，可通过 `tiktok_category_name_search` 或 `tiktok_category_search_from_name` 获取。 |
| `site` | String；允许值："US"、"MY"、"PH"、"VN"、"TH"、"ID"、"GB"、"JP" | 是 | TikTok 站点。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "node_id": "1055398",
  "site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.avg_price` | String | Top 商品的平均价格（字符串，含货币符号）。 |
| `data.avg_review_count` | Integer | Top 商品的平均评论数。 |
| `data.avg_star` | Number | Top 商品的平均星级（满分 5）。 |
| `data.category_name` | String | 类目名称。 |
| `data.median_price` | String | Top 商品的价格中位数（字符串，含货币符号）。 |
| `data.monthly_sale_count` | Integer | Top100/Top300 商品的总月销量。 |
| `data.monthly_sale_count_mom` | Number | 月环比销量变化（百分比；正数=增长，负数=下降）。 |
| `data.new_product_avg_price_within_3_months` | Number | 近 3 个月内上架新品的平均价格（数值，本地货币）。 |
| `data.new_product_count_within_3_months` | Integer | Top 池中近 3 个月内上架的新品数量。 |
| `data.new_product_sale_ratio_within_3_months` | Number | Top 池中新品（≤3 个月）的销量占比（百分比）。 |
| `data.new_product_sale_sum_within_3_months` | Integer | 近 3 个月内上架新品的月销量合计。 |
| `data.top10_product_monthly_sale_ratio` | Number | Top10 商品在 Top100 中的月销量占比（百分比）。 |
| `data.top10_seller_monthly_sale_ratio` | Number | 按卖家聚合后，Top10 卖家在 Top100 中的月销量占比（百分比）。 |
| `data.top300_product_store_count` | Integer | Top300 商品覆盖的去重店铺数。 |
| `data.top50_products[]` | Array | Top50 商品详情数组。 |
| `data.top50_products[].brand` | String | 商品品牌（缺失时为 "N/A"）。 |
| `data.top50_products[].monthly_sale_count` | Integer | 月销量。 |
| `data.top50_products[].price` | String | 价格（字符串，含货币符号）。 |
| `data.top50_products[].review_count` | Integer | 总评论数。 |
| `data.top50_products[].seller` | String | 卖家店铺名称。 |
| `data.top50_products[].star` | Number | 星级（满分 5）。 |
| `data.top50_products[].title` | String | 商品标题。 |
| `data.top50_products[].weekly_sale_count` | Integer | 近 7 天销量。 |
| `data.top50_products[].weekly_sale_count_mom` | Number | 周环比销量变化（百分比）。 |

## 使用要点

- 必填字段：`node_id`, `site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/tiktok-category-report" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"node_id":"1055398","site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

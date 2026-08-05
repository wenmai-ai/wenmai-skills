# Wenmai Sorftime `category_keywords` API 参考

类目核心关键词。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/category-keywords`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`category_keywords`
- **脚本入口**：`scripts/category_keywords.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `node_id` | String | 是 | 按 nodeid 查询指定子类目市场；数据类型：string。 |
| `page` | Number | 否 | 查询结果的页码。默认 1，每页返回 20 条记录。 |
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
| `data.cpc_exact_bid` | String | CPC 精确匹配出价（字符串，本地货币）。 |
| `data.keyword` | String | 核心关键词文本。 |
| `data.monthly_search_volume` | String | 月搜索量（字符串）。 |
| `data.search_result_count` | String | 搜索结果总数（字符串）。 |
| `data.search_result_first_page_organic_avg_monthly_sales` | String | 搜索结果首页自然商品的月平均销量（字符串）。 |
| `data.search_result_second_page_organic_avg_monthly_sales` | String | 搜索结果第二页自然商品的月平均销量（字符串）。 |
| `data.search_result_third_page_organic_avg_monthly_sales` | String | 搜索结果第三页自然商品的月平均销量（字符串）。 |
| `data.search_result_top3_pages_amazon_owned_count_share` | String | 前 3 页中 Amazon 自营商品的数量占比。 |
| `data.search_result_top3_pages_amazon_owned_sales_share` | String | 前 3 页中 Amazon 自营商品的销量占比。 |
| `data.search_result_top3_pages_avg_price` | String | 前 3 页商品的平均售价（字符串）。 |
| `data.search_result_top3_pages_new_product_3m_count_share` | String | 前 3 页中上架 3 个月内新品的数量占比。 |
| `data.search_result_top3_pages_new_product_3m_sales_share` | String | 前 3 页中上架 3 个月内新品的销量占比。 |
| `data.search_result_top3_pages_organic_avg_monthly_sales` | String | 前 3 页自然商品的月平均销量（字符串）。 |
| `data.search_result_top3_pages_top100_total_monthly_sales` | String | 前 3 页 Top-100 商品月销量合计（字符串）。 |
| `data.search_result_top3_pages_top3_brand_sales_share` | String | 前 3 页中 Top-3 品牌的销量占比。 |
| `data.search_result_top3_pages_top3_product_sales_share` | String | 前 3 页中 Top-3 商品的销量占比。 |
| `data.search_result_top3_pages_top3_seller_sales_share` | String | 前 3 页中 Top-3 卖家的销量占比。 |
| `data.search_volume_peak_season` | String | 搜索量的旺季月份。 |
| `data.weekly_search_rank` | String | 周搜索量排名（字符串）。 |
| `data.weekly_search_rank_change` | String | 周排名变化（字符串）。 |
| `data.weekly_search_volume` | String | 周搜索量（字符串）。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/category-keywords" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"node_id":"1055398","amz_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

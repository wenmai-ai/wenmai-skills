# Wenmai Sorftime `category_search_from_product_name` API 参考

按产品名称搜类目。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/category-search-from-product-name`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`category_search_from_product_name`
- **脚本入口**：`scripts/category_search_from_product_name.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_name` | String | 是 | 要搜索的产品类目名称（如 air fryer、phone power bank）。 |
| `month_sales_volume_min` | Number | 否 | 可选：筛选月销量大于等于该值的子类目市场。 |
| `month_sales_volume_max` | Number | 否 | 可选：筛选月销量小于等于该值的子类目市场。 |
| `ratings_min` | Number | 否 | 可选：筛选星级大于等于该值的子类目市场。 |
| `ratings_max` | Number | 否 | 可选：筛选星级小于等于该值的子类目市场。 |
| `ratings_count_min` | Number | 否 | 可选：筛选评论数大于等于该值的子类目市场。 |
| `ratings_count_max` | Number | 否 | 可选：筛选评论数小于等于该值的子类目市场。 |
| `price_min` | Number | 否 | 可选：筛选平均售价（本地货币）大于等于该值的子类目市场。 |
| `price_max` | Number | 否 | 可选：筛选平均售价（本地货币）小于等于该值的子类目市场。 |
| `seasonal_popular_product` | String；可选值："Both"、"January"、"February"、"March"、"April"、"May"、"June"、"July"、"August"、"September"、"October"、"November"、"December" | 否 | 可选：筛选旺季为指定月份的子类目。允许值：Both、January、February、March、April、May、June、July、August、September、October、November、December；默认 Both。 |
| `top3_product_sales_share_min` | Number | 否 | 可选：用 0~1 表示百分比。筛选 Top-3 商品销量占比大于等于该值的子类目市场。 |
| `top3_product_sales_share_max` | Number | 否 | 可选：用 0~1 表示百分比。筛选 Top-3 商品销量占比小于等于该值的子类目市场。 |
| `amazon_owned_sales_share_min` | Number | 否 | 可选：用 0~1 表示百分比。筛选 Amazon 自营销量占比大于等于该值的子类目市场。 |
| `amazon_owned_sales_share_max` | Number | 否 | 可选：用 0~1 表示百分比。筛选 Amazon 自营销量占比小于等于该值的子类目市场。 |
| `top100_top400_sales_share_min` | Number | 否 | 可选：用 0~1 表示百分比。筛选 Top-100 占 Top-400 销量比大于等于该值的子类目市场。 |
| `top100_top400_sales_share_max` | Number | 否 | 可选：用 0~1 表示百分比。筛选 Top-100 占 Top-400 销量比小于等于该值的子类目市场。 |
| `newproduct_sales_share_min` | Number | 否 | 可选：用 0~1 表示百分比。筛选新品（3 个月内上架）销量占比大于等于该值的子类目市场。 |
| `newproduct_sales_share_max` | Number | 否 | 可选：用 0~1 表示百分比。筛选新品（3 个月内上架）销量占比小于等于该值的子类目市场。 |
| `page` | Number | 否 | 查询结果的页码。默认 1，每页返回 20 条记录。 |
| `amz_site` | String；允许值："US"、"GB"、"DE"、"FR"、"IN"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、IN、CA、JP、ES、IT、MX、AE、AU、BR、SA。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "product_name": "wireless earbuds",
  "amz_site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.amazon_owned_sales_share` | String | Top-100 中 Amazon 自营的月销量占比。 |
| `data.average_price` | String | Top-100 商品的平均售价（字符串，本地货币）。 |
| `data.average_review_count` | Number | Top-100 商品的平均评论数。 |
| `data.average_star_rating` | Number | Top-100 商品的平均星级。 |
| `data.category_name` | String | 子类目名称。 |
| `data.china_seller_share` | String | Top-100 中中国卖家的月销量占比。 |
| `data.new_product_3m_sales_share` | String | Top-100 中上架 3 个月内的新品月销量占比。 |
| `data.node_id` | String | 子类目节点 ID（NodeID）。 |
| `data.peak_season` | String | 子类目的旺季月份；"均衡" 表示全年无明显旺季。 |
| `data.top100_monthly_sales_amount` | String | Top-100 商品的月销售额合计（字符串，本地货币）。 |
| `data.top100_monthly_sales_volume` | String | Top-100 商品的月销量合计（字符串）。 |
| `data.top3_brand_sales_share` | String | Top-3 品牌在 Top-100 中的月销量占比。 |
| `data.top3_product_sales_share` | String | Top-3 商品在 Top-100 中的月销量占比。 |
| `data.top3_seller_sales_share` | String | Top-3 卖家在 Top-100 中的月销量占比。 |

## 使用要点

- 必填字段：`product_name`, `amz_site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/category-search-from-product-name" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_name":"wireless earbuds","amz_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

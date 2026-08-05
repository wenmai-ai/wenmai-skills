# Wenmai Sorftime `category_report` API 参考

类目实时市场报告。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/category-report`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`category_report`
- **脚本入口**：`scripts/category_report.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `node_id` | String | 是 | 子类目 node_id，查询该子类目的数据；数据类型：string。 |
| `amz_site` | String；允许值："US"、"GB"、"DE"、"FR"、"IN"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、IN、CA、JP、ES、IT、MX、AE、AU、BR、SA。实际调用必须明确指定。 |

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
| `data.category_stats_report` | Object | 该子类目的统计汇总对象。 |
| `data.category_stats_report.amazon_owned_sales_volume` | String | Amazon 自营月销量的文本描述。 |
| `data.category_stats_report.amazon_owned_sales_volume_share` | String | Amazon 自营月销量占比的文本描述。 |
| `data.category_stats_report.average_price` | String | Top-80% 商品平均价的文本描述。 |
| `data.category_stats_report.first_brand` | String | 第 1 名品牌的文本描述。 |
| `data.category_stats_report.first_brand_sales_amount` | String | 第 1 名品牌月销售额的文本描述。 |
| `data.category_stats_report.first_brand_sales_volume` | String | 第 1 名品牌月销量的文本描述。 |
| `data.category_stats_report.first_product_sales_amount` | String | 第 1 名商品月销售额的文本描述。 |
| `data.category_stats_report.first_product_sales_volume` | String | 第 1 名商品月销量的文本描述。 |
| `data.category_stats_report.first_seller` | String | 第 1 名卖家的文本描述。 |
| `data.category_stats_report.first_seller_sales_amount` | String | 第 1 名卖家月销售额的文本描述。 |
| `data.category_stats_report.first_seller_sales_volume` | String | 第 1 名卖家月销量的文本描述。 |
| `data.category_stats_report.high_rated_sales_volume` | String | 4 星及以上商品月销量的文本描述。 |
| `data.category_stats_report.high_rated_sales_volume_share` | String | 4 星及以上商品月销量占比的文本描述。 |
| `data.category_stats_report.high_reviews_sales_volume` | String | 1000+ 评论商品月销量的文本描述。 |
| `data.category_stats_report.high_reviews_sales_volume_share` | String | 1000+ 评论商品月销量占比的文本描述。 |
| `data.category_stats_report.low_reviews_sales_volume` | String | 少于 300 评论商品月销量的文本描述。 |
| `data.category_stats_report.low_reviews_sales_volume_share` | String | 少于 300 评论商品月销量占比的文本描述。 |
| `data.category_stats_report.median_price` | String | Top-80% 商品中位价的文本描述。 |
| `data.category_stats_report.node_id` | String | 子类目节点 ID（NodeID）。 |
| `data.category_stats_report.second_brand` | String | 第 2 名品牌的文本描述。 |
| `data.category_stats_report.second_brand_sales_amount` | String | 第 2 名品牌月销售额的文本描述。 |
| `data.category_stats_report.second_brand_sales_volume` | String | 第 2 名品牌月销量的文本描述。 |
| `data.category_stats_report.second_product_sales_amount` | String | 第 2 名商品月销售额的文本描述。 |
| `data.category_stats_report.second_product_sales_volume` | String | 第 2 名商品月销量的文本描述。 |
| `data.category_stats_report.second_seller` | String | 第 2 名卖家的文本描述。 |
| `data.category_stats_report.second_seller_sales_amount` | String | 第 2 名卖家月销售额的文本描述。 |
| `data.category_stats_report.second_seller_sales_volume` | String | 第 2 名卖家月销量的文本描述。 |
| `data.category_stats_report.third_brand` | String | 第 3 名品牌的文本描述。 |
| `data.category_stats_report.third_brand_sales_amount` | String | 第 3 名品牌月销售额的文本描述。 |
| `data.category_stats_report.third_brand_sales_volume` | String | 第 3 名品牌月销量的文本描述。 |
| `data.category_stats_report.third_product_sales_amount` | String | 第 3 名商品月销售额的文本描述。 |
| `data.category_stats_report.third_product_sales_volume` | String | 第 3 名商品月销量的文本描述。 |
| `data.category_stats_report.third_seller` | String | 第 3 名卖家的文本描述。 |
| `data.category_stats_report.third_seller_sales_amount` | String | 第 3 名卖家月销售额的文本描述。 |
| `data.category_stats_report.third_seller_sales_volume` | String | 第 3 名卖家月销量的文本描述。 |
| `data.category_stats_report.top100_monthly_sales_amount` | String | Top-100 月销售额合计。 |
| `data.category_stats_report.top100_monthly_sales_volume` | String | Top-100 月销量合计。 |
| `data.category_stats_report.top3_brands_sales_volume_share` | String | Top-3 品牌销量占比的文本描述。 |
| `data.category_stats_report.top3_product_sales_volume_share` | String | Top-3 商品销量占比的文本描述。 |
| `data.category_stats_report.top3_seller_sales_volume_share` | String | Top-3 卖家销量占比的文本描述。 |
| `data.top100_products[]` | Array | Top-100 商品数组；每个元素为一个商品的销售数据。 |
| `data.top100_products[].asin` | String | 商品 ASIN。 |
| `data.top100_products[].brand` | String | 商品品牌。 |
| `data.top100_products[].category_rank` | String | 子类目排名文本。 |
| `data.top100_products[].days_listed` | Integer | 上架天数。 |
| `data.top100_products[].gross_profit` | Number | 毛利润（本地货币）。 |
| `data.top100_products[].gross_profit_margin` | Number | 毛利率（百分比）。 |
| `data.top100_products[].monthly_sales_amount` | String | 该商品的月销售额（字符串，本地货币）。 |
| `data.top100_products[].monthly_sales_volume` | String | 该商品的月销量（字符串）。 |
| `data.top100_products[].online_date` | String | 上架日期（yyyy-MM-dd）。 |
| `data.top100_products[].package_size` | String | 包装尺寸，格式 "L*W*H"，单位 cm。 |
| `data.top100_products[].price` | Number | 商品价格（本地货币）。 |
| `data.top100_products[].product_category` | String | 商品所属类目。 |
| `data.top100_products[].review_count` | Integer | 评论数。 |
| `data.top100_products[].seller` | String | 卖家名称。 |
| `data.top100_products[].seller_origin` | String | 卖家来源国家/地区。 |
| `data.top100_products[].star_rating` | Number | 星级。 |
| `data.top100_products[].title` | String | 商品标题。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/category-report" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"node_id":"1055398","amz_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

# Wenmai Sorftime `temu_category_search` API 参考

选类目。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/temu-category-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`temu_category_search`
- **脚本入口**：`scripts/temu_category_search.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `node_id` | String | 否 | 可选。若指定：将搜索范围限制在指定类目及其子类目（指定的类目 nodeId 不限于叶子类目）。 |
| `sale_count_min` | Integer | 否 | 可选。若指定：筛选 Top-100 商品月销量大于等于该值的类目市场；值越大表示商品销售集中度越高。 |
| `sale_count_max` | Integer | 否 | 可选。若指定：筛选 Top-100 商品月销量小于等于该值的类目市场；值越大表示商品销售集中度越高。 |
| `sale_count_share_ratio_min` | Number | 否 | 可选。若指定：筛选 Top-100 占 Top-600 月销量比例大于等于该值（%）的类目；越高表示越集中于 Top-100，越低表示是长尾类目。 |
| `sale_count_share_ratio_max` | Number | 否 | 可选。若指定：筛选 Top-100 占 Top-600 月销量比例小于等于该值（%）的类目。 |
| `sale_count_mom_min` | Number | 否 | 可选。若指定：筛选 Top-100 月销量月环比增长率大于等于该值（%）的类目；值越大表示增长越快。 |
| `sale_count_mom_max` | Number | 否 | 可选。若指定：筛选 Top-100 月销量月环比增长率小于等于该值（%）的类目。 |
| `sale_amount_min` | Number | 否 | 可选。若指定：筛选 Top-100 月销售额大于等于该值的类目。 |
| `sale_amount_max` | Number | 否 | 可选。若指定：筛选 Top-100 月销售额小于等于该值的类目。 |
| `price_min` | Number | 否 | 可选。若指定：筛选 Top-100 商品售价大于等于该值的类目。 |
| `price_max` | Number | 否 | 可选。若指定：筛选 Top-100 商品售价小于等于该值的类目。 |
| `avg_review_count_min` | Number | 否 | 可选。若指定：筛选 Top-100 平均评论数大于等于该值的类目。 |
| `avg_review_count_max` | Number | 否 | 可选。若指定：筛选 Top-100 平均评论数小于等于该值的类目。 |
| `avg_star_min` | Number | 否 | 可选。若指定：筛选 Top-100 平均星级大于等于该值的类目。 |
| `avg_star_max` | Number | 否 | 可选。若指定：筛选 Top-100 平均星级小于等于该值的类目。 |
| `seller_count_min` | Integer | 否 | 可选。若指定：筛选 Top-100 独立卖家数大于等于该值的类目。 |
| `seller_count_max` | Integer | 否 | 可选。若指定：筛选 Top-100 独立卖家数小于等于该值的类目。 |
| `brand_count_min` | Integer | 否 | 可选。若指定：筛选 Top-100 独立品牌数大于等于该值的类目。 |
| `brand_count_max` | Integer | 否 | 可选。若指定：筛选 Top-100 独立品牌数小于等于该值的类目。 |
| `top10_product_sale_count_share_ratio_min` | Number | 否 | 可选。若指定：筛选 Top-10 占 Top-100 销量比例大于等于该值（%）的类目；越高表示商品集中度越强。 |
| `top10_product_sale_count_share_ratio_max` | Number | 否 | 可选。若指定：筛选 Top-10 占 Top-100 销量比例小于等于该值（%）的类目。 |
| `top10_seller_sale_count_share_ratio_min` | Number | 否 | 可选。若指定：在 Top-100 商品中，筛选 Top-10 卖家销量占比大于等于该值（%）的类目；越高表示卖家集中度越强。 |
| `top10_seller_sale_count_share_ratio_max` | Number | 否 | 可选。若指定：在 Top-100 商品中，筛选 Top-10 卖家销量占比小于等于该值（%）的类目。 |
| `semi_managed_shop_count_min` | Integer | 否 | 可选。若指定：筛选 Top-100 半托管店铺数大于等于该值的类目。 |
| `semi_managed_shop_count_max` | Integer | 否 | 可选。若指定：筛选 Top-100 半托管店铺数小于等于该值的类目。 |
| `semi_managed_shop_sale_count_min` | Integer | 否 | 可选。若指定：筛选 Top-100 半托管店铺月销量大于等于该值的类目。 |
| `semi_managed_shop_sale_count_max` | Integer | 否 | 可选。若指定：筛选 Top-100 半托管店铺月销量小于等于该值的类目。 |
| `semi_managed_shop_cumulative_sale_count_min` | Integer | 否 | 可选。若指定：筛选 Top-100 半托管店铺累计销量大于等于该值的类目。 |
| `semi_managed_shop_cumulative_sale_count_max` | Integer | 否 | 可选。若指定：筛选 Top-100 半托管店铺累计销量小于等于该值的类目。 |
| `star_seller_count_min` | Integer | 否 | 可选。若指定：筛选 Top-100 明星卖家数大于等于该值的类目。 |
| `star_seller_count_max` | Integer | 否 | 可选。若指定：筛选 Top-100 明星卖家数小于等于该值的类目。 |
| `star_seller_monthly_sale_count_min` | Integer | 否 | 可选。若指定：筛选 Top-100 明星卖家月销量大于等于该值的类目。 |
| `star_seller_monthly_sale_count_max` | Integer | 否 | 可选。若指定：筛选 Top-100 明星卖家月销量小于等于该值的类目。 |
| `new_product_count_min` | Integer | 否 | 可选。若指定：筛选 Top-600 新品（30 天内上架）数量大于等于该值的类目。 |
| `new_product_count_max` | Integer | 否 | 可选。若指定：筛选 Top-600 新品（30 天内上架）数量小于等于该值的类目。 |
| `new_product_sale_count_min` | Integer | 否 | 可选。若指定：筛选 Top-600 新品（30 天内）月销量大于等于该值的类目。 |
| `new_product_sale_count_max` | Integer | 否 | 可选。若指定：筛选 Top-600 新品（30 天内）月销量小于等于该值的类目。 |
| `new_product_sale_count_share_ratio_min` | Number | 否 | 可选。若指定：筛选 Top-600 新品（30 天内）月销量占比大于等于该值（%）的类目。 |
| `new_product_sale_count_share_ratio_max` | Number | 否 | 可选。若指定：筛选 Top-600 新品（30 天内）月销量占比小于等于该值（%）的类目。 |
| `page` | Integer | 否 | 查询结果的页码。默认第 1 页。 |
| `site` | String；允许值："US"、"EU" | 是 | Temu 站点，支持：701:US、705:EU。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.avg_price` | Number | Top-100 商品的平均售价。 |
| `data.avg_review_count` | Integer | Top-100 商品的平均评论数。 |
| `data.avg_star` | Number | Top-100 商品的平均星级。 |
| `data.brand_count` | Integer | Top-100 中的独立品牌数。 |
| `data.monthly_sale_amount` | Number | Top-100 商品的月销售额合计。 |
| `data.monthly_sale_count` | Integer | 该类目 Top-100 商品的月销量合计。 |
| `data.monthly_sale_count_mom` | Number | Top-100 月销量的月环比增长率（%）。 |
| `data.monthly_sale_count_share_ratio` | Number | Top-100 占 Top-600 月销量的比例（%）。 |
| `data.name` | String | Temu 类目显示名称。 |
| `data.new_product_count` | Integer | 进入 Top-600 的新品（30 天内上架）数量。 |
| `data.new_product_sale_count` | Integer | Top-600 中新品（30 天内）的月销量。 |
| `data.new_product_sale_count_share_ratio` | Number | Top-600 中新品月销量占比（%）。 |
| `data.node_id` | String | Temu 类目节点 ID。 |
| `data.seller_count` | Integer | Top-100 中的独立卖家数。 |
| `data.semi_managed_shop_count` | Integer | Top-100 中的半托管店铺数。 |
| `data.semi_managed_shop_cumulative_sale_count` | Integer | Top-100 中半托管店铺的累计销量。 |
| `data.semi_managed_shop_sale_count` | Integer | Top-100 中半托管店铺的月销量。 |
| `data.star_seller_count` | Integer | Top-100 中的明星卖家数。 |
| `data.star_seller_monthly_sale_count` | Integer | Top-100 中明星卖家的月销量。 |
| `data.top10_product_sale_count_share_ratio` | Number | Top-10 商品占 Top-100 销量的比例（%）。 |
| `data.top10_seller_sale_count_share_ratio` | Number | Top-10 卖家占 Top-100 销量的比例（%）。 |

## 使用要点

- 必填字段：`site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/temu-category-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

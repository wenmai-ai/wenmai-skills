# Wenmai Sorftime `temu_product_search` API 参考

选产品。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/temu-product-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`temu_product_search`
- **脚本入口**：`scripts/temu_product_search.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_id` | String | 否 | 可选。若指定：基于给定 ProductId 查询相似商品。 |
| `node_id` | String | 否 | 可选。若指定：将搜索范围限制在指定类目及其子类目（指定的类目 nodeId 不限于叶子类目）。 |
| `brand` | String | 否 | 可选。若指定：查询指定品牌的热销商品。 |
| `seller_name` | String | 否 | 可选。若指定：查询指定卖家的热销商品。 |
| `cumulative_sale_count_min` | Integer | 否 | 可选。若指定：筛选累计销量大于等于该值的商品。 |
| `cumulative_sale_count_max` | Integer | 否 | 可选。若指定：筛选累计销量小于等于该值的商品。 |
| `sale_count_min` | Integer | 否 | 可选。若指定：筛选月销量大于等于该值的商品。 |
| `sale_count_max` | Integer | 否 | 可选。若指定：筛选月销量小于等于该值的商品。 |
| `sale_amount_min` | Number | 否 | 可选。若指定：筛选月销售额大于等于该值的商品。 |
| `sale_amount_max` | Number | 否 | 可选。若指定：筛选月销售额小于等于该值的商品。 |
| `sale_count_mom_min` | Number | 否 | 可选。若指定：筛选月环比增长率大于等于该值（%）的商品。 |
| `sale_count_mom_max` | Number | 否 | 可选。若指定：筛选月环比增长率小于等于该值（%）的商品。 |
| `price_min` | Number | 否 | 可选。若指定：筛选售价大于等于该值的商品。 |
| `price_max` | Number | 否 | 可选。若指定：筛选售价小于等于该值的商品。 |
| `manage_type` | Integer | 否 | 可选。若指定：按托管类型筛选商品。允许值：0=全部，1=半托管，2=全托管。 |
| `comment_count_min` | Integer | 否 | 可选。若指定：筛选评论数大于等于该值的商品。 |
| `comment_count_max` | Integer | 否 | 可选。若指定：筛选评论数小于等于该值的商品。 |
| `star_min` | Number | 否 | 可选。若指定：筛选星级大于等于该值的商品。 |
| `star_max` | Number | 否 | 可选。若指定：筛选星级小于等于该值的商品。 |
| `sale_time_min` | String | 否 | 可选。若指定：按上架起始日期筛选商品（yyyy-MM-dd）。 |
| `sale_time_max` | String | 否 | 可选。若指定：按上架结束日期筛选商品（yyyy-MM-dd）。 |
| `site` | String；允许值："US"、"EU" | 是 | Temu 站点，支持：701:US、705:EU。 实际调用必须明确指定。 |
| `page` | Integer | 否 | 分页，每页最多 20 个商品。默认 1（页码从 1 开始，非 0）。 |

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
| `data.brand_name` | String | 品牌名称。 |
| `data.bsr_category[]` | Array | 商品所在的 BSR（Best Seller Rank）类目数组。 |
| `data.bsr_category[].name` | String | BSR 类目名称。 |
| `data.bsr_category[].node_id` | String | BSR 类目节点 ID。 |
| `data.cumulative_sale_count` | Integer | 商品的累计销量。 |
| `data.department` | Object | 商品所属一级类目。 |
| `data.department.name` | String | 一级类目名称。 |
| `data.department.node_id` | String | 一级类目节点 ID。 |
| `data.managed_type` | String | 托管类型（半托管 / 全托管 等）。 |
| `data.monthly_sale_amount` | Number | 商品的月销售额。 |
| `data.monthly_sale_count` | Integer | 商品的月销量。 |
| `data.monthly_sale_count_growth` | Number | 商品月销量的月环比增长率（%）。 |
| `data.photo` | String | 商品主图 URL。 |
| `data.price` | Number | 商品售价。 |
| `data.product_id` | String | Temu 商品 ID。 |
| `data.product_name` | String | 商品标题。 |
| `data.review_count` | Integer | 商品评论数。 |
| `data.sale_time` | String | 商品上架日期（yyyy-MM-dd）。 |
| `data.star` | Number | 商品星级。 |
| `data.store_name` | String | 店铺名称（可能是店铺显示名或数字形式的 ShopId）。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/temu-product-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

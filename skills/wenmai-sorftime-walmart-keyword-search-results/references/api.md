# Wenmai Sorftime `walmart_keyword_search_results` API 参考

关键词搜索结果。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/walmart-keyword-search-results`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`walmart_keyword_search_results`
- **脚本入口**：`scripts/walmart_keyword_search_results.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keyword` | String | 是 | 要查询的关键词。 |
| `page` | Number | 否 | 查询结果的页码。默认第 1 页，每页返回 20 条记录。 |

## 请求示例

```json
{
  "keyword": "wireless earbuds"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.brand` | String | 品牌。 |
| `data.clearance` | Boolean | 是否为清仓商品。 |
| `data.flash_deal` | Boolean | 是否参与 Flash Deal。 |
| `data.label[]` | Array | 商品标签数组。 |
| `data.listing_sales_of_month` | String | 商品近 30 天的销售额（字符串，带前导 "$"）。 |
| `data.listing_sales_volume_of_month` | Integer | 商品近 30 天的销量（件）。 |
| `data.node_tree[]` | Array | 类目路径与日期数组（搜索结果中常为空）。 |
| `data.number_of_star[]` | Array | 星级分布数组。 |
| `data.parent_product_id` | String | 父商品 ID。 |
| `data.photo[]` | Array | 商品图片 URL 数组（主图在前）。 |
| `data.popular_pick` | Boolean | 是否标记为 "Popular Pick"。 |
| `data.price` | String | 商品售价（字符串，带前导 "$"）。 |
| `data.product_id` | String | Walmart 商品 ID。 |
| `data.ratings` | Number | 平均评分（满分 5）。 |
| `data.reduced_price` | Boolean | 价格是否已下调。 |
| `data.reviews_count` | Integer | 总评论数。 |
| `data.rollback` | Boolean | 是否参与 Rollback 折扣。 |
| `data.seller` | String | 卖家名称。 |
| `data.shipedby` | String | 配送方式（如 WFS）。 |
| `data.title` | String | 商品标题。 |
| `data.variants[]` | Array | 变体数组。 |
| `data.variants[].detail_update` | String | 变体最近一次详情更新日期（yyyy-MM-dd）。 |
| `data.variants[].price_update` | String | 变体最近一次价格更新日期（yyyy-MM-dd）。 |
| `data.variants[].property[]` | Array | 变体属性键值扁平数组（每两个元素为一对 key+value）。 |
| `data.variants[].url` | String | 变体详情页 URL。 |
| `data.variants[].variant_id` | String | 变体 ID。 |
| `data.weight` | Number | 商品重量（单位未说明，0 表示未填写）。 |
| `data.wfs_fee` | Integer | WFS 履约费。 |

## 使用要点

- 必填字段：`keyword`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/walmart-keyword-search-results" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword":"wireless earbuds"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

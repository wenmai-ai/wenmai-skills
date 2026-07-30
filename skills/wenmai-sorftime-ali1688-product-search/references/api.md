# Wenmai Sorftime `ali1688_product_search` API 参考

1688平台产品多维度搜索。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/ali1688-product-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ali1688_product_search`
- **脚本入口**：`scripts/ali1688_product_search.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `node_id` | String | 否 | 基于类目查询（不限于叶子类目）；若指定则在该类目范围内搜索。 |
| `product_id` | String | 否 | 基于 ProductId 查询相似商品（注：并非只查该 ProductId，若需精确获取该商品请调用 product_request 工具）。 |
| `supplier_name` | String | 否 | 按供应商名称模糊匹配商品。 |
| `supplier_type` | Integer | 否 | 按供应商类型筛选，单选。1：实力商家，2：超级工厂。 |
| `supplier_member_type` | Integer | 否 | 按供应商会员类型筛选，单选。1：深度认证，2：非深度认证。 |
| `rights` | String | 否 | 按权益/服务筛选。多选用逗号分隔，例如 "1,2,3"。1：7 天无理由退货，2：运费险，3：48 小时内发货。 |
| `dropshipping_price_range_min` | Number | 否 | 筛选售价大于等于该值的商品。 |
| `dropshipping_price_range_max` | Number | 否 | 筛选售价小于等于该值的商品。 |
| `cumulative_sale_count_min` | Integer | 否 | 筛选累计销量大于等于该值的商品。 |
| `cumulative_sale_count_max` | Integer | 否 | 筛选累计销量小于等于该值的商品。 |
| `recent_30_day_sale_min` | Integer | 否 | 筛选近 30 天销量大于等于该值的商品。 |
| `recent_30_day_sale_max` | Integer | 否 | 筛选近 30 天销量小于等于该值的商品。 |
| `repurchase_rate_min` | Number | 否 | 筛选复购率大于等于该值的商品。 |
| `repurchase_rate_max` | Number | 否 | 筛选复购率小于等于该值的商品。 |
| `service_score_min` | Number | 否 | 筛选综合服务分大于等于该值的商品。 |
| `service_score_max` | Number | 否 | 筛选综合服务分小于等于该值的商品。 |
| `sku_count_min` | Integer | 否 | 筛选 SKU 数量大于等于该值的商品。 |
| `sku_count_max` | Integer | 否 | 筛选 SKU 数量小于等于该值的商品。 |
| `stock_count_min` | Integer | 否 | 筛选库存数量大于等于该值的商品。 |
| `stock_count_max` | Integer | 否 | 筛选库存数量小于等于该值的商品。 |
| `online_date_range_min` | String | 否 | 按上架起始日期筛选商品，日期格式 yyyy-MM-dd。 |
| `online_date_range_max` | String | 否 | 按上架结束日期筛选商品，日期格式 yyyy-MM-dd。 |
| `page` | Integer | 否 | 查询数据的页码，默认第 1 页。 |

## 请求示例

```json
{}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.online_date` | String | 商品上架日期（yyyy-MM-dd）。 |
| `data.photo` | String | 商品主图 URL。 |
| `data.price` | Number | 商品显示价格（人民币）。 |
| `data.product_id` | String | 1688 商品 ID（offer id），用于后续详情/变体查询。 |
| `data.repurchase_rate` | Number | 复购率（百分比值）。 |
| `data.review_count` | Integer | 评论数。 |
| `data.sales_of_30d` | Integer | 近 30 天销量（件）。 |
| `data.score` | Number | 商品评分（满分 5）。 |
| `data.service_score` | Number | 综合服务分（满分 5）。 |
| `data.service_score_detail[]` | Array | 服务评分明细数组。 |
| `data.service_score_detail[].score` | Number | 该维度的分值（满分 5）。 |
| `data.service_score_detail[].title` | String | 评分维度名称（如采购咨询、物流时效、纠纷解决、品质体验、退换体验）。 |
| `data.shipping_origin` | String | 发货地。 |
| `data.sku_count` | Integer | SKU（变体）数量。 |
| `data.store_name` | String | 供应商店铺名称。 |
| `data.title` | String | 商品标题。 |
| `data.url` | String | 1688 商品详情页 URL。 |
| `data.wholesale_price_range[]` | Array | 批发阶梯价格数组。 |
| `data.wholesale_price_range[].price` | Number | 该阶梯的单价（字符串，单位人民币）。 |
| `data.wholesale_price_range[].purchase_quantity` | String | 该阶梯的采购数量条件（如 ≥1、500~999 件）。 |

## 使用要点

- 必填字段：无。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/ali1688-product-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

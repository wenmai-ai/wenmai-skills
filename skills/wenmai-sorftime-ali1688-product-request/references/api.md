# Wenmai Sorftime `ali1688_product_request` API 参考

1688平台产品详情查询。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/ali1688-product-request`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ali1688_product_request`
- **脚本入口**：`scripts/ali1688_product_request.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_id` | String | 是 | 要查询的商品 ID。 |

## 请求示例

```json
{
  "product_id": "789542752062"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.online_date` | String | 商品上架日期（yyyy-MM-dd）。 |
| `data.photo` | String | 商品主图 URL。 |
| `data.price` | Number | 商品显示价格（人民币）。 |
| `data.product_id` | String | 1688 商品 ID（offer id）。 |
| `data.repurchase_rate` | Number | 复购率（百分比值）。 |
| `data.review_count` | Integer | 评论数。 |
| `data.sales_of_30d` | Integer | 近 30 天销量（件）。 |
| `data.score` | Number | 商品评分（满分 5）。 |
| `data.service_score` | Number | 综合服务分（满分 5）。 |
| `data.service_score_detail[]` | Array | 服务评分明细数组。 |
| `data.service_score_detail[].score` | Number | 该维度的分值（满分 5）。 |
| `data.service_score_detail[].title` | String | 评分维度名称。 |
| `data.shipping_origin` | String | 发货地。 |
| `data.sku_count` | Integer | SKU（变体）数量。 |
| `data.store_name` | String | 供应商店铺名称。 |
| `data.title` | String | 商品标题。 |
| `data.url` | String | 1688 商品详情页 URL。 |
| `data.wholesale_price_range[]` | Array | 批发阶梯价格数组。 |
| `data.wholesale_price_range[].price` | Number | 该阶梯的单价（字符串，单位人民币）。 |
| `data.wholesale_price_range[].purchase_quantity` | String | 该阶梯的采购数量条件。 |

## 使用要点

- 必填字段：`product_id`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/ali1688-product-request" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id":"789542752062"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

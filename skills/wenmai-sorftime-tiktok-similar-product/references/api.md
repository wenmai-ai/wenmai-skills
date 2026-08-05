# Wenmai Sorftime `tiktok_similar_product` API 参考

相似产品查询。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/tiktok-similar-product`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`tiktok_similar_product`
- **脚本入口**：`scripts/tiktok_similar_product.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_name` | String | 是 | 要查询的商品名称。 |
| `page` | Integer | 否 | 查询结果的页码。默认第 1 页，每页返回 20 条记录。 |
| `site` | String；允许值："US"、"MY"、"PH"、"VN"、"TH"、"ID"、"GB"、"JP" | 是 | TikTok 站点。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "product_name": "wireless earbuds",
  "site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.brand_name` | String | 商品品牌（缺失时为空字符串）。 |
| `data.cumulative_sale_count` | Integer | 累计销量（件）。 |
| `data.monthly_sale_amount` | Number | 月销售额（本地货币；US 站点为 USD）。 |
| `data.monthly_sale_count` | Integer | 月销量（件）。 |
| `data.monthly_sale_count_growth` | Number | 月环比销量增长（百分比；正数=增长，负数=下降）。 |
| `data.photo` | String | 商品主图 URL。 |
| `data.price` | Number | 价格（本地货币）。 |
| `data.product_id` | String | TikTok 商品 ID（字符串），用于后续 detail/trend/video/author 查询。 |
| `data.product_name` | String | 商品标题。 |
| `data.review_count` | Integer | 总评论数。 |
| `data.star` | Number | 星级（满分 5）。 |
| `data.store_name` | String | 卖家店铺名称。 |

## 使用要点

- 必填字段：`product_name`, `site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/tiktok-similar-product" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_name":"wireless earbuds","site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

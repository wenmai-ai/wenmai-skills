# Wenmai Sorftime `temu_category_request` API 参考

类目Best Seller查询。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/temu-category-request`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`temu_category_request`
- **脚本入口**：`scripts/temu_category_request.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `node_id` | String | 是 | 要查询的类目 ID。 |
| `page` | Integer | 否 | 查询结果的页码。默认第 1 页。 |
| `site` | String；允许值："US"、"EU" | 是 | Temu 站点，支持：701:US、705:EU。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "node_id": "248",
  "site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.is_sub_category` | Boolean | 是否为叶子类目（true=是，false=否）。 |
| `data.products[]` | Array | 该类目下的 Best Seller 商品列表。 |
| `data.products[].brand_name` | String | 品牌名称。 |
| `data.products[].bsr_category[]` | Array | 商品所在的 BSR（Best Seller Rank）类目数组。 |
| `data.products[].bsr_category[].name` | String | BSR 类目名称。 |
| `data.products[].bsr_category[].node_id` | String | BSR 类目节点 ID。 |
| `data.products[].cumulative_sale_count` | Integer | 商品的累计销量。 |
| `data.products[].department` | Object | 商品所属一级类目。 |
| `data.products[].department.name` | String | 一级类目名称。 |
| `data.products[].department.node_id` | String | 一级类目节点 ID。 |
| `data.products[].managed_type` | String | 托管类型（半托管 / 全托管 等）。 |
| `data.products[].monthly_sale_amount` | Number | 商品的月销售额。 |
| `data.products[].monthly_sale_count` | Integer | 商品的月销量。 |
| `data.products[].monthly_sale_count_growth` | Number | 商品月销量的月环比增长率（%）。 |
| `data.products[].photo` | String | 商品主图 URL。 |
| `data.products[].price` | Number | 商品售价。 |
| `data.products[].product_id` | String | Temu 商品 ID。 |
| `data.products[].product_name` | String | 商品标题。 |
| `data.products[].review_count` | Integer | 商品评论数。 |
| `data.products[].sale_time` | String | 商品上架日期（yyyy-MM-dd）。 |
| `data.products[].star` | Number | 商品星级。 |
| `data.products[].store_name` | String | 店铺名称（可能是店铺显示名或数字形式的 ShopId）。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/temu-category-request" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"node_id":"248","site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

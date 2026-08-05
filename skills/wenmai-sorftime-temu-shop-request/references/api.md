# Wenmai Sorftime `temu_shop_request` API 参考

店铺详情。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/temu-shop-request`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`temu_shop_request`
- **脚本入口**：`scripts/temu_shop_request.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shop_id` | String | 是 | 要查询的店铺 ID。 |
| `site` | String；允许值："US"、"EU" | 是 | Temu 站点，支持：701:US、705:EU。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "shop_id": "16197192",
  "site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.fans_count` | Integer | 店铺粉丝数（重复/备用字段；本样本中为 0）。 |
| `data.managed_type` | String | 店铺托管类型（半托管 / 全托管 等）。 |
| `data.max_sale_category` | Object | 销售额最高的类目。 |
| `data.max_sale_category.name` | String | 类目名称。 |
| `data.max_sale_category.node_id` | String | 类目节点 ID。 |
| `data.max_sale_category.sale_count` | Integer | 该类目的销量。 |
| `data.product_count` | Integer | 店铺在售商品数。 |
| `data.sale_amount` | Number | 店铺总销售额。 |
| `data.sale_count` | Integer | 店铺总销量（聚合自 Top-500）。 |
| `data.second_sale_category` | Object | 销售额第二的类目。 |
| `data.second_sale_category.name` | String | 类目名称。 |
| `data.second_sale_category.node_id` | String | 类目节点 ID。 |
| `data.second_sale_category.sale_count` | Integer | 该类目的销量。 |
| `data.seller_star` | Number | 卖家评分（本样本中为 0.0）。 |
| `data.shop_fans_count` | Integer | 店铺粉丝数。 |
| `data.shop_id` | String | Temu 店铺 ID。 |
| `data.shop_name` | String | 店铺名称。 |
| `data.shop_photo` | String | 店铺头像 / Logo 图片 URL。 |
| `data.shop_star` | Number | 店铺综合星级。 |
| `data.shop_type` | String | 店铺类型（如 "Star Seller" / "明星卖家"）。 |
| `data.third_sale_category` | Object | 销售额第三的类目。 |
| `data.third_sale_category.name` | String | 类目名称。 |
| `data.third_sale_category.node_id` | String | 类目节点 ID。 |
| `data.third_sale_category.sale_count` | Integer | 该类目的销量。 |
| `data.top500_products[]` | Array | 店铺 Top-500 商品列表（本样本中为空数组）。 |

## 使用要点

- 必填字段：`shop_id`, `site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/temu-shop-request" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shop_id":"16197192","site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

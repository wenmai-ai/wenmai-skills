# Wenmai Sorftime `product_detail` API 参考

产品详情。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/product-detail`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`product_detail`
- **脚本入口**：`scripts/product_detail.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | String | 是 | 商品 ASIN，仅支持单 ASIN 查询。 |
| `amz_site` | String；允许值："US"、"GB"、"DE"、"FR"、"IN"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、IN、CA、JP、ES、IT、MX、AE、AU、BR、SA。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "asin": "B0CZPLV566",
  "amz_site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.a_plus` | Boolean | 是否包含 A+ 内容。 |
| `data.asin` | String | 商品 ASIN。 |
| `data.attributes` | String | 商品属性键值对。 |
| `data.brand` | String | 品牌。 |
| `data.category` | String | 商品所属类目（Amazon 上展示的顶级类目）。 |
| `data.days_on_shelf` | Integer | 上架天数。 |
| `data.description` | String | 商品描述（包含 HTML 标签）。 |
| `data.fba_fee` | Number | FBA 费用（USD）。 |
| `data.gross_profit` | Number | 毛利润（USD）。 |
| `data.gross_profit_rate` | Number | 毛利率（百分比）。 |
| `data.main_image` | String | 主图 URL。 |
| `data.monthly_sales_amount` | String | 月销售额（USD）。 |
| `data.monthly_sales_volume` | String | 月销量（件）。 |
| `data.node_id` | String | 类目节点 ID。 |
| `data.online_date` | String | 上架日期（yyyy-MM-dd）。 |
| `data.package_size_cm` | String | 包装尺寸 L*W*H（cm）。 |
| `data.parent_asin` | String | 父 ASIN。 |
| `data.price` | Number | 售价（USD）。 |
| `data.review_count` | Integer | 评论数。 |
| `data.seller_name` | String | 卖家名称。 |
| `data.star_rating` | Number | 星级（满分 5）。 |
| `data.subcategory` | String | 子类目及其销量排名。 |
| `data.title` | String | 商品标题。 |
| `data.top_category` | String | 一级类目及其排名。 |
| `data.variation_count` | Integer | 变体（子 ASIN）数量。 |
| `data.weight_g` | Number | 重量（g）。 |

## 使用要点

- 必填字段：`asin`, `amz_site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/product-detail" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B0CZPLV566","amz_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

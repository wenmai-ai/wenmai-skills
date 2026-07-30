# Wenmai Sorftime `product_search` API 参考

选产品（实时）。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/product-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`product_search`
- **脚本入口**：`scripts/product_search.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `seasonal_popular_product` | String；可选值："Both"、"January"、"February"、"March"、"April"、"May"、"June"、"July"、"August"、"September"、"October"、"November"、"December" | 否 | 可选：筛选旺季为指定月份的产品。允许值：Both、January、February、March、April、May、June、July、August、September、October、November、December；默认 Both。 |
| `brand` | String | 否 | 可选：筛选指定品牌的产品。 |
| `seller_name` | String | 否 | 可选：筛选指定卖家的产品。 |
| `search_name` | String | 否 | 可选：按此名称搜索相关产品。 |
| `property_name` | String | 否 | 可选：筛选标题或属性中包含指定属性的产品。 |
| `price_min` | Number | 否 | 可选：筛选售价大于等于该值的产品。 |
| `price_max` | Number | 否 | 可选：筛选售价小于等于该值的产品。 |
| `month_sales_volume_min` | Number | 否 | 可选：筛选月销量大于等于该值的产品。 |
| `month_sales_volume_max` | Number | 否 | 可选：筛选月销量小于等于该值的产品。 |
| `ratings_min` | Number | 否 | 可选：筛选星级大于等于该值的产品。 |
| `ratings_max` | Number | 否 | 可选：筛选星级小于等于该值的产品。 |
| `ratings_count_min` | Number | 否 | 可选：筛选评论数大于等于该值的产品。 |
| `ratings_count_max` | Number | 否 | 可选：筛选评论数小于等于该值的产品。 |
| `subcategory_sales_volume_rank_min` | Number | 否 | 可选：筛选子类目销量排名大于等于该值的产品。 |
| `subcategory_sales_volume_rank_max` | Number | 否 | 可选：筛选子类目销量排名小于等于该值的产品。 |
| `delivery_type` | String；可选值："Both"、"FBM"、"FBA"、"AmzFBA" | 否 | 可选：按履约方式筛选产品。允许值：Both、FBM、FBA；默认 Both。 |
| `variation_count_min` | Number | 否 | 可选：筛选变体（子 ASIN）数量大于等于该值的产品。 |
| `variation_count_max` | Number | 否 | 可选：筛选变体（子 ASIN）数量小于等于该值的产品。 |
| `sortby_potential_index` | Boolean | 否 | 可选：若为 true，则按潜力指数从高到低排序。 |
| `page` | Number | 否 | 查询结果的页码。默认 1，每页返回 20 条记录。 |
| `amz_site` | String；允许值："US"、"GB"、"DE"、"FR"、"IN"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、IN、CA、JP、ES、IT、MX、AE、AU、BR、SA。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "amz_site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.asin` | String | 商品 ASIN。 |
| `data.brand` | String | 品牌。 |
| `data.delivery_type` | String | 履约方式，取值为 `FBA`（卖家通过 Amazon FBA 发货）、`AmzFBA`（第三方卖家如 1688 通过 Amazon FBA 发货）、`FBM`（卖家自发货）之一。 |
| `data.fba_fee` | Number | FBA 费用（USD）。 |
| `data.fbm_delivery_fee` | Number | FBM 配送费（USD）。 |
| `data.main_image` | String | 主图 URL。 |
| `data.monthly_sales_amount` | Number | 月销售额（USD）。 |
| `data.monthly_sales_volume` | Integer | 月销量（件）。 |
| `data.online_date` | String | 上架日期（yyyy-MM-dd）。 |
| `data.package_size` | Integer | 包装尺寸等级编号。 |
| `data.price` | Number | 历史时点的售价（USD）；无值时为 0.0。 |
| `data.review_count` | Integer | 评论数。 |
| `data.star_rating` | Number | 星级（满分 5）。 |
| `data.subcategory` | String | 子类目及其销量排名。 |
| `data.title` | String | 商品标题。 |
| `data.top_category` | String | 一级类目及其排名。 |
| `data.weight` | Number | 重量（lb）。 |

## 使用要点

- 必填字段：`amz_site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/product-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"amz_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

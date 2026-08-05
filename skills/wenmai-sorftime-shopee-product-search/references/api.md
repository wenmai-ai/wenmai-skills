# Wenmai Sorftime `shopee_product_search` API 参考

选产品。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-product-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`shopee_product_search`
- **脚本入口**：`scripts/shopee_product_search.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_id` | String | 否 | 可选。若指定：基于该 ProductId 查询相似商品（注：并非只查该 ProductId，若需精确获取该商品请调用 ProductRequest 工具）。 |
| `node_id` | String | 否 | 可选。若指定：在该类目范围内查询（不限于子类目）。 |
| `price_range_min` | Number | 否 | 可选。若指定：限制最低售价（值 >= 设置值）。 |
| `price_range_max` | Number | 否 | 可选。若指定：限制最高售价（值 <= 设置值）。 |
| `month_sale_volume_range_min` | Integer | 否 | 可选。若指定：限制最低月销量（值 >= 设置值）。 |
| `month_sale_volume_range_max` | Integer | 否 | 可选。若指定：限制最高月销量（值 <= 设置值）。 |
| `online_date_range_min` | String | 否 | 可选。若指定：限制上架起始日期（yyyy-MM-dd）。 |
| `online_date_range_max` | String | 否 | 可选。若指定：限制上架结束日期（yyyy-MM-dd）。 |
| `star_range_min` | Number | 否 | 可选。若指定：限制最低星级。 |
| `star_range_max` | Number | 否 | 可选。若指定：限制最高星级。 |
| `comment_count_range_min` | Integer | 否 | 可选。若指定：限制最低评论数。 |
| `comment_count_range_max` | Integer | 否 | 可选。若指定：限制最高评论数。 |
| `variation_count_range_min` | Integer | 否 | 可选。若指定：限制最低变体数。 |
| `variation_count_range_max` | Integer | 否 | 可选。若指定：限制最高变体数。 |
| `shop_location` | Integer | 否 | 可选。店铺位置类型：1 = 本土店，2 = 跨境店。 |
| `shop_type` | Integer | 否 | 可选。店铺类型：1 = 普通店，2 = 优选店，3 = 旗舰店。 |
| `site` | String；允许值："VN"、"ID"、"SG"、"TH"、"MY"、"TW"、"PH"、"BR" | 是 | Shopee 站点代码。允许值：`VN`、`ID`、`SG`、`TH`、`MY`、`TW`、`PH`、`BR`。 实际调用必须明确指定。 |
| `page` | Integer | 否 | 分页查询，每页最多 20 个产品。默认 1（页码从 1 开始，非 0）。 |

## 请求示例

```json
{
  "site": "TH"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.bad_rate` | Number | 差评率（%，0~100）。 |
| `data.category` | String | 一级类目（多语言）。 |
| `data.good_rate` | Number | 好评率（%，0~100）。 |
| `data.his_sales_count` | Integer | 累计销量（件）。 |
| `data.like_count` | Integer | 点赞 / 收藏数。 |
| `data.monthly_sales_growth` | Number | 月销量增长率（%，可正可负）。 |
| `data.photo[]` | Array | 商品图片 URL 数组。 |
| `data.price` | Number | 售价（查询站点的本地货币：SG 站 SGD、TH 站 THB、MY 站 MYR、ID 站 IDR、VN 站 VND、TW 站 TWD、PH 站 PHP、BR 站 BRL）。 |
| `data.product_id` | String | Shopee 商品 ID。 |
| `data.ratings` | Number | 星级（满分 5）。 |
| `data.ratings_count` | Integer | 评论数。 |
| `data.sale_time` | String | 上架日期（yyyy-MM-dd）。 |
| `data.sales_amount` | Number | 月销售额（查询站点的本地货币）。 |
| `data.sales_count` | Integer | 月销量（件）。 |
| `data.sales_count_of_7d` | Integer | 近 7 天销量（件）。 |
| `data.shop_loc_type` | String | 店铺位置类型（本土店 / 跨境店）。 |
| `data.shop_type` | String | 店铺类型（普通店 / 优选店 / 旗舰店）。 |
| `data.sub_category[]` | Array | 子类目标签数组。 |
| `data.title` | String | 商品标题。 |
| `data.variation_count` | Integer | 变体（SKU）数量。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-product-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"site":"TH"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

# Wenmai Sorftime `shopee_keyword_relation_results` API 参考

关键词关联产品。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-keyword-relation-results`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`shopee_keyword_relation_results`
- **脚本入口**：`scripts/shopee_keyword_relation_results.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keyword` | String | 否 | 要查询的关键词（如 summer dress）。 |
| `page` | Integer | 否 | 查询结果的页码。默认第 1 页，每页返回 20 条记录。 |
| `site` | String；允许值："VN"、"ID"、"SG"、"TH"、"MY"、"TW"、"PH"、"BR" | 是 | Shopee 站点，支持：201:VN、202:ID、203:SG、204:TH、205:MY、206:TW、207:PH、208:BR。 实际调用必须明确指定。 |

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
| `data.category` | String | 类目（可能为空字符串）。 |
| `data.has_main_video` | Boolean | 商品是否有主图视频。 |
| `data.his_sales_count` | Integer | 累计销量（件）。 |
| `data.is_official_store` | Boolean | 店铺是否为 Shopee 官方店。 |
| `data.like_count` | Integer | 点赞 / 收藏数。 |
| `data.photo[]` | Array | 商品图片 URL 数组。 |
| `data.price` | Number | 售价（THB）。 |
| `data.product_id` | String | Shopee 商品 ID。 |
| `data.ratings` | Number | 星级（满分 5）。 |
| `data.ratings_count` | Integer | 评论数。 |
| `data.sale_time` | String | 上架日期（yyyy-MM-dd）。 |
| `data.sales_amount` | Number | 月销售额（THB）。 |
| `data.sales_count` | Integer | 月销量（件）。 |
| `data.saleshare` | Number | 该商品在关键词下的销量份额，以小数百分比表示（如 22.94 = 22.94%）。 |
| `data.shop_name` | String | 店铺名称。 |
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-keyword-relation-results" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"site":"TH"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

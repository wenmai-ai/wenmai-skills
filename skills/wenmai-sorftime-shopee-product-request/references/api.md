# Wenmai Sorftime `shopee_product_request` API 参考

产品详情。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-product-request`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`shopee_product_request`
- **脚本入口**：`scripts/shopee_product_request.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_id` | String | 是 | 要查询的商品 ID。 |
| `site` | String；允许值："VN"、"ID"、"SG"、"TH"、"MY"、"TW"、"PH"、"BR" | 是 | Shopee 站点，支持：201:VN、202:ID、203:SG、204:TH、205:MY、206:TW、207:PH、208:BR。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "product_id": "51953524682",
  "site": "TH"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.brand` | String | 品牌名称。 |
| `data.brand_id` | String | 品牌 ID。 |
| `data.bsr_category[]` | Array | BSR 类目数组 [类目名, 类目 ID, 排名]。 |
| `data.coupon_str` | String | 店铺优惠券描述文本。 |
| `data.discount` | Number | 折扣率（小数）。 |
| `data.his_sales_count` | Integer | 累计销量（件）。 |
| `data.list_price` | Number | 原价 / 划线价（THB）。 |
| `data.photo[]` | Array | 商品图片 URL 数组。 |
| `data.price` | Number | 当前售价（THB）。 |
| `data.product_id` | String | Shopee 商品 ID。 |
| `data.rating_detail[]` | Array | 评论数分布（1 星到 5 星）。 |
| `data.ratings` | Number | 商品综合星级（满分 5）。 |
| `data.ratings_count` | Integer | 评论数。 |
| `data.sale_is_correction` | String | 销量修正时间。 |
| `data.sale_time` | String | 上架日期（yyyy-MM-dd）。 |
| `data.sales_amount` | Number | 月销售额（THB）。 |
| `data.sales_calc_time` | String | 销量计算时间。 |
| `data.sales_count` | Integer | 月销量（件）。 |
| `data.shop_id` | String | 店铺 ID。 |
| `data.shop_loc_type` | String | 店铺位置类型（本土店 / 跨境店）。 |
| `data.shop_location` | String | 店铺位置（字符串，可能为空）。 |
| `data.shop_name` | String | 店铺名称。 |
| `data.shop_type` | String | 店铺类型（普通店 / 优选店 / 旗舰店）。 |
| `data.title` | String | 商品标题。 |

## 使用要点

- 必填字段：`product_id`, `site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-product-request" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id":"51953524682","site":"TH"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

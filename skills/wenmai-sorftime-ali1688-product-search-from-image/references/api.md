# Wenmai Sorftime `ali1688_product_search_from_image` API 参考

1688平台以图搜产品。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/ali1688-product-search-from-image`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ali1688_product_search_from_image`
- **脚本入口**：`scripts/ali1688_product_search_from_image.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `image_url` | String | 是 | 图片 URL，必填。需传入公网图片 URL，且图片大小不超过 1MB。 |
| `page` | Integer | 否 | 查询数据的页码，默认第 1 页。 |

## 请求示例

```json
{
  "image_url": "https://cbu01.alicdn.com/img/ibank/O1CN01HrY28j1LS4eMNQV1G_!!3086091297-0-cib.jpg"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.is_drop_shipping` | Boolean | 是否支持一件代发（Boolean）。 |
| `data.min_order_quantity` | Integer | 最小起批量（Integer）。 |
| `data.offer_identities[]` | Array | 商品标签数组，例如 `["严选"]`。 |
| `data.online_date` | String | 上线时间（yyyy-MM-dd）。 |
| `data.photo` | String | 商品主图 URL。 |
| `data.price` | Number | 商品售价（Decimal，单位人民币）。 |
| `data.product_id` | String | 商品 ID。 |
| `data.repurchase_rate` | Number | 复购率，单位 %。 |
| `data.sales_of_30d` | Integer | 近 30 日销售件数（Integer）。 |
| `data.seller_identities[]` | Array | 商家身份标签数组，例如 `["超级工厂", "实力商家"]`。 |
| `data.service_score` | Number | 服务综合星级（数值，0-5）。 |
| `data.service_score_detail[]` | Array | 服务评分明细，JSON 数组结构，每个元素含 `title` 和 `score` 字段。 |
| `data.service_score_detail[].score` | Number | 该维度的分值（0-5）。 |
| `data.service_score_detail[].title` | String | 评分维度名称（采购咨询 / 物流时效 / 纠纷解决 / 品质体验 / 退换体验）。 |
| `data.shipping_origin` | String | 发货地。 |
| `data.shipping_time` | String | 发货时效（中文描述，例如 "24 小时发货"）。 |
| `data.store_name` | String | 店铺名称。 |
| `data.title` | String | 商品标题。 |
| `data.url` | String | 商品链接（含 `?sk=order` 下单跳转参数）。 |

## 使用要点

- 必填字段：`image_url`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/ali1688-product-search-from-image" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"image_url":"https://cbu01.alicdn.com/img/ibank/O1CN01HrY28j1LS4eMNQV1G_!!3086091297-0-cib.jpg"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

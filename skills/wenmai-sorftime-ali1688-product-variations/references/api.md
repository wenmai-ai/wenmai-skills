# Wenmai Sorftime `ali1688_product_variations` API 参考

1688平台产品SKU数据查询。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/ali1688-product-variations`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ali1688_product_variations`
- **脚本入口**：`scripts/ali1688_product_variations.py`
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
| `data.height` | Number | 包装高度（cm，0 表示未填写）。 |
| `data.length` | Number | 包装长度（cm，0 表示未填写）。 |
| `data.offer_price` | Number | SKU 实际报价（人民币）。 |
| `data.pkg_size_source` | String | 包装尺寸/重量数据来源（如 "商家自填写"）。 |
| `data.price` | Number | SKU 显示价格（人民币）。 |
| `data.sku_id` | String | 唯一的 SKU（变体）标识符。 |
| `data.sku_name` | String | SKU 名称，通常由规格属性组成（如颜色 + 容量）。 |
| `data.stock` | Integer | SKU 库存数量。 |
| `data.weight` | Number | 包装重量（kg）。 |
| `data.width` | Number | 包装宽度（cm，0 表示未填写）。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/ali1688-product-variations" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id":"789542752062"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

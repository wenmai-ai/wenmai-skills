# Wenmai Sorftime `keyword_search_results` API 参考

关键词搜索结果。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/keyword-search-results`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`keyword_search_results`
- **脚本入口**：`scripts/keyword_search_results.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keyword` | String | 是 | 要查询的关键词。 |
| `keyword_support_site` | String；允许值："US"、"GB"、"DE"、"FR"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、CA、JP、ES、IT、MX、AE、AU、BR、SA。 实际调用必须明确指定。 |
| `page` | Number | 否 | 查询结果的页码。默认 1，每页返回 20 条记录。 |
| `position_type` | Number | 否 | 曝光位置类型。0：全部，1：仅自然位（默认），2：仅广告位。 |

## 请求示例

```json
{
  "keyword": "wireless earbuds",
  "keyword_support_site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.asin` | String | 商品 ASIN。 |
| `data.brand` | String | 商品品牌。 |
| `data.monthly_sales_volume` | Integer | 该商品的月销量。 |
| `data.monthly_sales_volume_share_in_top100` | String | 该商品的月销量占该关键词搜索结果 Top-100 中的份额。 |
| `data.price` | Integer | 商品价格，以整数表示（如 1537 即 USD 15.37，即以美分为单位）。 |
| `data.seller` | String | 商品卖家。 |
| `data.title` | String | 商品标题。 |

## 使用要点

- 必填字段：`keyword`, `keyword_support_site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/keyword-search-results" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword":"wireless earbuds","keyword_support_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

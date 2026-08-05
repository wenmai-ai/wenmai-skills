# Wenmai Sorftime `walmart_keyword_search_from_name` API 参考

按名称查询 Walmart 热搜关键词。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/walmart-keyword-search-from-name`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`walmart_keyword_search_from_name`
- **脚本入口**：`scripts/walmart_keyword_search_from_name.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | 是 | 要查询的关键词名称。 |
| `page` | integer | 否 | 查询结果页码，默认第 1 页，每页返回 20 条记录。 |

## 请求示例

```json
{
  "name": "wireless earbuds"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data[].keyword` | string | 关键词文本。 |
| `data[].keyword_cn_name` | string | 关键词中文翻译，由机器翻译生成，可能为空。 |
| `data[].images[]` | array | 该关键词的代表商品图片 URL 数组。 |
| `data[].update` | string | 关键词数据更新日期，格式为 yyyyMMdd。 |
| `data[].rank` | integer | 关键词在热搜榜中的周搜索量或月搜索量排名。 |
| `data[].search_volume` | integer | 关键词月搜索量。 |
| `data[].product_count` | integer | 该关键词下的商品数量。 |
| `data[].search_first_page_avg_price` | number | 关键词搜索结果首页商品的平均售价，单位为美元。 |
| `data[].search_first_page_avg_reviews` | number | 关键词搜索结果首页商品的平均评论数。 |
| `data[].search_first_page_avg_star` | number | 关键词搜索结果首页商品的平均星级，满分 5 分。 |

## 使用要点

- 必填字段：`name`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/walmart-keyword-search-from-name" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name":"wireless earbuds"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

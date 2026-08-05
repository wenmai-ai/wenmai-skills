# Wenmai Sorftime `walmart_product_traffic_terms` API 参考

产品流量词反查。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/walmart-product-traffic-terms`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`walmart_product_traffic_terms`
- **脚本入口**：`scripts/walmart_product_traffic_terms.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_id` | String | 是 | 要查询的商品 ID。 |
| `page` | Number | 否 | 查询结果的页码。默认第 1 页，每页返回 20 条记录。 |

## 请求示例

```json
{
  "product_id": "11381374703"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.ad_position` | String | 广告位位置（格式 "page,row/total_rows"，"0,0/0" 表示无广告曝光）。 |
| `data.keyword` | Object | 关键词对象（包含该曝光关键词的详细指标；见下方子字段）。 |
| `data.keyword.keyword` | Object | 关键词名称。 |
| `data.keyword.keyword_cn_name` | String | 关键词中文翻译（机器翻译，可能为空字符串）。 |
| `data.keyword.product_count` | Integer | 该关键词下的商品数。 |
| `data.keyword.rank` | Integer | 关键词周搜索量排名。 |
| `data.keyword.search_first_page_avg_price` | Number | 该关键词搜索结果首页的平均售价（USD）。 |
| `data.keyword.search_first_page_avg_reviews` | Number | 该关键词搜索结果首页的平均评论数。 |
| `data.keyword.search_first_page_avg_star` | Number | 该关键词搜索结果首页的平均星级（满分 5）。 |
| `data.keyword.search_volume` | Number | 关键词月搜索量。 |
| `data.keyword.update` | String | 关键词数据更新日期（yyyyMMDD）。 |
| `data.organic_position` | String | 自然位位置（格式 "page,row/total_rows"）。 |
| `data.recently_position` | String | 近 30 天的曝光位置（格式 "page,row/total_rows"）。 |
| `data.show_share` | Number | 在该关键词下商品的曝光份额占其总曝光的比例（%）。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/walmart-product-traffic-terms" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id":"11381374703"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

# Wenmai Sorftime `keyword_detail` API 参考

关键词详情。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/keyword-detail`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`keyword_detail`
- **脚本入口**：`scripts/keyword_detail.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keyword` | String | 是 | 要查询的关键词。 |
| `keyword_support_site` | String；允许值："US"、"GB"、"DE"、"FR"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、CA、JP、ES、IT、MX、AE、AU、BR、SA。 实际调用必须明确指定。 |

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
| `data.keyword` | String | 所查询的关键词文本。 |
| `data.monthly_search_volume` | String | 月搜索量（字符串）。 |
| `data.recent_15d_top3_pages_organic_top100_stats` | Object | 近 15 天前 3 页自然位销量 Top-100 的统计对象。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_brand[]` | Array | 销量前 5 名品牌数组。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_brand[].brand` | String | 品牌名称。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_brand[].monthly_sales` | String | 该品牌样本中月销量合计及占比的文本描述。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_brand[].product_count` | String | 该品牌样本中商品数量的文本描述。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_product[]` | Array | 销量前 5 名商品数组。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_product[].asin` | String | 商品 ASIN。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_product[].brand` | String | 商品品牌。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_product[].monthly_sales` | String | 该商品月销量及占比的文本描述。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_product[].price` | Number | 商品价格（USD）。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_product[].seller` | String | 商品卖家。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_product[].title` | String | 商品标题。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_product[].url` | String | 商品详情页 URL。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_seller[]` | Array | 销量前 5 名卖家数组。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_seller[].monthly_sales` | String | 该卖家样本中月销量合计及占比的文本描述。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_seller[].product_count` | String | 该卖家样本中商品数量的文本描述。 |
| `data.recent_15d_top3_pages_organic_top100_stats.top5_seller[].seller` | String | 卖家名称。 |
| `data.recommended_cpc_bid` | String | 推荐 CPC 出价（字符串，USD）。 |
| `data.search_result_competitor_count` | String | 搜索结果的竞品数量（字符串）。 |
| `data.search_result_first_page_stats` | String | 搜索结果首页的文本统计，覆盖近 15 天首页销量 Top-100 的自然位/广告位评论数、星级与优惠券促销情况。 |
| `data.search_volume_peak_season` | String | 该关键词搜索量的旺季月份。 |
| `data.weekly_search_rank` | String | 周搜索量排名（字符串）。 |
| `data.weekly_search_volume` | String | 周搜索量（字符串）。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/keyword-detail" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword":"wireless earbuds","keyword_support_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

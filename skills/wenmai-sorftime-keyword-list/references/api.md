# Wenmai Sorftime `keyword_list` API 参考

实时热搜关键词榜。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/keyword-list`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`keyword_list`
- **脚本入口**：`scripts/keyword_list.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keyword_support_site` | String；允许值："US"、"GB"、"DE"、"FR"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、CA、JP、ES、IT、MX、AE、AU、BR、SA。 实际调用必须明确指定。 |
| `page` | Number | 否 | 查询结果的页码。默认 1，每页返回 20 条记录。 |
| `rank_min` | Number | 否 | 可选：筛选周搜索量排名大于等于该值的关键词。 |
| `rank_max` | Number | 否 | 可选：筛选周搜索量排名小于等于该值的关键词。 |
| `search_volume_min` | Number | 否 | 可选：筛选月搜索量大于等于该值的关键词。 |
| `search_volume_max` | Number | 否 | 可选：筛选月搜索量小于等于该值的关键词。 |

## 请求示例

```json
{
  "keyword_support_site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.click_conversion_rate_90d` | Number | 近 90 天点击转化率；目前仅支持 US 站点，无值时显示 -1。 |
| `data.click_volume_90d` | Integer | 近 90 天点击量；目前仅支持 US 站点，无值时显示 -1。 |
| `data.cpc_exact_bid` | Integer | 参考 CPC 精确匹配出价。 |
| `data.cpc_exact_bid_range[]` | Array | CPC 精确匹配出价区间数组，[min, max]。 |
| `data.data_update_time` | String | 该关键词的数据更新时间，格式 yyyyMMdd。 |
| `data.keyword` | String | 热门关键词文本。 |
| `data.keyword_cn` | String | 关键词的中文翻译。 |
| `data.peak_season` | String | 搜索量的旺季月份；"均衡" 表示全年无明显旺季。 |
| `data.purchase_volume_after_search_90d` | Integer | 近 90 天搜索后购买量；-1 表示无数据。 |
| `data.search_conversion_rate_90d` | Number | 近 90 天搜索转化率；目前仅支持 US 站点，无值时显示 -1。 |
| `data.search_volume_30d` | Integer | 近 30 天搜索量。 |
| `data.top3_product_click_share` | Number | 搜索结果中 Top-3 商品的点击占比（百分比）。 |
| `data.top3_product_conversion_share` | Number | 搜索结果中 Top-3 商品的转化占比（百分比）。 |
| `data.weekly_search_rank` | Integer | 周搜索量排名。 |

## 使用要点

- 必填字段：`keyword_support_site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/keyword-list" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword_support_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

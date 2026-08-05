# Wenmai Sorftime `shopee_keyword_search` API 参考

热搜关键词榜单。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-keyword-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`shopee_keyword_search`
- **脚本入口**：`scripts/shopee_keyword_search.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keyword` | String | 否 | 可选。要查询的关键词（如 summer dress）。若提供则按关键词精确搜索；否则返回热门榜单。 |
| `rank_min` | Integer | 否 | 可选。按最低月排名筛选。 |
| `rank_max` | Integer | 否 | 可选。按最高月排名筛选。 |
| `search_volume_min` | Integer | 否 | 可选。按最低月搜索量筛选。 |
| `search_volume_max` | Integer | 否 | 可选。按最高月搜索量筛选。 |
| `page` | Integer | 否 | 可选。页码，默认第 1 页，每页返回 20 条记录。 |
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
| `data.cpc` | Integer | 最新 CPC（站点货币，如 THB）。 |
| `data.cpc_trend[]` | Array | 历史 CPC 趋势，扁平 [年(yyyyMM), cpc, ...] 数组。 |
| `data.department[]` | Array | 相关类目 ID 数组。 |
| `data.images[]` | Array | 该关键词对应的商品图片 URL 数组。 |
| `data.images_from_product_id[]` | Array | 来源商品 ID（可能为空）。 |
| `data.keyword` | String | 关键词文本（多语言，如英文 / 泰文）。 |
| `data.keyword_cn_name` | String | 可选的关键词中文释义（可能缺失）。 |
| `data.product_count` | Integer | 该关键词下的商品数量。 |
| `data.rank` | Integer | 当前搜索量排名。 |
| `data.search_rank_trend[]` | Array | 历史排名趋势，扁平 [年(yyyyMM), 排名, ...] 数组。 |
| `data.search_volume` | Integer | 最新月搜索量。 |
| `data.search_volume_trend[]` | Array | 历史搜索量趋势，扁平 [年(yyyyMM), 搜索量, ...] 数组。 |
| `data.season` | String | 季节性信息（如 "均衡" = 全年均衡，或列出旺季月份）。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-keyword-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"site":"TH"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

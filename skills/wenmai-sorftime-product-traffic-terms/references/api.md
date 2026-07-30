# Wenmai Sorftime `product_traffic_terms` API 参考

产品流量词反查。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/product-traffic-terms`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`product_traffic_terms`
- **脚本入口**：`scripts/product_traffic_terms.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | String | 是 | 商品 ASIN。 |
| `page` | Number | 否 | 查询结果的页码。默认 1，每页返回 20 条记录。 |
| `amz_site` | String；允许值："US"、"GB"、"DE"、"FR"、"IN"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、IN、CA、JP、ES、IT、MX、AE、AU、BR、SA。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "asin": "B0CZPLV566",
  "amz_site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.exposure_position` | String | 商品的曝光位置类型（自然位 / 广告位 / 两者皆有，逗号分隔）。 |
| `data.keyword` | String | 反查得到的关键词。 |
| `data.latest_ad_exposure_time` | String | 最新广告位曝光时间（yyyy-MM-dd HH:mm）；无曝光时为空。 |
| `data.latest_ad_position` | String | 最新广告位曝光位置文本（如 "Page X, Pos Y/Z"）；无曝光时为空。 |
| `data.latest_organic_exposure_time` | String | 最新自然位曝光时间（yyyy-MM-dd HH:mm）；无曝光时为空。 |
| `data.latest_organic_position` | String | 最新自然位曝光位置文本（如 "Page X, Pos Y/Z"）；无曝光时为空。 |
| `data.monthly_search_volume` | Integer | 该关键词的月搜索量。 |
| `data.recommended_bid` | String | 该关键词的推荐 CPC 出价（字符串，USD）。 |
| `data.recommended_bid_range` | String | 该关键词的推荐 CPC 出价区间，如 "0.38-0.63"。 |

## 使用要点

- 必填字段：`asin`, `amz_site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/product-traffic-terms" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B0CZPLV566","amz_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。

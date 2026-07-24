# Wenmai XYDC asin商品信息趋势图（天） API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/xydc/get-asin-info-trends`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`get_asin_info_trends`
- **接口说明**：asin商品信息趋势图（天）。
- **脚本入口**：`scripts/xydc_asin_info_trends.py`，脚本参数即标准 API POST Body JSON

### 运行时覆盖

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `WENMAI_API_ORIGIN` | Wenmai API 地址 | `https://all-api.wenmai-ai.com` |
| `WENMAI_API_BASE_PATH` | 标准 API Base Path | `/wmapi/v1` |
| `WENMAI_API_TIMEOUT` | HTTP 超时时间，单位秒 | `120` |

## 请求参数

POST Body（JSON）：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `asin` | string | 是 | ASIN；示例：`B09PCSR9SX`。 |
| `country` | string | 是 | 站点国家码；示例：`US`。 |
| `end_date` | string | 是 | 结束日期 YYYY-MM-DD；示例：`2026-06-07`。 |
| `start_date` | string | 是 | 开始日期 YYYY-MM-DD；示例：`2026-06-01`。 |

## 请求示例

```json
{
  "asin": "B09PCSR9SX",
  "country": "US",
  "start_date": "2026-06-01",
  "end_date": "2026-06-07"
}
```

## 响应结构

公共响应字段：`code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.country` | string | 国家。 |
| `data.asin` | string | ASIN。 |
| `data.trends` | Array | data.trends 字段。 |
| `data.trends[].date` | string | 日期（YYYY-MM-DD格式）。 |
| `data.trends[].ratings` | integer | Ratings数量。 |
| `data.trends[].stars` | string | Ratings评分。 |
| `data.trends[].priceDistribution` | object | 价格及促销数据。 |
| `data.trends[].priceDistribution.display` | string | 展示价格（非划线价）。 |
| `data.trends[].priceDistribution.deal` | string | Deal价格。 |
| `data.trends[].priceDistribution.strikethrough` | string | 划线价。 |
| `data.trends[].priceDistribution.prime` | string | Prime价格。 |
| `data.trends[].priceDistribution.promotion` | Array | Promotion列表。 |
| `data.trends[].priceDistribution.coupon` | Array | Coupon列表。 |
| `data.trends[].priceDistribution.subscribe` | Array | Subscription列表。 |
| `data.trends[].priceDistribution.other` | Array | 其它促销列表。 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/xydc/get-asin-info-trends`。
- 成功响应位于 `data`；失败时优先读取 `code`、`message`、`requestId` 和 HTTP 状态。
- 保留用户给出的 ASIN、关键词、站点国家码、日期/月/周范围、分页和筛选条件，不要擅自扩大查询窗口。
- 输出分析时保留原始字段名，确保 ASIN、关键词、日期、排名、流量分数、订单量、BSR、ABA 或广告活动 ID 可追溯。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按请求参数表修正 ASIN、关键词、站点国家码、日期/月/周格式、分页范围和必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/xydc/get-asin-info-trends" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B09PCSR9SX", "country": "US", "start_date": "2026-06-01", "end_date": "2026-06-07"}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs#xydc-get_asin_info_trends（2026-07-07 访问）。

# Wenmai XYDC 关键词分析列表（月） API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/xydc/get-keyword-analysis-monthly`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`get_keyword_analysis_monthly`
- **接口说明**：关键词分析列表（月）。
- **脚本入口**：`scripts/xydc_keyword_analysis_monthly.py`，脚本参数即标准 API POST Body JSON

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
| `country` | string | 是 | country；示例：`US`。 |
| `end_month` | string | 是 | 结束月份 YYYY-MM；示例：`2026-06`。 |
| `keyword` | string | 是 | keyword；示例：`usb c cable`。 |
| `page` | integer | 否 | 页码；示例：`1`。 |
| `page_size` | integer | 否 | 每页数量；示例：`20`。 |
| `sort_field` | string | 否 | 排序字段，默认 traffic。 |
| `sort_order` | string | 否 | 排序方向 asc/desc。 |
| `start_month` | string | 是 | 开始月份 YYYY-MM；示例：`2026-05`。 |

## 请求示例

```json
{
  "keyword": "usb c cable",
  "country": "US",
  "start_month": "2026-05",
  "end_month": "2026-06",
  "page": 1,
  "page_size": 20
}
```

## 响应结构

公共响应字段：`code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.list` | Array | 数据列表。 |
| `data.list[].country` | string | 国家。 |
| `data.list[].asin` | string | ASIN。 |
| `data.list[].ranks` | Array | 排名数据。 |
| `data.list[].ranks[].position` | string | 展示位。 |
| `data.list[].ranks[].totalRank` | integer | 总排名。 |
| `data.list[].ranks[].page` | integer | 页码。 |
| `data.list[].ranks[].pageRank` | integer | 页内排名。 |
| `data.list[].ranks[].rankTime` | string | 排名时间（ISO 8601标准）。 |
| `data.list[].trafficSummary` | object | 流量数据。 |
| `data.list[].trafficSummary.traffic` | object | 流量。 |
| `data.list[].trafficSummary.traffic.total` | integer | 总流量。 |
| `data.list[].trafficSummary.traffic.organic` | integer | 自然流量。 |
| `data.list[].trafficSummary.traffic.advertising` | integer | 广告流量。 |
| `data.list[].trafficSummary.traffic.totalGrowthRate` | string | 总流量增长率。 |
| `data.list[].trafficSummary.traffic.organicGrowthRate` | string | 自然流量增长率。 |
| `data.list[].trafficSummary.traffic.advertisingGrowthRate` | string | 广告流量增长率。 |
| `data.list[].trafficSummary.trafficRatio` | object | 占词总流量比例。 |
| `data.list[].trafficSummary.trafficRatio.total` | string | 总流量的比例值。 |
| `data.list[].trafficSummary.trafficRatio.organic` | string | 自然流量的比例值。 |
| `data.list[].trafficSummary.trafficRatio.advertising` | string | 广告流量的比例值。 |
| `data.list[].trafficSummary.trafficAcquisitionRate` | object | 流量获取率相关数据。 |
| `data.list[].trafficSummary.trafficAcquisitionRate.total` | string | 总流量获得率。 |
| `data.list[].trafficSummary.trafficAcquisitionRate.organic` | string | 自然流量获得率。 |
| `data.list[].trafficSummary.trafficAcquisitionRate.advertising` | string | 广告流量获得率。 |
| `data.list[].trafficSummary.trafficAcquisitionRate.totalGrowthRate` | string | 总流量获得率增长率。 |
| `data.list[].trafficSummary.trafficAcquisitionRate.organicGrowthRate` | string | 自然流量获得率增长率。 |
| `data.list[].trafficSummary.trafficAcquisitionRate.advertisingGrowthRate` | string | 广告流量获得率增长率。 |
| `data.list[].asinInfo` | object | ASIN信息。 |
| `data.list[].asinInfo.country` | string | 商品所在国家。 |
| `data.list[].asinInfo.asin` | string | 商品ASIN。 |
| `data.list[].asinInfo.amazonUrl` | string | 商品在亚马逊上的URL。 |
| `data.list[].asinInfo.picUrl` | string | 商品图片的URL。 |
| `data.list[].asinInfo.currency` | string | 价格货币单位。 |
| `data.list[].asinInfo.price` | number | 商品价格。 |
| `data.list[].asinInfo.ratings` | integer | 用户评价数量。 |
| `data.list[].asinInfo.stars` | number | 商品星级评分。 |
| `data.list[].asinInfo.title` | string | 商品标题。 |
| `data.total` | integer | 总数。 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/xydc/get-keyword-analysis-monthly`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/xydc/get-keyword-analysis-monthly" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "usb c cable", "country": "US", "start_month": "2026-05", "end_month": "2026-06", "page": 1, "page_size": 20}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs#xydc-get_keyword_analysis_monthly（2026-07-07 访问）。

# Wenmai JIIMORE jiimore_get_niche_details API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/niche-details`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`jiimore_get_niche_details`
- **脚本入口**：`scripts/jiimore_get_niche_details.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 极目业务请求对象。 |
| `request.countryCode` | string | 否 | 两位 Amazon 市场国家码，例如 US、JP、DE；省略时使用服务端默认市场。 |
| `request.nicheId` | string | 是 | Amazon 细分市场标识，非空且最多 128 字符。 |

## 请求示例

```json
{
  "request": {
    "nicheId": "sample-niche",
    "countryCode": "US"
  }
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`；下表描述文档所列业务数据字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `countryCode` | string | 实际市场国家码。 |
| `nicheId` | string | 细分市场 ID。 |
| `baseInfo` | object | 细分市场基础信息。 |
| `baseInfo.nicheId` | string | 细分市场 ID。 |
| `baseInfo.nicheTitle` | string | 细分市场名称。 |
| `baseInfo.translationZh` | string | 中文翻译。 |
| `baseInfo.referenceAsinImageUrl` | string | 参考 ASIN 图片 URL。 |
| `baseInfo.demand` | number | 市场需求。 |
| `baseInfo.avgPrice` | number | 平均价格。 |
| `baseInfo.minimumPrice` | number | 最低价格。 |
| `baseInfo.maximumPrice` | number | 最高价格。 |
| `baseInfo.productCount` | integer | 商品数量。 |
| `baseInfo.brandCount` | integer | 品牌数量。 |
| `baseInfo.searchVolume7d` | integer | 7 日搜索量。 |
| `baseInfo.searchVolume90d` | integer | 90 日搜索量。 |
| `baseInfo.searchVolume180d` | integer | 180 日搜索量。 |
| `baseInfo.searchVolume360d` | integer | 360 日搜索量。 |
| `baseInfo.unitsSold7d` | integer | 7 日销量。 |
| `baseInfo.unitsSold90d` | integer | 90 日销量。 |
| `baseInfo.unitsSold180d` | integer | 180 日销量。 |
| `baseInfo.unitsSold360d` | integer | 360 日销量。 |
| `baseInfo.clickCount7d` | integer | 7 日点击量。 |
| `baseInfo.clickCount90d` | integer | 90 日点击量。 |
| `baseInfo.clickCount180d` | integer | 180 日点击量。 |
| `baseInfo.clickCount360d` | integer | 360 日点击量。 |
| `baseInfo.searchConversionRate7d` | number | 7 日搜索转化率。 |
| `baseInfo.clickConversionRate7d` | number | 7 日点击转化率。 |
| `baseInfo.top5ProductsClickShare` | number | Top 5 商品点击份额。 |
| `baseInfo.top20ProductsClickShare` | number | Top 20 商品点击份额。 |
| `baseInfo.top5BrandsClickShare` | number | Top 5 品牌点击份额。 |
| `baseInfo.top20BrandsClickShare` | number | Top 20 品牌点击份额。 |
| `baseInfo.sponsoredProductsPercentage` | number | 广告商品占比。 |
| `baseInfo.launchRate180d` | number | 180 日新品成功率。 |
| `baseInfo.launchRate360d` | number | 360 日新品成功率。 |
| `baseInfo.returnRate360d` | number | 360 日退货率。 |
| `baseInfo.cpc` | object | CPC 估算。 |
| `baseInfo.cpc.low` | number | 低位 CPC。 |
| `baseInfo.cpc.medium` | number | 中位 CPC。 |
| `baseInfo.cpc.high` | number | 高位 CPC。 |
| `baseInfo.trend` | array<object> | 趋势序列；摘要接口可能为空。 |
| `baseInfo.trend[].day` | integer | 日期，格式 yyyyMMdd。 |
| `baseInfo.trend[].searchVolume7d` | integer | 该时间点的 7 日搜索量。 |
| `baseInfo.trend[].unitsSold7d` | integer | 该时间点的 7 日销量。 |
| `baseInfo.trend[].searchConversionRate7d` | number | 该时间点的 7 日搜索转化率。 |
| `baseInfo.marketplaceId` | string | Amazon marketplace ID。 |
| `potentialSignals` | array<object> | 市场潜力指标。 |
| `potentialSignals[].key` | string | 指标键。 |
| `potentialSignals[].currentValue` | string | 当前值。 |
| `potentialSignals[].qoq` | string | 环比值，条件字段。 |
| `potentialSignals[].yoy` | string | 同比值，条件字段。 |
| `positiveReviewInsights` | array<object> | 正面评论洞察。 |
| `positiveReviewInsights[].topic` | string | 主题。 |
| `positiveReviewInsights[].percentOfMentions` | number | 提及占比。 |
| `positiveReviewInsights[].verbatims` | array<string> | 支撑该主题的原始评论短句。 |
| `negativeReviewInsights` | array<object> | 负面评论洞察。 |
| `negativeReviewInsights[].topic` | string | 主题。 |
| `negativeReviewInsights[].percentOfMentions` | number | 提及占比。 |
| `negativeReviewInsights[].verbatims` | array<string> | 支撑该主题的原始评论短句。 |

## 使用要点

- 保持 `request` 包装层，不要把内部字段提升到顶层。
- ASIN、关键词列表及分页范围遵循上表限制；不要静默截断用户输入。
- 返回 `warnings` 时，在结果摘要中明确保留截断、部分失败或完整性警告。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 设置 `WENMAI_API_KEY`，不要把 key 写入 Skill、日志或对话。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 检查必填字段、数组数量、ASIN 格式、分页范围和国家码。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/niche-details" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"nicheId": "sample-niche", "countryCode": "US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（访问日期：2026-07-14）。

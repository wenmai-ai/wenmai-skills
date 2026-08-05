# Wenmai JIIMORE jiimore_find_niches_by_keyword API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/niches-by-keyword`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`jiimore_find_niches_by_keyword`
- **脚本入口**：`scripts/jiimore_find_niches_by_keyword.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 极目业务请求对象。 |
| `request.countryCode` | string | 否 | 两位 Amazon 市场国家码，例如 US、JP、DE；省略时使用服务端默认市场。 |
| `request.keyword` | string | 是 | 搜索关键词或短语，去除首尾空格后长度为 1～200。 |
| `request.page` | integer | 否 | 页码，从 1 开始，默认 1。 |
| `request.pageSize` | integer | 否 | 每页数量，范围 1～50，默认 20。 |

## 请求示例

```json
{
  "request": {
    "keyword": "neck fan",
    "countryCode": "US"
  }
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`；下表描述文档所列业务数据字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `countryCode` | string | 实际市场国家码。 |
| `page` | integer | 当前页。 |
| `pageSize` | integer | 每页数量。 |
| `totalRows` | integer | 总记录数。 |
| `totalPages` | integer | 总页数。 |
| `items` | array<object> | 业务数据列表。 |
| `items[].nicheId` | string | 细分市场 ID。 |
| `items[].nicheTitle` | string | 细分市场名称。 |
| `items[].translationZh` | string | 中文翻译。 |
| `items[].referenceAsinImageUrl` | string | 参考 ASIN 图片 URL。 |
| `items[].demand` | number | 市场需求。 |
| `items[].avgPrice` | number | 平均价格。 |
| `items[].minimumPrice` | number | 最低价格。 |
| `items[].maximumPrice` | number | 最高价格。 |
| `items[].productCount` | integer | 商品数量。 |
| `items[].brandCount` | integer | 品牌数量。 |
| `items[].searchVolume7d` | integer | 7 日搜索量。 |
| `items[].searchVolume90d` | integer | 90 日搜索量。 |
| `items[].searchVolume180d` | integer | 180 日搜索量。 |
| `items[].searchVolume360d` | integer | 360 日搜索量。 |
| `items[].unitsSold7d` | integer | 7 日销量。 |
| `items[].unitsSold90d` | integer | 90 日销量。 |
| `items[].unitsSold180d` | integer | 180 日销量。 |
| `items[].unitsSold360d` | integer | 360 日销量。 |
| `items[].clickCount7d` | integer | 7 日点击量。 |
| `items[].clickCount90d` | integer | 90 日点击量。 |
| `items[].clickCount180d` | integer | 180 日点击量。 |
| `items[].clickCount360d` | integer | 360 日点击量。 |
| `items[].searchConversionRate7d` | number | 7 日搜索转化率。 |
| `items[].clickConversionRate7d` | number | 7 日点击转化率。 |
| `items[].top5ProductsClickShare` | number | Top 5 商品点击份额。 |
| `items[].top20ProductsClickShare` | number | Top 20 商品点击份额。 |
| `items[].top5BrandsClickShare` | number | Top 5 品牌点击份额。 |
| `items[].top20BrandsClickShare` | number | Top 20 品牌点击份额。 |
| `items[].sponsoredProductsPercentage` | number | 广告商品占比。 |
| `items[].launchRate180d` | number | 180 日新品成功率。 |
| `items[].launchRate360d` | number | 360 日新品成功率。 |
| `items[].returnRate360d` | number | 360 日退货率。 |
| `items[].cpc` | object | CPC 估算。 |
| `items[].cpc.low` | number | 低位 CPC。 |
| `items[].cpc.medium` | number | 中位 CPC。 |
| `items[].cpc.high` | number | 高位 CPC。 |
| `items[].trend` | array<object> | 趋势序列；摘要接口可能为空。 |
| `items[].trend[].day` | integer | 日期，格式 yyyyMMdd。 |
| `items[].trend[].searchVolume7d` | integer | 该时间点的 7 日搜索量。 |
| `items[].trend[].unitsSold7d` | integer | 该时间点的 7 日销量。 |
| `items[].trend[].searchConversionRate7d` | number | 该时间点的 7 日搜索转化率。 |
| `returnedRows` | integer | 本次实际返回记录数。 |
| `warnings` | array<string> | 截断、部分失败或数据完整性警告；正常时为空数组。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/niches-by-keyword" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"keyword": "neck fan", "countryCode": "US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（访问日期：2026-07-14）。

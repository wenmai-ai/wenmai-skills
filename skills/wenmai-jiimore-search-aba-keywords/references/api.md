# Wenmai JIIMORE jiimore_search_aba_keywords API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/aba-keywords`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`jiimore_search_aba_keywords`
- **脚本入口**：`scripts/jiimore_search_aba_keywords.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 极目业务请求对象。 |
| `request.asins` | array<string> | 是 | ASIN 列表，1～20 个；服务端会去除首尾空格、转为大写并去重。 |
| `request.countryCode` | string | 否 | 两位 Amazon 市场国家码，例如 US、JP、DE；省略时使用服务端默认市场。 |
| `request.page` | integer | 否 | 页码，从 1 开始，默认 1。 |
| `request.pageSize` | integer | 否 | 每页数量，范围 1～50，默认 20。 |

## 请求示例

```json
{
  "request": {
    "asins": [
      "B09PCSR9SX"
    ],
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
| `items[].searchTerm` | string | 搜索词。 |
| `items[].translationZh` | string | 中文翻译。 |
| `items[].searchVolume7d` | integer | 7 日搜索量。 |
| `items[].clickCount7d` | integer | 7 日点击量。 |
| `items[].unitsSold7d` | integer | 7 日销量。 |
| `items[].searchConversionRate7d` | number | 7 日搜索转化率。 |
| `items[].clickConversionRate7d` | number | 7 日点击转化率。 |
| `items[].cpc` | object | CPC 估算。 |
| `items[].cpc.low` | number | 低位 CPC。 |
| `items[].cpc.medium` | number | 中位 CPC。 |
| `items[].cpc.high` | number | 高位 CPC。 |
| `items[].cpr` | integer | CPR 指标。 |
| `items[].abaRank` | integer | 当前 ABA 排名。 |
| `items[].previousAbaRank` | integer | 上期 ABA 排名。 |
| `items[].abaRankChange` | integer | ABA 排名变化。 |
| `items[].searchVolumeGrowth7d` | number | 7 日搜索量增长率。 |
| `items[].impressionClickRate` | number | 展现点击率。 |
| `items[].top3AsinClickShare` | number | Top 3 ASIN 点击份额。 |
| `items[].top3AsinConversionShare` | number | Top 3 ASIN 转化份额。 |
| `items[].nicheId` | string | 关联细分市场 ID。 |
| `items[].nicheTitle` | string | 关联细分市场名称。 |
| `items[].relationGrade` | integer | 相关度等级，ABA 接口返回。 |
| `items[].relationGradeLabel` | string | 相关度等级文案。 |
| `items[].competeLevel` | integer | 竞争等级。 |
| `items[].competeLevelLabel` | string | 竞争等级文案。 |
| `items[].topAsins` | array<string> | Top ASIN 列表。 |
| `items[].asinInCount` | integer | 命中 ASIN 数量。 |
| `items[].productCount` | integer | 商品数量。 |
| `items[].top50ProductCount` | integer | Top 50 商品数量。 |
| `items[].avgPrice` | number | 平均价格。 |
| `items[].acos` | number | 广告销售成本比估算。 |
| `items[].cpa` | number | 单次转化成本估算。 |
| `items[].advertisingCost` | number | 广告费用估算。 |
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/aba-keywords" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"asins": ["B09PCSR9SX"], "countryCode": "US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（访问日期：2026-07-14）。

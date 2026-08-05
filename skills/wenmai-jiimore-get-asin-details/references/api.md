# Wenmai JIIMORE jiimore_get_asin_details API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/asin-details`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`jiimore_get_asin_details`
- **脚本入口**：`scripts/jiimore_get_asin_details.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 极目业务请求对象。 |
| `request.asins` | array<string> | 是 | ASIN 列表，1～20 个；服务端会去除首尾空格、转为大写并去重。 |
| `request.countryCode` | string | 否 | 两位 Amazon 市场国家码，例如 US、JP、DE；省略时使用服务端默认市场。 |

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
| `resolvedAsins` | array<string> | 成功规范化并解析的 ASIN。 |
| `dataCompleteness` | string | 整体数据完整性。 |
| `items` | array<object> | ASIN 详情列表。 |
| `items[].asin` | string | 商品 ASIN。 |
| `items[].title` | string | 商品标题。 |
| `items[].imageUrl` | string | 商品图片 URL。 |
| `items[].currentPrice` | number | 标准化当前价格。 |
| `items[].priceCurrency` | string | 价格币种，例如 USD。 |
| `items[].fbaFee360d` | number | 360 日口径 FBA 费用。 |
| `items[].referralFee360d` | number | 360 日口径推荐费。 |
| `items[].clickCount7d` | integer | 7 日点击量。 |
| `items[].clickCount30d` | integer | 30 日点击量。 |
| `items[].purchasedClicks360d` | integer | 360 日购买点击量。 |
| `items[].clickConversionRate` | number | 点击转化率。 |
| `items[].compositeClickConversionRate` | number | 综合点击转化率。 |
| `items[].conversionRateBasis` | string | 转化率时间口径。 |
| `items[].highlights` | array<string> | Amazon bullet-point 摘要。 |
| `items[].bestSellerRanks` | array<object> | Best Seller Rank 列表。 |
| `items[].bestSellerRanks[].category` | string | 分类名称。 |
| `items[].bestSellerRanks[].rank` | integer | 分类排名。 |
| `items[].dataCompleteness` | string | 单 ASIN 数据完整性。 |
| `warnings` | array<string> | 未解析 ASIN 或数据完整性警告，存在时返回。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/asin-details" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"asins": ["B09PCSR9SX"], "countryCode": "US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（访问日期：2026-07-14）。

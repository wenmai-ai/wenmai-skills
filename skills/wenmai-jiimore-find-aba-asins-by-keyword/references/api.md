# Wenmai JIIMORE jiimore_find_aba_asins_by_keyword API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/aba-asins-by-keyword`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`jiimore_find_aba_asins_by_keyword`
- **脚本入口**：`scripts/jiimore_find_aba_asins_by_keyword.py`
- **凭据与充值**：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`，额度不足时在同一入口充值

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 极目业务请求对象。 |
| `request.countryCode` | string | 否 | 两位 Amazon 市场国家码，例如 US、JP、DE；省略时使用服务端默认市场。 |
| `request.keywords` | array<string> | 是 | 关键词列表，1～20 个，每个最多 200 字符；服务端会去除首尾空格并去重。 |
| `request.page` | integer | 否 | 页码，从 1 开始，默认 1。 |
| `request.pageSize` | integer | 否 | 每页数量，范围 1～50，默认 20。 |

## 请求示例

```json
{
  "request": {
    "keywords": [
      "neck fan"
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
| `items[].asin` | string | 商品 ASIN。 |
| `items[].parentAsin` | string | 父 ASIN，可能为空。 |
| `items[].title` | string | 商品标题。 |
| `items[].imageUrl` | string | 商品图片 URL。 |
| `items[].brand` | string | 品牌。 |
| `items[].currentPrice` | number | 当前价格；可能不完整。 |
| `items[].customerRating` | number | 商品评分。 |
| `items[].totalReviews` | integer | 评论数量。 |
| `items[].clickCount7d` | integer | 7 日点击量。 |
| `items[].clickCount30d` | integer | 30 日点击量。 |
| `items[].purchasedClicks360d` | integer | 360 日购买点击量。 |
| `items[].clickConversionRate` | number | 点击转化率。 |
| `items[].sellerName` | string | 卖家展示名称，条件字段。 |
| `items[].sellerId` | string | 卖家 ID，条件字段，可能为空。 |
| `items[].similarityScore` | number | ABA 相似度，条件字段。 |
| `items[].relationGrade` | string | 相关等级编码，条件字段。 |
| `items[].relationGradeLabel` | string | 相关等级文案，条件字段。 |
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/jiimore/aba-asins-by-keyword" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"keywords": ["neck fan"], "countryCode": "US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（访问日期：2026-07-14）。

# Wenmai SellerSprite `market_seller_concentration` API 参考

用于分析指定 Amazon 市场类目节点下的卖家集中度情况。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/market-seller-concentration`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`market_seller_concentration`
- **脚本入口**：`scripts/market_seller_concentration.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 业务请求对象。 |
| `request.marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `request.month` | string | 否 | 筛选日期，默认最近30天，格式 yyyyMM |
| `request.topN` | integer | 否 | 头部Listing数量；示例：10。 |
| `request.newProduct` | integer | 否 | 新品定义；示例：6。 |
| `request.nodeIdPath` | string | 是 | 节点 id 路径字符串；示例：1064954:1069242:1069784:1069820:1069838:1069828。 |

## 请求示例

```json
{
  "request": {
    "nodeIdPath": "172282:281407",
    "marketplace": "US"
  }
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `name` | string | 卖家名称；JA Wholesale LLC |
| `ranking` | integer | 排名；官方示例值：1。 |
| `asinSet` | array | 包含的商品ASIN集合；["B00P19MFYE"] |
| `products` | integer | 商品数量，包含新品；官方示例值：4。 |
| `newProducts` | integer | 新品数量；官方示例值：1。 |
| `newUnits` | integer | 新品销量；官方示例值：45。 |
| `newRevenue` | number | 新品销售额；官方示例值：2342。 |
| `newUnitsRatio` | number | 新品销量占比；官方示例值：4.3。 |
| `newRevenueRatio` | number | 新品销售额占比；官方示例值：4。 |
| `avgPrice` | number | 平均价格；官方示例值：6.19。 |
| `ratings` | integer | 评分数；官方示例值：5695。 |
| `rating` | number | 评分值；官方示例值：4.8。 |
| `reviews` | integer | 评论数；官方示例值：234。 |
| `totalUnits` | integer | 总销量；官方示例值：32342。 |
| `totalRevenue` | number | 总销额；官方示例值：18837.35。 |
| `totalUnitsRatio` | number | 总销量占比；官方示例值：0.4478。 |
| `totalRevenueRatio` | number | 总销额占比；官方示例值：0.3052。 |

## 使用要点

- 必填字段：`request`, `request.marketplace`, `request.nodeIdPath`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/market-seller-concentration" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request":{"nodeIdPath":"172282:281407","marketplace":"US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

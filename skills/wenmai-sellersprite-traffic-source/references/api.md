# Wenmai SellerSprite traffic source API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-source`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 在 https://agent.wenmai-ai.com/app/account 的个人中心获取，充值也在同一入口完成。
- **接口编码**：`traffic_source`
- **脚本入口**：`scripts/traffic_source.py`，脚本参数即标准 API POST Body JSON

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
| `request` | object | 是 | 业务请求对象。 |
| `request.marketplace` | string | 是 | 站点编码。可选值：`US`、`JP`、`UK`、`DE`、`FR`、`IT`、`ES`、`CA`、`IN`。 |
| `request.q` | string | 是 | asin 或者 关键词；B07Z82895W |
| `request.month` | string | 是 | 筛选日期,yyyyMM格式；202203 |
| `request.page` | integer | 否 | 页码，从 1 开始；默认：1 |
| `request.size` | integer | 否 | 每页条数；默认：50最大： 100 |
| `request.order` | object | 否 | 排序 |
| `request.order.field` | string | 否 | 排序字段 |
| `request.order.desc` | boolean | 否 | true为降序 false为升序；默认降序 |

## 请求示例

```json
{
  "request": {
    "marketplace": "US",
    "q": "B08GHW4TBS",
    "month": "202203"
  }
}
```


## 响应结构

公共响应字段：`code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `guestId` | string | 访客 ID。 |
| `pages` | integer | 总页数。 |
| `page` | integer | 当前页码。 |
| `size` | integer | 每页数量。 |
| `total` | integer | 总数量。 |
| `took` | integer | 请求耗时。 |
| `url` | string | 链接地址。 |
| `order` | object | 排序对象。 |
| `order.field` | string | 排序字段。 |
| `order.desc` | boolean | 是否降序。 |
| `items[]` | array | 列表数据。 |
| `items[].keywords` | string | 关键词数量。 |
| `items[].searchKeywords` | string | 搜索关键词。 |
| `items[].acKeywords` | string | 自然流量关键词数量。 |
| `items[].editorialKeywords` | string | 关键词。 |
| `items[].fourStarsKeywords` | string | 关键词。 |
| `items[].hrKeywords` | string | 关键词。 |
| `items[].adKeywords` | string | 广告流量关键词数量。 |
| `items[].videoKeywords` | string | 关键词。 |
| `items[].brandKeywords` | string | 品牌关键词。 |
| `items[].badgeDetails` | object | badgeDetails。 |
| `items[].badgeDetails.OFFICIAL[]` | array | OFFICIAL列表。 |
| `items[].badgeDetails.SEARCH[]` | array | 搜索列表。 |
| `items[].badgeLabels[]` | array | badgeLabels列表。 |
| `items[].asinInfo` | object | ASIN。 |
| `items[].asinInfo.asin` | object | ASIN。 |
| `items[].asinInfo.asinUrl` | object | ASIN 商品链接。 |
| `items[].asinInfo.currency` | object | 币种。 |
| `items[].asinInfo.price` | number | 价格。 |
| `items[].asinInfo.rating` | object | 评分。 |
| `items[].asinInfo.reviews` | integer | 评论数量。 |
| `items[].asinInfo.sku` | object | SKU。 |
| `items[].asinInfo.title` | object | 标题。 |
| `items[].asinInfo.variations` | integer | 变体数量。 |
| `items[].asinInfo.category1Id` | object | category1Id。 |
| `items[].asinInfo.category1Name` | object | category1Name。 |
| `items[].asinInfo.nodeId` | object | 类目节点 ID。 |
| `items[].asinInfo.nodeIdPath` | object | 类目节点路径。 |
| `items[].asinInfo.nodeLabelPath` | object | 类目名称路径。 |
| `items[].asinInfo.bsrRank` | integer | BSR 排名。 |
| `items[].asinInfo.bsrId` | object | BSR 类目 ID。 |
| `items[].asinInfo.bsrLabel` | object | BSR 类目名称。 |
| `items[].badgeDetails.AD[]` | array | 广告列表。 |
| `terminal` | string | 终端类型。 |
| `hasNextPage` | integer | 是否还有下一页。 |
| `guestVisited` | boolean | 访客是否访问过。 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/sellersprite/traffic-source`。
- 成功响应位于 `data`；失败时优先读取 `code`、`message`、`requestId` 和 HTTP 状态。
- 保留用户给出的筛选、分页、排序、日期和站点参数，不要擅自扩大查询范围。
- 长数组结果先汇总关键行，再按用户需要继续展开。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 到 https://agent.wenmai-ai.com/app/account 的个人中心获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 到 https://agent.wenmai-ai.com/app/account 的个人中心充值后重试。 |
| 参数错误 | 按请求参数表修正必填字段、枚举值、日期格式、分页范围。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-source" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"marketplace": "US", "q": "B08GHW4TBS", "month": "202203"}}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（2026-07-23 访问）。

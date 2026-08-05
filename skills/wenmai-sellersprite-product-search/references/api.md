# Wenmai 卖家精灵商品搜索 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/product-research`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 在 https://agent.wenmai-ai.com/app/account 的个人中心获取，充值也在同一入口完成。
- **接口编码**：`product_research`
- **脚本入口**：`scripts/sellersprite_product_search.py`，脚本参数即标准 API POST Body JSON

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
| `request.marketplace` | string | 是 | 站点编码。可选值：`US`、`JP`、`UK`、`DE`、`FR`、`IT`、`ES`、`CA`、`IN`。 |
| `request.month` | string | 否 | 查询月份，格式 `yyyyMM`，示例 `202507`。 |
| `request.keyword` | string | 否 | 搜索关键词。 |
| `request.brand` | string | 否 | 品牌，示例 `WWDOLL`。 |
| `request.sellerName` | string | 否 | 卖家，示例 `Apple`。 |
| `request.asins` | array | 否 | ASIN 列表，最多 `40` 个。 |
| `request.nodeIdPath` | string | 否 | 类目节点字符串；示例见产品类目。 |
| `request.nodeIdPathEqual` | boolean | 否 | 类目查询方式；`true` 精确类目，`false` 当前及子类目；默认 `false`。 |
| `request.matchType` | integer | 否 | 关键词匹配方式；可选值：`1` 词组匹配、`2` 模糊匹配、`3` 精准匹配；默认 `2`。 |
| `request.variation` | string | 否 | 是否查询变体 ASIN；可选值：`N` 含变体、`Y` 不含变体。 |
| `request.page` | integer | 否 | 页码，默认 `1`。 |
| `request.size` | integer | 否 | 每页条数，默认 `50`，最大 `100`。 |
| `request.order.field` | string | 否 | 排序字段，默认 `total_units`。 |
| `request.order.desc` | boolean | 否 | 排序方式；`true` 降序，`false` 升序；默认 `true`。 |

## 请求示例

脚本入参示例：

```json
{
  "request": {
    "marketplace": "US",
    "keyword": "water bottle",
    "page": 1,
    "size": 50,
    "order": {
      "field": "total_units",
      "desc": true
    }
  }
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.items[]` | array | 商品列表。 |
| `items[].asin / title / brand` | string | ASIN、标题、品牌。 |
| `items[].units / revenue / price` | mixed | 销量、销售额、价格。 |
| `items[].bsr / rating / fulfillment` | mixed | BSR、评分、配送方式。 |


## 使用要点

- 当前映射到 Wenmai `competitor_lookup`，用于商品池筛选。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 到 https://agent.wenmai-ai.com/app/account 的个人中心获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 到 https://agent.wenmai-ai.com/app/account 的个人中心充值后重试。 |
| 参数错误 | 按上方请求参数表修正枚举值、日期格式、分页范围或必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/product-research" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"marketplace": "US", "keyword": "water bottle", "page": 1, "size": 50, "order": {"field": "total_units", "desc": true}}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（2026-07-23 访问）。

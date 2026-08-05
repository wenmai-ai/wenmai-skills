# Wenmai 卖家精灵市场研究 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/market-research`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 在 https://agent.wenmai-ai.com/app/account 的个人中心获取，充值也在同一入口完成。
- **接口编码**：`market_research`
- **脚本入口**：`scripts/sellersprite_market_research.py`，脚本参数即标准 API POST Body JSON

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
| `request.month` | string | 否 | 筛选月份，格式 `yyyyMM`；默认最近 `30` 天。 |
| `request.topNum` | integer | 否 | 头部 Listing 数量，示例 `10`。 |
| `request.newProduct` | integer | 否 | 新品定义窗口，默认 `3`。 |
| `request.nodeIdPath` | string | 否 | 类目节点路径，示例 `172282:281407`。 |
| `request.departmentKeyword` | string | 否 | 类目关键字路径，示例 `Electronics:Accessories & Supplies`。 |
| `request.minAvgUnits/request.maxAvgUnits` | integer | 否 | 月均销量范围，示例 `100` 到 `10000`。 |
| `request.minAvgRevenue/request.maxAvgRevenue` | number | 否 | 月均销售额范围，示例 `100` 到 `900`。 |
| `request.minAvgRating/request.maxAvgRating` | number | 否 | 平均星级范围，示例 `2.5` 到 `3`。 |
| `request.minAvgPrice/request.maxAvgPrice` | number | 否 | 平均价格范围，示例 `30` 到 `50`。 |
| `request.sellerLocation` | string | 否 | 卖家所属地，多值逗号分隔，示例 `US,GB`。 |
| `request.page` | integer | 否 | 页码，从 `1` 开始，默认 `1`。 |
| `request.size` | integer | 否 | 每页条数，默认 `50`，最大 `200`。 |
| `request.order.desc` | boolean | 否 | 排序方式；`true` 降序，`false` 升序；默认降序。 |

## 请求示例

脚本入参示例：

```json
{
  "request": {
    "marketplace": "US",
    "nodeIdPath": "172282:281407",
    "page": 1,
    "size": 50
  }
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.items[]` | array | 类目市场列表。 |
| `items[].totalProducts / totalUnits / totalRevenue` | mixed | 商品数、销量、销售额。 |
| `items[].avgPrice / avgRating / avgBsr` | mixed | 均价、平均评分、平均 BSR。 |
| `items[].brands / sellers` | mixed | 品牌数、卖家数。 |


## 使用要点

- 适合类目规模、集中度、新品机会和履约结构分析。

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/market-research" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"marketplace": "US", "nodeIdPath": "172282:281407", "page": 1, "size": 50}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（2026-07-23 访问）。

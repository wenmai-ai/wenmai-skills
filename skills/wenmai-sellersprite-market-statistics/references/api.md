# Wenmai 卖家精灵市场统计 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/market-research-statistics`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 在 https://agent.wenmai-ai.com/app/account 的个人中心获取，充值也在同一入口完成。
- **接口编码**：`market_research_statistics`
- **脚本入口**：`scripts/sellersprite_market_statistics.py`，脚本参数即标准 API POST Body JSON

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
| `request.nodeIdPath` | string | 是 | 节点 id 路径字符串，示例 `1064954:1069242:1069784:1069820:1069838:1069828`。 |
| `request.month` | string | 否 | 筛选月份，格式 `yyyyMM`；默认最近 `30` 天。 |
| `request.topN` | integer | 否 | 头部 Listing 数量，示例 `10`。 |
| `request.newProduct` | integer | 否 | 新品定义窗口，示例 `6`。 |

## 请求示例

脚本入参示例：

```json
{
  "request": {
    "marketplace": "US",
    "nodeIdPath": "172282:281407",
    "topN": 10,
    "newProduct": 6
  }
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.marketplace` | string | Amazon 站点。 |
| `data.nodeIdPath / nodeLabelPath` | string | 类目节点路径和名称路径。 |
| `data.totalProducts / totalUnits / totalRevenue` | mixed | 市场规模指标。 |
| `data.countryCode / currency` | string | 国家/站点代码和币种。 |


## 使用要点

- 这是节点级统计，`nodeIdPath` 必填。

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/market-research-statistics" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"marketplace": "US", "nodeIdPath": "172282:281407", "topN": 10}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（2026-07-23 访问）。

# Wenmai 卖家精灵流量关键词 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-keyword`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 在 https://agent.wenmai-ai.com/app/account 的个人中心获取，充值也在同一入口完成。
- **接口编码**：`traffic_keyword`
- **脚本入口**：`scripts/sellersprite_traffic_keyword.py`，脚本参数即标准 API POST Body JSON

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
| `request.asin` | string | 是 | ASIN，示例 `B07Z82895W`。 |
| `request.keyword` | string | 否 | 关键词筛选，示例 `phone stand`。 |
| `request.month` | string | 否 | 历史月份，格式 `yyyyMM`；不传默认最近 `30` 天，示例 `202308`。 |
| `request.badges` | array | 否 | 流量词类型；WMAPI 文档未给固定枚举，按线上 tool schema 支持值传。 |
| `request.trafficKeywordTypes` | array | 否 | 流量占比类型；WMAPI 文档未给固定枚举，按线上 tool schema 支持值传。 |
| `request.conversionKeywordTypes` | array | 否 | 流量转化类型；WMAPI 文档未给固定枚举，按线上 tool schema 支持值传。 |
| `request.page` | integer | 否 | 当前页，默认 `1`。 |
| `request.size` | integer | 否 | 每页条数，默认 `50`，最大 `100`，最多查询 `2000` 条数据。 |
| `request.order.field` | string | 否 | 排序字段，默认 `rankPosition`。 |
| `request.order.desc` | boolean | 否 | 是否倒序；可选值：`true`、`false`；默认 `false`。 |

## 请求示例

脚本入参示例：

```json
{
  "request": {
    "marketplace": "US",
    "asin": "B08GHW4TBS",
    "page": 1,
    "size": 50,
    "order": {
      "field": "rankPosition",
      "desc": false
    }
  }
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.total` | integer | 总数量。 |
| `data.items[]` | array | 流量关键词列表。 |
| `items[].keyword / keywordCn` | string | 关键词和中文翻译。 |
| `items[].searches / products / rankPosition` | mixed | 搜索量、商品数、自然排名。 |


## 使用要点

- 用于指定 ASIN 的流量词反查。

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-keyword" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"marketplace": "US", "asin": "B08GHW4TBS", "page": 1, "size": 50}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（2026-07-23 访问）。

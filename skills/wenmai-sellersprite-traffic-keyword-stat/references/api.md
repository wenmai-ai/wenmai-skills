# Wenmai SellerSprite traffic keyword stat API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-keyword-stat`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 在 https://agent.wenmai-ai.com/app/account 的个人中心获取，充值也在同一入口完成。
- **接口编码**：`traffic_keyword_stat`
- **脚本入口**：`scripts/traffic_keyword_stat.py`，脚本参数即标准 API POST Body JSON

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
| `marketplace` | string | 是 | 站点编码。可选值：`US`、`JP`、`UK`、`DE`、`FR`、`IT`、`ES`、`CA`、`IN`、`MX`、`BR`、`AU`、`AE`。 |
| `asin` | string | 是 | asin；B07Z82895W |
| `month` | string | 否 | 查询月份；202605 |

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B08GHW4TBS"
}
```


## 响应结构

公共响应字段：`code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `marketplace` | string | Amazon 站点。 |
| `asin` | string | ASIN。 |
| `keywords` | string | 关键词总数。 |
| `ranks` | string | 自然排名关键词数量。 |
| `ads` | string | 广告流量词数量。 |
| `badgeCount` | integer | 商品标签数量。 |
| `calcTime` | string | 数据计算时间。 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/sellersprite/traffic-keyword-stat`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-keyword-stat" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"marketplace": "US", "asin": "B08GHW4TBS"}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（2026-07-23 访问）。

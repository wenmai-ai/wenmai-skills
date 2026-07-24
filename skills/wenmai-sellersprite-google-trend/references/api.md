# Wenmai SellerSprite google trend API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/google-trend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`google_trend`
- **脚本入口**：`scripts/google_trend.py`，脚本参数即标准 API POST Body JSON

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
| `request.marketplace` | string | 是 | 站点编码，例如 US |
| `request.keyword` | string | 否 | 关键字；iphone stand |
| `request.googleProp` | string | 否 | 类别；web:google网页搜索shoppingCart:google购物搜索 |
| `request.monthly` | boolean | 否 | 按照月份；false（默认值） |

## 请求示例

```json
{
  "request": {
    "marketplace": "US"
  }
}
```


## 响应结构

公共响应字段：`code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `marketplace` | string | 市场；US |
| `keyword` | string | 关键字；phone stand |
| `link` | string | google trend链接 |
| `items` | array | 明细 |
| `items[].time` | integer | 时间戳；1555804800000 |
| `items[].value` | integer | 值；2 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/sellersprite/google-trend`。
- 成功响应位于 `data`；失败时优先读取 `code`、`message`、`requestId` 和 HTTP 状态。
- 保留用户给出的筛选、分页、排序、日期和站点参数，不要擅自扩大查询范围。
- 长数组结果先汇总关键行，再按用户需要继续展开。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按请求参数表修正必填字段、枚举值、日期格式、分页范围。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/google-trend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"marketplace": "US"}}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。

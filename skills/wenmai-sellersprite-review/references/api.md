# Wenmai SellerSprite review API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/review`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 在 https://agent.wenmai-ai.com/app/account 的个人中心获取，充值也在同一入口完成。
- **接口编码**：`review`
- **脚本入口**：`scripts/review.py`，脚本参数即标准 API POST Body JSON

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
| `asin` | string | 是 | ASIN |
| `starList` | array | 否 | 评论星级；1: 一星, 2: 二星, 3: 三星, 4: 四星, 5: 五星 |
| `typeList` | array | 否 | 评论类型；1：图片评论, 2：视频评论, 3：VP评论, 4：vine评论 |
| `page` | integer | 否 | 页码，从 1 开始；默认：1 |
| `size` | integer | 否 | 每页条数，最大10；默认：5 |

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
| `items[].author` | string | 评论作者。 |
| `items[].title` | string | 标题。 |
| `items[].content` | string | 内容。 |
| `items[].date` | string | 日期。 |
| `items[].star` | string | 星级。 |
| `items[].authorLabels[]` | array | 评论作者标签列表。 |
| `items[].skus[]` | array | SKU 列表。 |
| `items[].images` | string | 图片列表。 |
| `items[].videos` | string | 视频列表。 |
| `items[].likes` | string | likes。 |
| `items[].image` | string | 图片地址。 |
| `items[].video` | string | 是否有视频。 |
| `items[].verified` | string | verified。 |
| `items[].vine` | string | vine。 |
| `items[].free` | string | free。 |
| `items[].experience` | string | experience。 |
| `terminal` | string | 终端类型。 |
| `hasNextPage` | integer | 是否还有下一页。 |
| `guestVisited` | boolean | 访客是否访问过。 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/sellersprite/review`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/review" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"marketplace": "US", "asin": "B08GHW4TBS"}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（2026-07-23 访问）。

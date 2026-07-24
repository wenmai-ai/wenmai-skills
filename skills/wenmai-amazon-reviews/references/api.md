# Wenmai Amazon Reviews 评论 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/carvenmaster/get-asin-reviews`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`get_asin_reviews`
- **脚本入口**：`scripts/amazon_reviews.py`，脚本参数即标准 API POST Body JSON

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
| `asin` | string | 是 | 商品 ASIN，示例 `B08N5WRWNW`。 |
| `country` | string | 是 | 站点国家代码；可选值：`US`、`DE`、`UK`、`AU`、`MX`、`CA`、`IN`、`EG`、`AE`。 |
| `filter_by_star` | string | 否 | 星级过滤；可选值：`all_stars`、`one_star`、`two_star`、`three_star`、`four_star`、`five_star`、`positive`、`critical`；默认可不传。 |
| `sort_by` | string | 否 | 排序方式；可选值：`recent` 最新、`helpful` 热门/有帮助；示例 `recent`。 |

## 请求示例

脚本入参示例：

```json
{
  "asin": "B08N5WRWNW",
  "country": "US",
  "sort_by": "recent",
  "filter_by_star": "all_stars"
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.reviews[] / data.content[]` | array | 评论列表或 API text content，按上游返回解析。 |
| `rating/title/content/comment_at` | mixed | 评分、标题、正文、评论时间。 |
| `verified_purchase / vine_voice` | boolean | 是否已验证购买、是否 Vine 评论。 |
| `helpful_count / total` | integer | 有用数量和总数。 |


## 使用要点

- 一次只查一个 ASIN。
- 做差评分析时优先使用 `critical` 或 `one_star`/`two_star`/`three_star`。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按上方请求参数表修正枚举值、日期格式、分页范围或必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/carvenmaster/get-asin-reviews" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B08N5WRWNW", "country": "US", "sort_by": "recent", "filter_by_star": "all_stars"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。

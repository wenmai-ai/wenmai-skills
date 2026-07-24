# Wenmai Keepa 商品历史 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/keepa/get-keepa-product-history`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`get_keepa_product_history`
- **脚本入口**：`scripts/keepa_product_history.py`，脚本参数即标准 API POST Body JSON

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
| `domain` | integer | 是 | 可选值：`1` 美国、`2` 英国、`3` 德国、`4` 法国、`5` 日本、`6` 加拿大、`8` 意大利、`9` 西班牙、`10` 印度、`11` 墨西哥、`12` 巴西；默认建议美国站用 `1`。 |
| `asin` | string | 是 | ASIN、ISBN 或商品编码；多个值用英文逗号分隔，最多 `100` 个。 |
| `code` | string | 否 | 商品编码；使用 code 类型查询时传入。 |
| `stats` | integer/string | 否 | 统计窗口；常用示例 `90`，也可传上游支持的日期范围。 |
| `offers` | integer | 否 | 返回报价数量；传入后返回 `products[].offers`。 |
| `history` | boolean | 否 | 是否返回历史序列 csv；可选值：`true`、`false`；默认返回。 |
| `rating` | boolean | 否 | 是否请求评分和评论历史；可选值：`true`、`false`。 |
| `buybox` | boolean | 否 | 是否请求 Buy Box 信息；可选值：`true`、`false`。 |
| `update` | integer | 否 | 数据新鲜度阈值，单位小时。 |
| `days` | integer | 否 | 限制最近 N 天历史；常用 `30`、`90`、`365`。 |
| `only-live-offers` | boolean | 否 | 仅返回当前有效报价；可选值：`true`、`false`。 |

## 请求示例

脚本入参示例：

```json
{
  "domain": 1,
  "asin": "B08GHW4TBS",
  "stats": 90,
  "history": true,
  "rating": true
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.products[]` | array | Keepa 商品历史对象。 |
| `products[].csv[]` | array | 历史序列数据。 |
| `products[].stats` | object | 价格、排名、Buy Box 等统计。 |
| `products[].monthlySoldHistory` | array | 月销量历史。 |
| `products[].buyBoxSellerIdHistory` | array | Buy Box 卖家历史。 |


## 使用要点

- BSR 数字越小排名越好。
- 长历史建议配合 `days` 或 `stats` 控制响应长度。

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/keepa/get-keepa-product-history" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": 1, "asin": "B08GHW4TBS", "stats": 90, "history": true, "rating": true}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。

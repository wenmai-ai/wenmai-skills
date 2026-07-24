# Wenmai Keepa 商品搜索 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/keepa/keepa-product-search`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`keepa_product_search`
- **脚本入口**：`scripts/keepa_product_search.py`，脚本参数即标准 API POST Body JSON

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
| `term` | string | 是 | 搜索词，示例 `water bottle`。 |
| `type` | string | 否 | 搜索类型；WMAPI 文档未定义固定可选值，按上游 Keepa 支持值传入，默认可不传。 |
| `page` | integer | 否 | 结果页码，从 `0` 开始；示例 `0`。 |
| `asins-only` | integer/boolean | 否 | 是否只返回 ASIN 列表；可选值：`true`/`false` 或上游接受的 `1`/`0`，默认可不传。 |

## 请求示例

脚本入参示例：

```json
{
  "term": "water bottle",
  "domain": 1,
  "page": 0
}
```


## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.products[]` | array | 搜索命中的商品对象。 |
| `products[].asin` | string | ASIN。 |
| `products[].title / brand` | string | 标题和品牌。 |
| `products[].domainId` | integer | Amazon domain id。 |


## 使用要点

- 搜索结果页码从 `0` 开始，不是从 1 开始。

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/keepa/keepa-product-search" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": 1, "term": "water bottle", "page": 0, "asins-only": 1}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。

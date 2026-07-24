# Wenmai Alpha Temu Products Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/temu-products-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_temu_products_scraper`
- **接口说明**：Temu Products Scraper
- **脚本入口**：`scripts/alpha_temu_products_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `searchQueries` | array | 是 | 搜索关键词列表。 |
| `currency` | string | 否 | 币种。可选值：USD、EUR、ILS、BRL。 |
| `maxResults` | integer | 否 | 最大采集或返回数量。 |

## 请求示例

脚本入参示例：

```json
{
  "currency": "USD",
  "maxResults": 40,
  "searchQueries": [
    "women dress"
  ]
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `thumb_url` | string | 缩略图链接。 |
| `title` | string | 商品标题。 |
| `price_info` | object | 价格信息。 |
| `price_info.price_str` | string | 商品价格。 |
| `price_info.market_price_str` | string | 市场价格。 |
| `comment` | object | 评论和评分信息。 |
| `comment.goods_score` | number | 商品评分。 |
| `sales_num` | string | 销量。 |
| `link_url` | string | 商品链接。 |
| `goods_id` | number | 商品 ID。 |

## 使用要点

- 本接口适合：Temu 商品池。
- 优先使用用户给定的 URL、关键词、商品 ID、站点、国家、语言、排序、分页和数量限制。
- 采集类接口的字段会随目标平台页面结构变化；输出分析时保留原始字段名和 URL，避免把缺失字段补写成事实。
- 当用户需要多平台对比时，分别调用对应 Alpha 原子 Skill，再在上层分析中合并结果。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按上方请求参数表修正枚举值、日期格式、分页范围、URL/关键词数组、数量范围或必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/temu-products-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"currency": "USD", "maxResults": 40, "searchQueries": ["women dress"]}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

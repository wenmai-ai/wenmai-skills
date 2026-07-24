# Wenmai Alpha Jumia Product Search Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/jumia-product-search-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_jumia_product_search_scraper`
- **接口说明**：Scraping search page in jumia.com.ng
- **脚本入口**：`scripts/alpha_jumia_product_search_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `urls` | array | 否 | 页面链接列表。 |
| `ignore_url_failures` | boolean | 否 | 页面链接列表。 |
| `max_items_per_url` | integer | 否 | 链接地址。 |

## 请求示例

脚本入参示例：

```json
{
  "urls": [
    "https://www.jumia.com.ng/catalog/?q=shoe&page=11#catalog-listing"
  ],
  "max_items_per_url": 3,
  "ignore_url_failures": true
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `categories` | array<string> | categories 字段。 |
| `simples` | array | simples 字段。 |
| `simples.is_buyable` | boolean | 是否启用该选项。 |
| `simples.prices` | object | 价格。 |
| `simples.prices.discount` | string | 数量。 |
| `simples.prices.discount_euro` | string | 数量。 |
| `simples.prices.old_price` | string | 价格。 |
| `simples.prices.old_price_euro` | string | 价格。 |
| `simples.prices.price` | string | 价格。 |
| `simples.prices.price_euro` | string | 价格。 |
| `simples.prices.raw_price` | string | 价格。 |
| `simples.prices.tax_euro` | string | tax_euro 字段。 |
| `simples.login_url` | string | 链接地址。 |
| `simples.name` | string | 名称。 |
| `simples.sku` | string | ID 标识。 |
| `is_buyable` | boolean | 是否启用该选项。 |
| `is_shop_express` | boolean | 是否启用该选项。 |
| `is_sponsored` | boolean | 是否启用该选项。 |
| `variation_selection` | boolean | variation_selection 字段。 |
| `selected_variation` | string | selected_variation 字段。 |
| `seller_id` | number | 卖家信息。 |
| `shop_express` | string | 店铺信息。 |
| `prices` | object | 价格。 |
| `prices.discount` | string | 数量。 |
| `prices.discount_euro` | string | 数量。 |
| `prices.old_price` | string | 价格。 |
| `prices.old_price_euro` | string | 价格。 |
| `prices.price` | string | 价格。 |
| `prices.price_euro` | string | 价格。 |
| `prices.raw_price` | string | 价格。 |
| `prices.tax_euro` | string | tax_euro 字段。 |
| `rating` | object | 评分。 |
| `rating.average` | number | average 字段。 |
| `rating.total_ratings` | number | 评分。 |
| `tracking` | object | tracking 字段。 |
| `tracking.is_second_chance` | boolean | 是否启用该选项。 |
| `tracking.brand_key` | string | 品牌。 |
| `tracking.category_key` | string | 分类。 |
| `tracking.name` | string | 名称。 |
| `wishlist` | object | wishlist 字段。 |
| `wishlist.added` | boolean | added 字段。 |
| `wishlist.remove_url` | string | 链接地址。 |
| `brand` | string | 品牌。 |
| `display_name` | string | 名称。 |
| `from_url` | string | 链接地址。 |
| `image` | string | 图片链接。 |
| `image_alt` | string | image_alt 字段。 |
| `name` | string | 名称。 |
| `sku` | string | ID 标识。 |
| `tags` | string | tags 字段。 |
| `url` | string | 链接地址。 |

## 使用要点

- 本接口适合：Jumia 非洲电商商品。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/jumia-product-search-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://www.jumia.com.ng/catalog/?q=shoe&page=11#catalog-listing"], "max_items_per_url": 3, "ignore_url_failures": true}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

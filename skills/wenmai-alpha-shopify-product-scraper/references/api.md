# Wenmai Alpha Shopify Product Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/shopify-product-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_shopify_product_scraper`
- **接口说明**：Shopify Scraper - Extract Products, Prices, Reviews & Variants
- **脚本入口**：`scripts/alpha_shopify_product_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `mode` | string | 否 | 采集模式。可选值：url、discovery。 |
| `category` | string | 否 | 分类。可选值：fashion、fashion/shoes、fashion/jewellery、fashion/bags、fashion/lingerie、fashion/outerwear、fashion/swimwear、fashion/activewear、fashion/kids、beauty、skincare、skincare/serum、skincare/mask、skincare/cleanser、skincare/sunscreen、skincare/acne、skincare/toner、skincare/exfoliant、haircare、haircare/shampoo、haircare/conditioner、haircare/styling、haircare/tools、food、food/snack、food/candy、food/bakery、food/meat、food/seafood、food/vegan、food/organic、food/glutenfree、food/coffee、food/tea、food/alcohol、electronics、electronics/phone、electronics/computer、electronics/camera、electronics/audio、electronics/wearable、home、home/furniture、home/lighting、home/decor、home/storage、kitchen、kitchen/appliance、kitchen/cookware、kitchen/utensil、kitchen/storage、kitchen/tableware、kitchen/drinkware、sports、sports/equipment、sports/clothing、pets、pets/food、pets/accessory、pets/health、baby、baby/clothing、baby/gear、baby/feeding、baby/toys、bedding、bedding/blanket、bedding/sleepwear、bedding/mattress、bedding/pillow、bedding/duvet、bathroom、bathroom/accessory、bath-body、bath-body/oil、bath-body/lotion、bath-body/scrub、dental、dental/toothbrush、dental/toothpaste、等。 |
| `maxStores` | integer | 否 | 最大采集或返回数量。 |
| `maxPages` | integer | 否 | 最大采集或返回数量。 |
| `storeUrls` | array | 否 | 页面链接列表。 |
| `maxProducts` | integer | 否 | 最大采集或返回数量。 |

## 请求示例

脚本入参示例：

```json
{
  "mode": "url",
  "maxPages": 1,
  "storeUrls": [
    {
      "url": "https://www.allbirds.com"
    }
  ],
  "maxProducts": 20
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `store` | string | 店铺信息。 |
| `product_id` | integer | ID 标识。 |
| `product_url` | string | 链接地址。 |
| `handle` | string | handle 字段。 |
| `title` | string | 标题。 |
| `description` | string | 描述。 |
| `vendor` | string | 卖家信息。 |
| `type` | string | 采集模式。 |
| `tags` | array | tags 字段。 |
| `price` | integer | 价格。 |
| `compare_at_price` | string | 价格。 |
| `discount_pct` | string | 数量。 |
| `price_min` | integer | 价格。 |
| `price_max` | integer | 价格。 |
| `currency` | string | 币种。 |
| `variants` | array | variants 字段。 |
| `variants.id` | integer | ID 标识。 |
| `variants.title` | string | 标题。 |
| `variants.option1` | string | option1 字段。 |
| `variants.option2` | string | option2 字段。 |
| `variants.option3` | string | option3 字段。 |
| `variants.price` | integer | 价格。 |
| `variants.sku` | string | ID 标识。 |
| `variants.available` | boolean | 库存信息。 |
| `variants.inventory_quantity` | string | inventory_quantity 字段。 |
| `variants.barcode` | string | barcode 字段。 |
| `variant_count` | integer | 数量。 |
| `available_variants` | integer | 库存信息。 |
| `reviews_count` | integer | 评论列表。 |
| `rating` | number | 评分。 |
| `review_app` | string | 评论列表。 |
| `estimated_sales_min` | integer | estimated_sales_min 字段。 |
| `estimated_sales_max` | integer | estimated_sales_max 字段。 |
| `estimated_sales_midpoint` | integer | estimated_sales_midpoint 字段。 |
| `images` | array | 图片列表。 |
| `featured_image` | string | featured_image 字段。 |
| `published_at` | string | published_at 字段。 |
| `created_at` | string | created_at 字段。 |
| `scraped_at` | string | scraped_at 字段。 |

## 使用要点

- 本接口适合：Shopify 品牌站商品。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/shopify-product-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode": "url", "maxPages": 1, "storeUrls": [{"url": "https://www.allbirds.com"}], "maxProducts": 20}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。

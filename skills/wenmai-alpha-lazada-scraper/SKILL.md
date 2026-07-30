---
name: wenmai-alpha-lazada-scraper
description: "Lazada 商品采集接口，用于获取东南亚站点的商品搜索、价格、销量及接口支持的 Listing 数据。当用户提到 Lazada 搜品、东南亚电商选品、Lazada 商品、竞品价格、类目研究或 Lazada scraper 时触发此技能。即使用户未明确提及数据源，只要目标是用 Lazada 商品数据做选品或竞品分析，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Alpha Lazada Scraper

## Purpose
Use this Skill to fetch Lazada Scraper data through Wenmai standard API. It is useful for Lazada 东南亚电商商品.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/lazada-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_lazada_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_lazada_scraper.py '{"mode": "search", "urls": ["https://www.lazada.sg/catalog/?q=earbuds"], "sortBy": "popularity", "country": "sg", "queries": ["laptop"], "maxPages": 0, "maxPrice": 3, "minPrice": 1, "minRating": 1, "categoryId": "keyboard", "maxListings": 3, "reviewsOnly": false, "fetchDetails": false, "fetchReviews": false, "freeShippingOnly": false, "maxNotifyListings": 3, "maxReviewsPerProduct": 3}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: `mode`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Extra-charge Parameter Rules

Treat `fetchDetails: true` as an opt-in, separately billed detail-page enrichment capability. Do not infer or enable it automatically. Include it only when the user explicitly requests enriched product details, and tell the user before the request that enabling it is billed separately.

Do not quote or explain upstream prices, plans, tiers, or billing formulas.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

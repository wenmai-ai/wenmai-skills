---
name: wenmai-alpha-etsy-scraper
description: "Etsy 商品采集接口，用于研究手作、设计、小众和个性化商品，返回接口支持的商品与市场结果数据。当用户提到 Etsy 搜品、手工品选品、小众产品、个性化商品、Etsy 竞品、价格研究或 Etsy scraper 时触发此技能。即使用户未明确提及 Etsy API，只要需要基于 Etsy 商品数据开展市场或竞品研究，也应触发此技能。"
---

# Wenmai Alpha Etsy Scraper

## Purpose
Use this Skill to fetch Etsy Scraper data through Wenmai standard API. It is useful for Etsy 手作/小众商品.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/etsy-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_etsy_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_etsy_scraper.py '{"sort": "most_relevant", "locale": "en-US", "onSale": false, "category": "jewelry-and-accessories", "currency": "USD", "maxItems": 3, "maxPrice": 3, "minPrice": 10, "searchQuery": "handmade necklace", "freeShipping": false, "excludeKeywords": ["digital", "download"], "includeKeywords": ["handmade"], "excludeDigitalDownloads": false}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: `searchQuery`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

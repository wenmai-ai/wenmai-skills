---
name: wenmai-alpha-walmart-fast-product-scraper
description: "Use when users need the Wenmai Alpha standard API `alpha_walmart_fast_product_scraper` for Walmart Fast Product Scraper, including Walmart 商品或评论. Sends user parameters as a JSON POST body to `/wmapi/v1/alpha/walmart-fast-product-scraper` and returns traceable raw gateway data for ecommerce research, competitor discovery, VOC, social trend analysis, or reporting."
---

# Wenmai Alpha Walmart Fast Product Scraper

## Purpose
Use this Skill to fetch Walmart Fast Product Scraper data through Wenmai standard API. It is useful for Walmart 商品或评论.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/walmart-fast-product-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_walmart_fast_product_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_walmart_fast_product_scraper.py '{"startUrls": [{"url": "https://walmart.com/search?q=tshirt"}], "maxProductsPerStartUrl": 3}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: `startUrls`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

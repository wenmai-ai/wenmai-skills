---
name: wenmai-alpha-kaufland-fast-product-scraper
description: "Use when users need the Wenmai Alpha standard API `alpha_kaufland_fast_product_scraper` for Kaufland Fast Product Scraper, including Kaufland 商品/类目. Sends user parameters as a JSON POST body to `/wmapi/v1/alpha/kaufland-fast-product-scraper` and returns traceable raw gateway data for ecommerce research, competitor discovery, VOC, social trend analysis, or reporting."
---

# Wenmai Alpha Kaufland Fast Product Scraper

## Purpose
Use this Skill to fetch Kaufland Fast Product Scraper data through Wenmai standard API. It is useful for Kaufland 商品/类目.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/kaufland-fast-product-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_kaufland_fast_product_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_kaufland_fast_product_scraper.py '{"keyword": "keyboard", "startUrlsCategories": [{"url": "https://www.kaufland.de/c/badausstattung/~27721/"}], "maxProductsPerCategory": 3}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

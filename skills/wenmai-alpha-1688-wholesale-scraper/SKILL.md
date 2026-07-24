---
name: wenmai-alpha-1688-wholesale-scraper
description: "Use when users need the Wenmai Alpha standard API `alpha_1688_wholesale_scraper` for 1688 Wholesale Scraper, including 1688 批发商品、供应商、MOQ、价格与销量. Sends user parameters as a JSON POST body to `/wmapi/v1/alpha/1688-wholesale-scraper` and returns traceable raw gateway data for ecommerce research, competitor discovery, VOC, social trend analysis, or reporting."
---

# Wenmai Alpha 1688 Wholesale Scraper

## Purpose
Use this Skill to fetch 1688 Wholesale Scraper data through Wenmai standard API. It is useful for 1688 批发商品、供应商、MOQ、价格与销量.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/1688-wholesale-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_1688_wholesale_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_1688_wholesale_scraper.py '{"sortBy": "relevance", "keywords": ["phone case"], "maxResults": 10}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Extra-charge Parameter Rules

Treat `includeSupplierIntelligence: true` as an opt-in, separately billed supplier-intelligence capability. Do not infer or enable it automatically. Include it only when the user explicitly requests supplier intelligence, and tell the user before the request that enabling it is billed separately.

Do not quote or explain upstream prices, plans, tiers, or billing formulas.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

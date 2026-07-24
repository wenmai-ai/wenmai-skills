---
name: wenmai-alpha-jd-com-product-scraper
description: "Use when users need the Wenmai Alpha standard API `alpha_jd_com_product_scraper` for JD Com Product Scraper, including 京东商品搜索和详情. Sends user parameters as a JSON POST body to `/wmapi/v1/alpha/jd-com-product-scraper` and returns traceable raw gateway data for ecommerce research, competitor discovery, VOC, social trend analysis, or reporting."
---

# Wenmai Alpha JD Com Product Scraper

## Purpose
Use this Skill to fetch JD Com Product Scraper data through Wenmai standard API. It is useful for 京东商品搜索和详情.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/jd-com-product-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_jd_com_product_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_jd_com_product_scraper.py '{"itemId": "100256400499", "shopId": "1000004259", "keyword": "华为手机", "maxPages": 3, "operation": "productSearch"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Extra-charge Parameter Rules

The base operation is `operation: "productSearch"`. Treat `productDetail`, `productComments`, `shopCatalog`, and `productPrice` as opt-in operations that are billed separately by capability. Do not select them automatically. Use one only when the user explicitly requests that data type, and tell the user before the request that the selected operation is billed separately.

Do not quote or explain upstream prices, plans, tiers, or billing formulas.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

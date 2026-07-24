---
name: wenmai-alpha-taobao-tmall-product-scraper
description: "Use when users need the Wenmai Alpha standard API `alpha_taobao_tmall_product_scraper` for Taobao TMALL Product Scraper, including 淘宝/天猫商品. Sends user parameters as a JSON POST body to `/wmapi/v1/alpha/taobao-tmall-product-scraper` and returns traceable raw gateway data for ecommerce research, competitor discovery, VOC, social trend analysis, or reporting."
---

# Wenmai Alpha Taobao Tmall Product Scraper

## Purpose
Use this Skill to fetch Taobao TMALL Product Scraper data through Wenmai standard API. It is useful for 淘宝/天猫商品.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/taobao-tmall-product-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_taobao_tmall_product_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_taobao_tmall_product_scraper.py '{"sort": "_sale", "itemId": "744983869996", "shopId": "67095450", "userId": "713464357", "keyword": "iphone 15", "endPrice": 5000, "maxPages": 3, "operation": "keywordSearch", "orderType": "feedbackdate", "tmallOnly": false, "startPrice": 100, "detailVersion": "v9", "catalogVersion": "v1"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Extra-charge Parameter Rules

The base operation is `operation: "keywordSearch"`. Treat `productDetail`, `shopCatalog`, `productReviews`, and `productQuestions` as opt-in operations that are billed separately by capability. Within `productDetail`, treat `detailVersion: "v4"` as a separately billed premium-detail capability.

Do not select these operations or the premium detail version automatically. Use them only when the user explicitly requests the corresponding data, and tell the user before the request that the selected capability is billed separately. Do not quote or explain upstream prices, plans, tiers, or billing formulas.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

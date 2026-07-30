---
name: wenmai-alpha-ozon-scraper-pro
description: "Ozon 商品采集接口，用于检索俄罗斯 Ozon 平台商品并获取接口支持的价格、销量、评价、卖家或商品池数据。当用户提到 Ozon 搜品、俄罗斯电商、Ozon 商品池、竞品分析、类目研究或 Ozon scraper 时触发此技能。只要用户需要基于 Ozon 真实商品数据进行选品或市场判断，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Alpha Ozon Scraper Pro

## Purpose
Use this Skill to fetch Ozon Scraper Pro data through Wenmai standard API. It is useful for Ozon 商品池.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/ozon-scraper-pro`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_ozon_scraper_pro.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_ozon_scraper_pro.py '{"urls": ["https://www.ozon.ru/category/noutbuki-15692/"], "onSale": false, "sorting": "score", "currency": "RUB", "language": "ru", "maxPrice": 3, "minPrice": 1, "maxResults": 3, "hasDiscount": false, "skipDetails": false, "isInstallment": false, "brandCertified": false, "hasReviewPoints": false, "includeSellerDetails": false}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Extra-charge Parameter Rules

Passing a non-empty `queries` list enables the supplier's separately billed search-results capability. Do not infer or expand queries automatically. Include them only when the user explicitly requests search, and tell the user before the request that search results are billed separately.

Do not quote or explain upstream prices, plans, tiers, or billing formulas.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

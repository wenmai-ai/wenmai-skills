---
name: wenmai-alpha-shopee-scraper
description: "Shopee 商品与店铺采集接口，用于获取东南亚等站点的商品、价格、销量、店铺及接口支持的市场数据。当用户提到 Shopee 搜品、店铺分析、东南亚选品、竞品商品、价格研究或 Shopee scraper 时触发此技能。即使用户未点名接口，只要需要使用 Shopee 商品或店铺数据开展市场研究，也应触发此技能。"
---

# Wenmai Alpha Shopee Scraper

## Purpose
Use this Skill to fetch Shopee Scraper data through Wenmai standard API. It is useful for Shopee 商品和店铺.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/shopee-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_shopee_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_shopee_scraper.py '{"debug": false, "country": "SG", "keywords": ["phone case"], "maxItems": 10, "priceSlicing": false}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

---
name: wenmai-alpha-temu-products-scraper
description: "Temu 商品采集接口，用于检索 Temu 商品池并获取接口支持的标题、价格、销量、评价和 Listing 数据。当用户提到 Temu 搜品、Temu 爆品、低价商品、竞品价格、商品池或 Temu scraper 时触发此技能。只要用户希望基于 Temu 商品数据开展选品、定价或竞品研究，也应触发此技能。"
---

# Wenmai Alpha Temu Products Scraper

## Purpose
Use this Skill to fetch Temu Products Scraper data through Wenmai standard API. It is useful for Temu 商品池.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/temu-products-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_temu_products_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_temu_products_scraper.py '{"currency": "USD", "maxResults": 40, "searchQueries": ["women dress"]}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: `searchQueries`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

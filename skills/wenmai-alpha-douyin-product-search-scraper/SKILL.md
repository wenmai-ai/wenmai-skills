---
name: wenmai-alpha-douyin-product-search-scraper
description: "抖音商品搜索采集接口，用于按关键词检索抖音电商商品并获取可用的商品、价格、销量及相关搜索结果数据。当用户提到抖音搜品、抖音商品搜索、抖音爆品、短视频电商选品、抖音竞品或 Douyin product search 时触发此技能。即使用户未点名 Alpha 接口，只要目标是在抖音商品池中查找或比较商品，也应触发此技能。"
---

# Wenmai Alpha Douyin Product Search Scraper

## Purpose
Use this Skill to fetch Douyin Product Search Scraper data through Wenmai standard API. It is useful for 抖音商品搜索.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/douyin-product-search-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_douyin_product_search_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_douyin_product_search_scraper.py '{"keywords": ["口红"], "maxResults": 3}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: `keywords`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

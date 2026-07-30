---
name: wenmai-alpha-walmart-reviews-scraper
description: "Walmart 评论采集接口，用于获取商品买家评论、评分及接口支持的评论元数据，为 VOC、痛点和竞品口碑分析提供依据。当用户提到 Walmart 评论、买家反馈、差评分析、商品口碑、用户痛点或 Walmart review scraper 时触发此技能。只要用户需要从 Walmart 评论中提炼真实消费者意见，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Alpha Walmart Reviews Scraper

## Purpose
Use this Skill to fetch Walmart Reviews Scraper data through Wenmai standard API. It is useful for Walmart 商品或评论.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/walmart-reviews-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_walmart_reviews_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_walmart_reviews_scraper.py '{"startUrls": [{"url": "https://walmart.com/search?q=tshirt"}], "reviewsSortType": "relevancy", "scrapeUntilDate": "keyboard", "maxReviewsPerProduct": 3, "maxProductsPerStartUrl": 3}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

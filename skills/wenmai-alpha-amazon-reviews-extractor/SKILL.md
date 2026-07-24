---
name: wenmai-alpha-amazon-reviews-extractor
description: "Use when users need the Wenmai Alpha standard API `alpha_amazon_reviews_extractor` for Amazon Reviews Extractor, including Amazon 商品、评论、Listing、竞品或搜索结果. Sends user parameters as a JSON POST body to `/wmapi/v1/alpha/amazon-reviews-extractor` and returns traceable raw gateway data for ecommerce research, competitor discovery, VOC, social trend analysis, or reporting."
---

# Wenmai Alpha Amazon Reviews Extractor

## Purpose
Use this Skill to fetch Amazon Reviews Extractor data through Wenmai standard API. It is useful for Amazon 商品、评论、Listing、竞品或搜索结果.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/amazon-reviews-extractor`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_amazon_reviews_extractor.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_amazon_reviews_extractor.py '{"sort": "helpful", "limit": 3, "rating": "all", "region": "amazon.com", "keywords": ["keyboard"], "language": "all", "products": ["https://www.amazon.com/Logitech-LIGHTSPEED-Wireless-Gaming-Mouse/product-reviews/B07CMS5Q6P/ref=cm_cr_getr_mb_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2&formatType=current_format", "B07MVJZQTC"], "all_stars": false, "avp_reviews": false, "personal_data": false, "include_variants": true, "scrape_image_reviews": true, "scrape_video_reviews": true}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: `products`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

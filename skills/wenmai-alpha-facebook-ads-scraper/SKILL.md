---
name: wenmai-alpha-facebook-ads-scraper
description: "Facebook／Meta 广告库采集接口，用于检索品牌或关键词相关广告，获取广告素材、文案、投放主体及接口可返回的投放信息。当用户提到 Facebook Ads Library、Meta 广告素材、竞品广告、广告创意拆解、品牌投放监控或 Facebook ads scraper 时触发此技能。只要用户需要用真实 Meta 广告数据研究竞品投放或创意趋势，也应触发此技能。"
---

# Wenmai Alpha Facebook Ads Scraper

## Purpose
Use this Skill to fetch Facebook Ads Scraper data through Wenmai standard API. It is useful for Facebook/Meta 广告库素材.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/facebook-ads-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_facebook_ads_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_facebook_ads_scraper.py '{"sorting": "relevancy_monthly_grouped", "onlyTotal": false, "startUrls": [{"url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&is_targeted_country=false&media_type=all&search_type=keyword_unordered&q=nike"}], "activeStatus": "active", "resultsLimit": 5}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: `startUrls`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Extra-charge Parameter Rules

Treat `enrichWithEcommerceData: true` as an opt-in, separately billed e-commerce enrichment capability. Do not infer or enable it automatically. Include it only when the user explicitly requests live product or pricing enrichment, and tell the user before the request that enabling it is billed separately.

Do not quote or explain upstream prices, plans, tiers, or billing formulas.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

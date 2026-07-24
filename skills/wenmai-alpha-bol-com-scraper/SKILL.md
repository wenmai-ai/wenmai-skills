---
name: wenmai-alpha-bol-com-scraper
description: "Use when users need the Wenmai Alpha standard API `alpha_bol_com_scraper` for Bol Com Scraper, including Bol.com 商品池. Sends user parameters as a JSON POST body to `/wmapi/v1/alpha/bol-com-scraper` and returns traceable raw gateway data for ecommerce research, competitor discovery, VOC, social trend analysis, or reporting."
---

# Wenmai Alpha Bol Com Scraper

## Purpose
Use this Skill to fetch Bol Com Scraper data through Wenmai standard API. It is useful for Bol.com 商品池.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/bol-com-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_bol_com_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_bol_com_scraper.py '{"q": "keyboard", "url": "https://www.amazon.com/s?k=keyboard", "mode": "search", "urls": ["https://www.amazon.com/s?k=keyboard"], "query": "keyboard", "sortBy": "relevance", "country": "be", "keyword": "keyboard", "category": "keyboard", "llmModel": "keyboard", "maxItems": 3, "watchMode": false, "maxResults": 3, "productUrl": "https://www.amazon.com/s?k=keyboard", "searchTerm": "keyboard", "bolClientId": "keyboard", "llmProvider": "openrouter", "maxProducts": 3, "productUrls": ["https://www.amazon.com/s?k=keyboard"], "searchQuery": "PlayStation 5", "fetchDetails": false, "googleApiKey": "keyboard", "openaiApiKey": "keyboard", "ollamaBaseUrl": "http://localhost:11434", "includeDetails": false, "anthropicApiKey": "keyboard", "bolClientSecret": "keyboard", "enableAiAnalysis": false, "openrouterApiKey": "keyboard"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Extra-charge Parameter Rules

Treat `watchMode: true` and `enableAiAnalysis: true` as opt-in, separately billed capabilities. Do not infer or enable them automatically. Include either parameter only when the user explicitly requests price-history/drop monitoring or AI analysis, and tell the user before the request that the capability is billed separately.

Do not quote or explain upstream prices, plans, tiers, or billing formulas. Supplier events that are not controlled by a documented input parameter must not be presented as optional parameter switches.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

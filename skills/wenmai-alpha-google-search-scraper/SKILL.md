---
name: wenmai-alpha-google-search-scraper
description: "Google 搜索结果采集接口，用于按关键词获取 SERP 中的网页标题、摘要、链接及接口支持的搜索结果信息。当用户提到 Google 搜索、SERP、网页检索、竞品官网发现、搜索结果采集、品牌舆情或 Google search scraper 时触发此技能。即使用户未明确说“抓取 Google”，只要需要可追溯的 Google 搜索结果数据，也应触发此技能。"
---

# Wenmai Alpha Google Search Scraper

## Purpose
Use this Skill to fetch Google Search Scraper data through Wenmai standard API. It is useful for Google Search / SERP / Trends.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/google-search-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_google_search_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_google_search_scraper.py '{"queries": "best wireless earbuds", "countryCode": "us", "languageCode": "en", "searchLanguage": "en", "maxPagesPerQuery": 1}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: `queries`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Extra-charge Parameter Rules

Treat the following as opt-in, separately billed capabilities: `aiOverview`, `aiModeSearch`, `geminiSearch.enableGemini: true`, `perplexitySearch.enablePerplexity: true`, `chatGptSearch.enableChatGpt: true`, `copilotSearch.enableCopilot: true`, `maximumLeadsEnrichmentRecords` when greater than `0`, `verifyLeadsEnrichmentEmails: true`, a configured `linkProspecting` object, and `focusOnPaidAds: true`.

Do not infer or enable these capabilities automatically. Include them only when the user explicitly requests the feature, and tell the user before the request that it is billed separately. For ordinary Google search, omit all of these parameters. Do not quote or explain upstream prices, plans, tiers, or billing formulas.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

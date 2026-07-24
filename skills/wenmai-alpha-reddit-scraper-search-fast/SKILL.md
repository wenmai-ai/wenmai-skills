---
name: wenmai-alpha-reddit-scraper-search-fast
description: "Reddit 快速搜索采集接口，用于按关键词查找帖子、评论和社区讨论，获取用户观点与接口支持的互动数据。当用户提到 Reddit 搜索、帖子评论、社区舆情、用户痛点、需求洞察、VOC、subreddit 或 Reddit scraper 时触发此技能。即使用户未明确提及 Reddit API，只要希望从 Reddit 讨论中提炼真实用户声音，也应触发此技能。"
---

# Wenmai Alpha Reddit Scraper Search Fast

## Purpose
Use this Skill to fetch Reddit Scraper Search Fast data through Wenmai standard API. It is useful for Reddit 搜索、帖子、评论和舆情.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/reddit-scraper-search-fast`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_reddit_scraper_search_fast.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_reddit_scraper_search_fast.py '{"sort": "relevance", "queries": ["Cheesecake", "Swimming Pool"], "maxPosts": 3, "timeframe": "all", "includeNsfw": false, "maxComments": 3, "strictSearch": false, "subredditSort": "relevance", "scrapeComments": false, "content_analysis": false, "maximize_coverage": false, "strictTokenFilter": false, "subredditKeywords": ["keyboard"], "sentiment_analysis": false, "subredditTimeframe": "all", "forceSortNewForTimeFilteredRuns": false}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

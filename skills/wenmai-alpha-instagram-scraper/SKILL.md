---
name: wenmai-alpha-instagram-scraper
description: "Instagram 内容采集接口，用于获取接口支持的账号、帖子、话题标签和互动数据，服务于社媒趋势、达人和品牌内容研究。当用户提到 Instagram 账号分析、帖子采集、hashtag、品牌内容、达人研究、互动表现或 Instagram scraper 时触发此技能。即使用户未点名接口，只要需要基于 Instagram 公开内容开展社媒分析，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Alpha Instagram Scraper

## Purpose
Use this Skill to fetch Instagram Scraper data through Wenmai standard API. It is useful for Instagram 账号、话题和内容.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/instagram-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_instagram_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_instagram_scraper.py '{"search": "keyboard", "directUrls": ["https://www.instagram.com/humansofny/"], "searchType": "hashtag", "resultsType": "posts", "searchLimit": 3, "resultsLimit": 3, "addParentData": false}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

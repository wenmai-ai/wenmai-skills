---
name: wenmai-alpha-tiktok-scraper
description: "TikTok 内容采集接口，用于获取接口支持的视频、账号、话题标签、互动表现和趋势数据。当用户提到 TikTok 视频、达人账号、hashtag、热门内容、社媒趋势、爆款内容或 TikTok scraper 时触发此技能。即使用户未明确说“采集 TikTok”，只要需要用 TikTok 公开数据研究内容或趋势，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Alpha Tiktok Scraper

## Purpose
Use this Skill to fetch Tiktok Scraper data through Wenmai standard API. It is useful for TikTok 视频、账号、话题和趋势.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/tiktok-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_tiktok_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_tiktok_scraper.py '{"searchQueries": ["keyboard"], "searchSection": "/video", "resultsPerPage": 10}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: none documented by the API reference; pass at least one meaningful query, URL, ID, keyword, mode, or filter parameter from `references/api.md`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Extra-charge Parameter Rules

Treat the following as opt-in, separately billed capabilities: date filters (`oldestPostDateUnified`, `newestPostDate`, `videoSearchDateFilter`), popularity filters (`mostDiggs`, `leastDiggs`), follower/following collection (`maxFollowersPerProfile`, `maxFollowingPerProfile`), video search sorting (`videoSearchSorting`), video downloads (`shouldDownloadVideos`), comments (`commentsPerPost`, `topLevelCommentsPerPost`, `maxRepliesPerComment`), and transcription modes in `downloadSubtitlesOptions`.

Do not infer or enable these capabilities automatically. Include them only when the user explicitly requests the feature, and tell the user before the request that it is billed separately. Do not quote or explain upstream prices, plans, tiers, or billing formulas.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

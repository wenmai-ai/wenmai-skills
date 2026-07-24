---
name: wenmai-alpha-youtube-comments-scraper
description: "YouTube 评论采集接口，用于获取指定视频的评论、回复及接口支持的互动元数据，为受众反馈和 VOC 分析提供原始数据。当用户提到 YouTube 评论、视频反馈、观众观点、评论舆情、用户痛点或 YouTube comments scraper 时触发此技能。只要用户希望从 YouTube 评论中提炼真实受众声音，也应触发此技能。"
---

# Wenmai Alpha Youtube Comments Scraper

## Purpose
Use this Skill to fetch Youtube Comments Scraper data through Wenmai standard API. It is useful for YouTube 视频、频道、搜索或评论.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/alpha/youtube-comments-scraper`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/alpha_youtube_comments_scraper.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/alpha_youtube_comments_scraper.py '{"startUrls": [{"url": "https://www.youtube.com/watch?v=xObhZ0Ga7EQ"}], "maxComments": 3, "sortCommentsBy": "NEWEST_FIRST", "oldestCommentDate": "2026-03-01"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, allowed values, defaults, request examples, or response fields.

## Parameter Rules

Required top-level fields: `startUrls`.

Default assumptions: preserve the user's requested marketplace, country, language, URL list, keyword list, IDs, filters, pagination, and result limits. For scraper-style endpoints, avoid expanding result limits unless the user asks for a broader scrape.

## Response Rules

Present returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers and source URLs traceable to response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

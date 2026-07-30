---
name: wenmai-sif-keyword-overview
description: "SIF Amazon 关键词需求概览接口，用于查询搜索量历史、ABA 排名历史、Top 3 点击或转化集中度、市场需求规模和关键词趋势。当用户提到关键词搜索量、ABA 排名、点击集中度、转化集中度、需求趋势或 SIF keyword overview 时触发此技能。只要用户需要判断某个 Amazon 关键词的需求大小与变化，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SIF Keyword Overview

## Purpose
Use this Skill to fetch SIF 关键词概览 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sif/market-get-keyword-history`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sif_keyword_overview.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sif_keyword_overview.py '{"keywords": ["wireless earbuds"], "country": "US", "granularity": "week"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `keywords`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

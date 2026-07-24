---
name: wenmai-sif-asin-keywords
description: "Use when users need SIF reverse ASIN keyword intelligence through Wenmai standard API, including traffic keywords, organic or ad rank signals, keyword contribution changes, rank gaps, gaining or declining keywords, and competitor ASIN keyword source analysis."
---

# Wenmai SIF ASIN Keywords

## Purpose
Use this Skill to fetch SIF ASIN 关键词 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sif/market-get-asin-keyword-signals`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sif_asin_keywords.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sif_asin_keywords.py '{"asin": "B08GHW4TBS", "country": "US", "time_type": "lately", "time_value": "7", "topN": 50}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `asin`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

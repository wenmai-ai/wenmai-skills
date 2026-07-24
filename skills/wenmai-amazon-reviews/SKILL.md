---
name: wenmai-amazon-reviews
description: "Use when users need Amazon review retrieval or VOC analysis by ASIN, including star filters, recent/helpful sorting, buyer complaints, positive feedback, verified purchase review checks, competitor review research, or customer feedback mining through Wenmai standard API."
---

# Wenmai Amazon Reviews

## Purpose
Use this Skill to fetch Amazon 评论 / VOC data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/carvenmaster/get-asin-reviews`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/amazon_reviews.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/amazon_reviews.py '{"asin": "B08N5WRWNW", "country": "US", "sort_by": "recent", "filter_by_star": "all_stars"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `asin`, `country`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

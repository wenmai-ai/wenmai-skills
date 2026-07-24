---
name: wenmai-sellersprite-market-statistics
description: "Use when users need SellerSprite node-level market statistics through Wenmai standard API, including a specific Amazon category node summary, topN market statistics, new product metrics, average sales/revenue/price/rating/BSR, and node-level opportunity assessment."
---

# Wenmai SellerSprite Market Statistics

## Purpose
Use this Skill to fetch 卖家精灵类目统计 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/market-research-statistics`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sellersprite_market_statistics.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sellersprite_market_statistics.py '{"request": {"marketplace": "US", "nodeIdPath": "172282:281407", "topN": 10}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `request`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

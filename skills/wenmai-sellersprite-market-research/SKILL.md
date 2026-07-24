---
name: wenmai-sellersprite-market-research
description: "Use when users need SellerSprite category market research through Wenmai standard API, including category market size, total products, sales, revenue, average price, average rating, BSR, brand/seller concentration, new product ratio, fulfillment mix, or opportunity screening."
---

# Wenmai SellerSprite Market Research

## Purpose
Use this Skill to fetch 卖家精灵市场研究 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/market-research`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sellersprite_market_research.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sellersprite_market_research.py '{"request": {"marketplace": "US", "nodeIdPath": "172282:281407", "page": 1, "size": 50}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `request`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

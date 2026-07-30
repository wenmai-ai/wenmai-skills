---
name: wenmai-sellersprite-market-research
description: "卖家精灵 Amazon 类目市场研究接口，用于分析市场规模、商品数量、销量、销售额、均价、评分、BSR、品牌与卖家集中度、新品占比和配送结构。当用户提到类目市场分析、市场容量、竞争集中度、新品机会、FBA 占比、选品赛道或 SellerSprite market research 时触发此技能。只要需要评估某个 Amazon 类目的进入机会，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
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

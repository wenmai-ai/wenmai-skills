---
name: wenmai-sellersprite-competitor
description: "卖家精灵竞品查询接口，用于按 ASIN、品牌、卖家、类目、站点、月份、关键词或变体条件查找 Amazon 竞品及其指标。当用户提到竞品查询、相似 ASIN、品牌竞品、卖家商品、类目竞品、变体竞品或 SellerSprite competitor lookup 时触发此技能。只要用户需要建立或筛选 Amazon 竞品清单，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SellerSprite Competitor Lookup

## Purpose
Use this Skill to fetch 卖家精灵竞品查询 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/competitor-lookup`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sellersprite_competitor_lookup.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sellersprite_competitor_lookup.py '{"request": {"marketplace": "US", "asins": ["B08GHW4TBS"], "page": 1, "size": 50}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `request`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

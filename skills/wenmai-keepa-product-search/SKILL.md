---
name: wenmai-keepa-product-search
description: "Keepa Amazon 商品搜索接口，用于按关键词和站点检索商品，返回 ASIN 及接口支持的轻量商品结果，可用于建立候选商品池。当用户提到 Keepa 搜品、Amazon 关键词搜品、ASIN 搜索、商品发现、候选商品池或 marketplace product search 时触发此技能。即使用户未明确提及 Keepa，只要希望按关键词获取 Amazon 商品或 ASIN 列表，也应触发此技能。"
---

# Wenmai Keepa Product Search

## Purpose
Use this Skill to fetch Keepa 商品搜索 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/keepa/keepa-product-search`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/keepa_product_search.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/keepa_product_search.py '{"domain": 1, "term": "water bottle", "page": 0, "asins-only": 1}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `domain`, `term`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

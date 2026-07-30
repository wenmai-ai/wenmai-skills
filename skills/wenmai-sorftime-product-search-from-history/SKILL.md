---
name: wenmai-sorftime-product-search-from-history
description: "Sorftime Amazon 历史商品搜索接口，用于按历史月份、站点及接口支持的筛选条件查询商品池。当用户提到历史搜品、历史选品、指定月份商品数据、过往市场快照或 historical product search 时触发此技能。只要需要基于某个历史时间点筛选 Amazon 商品，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Search From History

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_search_from_history` for Amazon 历史商品搜索.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-search-from-history`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_search_from_history.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_search_from_history.py '{"search_time":"2026-06","amz_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `search_time`, `amz_site`.

Preserve the user's historical month, marketplace, keywords, categories, filters, sorting, pagination, and result limits. Do not replace the requested period.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

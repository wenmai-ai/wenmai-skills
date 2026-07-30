---
name: wenmai-sorftime-product-search
description: "Sorftime Amazon 实时商品搜索接口，用于按站点及接口支持的筛选条件查询当前商品池和市场数据。当用户提到 Amazon 实时搜品、商品筛选、候选 ASIN、市场选品、竞品发现或 Sorftime product search 时触发此技能。只要需要基于实时条件建立 Amazon 候选商品池，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Search

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_search` for Amazon 实时商品搜索.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-search`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_search.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_search.py '{"amz_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `amz_site`.

Preserve the user's marketplace, keywords, categories, filters, sorting, pagination, and result limits. Do not broaden filters automatically.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

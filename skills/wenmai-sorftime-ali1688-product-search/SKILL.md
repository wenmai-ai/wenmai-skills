---
name: wenmai-sorftime-ali1688-product-search
description: "Sorftime 1688 商品多维搜索接口，用于按关键词、类目和接口支持的筛选条件查找 1688 货源商品。当用户提到 1688 搜品、阿里巴巴货源、批发选品、供应商商品搜索、以关键词找货或 Sorftime 1688 product search 时触发此技能。只要需要通过 1688 商品池寻找或比较货源，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime 1688 Product Search

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `ali1688_product_search` for 1688 商品多维搜索.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/ali1688-product-search`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/ali1688_product_search.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/ali1688_product_search.py '{}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: none.

Preserve the user's keywords, category, filters, sorting, pagination, and result limits. Do not broaden the search scope unless the user asks.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

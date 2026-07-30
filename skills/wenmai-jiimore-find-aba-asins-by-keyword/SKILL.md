---
name: wenmai-jiimore-find-aba-asins-by-keyword
description: "JIIMORE ABA 商品查询接口，用于按 Amazon 关键词查找 ABA 关联商品或 ASIN，发现关键词下的头部点击商品和竞品。当用户提到按关键词找 ASIN、ABA 点击商品、关键词头部商品、竞品发现或 ABA 商品分析时触发此技能。只要用户需要确认某个关键词对应哪些 Amazon 商品，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai JIIMORE find aba asins by keyword

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_find_aba_asins_by_keyword` for 按关键词查询 ABA 商品.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/aba-asins-by-keyword`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_find_aba_asins_by_keyword.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_find_aba_asins_by_keyword.py '{"request": {"keywords": ["neck fan"], "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.keywords`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

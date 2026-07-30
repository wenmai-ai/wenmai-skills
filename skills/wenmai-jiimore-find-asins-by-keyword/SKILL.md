---
name: wenmai-jiimore-find-asins-by-keyword
description: "JIIMORE Amazon 商品搜索接口，用于按关键词查找商品或 ASIN，建立候选商品池并发现竞品。当用户提到关键词搜品、按词找 ASIN、Amazon 商品搜索、候选商品池、竞品发现或选品研究时触发此技能。只要用户希望根据搜索词获取 Amazon 商品列表，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai JIIMORE find asins by keyword

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_find_asins_by_keyword` for 按关键词查询商品.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/asins-by-keyword`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_find_asins_by_keyword.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_find_asins_by_keyword.py '{"request": {"keyword": "neck fan", "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.keyword`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

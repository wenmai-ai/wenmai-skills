---
name: wenmai-jiimore-find-niches-by-asin
description: "JIIMORE ASIN 细分市场查询接口，用于查找某个 Amazon 商品所属或相关的 niche，判断市场归属并映射竞品市场。当用户提到按 ASIN 找细分市场、商品属于哪个 niche、市场归属、竞品市场或细分机会时触发此技能。只要用户需要从一个 ASIN 反查相关细分市场，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai JIIMORE find niches by asin

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_find_niches_by_asin` for 按 ASIN 查询细分市场.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/niches-by-asin`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_find_niches_by_asin.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_find_niches_by_asin.py '{"request": {"asin": "B09PCSR9SX", "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.asin`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

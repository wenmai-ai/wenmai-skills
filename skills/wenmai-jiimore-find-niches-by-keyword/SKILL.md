---
name: wenmai-jiimore-find-niches-by-keyword
description: "JIIMORE 关键词细分市场查询接口，用于按 Amazon 关键词查找相关 niche，发现市场并筛选类目机会。当用户提到按关键词找细分市场、关键词对应 niche、市场发现、类目机会或细分赛道研究时触发此技能。只要用户希望从一个搜索词定位相关 Amazon 细分市场，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai JIIMORE find niches by keyword

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_find_niches_by_keyword` for 按关键词查询细分市场.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/niches-by-keyword`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_find_niches_by_keyword.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_find_niches_by_keyword.py '{"request": {"keyword": "neck fan", "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.keyword`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

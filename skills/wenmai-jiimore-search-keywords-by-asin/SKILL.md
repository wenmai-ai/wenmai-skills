---
name: wenmai-jiimore-search-keywords-by-asin
description: "JIIMORE ASIN 关联关键词接口，用于根据 Amazon 商品发现相关搜索词并构建竞品关键词池。当用户提到 ASIN 反查关键词、商品关联词、竞品关键词池、按 ASIN 找搜索词或 keywords by ASIN 时触发此技能。即使用户未明确提及 JIIMORE，只要需要从一个 ASIN 出发发现相关关键词，也应触发此技能。"
---

# Wenmai JIIMORE search keywords by asin

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_search_keywords_by_asin` for 按 ASIN 查询关键词.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/keywords-by-asin`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_search_keywords_by_asin.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_search_keywords_by_asin.py '{"request": {"asin": "B09PCSR9SX", "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.asin`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

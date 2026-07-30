---
name: wenmai-jiimore-search-keywords-by-keyword
description: "JIIMORE Amazon 普通关键词扩展接口，用于围绕种子词发现相关词、长尾词和可用于商品研究的搜索词。当用户提到关键词扩词、长尾词、相关关键词、搜索词挖掘、关键词池或 keywords by keyword 时触发此技能。只要用户需要从一个 Amazon 关键词扩展普通相关词而非限定 ABA 数据，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai JIIMORE search keywords by keyword

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_search_keywords_by_keyword` for 关键词扩词.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/keywords-by-keyword`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_search_keywords_by_keyword.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_search_keywords_by_keyword.py '{"request": {"keyword": "neck fan", "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.keyword`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

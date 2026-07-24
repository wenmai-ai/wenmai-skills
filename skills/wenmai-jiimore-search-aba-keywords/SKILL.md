---
name: wenmai-jiimore-search-aba-keywords
description: "JIIMORE ASIN ABA 关键词接口，用于按 Amazon 商品反查 ABA 搜索词，分析商品点击关键词和流量来源。当用户提到 ASIN 的 ABA 词、ABA 搜索词、点击关键词、竞品 ABA 关键词、流量来源或 ABA reverse lookup 时触发此技能。只要需要查找与某个 ASIN 关联的 ABA 关键词，也应触发此技能。"
---

# Wenmai JIIMORE search aba keywords

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_search_aba_keywords` for 按 ASIN 查询 ABA 关键词.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/aba-keywords`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_search_aba_keywords.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_search_aba_keywords.py '{"request": {"asins": ["B09PCSR9SX"], "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.asins`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

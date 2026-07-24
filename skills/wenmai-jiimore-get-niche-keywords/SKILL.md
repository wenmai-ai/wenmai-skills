---
name: wenmai-jiimore-get-niche-keywords
description: "JIIMORE 细分市场关键词接口，用于获取指定 Amazon niche 的关键词池，分析搜索需求和流量词。当用户提到 niche 关键词、细分市场流量词、赛道关键词、市场搜索词、关键词池或 niche keywords 时触发此技能。只要用户希望获取某个细分市场对应的 Amazon 关键词列表，也应触发此技能。"
---

# Wenmai JIIMORE get niche keywords

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_get_niche_keywords` for 查询细分市场关键词.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/niche-keywords`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_get_niche_keywords.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_get_niche_keywords.py '{"request": {"nicheId": "sample-niche", "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.nicheId`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

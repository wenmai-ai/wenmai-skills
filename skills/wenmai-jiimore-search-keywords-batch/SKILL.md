---
name: wenmai-jiimore-search-keywords-batch
description: "JIIMORE Amazon 关键词批量查询接口，用于一次获取多个关键词的搜索与接口支持的市场指标，便于横向比较。当用户提到批量关键词、关键词指标对比、多个搜索词、关键词数据表、批量查词或 keyword batch 时触发此技能。只要用户需要同时核验一组 Amazon 关键词的数据，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai JIIMORE search keywords batch

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_search_keywords_batch` for 批量查询关键词指标.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/keywords-batch`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_search_keywords_batch.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_search_keywords_batch.py '{"request": {"keywords": ["neck fan"], "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.keywords`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

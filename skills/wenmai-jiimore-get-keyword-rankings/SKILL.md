---
name: wenmai-jiimore-get-keyword-rankings
description: "JIIMORE ASIN 关键词排名接口，用于反查 Amazon 商品的关联关键词及其排名表现。当用户提到 ASIN 关键词排名、自然排名、关键词位置、竞品排名、反查排名词或 keyword rankings 时触发此技能。即使用户未明确提及 JIIMORE，只要需要查看某个 ASIN 在相关关键词下的排名，也应触发此技能。"
---

# Wenmai JIIMORE get keyword rankings

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_get_keyword_rankings` for ASIN 反查关键词排名.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/keyword-rankings`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_get_keyword_rankings.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_get_keyword_rankings.py '{"request": {"asin": "B09PCSR9SX", "countryCode": "US", "days": 7}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.asin`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

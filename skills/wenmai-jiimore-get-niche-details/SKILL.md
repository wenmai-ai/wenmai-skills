---
name: wenmai-jiimore-get-niche-details
description: "JIIMORE Amazon 细分市场详情接口，用于获取指定 niche 的基础信息、市场指标、竞争情况和机会评估数据。当用户提到 niche 详情、细分市场指标、市场规模、竞争情况、赛道分析或 niche details 时触发此技能。只要用户需要深入查看一个明确的 Amazon 细分市场，也应触发此技能。"
---

# Wenmai JIIMORE get niche details

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_get_niche_details` for 查询细分市场详情.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/niche-details`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_get_niche_details.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_get_niche_details.py '{"request": {"nicheId": "sample-niche", "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.nicheId`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

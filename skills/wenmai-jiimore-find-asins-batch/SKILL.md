---
name: wenmai-jiimore-find-asins-batch
description: "JIIMORE ASIN 批量查询接口，用于一次获取多个 Amazon 商品的摘要信息和接口支持的关键指标。当用户提到批量 ASIN、商品摘要、批量核验商品、补全竞品清单或多个 ASIN 对比时触发此技能。即使用户未明确提及 JIIMORE，只要需要批量查询 Amazon ASIN 基础数据，也应触发此技能。"
---

# Wenmai JIIMORE find asins batch

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_find_asins_batch` for 批量查询 ASIN 摘要.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/asins-batch`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_find_asins_batch.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_find_asins_batch.py '{"request": {"asins": ["B09PCSR9SX"], "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.asins`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

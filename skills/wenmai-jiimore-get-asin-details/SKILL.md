---
name: wenmai-jiimore-get-asin-details
description: "JIIMORE Amazon ASIN 商品详情接口，用于查询一个或多个商品的基础信息、类目和接口支持的市场指标。当用户提到 ASIN 详情、商品信息、批量商品详情、候选商品核验、竞品资料或 JIIMORE 商品查询时触发此技能。只要用户需要获取指定 Amazon ASIN 的详细数据，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai JIIMORE get asin details

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_get_asin_details` for ASIN 商品详情.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/asin-details`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_get_asin_details.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_get_asin_details.py '{"request": {"asins": ["B09PCSR9SX"], "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.asins`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

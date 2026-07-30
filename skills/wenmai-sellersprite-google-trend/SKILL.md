---
name: wenmai-sellersprite-google-trend
description: "卖家精灵 Google Trends 关键词趋势接口，用于查询指定关键词在目标市场和时间范围内的搜索热度变化。当用户提到 Google 趋势、关键词热度、需求变化、季节性、市场趋势、关键词对比或 SellerSprite Google Trend 时触发此技能。只要用户希望通过搜索趋势判断 Amazon 市场需求走势，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SellerSprite google trend

## Purpose
Use this Skill to call the Wenmai SellerSprite standard API `google_trend`.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/google-trend`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/google_trend.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/google_trend.py '{"request": {"marketplace": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for parameter details, response fields, and the exact API payload.

## Parameter Rules

Required fields: `request, request.marketplace`.

Preserve the user's requested marketplace, ASIN, keyword, date range, pagination, filters, and sort order. Use Amazon US / `US` only when the user does not specify a marketplace and the parameter set supports that default.

## Response Rules

Return compact tables or summaries for inspection tasks, keeping raw numbers traceable to response fields. If the API response contains `error` or a non-`OK` `code`, report the gateway message and suggest parameter corrections. Never invent missing data.

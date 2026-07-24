---
name: wenmai-sellersprite-traffic-source
description: "Use when users need the Wenmai SellerSprite standard API `traffic_source` for Amazon 流量关键词结构分析工具（ASIN / 关键词维度）. Sends user parameters as a JSON POST body to `/wmapi/v1` and returns traceable raw gateway data for analysis or reporting."
---

# Wenmai SellerSprite traffic source

## Purpose
Use this Skill to call the Wenmai SellerSprite standard API `traffic_source`.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/traffic-source`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/traffic_source.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/traffic_source.py '{"request": {"marketplace": "US", "q": "B08GHW4TBS", "month": "202203"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for parameter details, response fields, and the exact API payload.

## Parameter Rules

Required fields: `request, request.marketplace, request.q, request.month`.

Preserve the user's requested marketplace, ASIN, keyword, date range, pagination, filters, and sort order. Use Amazon US / `US` only when the user does not specify a marketplace and the parameter set supports that default.

## Response Rules

Return compact tables or summaries for inspection tasks, keeping raw numbers traceable to response fields. If the API response contains `error` or a non-`OK` `code`, report the gateway message and suggest parameter corrections. Never invent missing data.

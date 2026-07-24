---
name: wenmai-sellersprite-traffic-source
description: "卖家精灵 Amazon 流量来源分析接口，用于从 ASIN 或关键词维度查看流量关键词结构和接口支持的来源指标。当用户提到流量来源、ASIN 流量结构、关键词来源、自然流量与广告流量、竞品流量入口或 SellerSprite traffic source 时触发此技能。只要用户需要判断 Amazon 商品的搜索流量从哪里来，也应触发此技能。"
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

---
name: wenmai-sellersprite-traffic-keyword-stat
description: "卖家精灵 ASIN 流量关键词概览统计接口，用于汇总自然词、广告词、流量词和转化词等关键词结构指标。当用户提到关键词结构、流量词统计、自然与广告关键词占比、ASIN 关键词概览或 traffic keyword stat 时触发此技能。只要用户想先查看 Amazon 商品关键词结构的总体盘面而非逐词明细，也应触发此技能。"
---

# Wenmai SellerSprite traffic keyword stat

## Purpose
Use this Skill to call the Wenmai SellerSprite standard API `traffic_keyword_stat`.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/traffic-keyword-stat`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/traffic_keyword_stat.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/traffic_keyword_stat.py '{"marketplace": "US", "asin": "B08GHW4TBS"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for parameter details, response fields, and the exact API payload.

## Parameter Rules

Required fields: `marketplace, asin`.

Preserve the user's requested marketplace, ASIN, keyword, date range, pagination, filters, and sort order. Use Amazon US / `US` only when the user does not specify a marketplace and the parameter set supports that default.

## Response Rules

Return compact tables or summaries for inspection tasks, keeping raw numbers traceable to response fields. If the API response contains `error` or a non-`OK` `code`, report the gateway message and suggest parameter corrections. Never invent missing data.

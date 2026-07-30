---
name: wenmai-sellersprite-traffic-keyword
description: "卖家精灵 ASIN 流量关键词接口，用于查询关键词列表、自然位与广告位、搜索量、购买率、流量占比、关键词类型、转化类型和排名位置。当用户提到 ASIN 反查关键词、自然排名、广告排名、流量词、转化词、关键词占比或 SellerSprite traffic keyword 时触发此技能。只要用户需要分析哪些搜索词为 Amazon 商品带来流量，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SellerSprite Traffic Keyword

## Purpose
Use this Skill to fetch 卖家精灵流量关键词 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/traffic-keyword`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sellersprite_traffic_keyword.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sellersprite_traffic_keyword.py '{"request": {"marketplace": "US", "asin": "B08GHW4TBS", "page": 1, "size": 50}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `request`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

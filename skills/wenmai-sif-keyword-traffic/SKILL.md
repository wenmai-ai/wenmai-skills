---
name: wenmai-sif-keyword-traffic
description: "SIF 关键词流量与竞争分析接口，用于查看头部 ASIN 的流量份额、自然／SP／SB／SBV 占比、集中度、竞争位置和关键词机会。当用户提到关键词竞争、流量份额、头部 ASIN、自然广告结构、关键词垄断、竞争强度或 SIF keyword traffic 时触发此技能。只要用户需要判断 Amazon 关键词是否拥挤或仍有进入机会，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SIF Keyword Traffic

## Purpose
Use this Skill to fetch SIF 关键词竞争 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sif/market-get-keyword-competition`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sif_keyword_traffic.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sif_keyword_traffic.py '{"keyword": "wireless earbuds", "country": "US", "time_type": "all", "rank_evolution": false}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `keyword`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

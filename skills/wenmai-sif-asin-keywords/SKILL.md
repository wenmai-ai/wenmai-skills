---
name: wenmai-sif-asin-keywords
description: "SIF ASIN 反查关键词接口，用于获取流量关键词、自然排名、广告排名、关键词贡献变化、排名差距以及上升或下降关键词。当用户提到 SIF 反查、ASIN 关键词、自然位、广告位、流量词、关键词涨跌、竞品关键词或 reverse ASIN 时触发此技能。即使用户未明确提及 SIF，只要需要查找与某个 Amazon ASIN 关联并带来流量的关键词，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SIF ASIN Keywords

## Purpose
Use this Skill to fetch SIF ASIN 关键词 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sif/market-get-asin-keyword-signals`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sif_asin_keywords.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sif_asin_keywords.py '{"asin": "B08GHW4TBS", "country": "US", "time_type": "lately", "time_value": "7", "topN": 50}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `asin`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

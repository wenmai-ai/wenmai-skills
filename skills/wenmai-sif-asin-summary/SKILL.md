---
name: wenmai-sif-asin-summary
description: "SIF ASIN 流量概览接口，用于汇总 Listing 的自然与广告流量占比、SP／SB／SBV 渠道结构、推荐流量来源和整体流量健康度。当用户提到 ASIN 流量概览、自然广告占比、广告渠道结构、Listing 流量健康或 SIF ASIN summary 时触发此技能。只要用户需要先查看 Amazon 商品整体流量结构而非逐关键词明细，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SIF ASIN Traffic Summary

## Purpose
Use this Skill to fetch SIF ASIN 流量概览 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sif/ops-get-listing-traffic-overview`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sif_asin_summary.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sif_asin_summary.py '{"asin": "B08GHW4TBS", "country": "US", "timePieceType": "latelyDay", "timePieceValue": "7"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `asin`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

---
name: wenmai-sorftime-product-trend
description: "Sorftime Amazon 商品历史趋势接口，用于查询指定 ASIN 的价格、销量、排名、评分及接口支持的历史变化。当用户提到商品趋势、历史销量、价格走势、BSR 变化、评论趋势或 product trend 时触发此技能。只要需要分析某个 Amazon 商品的时间序列表现，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Trend

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_trend` for Amazon 商品历史趋势查询.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-trend`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_trend.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_trend.py '{"asin":"B0CZPLV566","amz_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `asin`, `amz_site`.

Preserve the user's ASIN, marketplace, requested metrics, and time range. Do not interpolate or invent missing history points.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

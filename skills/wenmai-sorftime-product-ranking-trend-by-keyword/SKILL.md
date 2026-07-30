---
name: wenmai-sorftime-product-ranking-trend-by-keyword
description: "Sorftime Amazon 商品关键词排名趋势接口，用于查询指定 ASIN 在目标关键词下的历史排名变化。当用户提到关键词排名趋势、自然位变化、ASIN 排名监控、关键词表现、排名涨跌或 ranking trend 时触发此技能。只要需要跟踪商品在某个搜索词下的排名走势，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Ranking Trend By Keyword

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_ranking_trend_by_keyword` for Amazon 商品关键词排名趋势查询.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-ranking-trend-by-keyword`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_ranking_trend_by_keyword.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_ranking_trend_by_keyword.py '{"asin":"B0CZPLV566","keyword":"wireless earbuds","amz_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `asin`, `keyword`, `amz_site`.

Preserve the user's ASIN, keyword, marketplace, and requested time range. Do not substitute related keywords or infer missing dates.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

---
name: wenmai-sorftime-product-traffic-terms
description: "Sorftime Amazon 商品流量词反查接口，用于查询指定 ASIN 的关联流量关键词及接口支持的排名和流量指标。当用户提到 ASIN 反查、流量词、自然关键词、广告关键词、竞品关键词或 traffic terms 时触发此技能。只要需要发现为某个 Amazon 商品带来流量的关键词，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Traffic Terms

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_traffic_terms` for Amazon 商品流量关键词反查.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-traffic-terms`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_traffic_terms.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_traffic_terms.py '{"asin":"B0CZPLV566","amz_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `asin`, `amz_site`.

Preserve the user's ASIN, marketplace, filters, sorting, pagination, and requested time range. Keep keyword metrics traceable to response fields.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

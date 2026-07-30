---
name: wenmai-sorftime-product-customers-say
description: "Sorftime Amazon 评论总结接口，用于汇总指定 ASIN 的买家反馈、用户关注点及接口支持的评论洞察。当用户提到 customers say、评论总结、买家声音、用户痛点、VOC、产品优缺点或 Amazon 口碑分析时触发此技能。只要需要基于指定商品评论提炼真实用户反馈，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Customers Say

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_customers_say` for Amazon 商品评论总结.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-customers-say`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_customers_say.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_customers_say.py '{"asin":"B0CZPLV566","site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `asin`, `site`.

Preserve the user's ASIN and marketplace. Keep summaries traceable to returned fields and never invent review themes that are absent from the response.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

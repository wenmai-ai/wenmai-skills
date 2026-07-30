---
name: wenmai-sorftime-product-reviews
description: "Sorftime Amazon 商品评论接口，用于获取指定 ASIN 的评论列表、评分及接口支持的评论元数据。当用户提到 Amazon 评论抓取、买家反馈、差评分析、VOC、产品口碑或 product reviews 时触发此技能。只要需要从指定商品评论中提取真实用户声音，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Reviews

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_reviews` for Amazon 商品评论查询.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-reviews`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_reviews.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_reviews.py '{"asin":"B0CZPLV566","amz_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `asin`, `amz_site`.

Preserve the user's ASIN, marketplace, rating filters, sorting, pagination, and result limits. Never fabricate missing review content.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

---
name: wenmai-sorftime-product-variations
description: "Sorftime Amazon 商品变体查询接口，用于获取指定 ASIN 的父子变体关系和接口支持的变体信息。当用户提到父 ASIN、子 ASIN、商品变体、variation family、颜色尺码款式或 product variations 时触发此技能。只要需要查看 Amazon 商品的变体结构，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Variations

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_variations` for Amazon 商品变体查询.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-variations`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_variations.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_variations.py '{"asin":"B0CZPLV566","amz_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `asin`, `amz_site`.

Preserve the user's ASIN and marketplace. Keep parent-child relationships traceable to response fields and never infer absent variants.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

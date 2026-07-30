---
name: wenmai-sorftime-product-detail
description: "Sorftime Amazon 商品详情接口，用于查询指定 ASIN 的标题、品牌、价格、类目、销量、评分及接口支持的商品信息。当用户提到商品详情、ASIN 信息、竞品资料、产品核验、上架时间或 Sorftime product detail 时触发此技能。只要需要获取指定 Amazon 商品的详细数据，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Detail

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_detail` for Amazon 商品详情查询.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-detail`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_detail.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_detail.py '{"asin":"B0CZPLV566","amz_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `asin`, `amz_site`.

Preserve the user's ASIN and marketplace. Do not infer missing identifiers, marketplace values, or product attributes.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

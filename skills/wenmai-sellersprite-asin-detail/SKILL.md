---
name: wenmai-sellersprite-asin-detail
description: "卖家精灵 Amazon ASIN 商品详情接口，用于查询单个商品的标题、品牌、类目、价格、销量、收入、评分、BSR 及接口支持的完整指标。当用户提到 ASIN 详情、商品数据、销量收入、BSR、竞品详情、Listing 基础指标或 SellerSprite 商品查询时触发此技能。只要用户需要核验某个 Amazon ASIN 的完整经营数据，也应触发此技能。"
---

# Wenmai SellerSprite asin detail

## Purpose
Use this Skill to call the Wenmai SellerSprite standard API `asin_detail`.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/asin-detail`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/asin_detail.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/asin_detail.py '{"marketplace": "US", "asin": "B08GHW4TBS"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for parameter details, response fields, and the exact API payload.

## Parameter Rules

Required fields: `marketplace, asin`.

Preserve the user's requested marketplace, ASIN, keyword, date range, pagination, filters, and sort order. Use Amazon US / `US` only when the user does not specify a marketplace and the parameter set supports that default.

## Response Rules

Return compact tables or summaries for inspection tasks, keeping raw numbers traceable to response fields. If the API response contains `error` or a non-`OK` `code`, report the gateway message and suggest parameter corrections. Never invent missing data.

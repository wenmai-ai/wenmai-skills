---
name: wenmai-sellersprite-asin-detail-with-coupon-trend
description: "卖家精灵 ASIN 商品详情与 Coupon 趋势接口，用于查询指定 Amazon 市场中的商品完整信息及优惠券变化数据。当用户提到 ASIN 详情、Coupon 趋势、优惠券历史、促销变化、竞品折扣或 SellerSprite coupon analysis 时触发此技能。即使用户未明确提及接口名称，只要需要同时分析商品指标与优惠券趋势，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SellerSprite asin detail with coupon trend

## Purpose
Use this Skill to call the Wenmai SellerSprite standard API `asin_detail_with_coupon_trend`.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/asin-detail-with-coupon-trend`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/asin_detail_with_coupon_trend.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/asin_detail_with_coupon_trend.py '{"marketplace": "US", "asin": "B08GHW4TBS"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for parameter details, response fields, and the exact API payload.

## Parameter Rules

Required fields: `marketplace, asin`.

Preserve the user's requested marketplace, ASIN, keyword, date range, pagination, filters, and sort order. Use Amazon US / `US` only when the user does not specify a marketplace and the parameter set supports that default.

## Response Rules

Return compact tables or summaries for inspection tasks, keeping raw numbers traceable to response fields. If the API response contains `error` or a non-`OK` `code`, report the gateway message and suggest parameter corrections. Never invent missing data.

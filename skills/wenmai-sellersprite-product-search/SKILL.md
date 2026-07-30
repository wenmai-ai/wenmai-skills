---
name: wenmai-sellersprite-product-search
description: "卖家精灵 Amazon 商品搜索与商品池筛选接口，可按关键词、类目、销量、销售额、BSR、价格、评分、卖家、品牌、徽章和配送方式等条件筛选商品。当用户提到 Amazon 搜品、商品池、条件选品、竞品筛选、类目商品过滤或 SellerSprite product research 时触发此技能。只要用户希望按经营指标寻找候选 ASIN，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SellerSprite Product Search

## Purpose
Use this Skill to fetch 卖家精灵商品筛选 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/product-research`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sellersprite_product_search.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sellersprite_product_search.py '{"request": {"marketplace": "US", "keyword": "water bottle", "page": 1, "size": 50, "order": {"field": "total_units", "desc": true}}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `request`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

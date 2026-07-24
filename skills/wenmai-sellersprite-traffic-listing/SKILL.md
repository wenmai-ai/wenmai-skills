---
name: wenmai-sellersprite-traffic-listing
description: "卖家精灵 Amazon 关联商品接口，用于查询指定 ASIN 在站内关联的 Listing，分析商品间的竞品和流量关联关系。当用户提到关联商品、相似 Listing、ASIN 竞品关系、流量关联、站内推荐商品或 SellerSprite traffic listing 时触发此技能。只要用户需要扩展某个 ASIN 的关联竞品池，也应触发此技能。"
---

# Wenmai SellerSprite traffic listing

## Purpose
Use this Skill to call the Wenmai SellerSprite standard API `traffic_listing`.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/traffic-listing`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/traffic_listing.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/traffic_listing.py '{"request": {"asinList": ["B08GHW4TBS"], "marketplace": "US", "relations": ["vav"]}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for parameter details, response fields, and the exact API payload.

## Parameter Rules

Required fields: `request, request.marketplace, request.asinList, request.relations`.

Preserve the user's requested marketplace, ASIN, keyword, date range, pagination, filters, and sort order. Use Amazon US / `US` only when the user does not specify a marketplace and the parameter set supports that default.

## Response Rules

Return compact tables or summaries for inspection tasks, keeping raw numbers traceable to response fields. If the API response contains `error` or a non-`OK` `code`, report the gateway message and suggest parameter corrections. Never invent missing data.

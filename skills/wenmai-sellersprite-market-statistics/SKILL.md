---
name: wenmai-sellersprite-market-statistics
description: "卖家精灵 Amazon 类目节点统计接口，用于获取指定节点的 Top N 市场汇总、新品指标、平均销量、销售额、价格、评分和 BSR。当用户提到类目节点统计、Top N 商品、新品表现、节点均值、类目基准或 SellerSprite market statistics 时触发此技能。只要用户需要对一个明确的 Amazon 类目节点做量化评估，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai SellerSprite Market Statistics

## Purpose
Use this Skill to fetch 卖家精灵类目统计 data through Wenmai standard API.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/market-research-statistics`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/sellersprite_market_statistics.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/sellersprite_market_statistics.py '{"request": {"marketplace": "US", "nodeIdPath": "172282:281407", "topN": 10}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` when you need parameter details, field meanings, or the exact API payload.

## Parameter Rules

Required top-level fields: `request`.

Default marketplace assumptions: use Amazon US / `US` / domain `1` unless the user specifies another marketplace. Preserve the user's requested time window, ASIN list, keyword, filters, pagination, and sort order.

## Response Rules

Present the returned data in compact tables when the user asks for inspection or comparison. For long arrays, summarize the most decision-relevant rows first, then offer to continue with more rows. Keep raw numbers traceable to the response fields.

If the API response contains an `error` or a non-`OK` `code`, report the message and suggest parameter corrections. Never invent missing data.

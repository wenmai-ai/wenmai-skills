---
name: wenmai-sellersprite-review
description: "卖家精灵 Amazon 评论接口，用于按 ASIN 查询评论标题、正文、评分、评论人、评论时间及接口支持的评价数据。当用户提到 Amazon 评论、ASIN 评价、差评分析、用户反馈、竞品口碑、VOC 或 SellerSprite review 时触发此技能。即使用户未明确提及卖家精灵，只要需要获取指定 Amazon 商品的评论列表，也应触发此技能。"
---

# Wenmai SellerSprite review

## Purpose
Use this Skill to call the Wenmai SellerSprite standard API `review`.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sellersprite/review`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/review.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/review.py '{"marketplace": "US", "asin": "B08GHW4TBS"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for parameter details, response fields, and the exact API payload.

## Parameter Rules

Required fields: `marketplace, asin`.

Preserve the user's requested marketplace, ASIN, keyword, date range, pagination, filters, and sort order. Use Amazon US / `US` only when the user does not specify a marketplace and the parameter set supports that default.

## Response Rules

Return compact tables or summaries for inspection tasks, keeping raw numbers traceable to response fields. If the API response contains `error` or a non-`OK` `code`, report the gateway message and suggest parameter corrections. Never invent missing data.

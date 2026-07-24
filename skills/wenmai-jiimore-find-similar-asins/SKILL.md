---
name: wenmai-jiimore-find-similar-asins
description: "JIIMORE ABA 相似商品接口，用于基于 ABA 关联关系查找与指定 Amazon ASIN 相似的商品。当用户提到相似 ASIN、ABA 相似商品、关联竞品、替代商品、相似竞品或扩展竞品样本时触发此技能。只要用户希望利用 ABA 数据寻找相似 Amazon 商品，也应触发此技能。"
---

# Wenmai JIIMORE find similar asins

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_find_similar_asins` for 查询 ABA 相似商品.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/similar-asins`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_find_similar_asins.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_find_similar_asins.py '{"request": {"asins": ["B09PCSR9SX"], "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.asins`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

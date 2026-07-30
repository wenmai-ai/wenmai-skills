---
name: wenmai-jiimore-find-same-niche-asins
description: "JIIMORE 同细分市场商品接口，用于根据 Amazon ASIN 查找同一 niche 中的其他商品，扩展直接竞品池。当用户提到同 niche 商品、同细分市场竞品、相同赛道 ASIN、竞品扩展或细分市场对标时触发此技能。只要用户需要围绕一个 ASIN 寻找同市场商品，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai JIIMORE find same niche asins

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_find_same_niche_asins` for 查询同细分市场商品.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/same-niche-asins`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_find_same_niche_asins.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_find_same_niche_asins.py '{"request": {"asin": "B09PCSR9SX", "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.asin`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

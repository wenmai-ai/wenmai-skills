---
name: wenmai-jiimore-get-niche-asins
description: "JIIMORE 细分市场商品接口，用于查询指定 Amazon niche 中的商品或 ASIN，建立市场商品池并识别竞争者。当用户提到 niche 商品、细分市场 ASIN、赛道商品池、市场参与者、细分竞品或 niche products 时触发此技能。只要用户需要获取某个细分市场中的 Amazon 商品列表，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai JIIMORE get niche asins

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_get_niche_asins` for 查询细分市场商品.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/niche-asins`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_get_niche_asins.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_get_niche_asins.py '{"request": {"nicheId": "sample-niche", "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.nicheId`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

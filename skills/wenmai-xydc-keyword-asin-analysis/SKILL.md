---
name: wenmai-xydc-keyword-asin-analysis
description: "Use when users need the Wenmai XYDC standard API `get_keyword_asin_analysis` for 关键词分析列表（最近天）, including traceable Amazon ASIN, keyword, country, date, rank, traffic, order, BSR, ABA, variation, or advertising trend data as documented for this endpoint. Sends user parameters as a JSON POST body to `/wmapi/v1/xydc/get-keyword-asin-analysis` and returns raw gateway data for ecommerce operations, competitor monitoring, keyword research, or reporting."
metadata:
  version: "1.0.0"
---

# Wenmai XYDC Keyword ASIN Analysis

## Purpose
Use this Skill to call the Wenmai XYDC standard API `get_keyword_asin_analysis` for 关键词分析列表（最近天）.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/xydc/get-keyword-asin-analysis`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/xydc_keyword_asin_analysis.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY="replace-with-real-wenmai-api-key"
python3 scripts/xydc_keyword_asin_analysis.py '{"keyword": "usb c cable", "country": "US", "page": 1, "page_size": 20}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for parameter details, response fields, and the exact API payload.

## Parameter Rules

Required fields: `country, keyword`.

Preserve the user's requested ASINs, keywords, marketplace country code, dates, months, weeks, pagination, and filters. Do not expand or shift a query window unless the user explicitly asks.

## Response Rules

Summarize list rows in compact tables, prioritizing the most decision-relevant fields and preserving pagination fields. Keep raw field names, IDs, dates, ASINs, keywords, ranks, and scores traceable to response fields.

If the API response contains `error` or a non-`OK` `code`, report the gateway message and `requestId` if present, then suggest parameter corrections. Never invent missing data.

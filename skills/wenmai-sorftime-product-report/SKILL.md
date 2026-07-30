---
name: wenmai-sorftime-product-report
description: "Sorftime Amazon 产品分析报告接口，用于获取指定 ASIN 的综合分析和接口支持的经营指标。当用户提到产品分析报告、ASIN 诊断、竞品报告、商品表现评估、选品报告或 product report 时触发此技能。只要需要对单个 Amazon 商品进行结构化分析，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Product Report

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `product_report` for Amazon 产品分析报告查询.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/product-report`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/product_report.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/product_report.py '{"asin":"B0CZPLV566","amz_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `asin`, `amz_site`.

Preserve the user's ASIN and marketplace. Keep every conclusion traceable to returned report fields and do not fill gaps with assumptions.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

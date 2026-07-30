---
name: wenmai-sorftime-keyword-extends
description: "Sorftime Amazon 延伸关键词接口，用于围绕种子词扩展相关搜索词和接口支持的关键词指标。当用户提到关键词扩展、拓词、长尾词、相关词、Amazon 搜索词研究或 keyword expansion 时触发此技能。只要需要从一个种子词建立候选关键词池，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime Keyword Extends

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `keyword_extends` for Amazon 延伸关键词查询.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/keyword-extends`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/keyword_extends.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/keyword_extends.py '{"keyword":"wireless earbuds","keyword_support_site":"US"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `keyword`, `keyword_support_site`.

Preserve the user's seed keyword, marketplace, filters, sorting, pagination, and result limits. Do not replace the requested marketplace.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

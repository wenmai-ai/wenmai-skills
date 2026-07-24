---
name: wenmai-jiimore-expand-aba-keywords-by-keyword
description: "JIIMORE ABA 关键词扩展接口，用于根据一个种子关键词发现相关 Amazon ABA 搜索词并扩充关键词池。当用户提到 ABA 扩词、关键词拓展、相关搜索词、选品关键词、搜索词机会或按关键词找 ABA 词时触发此技能。即使用户未明确提及 JIIMORE，只要需要围绕种子词扩展 ABA 关键词，也应触发此技能。"
---

# Wenmai JIIMORE expand aba keywords by keyword

## Purpose
Use this Skill to call the Wenmai JIIMORE standard API `jiimore_expand_aba_keywords_by_keyword` for 按关键词扩展 ABA 关键词.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/jiimore/aba-keywords-by-keyword`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_expand_aba_keywords_by_keyword.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_expand_aba_keywords_by_keyword.py '{"request": {"keywords": ["neck fan"], "countryCode": "US"}}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required fields: `request, request.keywords`.

Preserve the user's ASINs, keywords, marketplace country code, niche ID, ranking window, pagination, filters, and sort order. Do not flatten the required `request` object.

## Response Rules

Return compact tables or summaries while keeping values traceable to response fields. If the API returns `error` or a non-`OK` code, report the gateway message and suggest parameter corrections. Never invent missing data.

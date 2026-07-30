---
name: wenmai-sorftime-ali1688-product-search-from-image
description: "Sorftime 1688 以图搜款接口，用于根据公开图片 URL 查找相同或相似的 1688 货源商品。当用户提到 1688 以图搜货、图片找同款、反向搜图、供应链找款或 image search 时触发此技能。只要需要用产品图片定位 1688 候选货源，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai Sorftime 1688 Product Search From Image

## Purpose
Use this Skill to call the Wenmai Sorftime standard API `ali1688_product_search_from_image` for 1688 以图搜索相同或相似商品.

The Skill calls exactly one fixed standard API endpoint:

- Endpoint: `POST /wmapi/v1/sorftime/ali1688-product-search-from-image`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/ali1688_product_search_from_image.py`

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，把复制的 key 导出为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/ali1688_product_search_from_image.py '{"image_url":"https://cbu01.alicdn.com/img/ibank/O1CN01HrY28j1LS4eMNQV1G_!!3086091297-0-cib.jpg"}'
```

The script prints the raw Wenmai API response as formatted JSON. Read `references/api.md` for the exact request and response contract.

## Parameter Rules

Required top-level fields: `image_url`.

Preserve the user's image URL, filters, sorting, pagination, and result limits. Never invent or silently replace the source image.

## Response Rules

Present returned data in compact tables or summaries while keeping values traceable to response fields. For long arrays, summarize the most decision-relevant rows first.

If the API response contains an `error` or a non-`OK` `code`, report the message and `requestId` if present, then suggest parameter corrections. Never expose the API key or invent missing data.

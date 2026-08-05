# SIF ASIN Traffic Summary

SIF ASIN 流量概览接口，用于汇总 Listing 的自然与广告流量占比、SP／SB／SBV 渠道结构、推荐流量来源和整体流量健康度。

固定调用 Wenmai SIF standard API `ops_get_listing_traffic_overview`，不接受动态端点或其他操作。

- Provider: SIF
- Platform: Amazon（亚马逊）
- Operation: `ops_get_listing_traffic_overview`
- Endpoint: `POST /wmapi/v1/sif/ops-get-listing-traffic-overview`
- Script: `scripts/sif_asin_summary.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

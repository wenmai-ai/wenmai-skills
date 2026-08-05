# SIF ads_get_campaign_contribution_breakdown

SIF Amazon（亚马逊） 功能：查询某 campaign 在单个自然周内的贡献明细，支持按 keyword 或 ad_group 维度拆解接口，通过固定 Wenmai standard API `ads_get_campaign_contribution_breakdown` 返回可追溯的原始网关数据。

固定调用 Wenmai SIF standard API `ads_get_campaign_contribution_breakdown`，不接受动态端点或其他操作。

- Provider: SIF
- Platform: Amazon（亚马逊）
- Operation: `ads_get_campaign_contribution_breakdown`
- Endpoint: `POST /wmapi/v1/sif/ads-get-campaign-contribution-breakdown`
- Script: `scripts/ads_get_campaign_contribution_breakdown.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

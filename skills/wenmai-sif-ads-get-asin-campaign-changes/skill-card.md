# SIF ads_get_asin_campaign_changes

SIF Amazon（亚马逊） 功能：查询某 ASIN 在历史各周内新上线的 campaign 变更事件，即 campaign_created 事件列表接口，通过固定 Wenmai standard API `ads_get_asin_campaign_changes` 返回可追溯的原始网关数据。

固定调用 Wenmai SIF standard API `ads_get_asin_campaign_changes`，不接受动态端点或其他操作。

- Provider: SIF
- Platform: Amazon（亚马逊）
- Operation: `ads_get_asin_campaign_changes`
- Endpoint: `POST /wmapi/v1/sif/ads-get-asin-campaign-changes`
- Script: `scripts/ads_get_asin_campaign_changes.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- Remote state: 此操作会修改远程状态；执行前必须复核最终完整请求及全部目标/作用域字段。
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

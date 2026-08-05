# SIF Keyword Traffic

SIF 关键词流量与竞争分析接口，用于查看头部 ASIN 的流量份额、自然／SP／SB／SBV 占比、集中度、竞争位置和关键词机会。

固定调用 Wenmai SIF standard API `market_get_keyword_competition`，不接受动态端点或其他操作。

- Provider: SIF
- Platform: Amazon（亚马逊）
- Operation: `market_get_keyword_competition`
- Endpoint: `POST /wmapi/v1/sif/market-get-keyword-competition`
- Script: `scripts/sif_keyword_traffic.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

# 卖家精灵（SellerSprite） traffic source

卖家精灵（SellerSprite） Amazon 流量来源分析接口，用于从 ASIN 或关键词维度查看流量关键词结构和接口支持的来源指标。

固定调用 Wenmai 卖家精灵（SellerSprite） standard API `traffic_source`，不接受动态端点或其他操作。

- Provider: 卖家精灵（SellerSprite）
- Platform: Amazon（亚马逊）
- Operation: `traffic_source`
- Endpoint: `POST /wmapi/v1/sellersprite/traffic-source`
- Script: `scripts/traffic_source.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

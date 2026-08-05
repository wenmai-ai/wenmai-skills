# 卖家精灵（SellerSprite） keyword_order

卖家精灵（SellerSprite） Amazon（亚马逊） 基于 ASIN 的关键词反查工具，用于分析某个或多个 ASIN接口，通过固定 Wenmai standard API `keyword_order` 返回可追溯的原始网关数据。

固定调用 Wenmai 卖家精灵（SellerSprite） standard API `keyword_order`，不接受动态端点或其他操作。

- Provider: 卖家精灵（SellerSprite）
- Platform: Amazon（亚马逊）
- Operation: `keyword_order`
- Endpoint: `POST /wmapi/v1/sellersprite/keyword-order`
- Script: `scripts/keyword_order.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

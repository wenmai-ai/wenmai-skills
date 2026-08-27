# FastMoss product_creator_analysis（TikTok Shop 数据）

FastMoss TikTok Shop 查看是哪些达人在卖这个商品，通过固定 Wenmai standard API 返回可追溯的原始网关数据。

固定调用 Wenmai FastMoss standard API `product_creator_analysis`，不接受动态端点或其他操作。

- Provider: FastMoss
- Platform: TIKTOK（TikTok Shop）
- Operation: `product_creator_analysis`
- Endpoint: `POST /wmapi/v1/fastmoss/product-creator-analysis`
- Script: `scripts/product_creator_analysis.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

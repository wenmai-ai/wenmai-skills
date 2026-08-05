# 卖家精灵（SellerSprite） Product Search

卖家精灵（SellerSprite） Amazon 商品搜索与商品池筛选接口，可按关键词、类目、销量、销售额、BSR、价格、评分、卖家、品牌、徽章和配送方式等条件筛选商品。

固定调用 Wenmai 卖家精灵（SellerSprite） standard API `product_research`，不接受动态端点或其他操作。

- Provider: 卖家精灵（SellerSprite）
- Platform: Amazon（亚马逊）
- Operation: `product_research`
- Endpoint: `POST /wmapi/v1/sellersprite/product-research`
- Script: `scripts/sellersprite_product_search.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

# 卖家精灵（SellerSprite） asin detail

卖家精灵（SellerSprite） Amazon ASIN 商品详情接口，用于查询单个商品的标题、品牌、类目、价格、销量、收入、评分、BSR 及接口支持的完整指标。

固定调用 Wenmai 卖家精灵（SellerSprite） standard API `asin_detail`，不接受动态端点或其他操作。

- Provider: 卖家精灵（SellerSprite）
- Platform: Amazon（亚马逊）
- Operation: `asin_detail`
- Endpoint: `POST /wmapi/v1/sellersprite/asin-detail`
- Script: `scripts/asin_detail.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

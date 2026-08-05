# 卖家精灵（SellerSprite） asin detail with coupon trend

卖家精灵（SellerSprite） ASIN 商品详情与 Coupon 趋势接口，用于查询指定 Amazon 市场中的商品完整信息及优惠券变化数据。

固定调用 Wenmai 卖家精灵（SellerSprite） standard API `asin_detail_with_coupon_trend`，不接受动态端点或其他操作。

- Provider: 卖家精灵（SellerSprite）
- Platform: Amazon（亚马逊）
- Operation: `asin_detail_with_coupon_trend`
- Endpoint: `POST /wmapi/v1/sellersprite/asin-detail-with-coupon-trend`
- Script: `scripts/asin_detail_with_coupon_trend.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

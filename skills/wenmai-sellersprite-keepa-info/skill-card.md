# 卖家精灵（SellerSprite） keepa_info

卖家精灵（SellerSprite） Amazon（亚马逊） 获取指定 Amazon ASIN 的完整商品画像及多维度历史趋势数据(不含有销量数据)接口，通过固定 Wenmai standard API `keepa_info` 返回可追溯的原始网关数据。

固定调用 Wenmai 卖家精灵（SellerSprite） standard API `keepa_info`，不接受动态端点或其他操作。

- Provider: 卖家精灵（SellerSprite）
- Platform: Amazon（亚马逊）
- Operation: `keepa_info`
- Endpoint: `POST /wmapi/v1/sellersprite/keepa-info`
- Script: `scripts/keepa_info.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

# 极目数据（JIIMORE）Amazon 同细分市场商品

极目数据（JIIMORE）Amazon 同细分市场商品接口，按单个 ASIN 查找同一 niche 的商品，并返回父 ASIN、价格、评分、评论量、7/30/360 日点击与转化及同市场命中计数。

固定调用 Wenmai 极目数据（JIIMORE） standard API `jiimore_find_same_niche_asins`，不接受动态端点或其他操作。

- Provider: 极目数据（JIIMORE）
- Platform: Amazon（亚马逊）
- Operation: `jiimore_find_same_niche_asins`
- Endpoint: `POST /wmapi/v1/jiimore/same-niche-asins`
- Script: `scripts/jiimore_find_same_niche_asins.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

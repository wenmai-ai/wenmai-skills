# 极目数据（JIIMORE）Amazon 细分市场详情

极目数据（JIIMORE）Amazon 细分市场详情接口，按 niche ID 返回市场需求、价格区间、商品/品牌数量、多周期搜索/销量/点击、转化与集中度、广告/新品/退货/CPC、趋势、潜力信号及正负面评论洞察。

固定调用 Wenmai 极目数据（JIIMORE） standard API `jiimore_get_niche_details`，不接受动态端点或其他操作。

- Provider: 极目数据（JIIMORE）
- Platform: Amazon（亚马逊）
- Operation: `jiimore_get_niche_details`
- Endpoint: `POST /wmapi/v1/jiimore/niche-details`
- Script: `scripts/jiimore_get_niche_details.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

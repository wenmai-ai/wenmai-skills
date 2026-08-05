# 极目数据（JIIMORE）Amazon 关键词关联细分市场

极目数据（JIIMORE）Amazon 关键词关联细分市场接口，按搜索词返回 niche 名称、需求、价格区间、商品/品牌数量、多周期搜索量/销量/点击、转化率、集中度、广告占比、新品成功率、退货率、CPC 和趋势。

固定调用 Wenmai 极目数据（JIIMORE） standard API `jiimore_find_niches_by_keyword`，不接受动态端点或其他操作。

- Provider: 极目数据（JIIMORE）
- Platform: Amazon（亚马逊）
- Operation: `jiimore_find_niches_by_keyword`
- Endpoint: `POST /wmapi/v1/jiimore/niches-by-keyword`
- Script: `scripts/jiimore_find_niches_by_keyword.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

# 极目数据（JIIMORE）Amazon ASIN 商品详情

极目数据（JIIMORE）Amazon ASIN 商品详情接口，支持一次查询 1～20 个 ASIN，返回实际市场、标题、图片、当前价格与币种、FBA 和推荐费、点击与转化指标、Highlights、Best Seller Rank，以及数据完整性和未解析 ASIN 警告。

固定调用 Wenmai 极目数据（JIIMORE） standard API `jiimore_get_asin_details`，不接受动态端点或其他操作。

- Provider: 极目数据（JIIMORE）
- Platform: Amazon（亚马逊）
- Operation: `jiimore_get_asin_details`
- Endpoint: `POST /wmapi/v1/jiimore/asin-details`
- Script: `scripts/jiimore_get_asin_details.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

# 极目数据（JIIMORE）Amazon 关键词批量指标

极目数据（JIIMORE）Amazon 关键词批量指标接口，支持一次查询 1～20 个关键词，返回搜索量、点击、销量、搜索/点击转化、CPC/CPR、ABA 排名变化、增长率、Top 3 集中度及关联 niche。

固定调用 Wenmai 极目数据（JIIMORE） standard API `jiimore_search_keywords_batch`，不接受动态端点或其他操作。

- Provider: 极目数据（JIIMORE）
- Platform: Amazon（亚马逊）
- Operation: `jiimore_search_keywords_batch`
- Endpoint: `POST /wmapi/v1/jiimore/keywords-batch`
- Script: `scripts/jiimore_search_keywords_batch.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

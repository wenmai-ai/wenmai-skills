# 极目数据（JIIMORE）Amazon ABA 关键词扩展

极目数据（JIIMORE）Amazon ABA 关键词扩展接口，支持按 1～20 个种子词查询相关搜索词、7 日搜索/点击/销量与转化、CPC/CPR、ABA 排名变化、流量集中度、关联细分市场和竞争/广告成本信号。

固定调用 Wenmai 极目数据（JIIMORE） standard API `jiimore_expand_aba_keywords_by_keyword`，不接受动态端点或其他操作。

- Provider: 极目数据（JIIMORE）
- Platform: Amazon（亚马逊）
- Operation: `jiimore_expand_aba_keywords_by_keyword`
- Endpoint: `POST /wmapi/v1/jiimore/aba-keywords-by-keyword`
- Script: `scripts/jiimore_expand_aba_keywords_by_keyword.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

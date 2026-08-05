# 极目数据（JIIMORE）Amazon 细分市场关键词

极目数据（JIIMORE）Amazon 细分市场关键词接口，按 niche ID 返回搜索词、搜索量、点击、销量、转化、CPC/CPR、ABA 排名变化、集中度及关键词在细分市场中的 90 日点击/搜索份额。

固定调用 Wenmai 极目数据（JIIMORE） standard API `jiimore_get_niche_keywords`，不接受动态端点或其他操作。

- Provider: 极目数据（JIIMORE）
- Platform: Amazon（亚马逊）
- Operation: `jiimore_get_niche_keywords`
- Endpoint: `POST /wmapi/v1/jiimore/niche-keywords`
- Script: `scripts/jiimore_get_niche_keywords.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、包装层、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留存在的 `requestId` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数、市场或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

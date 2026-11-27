# ScrapeCreators Reddit 全站搜索 Reddit 帖子或评论

ScrapeCreators Reddit 全站搜索 Reddit 帖子或评论接口，固定调用 Wenmai standard API `scrapecreators_reddit_search`，不接受动态端点或其他操作。

- Provider: ScrapeCreators
- Platform: Reddit
- Operation: `scrapecreators_reddit_search`
- Endpoint: `POST /wmapi/v1/scrapecreators/reddit-search`
- Parent: `$wenmai-scrapecreators-reddit`
- Script: `modules/search/scripts/search.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯，并保留存在的 `requestId`、`costCredit` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

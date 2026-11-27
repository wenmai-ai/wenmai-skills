# ScrapeCreators Instagram 获取 Instagram 帖子总数

ScrapeCreators Instagram 获取 Instagram 帖子总数接口，固定调用 Wenmai standard API `scrapecreators_instagram_profile_post_count`，不接受动态端点或其他操作。

- Provider: ScrapeCreators
- Platform: Instagram
- Operation: `scrapecreators_instagram_profile_post_count`
- Endpoint: `POST /wmapi/v1/scrapecreators/instagram-profile-post-count`
- Parent: `$wenmai-scrapecreators-instagram`
- Script: `modules/profile-post-count/scripts/profile_post_count.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯，并保留存在的 `requestId`、`costCredit` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

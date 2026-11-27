# ScrapeCreators YouTube 获取 YouTube 视频评论

ScrapeCreators YouTube 获取 YouTube 视频评论接口，固定调用 Wenmai standard API `scrapecreators_youtube_video_comments`，不接受动态端点或其他操作。

- Provider: ScrapeCreators
- Platform: YouTube
- Operation: `scrapecreators_youtube_video_comments`
- Endpoint: `POST /wmapi/v1/scrapecreators/youtube-video-comments`
- Parent: `$wenmai-scrapecreators-youtube`
- Script: `modules/video-comments/scripts/video_comments.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯，并保留存在的 `requestId`、`costCredit` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

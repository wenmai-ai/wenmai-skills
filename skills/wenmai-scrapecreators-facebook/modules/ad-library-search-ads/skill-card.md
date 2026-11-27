# ScrapeCreators Facebook 按关键词搜索 Facebook 广告库

ScrapeCreators Facebook 按关键词搜索 Facebook 广告库接口，固定调用 Wenmai standard API `scrapecreators_facebook_ad_library_search_ads`，不接受动态端点或其他操作。

- Provider: ScrapeCreators
- Platform: Facebook
- Operation: `scrapecreators_facebook_ad_library_search_ads`
- Endpoint: `POST /wmapi/v1/scrapecreators/facebook-ad-library-search-ads`
- Parent: `$wenmai-scrapecreators-facebook`
- Script: `modules/ad-library-search-ads/scripts/ad_library_search_ads.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、默认值和限制以 API 契约为准
- Output: 原始 JSON 响应；摘要必须可追溯，并保留存在的 `requestId`、`costCredit` 和 `warnings`
- Limitations: 不接受动态端点；不静默截断或补造数据；不绕过上游额度、参数或分页限制
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

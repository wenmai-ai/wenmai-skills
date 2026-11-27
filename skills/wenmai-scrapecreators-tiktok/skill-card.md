# TikTok 达人与爆款内容调研

一个顶层 Skill 索引 21 个 TikTok 社媒接口：搜索、主页、作品、评论、粉丝、直播和音乐。

- Provider: ScrapeCreators
- Platform: TikTok
- Runtime: 顶层 `$wenmai-scrapecreators-tiktok`，子 Skill 在 `modules/`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Billing: 普通接口 3 积分；观众分布 67 积分
- Limitations: 不作为 21 个独立顶层 Skill 安装；按用户需求只调用所需接口；不含 TikTok Shop
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

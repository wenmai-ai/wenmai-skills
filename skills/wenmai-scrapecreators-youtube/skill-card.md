# YouTube 频道与爆款内容调研

一个顶层 Skill 索引 18 个 YouTube 社媒接口：搜索、频道、视频、字幕、评论和 Shorts。按需调用；普通 3 积分。

- Provider: ScrapeCreators
- Platform: YouTube
- Runtime: 顶层 `$wenmai-scrapecreators-youtube`，子 Skill 在 `modules/`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Billing: 普通接口 3 积分；`includeExtras` 不要当默认
- Limitations: 不作为 18 个独立顶层 Skill 安装；按用户需求只调用所需接口；不含 Facebook 和 TikTok Shop
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

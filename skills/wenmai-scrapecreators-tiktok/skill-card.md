# TikTok 达人与爆款内容调研

卖家做 TikTok 达人筛选、爆款拆解和评论 VOC 时用。覆盖搜索、主页地区、作品、粉丝、评论字幕、直播和音乐；按需只打需要的接口。普通查询 2 积分，观众分布 36 积分。不含 TikTok Shop。

- Provider: ScrapeCreators
- Platform: TikTok
- Runtime: 顶层 `$wenmai-scrapecreators-tiktok`，子 Skill 在 `modules/`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Billing: 普通接口 2 积分；观众分布 36 积分
- Limitations: 不作为 21 个独立顶层 Skill 安装；按用户需求只调用所需接口；不含 TikTok Shop
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

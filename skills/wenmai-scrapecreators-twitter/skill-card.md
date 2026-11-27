# Twitter 帖子搜索调研

一个顶层 Skill 索引 7 个 Twitter / X 社媒接口：帖子搜索、账号资料、热门推文、推文详情、视频转写和社群。按需调用；普通 2 积分。

- Provider: ScrapeCreators
- Platform: Twitter / X
- Runtime: 顶层 `$wenmai-scrapecreators-twitter`，子 Skill 在 `modules/`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Billing: 普通接口 2 积分；长转写和 trim 不要当默认
- Limitations: 不作为 7 个独立顶层 Skill 安装；按用户需求只调用所需接口
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

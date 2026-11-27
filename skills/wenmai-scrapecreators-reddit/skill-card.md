# Reddit 社群与帖子调研

一个顶层 Skill 索引 7 个 Reddit 社媒接口：Subreddit 详情、帖子、评论和搜索。按需调用；普通 2 积分。

- Provider: ScrapeCreators
- Platform: Reddit
- Runtime: 顶层 `$wenmai-scrapecreators-reddit`，子 Skill 在 `modules/`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Billing: 普通接口 2 积分；trim 不要当默认
- Limitations: 不作为 7 个独立顶层 Skill 安装；按用户需求只调用所需接口
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

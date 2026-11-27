# Facebook 主页与广告调研

一个顶层 Skill 索引 23 个 Facebook 社媒接口：主页、帖子、群组、Marketplace 和广告库。按需调用；普通 3 积分。

- Provider: ScrapeCreators
- Platform: Facebook
- Runtime: 顶层 `$wenmai-scrapecreators-facebook`，子 Skill 在 `modules/`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Billing: 普通接口 3 积分；长字幕、get_transcript 和 trim 不要当默认
- Limitations: 不作为 23 个独立顶层 Skill 安装；按用户需求只调用所需接口
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

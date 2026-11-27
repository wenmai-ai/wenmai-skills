# Instagram 达人与内容调研

一个顶层 Skill 索引 19 个 Instagram 社媒接口：搜索、主页、帖子、Reels 和评论。不含字幕转写。Popular 只用专题词。

- Provider: ScrapeCreators
- Platform: Instagram
- Runtime: 顶层 `$wenmai-scrapecreators-instagram`，子 Skill 在 `modules/`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Billing: 普通接口 3 积分；贵参数不要当默认
- Limitations: 不作为 19 个独立顶层 Skill 安装；按用户需求只调用所需接口；不含 Facebook 和字幕转写；Popular 只用专题词，不要拿品牌名
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/

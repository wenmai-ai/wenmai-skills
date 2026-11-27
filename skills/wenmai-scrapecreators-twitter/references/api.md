# Wenmai SCRAPECREATORS Twitter 套件 API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 顶层 Skill 是索引目录，真正请求发到下表 7 个 `/wmapi/v1/scrapecreators/twitter-*` 端点。不要因为套件有 7 个接口就全打一遍。
- 认证：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- 凭据与充值：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`
- 稳卖积分：普通接口成功为 2。贵参数会提高官方成本，默认不要开。

## 接口索引

| 子 Skill | 接口代码 | 请求地址 | 稳卖积分 | 详细契约 |
|---|---|---|---|---|
| 搜索 Google 索引的公开 Twitter / X 帖子 | `scrapecreators_twitter_search_posts` | `/wmapi/v1/scrapecreators/twitter-search-posts` | 2 | [modules/search-posts/references/api.md](../modules/search-posts/references/api.md) |
| 获取 Twitter / X 用户资料 | `scrapecreators_twitter_profile` | `/wmapi/v1/scrapecreators/twitter-profile` | 2 | [modules/profile/references/api.md](../modules/profile/references/api.md) |
| 获取用户主页上的热门推文 | `scrapecreators_twitter_user_tweets` | `/wmapi/v1/scrapecreators/twitter-user-tweets` | 2 | [modules/user-tweets/references/api.md](../modules/user-tweets/references/api.md) |
| 获取单条 Twitter / X 推文详情 | `scrapecreators_twitter_tweet` | `/wmapi/v1/scrapecreators/twitter-tweet` | 2 | [modules/tweet/references/api.md](../modules/tweet/references/api.md) |
| 获取视频推文的 AI 转写 | `scrapecreators_twitter_tweet_transcript` | `/wmapi/v1/scrapecreators/twitter-tweet-transcript` | 2 | [modules/tweet-transcript/references/api.md](../modules/tweet-transcript/references/api.md) |
| 获取 Twitter / X 社群详情 | `scrapecreators_twitter_community` | `/wmapi/v1/scrapecreators/twitter-community` | 2 | [modules/community/references/api.md](../modules/community/references/api.md) |
| 获取 Twitter / X 社群帖子 | `scrapecreators_twitter_community_tweets` | `/wmapi/v1/scrapecreators/twitter-community-tweets` | 2 | [modules/community-tweets/references/api.md](../modules/community-tweets/references/api.md) |

每个子 Skill 的请求参数、响应字段、示例和 curl 写在对应模块的 `references/api.md`，不要在索引页发明字段。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 打开对应子 Skill 的 `references/api.md` 核对必填字段、handle、推文链接、社群链接和 cursor。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。各模块的官方来源链接见对应接口参考。响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

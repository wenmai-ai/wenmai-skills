# Wenmai SCRAPECREATORS Instagram 套件 API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 顶层 Skill 是索引目录，真正请求发到下表 19 个 `/wmapi/v1/scrapecreators/instagram-**` 端点。不要调用 media-transcript。search-popular 只用专题词。
- 认证：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- 凭据与充值：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`
- 稳卖积分：普通接口成功为 2。贵参数会提高官方成本，默认不要开。

## 接口索引

| 子 Skill | 接口代码 | 请求地址 | 稳卖积分 | 详细契约 |
|---|---|---|---|---|
| 搜索 Instagram 用户、话题、地点和关键词 | `scrapecreators_instagram_search` | `/wmapi/v1/scrapecreators/instagram-search` | 2 | [modules/search/references/api.md](../modules/search/references/api.md) |
| 按热门话题搜索 Instagram 帖子 | `scrapecreators_instagram_search_popular` | `/wmapi/v1/scrapecreators/instagram-search-popular` | 2 | [modules/search-popular/references/api.md](../modules/search-popular/references/api.md) |
| 按话题搜索 Instagram 帖子 | `scrapecreators_instagram_search_hashtag` | `/wmapi/v1/scrapecreators/instagram-search-hashtag` | 2 | [modules/search-hashtag/references/api.md](../modules/search-hashtag/references/api.md) |
| 搜索 Instagram 用户主页 | `scrapecreators_instagram_search_profiles` | `/wmapi/v1/scrapecreators/instagram-search-profiles` | 2 | [modules/search-profiles/references/api.md](../modules/search-profiles/references/api.md) |
| 按关键词搜索 Instagram Reels | `scrapecreators_instagram_reels_search` | `/wmapi/v1/scrapecreators/instagram-reels-search` | 2 | [modules/reels-search/references/api.md](../modules/reels-search/references/api.md) |
| 获取近 7 天热门 Reels | `scrapecreators_instagram_reels_trending` | `/wmapi/v1/scrapecreators/instagram-reels-trending` | 2 | [modules/reels-trending/references/api.md](../modules/reels-trending/references/api.md) |
| 获取 Instagram 用户主页 | `scrapecreators_instagram_profile` | `/wmapi/v1/scrapecreators/instagram-profile` | 2 | [modules/profile/references/api.md](../modules/profile/references/api.md) |
| 获取 Instagram 基础主页 | `scrapecreators_instagram_basic_profile` | `/wmapi/v1/scrapecreators/instagram-basic-profile` | 2 | [modules/basic-profile/references/api.md](../modules/basic-profile/references/api.md) |
| 获取 Instagram 帖子总数 | `scrapecreators_instagram_profile_post_count` | `/wmapi/v1/scrapecreators/instagram-profile-post-count` | 2 | [modules/profile-post-count/references/api.md](../modules/profile-post-count/references/api.md) |
| 获取 Instagram 主页嵌入 HTML | `scrapecreators_instagram_user_embed` | `/wmapi/v1/scrapecreators/instagram-user-embed` | 2 | [modules/user-embed/references/api.md](../modules/user-embed/references/api.md) |
| 获取 Instagram 用户帖子列表 | `scrapecreators_instagram_user_posts` | `/wmapi/v1/scrapecreators/instagram-user-posts` | 2 | [modules/user-posts/references/api.md](../modules/user-posts/references/api.md) |
| 获取 Instagram 用户 Reels 列表 | `scrapecreators_instagram_user_reels` | `/wmapi/v1/scrapecreators/instagram-user-reels` | 2 | [modules/user-reels/references/api.md](../modules/user-reels/references/api.md) |
| 获取用户被标记的帖子 | `scrapecreators_instagram_user_tagged_posts` | `/wmapi/v1/scrapecreators/instagram-user-tagged-posts` | 2 | [modules/user-tagged-posts/references/api.md](../modules/user-tagged-posts/references/api.md) |
| 获取用户故事精选列表 | `scrapecreators_instagram_user_highlights` | `/wmapi/v1/scrapecreators/instagram-user-highlights` | 2 | [modules/user-highlights/references/api.md](../modules/user-highlights/references/api.md) |
| 按音频 ID 获取使用该音频的 Reels | `scrapecreators_instagram_audio_reels` | `/wmapi/v1/scrapecreators/instagram-audio-reels` | 2 | [modules/audio-reels/references/api.md](../modules/audio-reels/references/api.md) |
| 获取 Instagram 帖子或 Reels 详情 | `scrapecreators_instagram_post` | `/wmapi/v1/scrapecreators/instagram-post` | 2 | [modules/post/references/api.md](../modules/post/references/api.md) |
| 获取故事精选详情 | `scrapecreators_instagram_highlight_detail` | `/wmapi/v1/scrapecreators/instagram-highlight-detail` | 2 | [modules/highlight-detail/references/api.md](../modules/highlight-detail/references/api.md) |
| 获取帖子或 Reels 评论 | `scrapecreators_instagram_post_comments` | `/wmapi/v1/scrapecreators/instagram-post-comments` | 2 | [modules/post-comments/references/api.md](../modules/post-comments/references/api.md) |
| 获取指定评论的回复 | `scrapecreators_instagram_comment_replies` | `/wmapi/v1/scrapecreators/instagram-comment-replies` | 2 | [modules/comment-replies/references/api.md](../modules/comment-replies/references/api.md) |

每个子 Skill 的请求参数、响应字段、示例和 curl 写在对应模块的 `references/api.md`，不要在索引页发明字段。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 打开对应子 Skill 的 `references/api.md` 核对必填字段、handle、userId 和帖子链接。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。各模块的官方来源链接见对应接口参考。响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

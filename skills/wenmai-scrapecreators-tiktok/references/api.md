# Wenmai SCRAPECREATORS TikTok 套件 API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 顶层 Skill 是索引目录，真正请求发到下表 21 个 `/wmapi/v1/scrapecreators/tiktok-**` 端点。
- 认证：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- 凭据与充值：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`
- 稳卖积分：普通接口成功为 3；观众分布成功为 67。

## 接口索引

| 子 Skill | 接口代码 | 请求地址 | 稳卖积分 | 详细契约 |
|---|---|---|---|---|
| 按关键词搜索 TikTok 视频 | `scrapecreators_tiktok_search_keyword` | `/wmapi/v1/scrapecreators/tiktok-search-keyword` | 3 | [modules/search-keyword/references/api.md](../modules/search-keyword/references/api.md) |
| TikTok Top 综合搜索 | `scrapecreators_tiktok_search_top` | `/wmapi/v1/scrapecreators/tiktok-search-top` | 3 | [modules/search-top/references/api.md](../modules/search-top/references/api.md) |
| 按话题搜索 TikTok 视频 | `scrapecreators_tiktok_search_hashtag` | `/wmapi/v1/scrapecreators/tiktok-search-hashtag` | 3 | [modules/search-hashtag/references/api.md](../modules/search-hashtag/references/api.md) |
| 搜索 TikTok 用户 | `scrapecreators_tiktok_search_users` | `/wmapi/v1/scrapecreators/tiktok-search-users` | 3 | [modules/search-users/references/api.md](../modules/search-users/references/api.md) |
| 获取 TikTok 搜索联想词 | `scrapecreators_tiktok_search_suggestions` | `/wmapi/v1/scrapecreators/tiktok-search-suggestions` | 3 | [modules/search-suggestions/references/api.md](../modules/search-suggestions/references/api.md) |
| 获取 TikTok 热门推荐流 | `scrapecreators_tiktok_trending_feed` | `/wmapi/v1/scrapecreators/tiktok-trending-feed` | 3 | [modules/trending-feed/references/api.md](../modules/trending-feed/references/api.md) |
| 获取 TikTok 用户主页 | `scrapecreators_tiktok_profile` | `/wmapi/v1/scrapecreators/tiktok-profile` | 3 | [modules/profile/references/api.md](../modules/profile/references/api.md) |
| 获取 TikTok 用户主页地区 | `scrapecreators_tiktok_profile_region` | `/wmapi/v1/scrapecreators/tiktok-profile-region` | 3 | [modules/profile-region/references/api.md](../modules/profile-region/references/api.md) |
| 获取 TikTok 用户视频列表 | `scrapecreators_tiktok_profile_videos` | `/wmapi/v1/scrapecreators/tiktok-profile-videos` | 3 | [modules/profile-videos/references/api.md](../modules/profile-videos/references/api.md) |
| 获取 TikTok 用户观众国家分布 | `scrapecreators_tiktok_user_audience` | `/wmapi/v1/scrapecreators/tiktok-user-audience` | 67 | [modules/user-audience/references/api.md](../modules/user-audience/references/api.md) |
| 获取公开合集中的视频 | `scrapecreators_tiktok_collection_videos` | `/wmapi/v1/scrapecreators/tiktok-collection-videos` | 3 | [modules/collection-videos/references/api.md](../modules/collection-videos/references/api.md) |
| 获取 TikTok 视频或图文详情 | `scrapecreators_tiktok_video` | `/wmapi/v1/scrapecreators/tiktok-video` | 3 | [modules/video/references/api.md](../modules/video/references/api.md) |
| 获取 TikTok 视频字幕或转写 | `scrapecreators_tiktok_video_transcript` | `/wmapi/v1/scrapecreators/tiktok-video-transcript` | 3 | [modules/video-transcript/references/api.md](../modules/video-transcript/references/api.md) |
| 获取 TikTok 视频评论 | `scrapecreators_tiktok_video_comments` | `/wmapi/v1/scrapecreators/tiktok-video-comments` | 3 | [modules/video-comments/references/api.md](../modules/video-comments/references/api.md) |
| 获取指定评论的回复 | `scrapecreators_tiktok_video_comment_replies` | `/wmapi/v1/scrapecreators/tiktok-video-comment-replies` | 3 | [modules/video-comment-replies/references/api.md](../modules/video-comment-replies/references/api.md) |
| 获取用户关注列表 | `scrapecreators_tiktok_user_following` | `/wmapi/v1/scrapecreators/tiktok-user-following` | 3 | [modules/user-following/references/api.md](../modules/user-following/references/api.md) |
| 获取用户粉丝列表 | `scrapecreators_tiktok_user_followers` | `/wmapi/v1/scrapecreators/tiktok-user-followers` | 3 | [modules/user-followers/references/api.md](../modules/user-followers/references/api.md) |
| 查询用户是否在直播 | `scrapecreators_tiktok_user_live` | `/wmapi/v1/scrapecreators/tiktok-user-live` | 3 | [modules/user-live/references/api.md](../modules/user-live/references/api.md) |
| 获取直播间精简信息 | `scrapecreators_tiktok_live_info` | `/wmapi/v1/scrapecreators/tiktok-live-info` | 3 | [modules/live-info/references/api.md](../modules/live-info/references/api.md) |
| 获取 TikTok 歌曲详情 | `scrapecreators_tiktok_song` | `/wmapi/v1/scrapecreators/tiktok-song` | 3 | [modules/song/references/api.md](../modules/song/references/api.md) |
| 获取使用该歌曲的视频 | `scrapecreators_tiktok_song_videos` | `/wmapi/v1/scrapecreators/tiktok-song-videos` | 3 | [modules/song-videos/references/api.md](../modules/song-videos/references/api.md) |

每个子 Skill 的请求参数、响应字段、示例和 curl 写在对应模块的 `references/api.md`，不要在索引页发明字段。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 打开对应子 Skill 的 `references/api.md` 核对必填字段、clipId 和 handle。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。各模块的官方来源链接见对应接口参考。响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

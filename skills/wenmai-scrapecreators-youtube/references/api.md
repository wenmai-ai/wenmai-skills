# Wenmai SCRAPECREATORS YouTube 套件 API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 顶层 Skill 是索引目录，真正请求发到下表 18 个 `/wmapi/v1/scrapecreators/youtube-**` 端点。不要因为套件有 18 个接口就全打一遍。
- 认证：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- 凭据与充值：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`
- 稳卖积分：普通接口成功为 2。贵参数会提高官方成本，默认不要开。

## 接口索引

| 子 Skill | 接口代码 | 请求地址 | 稳卖积分 | 详细契约 |
|---|---|---|---|---|
| 搜索 YouTube 视频、频道、播放列表、Shorts 和直播 | `scrapecreators_youtube_search` | `/wmapi/v1/scrapecreators/youtube-search` | 2 | [modules/search/references/api.md](../modules/search/references/api.md) |
| 获取 YouTube 搜索联想词 | `scrapecreators_youtube_search_typeahead` | `/wmapi/v1/scrapecreators/youtube-search-typeahead` | 2 | [modules/search-typeahead/references/api.md](../modules/search-typeahead/references/api.md) |
| 按话题搜索 YouTube 视频 | `scrapecreators_youtube_search_hashtag` | `/wmapi/v1/scrapecreators/youtube-search-hashtag` | 2 | [modules/search-hashtag/references/api.md](../modules/search-hashtag/references/api.md) |
| 获取 YouTube 频道详情 | `scrapecreators_youtube_channel` | `/wmapi/v1/scrapecreators/youtube-channel` | 2 | [modules/channel/references/api.md](../modules/channel/references/api.md) |
| 获取 YouTube 频道视频列表 | `scrapecreators_youtube_channel_videos` | `/wmapi/v1/scrapecreators/youtube-channel-videos` | 2 | [modules/channel-videos/references/api.md](../modules/channel-videos/references/api.md) |
| 在指定 YouTube 频道内搜索 | `scrapecreators_youtube_channel_search` | `/wmapi/v1/scrapecreators/youtube-channel-search` | 2 | [modules/channel-search/references/api.md](../modules/channel-search/references/api.md) |
| 获取 YouTube 频道播放列表 | `scrapecreators_youtube_channel_playlists` | `/wmapi/v1/scrapecreators/youtube-channel-playlists` | 2 | [modules/channel-playlists/references/api.md](../modules/channel-playlists/references/api.md) |
| 获取 YouTube 频道直播和历史直播 | `scrapecreators_youtube_channel_lives` | `/wmapi/v1/scrapecreators/youtube-channel-lives` | 2 | [modules/channel-lives/references/api.md](../modules/channel-lives/references/api.md) |
| 获取 YouTube 频道社区帖 | `scrapecreators_youtube_channel_community_posts` | `/wmapi/v1/scrapecreators/youtube-channel-community-posts` | 2 | [modules/channel-community-posts/references/api.md](../modules/channel-community-posts/references/api.md) |
| 获取 YouTube 频道 Shorts | `scrapecreators_youtube_channel_shorts` | `/wmapi/v1/scrapecreators/youtube-channel-shorts` | 2 | [modules/channel-shorts/references/api.md](../modules/channel-shorts/references/api.md) |
| 获取 YouTube 视频或 Short 详情 | `scrapecreators_youtube_video` | `/wmapi/v1/scrapecreators/youtube-video` | 2 | [modules/video/references/api.md](../modules/video/references/api.md) |
| 获取 YouTube 视频或 Short 字幕或转写 | `scrapecreators_youtube_video_transcript` | `/wmapi/v1/scrapecreators/youtube-video-transcript` | 2 | [modules/video-transcript/references/api.md](../modules/video-transcript/references/api.md) |
| 推断 YouTube 视频可能的赞助商 | `scrapecreators_youtube_video_sponsors` | `/wmapi/v1/scrapecreators/youtube-video-sponsors` | 2 | [modules/video-sponsors/references/api.md](../modules/video-sponsors/references/api.md) |
| 获取 YouTube 视频评论 | `scrapecreators_youtube_video_comments` | `/wmapi/v1/scrapecreators/youtube-video-comments` | 2 | [modules/video-comments/references/api.md](../modules/video-comments/references/api.md) |
| 获取指定 YouTube 评论的回复 | `scrapecreators_youtube_video_comment_replies` | `/wmapi/v1/scrapecreators/youtube-video-comment-replies` | 2 | [modules/video-comment-replies/references/api.md](../modules/video-comment-replies/references/api.md) |
| 获取 YouTube 热门 Shorts | `scrapecreators_youtube_shorts_trending` | `/wmapi/v1/scrapecreators/youtube-shorts-trending` | 2 | [modules/shorts-trending/references/api.md](../modules/shorts-trending/references/api.md) |
| 获取 YouTube 播放列表中的视频 | `scrapecreators_youtube_playlist` | `/wmapi/v1/scrapecreators/youtube-playlist` | 2 | [modules/playlist/references/api.md](../modules/playlist/references/api.md) |
| 获取 YouTube 社区帖详情 | `scrapecreators_youtube_community_post` | `/wmapi/v1/scrapecreators/youtube-community-post` | 2 | [modules/community-post/references/api.md](../modules/community-post/references/api.md) |

每个子 Skill 的请求参数、响应字段、示例和 curl 写在对应模块的 `references/api.md`，不要在索引页发明字段。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 打开对应子 Skill 的 `references/api.md` 核对必填字段、handle、channelId、视频链接和 continuationToken。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。各模块的官方来源链接见对应接口参考。响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。

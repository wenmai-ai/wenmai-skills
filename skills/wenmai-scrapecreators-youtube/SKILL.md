---
name: wenmai-scrapecreators-youtube
description: "ScrapeCreators YouTube 社媒标准 API 套件。一个顶层 Skill 索引 18 个子 Skill：综合搜索、搜索联想、话题搜索、频道详情、频道视频、频道内搜索、频道播放列表、频道直播、频道社区帖、频道 Shorts、视频详情、字幕、赞助推断、评论、评论回复、热门 Shorts、播放列表视频、社区帖详情。普通接口每次成功 3 积分。不含 Facebook、TikTok Shop 和 Ad Library。当用户需要 YouTube 频道、爆款视频、字幕、评论、Shorts 或提到 ScrapeCreators 时使用；即使用户未明确提及 ScrapeCreators，只要任务需要该数据源也应触发本套件，再按索引只调用所需子 Skill。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
  short-description: 搜频道和爆款视频，查详情、字幕、评论和 Shorts；按需调用，普通 3 积分。
---

# YouTube 频道与爆款内容调研

## Overview

这是 ScrapeCreators YouTube 的**索引 Skill**。官方包和 Polaris 都只安装这一个顶层 Skill；整个 ZIP 里只能有这一份 `SKILL.md`。
18 个接口的完整契约放在 `modules/<name>/MODULE.md`，不作为独立 Skill 安装，也不要 `load_skill(wenmai-scrapecreators-youtube-xxx)`。

先加载 `$wenmai-scrapecreators-youtube`，再按用户目标只阅读并调用需要的子模块。用户要搜视频就打搜索，要频道就打频道；不要因为套件有 18 个接口就全打一遍。`includeExtras` 会变慢且可能提高官方成本，用户没点名不要开。

- Platform: YouTube
- Provider: ScrapeCreators
- Auth: Header `secret-key: $WENMAI_API_KEY`
- 总契约: [`references/api.md`](references/api.md)

## 子 Skill 索引

| 场景 | 子 Skill | Endpoint | 稳卖积分 | 脚本 |
|---|---|---|---|---|
| 搜索 YouTube 视频、频道、播放列表、Shorts 和直播 | [`modules/search`](modules/search/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-search` | 3 | `modules/search/scripts/search.py` |
| 获取 YouTube 搜索联想词 | [`modules/search-typeahead`](modules/search-typeahead/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-search-typeahead` | 3 | `modules/search-typeahead/scripts/search_typeahead.py` |
| 按话题搜索 YouTube 视频 | [`modules/search-hashtag`](modules/search-hashtag/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-search-hashtag` | 3 | `modules/search-hashtag/scripts/search_hashtag.py` |
| 获取 YouTube 频道详情 | [`modules/channel`](modules/channel/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-channel` | 3 | `modules/channel/scripts/channel.py` |
| 获取 YouTube 频道视频列表 | [`modules/channel-videos`](modules/channel-videos/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-channel-videos` | 3 | `modules/channel-videos/scripts/channel_videos.py` |
| 在指定 YouTube 频道内搜索 | [`modules/channel-search`](modules/channel-search/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-channel-search` | 3 | `modules/channel-search/scripts/channel_search.py` |
| 获取 YouTube 频道播放列表 | [`modules/channel-playlists`](modules/channel-playlists/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-channel-playlists` | 3 | `modules/channel-playlists/scripts/channel_playlists.py` |
| 获取 YouTube 频道直播和历史直播 | [`modules/channel-lives`](modules/channel-lives/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-channel-lives` | 3 | `modules/channel-lives/scripts/channel_lives.py` |
| 获取 YouTube 频道社区帖 | [`modules/channel-community-posts`](modules/channel-community-posts/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-channel-community-posts` | 3 | `modules/channel-community-posts/scripts/channel_community_posts.py` |
| 获取 YouTube 频道 Shorts | [`modules/channel-shorts`](modules/channel-shorts/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-channel-shorts` | 3 | `modules/channel-shorts/scripts/channel_shorts.py` |
| 获取 YouTube 视频或 Short 详情 | [`modules/video`](modules/video/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-video` | 3 | `modules/video/scripts/video.py` |
| 获取 YouTube 视频或 Short 字幕或转写 | [`modules/video-transcript`](modules/video-transcript/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-video-transcript` | 3 | `modules/video-transcript/scripts/video_transcript.py` |
| 推断 YouTube 视频可能的赞助商 | [`modules/video-sponsors`](modules/video-sponsors/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-video-sponsors` | 3 | `modules/video-sponsors/scripts/video_sponsors.py` |
| 获取 YouTube 视频评论 | [`modules/video-comments`](modules/video-comments/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-video-comments` | 3 | `modules/video-comments/scripts/video_comments.py` |
| 获取指定 YouTube 评论的回复 | [`modules/video-comment-replies`](modules/video-comment-replies/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-video-comment-replies` | 3 | `modules/video-comment-replies/scripts/video_comment_replies.py` |
| 获取 YouTube 热门 Shorts | [`modules/shorts-trending`](modules/shorts-trending/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-shorts-trending` | 3 | `modules/shorts-trending/scripts/shorts_trending.py` |
| 获取 YouTube 播放列表中的视频 | [`modules/playlist`](modules/playlist/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-playlist` | 3 | `modules/playlist/scripts/playlist.py` |
| 获取 YouTube 社区帖详情 | [`modules/community-post`](modules/community-post/MODULE.md) | `POST /wmapi/v1/scrapecreators/youtube-community-post` | 3 | `modules/community-post/scripts/community_post.py` |

## 怎么选

1. 搜视频、频道、播放列表、Shorts 和直播：`search`。联想词用 `search-typeahead`。按话题搜用 `search-hashtag`。
2. 已有 handle / channelId / 频道链接：先 `channel` 看详情，再按需 `channel-videos`、`channel-shorts`、`channel-playlists`、`channel-lives`、`channel-community-posts` 或 `channel-search`。
3. 看全站热门 Shorts：`shorts-trending`。
4. 已有视频或 Short 链接：详情 `video`，字幕 `video-transcript`，评论 `video-comments`；只要某条回复才用评论返回的 `repliesContinuationToken` 打 `video-comment-replies`。
5. 赞助商推断 `video-sponsors` 是实验能力，用户没点名不要打。
6. 播放列表用 `playlist`；社区帖详情用 `community-post`。

普通接口成功 `costCredit=3`。不要默认开启 `includeExtras`。

## Workflow

1. 从用户问题映射到上表中的 1 个子 Skill；链路任务按「搜索/频道 → 视频 → 字幕/评论」展开，仍只调用当前步骤需要的接口。
2. 阅读对应 `modules/<name>/MODULE.md` 和 `modules/<name>/references/api.md`，不要凭记忆补字段；子模块不是独立 Skill。
3. 在套件根目录运行该子 Skill 脚本，保留原始 JSON。
4. 检查 `code`、`requestId`、`costCredit`；成功应为 3。
5. 摘要必须能追溯到响应字段；缺失就写缺失。

## How To Run

调用 API 前，先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。任一变量存在时直接用于调用，不得展示、复述或记录密钥值；仅当两个环境变量都未获取到时，才请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`，并在本机配置环境变量。不得在未检查环境变量的情况下声称缺少 API Key。Wenmai 个人中心为 https://agent.wenmai-ai.com/；额度或余额不足时，按该指南完成充值。

在套件根目录 `Skills/wenmai-scrapecreators-youtube/` 执行：

```bash
export WENMAI_API_KEY="replace-with-real-wenmai-api-key"
# 搜索 YouTube 视频、频道、播放列表、Shorts 和直播
python3 modules/search/scripts/search.py '{"query": "gymshark", "region": "US"}'
# 获取 YouTube 搜索联想词
python3 modules/search-typeahead/scripts/search_typeahead.py '{"query": "gymshark"}'
# 按话题搜索 YouTube 视频
python3 modules/search-hashtag/scripts/search_hashtag.py '{"hashtag": "gymshark", "type": "all"}'
# 获取 YouTube 频道详情
python3 modules/channel/scripts/channel.py '{"handle": "gymshark"}'
# 获取 YouTube 频道视频列表
python3 modules/channel-videos/scripts/channel_videos.py '{"handle": "gymshark", "sort": "latest"}'
# 在指定 YouTube 频道内搜索
python3 modules/channel-search/scripts/channel_search.py '{"handle": "gymshark", "query": "training"}'
# 获取 YouTube 频道播放列表
python3 modules/channel-playlists/scripts/channel_playlists.py '{"handle": "gymshark"}'
# 获取 YouTube 频道直播和历史直播
python3 modules/channel-lives/scripts/channel_lives.py '{"handle": "gymshark"}'
# 获取 YouTube 频道社区帖
python3 modules/channel-community-posts/scripts/channel_community_posts.py '{"handle": "gymshark"}'
# 获取 YouTube 频道 Shorts
python3 modules/channel-shorts/scripts/channel_shorts.py '{"handle": "gymshark", "sort": "newest"}'
# 获取 YouTube 视频或 Short 详情
python3 modules/video/scripts/video.py '{"url": "https://www.youtube.com/watch?v=Y2Ah_DFr8cw"}'
# 获取 YouTube 视频或 Short 字幕或转写
python3 modules/video-transcript/scripts/video_transcript.py '{"url": "https://www.youtube.com/watch?v=bjVIDXPP7Uk", "language": "en"}'
# 推断 YouTube 视频可能的赞助商
python3 modules/video-sponsors/scripts/video_sponsors.py '{"url": "https://www.youtube.com/watch?v=AVO0ifle-OU", "language": "en"}'
# 获取 YouTube 视频评论
python3 modules/video-comments/scripts/video_comments.py '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "order": "top"}'
# 获取指定 YouTube 评论的回复
python3 modules/video-comment-replies/scripts/video_comment_replies.py '{"continuationToken": "Eg0SC2RRdzR3OVdnWGNRGAYygwEaUBIa"}'
# 获取 YouTube 热门 Shorts
python3 modules/shorts-trending/scripts/shorts_trending.py '{}'
# 获取 YouTube 播放列表中的视频
python3 modules/playlist/scripts/playlist.py '{"playlist_id": "PLP32wGpgzmIlInfgKVFfCwVsxgGqZNIiS"}'
# 获取 YouTube 社区帖详情
python3 modules/community-post/scripts/community_post.py '{"url": "https://www.youtube.com/post/Ugkxvj2KoApYAXoqLWnKVr6zZe5JjeHrQeP8"}'
```

脚本将 Wenmai API 原始响应输出为格式化 JSON。不得把 API Key 写入文件、日志或回答。本地或测试网关可设置 `WENMAI_API_ORIGIN`。

## Request Rules

- 顶层直接传业务字段，不要增加 `request` 包装层。
- 每个子 Skill 的必填字段、分页和枚举以该模块 `references/api.md` 为准。
- 只发送当前子 Skill 文档里的字段，不把其他接口的筛选混进去。
- 评论回复必须用评论接口返回的 `repliesContinuationToken`，不要把视频链接误传到该接口。

## Response Rules

- 先报告 `code`、`requestId` 和 `costCredit`。
- 所有摘要值必须能追溯到原始响应字段；缺失字段标记为缺失，不估算、推断或补造。
- 长列表先汇总再按需展开；存在 `warnings` 时原样保留。
- 无字幕、无社区帖、无直播时字段可能为空，这仍可能是成功响应。

## Error Handling

- 调用前先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 参数错误时，对照对应子 Skill 的 `references/api.md` 检查必填字段、handle、channelId、视频链接和 continuationToken。
- HTTP、网络、超时、网关错误、`error`、非 `OK` 状态或非 JSON 响应发生时，报告脱敏后的状态码、消息、`requestId` 和 `warnings`，不要把异常或部分数据当作成功。
- 额度或余额不足时，引导用户参考上述使用指南完成充值；不要反复重试或绕过上游限制。

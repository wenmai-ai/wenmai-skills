---
name: wenmai-scrapecreators-tiktok
description: "ScrapeCreators TikTok 社媒标准 API 套件。一个顶层 Skill 索引 21 个子 Skill：关键词/Top/话题/用户/联想搜索、热门流、主页、地区、作品列表、观众分布、合集、视频详情、字幕、评论、评论回复、关注、粉丝、直播状态、直播间信息、歌曲、歌曲视频。普通接口每次成功 2 积分，观众分布 36 积分。不含 TikTok Shop。当用户需要 TikTok 达人、视频、评论、粉丝、直播、音乐或提到 ScrapeCreators 时使用；即使用户未明确提及 ScrapeCreators，只要任务需要该数据源也应触发本套件，再按索引只调用所需子 Skill。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
  short-description: 搜达人和爆款视频，查主页地区、粉丝、评论字幕、直播和音乐；按需调用，普通 2 积分。
---

# TikTok 达人与爆款内容调研

## Overview

这是 ScrapeCreators TikTok 的**索引 Skill**。官方包和 Polaris 都只安装这一个顶层 Skill；整个 ZIP 里只能有这一份 `SKILL.md`。
21 个接口的完整契约放在 `modules/<name>/MODULE.md`，不作为独立 Skill 安装，也不要 `load_skill(wenmai-scrapecreators-tiktok-xxx)`。

先加载 `$wenmai-scrapecreators-tiktok`，再按用户目标只阅读并调用需要的子模块。用户要搜视频就打搜索，要主页就打主页；不要因为套件有 21 个接口就全打一遍。观众分布一次 36 积分，确认需要后再调用。

- Platform: TikTok
- Provider: ScrapeCreators
- Auth: Header `secret-key: $WENMAI_API_KEY`
- 总契约: [`references/api.md`](references/api.md)

## 子 Skill 索引

| 场景 | 子 Skill | Endpoint | 稳卖积分 | 脚本 |
|---|---|---|---|---|
| 按关键词搜索 TikTok 视频 | [`modules/search-keyword`](modules/search-keyword/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-search-keyword` | 2 | `modules/search-keyword/scripts/search_keyword.py` |
| TikTok Top 综合搜索 | [`modules/search-top`](modules/search-top/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-search-top` | 2 | `modules/search-top/scripts/search_top.py` |
| 按话题搜索 TikTok 视频 | [`modules/search-hashtag`](modules/search-hashtag/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-search-hashtag` | 2 | `modules/search-hashtag/scripts/search_hashtag.py` |
| 搜索 TikTok 用户 | [`modules/search-users`](modules/search-users/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-search-users` | 2 | `modules/search-users/scripts/search_users.py` |
| 获取 TikTok 搜索联想词 | [`modules/search-suggestions`](modules/search-suggestions/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-search-suggestions` | 2 | `modules/search-suggestions/scripts/search_suggestions.py` |
| 获取 TikTok 热门推荐流 | [`modules/trending-feed`](modules/trending-feed/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-trending-feed` | 2 | `modules/trending-feed/scripts/trending_feed.py` |
| 获取 TikTok 用户主页 | [`modules/profile`](modules/profile/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-profile` | 2 | `modules/profile/scripts/profile.py` |
| 获取 TikTok 用户主页地区 | [`modules/profile-region`](modules/profile-region/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-profile-region` | 2 | `modules/profile-region/scripts/profile_region.py` |
| 获取 TikTok 用户视频列表 | [`modules/profile-videos`](modules/profile-videos/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-profile-videos` | 2 | `modules/profile-videos/scripts/profile_videos.py` |
| 获取 TikTok 用户观众国家分布 | [`modules/user-audience`](modules/user-audience/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-user-audience` | 36 | `modules/user-audience/scripts/user_audience.py` |
| 获取公开合集中的视频 | [`modules/collection-videos`](modules/collection-videos/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-collection-videos` | 2 | `modules/collection-videos/scripts/collection_videos.py` |
| 获取 TikTok 视频或图文详情 | [`modules/video`](modules/video/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-video` | 2 | `modules/video/scripts/video.py` |
| 获取 TikTok 视频字幕或转写 | [`modules/video-transcript`](modules/video-transcript/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-video-transcript` | 2 | `modules/video-transcript/scripts/video_transcript.py` |
| 获取 TikTok 视频评论 | [`modules/video-comments`](modules/video-comments/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-video-comments` | 2 | `modules/video-comments/scripts/video_comments.py` |
| 获取指定评论的回复 | [`modules/video-comment-replies`](modules/video-comment-replies/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-video-comment-replies` | 2 | `modules/video-comment-replies/scripts/video_comment_replies.py` |
| 获取用户关注列表 | [`modules/user-following`](modules/user-following/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-user-following` | 2 | `modules/user-following/scripts/user_following.py` |
| 获取用户粉丝列表 | [`modules/user-followers`](modules/user-followers/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-user-followers` | 2 | `modules/user-followers/scripts/user_followers.py` |
| 查询用户是否在直播 | [`modules/user-live`](modules/user-live/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-user-live` | 2 | `modules/user-live/scripts/user_live.py` |
| 获取直播间精简信息 | [`modules/live-info`](modules/live-info/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-live-info` | 2 | `modules/live-info/scripts/live_info.py` |
| 获取 TikTok 歌曲详情 | [`modules/song`](modules/song/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-song` | 2 | `modules/song/scripts/song.py` |
| 获取使用该歌曲的视频 | [`modules/song-videos`](modules/song-videos/MODULE.md) | `POST /wmapi/v1/scrapecreators/tiktok-song-videos` | 2 | `modules/song-videos/scripts/song_videos.py` |

## 怎么选

1. 搜视频：`search-keyword` / `search-top` / `search-hashtag`。
2. 搜人或联想：`search-users` / `search-suggestions`。
3. 热门推荐：`trending-feed`，必填 `region`。
4. 已有 handle：`profile`、`profile-region`、`profile-videos`、`user-following`、`user-followers`、`user-live`。
5. 观众国家分布用 `user-audience`，一次 36 积分，确认需要再打。
6. 已有视频链接：详情 `video`，字幕 `video-transcript`，评论 `video-comments`；回复先拿未 trim 的 `cid` 再打 `video-comment-replies`。
7. 直播间：先 `user-live` 拿 `roomId`，再 `live-info`。
8. 音乐：`song` / `song-videos` 必须传音乐 URL 上的 `clipId`，不要传 `music.id`。

普通接口成功 `costCredit=2`。不要默认开启 `download_media`。

## Workflow

1. 从用户问题映射到上表中的 1 个子 Skill；链路任务按「搜索/主页 → 视频 → 评论/字幕/直播/音乐」展开，仍只调用当前步骤需要的接口。
2. 阅读对应 `modules/<name>/MODULE.md` 和 `modules/<name>/references/api.md`，不要凭记忆补字段；子模块不是独立 Skill。
3. 在套件根目录运行该子 Skill 脚本，保留原始 JSON。
4. 检查 `code`、`requestId`、`costCredit`；普通接口成功应为 2，观众分布应为 36。
5. 摘要必须能追溯到响应字段；缺失就写缺失。

## How To Run

调用 API 前，先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。任一变量存在时直接用于调用，不得展示、复述或记录密钥值；仅当两个环境变量都未获取到时，才请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`，并在本机配置环境变量。不得在未检查环境变量的情况下声称缺少 API Key。Wenmai 个人中心为 https://agent.wenmai-ai.com/；额度或余额不足时，按该指南完成充值。

在套件根目录 `Skills/wenmai-scrapecreators-tiktok/` 执行：

```bash
export WENMAI_API_KEY="replace-with-real-wenmai-api-key"
# 按关键词搜索 TikTok 视频
python3 modules/search-keyword/scripts/search_keyword.py '{"query": "amazon finds", "region": "US", "trim": true}'
# TikTok Top 综合搜索
python3 modules/search-top/scripts/search_top.py '{"query": "amazon finds", "trim": true}'
# 按话题搜索 TikTok 视频
python3 modules/search-hashtag/scripts/search_hashtag.py '{"hashtag": "amazonfinds", "trim": true}'
# 搜索 TikTok 用户
python3 modules/search-users/scripts/search_users.py '{"query": "gymshark", "trim": true}'
# 获取 TikTok 搜索联想词
python3 modules/search-suggestions/scripts/search_suggestions.py '{"query": "amazon"}'
# 获取 TikTok 热门推荐流
python3 modules/trending-feed/scripts/trending_feed.py '{"region": "US", "trim": true}'
# 获取 TikTok 用户主页
python3 modules/profile/scripts/profile.py '{"handle": "gymshark", "cache_max_age": "7d"}'
# 获取 TikTok 用户主页地区
python3 modules/profile-region/scripts/profile_region.py '{"handle": "gymshark"}'
# 获取 TikTok 用户视频列表
python3 modules/profile-videos/scripts/profile_videos.py '{"handle": "gymshark", "trim": true}'
# 获取 TikTok 用户观众国家分布
python3 modules/user-audience/scripts/user_audience.py '{"handle": "gymshark"}'
# 获取公开合集中的视频
python3 modules/collection-videos/scripts/collection_videos.py '{"url": "https://www.tiktok.com/@kibblemaster808/collection/Want-to-go-7665668414573546258"}'
# 获取 TikTok 视频或图文详情
python3 modules/video/scripts/video.py '{"url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335", "trim": true}'
# 获取 TikTok 视频字幕或转写
python3 modules/video-transcript/scripts/video_transcript.py '{"url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335"}'
# 获取 TikTok 视频评论
python3 modules/video-comments/scripts/video_comments.py '{"url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335"}'
# 获取指定评论的回复
python3 modules/video-comment-replies/scripts/video_comment_replies.py '{"url": "https://www.tiktok.com/@karissa.brighton/video/7702948337007234335", "comment_id": "7703257909974549279"}'
# 获取用户关注列表
python3 modules/user-following/scripts/user_following.py '{"handle": "gymshark", "trim": true}'
# 获取用户粉丝列表
python3 modules/user-followers/scripts/user_followers.py '{"handle": "gymshark", "trim": true}'
# 查询用户是否在直播
python3 modules/user-live/scripts/user_live.py '{"handle": "gymshark"}'
# 获取直播间精简信息
python3 modules/live-info/scripts/live_info.py '{"room_id": "7442820520199981856", "user_id": "6536068161471517696"}'
# 获取 TikTok 歌曲详情
python3 modules/song/scripts/song.py '{"clipId": "7694359127636265750"}'
# 获取使用该歌曲的视频
python3 modules/song-videos/scripts/song_videos.py '{"clipId": "7694359127636265750"}'
```

脚本将 Wenmai API 原始响应输出为格式化 JSON。不得把 API Key 写入文件、日志或回答。本地或测试网关可设置 `WENMAI_API_ORIGIN`。

## Request Rules

- 顶层直接传业务字段，不要增加 `request` 包装层。
- 每个子 Skill 的必填字段、分页和枚举以该模块 `references/api.md` 为准。
- 只发送当前子 Skill 文档里的字段，不把其他接口的筛选混进去。
- 歌曲接口只传 `clipId`；评论回复必须用未 trim 的 `cid`。

## Response Rules

- 先报告 `code`、`requestId` 和 `costCredit`。
- 所有摘要值必须能追溯到原始响应字段；缺失字段标记为缺失，不估算、推断或补造。
- 长列表先汇总再按需展开；存在 `warnings` 时原样保留。
- 字幕、未开播、历史直播间可能字段为空，这仍可能是成功响应。

## Error Handling

- 调用前先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 参数错误时，对照对应子 Skill 的 `references/api.md` 检查必填字段、clipId 和 handle。
- HTTP、网络、超时、网关错误、`error`、非 `OK` 状态或非 JSON 响应发生时，报告脱敏后的状态码、消息、`requestId` 和 `warnings`，不要把异常或部分数据当作成功。
- 额度或余额不足时，引导用户参考上述使用指南完成充值；不要反复重试或绕过上游限制。

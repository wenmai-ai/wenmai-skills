---
name: wenmai-scrapecreators-instagram
description: "ScrapeCreators Instagram 社媒标准 API 套件。一个顶层 Skill 索引 19 个子 Skill：综合搜索、热门专题、话题帖、主页搜索、Reels 搜索、热门 Reels、主页、基础主页、帖子总数、嵌入、帖子列表、Reels 列表、被标记帖、故事精选、音频 Reels、帖子详情、精选详情、评论、评论回复。普通接口每次成功 3 积分。不含 Facebook、TikTok Shop、Ad Library 和字幕转写。当用户需要 Instagram 达人、帖子、Reels、评论或提到 ScrapeCreators 时使用；即使用户未明确提及 ScrapeCreators，只要任务需要该数据源也应触发本套件，再按索引只调用所需子 Skill。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
  short-description: 搜账号、帖子、Reels 和评论，按需调用；普通 3 积分，不含 Facebook。
---

# Instagram 达人与内容调研

## Overview

这是 ScrapeCreators Instagram 的**索引 Skill**。官方包和 Polaris 都只安装这一个顶层 Skill；整个 ZIP 里只能有这一份 `SKILL.md`。
19 个接口的完整契约放在 `modules/<name>/MODULE.md`，不作为独立 Skill 安装，也不要 `load_skill(wenmai-scrapecreators-instagram-xxx)`。

先加载 `$wenmai-scrapecreators-instagram`，再按用户目标只阅读并调用需要的子模块。用户要搜视频就打搜索，要主页就打主页；不要因为套件有 19 个接口就全打一遍。`include_replies=true`、`download_media=true` 是贵参数，用户没点名不要开。

- Platform: Instagram
- Provider: ScrapeCreators
- Auth: Header `secret-key: $WENMAI_API_KEY`
- 总契约: [`references/api.md`](references/api.md)

## 子 Skill 索引

| 场景 | 子 Skill | Endpoint | 稳卖积分 | 脚本 |
|---|---|---|---|---|
| 搜索 Instagram 用户、话题、地点和关键词 | [`modules/search`](modules/search/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-search` | 3 | `modules/search/scripts/search.py` |
| 按热门话题搜索 Instagram 帖子 | [`modules/search-popular`](modules/search-popular/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-search-popular` | 3 | `modules/search-popular/scripts/search_popular.py` |
| 按话题搜索 Instagram 帖子 | [`modules/search-hashtag`](modules/search-hashtag/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-search-hashtag` | 3 | `modules/search-hashtag/scripts/search_hashtag.py` |
| 搜索 Instagram 用户主页 | [`modules/search-profiles`](modules/search-profiles/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-search-profiles` | 3 | `modules/search-profiles/scripts/search_profiles.py` |
| 按关键词搜索 Instagram Reels | [`modules/reels-search`](modules/reels-search/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-reels-search` | 3 | `modules/reels-search/scripts/reels_search.py` |
| 获取近 7 天热门 Reels | [`modules/reels-trending`](modules/reels-trending/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-reels-trending` | 3 | `modules/reels-trending/scripts/reels_trending.py` |
| 获取 Instagram 用户主页 | [`modules/profile`](modules/profile/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-profile` | 3 | `modules/profile/scripts/profile.py` |
| 获取 Instagram 基础主页 | [`modules/basic-profile`](modules/basic-profile/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-basic-profile` | 3 | `modules/basic-profile/scripts/basic_profile.py` |
| 获取 Instagram 帖子总数 | [`modules/profile-post-count`](modules/profile-post-count/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-profile-post-count` | 3 | `modules/profile-post-count/scripts/profile_post_count.py` |
| 获取 Instagram 主页嵌入 HTML | [`modules/user-embed`](modules/user-embed/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-user-embed` | 3 | `modules/user-embed/scripts/user_embed.py` |
| 获取 Instagram 用户帖子列表 | [`modules/user-posts`](modules/user-posts/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-user-posts` | 3 | `modules/user-posts/scripts/user_posts.py` |
| 获取 Instagram 用户 Reels 列表 | [`modules/user-reels`](modules/user-reels/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-user-reels` | 3 | `modules/user-reels/scripts/user_reels.py` |
| 获取用户被标记的帖子 | [`modules/user-tagged-posts`](modules/user-tagged-posts/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-user-tagged-posts` | 3 | `modules/user-tagged-posts/scripts/user_tagged_posts.py` |
| 获取用户故事精选列表 | [`modules/user-highlights`](modules/user-highlights/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-user-highlights` | 3 | `modules/user-highlights/scripts/user_highlights.py` |
| 按音频 ID 获取使用该音频的 Reels | [`modules/audio-reels`](modules/audio-reels/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-audio-reels` | 3 | `modules/audio-reels/scripts/audio_reels.py` |
| 获取 Instagram 帖子或 Reels 详情 | [`modules/post`](modules/post/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-post` | 3 | `modules/post/scripts/post.py` |
| 获取故事精选详情 | [`modules/highlight-detail`](modules/highlight-detail/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-highlight-detail` | 3 | `modules/highlight-detail/scripts/highlight_detail.py` |
| 获取帖子或 Reels 评论 | [`modules/post-comments`](modules/post-comments/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-post-comments` | 3 | `modules/post-comments/scripts/post_comments.py` |
| 获取指定评论的回复 | [`modules/comment-replies`](modules/comment-replies/MODULE.md) | `POST /wmapi/v1/scrapecreators/instagram-comment-replies` | 3 | `modules/comment-replies/scripts/comment_replies.py` |

## 怎么选

1. 搜账号：`search` / `search-profiles`。
2. 搜话题帖：默认 `search-hashtag`。只有用户要 Instagram Popular 专题页时才打 `search-popular`，query 必须是 music、travel 这类专题词，不要传品牌名或账号名；官方示例 basketball 现在也可能失败。失败后立刻改打 `search-hashtag` 或 `reels-search`，不要换词连打。
3. 搜 Reels：`reels-search`；看近 7 天热门：`reels-trending`。
4. 已有 handle：先 `profile-post-count` 或 `basic-profile`，需要完整主页再 `profile`，再按需 `user-posts` / `user-reels` / `user-highlights`。
5. 已有帖子链接：`post` 看详情，`post-comments` 看评论；只要某条回复才打 `comment-replies`。
6. 禁止调用 `instagram-media-transcript`。生产网关即使有该端点，本 Skill 也不暴露、不介绍、不调用。字幕需求直接告知当前不支持。
7. 禁止默认打开 `include_replies`、`download_media`。

## How To Run

调用 API 前，先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。任一变量存在时直接用于调用，不得展示、复述或记录密钥值；仅当两个环境变量都未获取到时，才请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`，并在本机配置环境变量。不得在未检查环境变量的情况下声称缺少 API Key。Wenmai 个人中心为 https://agent.wenmai-ai.com/；额度或余额不足时，按该指南完成充值。

在套件根目录 `Skills/wenmai-scrapecreators-instagram/` 执行：

```bash
export WENMAI_API_KEY="replace-with-real-wenmai-api-key"
# 搜索 Instagram 用户、话题、地点和关键词
python3 modules/search/scripts/search.py '{"query": "gymshark"}'
# 按热门话题搜索 Instagram 帖子
python3 modules/search-popular/scripts/search_popular.py '{"query": "music"}'
# 按话题搜索 Instagram 帖子
python3 modules/search-hashtag/scripts/search_hashtag.py '{"hashtag": "gymshark", "media_type": "all"}'
# 搜索 Instagram 用户主页
python3 modules/search-profiles/scripts/search_profiles.py '{"query": "gymshark"}'
# 按关键词搜索 Instagram Reels
python3 modules/reels-search/scripts/reels_search.py '{"query": "gymshark", "page": 1}'
# 获取近 7 天热门 Reels
python3 modules/reels-trending/scripts/reels_trending.py '{}'
# 获取 Instagram 用户主页
python3 modules/profile/scripts/profile.py '{"handle": "gymshark"}'
# 获取 Instagram 基础主页
python3 modules/basic-profile/scripts/basic_profile.py '{"userId": "390927249"}'
# 获取 Instagram 帖子总数
python3 modules/profile-post-count/scripts/profile_post_count.py '{"handle": "gymshark"}'
# 获取 Instagram 主页嵌入 HTML
python3 modules/user-embed/scripts/user_embed.py '{"handle": "gymshark"}'
# 获取 Instagram 用户帖子列表
python3 modules/user-posts/scripts/user_posts.py '{"handle": "gymshark", "trim": true}'
# 获取 Instagram 用户 Reels 列表
python3 modules/user-reels/scripts/user_reels.py '{"handle": "gymshark", "trim": true}'
# 获取用户被标记的帖子
python3 modules/user-tagged-posts/scripts/user_tagged_posts.py '{"user_id": "390927249"}'
# 获取用户故事精选列表
python3 modules/user-highlights/scripts/user_highlights.py '{"handle": "gymshark"}'
# 按音频 ID 获取使用该音频的 Reels
python3 modules/audio-reels/scripts/audio_reels.py '{"audio_id": "1392969992841787"}'
# 获取 Instagram 帖子或 Reels 详情
python3 modules/post/scripts/post.py '{"url": "https://www.instagram.com/p/Df5MwAKiCVI/", "trim": true}'
# 获取故事精选详情
python3 modules/highlight-detail/scripts/highlight_detail.py '{"id": "18125552704906006"}'
# 获取帖子或 Reels 评论
python3 modules/post-comments/scripts/post_comments.py '{"url": "https://www.instagram.com/p/Df5MwAKiCVI/"}'
# 获取指定评论的回复
python3 modules/comment-replies/scripts/comment_replies.py '{"url": "https://www.instagram.com/p/Df5MwAKiCVI/", "comment_id": "18104065796374460"}'
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
- 参数错误时，对照对应子 Skill 的 `references/api.md` 检查必填字段、handle、userId 和帖子链接。
- HTTP、网络、超时、网关错误、`error`、非 `OK` 状态或非 JSON 响应发生时，报告脱敏后的状态码、消息、`requestId` 和 `warnings`，不要把异常或部分数据当作成功。
- 额度或余额不足时，引导用户参考上述使用指南完成充值；不要反复重试或绕过上游限制。

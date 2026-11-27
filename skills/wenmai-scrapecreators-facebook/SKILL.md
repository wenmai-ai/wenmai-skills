---
name: wenmai-scrapecreators-facebook
description: "ScrapeCreators Facebook 社媒标准 API 套件。一个顶层 Skill 索引 23 个子 Skill：主页详情、主页 Reels、主页照片、主页帖子、主页活动、公开视频搜索、帖子详情、帖子字幕、帖子评论、评论回复、群组信息、群组帖子、Marketplace 地点、Marketplace 商品搜索、Marketplace 商品详情、活动搜索、城市活动、活动详情、广告库广告详情、广告库字幕、广告库搜索、公司在投广告、广告主搜索。普通接口每次成功 3 积分。长字幕、get_transcript 和 trim 不要当默认。当用户需要 Facebook 主页、帖子、群组、Marketplace、广告库或提到 ScrapeCreators 时使用；即使用户未明确提及 ScrapeCreators，只要任务需要该数据源也应触发本套件，再按索引只调用所需子 Skill。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
  short-description: 搜主页、帖子、群组、Marketplace 和广告库；按需调用，普通 3 积分。
---

# Facebook 主页与广告调研

## Overview

这是 ScrapeCreators Facebook 的**索引 Skill**。官方包和 Polaris 都只安装这一个顶层 Skill；整个 ZIP 里只能有这一份 `SKILL.md`。
23 个接口的完整契约放在 `modules/<name>/MODULE.md`，不作为独立 Skill 安装，也不要 `load_skill(wenmai-scrapecreators-facebook-xxx)`。

先加载 `$wenmai-scrapecreators-facebook`，再按用户目标只阅读并调用需要的子模块。用户要主页就打主页，要广告库就打广告库；不要因为套件有 23 个接口就全打一遍。`allow_long_transcription`、`get_transcript`、`trim` 不要当默认。

- Platform: Facebook
- Provider: ScrapeCreators
- Auth: Header `secret-key: $WENMAI_API_KEY`
- 总契约: [`references/api.md`](references/api.md)

## 子 Skill 索引

| 场景 | 子 Skill | Endpoint | 稳卖积分 | 脚本 |
|---|---|---|---|---|
| 获取 Facebook 主页详情 | [`modules/profile`](modules/profile/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-profile` | 3 | `modules/profile/scripts/profile.py` |
| 获取 Facebook 主页 Reels | [`modules/profile-reels`](modules/profile-reels/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-profile-reels` | 3 | `modules/profile-reels/scripts/profile_reels.py` |
| 获取 Facebook 主页相册照片 | [`modules/profile-photos`](modules/profile-photos/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-profile-photos` | 3 | `modules/profile-photos/scripts/profile_photos.py` |
| 获取 Facebook 主页帖子 | [`modules/profile-posts`](modules/profile-posts/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-profile-posts` | 3 | `modules/profile-posts/scripts/profile_posts.py` |
| 获取 Facebook 主页活动 | [`modules/profile-events`](modules/profile-events/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-profile-events` | 3 | `modules/profile-events/scripts/profile_events.py` |
| 搜索 Facebook 公开视频和 Reels | [`modules/search-videos`](modules/search-videos/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-search-videos` | 3 | `modules/search-videos/scripts/search_videos.py` |
| 获取 Facebook 帖子或 Reel 详情 | [`modules/post`](modules/post/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-post` | 3 | `modules/post/scripts/post.py` |
| 获取 Facebook 帖子或 Reel 字幕 | [`modules/post-transcript`](modules/post-transcript/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-post-transcript` | 3 | `modules/post-transcript/scripts/post_transcript.py` |
| 获取 Facebook 帖子评论 | [`modules/post-comments`](modules/post-comments/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-post-comments` | 3 | `modules/post-comments/scripts/post_comments.py` |
| 获取指定 Facebook 评论的回复 | [`modules/post-comment-replies`](modules/post-comment-replies/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-post-comment-replies` | 3 | `modules/post-comment-replies/scripts/post_comment_replies.py` |
| 获取 Facebook 公开群组信息 | [`modules/group`](modules/group/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-group` | 3 | `modules/group/scripts/group.py` |
| 获取 Facebook 公开群组帖子 | [`modules/group-posts`](modules/group-posts/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-group-posts` | 3 | `modules/group-posts/scripts/group_posts.py` |
| 搜索 Facebook Marketplace 地点 | [`modules/marketplace-location-search`](modules/marketplace-location-search/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-marketplace-location-search` | 3 | `modules/marketplace-location-search/scripts/marketplace_location_search.py` |
| 搜索 Facebook Marketplace 商品 | [`modules/marketplace-search`](modules/marketplace-search/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-marketplace-search` | 3 | `modules/marketplace-search/scripts/marketplace_search.py` |
| 获取 Facebook Marketplace 商品详情 | [`modules/marketplace-item`](modules/marketplace-item/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-marketplace-item` | 3 | `modules/marketplace-item/scripts/marketplace_item.py` |
| 搜索 Facebook 活动 | [`modules/events-search`](modules/events-search/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-events-search` | 3 | `modules/events-search/scripts/events_search.py` |
| 获取某城市 Facebook 活动 | [`modules/events`](modules/events/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-events` | 3 | `modules/events/scripts/events.py` |
| 获取 Facebook 活动详情 | [`modules/event-details`](modules/event-details/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-event-details` | 3 | `modules/event-details/scripts/event_details.py` |
| 获取 Facebook 广告库广告详情 | [`modules/ad-library-ad`](modules/ad-library-ad/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-ad-library-ad` | 3 | `modules/ad-library-ad/scripts/ad_library_ad.py` |
| 获取 Facebook 广告库视频字幕 | [`modules/ad-library-ad-transcript`](modules/ad-library-ad-transcript/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-ad-library-ad-transcript` | 3 | `modules/ad-library-ad-transcript/scripts/ad_library_ad_transcript.py` |
| 按关键词搜索 Facebook 广告库 | [`modules/ad-library-search-ads`](modules/ad-library-search-ads/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-ad-library-search-ads` | 3 | `modules/ad-library-search-ads/scripts/ad_library_search_ads.py` |
| 获取某公司在 Facebook 广告库的在投广告 | [`modules/ad-library-company-ads`](modules/ad-library-company-ads/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-ad-library-company-ads` | 3 | `modules/ad-library-company-ads/scripts/ad_library_company_ads.py` |
| 在 Facebook 广告库搜索广告主 | [`modules/ad-library-search-companies`](modules/ad-library-search-companies/MODULE.md) | `POST /wmapi/v1/scrapecreators/facebook-ad-library-search-companies` | 3 | `modules/ad-library-search-companies/scripts/ad_library_search_companies.py` |

## 怎么选

1. 已有主页链接：先 `profile`，再按需 `profile-reels`、`profile-photos`、`profile-posts` 或 `profile-events`。
2. 搜公开视频和 Reels：`search-videos`。
3. 已有帖子或 Reel 链接：详情 `post`，字幕 `post-transcript`，评论 `post-comments`；只要某条回复才用评论返回的 `feedback_id` 和 `expansion_token` 打 `post-comment-replies`。
4. 公开群组：`group` 看信息，`group-posts` 看帖子。
5. Marketplace：先 `marketplace-location-search` 拿地点，再 `marketplace-search`，详情 `marketplace-item`。
6. 活动：关键词用 `events-search`，城市页用 `events`，详情 `event-details`。
7. 广告库：搜广告主 `ad-library-search-companies`，搜广告 `ad-library-search-ads`，公司在投优先 `pageId` 打 `ad-library-company-ads`，详情 `ad-library-ad`，字幕 `ad-library-ad-transcript`。
8. `allow_long_transcription` / `get_transcript` / `trim` 用户没点名不要开。

普通接口成功 `costCredit=3`。不要默认开启长字幕。

## Workflow

1. 从用户问题映射到上表中的 1 个子 Skill；链路任务按「主页/搜索 → 帖子/商品/广告 → 字幕/评论」展开，仍只调用当前步骤需要的接口。
2. 阅读对应 `modules/<name>/MODULE.md` 和 `modules/<name>/references/api.md`，不要凭记忆补字段；子模块不是独立 Skill。
3. 在套件根目录运行该子 Skill 脚本，保留原始 JSON。
4. 检查 `code`、`requestId`、`costCredit`；成功应为 3。
5. 摘要必须能追溯到响应字段；缺失就写缺失。

## How To Run

调用 API 前，先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。任一变量存在时直接用于调用，不得展示、复述或记录密钥值；仅当两个环境变量都未获取到时，才请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`，并在本机配置环境变量。不得在未检查环境变量的情况下声称缺少 API Key。Wenmai 个人中心为 https://agent.wenmai-ai.com/；额度或余额不足时，按该指南完成充值。

在套件根目录 `Skills/wenmai-scrapecreators-facebook/` 执行：

```bash
export WENMAI_API_KEY="replace-with-real-wenmai-api-key"
# 获取 Facebook 主页详情
python3 modules/profile/scripts/profile.py '{"url": "https://www.facebook.com/gymshark"}'
# 获取 Facebook 主页 Reels
python3 modules/profile-reels/scripts/profile_reels.py '{"url": "https://www.facebook.com/gymshark"}'
# 获取 Facebook 主页相册照片
python3 modules/profile-photos/scripts/profile_photos.py '{"url": "https://www.facebook.com/gymshark"}'
# 获取 Facebook 主页帖子
python3 modules/profile-posts/scripts/profile_posts.py '{"url": "https://www.facebook.com/gymshark"}'
# 获取 Facebook 主页活动
python3 modules/profile-events/scripts/profile_events.py '{"url": "https://www.facebook.com/gymshark"}'
# 搜索 Facebook 公开视频和 Reels
python3 modules/search-videos/scripts/search_videos.py '{"query": "gymshark"}'
# 获取 Facebook 帖子或 Reel 详情
python3 modules/post/scripts/post.py '{"url": "https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l"}'
# 获取 Facebook 帖子或 Reel 字幕
python3 modules/post-transcript/scripts/post_transcript.py '{"url": "https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l"}'
# 获取 Facebook 帖子评论
python3 modules/post-comments/scripts/post_comments.py '{"url": "https://www.facebook.com/Gymshark/posts/pfbid02mumZ6NPF23mgEothQrt93iBNay3UTttNcPsGerAwEyRpNayz11XZLyb185BEZSc4l", "sort": "most_relevant"}'
# 获取指定 Facebook 评论的回复
python3 modules/post-comment-replies/scripts/post_comment_replies.py '{"feedback_id": "replace-from-comments", "expansion_token": "replace-from-comments"}'
# 获取 Facebook 公开群组信息
python3 modules/group/scripts/group.py '{"url": "https://www.facebook.com/groups/python"}'
# 获取 Facebook 公开群组帖子
python3 modules/group-posts/scripts/group_posts.py '{"url": "https://www.facebook.com/groups/python"}'
# 搜索 Facebook Marketplace 地点
python3 modules/marketplace-location-search/scripts/marketplace_location_search.py '{"query": "Los Angeles"}'
# 搜索 Facebook Marketplace 商品
python3 modules/marketplace-search/scripts/marketplace_search.py '{"query": "gymshark", "lat": 34.0522, "lng": -118.2437}'
# 获取 Facebook Marketplace 商品详情
python3 modules/marketplace-item/scripts/marketplace_item.py '{"id": "1234567890"}'
# 搜索 Facebook 活动
python3 modules/events-search/scripts/events_search.py '{"query": "fitness"}'
# 获取某城市 Facebook 活动
python3 modules/events/scripts/events.py '{"url": "https://www.facebook.com/events/explore/los-angeles-california/112035925469106/", "time": "this_week"}'
# 获取 Facebook 活动详情
python3 modules/event-details/scripts/event_details.py '{"url": "https://www.facebook.com/events/2255360061870188"}'
# 获取 Facebook 广告库广告详情
python3 modules/ad-library-ad/scripts/ad_library_ad.py '{"id": "120229348090250398"}'
# 获取 Facebook 广告库视频字幕
python3 modules/ad-library-ad-transcript/scripts/ad_library_ad_transcript.py '{"id": "120229348090250398"}'
# 按关键词搜索 Facebook 广告库
python3 modules/ad-library-search-ads/scripts/ad_library_search_ads.py '{"query": "gymshark", "country": "US", "trim": true}'
# 获取某公司在 Facebook 广告库的在投广告
python3 modules/ad-library-company-ads/scripts/ad_library_company_ads.py '{"companyName": "Gymshark", "country": "US", "trim": true}'
# 在 Facebook 广告库搜索广告主
python3 modules/ad-library-search-companies/scripts/ad_library_search_companies.py '{"query": "gymshark"}'
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
- 参数错误时，对照对应子 Skill 的 `references/api.md` 检查必填字段、主页/帖子链接、pageId、feedback_id、expansion_token 和 cursor。
- HTTP、网络、超时、网关错误、`error`、非 `OK` 状态或非 JSON 响应发生时，报告脱敏后的状态码、消息、`requestId` 和 `warnings`，不要把异常或部分数据当作成功。
- 额度或余额不足时，引导用户参考上述使用指南完成充值；不要反复重试或绕过上游限制。

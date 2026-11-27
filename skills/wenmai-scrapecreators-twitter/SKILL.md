---
name: wenmai-scrapecreators-twitter
description: "ScrapeCreators Twitter / X 社媒标准 API 套件。一个顶层 Skill 索引 7 个子 Skill：搜索 Google 索引的公开 Twitter / X 帖子、获取 Twitter / X 用户资料、获取用户主页上的热门推文、获取单条 Twitter / X 推文详情、获取视频推文的 AI 转写、获取 Twitter / X 社群详情、获取 Twitter / X 社群帖子。普通接口每次成功 2 积分。长转写和 trim 不要当默认。当用户需要 Twitter 帖子搜索、账号资料、推文详情、视频转写、社群或提到 ScrapeCreators 时使用；即使用户未明确提及 ScrapeCreators，只要任务需要该数据源也应触发本套件，再按索引只调用所需子 Skill。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
  short-description: 搜 Twitter 帖子、账号、转写和社群；按需调用，普通 2 积分。
---

# Twitter 帖子搜索调研

## Overview

这是 ScrapeCreators Twitter 的**索引 Skill**。官方包和 Polaris 都只安装这一个顶层 Skill；整个 ZIP 里只能有这一份 `SKILL.md`。
7 个接口的完整契约放在 `modules/<name>/MODULE.md`，不作为独立 Skill 安装，也不要 `load_skill(wenmai-scrapecreators-twitter-xxx)`。

先加载 `$wenmai-scrapecreators-twitter`，再按用户目标只阅读并调用需要的子模块。用户要搜帖子就打搜索，要账号就打资料；不要因为套件有 7 个接口就全打一遍。`allow_long_transcription` 和 `trim` 不要当默认。

- Platform: Twitter / X
- Provider: ScrapeCreators
- Auth: Header `secret-key: $WENMAI_API_KEY`
- 总契约: [`references/api.md`](references/api.md)

## 子 Skill 索引

| 场景 | 子 Skill | Endpoint | 稳卖积分 | 脚本 |
|---|---|---|---|---|
| 搜索 Google 索引的公开 Twitter / X 帖子 | [`modules/search-posts`](modules/search-posts/MODULE.md) | `POST /wmapi/v1/scrapecreators/twitter-search-posts` | 2 | `modules/search-posts/scripts/search_posts.py` |
| 获取 Twitter / X 用户资料 | [`modules/profile`](modules/profile/MODULE.md) | `POST /wmapi/v1/scrapecreators/twitter-profile` | 2 | `modules/profile/scripts/profile.py` |
| 获取用户主页上的热门推文 | [`modules/user-tweets`](modules/user-tweets/MODULE.md) | `POST /wmapi/v1/scrapecreators/twitter-user-tweets` | 2 | `modules/user-tweets/scripts/user_tweets.py` |
| 获取单条 Twitter / X 推文详情 | [`modules/tweet`](modules/tweet/MODULE.md) | `POST /wmapi/v1/scrapecreators/twitter-tweet` | 2 | `modules/tweet/scripts/tweet.py` |
| 获取视频推文的 AI 转写 | [`modules/tweet-transcript`](modules/tweet-transcript/MODULE.md) | `POST /wmapi/v1/scrapecreators/twitter-tweet-transcript` | 2 | `modules/tweet-transcript/scripts/tweet_transcript.py` |
| 获取 Twitter / X 社群详情 | [`modules/community`](modules/community/MODULE.md) | `POST /wmapi/v1/scrapecreators/twitter-community` | 2 | `modules/community/scripts/community.py` |
| 获取 Twitter / X 社群帖子 | [`modules/community-tweets`](modules/community-tweets/MODULE.md) | `POST /wmapi/v1/scrapecreators/twitter-community-tweets` | 2 | `modules/community-tweets/scripts/community_tweets.py` |

## 怎么选

1. 按关键词搜公开帖子：`search-posts`。这是 Google 索引发现，不是 X 原生搜索。
2. 已有 handle：`profile` 看账号，`user-tweets` 看大约 100 条热门推文。
3. 已有推文链接：详情 `tweet`；视频转写 `tweet-transcript`。
4. 已有社群链接：`community` 看信息，`community-tweets` 看帖子。
5. `allow_long_transcription` / `trim` 用户没点名不要开。长转写会变贵。

普通接口成功 `costCredit=2`。不要默认开启长转写。

## Workflow

1. 从用户问题映射到上表中的 1 个子 Skill；链路任务按「搜索/账号 → 推文 → 转写/社群」展开，仍只调用当前步骤需要的接口。
2. 阅读对应 `modules/<name>/MODULE.md` 和 `modules/<name>/references/api.md`，不要凭记忆补字段；子模块不是独立 Skill。
3. 在套件根目录运行该子 Skill 脚本，保留原始 JSON。
4. 检查 `code`、`requestId`、`costCredit`；成功应为 2。
5. 摘要必须能追溯到响应字段；缺失就写缺失。

## How To Run

调用 API 前，先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。任一变量存在时直接用于调用，不得展示、复述或记录密钥值；仅当两个环境变量都未获取到时，才请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`，并在本机配置环境变量。不得在未检查环境变量的情况下声称缺少 API Key。Wenmai 个人中心为 https://agent.wenmai-ai.com/；额度或余额不足时，按该指南完成充值。

在套件根目录 `Skills/wenmai-scrapecreators-twitter/` 执行：

```bash
export WENMAI_API_KEY="replace-with-real-wenmai-api-key"
# 搜索 Google 索引的公开 Twitter / X 帖子
python3 modules/search-posts/scripts/search_posts.py '{"query": "ai agents"}'
# 获取 Twitter / X 用户资料
python3 modules/profile/scripts/profile.py '{"handle": "levelsio"}'
# 获取用户主页上的热门推文
python3 modules/user-tweets/scripts/user_tweets.py '{"handle": "levelsio"}'
# 获取单条 Twitter / X 推文详情
python3 modules/tweet/scripts/tweet.py '{"url": "https://x.com/levelsio/status/1834021269559501236"}'
# 获取视频推文的 AI 转写
python3 modules/tweet-transcript/scripts/tweet_transcript.py '{"url": "https://x.com/TheoVon/status/1916982720317821050"}'
# 获取 Twitter / X 社群详情
python3 modules/community/scripts/community.py '{"url": "https://x.com/i/communities/1926186499399139650"}'
# 获取 Twitter / X 社群帖子
python3 modules/community-tweets/scripts/community_tweets.py '{"url": "https://x.com/i/communities/1926186499399139650"}'
```

脚本将 Wenmai API 原始响应输出为格式化 JSON。不得把 API Key 写入文件、日志或回答。本地或测试网关可设置 `WENMAI_API_ORIGIN`。

## Request Rules

- 顶层直接传业务字段，不要增加 `request` 包装层。
- 每个子 Skill 的必填字段、分页和枚举以该模块 `references/api.md` 为准。
- 只发送当前子 Skill 文档里的字段，不把其他接口的筛选混进去。
- Search Posts 的 cursor 是 1 到 11，不要拿推文 id 当 cursor。

## Response Rules

- 先报告 `code`、`requestId` 和 `costCredit`。
- 所有摘要值必须能追溯到原始响应字段；缺失字段标记为缺失，不估算、推断或补造。
- 长列表先汇总再按需展开；存在 `warnings` 时原样保留。
- 无转写、空搜索结果或社群帖为空时字段可能为空，这仍可能是成功响应。

## Error Handling

- 调用前先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 参数错误时，对照对应子 Skill 的 `references/api.md` 检查必填字段、handle、推文链接、社群链接和 cursor。
- HTTP、网络、超时、网关错误、`error`、非 `OK` 状态或非 JSON 响应发生时，报告脱敏后的状态码、消息、`requestId` 和 `warnings`，不要把异常或部分数据当作成功。
- 额度或余额不足时，引导用户参考上述使用指南完成充值；不要反复重试或绕过上游限制。

---
name: wenmai-scrapecreators-reddit
description: "ScrapeCreators Reddit 社媒标准 API 套件。一个顶层 Skill 索引 7 个子 Skill：获取 Subreddit 详情、获取 Subreddit 帖子列表、在指定 Subreddit 内搜索、全站搜索 Reddit 帖子或评论、获取 Reddit 帖子详情、获取 Reddit 帖子评论、获取 Reddit 视频帖字幕。普通接口每次成功 2 积分。trim 不要当默认。字幕是原生 VTT，不是 AI 转写。当用户需要 Reddit 社群详情、帖子、评论、字幕、搜索或提到 ScrapeCreators 时使用；即使用户未明确提及 ScrapeCreators，只要任务需要该数据源也应触发本套件，再按索引只调用所需子 Skill。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
  short-description: 查 Subreddit 详情、帖子、评论和搜索；按需调用，普通 2 积分。
---

# Reddit 社群与帖子调研

## Overview

这是 ScrapeCreators Reddit 的**索引 Skill**。官方包和 Polaris 都只安装这一个顶层 Skill；整个 ZIP 里只能有这一份 `SKILL.md`。
7 个接口的完整契约放在 `modules/<name>/MODULE.md`，不作为独立 Skill 安装，也不要 `load_skill(wenmai-scrapecreators-reddit-xxx)`。

先加载 `$wenmai-scrapecreators-reddit`，再按用户目标只阅读并调用需要的子模块。用户要社群详情就打 details，要帖子就打列表或搜索；不要因为套件有 7 个接口就全打一遍。`trim` 不要当默认。

- Platform: Reddit
- Provider: ScrapeCreators
- Auth: Header `secret-key: $WENMAI_API_KEY`
- 总契约: [`references/api.md`](references/api.md)

## 子 Skill 索引

| 场景 | 子 Skill | Endpoint | 稳卖积分 | 脚本 |
|---|---|---|---|---|
| 获取 Subreddit 详情 | [`modules/subreddit-details`](modules/subreddit-details/MODULE.md) | `POST /wmapi/v1/scrapecreators/reddit-subreddit-details` | 2 | `modules/subreddit-details/scripts/subreddit_details.py` |
| 获取 Subreddit 帖子列表 | [`modules/subreddit`](modules/subreddit/MODULE.md) | `POST /wmapi/v1/scrapecreators/reddit-subreddit` | 2 | `modules/subreddit/scripts/subreddit.py` |
| 在指定 Subreddit 内搜索 | [`modules/subreddit-search`](modules/subreddit-search/MODULE.md) | `POST /wmapi/v1/scrapecreators/reddit-subreddit-search` | 2 | `modules/subreddit-search/scripts/subreddit_search.py` |
| 全站搜索 Reddit 帖子或评论 | [`modules/search`](modules/search/MODULE.md) | `POST /wmapi/v1/scrapecreators/reddit-search` | 2 | `modules/search/scripts/search.py` |
| 获取 Reddit 帖子详情 | [`modules/post`](modules/post/MODULE.md) | `POST /wmapi/v1/scrapecreators/reddit-post` | 2 | `modules/post/scripts/post.py` |
| 获取 Reddit 帖子评论 | [`modules/post-comments`](modules/post-comments/MODULE.md) | `POST /wmapi/v1/scrapecreators/reddit-post-comments` | 2 | `modules/post-comments/scripts/post_comments.py` |
| 获取 Reddit 视频帖字幕 | [`modules/post-transcript`](modules/post-transcript/MODULE.md) | `POST /wmapi/v1/scrapecreators/reddit-post-transcript` | 2 | `modules/post-transcript/scripts/post_transcript.py` |

## 怎么选

1. 已有社群名：详情 `subreddit-details`（大小写敏感），帖子列表 `subreddit`，社群内搜索 `subreddit-search`。
2. 全站搜帖子或评论：`search`。
3. 已有帖子链接：详情 `post`，评论 `post-comments`；视频字幕 `post-transcript`。
4. `trim` 用户没点名不要开。字幕不是 AI 转写，没有 VTT 就记缺失。

普通接口成功 `costCredit=2`。不要默认开启 trim。

## Workflow

1. 从用户问题映射到上表中的 1 个子 Skill；链路任务按「社群/搜索 → 帖子 → 评论/字幕」展开，仍只调用当前步骤需要的接口。
2. 阅读对应 `modules/<name>/MODULE.md` 和 `modules/<name>/references/api.md`，不要凭记忆补字段；子模块不是独立 Skill。
3. 在套件根目录运行该子 Skill 脚本，保留原始 JSON。
4. 检查 `code`、`requestId`、`costCredit`；成功应为 2。
5. 摘要必须能追溯到响应字段；缺失就写缺失。

## How To Run

调用 API 前，先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。任一变量存在时直接用于调用，不得展示、复述或记录密钥值；仅当两个环境变量都未获取到时，才请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`，并在本机配置环境变量。不得在未检查环境变量的情况下声称缺少 API Key。Wenmai 个人中心为 https://agent.wenmai-ai.com/；额度或余额不足时，按该指南完成充值。

在套件根目录 `Skills/wenmai-scrapecreators-reddit/` 执行：

```bash
export WENMAI_API_KEY="replace-with-real-wenmai-api-key"
# 获取 Subreddit 详情
python3 modules/subreddit-details/scripts/subreddit_details.py '{"subreddit": "AskReddit"}'
# 获取 Subreddit 帖子列表
python3 modules/subreddit/scripts/subreddit.py '{"subreddit": "AskReddit", "sort": "hot"}'
# 在指定 Subreddit 内搜索
python3 modules/subreddit-search/scripts/subreddit_search.py '{"subreddit": "AskReddit", "query": "amazon"}'
# 全站搜索 Reddit 帖子或评论
python3 modules/search/scripts/search.py '{"query": "gymshark", "filter": "posts"}'
# 获取 Reddit 帖子详情
python3 modules/post/scripts/post.py '{"url": "https://www.reddit.com/r/AskReddit/comments/1xzu5c9/mamdani_wants_to_have_social_workers_handle/"}'
# 获取 Reddit 帖子评论
python3 modules/post-comments/scripts/post_comments.py '{"url": "https://www.reddit.com/r/AskReddit/comments/1xzu5c9/mamdani_wants_to_have_social_workers_handle/"}'
# 获取 Reddit 视频帖字幕
python3 modules/post-transcript/scripts/post_transcript.py '{"url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/football_nostalgiasa", "language": "en"}'
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

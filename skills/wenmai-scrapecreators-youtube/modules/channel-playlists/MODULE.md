---
name: wenmai-scrapecreators-youtube-channel-playlists
description: "ScrapeCreators YouTube 套件内的获取 YouTube 频道播放列表子 Skill，调用 `scrapecreators_youtube_channel_playlists`。固定 `POST /wmapi/v1/scrapecreators/youtube-channel-playlists`。每次成功调用扣 3 稳卖积分。从属于 `$wenmai-scrapecreators-youtube`，不作为独立顶层 Skill 安装。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# ScrapeCreators YouTube 获取 YouTube 频道播放列表

## Overview

调用 Wenmai ScrapeCreators YouTube standard API `scrapecreators_youtube_channel_playlists`。只调用以下固定端点，不接受动态端点或其他操作：

- Platform: YouTube
- Provider: ScrapeCreators
- Endpoint: `POST /wmapi/v1/scrapecreators/youtube-channel-playlists`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Parent: `$wenmai-scrapecreators-youtube`
- Script: `modules/channel-playlists/scripts/channel_playlists.py`
- API contract: [`references/api.md`](references/api.md)

在构造请求或解释字段前阅读 `references/api.md`，以其中的参数、限制、响应字段和错误定义为事实来源。

## Workflow

1. 提取并校验用户输入，保留用户指定的频道 handle、视频链接、话题、clip/playlist 和分页。
2. 按照 API 契约构造顶层 JSON 请求，不要额外包一层 `request`。
3. 对照 API 契约处理数量、分页、枚举和标识符；不静默截断或添加未定义字段。
4. 运行固定脚本并保留原始 JSON 响应。
5. 检查网关状态、`requestId`、`costCredit`、分页/返回数量及 `warnings`。
6. 将结果映射回响应字段，按用户决策目的输出紧凑、可追溯的摘要。

## How To Run

调用 API 前，先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。任一变量存在时直接用于调用，不得展示、复述或记录密钥值；仅当两个环境变量都未获取到时，才请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`，并在本机配置环境变量。不得在未检查环境变量的情况下声称缺少 API Key。Wenmai 个人中心为 https://agent.wenmai-ai.com/；额度或余额不足时，按该指南完成充值。

```bash
export WENMAI_API_KEY="replace-with-real-wenmai-api-key"
python3 modules/channel-playlists/scripts/channel_playlists.py '{"handle": "gymshark"}'
```

脚本将 Wenmai API 原始响应输出为格式化 JSON。不得把 API Key 写入文件、日志或回答。

## Request Rules

- 必填规则：`channelId` 与 `handle` 二选一。
- 顶层直接传业务字段，不要增加 `request` 包装层，也不要把内部字段提升或改名。
- 保留用户指定的频道 handle、视频链接、话题、播放列表、分页、筛选和地区；缺少会改变查询范围的值时先询问，不自行猜测。
- 仅发送 `references/api.md` 定义的字段、类型、枚举值及受支持组合。
- 获取频道播放列表。每次成功扣 3 稳卖积分。

## Response Rules

- 先报告 `code`、`requestId` 和 `costCredit`。此接口成功时 `costCredit` 应为 `3`。
- 按用户决策目的展示关键字段，同时保留原始字段名和值。
- 仅在响应存在时展示 `warnings`、分页、返回数量和数据完整性字段。
- 明确区分成功、部分失败、未解析输入、截断和数据不完整；长数组需要摘要时说明覆盖范围，不静默遗漏或合并记录。
- 所有摘要值必须能追溯到原始响应字段；缺失字段标记为缺失，不估算、推断或补造。

## Error Handling

- 调用前先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 参数错误时，对照 `references/api.md` 检查必填字段、handle、channelId、视频链接、continuationToken 和分页。
- HTTP、网络、超时、网关错误、`error`、非 `OK` 状态或非 JSON 响应发生时，报告脱敏后的状态码、消息、`requestId` 和 `warnings`，不要把异常或部分数据当作成功。
- 额度或余额不足时，引导用户参考上述使用指南完成充值；不要反复重试或绕过上游限制。

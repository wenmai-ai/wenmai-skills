---
name: wenmai-yy-review-monitor
description: "YY数据Amazon 评论抓取接口：按 1 个 ASIN 提交评论抓取任务，异步抓取最新评论（每页 10 条，1～10 页，最多 100 条），可选整个 listing 全部变体或只抓所传 ASIN 这个变体；返回评论标题、正文、星级、日期、评论人、Verified Purchase、有用数、图片和视频，并用 review_asin、format_text 标明每条评论所属变体，同时返回评分、评分数和星级分布。支持按任务 ID 查询抓取进度、按评论日期和星级筛选取评论、查询抓取次数。当用户提到 Amazon 评论抓取、ASIN 最新评论、差评分析、变体评论、评论监控、VOC、竞品口碑或 YY 评论时触发此技能。即使用户未明确提及YY数据，只要任务需要抓取 Amazon 商品评论，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Wenmai 数据Amazon 评论抓取

## Overview

调用 Wenmai 数据评论监控 standard API。评论抓取是异步任务，只调用以下 4 个固定端点，不接受动态端点或其他操作：

| 步骤 | Endpoint | Script |
|------|----------|--------|
| 提交抓取任务 | `POST /wmapi/v1/yy/add-review-monitor-asins` | `scripts/add_review_monitor_asins.py` |
| 查询任务进度 | `POST /wmapi/v1/yy/get-review-monitor-tasks` | `scripts/get_review_monitor_tasks.py` |
| 获取评论 | `POST /wmapi/v1/yy/get-monitor-asin-reviews` | `scripts/get_monitor_asin_reviews.py` |
| 查询抓取次数 | `POST /wmapi/v1/yy/get-review-crawl-count` | `scripts/get_review_crawl_count.py` |

- 一键流程：`scripts/crawl_reviews.py` 依次提交、轮询、取评论。
- Auth: Header `secret-key: $WENMAI_API_KEY`
- API contract: [`references/api.md`](references/api.md)

在构造请求或解释字段前阅读 `references/api.md`，以其中的参数、限制、响应字段和错误定义为事实来源。

## Workflow

1. 提取 ASIN、站点、要抓的评论条数和变体范围。站点用数字编号字符串（`"1"` 美国站），条数换算为页数 `review_end_num` = 条数 ÷ 10 向上取整，最多 10 页；用户要全部变体还是只看这个变体不明确时先询问。
2. 每次只提交 1 个 ASIN；多个 ASIN 逐个提交，并告知用户每个 ASIN 单独计费。
3. 优先运行 `scripts/crawl_reviews.py`：它提交任务、每 30 秒查一次 `has_rel`，抓取完成（`has_rel=2`）后取评论并输出全部原始响应。
4. 已有任务 ID（`aid`）时，用 `crawl_reviews.py --aid <aid>` 或单步脚本继续，不要重复提交同一 ASIN。
5. 检查每一步的 `code`、`requestId`、`costCredit`，以及任务的 `has_rel`、`page_num`、`rev_cnt`。
6. 基于 `reviews` 原始字段输出可追溯的摘要；按变体分析时以 `review_asin`、`format_text` 分组。

## How To Run

调用 API 前，先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。任一变量存在时直接用于调用，不得展示、复述或记录密钥值；仅当两个环境变量都未获取到时，才请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`，并在本机配置环境变量。不得在未检查环境变量的情况下声称缺少 API Key。Wenmai 个人中心为 https://agent.wenmai-ai.com/；额度或余额不足时，按该指南完成充值。

```bash
export WENMAI_API_KEY=sk-...
# 一键：提交 B085DTZQNZ 抓 2 页（20 条），完成后只取 1～3 星评论
python3 scripts/crawl_reviews.py '{"station": "1", "asins": ["B085DTZQNZ"], "review_end_num": 2}' '{"star_start": 1, "star_end": 3}'
# 超时后继续已提交的任务（不会重新提交）
python3 scripts/crawl_reviews.py --aid 67124951
# 单步调用
python3 scripts/add_review_monitor_asins.py '{"station": "1", "asins": ["B085DTZQNZ"], "review_end_num": 1, "format_restrict": 1}'
python3 scripts/get_review_monitor_tasks.py '{"aids": [67124951]}'
python3 scripts/get_monitor_asin_reviews.py '{"aids": [67124951], "review_date_start": "2026-10-01"}'
```

脚本将 Wenmai API 原始响应输出为格式化 JSON；`crawl_reviews.py` 把各步骤原始响应合并为一个 JSON，进度写到 stderr，仍在抓取时以退出码 3 结束并给出续查命令。不得把 API Key 写入文件、日志或回答。

## Request Rules

- 提交：`station`、`asins` 必填；`asins` 只能有 1 个 ASIN。`review_end_num` 取值 1～10，未传按 1 页；用户要 100 条就传 10，不超过 10 页。
- `format_restrict`：0（默认）返回所传 ASIN 所属 listing 全部变体的评论；1 只返回所传 ASIN 这个变体本身的评论。保留用户指定的值。
- `craw_all_review`、`review_date_start`、`collect_source`、`language`、`site_restrict`、`priority` 只在用户指定时发送，取值以 `references/api.md` 为准。
- 查询类接口传 `aids`（任务 ID 整数数组，最多 100 个）；获取评论可加 `review_date_start`、`review_date_end`（年-月-日）和 `star_start`、`star_end`（1～5）。
- 仅发送 `references/api.md` 定义的字段，不把查询筛选放进提交请求。

## Response Rules

- 说明实际抓取页数 `page_num` 和返回条数；条数少于页数 × 10 时如实说明是评论不足，不补造。
- `rev_cnt`、`rating_str` 是 Amazon 页面展示的评论数（listing 超过 1 万时为 10000），`rating_cnt` 是评分总数，不要混为同一口径。
- 按变体统计时以 `review_asin` 分组，并给出 `format_text`；两者为空的评论单列为「无规格信息」，不归入任何变体。
- 评论按时间从新到旧；摘要时注明覆盖的日期范围和星级分布，长列表先汇总再按需展开。
- 所有摘要值必须能追溯到原始响应字段；缺失字段标记为缺失，不估算、推断或补造。

## Error Handling

- 调用前先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 参数错误（如 `REQ_001`）时，对照 `references/api.md` 检查：一次只能 1 个 ASIN、站点编号、`aids` 数量、`review_end_num` 范围。
- 任务超过 10 分钟仍为 `has_rel=0` 或 1 时，告知用户任务在供应商侧排队，给出 `aid` 和续查命令；不要重复提交。
- HTTP、网络、超时、网关错误、非 `OK` 状态或非 JSON 响应发生时，报告脱敏后的状态码、消息和 `requestId`，不要把异常或部分数据当作成功。
- 额度或余额不足时，引导用户参考上述使用指南完成充值；不要反复重试或绕过上游限制。

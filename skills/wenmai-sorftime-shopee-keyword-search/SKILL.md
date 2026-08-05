---
name: wenmai-sorftime-shopee-keyword-search
description: "Sorftime Shopee 热搜关键词榜单接口，通过固定 Wenmai standard API `shopee_keyword_search` 返回可追溯的原始网关数据。用于与该能力相关的数据查询、核验、分析或报告；当用户需要热搜关键词榜单或调用该接口时触发。即使用户未明确提及 Sorftime，只要任务需要上述接口能力，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# Sorftime shopee_keyword_search

## Overview

调用 Wenmai Sorftime standard API `shopee_keyword_search`。只调用以下固定端点，不接受动态端点或其他操作：

- Endpoint: `POST /wmapi/v1/sorftime/shopee-keyword-search`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/shopee_keyword_search.py`
- API contract: [`references/api.md`](references/api.md)

在构造请求或解释字段前阅读 `references/api.md`，以其中的参数、限制、响应字段和错误定义为事实来源。

## Workflow

1. 提取并校验用户输入，保留用户指定的平台、市场、标识符和查询范围。
2. 按照 API 契约构造 JSON 请求，保留文档要求的包装层和字段层级。
3. 对照 API 契约处理数量、长度、分页、日期和枚举限制；不静默截断或添加未定义字段。
4. 运行固定脚本并保留原始 JSON 响应。
5. 检查网关状态、`requestId`、实际市场、分页/返回数量及 `warnings`。
6. 将结果映射回响应字段，按用户决策目的输出紧凑、可追溯的摘要。

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；Wenmai 个人中心为 https://agent.wenmai-ai.com/。额度或余额不足时，按该指南完成充值。运行脚本前，将 key 导出为 `WENMAI_API_KEY`（或兼容的 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY="replace-with-real-wenmai-api-key"
python3 scripts/shopee_keyword_search.py '{"site":"TH"}'
```

脚本将 Wenmai API 原始响应输出为格式化 JSON。不得把 API Key 写入文件、日志或回答。

## Request Rules

- 必填字段、条件必填规则、默认值和允许值以 `references/api.md` 为准。
- 保留 API 契约要求的包装层和字段层级，不把内部字段提升到顶层。
- 保留用户指定的平台、市场、标识符、日期、分页、筛选、排序和返回数量；缺少会改变查询范围的值时先询问，不自行猜测。
- 对照 API 契约处理数量、长度、分页、日期和枚举限制；不静默截断、扩展、偏移或拆分请求。
- 仅发送 `references/api.md` 定义的字段、类型、枚举值及受支持组合。

## Response Rules

- 按用户决策目的展示关键字段，同时保留原始字段名和值。
- 仅在响应存在时展示 `warnings`、`requestId`、实际市场、时间窗口、分页、返回数量、规范化标识符、币种、单位和数据完整性字段。
- 明确区分成功、部分失败、未解析输入、截断和数据不完整；长数组需要摘要时说明覆盖范围，不静默遗漏或合并记录。
- 所有摘要值必须能追溯到原始响应字段；缺失字段标记为缺失，不估算、推断或补造。

## Error Handling

- 缺少凭据时，提示设置 `WENMAI_API_KEY` 或 `WENMAI_SECRET_KEY`，不要要求用户在对话中粘贴密钥。
- 参数错误时，对照 `references/api.md` 检查必填字段、包装层、字段类型、枚举值、市场、日期和分页限制。
- HTTP、网络、超时、网关错误、`error`、非 `OK` 状态或非 JSON 响应发生时，报告脱敏后的状态码、消息、`requestId` 和 `warnings`，不要把异常或部分数据当作成功。
- 额度或余额不足时，引导用户参考上述使用指南完成充值；不要反复重试或绕过上游限制。

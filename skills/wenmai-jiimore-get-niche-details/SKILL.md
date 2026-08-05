---
name: wenmai-jiimore-get-niche-details
description: "极目数据（JIIMORE）Amazon 细分市场详情接口，按 niche ID 返回市场需求、价格区间、商品/品牌数量、多周期搜索/销量/点击、转化与集中度、广告/新品/退货/CPC、趋势、潜力信号及正负面评论洞察。用于 niche 详情、市场规模、竞争格局、机会评估或 VOC 分析。即使用户未明确提及 JIIMORE，只要任务需要上述接口能力，也应触发此技能。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# 极目数据（JIIMORE）Amazon 细分市场详情

## Overview

调用 Wenmai 极目数据（JIIMORE）standard API `jiimore_get_niche_details`。只调用以下固定端点，不接受动态端点或其他操作：

- Endpoint: `POST /wmapi/v1/jiimore/niche-details`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/jiimore_get_niche_details.py`
- API contract: [`references/api.md`](references/api.md)

在构造请求或解释字段前阅读 `references/api.md`，以其中的参数、限制、响应字段和错误定义为事实来源。

## Workflow

1. 提取并校验用户输入，保留用户指定的 Amazon 市场和查询范围。
2. 使用必需的 `request` 包装层构造请求，不把内部字段提升到顶层。
3. 对照 API 契约处理数量、长度、分页和枚举限制；不静默截断或添加未定义字段。
4. 运行固定脚本并保留原始 JSON 响应。
5. 检查网关状态、`requestId`、实际 `countryCode`、分页/返回数量及 `warnings`。
6. 将结果映射回响应字段，按用户决策目的输出紧凑、可追溯的摘要。

## How To Run

请参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 `secret-key`；额度或余额不足时，按该指南完成充值。运行脚本前，将 key 导出为 `WENMAI_API_KEY`（或兼容的 `WENMAI_SECRET_KEY`）。

```bash
export WENMAI_API_KEY=sk-...
python3 scripts/jiimore_get_niche_details.py '{"request": {"nicheId": "sample-niche", "countryCode": "US"}}'
```

脚本将 Wenmai API 原始响应输出为格式化 JSON。不得把 API Key 写入文件、日志或回答。

## Request Rules

- 必须保留 `request` 包装层。
- `request.nicheId` 必填，必须非空且最多 128 字符。
- `request.countryCode` 可选；如用户未指定则省略，使用服务端默认市场，不自行假设。
- 若接口支持 `request.page` 和 `request.pageSize`，页码从 1 开始，`pageSize` 范围为 1～50；保留用户指定值。
- 仅发送 `references/api.md` 定义的字段。

## Response Rules

- 按基础市场指标、趋势、潜力信号、正面评论主题和负面评论主题分组展示。
- 保留评论主题的 `percentOfMentions` 与支撑原句 `verbatims`，不要把洞察改写成未经数据支持的结论。
- 明确区分响应中的时间窗口、币种、单位和指标口径，不混用不同周期。
- 保留实际市场、分页、`returnedRows`、规范化标识符和数据完整性字段；仅在响应存在时展示。
- 始终报告 `warnings`；将未解析输入、截断、部分失败或数据不完整与成功结果区分开。
- 所有摘要值必须能追溯到原始响应字段；缺失字段标记为缺失，不估算或补造。

## Error Handling

- 缺少凭据时，提示设置 `WENMAI_API_KEY` 或 `WENMAI_SECRET_KEY`，不要要求用户在对话中粘贴密钥。
- 参数错误时，检查 `request` 包装层、必填字段、格式及接口限制。
- HTTP、网关错误、`error` 或非 `OK` 状态发生时，报告脱敏后的状态码、消息和 `requestId`，并给出可操作的参数修正建议。
- 额度或余额不足时，引导用户参考上述使用指南完成充值。

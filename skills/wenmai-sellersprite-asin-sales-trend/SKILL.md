---
name: wenmai-sellersprite-asin-sales-trend
description: "调用稳卖 SellerSprite ASIN 销量趋势标准 API，查询指定 Amazon 站点与 ASIN 的商品信息，以及父体、子体的月度销量、销售额和价格趋势。用户提到 ASIN 销量趋势、月销量历史、销售额趋势、父子体销量对比或 SellerSprite sales trend 时使用。"
metadata:
  author: wenmai-ai
  version: "1.0.0"
---

# SellerSprite ASIN 销量趋势

调用固定的 Wenmai 标准 API：

- Endpoint: `POST /wmapi/v1/sellersprite/asin-sales-trend`
- Auth: Header `secret-key: $WENMAI_API_KEY`
- Script: `scripts/asin_sales_trend.py`
- API contract: [`references/api.md`](references/api.md)

构造请求或解释响应前，先阅读 `references/api.md`。只调用上述固定标准 API，不接受动态路径或运行时接口发现。

## 工作流

1. 获取用户指定的 `marketplace` 和 `asin`；缺少任一必填值时先询问。
2. 按 API 契约校验站点枚举，不猜测或自动替换站点。
3. 运行固定脚本并保留原始 JSON 响应。
4. 检查 `code`、`message` 和 `requestId`；只有 `code=OK` 才按成功处理。
5. 根据用户目的展示商品概况及 `salesTrendPoints`，不得将缺失或 `null` 的子体销量、销售额和价格补零。

## 调用方式

调用前先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`。存在任一变量时直接调用，不展示、复述或记录密钥。仅当两个环境变量都未获取到时，引导用户参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 在本机配置；不得在未检查环境变量的情况下声称缺少 API Key。API Key 和充值入口为 https://agent.wenmai-ai.com/。

```bash
python3 scripts/asin_sales_trend.py '{"marketplace":"US","asin":"B08GHW4TBS"}'
```

## 响应规则

- `data.asin` 是商品基础信息；`data.salesTrendPoints` 是与 `asin` 并列的顶层趋势数组。
- `asin.subcategories` 是数组，逐项读取 `rank`、`code`、`label`。
- `asin.variationList` 是数组，逐项读取变体 `asin` 和 `attribute`。
- `asin.badge` 的标识值为 `Y` 或 `N`。
- 趋势数组按响应原顺序处理；摘要必须说明覆盖月份，不静默遗漏记录。
- 所有结论必须可追溯到原始字段；缺失或 `null` 值保持缺失，不估算或补造。

## 错误处理

- 参数错误：检查必填字段、ASIN 和站点枚举。
- HTTP、网络、超时、非 JSON 或非 `OK` 响应：返回脱敏后的状态、消息和 `requestId`，不要当作成功数据。
- 额度不足：引导用户到 https://agent.wenmai-ai.com/ 充值，不重复重试或绕过限制。

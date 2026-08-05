# Wenmai SIF `analyze_traffic_anomaly` API 参考

所有流量变化分析的主入口工具。功能：对 ASIN 进行端到端的流量下跌根因分析——自动识别异常窗口，从广告侧、自然侧、关键词侧逐层拆因。注意：判断逻辑仍在持续迭。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/analyze-traffic-anomaly`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`analyze_traffic_anomaly`
- **脚本入口**：`scripts/analyze_traffic_anomaly.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | ASIN，例如 B0CLPGQWNB。 |
| `country` | string | 否 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |
| `time_type` | string；可选值：“all”、“week”、“month” | 否 | 时间类型：all / week / month；枚举含义：all=配合 days 使用回顾天数窗口，week=按指定周查询，month=按指定月查询。 |
| `time_value` | string | 否 | 时间值，time_type=week 时填周日日期（SIF 数据以周日为每周第一天，当周数据因T+1延迟不可用，如需查当周请使用近7天），如 '2026-03-29'；time_type=month 时填月份首日。 |
| `days` | integer | 否 | 回顾天数（与 time_type=all 搭配使用）。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `reasoning` | string | reasoning。 |
| `conclusion` | string | 结论。 |
| `recommendedAction` | string | recommendedAction。 |
| `scene` | string | 分析场景。 |
| `asin` | string | 目标 ASIN。 |
| `country` | string | 站点代码。 |
| `depth_reached` | integer | 已下钻分析深度。 |
| `judgment` | object | 判断结果对象。 |
| `judgment.conclusion` | string | 结论。 |
| `judgment.confidence` | string | 置信度。 |
| `evidence[]` | array | 证据说明。 |
| `evidence[].layer` | string | 证据层级。 |
| `evidence[].signal` | string | 信号。 |
| `evidence[].value` | string | 特征值。 |
| `evidence[].weight` | string | 权重。 |
| `recommendation` | object | 建议对象。 |
| `recommendation.action` | string | 建议动作。 |
| `recommendation.priority` | string | 优先级。 |
| `confidence_gaps[]` | string | 置信度缺口列表。 |

## 使用要点

- 必填字段：`asin`。
- 保留源文档字段名、类型和层级；数组字段以 `[]` 标识。
- 结果摘要必须保留到原始响应字段的映射，不推断缺失值。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 设置 `WENMAI_API_KEY` 或兼容的 `WENMAI_SECRET_KEY`，不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/ 充值。 |
| 参数错误 | 按请求表检查必填字段、字段类型、站点、日期和分页范围。 |
| HTTP、网络或超时错误 | 保留状态码和脱敏错误摘要，检查网关地址、网络和超时配置。 |
| 响应不是 JSON | 停止解析并报告响应格式错误，不把异常正文当作业务数据。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/analyze-traffic-anomaly" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

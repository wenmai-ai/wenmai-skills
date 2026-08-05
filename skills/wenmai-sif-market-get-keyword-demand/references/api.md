# Wenmai SIF `market_get_keyword_demand` API 参考

需求判断层——回答'这个词的需求处于什么生命周期阶段，是在增长、在萎缩还是只是季节性低谷，以及现在是进场、加速、收割还是收缩的时机'。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-keyword-demand`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`market_get_keyword_demand`
- **脚本入口**：`scripts/market_get_keyword_demand.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keywords` | array<string> | 是 | 关键词列表，1-20 个。 |
| `country` | string | 否 | 站点代码，如 US（默认 US）。 |

## 请求示例

```json
{
  "keywords": [
    "wireless earbuds"
  ]
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `keyword` | string | 该字段在不同返回分支中的含义：关键词原文；或关键词。 |
| `data_coverage` | string | 数据覆盖范围 |
| `weeks` | string | 覆盖了多少周的历史数据，越多分析越可靠 |
| `years` | string | 折合几年 |
| `current` | string | 当前时点状态 |
| `search_volume` | string | 当前这一期的搜索量数值 |
| `season_position` | string | 当前处于一年中哪个季节位置（如旺季/淡季/过渡期） |
| `vs_seasonal_baseline` | string | 当前搜索量比同期历史正常水平高多少或低多少， |
| `trend` | string | 长期趋势（基于多年数据的整体走向） |
| `direction` | string；可选值：growing、declining、stable | direction分类：growing（需求趋势上升）、declining（需求趋势下降）、stable（需求趋势平稳）。 |
| `yoy_change` | string | 同比变化率，即今年与去年同期相比涨跌幅百分比 |
| `annual_decay_rate` | string | 若趋势为下降，平均每年衰减的幅度（百分比） |
| `strength` | string；可选值：strong、moderate、weak | 该字段在不同返回分支中的含义：strength分类：strong（强趋势）、moderate（中等趋势）、weak（弱趋势）；或strength分类：strong（强趋势）、moderate（中等趋势）、weak（弱趋势）。 |
| `momentum` | string | 近期动量，即最近几周的走势相对于长期趋势的变化： |
| `seasonality` | string | 季节性特征 |
| `peak_months` | string | 历史上搜索量最高的月份列表（可能有多个，如圣诞词可能是 11、12 月） |
| `trough_months` | string | 历史上搜索量最低的月份列表（淡季月份） |
| `amplitude` | string | 峰值与谷值之间的搜索量差异幅度，越大说明季节性越剧烈 |
| `diagnosis` | string | 需求生命周期诊断标签（见下方含义说明） |
| `interpretation` | string | 系统生成的中文解读，直接面向用户输出，无需自行重新组织语言 |
| `current_phase` | string；可选值：rising、peak、falling、trough | 当前值phase分类：rising（需求上升阶段）、peak（需求峰值阶段）、falling（需求回落阶段）、trough（需求低谷阶段）。 |
| `weeks_to_peak` | string | 该字段在不同返回分支中的含义：距下一个历史峰值还有多少周，0 表示当前已处于峰值区间；或距峰值周数（越小越紧迫）。 |
| `peak_month` | string | 时机信号判断所依据的主要峰值月份（单个月份，与 seasonality.peak_months 的区别： |
| `trough_month` | string | 时机信号判断所依据的主要低谷月份 |
| `action_phase` | string | 内部阶段标签（不得直接展示给用户）： |
| `action_hint` | string | 该字段在不同返回分支中的含义：根据关键词需求趋势生成的建议动作；或行动建议。 |
| `seasonal_strength` | string；可选值：high、moderate、low | seasonalstrength分类：high（季节性信号高度可信）、moderate（季节性信号具有一定参考价值）、low（季节性信号较弱）。 |
| `timing_summary[]` | array | 按 weeks_to_peak 升序排列的摘要，最紧迫的排最前面 |

## 使用要点

- 必填字段：`keywords`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-keyword-demand" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords":["wireless earbuds"]}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

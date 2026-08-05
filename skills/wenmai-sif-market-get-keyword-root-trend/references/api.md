# Wenmai SIF `market_get_keyword_root_trend` API 参考

需求边界层——回答'这个词背后的整个市场有多大，买家需求是集中在精确词上，还是分散在大量长尾变体词里'。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-keyword-root-trend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`market_get_keyword_root_trend`
- **脚本入口**：`scripts/market_get_keyword_root_trend.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keyword` | string | 是 | 关键词（单个）。 |
| `country` | string | 否 | 站点代码，如 US（默认 US）。 |
| `granularity` | string；可选值：“week”、“month” | 否 | 时间粒度：week / month（默认 week）；枚举含义：week=按周汇总，month=按月汇总。 |

## 请求示例

```json
{
  "keyword": "wireless earbuds"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `keyword` | string | 关键词原文 |
| `data_points` | string | 历史数据点总数 |
| `dates[]` | array | 时间周期列表，按升序排列 |
| `keyword_search_volumes[]` | array | 精确词每期 ABA 搜索量，与 dates 一一对应 |
| `keyword_ranks[]` | array | 精确词每期 ABA 排名，与 dates 一一对应 |
| `ext_search_volumes[]` | array | 词根下所有变体词每期综合搜索量，与 dates 一一对应 |
| `latest` | string | 最新一期快照 |
| `date` | string | 最新数据日期 |
| `keyword_search_volume` | string | 精确词最新搜索量 |
| `keyword_rank` | string | 精确词最新 ABA 排名（0 = 未入榜） |
| `ext_search_volume` | string | 词根综合搜索量最新值 |
| `coverage_ratio` | string | 精确词搜索量 ÷ 词根综合量，取值 0-1 |

## 使用要点

- 必填字段：`keyword`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/market-get-keyword-root-trend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword":"wireless earbuds"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

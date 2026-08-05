# Wenmai SellerSprite `keyword_research_trends` API 参考

关键词选品-关键词的趋势数据，包含：搜索量，购买量，购买率，同比增长率，环比增长率，三个月增长率。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keyword-research-trends`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`keyword_research_trends`
- **脚本入口**：`scripts/keyword_research_trends.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN、MX、BR、AU、AE | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `keyword` | string | 是 | keyword |

## 请求示例

```json
{
  "keyword": "wireless earbuds",
  "marketplace": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `time` | string | 关键词趋势时间点。 |
| `keywrod` | string | 关键词文本。 |
| `keywrodCn` | string | 关键词-中文。 |
| `keywrodJp` | string | 关键词-日文。 |
| `search` | integer | 搜索量。 |
| `purchase` | number | 购买量。 |
| `purchaseRate` | number | 购买率。 |
| `yearlyGrowth` | number | 同比增长率。 |
| `chainGrowth` | number | 环比增长率。 |
| `threeMonthGrowth` | number | 三个月增长率。 |

## 使用要点

- 必填字段：`marketplace`, `keyword`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keyword-research-trends" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword":"wireless earbuds","marketplace":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

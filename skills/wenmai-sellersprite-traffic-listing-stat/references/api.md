# Wenmai SellerSprite `traffic_listing_stat` API 参考

用于分析 Amazon ASIN 的流量来源结构，包括免费流量、付费流量和关联类型分布。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-listing-stat`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`traffic_listing_stat`
- **脚本入口**：`scripts/traffic_listing_stat.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN、MX、BR、AU、AE | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `asinList` | array | 否 | asin列表；示例：["B07Z82895W"]。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS",
  "marketplace": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `marketplace` | string | Amazon 市场站点编码；官方示例值：US。 |
| `asin` | string | Amazon ASIN；官方示例值：B07Z82895W。 |
| `asinList` | string | ASIN 列表。 |
| `calcTime` | integer | 最近计算时间。 |
| `relations` | integer | 全部流量；官方示例值：1848。 |
| `freeRelations` | integer | 免费流量；官方示例值：1414。 |
| `paidRelations` | integer | 付费流量；官方示例值：286。 |
| `items[]` | array | 统计概要。 |
| `items[].relation` | string | 关联类型,忽略大小写；官方示例值：vav。 |
| `items[].count` | integer | 数量；官方示例值：3。 |

## 使用要点

- 必填字段：`marketplace`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-listing-stat" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","marketplace":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

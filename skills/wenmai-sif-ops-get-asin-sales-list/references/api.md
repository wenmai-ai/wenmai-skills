# Wenmai SIF `ops_get_asin_sales_list` API 参考

功能：以列表视图查询一个或多个 ASIN 的销量数据，返回各变体的销量、价格、属性及月度趋势迷你图。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-asin-sales-list`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ops_get_asin_sales_list`
- **脚本入口**：`scripts/ops_get_asin_sales_list.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asins` | array<string> | 是 | 一个或多个待查询的 ASIN 列表。 |
| `country` | string | 否 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |
| `dimension` | string；可选值：“asin”、“color”、“size” | 否 | 分组维度：asin / color / size；枚举含义：asin=按 ASIN 分组，color=按颜色分组，size=按尺码分组。 |
| `sortBy` | string；可选值：“boughtInPastMonth”、“boughtInMonth”、“pasinBoughtInPastMonth” | 否 | 排序字段：boughtInPastMonth / boughtInMonth / pasinBoughtInPastMonth；枚举含义：boughtInPastMonth=按近 30 天销量排序，boughtInMonth=按当月销量排序，pasinBoughtInPastMonth=按父 ASIN 近 30 天销量排序。 |
| `desc` | boolean | 否 | 是否降序排列（默认 true）。 |
| `pageNum` | integer | 否 | 页码（默认 1）。 |
| `pageSize` | integer | 否 | 每页条数（默认 20，最大 100）。 |
| `timePieceType` | string；可选值：“latelyDay”、“week”、“month” | 否 | 时间窗口类型：latelyDay / week / month（注意：week 必须传该周周日日期，如 '2026-03-29'，SIF 数据以周日为每周第一天，当周数据因T+1延迟不可用，如需查当周请使用近7天）；枚举含义：latelyDay=按最近若干天窗口查询，week=按周查询，日期使用目标周周日，month=按月查询，日期使用目标月份首日。 |
| `timePieceValue` | string | 否 | 时间窗口值：latelyDay 填天数如 '30'，week 填周日日期如 '2026-03-29'，month 填月份首日如 '2026-03-01'。 |

## 请求示例

```json
{
  "asins": [
    "B08GHW4TBS"
  ]
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `total` | string | 符合条件的 ASIN 总数 |
| `list[]` | array | 变体销量数据列表 |
| `asin` | string | 变体 ASIN |
| `price` | string | 当前价格 |
| `color` | string | 颜色属性 |
| `size` | string | 尺码属性 |
| `boughtInPastMonth` | string | 近30天销量 |
| `boughtInMonth` | string | 当月销量 |
| `monthlyTrend[]` | array | 月度销量趋势迷你图数据点 |

## 使用要点

- 必填字段：`asins`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-asin-sales-list" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asins":["B08GHW4TBS"]}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

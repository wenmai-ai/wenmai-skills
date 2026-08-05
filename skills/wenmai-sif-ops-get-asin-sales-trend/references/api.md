# Wenmai SIF `ops_get_asin_sales_trend` API 参考

功能：查看 ASIN Listing 下各变体的月度销量历史趋势，用于分析销量走势和季节性规律。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-asin-sales-trend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ops_get_asin_sales_trend`
- **脚本入口**：`scripts/ops_get_asin_sales_trend.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | 主 ASIN，例如 B0CLPGQWNB。 |
| `country` | string | 否 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |
| `asins` | array<string> | 否 | 指定要查询的变体 ASIN 列表（可选）。 |
| `dimension` | string；可选值：“asin”、“color”、“size”、“material_type” | 否 | 分组维度：asin / color / size / material_type；枚举含义：asin=按 ASIN 分组，color=按颜色分组，size=按尺码分组，material_type=按材质类型分组。 |
| `pageNum` | integer | 否 | 页码（默认 1）。 |
| `pageSize` | integer | 否 | 每页条数（默认 20，最大 100）。 |
| `timePieceType` | string；可选值：“latelyDay”、“week”、“month” | 否 | 时间类型：latelyDay / week / month（注意：week 必须传该周周日日期，如 '2026-03-29'，SIF 数据以周日为每周第一天，当周数据因T+1延迟不可用，如需查当周请使用近7天）；枚举含义：latelyDay=按最近若干天窗口查询，week=按周查询，日期使用目标周周日，month=按月查询，日期使用目标月份首日。 |
| `timePieceValue` | string | 否 | 时间值：latelyDay 填天数，week 填周日日期如 '2026-03-29'，month 填月份首日如 '2026-03-01'。 |

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
| `list[]` | array | 按变体或维度分组的销量时间序列 |
| `asin` | string | 变体 ASIN |
| `dimension` | string | 分组维度值（如颜色/尺码） |
| `months[]` | array | 月度销量数据点 |
| `date` | string | 月份（yyyy-MM） |
| `sales` | string | 该月销量 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-asin-sales-trend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

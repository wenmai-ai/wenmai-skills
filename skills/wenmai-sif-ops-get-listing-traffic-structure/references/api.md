# Wenmai SIF `ops_get_listing_traffic_structure` API 参考

功能：查看 Listing 内各变体的流量结构拆解，返回每个变体在自然流量、SP、SB、SBV 渠道中各自的分数与占比。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-listing-traffic-structure`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ops_get_listing_traffic_structure`
- **脚本入口**：`scripts/ops_get_listing_traffic_structure.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | ASIN，例如 B0CLPGQWNB。 |
| `country` | string | 否 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |
| `timePieceType` | string；可选值：“latelyDay”、“week”、“month” | 否 | 时间类型：latelyDay / week / month（注意：week 必须传该周周日日期，如 '2026-03-29'，SIF 数据以周日为每周第一天，当周数据因T+1延迟不可用，如需查当周请使用近7天）；枚举含义：latelyDay=按最近若干天窗口查询，week=按周查询，日期使用目标周周日，month=按月查询，日期使用目标月份首日。 |
| `timePieceValue` | string | 否 | 时间值：latelyDay 填 '7' 或 '30'；week 填周日日期如 '2026-03-29'；month 填月份首日如 '2026-03-01'。 |
| `dimension` | string | 否 | 结果分组维度；官方 inputSchema 未列出允许值。 |
| `sortBy` | string | 否 | 结果排序指标；官方 inputSchema 未列出允许值。 |
| `pageNum` | integer | 否 | 页码。 |
| `pageSize` | integer | 否 | 分页大小。 |

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
| `total` | string | 变体总数 |
| `list[]` | array | 各变体流量结构行数据 |
| `asin` | string | 变体 ASIN |
| `dimensionValue` | string | 分组维度值（如颜色/尺码） |
| `totalScore` | string | 总流量分数 |
| `nfs` | string | 自然流量分数 |
| `ads` | string | 广告总流量分数 |
| `sps` | string | SP 常规广告分数 |
| `recs` | string | SP 推荐广告分数 |
| `sbs` | string | SB 广告分数 |
| `sbvs` | string | SBV 广告分数 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-listing-traffic-structure" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

# Wenmai SIF `ads_get_asin_ad_traffic_trend` API 参考

功能：查询某 ASIN 历史全量的广告流量趋势，按 SP/SB/SBV 三个渠道分别输出曝光量时序。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-asin-ad-traffic-trend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ads_get_asin_ad_traffic_trend`
- **脚本入口**：`scripts/ads_get_asin_ad_traffic_trend.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | 目标 ASIN，例如 B0CLPGQWNB。 |
| `country` | string | 是 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |
| `granularity` | string；可选值：“week”、“month” | 是 | 时间粒度：week / month；枚举含义：week=按周汇总，month=按月汇总。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS",
  "country": "US",
  "granularity": "week"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `asin` | string | 目标 ASIN |
| `country` | string | 站点代码 |
| `metric` | string | 固定为 'impressions'，表示曝光量 |
| `granularity` | string | 实际使用的时间粒度 |
| `trend[]` | array | 按时间粒度分桶的曝光量序列 |
| `date` | string | 分桶起始日期 |
| `SP` | string | SP 渠道曝光量 |
| `SB` | string | SB 渠道曝光量 |
| `SBV` | string | SBV 渠道曝光量 |
| `trend_analysis` | string | 预计算的渠道趋势判断 |
| `SP_trend` | string；可选值：growing、stable、declining、inactive、emerging | SP趋势分类：growing（商品推广流量增长）、stable（商品推广流量稳定）、declining（商品推广流量下降）、inactive（商品推广当前无活跃流量）、emerging（商品推广流量开始出现）。 |
| `SB_trend` | string | SB 渠道趋势，同上 |
| `SBV_trend` | string | SBV 渠道趋势，同上 |
| `overall_trend` | string | 三渠道合计趋势，同上 |
| `dominant_channel` | string；可选值：SP、SB、SBV | 广告类型：SP（商品推广广告）、SB（品牌推广广告）、SBV（品牌推广视频广告）。 |

## 使用要点

- 必填字段：`asin`, `country`, `granularity`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-asin-ad-traffic-trend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","country":"US","granularity":"week"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

# Wenmai SIF `ads_get_campaign_traffic_trend` API 参考

功能：查询单个 campaign 从创建至今的全生命周期流量趋势，并附带广告组创建事件作为结构性上下文。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-campaign-traffic-trend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ads_get_campaign_traffic_trend`
- **脚本入口**：`scripts/ads_get_campaign_traffic_trend.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | ASIN，例如 B0CLPGQWNB。 |
| `campaignId` | string | 是 | Campaign 标识；支持短展示 ID 或加密 ID，例如 HLLE。 |
| `country` | string | 否 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS",
  "campaignId": "SUBD"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `campaignId` | string | campaign 标识符 |
| `campaignDisplayId` | string | campaign 可读展示 ID（fakeCampaignId） |
| `campaignType` | string；可选值：SP、SB、SBV、SB_SBV | 广告类型：SP（商品推广广告）、SB（品牌推广广告）、SBV（品牌推广视频广告）、SB_SBV（品牌推广与品牌推广视频合并口径）。 |
| `trendScope` | string | 固定为 'lifecycle'，表示覆盖 campaign 全生命周期 |
| `trafficTrend[]` | array | 按周时间序列的流量趋势 |
| `date` | string | 该字段在不同返回分支中的含义：周起始日期；或事件日期（周起始日）。 |
| `traffic` | string | 该周曝光得分 |
| `trafficChangeRate` | string | 较上周的曝光变化率 |
| `change_signal` | string；可选值：significant_gain、moderate_gain、stable、moderate_drop、significant_drop | changesignal分类：significant_gain（显著增长）、moderate_gain（中度增长）、stable（基本稳定）、moderate_drop（中度下降）、significant_drop（显著下降）。 |
| `trend_analysis` | string | 预计算趋势判断，避免 LLM 自行分类原始数据 |
| `overall_direction` | string；可选值：growing、mild_growth、stable、mild_decline、declining、insufficient_data | overalldirection分类：growing（持续增长）、mild_growth（温和增长）、stable（基本稳定）、mild_decline（温和下降）、declining（持续下降）、insufficient_data（数据不足，无法判断）。 |
| `recent_change` | string；可选值：sharp_growth、mild_growth、stable、mild_decline、sharp_decline | recentchange分类：sharp_growth（近期快速增长）、mild_growth（近期温和增长）、stable（近期稳定）、mild_decline（近期温和下降）、sharp_decline（近期快速下降）。 |
| `anomaly_weeks[]` | array | 流量较 4 周滚动基线下跌 20% 以上的异常周日期列表 |
| `events[]` | array | 广告组创建事件列表（用于关联流量节点与结构变化） |
| `eventType` | string | 固定为 'adgroup_created' |
| `adGroupId` | string | 被创建的广告组 ID（fakeAdId） |

## 使用要点

- 必填字段：`asin`, `campaignId`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-campaign-traffic-trend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","campaignId":"SUBD"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

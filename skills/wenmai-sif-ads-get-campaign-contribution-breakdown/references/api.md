# Wenmai SIF `ads_get_campaign_contribution_breakdown` API 参考

功能：查询某 campaign 在单个自然周内的贡献明细，支持按 keyword 或 ad_group 维度拆解。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-campaign-contribution-breakdown`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ads_get_campaign_contribution_breakdown`
- **脚本入口**：`scripts/ads_get_campaign_contribution_breakdown.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | ASIN，例如 B0CLPGQWNB。 |
| `campaignId` | string | 是 | Campaign 标识；支持短展示 ID 或加密 ID，例如 SUBD。 |
| `start_date` | string | 是 | 周窗口开始日期，必须传周日（SIF 数据以周日为每周第一天，当周数据因T+1延迟不可用，如需查当周请使用近7天），格式 yyyy-MM-dd，如 '2026-03-29'。 |
| `end_date` | string | 是 | 周窗口结束日期，必须等于 start_date + 6 天。 |
| `breakdown_by` | string；可选值：“keyword”、“ad_group” | 是 | 拆解维度：keyword 或 ad_group；枚举含义：keyword=按关键词拆解贡献，ad_group=按广告组拆解贡献。 |
| `limit` | integer | 否 | 返回数量限制；keyword 模式直接截断，ad_group 模式在全量聚合后截断。 |
| `country` | string | 否 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS",
  "end_date": "2026-04-04",
  "campaignId": "SUBD",
  "start_date": "2026-03-29",
  "breakdown_by": "keyword"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `campaignId` | string | campaign 标识符 |
| `campaignDisplayId` | string | campaign 可读展示 ID |
| `campaignType` | string；可选值：SP、SB、SBV、SB_SBV | 广告类型：SP（商品推广广告）、SB（品牌推广广告）、SBV（品牌推广视频广告）、SB_SBV（品牌推广与品牌推广视频合并口径）。 |
| `timeRange` | string | 实际查询时间范围，含 start_date 和 end_date |
| `breakdown_by` | string | 固定为 'keyword' |
| `items[]` | array | 该字段在不同返回分支中的含义：关键词明细列表；或广告组汇总列表。 |
| `keyword` | string | 关键词原文 |
| `translateKeyword` | string | 关键词翻译 |
| `traffic` | string | 该字段在不同返回分支中的含义：该字段在不同返回分支中的含义：该词在该周的曝光得分；或该广告组对该词的曝光得分；或该广告组本周总曝光得分。 |
| `trafficShare` | string | 该字段在不同返回分支中的含义：该词占该 campaign 本周总曝光的比例；或占该 campaign 本周总曝光的比例。 |
| `trafficChange` | string | 该字段在不同返回分支中的含义：该字段在不同返回分支中的含义：本周曝光得分与上周的变化量；或曝光变化量；或曝光变化量。 |
| `trafficChangeRate` | string | 该字段在不同返回分支中的含义：该字段在不同返回分支中的含义：本周曝光得分与上周的变化率；或曝光变化率；或曝光变化率。 |
| `exposedAdGroups[]` | array | 该词在哪些广告组上展示 |
| `adGroupId` | string | 广告组 ID。 |
| `variantCount` | string | 该广告组展示的变体数量 |
| `variants[]` | array | 变体 ASIN 列表，含 asin 和 img |
| `adGroupContributions[]` | array | 各广告组对该词的贡献明细 |
| `trafficShareWithinKeyword` | string | 该广告组贡献占该词总曝光的比例 |
| `adRankHistory` | string | 广告排名历史，含 dates[] 和 adGroups[]（每项含 adGroupId 和 points[]） |
| `naturalRankHistory` | string | 自然排名历史，含 dates[] 和 variants[]（每项含 asin 和 points[]） |
| `searchTrend` | string | 搜索趋势，含 dates[]/searchVolume[]/searchRank[]/currentSearchVolume/currentSearchRank |
| `keywordCount` | string | 该广告组本周覆盖的关键词数量 |

## 使用要点

- 必填字段：`asin`, `campaignId`, `start_date`, `end_date`, `breakdown_by`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-campaign-contribution-breakdown" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","end_date":"2026-04-04","campaignId":"SUBD","start_date":"2026-03-29","breakdown_by":"keyword"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

# Wenmai SIF `ads_get_asin_ad_historical_feature_profile` API 参考

功能：基于 ASIN 的历史全量广告数据，生成长期广告特征画像，描述投放节奏、渠道组合、集中度和增长轨迹。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-asin-ad-historical-feature-profile`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ads_get_asin_ad_historical_feature_profile`
- **脚本入口**：`scripts/ads_get_asin_ad_historical_feature_profile.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | ASIN，例如 B0CLPGQWNB。 |
| `country` | string | 是 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |
| `granularity` | string；可选值：“week”、“month” | 否 | 时间粒度，仅支持 week/month；默认 week；枚举含义：week=按周汇总，month=按月汇总。 |
| `lang` | string；可选值：“en”、“zh” | 否 | 返回文本字段语言；默认 en；枚举含义：en=返回英文文本，zh=返回中文文本。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS",
  "country": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `投放节奏` | string | 投放节奏。 |
| `campaign 集中度` | string | campaign 集中度。 |
| `渠道组合分布` | string | 渠道组合分布。 |
| `增长轨迹` | string | 增长轨迹。 |
| `asin` | string | 目标 ASIN。 |
| `country` | string | 站点代码。 |
| `features` | object | 特征对象。 |
| `features.dominant_ad_type` | string | 主导广告类型。 |
| `features.contribution_concentration` | string | 贡献集中度。 |
| `features.launch_rhythm` | string | 投放节奏。 |
| `features.structure_complexity` | string | 广告结构复杂度。 |
| `features.growth_mode` | string | 增长模式。 |
| `features.type_diversification` | string | 广告类型多样化程度。 |
| `features.maturity_level` | string | 成熟度等级。 |
| `features.ad_type_evolution_pattern` | string | 广告类型演化模式。 |
| `features.emerging_ad_type` | string | 新兴广告类型。 |
| `evolution_summary` | object | 演化摘要对象。 |
| `evolution_summary.stage_count` | integer | 阶段数量。 |
| `evolution_summary.phases[]` | array | 广告或流量演变过程中的阶段列表。 |
| `evolution_summary.phases[].stage` | string | 阶段。 |
| `evolution_summary.phases[].window` | string | 时间窗口。 |
| `evolution_summary.phases[].dominant_types[]` | array | 主导类型列表。 |
| `evolution_summary.phases[].summary` | string | 摘要。 |
| `signals` | object | 信号指标对象。 |
| `signals.granularity` | string | 时间粒度。 |
| `signals.total_campaign_count` | integer | 广告活动总数。 |
| `signals.sp_campaign_count` | integer | SP 广告活动数量。 |
| `signals.sb_campaign_count` | integer | SB 广告活动数量。 |
| `signals.sbv_campaign_count` | integer | SBV 广告活动数量。 |
| `signals.historical_active_type_count` | integer | 历史活跃广告类型数量。 |
| `signals.historical_top_1_share` | number | 历史 Top1 份额。 |
| `signals.historical_top_3_share` | number | 历史 Top3 份额。 |
| `signals.history_span_days` | integer | 历史跨度天数。 |

## 使用要点

- 必填字段：`asin`, `country`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-asin-ad-historical-feature-profile" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","country":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

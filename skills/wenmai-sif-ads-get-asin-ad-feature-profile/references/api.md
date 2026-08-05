# Wenmai SIF `ads_get_asin_ad_feature_profile` API 参考

功能：ads_get_asin_ad_window_feature_profile 的兼容别名，执行逻辑完全相同。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-asin-ad-feature-profile`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ads_get_asin_ad_feature_profile`
- **脚本入口**：`scripts/ads_get_asin_ad_feature_profile.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | ASIN，例如 B0CLPGQWNB。 |
| `country` | string | 是 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |
| `start_date` | string | 是 | 时间窗口开始日期，格式 yyyy-MM-dd。 |
| `end_date` | string | 是 | 时间窗口结束日期，格式 yyyy-MM-dd。 |
| `ad_type` | string；可选值：SP、SB、SBV、SB_SBV | 否 | 广告类型：SP（商品推广广告）、SB（品牌推广广告）、SBV（品牌推广视频广告）、SB_SBV（品牌推广与品牌推广视频合并口径）。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS",
  "country": "US",
  "end_date": "2026-04-04",
  "start_date": "2026-03-29"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `集中度指标` | string | 集中度指标。 |
| `渠道结构信号` | string | 渠道结构信号。 |
| `投放节奏判断` | string | 投放节奏判断。 |
| `注意` | string | 注意。 |
| `_render_hint` | string | 渲染提示。 |
| `asin` | string | 目标 ASIN。 |
| `country` | string | 站点代码。 |
| `start_date` | string | 开始日期。 |
| `end_date` | string | 结束日期。 |
| `ad_type` | string | 广告类型。 |
| `features` | object | 特征对象。 |
| `features.dominant_ad_type` | string | 主导广告类型。 |
| `features.contribution_concentration` | string | 贡献集中度。 |
| `features.launch_rhythm` | string | 投放节奏。 |
| `features.new_campaign_dependency` | string | 新广告活动依赖度。 |
| `features.structure_complexity` | string | 广告结构复杂度。 |
| `features.traffic_source_stability` | string | 流量来源稳定性。 |
| `signals` | object | 信号指标对象。 |
| `signals.top_1_share` | number | top_1_share数值。 |
| `signals.top_3_share` | number | top_3_share数值。 |
| `signals.total_campaign_count` | integer | 广告活动总数。 |
| `signals.sp_campaign_count` | integer | SP 广告活动数量。 |
| `signals.sb_campaign_count` | integer | SB 广告活动数量。 |
| `signals.sbv_campaign_count` | integer | SBV 广告活动数量。 |
| `signals.window_campaign_count` | integer | 窗口内广告活动数量。 |
| `signals.recent_new_campaign_count` | integer | 近期新广告活动数量。 |

## 使用要点

- 必填字段：`asin`, `country`, `start_date`, `end_date`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-asin-ad-feature-profile" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","country":"US","end_date":"2026-04-04","start_date":"2026-03-29"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

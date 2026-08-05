# Wenmai SIF `ads_get_asin_campaign_contribution_overview` API 参考

功能：基于曝光得分，查询某 ASIN 在指定时间窗口内各 campaign 的贡献总览，按贡献从高到低排序。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-asin-campaign-contribution-overview`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ads_get_asin_campaign_contribution_overview`
- **脚本入口**：`scripts/ads_get_asin_campaign_contribution_overview.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | ASIN，例如 B0CLPGQWNB。 |
| `country` | string | 是 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |
| `start_date` | string | 是 | 时间窗口开始日期，格式 yyyy-MM-dd。 |
| `end_date` | string | 是 | 时间窗口结束日期，格式 yyyy-MM-dd。 |
| `ad_type` | string；可选值：SP、SB、SBV、SB_SBV | 否 | 广告类型：SP（商品推广广告）、SB（品牌推广广告）、SBV（品牌推广视频广告）、SB_SBV（品牌推广与品牌推广视频合并口径）。 |
| `limit` | integer | 否 | 返回条数，范围 1~200，默认 20。 |

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
| `asin` | string | 目标 ASIN |
| `country` | string | 站点代码 |
| `metric` | string | 固定为 'exposure_score'，表示基于曝光得分排序 |
| `start_date` | string | 查询起始日 |
| `end_date` | string | 查询截止日 |
| `ad_type` | string；可选值：SP、SB、SBV、SB_SBV | 该字段在不同返回分支中的含义：广告类型过滤值（仅在传入时返回）；或广告类型：SP（商品推广广告）、SB（品牌推广广告）、SBV（品牌推广视频广告）、SB_SBV（品牌推广与品牌推广视频合并口径）。 |
| `campaigns[]` | array | campaign 贡献列表，按 contribution_score 从高到低排序 |
| `campaign_id` | string | campaign 加密 ID |
| `campaign_display_id` | string | campaign 可读展示 ID（fakeCampaignId） |
| `campaign_name` | string | campaign 名称 |
| `created_date` | string | campaign 创建日期 |
| `contribution_score` | string | 曝光得分，数值越高表示该周期内曝光越多 |
| `share` | string | 该 campaign 占窗口内总曝光的比例（0~1） |
| `contribution_tier` | string | 贡献等级，dominant（>=30%）/major（>=10%）/supporting（>=3%）/minor（<3%） |
| `rank` | string | 贡献排名，从 1 开始 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-asin-campaign-contribution-overview" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","country":"US","end_date":"2026-04-04","start_date":"2026-03-29"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

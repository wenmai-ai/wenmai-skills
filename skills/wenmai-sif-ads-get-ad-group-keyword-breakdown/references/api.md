# Wenmai SIF `ads_get_ad_group_keyword_breakdown` API 参考

功能：查询单个广告组在指定周的关键词明细，包含每个关键词的流量占比以及该关键词在哪些 ASIN 上展示。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-ad-group-keyword-breakdown`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ads_get_ad_group_keyword_breakdown`
- **脚本入口**：`scripts/ads_get_ad_group_keyword_breakdown.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | ASIN，例如 B0CLPGQWNB。 |
| `campaignId` | string | 是 | 目标 campaign ID，支持 encryptCampaignId 或 fakeCampaignId。 |
| `adGroupId` | string | 是 | 目标广告组 ID，支持 fakeAdId 或 encryptAdId。 |
| `date` | string | 是 | 目标周的起始日期，格式 yyyy-MM-dd。 |
| `country` | string | 否 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS",
  "date": "2026-03-29",
  "adGroupId": "CCL4",
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
| `adGroupId` | string | 广告组 ID |
| `date` | string | 目标周起始日期 |
| `displayAsins[]` | array | 该字段在不同返回分支中的含义：该广告组在该周展示的全部去重 ASIN 列表；或该关键词在该广告组中展示的 ASIN 列表。 |
| `keywords[]` | array | 该广告组的关键词明细列表 |
| `keyword` | string | 关键词原文 |
| `translateKeyword` | string | 关键词翻译 |
| `trafficShareWithinAdGroup` | string | 该词在广告组内的流量占比（0~1） |

## 使用要点

- 必填字段：`asin`, `campaignId`, `adGroupId`, `date`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ads-get-ad-group-keyword-breakdown" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","date":"2026-03-29","adGroupId":"CCL4","campaignId":"SUBD"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

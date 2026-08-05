# Wenmai SIF `ops_get_asin_traffic_trend_detail` API 参考

功能：查看 ASIN 在指定时间窗口内的关键词级流量明细，按关键词分页返回各渠道排名与分数拆解。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-asin-traffic-trend-detail`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`ops_get_asin_traffic_trend_detail`
- **脚本入口**：`scripts/ops_get_asin_traffic_trend_detail.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `asin` | string | 是 | ASIN，例如 B01NBNDC1T。 |
| `country` | string | 否 | 站点代码（country字段），如 US(美国) / UK(英国) / DE(德国) / CA(加拿大) / JP(日本) / FR(法国) / ES(西班牙) / IT(意大利) / MX(墨西哥) / AU(澳大利亚) / AE(阿联酋) / BR(巴西) / SA(沙特阿拉伯)（默认 US）。 |
| `endDay` | string | 是 | 指定周期开始时间的第一天，day：yyyy-MM-dd，week：yyyy-MM-dd（仅支持周日，当周数据有T+1延迟），month：yyyy-MM。 |
| `granularity` | string；可选值：“day”、“week”、“month” | 是 | 时间粒度（下钻建议使用 day）；枚举含义：day=按日汇总，week=按周汇总，month=按月汇总。 |
| `keywordType` | string；可选值：“all”、“nf”、“ad”、“sp”、“recSp”、“sb”、“sbv” | 否 | 流量类型；枚举含义：all=全部流量，nf=自然流量，ad=全部广告流量，sp=商品推广常规广告流量，recSp=商品推广推荐广告流量，sb=品牌推广广告流量，sbv=品牌推广视频广告流量。 |
| `desc` | boolean | 是 | 是否倒序。 |
| `pageNum` | integer | 是 | 页码，>=1。 |
| `pageSize` | integer | 是 | 分页大小，建议 <=200。 |
| `changeType` | string | 否 | 变化类型筛选值；官方 inputSchema 未列出允许值。 |
| `filter` | string | 否 | 附加筛选条件；官方 inputSchema 未说明表达式格式。 |
| `interval` | integer | 否 | 周期间隔数值；官方 inputSchema 未说明单位。 |
| `lastMonths` | integer | 否 | 最近月数窗口。 |
| `searchKeyword` | string | 否 | 关键词过滤。 |
| `sortBy` | string | 否 | 排序字段，如 searchesRank。 |
| `type` | string | 否 | 业务类型筛选值；官方 inputSchema 未列出允许值。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS",
  "desc": false,
  "endDay": "2026-03-29",
  "pageNum": 1,
  "pageSize": 1,
  "granularity": "day"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `total` | string | 符合条件的关键词总条数 |
| `list[]` | array | 分页的关键词行数据 |
| `keyword` | string | 关键词文本 |
| `totalScore` | string | 该关键词总流量分数 |
| `naturalScore` | string | 自然流量分数 |
| `adScore` | string | 广告流量分数 |
| `naturalRank` | string | 自然搜索排名 |
| `spRank` | string | SP 广告排名 |
| `sbRank` | string | SB 广告排名 |

## 使用要点

- 必填字段：`asin`, `endDay`, `granularity`, `desc`, `pageNum`, `pageSize`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/ops-get-asin-traffic-trend-detail" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","desc":false,"endDay":"2026-03-29","pageNum":1,"pageSize":1,"granularity":"day"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。

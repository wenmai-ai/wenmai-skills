# Wenmai SellerSprite `aba_research_weekly` API 参考

用于在指定 Amazon 站点和时间点（按周），。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/aba-research-weekly`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`aba_research_weekly`
- **脚本入口**：`scripts/aba_research_weekly.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 业务请求对象。 |
| `request.marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `request.date` | string | 否 | 为空时，查最新周；示例：20230610，限定为周六的日期）。 |
| `request.departments` | array | 否 | 类目列表；示例：["automotive","baby-products"]。 |
| `request.excludeKeywords` | string | 否 | 排除关键词；示例：portable。 |
| `request.includeKeywords` | string | 否 | 包含关键词。 |
| `request.exactFlag` | boolean | 否 | 是否精确匹配。 |
| `request.rankGrowthValue` | integer | 否 | 搜索增长量。 |
| `request.rankGrowthRate` | number | 否 | 搜索增长率。 |
| `request.minRankGrowthRate` | number | 否 | 最小排名增长率。 |
| `request.maxRankGrowthRate` | number | 否 | 最大排名增长率。 |
| `request.minSearchRank` | integer | 否 | 最小排名。 |
| `request.maxSearchRank` | integer | 否 | 最大排名。 |
| `request.minSearches` | integer | 否 | 最小搜索量。 |
| `request.maxSearches` | integer | 否 | 最大搜索量。 |
| `request.minMonopolyClickRate` | number | 否 | 最小点击集中度。 |
| `request.maxMonopolyClickRate` | number | 否 | 最大点击集中度。 |
| `request.minConversionRate` | number | 否 | 最小转化占比。 |
| `request.maxConversionRate` | number | 否 | 最大转化占比。 |
| `request.minWordCount` | integer | 否 | 最小单词数。 |
| `request.maxWordCount` | integer | 否 | 最大单词数。 |
| `request.minSPR` | integer | 否 | 最小SPR |
| `request.maxSPR` | integer | 否 | 最大SPR |
| `request.minTitleDensity` | integer | 否 | 最小标题密度。 |
| `request.maxTitleDensity` | integer | 否 | 最大标题密度。 |
| `request.minClicks` | integer | 否 | 最小点击量；示例：1。 |
| `request.maxClicks` | integer | 否 | 最大点击量；示例：10000。 |
| `request.minImpressions` | integer | 否 | 最小展示量；示例：10000。 |
| `request.maxImpressions` | integer | 否 | 最大展示量；示例：20000。 |
| `request.searchModel` | integer；可选值：1、2、3、4、5、6 | 否 | 搜索模式：1：热门市场2：异动市场3：持续增长市场4：快速飙升市场5：潜力市场6：长尾市场；示例：1。 |
| `request.page` | integer | 否 | 页码，从 1 开始；默认：1。 |
| `request.size` | integer | 否 | 每页条数，最大40；默认：40。 |
| `request.order` | object | 否 | 排序配置对象。 |
| `request.order.field` | string | 否 | 请求指定的排序字段；允许值由具体接口的供应商契约决定。 |
| `request.order.desc` | boolean | 否 | true为降序 false为升序；默认降序。 |

## 请求示例

```json
{
  "request": {
    "marketplace": "US"
  }
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `guestId` | string | 访客 ID。 |
| `pages` | integer | 分页结果的总页数。 |
| `page` | integer | 当前页码。 |
| `size` | integer | 本次分页结果每页返回的记录数。 |
| `total` | integer | 总数量。 |
| `took` | integer | 请求耗时。 |
| `url` | string | 用于打开当前页面、媒体或资源的链接。 |
| `order` | object | 排序对象。 |
| `order.field` | string | 分页结果实际采用的排序字段。 |
| `order.desc` | boolean | 是否降序。 |
| `items[]` | array | 列表数据。 |
| `items[].marketplace` | string | Amazon 市场站点编码；官方示例值：US。 |
| `items[].date` | string | 查询日期；官方示例值：20230610，限定为周六的日期。 |
| `items[].keyword` | string | 关键词文本；官方示例值：portable charger。 |
| `items[].keywordCn` | string | 关键词中文翻译。 |
| `items[].keywordJp` | string | 关键词日文。 |
| `items[].departments[]` | array | Amazon 类目；官方示例值：["Cell Phones & Accessories"]。 |
| `items[].searchRank` | integer | 搜索排名；官方示例值：62。 |
| `items[].searchRankCv` | integer | 排名增长量；官方示例值：19。 |
| `items[].searchRankCr` | number | 排名增长率；官方示例值：0.2346。 |
| `items[].searches` | integer | 搜索量；官方示例值：46147979。 |
| `items[].purchaseRate` | number | 购买率；官方示例值：0.0054。 |
| `items[].purchases` | integer | 购买量；官方示例值：2492。 |
| `items[].clicks` | integer | 点击量；官方示例值：1380。 |
| `items[].impressions` | integer | 展示量；官方示例值：73560。 |
| `items[].searchRankGrowthValue` | string | 搜索排名。 |
| `items[].searchRankGrowthRate` | number | 搜索排名率。 |
| `items[].cvsShareRate` | number | 前三转化总比；官方示例值：43.5。 |
| `items[].clickShareRate` | number | Top3 点击占比；官方示例值：54.2。 |
| `items[].titleDensityExact` | integer | 精确标题密度：Amazon 首页商品标题中包含该关键词的商品数量。 |
| `items[].cprExact` | integer | 精确 CPR（8天内确保关键词上首页的销量数）。 |
| `items[].w1SearchRank` | integer | 上周的排名。 |
| `items[].w1RankGrowthValue` | integer | 上周的排名变化值。 |
| `items[].w1RankGrowthRate` | number | 上周的排名变化率。 |
| `items[].w4SearchRank` | integer | 4周前的排名。 |
| `items[].w4RankGrowthValue` | integer | 4周前的排名变化值。 |
| `items[].w4RankGrowthRate` | number | 4周前的排名变化率。 |
| `items[].w12SearchRank` | integer | 12周前的排名。 |
| `items[].w12RankGrowthValue` | integer | 12周前的排名变化值。 |
| `items[].w12RankGrowthRate` | number | 12周前的排名变化率。 |
| `items[].top3Brands[]` | array | 点击量 Top3 品牌列表。 |
| `items[].bid` | number | ppc竞价。 |
| `items[].bidMax` | number | 最大ppc竞价。 |
| `items[].bidMin` | number | 最小ppc竞价。 |
| `items[].top3AsinDtoList[]` | array | 点击量 Top3 ASIN 明细列表。 |
| `items[].top3AsinDtoList[].asin` | string | Amazon ASIN。 |
| `items[].top3AsinDtoList[].imageUrl` | string | 图片URL。 |
| `items[].top3AsinDtoList[].clickRate` | number | 该 Top3 ASIN 的点击集中度。 |
| `items[].top3AsinDtoList[].conversionRate` | number | 该 Top3 ASIN 的转化率。 |
| `terminal` | string | 终端类型。 |
| `hasNextPage` | integer | 是否还有下一页。 |
| `guestVisited` | boolean | 访客是否访问过。 |

## 使用要点

- 必填字段：`request`, `request.marketplace`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/aba-research-weekly" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request":{"marketplace":"US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
